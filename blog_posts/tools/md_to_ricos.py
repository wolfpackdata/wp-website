#!/usr/bin/env python3
"""Convert a blog post's markdown into the Wix Blog draft-post payload.

Wix does not accept markdown. The Blog Draft Posts API takes ``richContent`` --
Ricos, Wix's rich-content node tree. This module is the deterministic transform
between the two, so a published post is a reproducible function of ``post.md``
and re-pushing an edited post is safe.

Stdlib only, matching the repo's no-build-step convention.

Usage
-----
List the local images a post references, so they can be uploaded first::

    python md_to_ricos.py ../2026-08-04-my-post --list-images

Build the payload, resolving those images to Wix media IDs::

    python md_to_ricos.py ../2026-08-04-my-post --media-map media.json --out payload.json

The push itself is a separate step -- see ``blog_posts/README.md``. This script
never talks to Wix; it only reads files and writes JSON.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# Wix rejects a draft post over 400KB.
MAX_POST_BYTES = 400 * 1024


class PostError(Exception):
    """A post that cannot be converted. Message is shown to the author."""


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------

# Only the subset a blog post needs: scalars, inline lists, and block lists.
# A real YAML parser would be a dependency; this stays honest about its limits
# and raises rather than silently mis-parsing anything it does not understand.
_SCALAR = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")
_ITEM = re.compile(r"^\s*-\s+(.*)$")

KNOWN_KEYS = {"title", "slug", "excerpt", "cover", "cover_alt", "date", "tags", "featured"}
REQUIRED_KEYS = {"title"}


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Split ``---`` delimited front matter from the markdown body."""
    if not text.startswith("---"):
        raise PostError(
            "post.md must open with a '---' front matter block. "
            "See blog_posts/_template/post.md."
        )

    lines = text.split("\n")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise PostError("Front matter block is never closed with '---'.") from None

    meta: dict = {}
    pending_list_key: str | None = None

    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        item = _ITEM.match(raw)
        if item and pending_list_key:
            meta[pending_list_key].append(_unquote(item.group(1)))
            continue

        scalar = _SCALAR.match(raw)
        if not scalar:
            raise PostError(f"Cannot parse front matter line: {raw!r}")

        key, value = scalar.group(1), scalar.group(2).strip()
        if not value:
            meta[key] = []
            pending_list_key = key
            continue

        pending_list_key = None
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            meta[key] = [_unquote(p) for p in inner.split(",") if p.strip()] if inner else []
        elif value.lower() in ("true", "false"):
            meta[key] = value.lower() == "true"
        else:
            meta[key] = _unquote(value)

    unknown = set(meta) - KNOWN_KEYS
    if unknown:
        raise PostError(
            f"Unknown front matter key(s): {', '.join(sorted(unknown))}. "
            f"Known keys: {', '.join(sorted(KNOWN_KEYS))}."
        )
    missing = REQUIRED_KEYS - set(meta)
    if missing:
        raise PostError(f"Front matter is missing required key(s): {', '.join(sorted(missing))}.")
    if not str(meta.get("title", "")).strip():
        raise PostError("Front matter 'title' cannot be empty.")

    return meta, "\n".join(lines[end + 1:])


def slugify(title: str) -> str:
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_title.lower()).strip("-")
    return slug or "post"


# --------------------------------------------------------------------------
# Inline markdown -> Ricos TEXT nodes
# --------------------------------------------------------------------------

_node_counter = 0


def _next_id(prefix: str) -> str:
    """Stable, sequential node IDs so the same markdown yields the same JSON."""
    global _node_counter
    _node_counter += 1
    return f"{prefix}{_node_counter}"


def reset_ids() -> None:
    global _node_counter
    _node_counter = 0


def _decorations(active: dict) -> list:
    """Render the active decoration set into Ricos decoration objects."""
    out = []
    if active.get("bold"):
        out.append({"type": "BOLD", "fontWeightValue": 700})
    if active.get("italic"):
        out.append({"type": "ITALIC", "italicData": True})
    if active.get("strike"):
        out.append({"type": "STRIKETHROUGH", "strikethroughData": True})
    # Inline code carries no decoration. Ricos has no inline-code type, and Wix
    # strips FONT_FAMILY on save -- verified against the live API with both
    # "monospace" and "Courier New". Backticks are still consumed and their
    # contents kept literal, so the text is right even though the styling is
    # not available. See README "Known fidelity limits".
    if active.get("link"):
        out.append({
            "type": "LINK",
            "linkData": {"link": {"url": active["link"], "target": "BLANK"}},
        })
    return out


