from __future__ import annotations

import re
from html import unescape
from pathlib import Path
from urllib.parse import urljoin, urlparse

import yaml
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter


ROOT = Path(__file__).resolve().parents[1]
SOURCE_BLOG_DIR = ROOT / "blog"
OUTPUT_DIR = ROOT / "src" / "content" / "blog"
SITE_ORIGIN = "https://michaellivs.com"


class AstroMarkdownConverter(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags):
        language = ""
        code_el = el.find("code")
        if el.get("data-language"):
            language = el["data-language"]
        elif code_el and code_el.get("data-language"):
            language = code_el["data-language"]

        code = el.get_text()
        code = code.rstrip("\n")
        return f"\n```{language}\n{code}\n```\n\n"

    def convert_code(self, el, text, parent_tags):
        if el.parent and el.parent.name == "pre":
            return text
        inner = text.strip().replace("`", "\\`")
        return f"`{inner}`"


def normalize_link(current_rel_path: str, raw_url: str) -> str:
    if not raw_url:
        return raw_url

    parsed = urlparse(raw_url)
    if parsed.scheme in {"mailto", "tel"}:
        return raw_url

    if parsed.scheme in {"http", "https"} and parsed.netloc not in {
        "michaellivs.com",
        "www.michaellivs.com",
    }:
        return raw_url

    current_url = f"{SITE_ORIGIN}/{current_rel_path}"
    resolved = urljoin(current_url, raw_url)
    resolved_parts = urlparse(resolved)
    path = resolved_parts.path

    if path == "/index.html":
        normalized = "/"
    elif path.endswith("/index.html"):
        normalized = path[: -len("index.html")]
    elif path.endswith(".html"):
        normalized = f"{path[:-5]}/"
    else:
        normalized = path

    if resolved_parts.fragment:
        return f"{normalized}#{resolved_parts.fragment}"
    return normalized


def clean_markup(content: BeautifulSoup, current_rel_path: str) -> str:
    for element in content.find_all(True):
        for attr in list(element.attrs):
            if attr in {"href", "src", "alt", "title", "data-language"}:
                continue
            del element.attrs[attr]

    for link in content.find_all("a", href=True):
        link["href"] = normalize_link(current_rel_path, link["href"])

    for image in content.find_all("img", src=True):
        image["src"] = normalize_link(current_rel_path, image["src"])

    markdown = AstroMarkdownConverter(
        heading_style="ATX",
        bullets="-",
        wrap=False,
        strip=["span"],
    ).convert_soup(content)
    markdown = markdown.replace("\r\n", "\n")
    markdown = re.sub(r"\n\[(.*?)\]\((.*?)\)\n", r"\n\n[\1](\2)\n\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"
    return unescape(markdown)


def yaml_frontmatter(data: dict) -> str:
    dumped = yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).strip()
    return f"---\n{dumped}\n---\n\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for target in OUTPUT_DIR.glob("*.md"):
        target.unlink()

    for article_path in sorted(SOURCE_BLOG_DIR.glob("*/index.html")):
        current_rel_path = article_path.relative_to(ROOT).as_posix()
        slug = article_path.parent.name
        soup = BeautifulSoup(article_path.read_text(), "html.parser")
        article = soup.select_one("article")
        if article is None:
            continue

        title = article.select_one("h1").get_text(" ", strip=True)
        description = (
            soup.select_one('meta[name="description"]')["content"].strip()
            if soup.select_one('meta[name="description"]')
            else ""
        )
        published = article.select_one("time")["datetime"][:10]
        tags = [tag.get_text(" ", strip=True) for tag in article.select(".meta-tags a")]

        content = article.select_one(".content")
        if content is None:
            continue

        markdown = clean_markup(content, current_rel_path)
        frontmatter = yaml_frontmatter(
            {
                "title": title,
                "description": description,
                "pubDate": published,
                "tags": tags,
            }
        )
        target_path = OUTPUT_DIR / f"{slug}.md"
        target_path.write_text(frontmatter + markdown)


if __name__ == "__main__":
    main()
