#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "src" / "data" / "leetcode-stats.json"
GRAPHQL_URL = "https://leetcode.cn/graphql/"

QUERY = """
query userStats($userSlug: String!) {
  userProfilePublicProfile(userSlug: $userSlug) {
    siteRanking
    profile {
      userSlug
      realName
      reputation
    }
  }
  userProfileUserQuestionProgress(userSlug: $userSlug) {
    numAcceptedQuestions {
      difficulty
      count
    }
    numFailedQuestions {
      difficulty
      count
    }
    numUntouchedQuestions {
      difficulty
      count
    }
  }
}
""".strip()


def post_graphql(payload: dict[str, object]) -> dict[str, object]:
    request = Request(
        GRAPHQL_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "SavvyM-Blog-LeetCode-Updater/1.0",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=20) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return json.loads(response.read().decode(charset))
    except HTTPError as exc:
        raise SystemExit(f"LeetCode GraphQL request failed with HTTP {exc.code}") from exc
    except URLError as exc:
        raise SystemExit(f"LeetCode GraphQL request failed: {exc.reason}") from exc


def to_difficulty_map(entries: list[dict[str, object]]) -> dict[str, int]:
    return {
        str(item["difficulty"]).lower(): int(item["count"])
        for item in entries
    }


def build_stats(response: dict[str, object]) -> dict[str, object]:
    errors = response.get("errors")
    if errors:
        raise SystemExit(f"LeetCode GraphQL returned errors: {json.dumps(errors, ensure_ascii=False)}")

    data = response.get("data")
    if not isinstance(data, dict):
        raise SystemExit("LeetCode GraphQL response did not contain data.")

    profile_payload = data.get("userProfilePublicProfile")
    progress_payload = data.get("userProfileUserQuestionProgress")

    if not isinstance(profile_payload, dict) or not isinstance(progress_payload, dict):
        raise SystemExit("LeetCode GraphQL response shape changed unexpectedly.")

    profile = profile_payload.get("profile")
    if not isinstance(profile, dict):
        raise SystemExit("LeetCode GraphQL response did not contain profile data.")

    accepted = to_difficulty_map(list(progress_payload.get("numAcceptedQuestions", [])))
    failed = to_difficulty_map(list(progress_payload.get("numFailedQuestions", [])))
    untouched = to_difficulty_map(list(progress_payload.get("numUntouchedQuestions", [])))

    stats: dict[str, object] = {
        "userSlug": str(profile.get("userSlug", "")),
        "realName": str(profile.get("realName", "")),
        "reputation": int(profile.get("reputation", 0) or 0),
        "siteRanking": int(profile_payload.get("siteRanking", 0) or 0),
        "updatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }

    total_solved = 0
    for difficulty in ("easy", "medium", "hard"):
        solved = accepted.get(difficulty, 0)
        total = solved + failed.get(difficulty, 0) + untouched.get(difficulty, 0)
        stats[difficulty] = {
            "solved": solved,
            "total": total,
        }
        total_solved += solved

    stats["totalSolved"] = total_solved
    return stats


def write_output(stats: dict[str, object]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(stats, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def load_existing() -> dict[str, object] | None:
    if not OUTPUT_PATH.exists():
        return None

    return json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))


def strip_timestamp(stats: dict[str, object] | None) -> dict[str, object] | None:
    if stats is None:
        return None

    return {key: value for key, value in stats.items() if key != "updatedAt"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update local LeetCode stats JSON.")
    parser.add_argument("--user-slug", default="savvym", help="LeetCode CN profile slug.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    response = post_graphql({
        "query": QUERY,
        "variables": {
            "userSlug": args.user_slug,
        },
    })
    stats = build_stats(response)
    existing = load_existing()

    if strip_timestamp(existing) == strip_timestamp(stats):
        print(f"No LeetCode stats change for {args.user_slug}.")
        return 0

    write_output(stats)
    print(f"Wrote {OUTPUT_PATH.relative_to(PROJECT_ROOT)} for {args.user_slug}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