def parse_inline(text: str) -> list:
    """Tokenize inline markdown into a list of Ricos TEXT nodes.

    Handles **bold**, *italic*/_italic_, ~~strike~~, `code`, [text](url), and
    backslash escapes. Decorations nest; each run of text carries the full set
    of decorations active at that point.
    """
    nodes: list = []
    active: dict = {}
    buf: list[str] = []

    def flush() -> None:
        if not buf:
            return
        nodes.append({
            "type": "TEXT",
            "id": "",
            "nodes": [],
            "textData": {"text": "".join(buf), "decorations": _decorations(active)},
        })
        buf.clear()

    i, n = 0, len(text)
    while i < n:
        ch = text[i]

        if ch == "\\" and i + 1 < n and text[i + 1] in "\\`*_~[]()#+-.!":
            buf.append(text[i + 1])
            i += 2
            continue

        # Inline code wins over every other marker, as in CommonMark.
        if ch == "`":
            close = text.find("`", i + 1)
            if close != -1:
                flush()
                active["code"] = True
                buf.append(text[i + 1:close])
                flush()
                active.pop("code", None)
                i = close + 1
                continue

        if text.startswith("**", i):
            flush()
            active["bold"] = not active.get("bold")
            i += 2
            continue

        if text.startswith("~~", i):
            flush()
            active["strike"] = not active.get("strike")
            i += 2
            continue

        if ch in "*_" and not text.startswith("**", i):
            # An underscore inside a word (snake_case) is literal, not emphasis.
            if ch == "_" and i > 0 and (text[i - 1].isalnum() or text[i - 1] == "_"):
                if i + 1 < n and (text[i + 1].isalnum() or text[i + 1] == "_"):
                    buf.append(ch)
                    i += 1
                    continue
            flush()
            active["italic"] = not active.get("italic")
            i += 1
            continue

        if ch == "[":
            match = _link_at(text, i)
            if match:
                label, url, end = match
                flush()
                active["link"] = url
                for sub in parse_inline(label):
                    sub["textData"]["decorations"] = _merge_link(
                        sub["textData"]["decorations"], url
                    )
                    nodes.append(sub)
                active.pop("link", None)
                i = end
                continue

        buf.append(ch)
        i += 1

    flush()
    return nodes


def _merge_link(decorations: list, url: str) -> list:
    if any(d["type"] == "LINK" for d in decorations):
        return decorations
    return decorations + [
        {"type": "LINK", "linkData": {"link": {"url": url, "target": "BLANK"}}}
    ]


def _link_at(text: str, start: int):
    """Match ``[label](url)`` at ``start``, respecting nested brackets."""
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "[" and (i == start or text[i - 1] != "\\"):
            depth += 1
        elif text[i] == "]" and text[i - 1] != "\\":
            depth -= 1
            if depth == 0:
                if i + 1 < len(text) and text[i + 1] == "(":
                    close = text.find(")", i + 2)
                    if close != -1:
                        return text[start + 1:i], text[i + 2:close].strip(), close + 1
                return None
    return None


# --------------------------------------------------------------------------
# Block markdown -> Ricos nodes
# --------------------------------------------------------------------------

_IMAGE_LINE = re.compile(r"^!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]+)\)\s*$")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_BULLET = re.compile(r"^\s*[-*+]\s+(.*)$")
_ORDERED = re.compile(r"^\s*(\d+)[.)]\s+(.*)$")
_QUOTE = re.compile(r"^>\s?(.*)$")
_RULE = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")


def _paragraph(text: str) -> dict:
    return {
        "type": "PARAGRAPH",
        "id": _next_id("p"),
        "nodes": parse_inline(text),
        "paragraphData": {},
    }


def _image_node(src: str, alt: str, media_map: dict, images: list) -> dict:
    images.append(src)
    media_id = media_map.get(src)
    if media_id is None and media_map:
        raise PostError(
            f"Image {src!r} is referenced in post.md but missing from the media map. "
            f"Re-run with --list-images and upload it."
        )
    image: dict = {"src": {"id": media_id} if media_id else {"id": f"LOCAL:{src}"}}
    node = {
        "type": "IMAGE",
        "id": _next_id("img"),
        "nodes": [],
        "imageData": {"image": image, "disableExpand": False},
    }
    if alt:
        node["imageData"]["altText"] = alt
    else:
        node["imageData"]["decorative"] = True
    return node


