#!/usr/bin/env python
"""Guard: the two recruiter-brief web pages cannot drift from their markdown.

WHY THIS EXISTS
---------------
Each brief exists twice — as markdown here (the copy Ry attaches to an email)
and as a page under `hire/` (the copy he links). Two copies of one string with
nothing forcing agreement is the failure `resume_build/verify_facts.py` was
written for: a correction lands in one and not the other, and nothing can see
the gap. This script is that check for the briefs.

    python ryan-resume-dev/for_recruiters/verify_brief.py     # from the repo root
    # exit 0 = clean, 1 = drift, and it says which brief and which check

WHAT IT CHECKS, per (markdown, page) pair
-----------------------------------------
  1. The pitch — the paragraph under "## In three sentences" — appears on the
     page VERBATIM (whitespace, entities and curly quotes normalised).
  2. Every dollar figure in the markdown ($300K, $20K, $175/hr, $13,400/mo,
     $5,000, $160–200K, $145K …) appears on the page.
  3. Every title in the markdown's title table appears on the page.
  4. Every industry in the markdown's "Out" list appears on the page — the
     exclusions are the line Ry holds no matter who is pitching, and a page
     that dropped one would be the page that gets him pitched the wrong role.

Every check first asserts it found its anchor in the markdown. A guard that
silently matches nothing is worse than no guard.

It is directional: the page may carry things the markdown lacks (the contact
line, the proof-point cards); the markdown may not carry a pitch, a figure, a
title, or an exclusion the page lacks. It deliberately does NOT compare the
proof points sentence for sentence — those are laid out differently on the
page by design, and a sentence-level guard would force the page to be the
markdown with tags on.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent

PAIRS = [
    (HERE / "recruiter-brief-engineering.md", REPO_ROOT / "hire" / "recruiter-brief" / "index.html"),
    (HERE / "recruiter-brief-music.md", REPO_ROOT / "hire" / "recruiter-brief-music" / "index.html"),
]

FIGURE = re.compile(r"\$\d[\d,]*(?:–\d[\d,]*)?[KkM]?(?:/hr|/mo)?")


def norm(text: str) -> str:
    """One comparable form for both sides: entities decoded, quotes straightened,
    whitespace collapsed. Markdown emphasis markers are stripped so *to* in the
    markdown matches <em>to</em> on the page."""
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"(?<!\w)[*_]{1,2}(?=\S)|(?<=\S)[*_]{1,2}(?!\w)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)      # [label](url) -> label
    return re.sub(r"\s+", " ", text).strip()


def section(md: str, heading: str) -> str | None:
    """Body of the `## heading` section, or None if the heading is absent."""
    m = re.search(rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)", md, re.M | re.S)
    return m.group(1) if m else None


def check_pair(md_path: Path, html_path: Path, errors: list[str]) -> None:
    label = f"{md_path.name} ↔ {html_path.relative_to(REPO_ROOT).as_posix()}"
    for p in (md_path, html_path):
        if not p.is_file():
            errors.append(f"{label}: file missing — {p}")
            return
    md = md_path.read_text(encoding="utf-8")
    page = norm(html_path.read_text(encoding="utf-8"))

    # -- 1. the pitch, verbatim ------------------------------------------
    body = section(md, "In three sentences")
    if body is None or not body.strip():
        errors.append(f"{label}: 1. anchor missing — no '## In three sentences' section in the markdown; this check is guarding nothing")
    else:
        pitch = norm(body)
        if pitch not in page:
            at = next((i for i, (a, b) in enumerate(zip(pitch, page[page.find(pitch[:40]):])) if a != b), None)
            errors.append(
                f"{label}: 1. the pitch on the page is not the markdown's pitch\n"
                f"    markdown: {pitch[:110]}…\n"
                f"    first divergence near character {at if at is not None else '?'} of the pitch"
            )

    # -- 2. every dollar figure -----------------------------------------
    figures = sorted(set(FIGURE.findall(md)))
    if not figures:
        errors.append(f"{label}: 2. anchor missing — no dollar figures found in the markdown; this check is guarding nothing")
    for fig in figures:
        if fig not in page:
            errors.append(f"{label}: 2. figure {fig!r} is in the markdown and not on the page")

    # -- 3. every title in the title table ------------------------------
    rows = re.findall(r"^\|\s*(?!Track\b|-+)([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", md, re.M)
    titles = [t.strip() for _, cell in rows for t in cell.split("·") if t.strip()]
    if not titles:
        errors.append(f"{label}: 3. anchor missing — no title table found in the markdown; this check is guarding nothing")
    for title in titles:
        if norm(title) not in page:
            errors.append(f"{label}: 3. title {title!r} is in the markdown and not on the page")

    # -- 4. every excluded industry -------------------------------------
    m = re.search(r"^\*\*Out, regardless of comp:\*\*\s*(.+)$", md, re.M)
    if not m:
        errors.append(f"{label}: 4. anchor missing — no 'Out, regardless of comp' line in the markdown; this check is guarding nothing")
    else:
        outs = [o.strip().rstrip(".") for o in m.group(1).split(",")]
        for out in outs:
            # "weapons and firearms retail" on the page is "Weapons & firearms retail"
            variants = {norm(out).lower(), norm(out).lower().replace(" and ", " & ")}
            if not any(v in page.lower() for v in variants):
                errors.append(f"{label}: 4. exclusion {out!r} is in the markdown and not on the page")


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
        except (AttributeError, OSError, ValueError):
            pass

    errors: list[str] = []
    for md_path, html_path in PAIRS:
        before = len(errors)
        check_pair(md_path, html_path, errors)
        status = "PASS" if len(errors) == before else f"FAIL ({len(errors) - before})"
        print(f"  {md_path.name.ljust(34)} {status}")
    print()
    if errors:
        print(f"FAIL — {len(errors)} problem(s)\n", file=sys.stderr)
        for e in errors:
            print(f"  x {e}", file=sys.stderr)
        return 1
    print(f"OK — {len(PAIRS)} briefs: pitch verbatim, every figure, title, and exclusion present on the page.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
