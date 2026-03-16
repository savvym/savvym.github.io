#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from collections import OrderedDict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OLD_ROOT = Path("/tmp/savvym-old-blog-20260316")
OLD_POSTS = OLD_ROOT / "content" / "posts"
NEW_POSTS = PROJECT_ROOT / "src" / "content" / "blog"
NB_IMAGES_SRC = OLD_ROOT / "static" / "nb_images"
NB_IMAGES_DEST = PROJECT_ROOT / "public" / "nb_images"
LLMS_FILE = PROJECT_ROOT / "public" / "llms.txt"
SKIP_POSTS = {
    Path("Paper/car_detection_with_yolo.md"),
}


def split_frontmatter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        return {}, text

    try:
        _, frontmatter, body = text.split("---\n", 2)
    except ValueError:
        return {}, text

    return parse_frontmatter(frontmatter), body.lstrip()


def parse_frontmatter(frontmatter: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current_key: str | None = None

    for raw_line in frontmatter.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue

        if line.lstrip().startswith("- ") and current_key:
            value = strip_quotes(line.split("- ", 1)[1].strip())
            existing = data.setdefault(current_key, [])
            if isinstance(existing, list):
                existing.append(value)
            continue

        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            continue

        key, value = match.groups()
        current_key = key
        if not value:
            data[key] = []
            continue

        data[key] = strip_quotes(value.strip())

    return data


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def slugify_piece(value: str) -> str:
    slug = value.lower()
    slug = slug.replace("c++", "c-plus-plus")
    slug = slug.replace("+", " plus ")
    slug = slug.replace("#", " sharp ")
    slug = slug.replace("&", " and ")
    slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "post"


def build_slug(path: Path) -> str:
    parts = [slugify_piece(part) for part in path.with_suffix("").parts]
    return "-".join(part for part in parts if part)


def plain_text(value: str) -> str:
    text = re.sub(r"(?is)<script.*?</script>", " ", value)
    text = re.sub(r"(?is)<style.*?</style>", " ", text)
    text = re.sub(r"\$\$([\s\S]*?)\$\$", r" \1 ", text)
    text = re.sub(r"\$([^\n$]+)\$", r" \1 ", text)
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def markdown_text(value: str) -> str:
    return value.replace("[", r"\[").replace("]", r"\]")


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def normalize_code_fences(content: str) -> str:
    aliases = {
        "C": "c",
        "CPP": "cpp",
        "C++": "cpp",
        "golang": "go",
        "shell": "bash",
    }

    def replace(match: re.Match[str]) -> str:
        language = match.group(1)
        mapped = aliases.get(language, aliases.get(language.lower(), language))
        return f"```{mapped}\n"

    normalized = re.sub(r"```[ \t]*([A-Za-z0-9+#-]+)[ \t]*\n", replace, content)
    if normalized.count("```") % 2 == 1:
        normalized = f"{normalized.rstrip()}\n```\n"
    return normalized


def extract_html_content(body: str) -> str:
    if "<!DOCTYPE html" not in body and "<html" not in body.lower():
        return body.strip()

    styles = re.findall(r"(?is)<style.*?</style>", body)
    body_match = re.search(r"(?is)<body[^>]*>(.*)</body>", body)
    inner = body_match.group(1).strip() if body_match else body.strip()
    inner = re.sub(r"(?is)<script.*?</script>", "", inner)

    sections = []
    if styles:
        sections.append("\n\n".join(style.strip() for style in styles))
    sections.append(inner)
    return "\n\n".join(section for section in sections if section).strip()


def unique(values: list[str]) -> list[str]:
    ordered: OrderedDict[str, str] = OrderedDict()
    for value in values:
        cleaned = value.strip()
        if cleaned:
            ordered.setdefault(slugify_piece(cleaned), cleaned)
    return list(ordered.values())


def collect_posts() -> list[dict[str, object]]:
    posts = []

    for source in sorted(OLD_POSTS.rglob("*.md")):
        if source.name == "_index.md" or source.name.startswith("."):
            continue

        relative = source.relative_to(OLD_POSTS)
        if relative in SKIP_POSTS:
            continue
        frontmatter, body = split_frontmatter(source.read_text(encoding="utf-8"))

        title = str(frontmatter.get("title", source.stem))
        date = str(frontmatter.get("date", "1970-01-01"))
        summary = str(frontmatter.get("summary", "")).strip()

        tags: list[str] = []
        for key in ("tags", "categories"):
            values = frontmatter.get(key, [])
            if isinstance(values, list):
                tags.extend(str(item) for item in values)

        if not tags and relative.parts[:-1]:
            tags.extend(relative.parts[:-1])

        tags = unique(tags)
        content = normalize_code_fences(extract_html_content(body))
        preview = plain_text(content)
        description = summary or (
            title if not preview or preview.startswith("$") else preview[:160].strip()
        )

        posts.append(
            {
                "title": title,
                "date": date,
                "description": description,
                "tags": tags,
                "slug": build_slug(relative),
                "content": content,
            }
        )

    posts.sort(key=lambda post: str(post["date"]), reverse=True)
    return posts


def write_posts(posts: list[dict[str, object]]) -> None:
    NEW_POSTS.mkdir(parents=True, exist_ok=True)

    for existing in NEW_POSTS.glob("*.md"):
        existing.unlink()

    for post in posts:
        lines = [
            "---",
            f"title: {yaml_quote(str(post['title']))}",
            f"description: {yaml_quote(str(post['description']))}",
            f'pubDate: "{post["date"]}"',
        ]

        tags = post["tags"]
        if tags:
            lines.append("tags:")
            for tag in tags:
                lines.append(f'  - "{tag}"')
        else:
            lines.append("tags: []")

        lines.extend(["---", "", str(post["content"]).rstrip(), ""])
        destination = NEW_POSTS / f'{post["slug"]}.md'
        destination.write_text("\n".join(lines), encoding="utf-8")


def sync_assets(posts: list[dict[str, object]]) -> None:
    if NB_IMAGES_DEST.exists():
        shutil.rmtree(NB_IMAGES_DEST)
    needs_nb_images = any("/nb_images/" in str(post["content"]) for post in posts)
    if NB_IMAGES_SRC.exists() and needs_nb_images:
        shutil.copytree(NB_IMAGES_SRC, NB_IMAGES_DEST)


def write_llms(posts: list[dict[str, object]]) -> None:
    lines = [
        "# SavvyM's Blog",
        "",
        "> Personal notes by SavvyM on algorithms, programming languages, Linux, and reading papers.",
        "",
        "## Pages",
        "",
        "- [Home](/)",
        "- [About](/about/)",
        "- [Blog](/blog/)",
        "",
        "## Posts",
        "",
    ]

    for post in posts:
        title = markdown_text(str(post["title"]))
        description = markdown_text(str(post["description"]))
        lines.append(f"- {title}: /blog/{post['slug']}/")
        lines.append(f"  {description}")

    LLMS_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    posts = collect_posts()
    write_posts(posts)
    sync_assets(posts)
    write_llms(posts)
    print(f"Migrated {len(posts)} posts.")


if __name__ == "__main__":
    main()