_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def markdown_to_nodes(body: str, media_map: dict | None = None, images: list | None = None) -> list:
    """Convert a markdown body into a flat list of Ricos block nodes."""
    media_map = media_map or {}
    images = images if images is not None else []

    # Authors leave notes to themselves in HTML comments; they are not content.
    body = _HTML_COMMENT.sub("", body)

    lines = body.split("\n")
    nodes: list = []
    i, n = 0, len(lines)

    while i < n:
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        # Fenced code block -- taken verbatim, never parsed for inline markers.
        if line.lstrip().startswith("```"):
            fence = line.strip()[:3]
            i += 1
            code: list[str] = []
            while i < n and not lines[i].strip().startswith(fence):
                code.append(lines[i])
                i += 1
            i += 1  # closing fence
            nodes.append({
                "type": "CODE_BLOCK",
                "id": _next_id("code"),
                "nodes": [{
                    "type": "TEXT",
                    "id": "",
                    "nodes": [],
                    "textData": {"text": "\n".join(code), "decorations": []},
                }],
                "codeBlockData": {},
            })
            continue

        if _RULE.match(line):
            nodes.append({
                "type": "DIVIDER",
                "id": _next_id("div"),
                "nodes": [],
                "dividerData": {"lineStyle": "SINGLE", "width": "LARGE", "alignment": "CENTER"},
            })
            i += 1
            continue

        image = _IMAGE_LINE.match(line.strip())
        if image:
            nodes.append(
                _image_node(image.group("src").strip(), image.group("alt").strip(), media_map, images)
            )
            i += 1
            continue

        heading = _HEADING.match(line)
        if heading:
            nodes.append({
                "type": "HEADING",
                "id": _next_id("h"),
                "nodes": parse_inline(heading.group(2).strip()),
                "headingData": {"level": len(heading.group(1))},
            })
            i += 1
            continue

        if _QUOTE.match(line):
            quoted: list[str] = []
            while i < n and _QUOTE.match(lines[i]):
                quoted.append(_QUOTE.match(lines[i]).group(1))
                i += 1
            nodes.append({
                "type": "BLOCKQUOTE",
                "id": _next_id("bq"),
                "nodes": [_paragraph(" ".join(q for q in quoted if q.strip()))],
                "blockquoteData": {"indentation": 1},
            })
            continue

        if _BULLET.match(line) or _ORDERED.match(line):
            ordered = bool(_ORDERED.match(line))
            pattern = _ORDERED if ordered else _BULLET
            items: list[str] = []
            while i < n and pattern.match(lines[i]):
                match = pattern.match(lines[i])
                items.append((match.group(2) if ordered else match.group(1)).strip())
                i += 1
            nodes.append({
                "type": "ORDERED_LIST" if ordered else "BULLETED_LIST",
                "id": _next_id("list"),
                "nodes": [
                    {
                        "type": "LIST_ITEM",
                        "id": _next_id("li"),
                        "nodes": [_paragraph(item)],
                    }
                    for item in items
                ],
                ("orderedListData" if ordered else "bulletedListData"): {"indentation": 0},
            })
            continue

        # Paragraph: consume until a blank line or the start of another block.
        para: list[str] = []
        while i < n and lines[i].strip():
            candidate = lines[i]
            if para and (
                _HEADING.match(candidate)
                or _BULLET.match(candidate)
                or _ORDERED.match(candidate)
                or _QUOTE.match(candidate)
                or _RULE.match(candidate)
                or candidate.lstrip().startswith("```")
                or _IMAGE_LINE.match(candidate.strip())
            ):
                break
            para.append(candidate.strip())
            i += 1
        nodes.append(_paragraph(" ".join(para)))

    return nodes


# --------------------------------------------------------------------------
# Payload assembly
# --------------------------------------------------------------------------

def build_payload(
    post_dir: Path,
    member_id: str,
    media_map: dict | None = None,
    tag_map: dict | None = None,
    publish: bool = False,
) -> tuple[dict, list, list]:
    """Read ``post.md`` and return the CreateDraftPost body, images, and tags.

    ``media_map`` resolves local image filenames to Wix media IDs; ``tag_map``
    resolves tag labels to Wix tag IDs. Both are looked up rather than fetched,
    so this stays a pure file-to-JSON transform.
    """
    md_path = post_dir / "post.md"
    if not md_path.is_file():
        raise PostError(f"No post.md in {post_dir}.")

    reset_ids()
    meta, body = parse_front_matter(md_path.read_text(encoding="utf-8"))

    images: list = []
    nodes = markdown_to_nodes(body, media_map, images)
    if not nodes:
        raise PostError("Post body is empty.")

    cover = meta.get("cover")
    if cover:
        images.append(cover)
        if not (post_dir / cover).is_file():
            raise PostError(f"Cover image {cover!r} is not in {post_dir}.")

    draft: dict = {
        "title": str(meta["title"]).strip(),
        "memberId": member_id,
        "richContent": {"nodes": nodes},
    }
    if meta.get("excerpt"):
        draft["excerpt"] = str(meta["excerpt"]).strip()

    # Tags are real Wix entities addressed by ID. The free-text `hashtags`
    # field is not settable through this API -- verified against the live API,
    # where submitted hashtags came back empty -- so labels must be resolved to
    # tag IDs by the push step before they mean anything.
    tags = [str(t).strip() for t in (meta.get("tags") or []) if str(t).strip()]
    if tags:
        tag_map = tag_map or {}
        resolved = [tag_map[t] for t in tags if t in tag_map]
        missing = [t for t in tags if t not in tag_map]
        if missing and tag_map:
            raise PostError(
                f"Tag(s) {', '.join(missing)} are missing from the tag map. "
                f"Re-run with --list-tags and create them."
            )
        if resolved:
            draft["tagIds"] = resolved

    if meta.get("featured"):
        draft["featured"] = True

    slug = str(meta.get("slug") or slugify(str(meta["title"]))).strip()
    draft["seoSlug"] = slug

    if cover:
        media_id = (media_map or {}).get(cover)
        draft["media"] = {
            "displayed": True,
            "custom": True,
            "altText": str(meta.get("cover_alt") or meta["title"]).strip(),
            "wixMedia": {"image": {"id": media_id} if media_id else {"id": f"LOCAL:{cover}"}},
        }

    payload = {"draftPost": draft, "publish": bool(publish), "fieldsets": ["URL"]}

    size = len(json.dumps(payload).encode("utf-8"))
    if size > MAX_POST_BYTES:
        raise PostError(
            f"Post payload is {size:,} bytes; Wix rejects anything over {MAX_POST_BYTES:,}."
        )

    # Preserve order, drop duplicates.
    return payload, list(dict.fromkeys(images)), tags


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("post_dir", type=Path, help="the post's folder, containing post.md")
    parser.add_argument("--member-id", default="e00ee638-af7f-4aac-aa2b-c99d795ecf78",
                        help="Wix blog author member ID (defaults to Ryan's)")
    parser.add_argument("--media-map", type=Path,
                        help="JSON mapping local image paths to Wix media IDs")
    parser.add_argument("--tag-map", type=Path,
                        help="JSON mapping tag labels to Wix tag IDs")
    parser.add_argument("--out", type=Path, help="write the payload here (default: stdout)")
    parser.add_argument("--list-images", action="store_true",
                        help="print the local images this post references, then exit")
    parser.add_argument("--list-tags", action="store_true",
                        help="print the tag labels this post references, then exit")
    parser.add_argument("--publish", action="store_true",
                        help="publish on create instead of leaving it an unpublished draft")
    args = parser.parse_args(argv)

    try:
        media_map = {}
        if args.media_map:
            media_map = json.loads(args.media_map.read_text(encoding="utf-8"))
        tag_map = {}
        if args.tag_map:
            tag_map = json.loads(args.tag_map.read_text(encoding="utf-8"))

        payload, images, tags = build_payload(
            args.post_dir, args.member_id, media_map, tag_map, publish=args.publish
        )

        if args.list_images or args.list_tags:
            listed = images if args.list_images else tags
            for item in listed:
                print(item)
            if not listed:
                print("(none)", file=sys.stderr)
            return 0

        missing = [i for i in images if i not in media_map]
        if missing:
            print(
                "Warning: no media ID for "
                + ", ".join(missing)
                + " -- these carry a LOCAL: placeholder and will not render. "
                  "Upload them and pass --media-map.",
                file=sys.stderr,
            )
        if tags and not tag_map:
            print(
                "Warning: this post declares tags ("
                + ", ".join(tags)
                + ") but no --tag-map was given, so it will publish untagged.",
                file=sys.stderr,
            )

        text = json.dumps(payload, indent=2, ensure_ascii=False)
        if args.out:
            args.out.write_text(text, encoding="utf-8")
            print(f"Wrote {args.out} ({len(text.encode('utf-8')):,} bytes)", file=sys.stderr)
        else:
            print(text)
        return 0

    except PostError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
