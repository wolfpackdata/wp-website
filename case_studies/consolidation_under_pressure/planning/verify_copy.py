#!/usr/bin/env python
"""Guard the "Consolidation Under Pressure" case study against its source document.

    python case_studies/consolidation_under_pressure/planning/verify_copy.py
    # exit 0 = clean, 1 = drift, and it says which check and which string

WHY THIS EXISTS
---------------
The report's copy now lives in two places: `01-ma-landscape-2016-2026.md` beside
this script, and the HTML page one directory up. The site brief's own rule is
that any string existing in more than one artifact gets a machine guard or it
will diverge, and the three largest duplications on this property are unguarded
precisely because nobody wrote one. This is the fourth duplication, and it is
guarded.

The `.md` was copied in here from `wolfpackdata/dj-gear-study` (`docs/strategy/`)
at build time, 2026-08-11. It is vendored rather than referenced because a check
that reaches into a sibling clone passes or fails depending on whether somebody
happens to have that clone — which is a check that reports nothing on most
machines.

⚠️ **THE PROSE IS NO LONGER FROZEN, AND THIS SCRIPT NO LONGER PRETENDS IT IS.**
The creative brief called the copy final, and until 2026-08-15 the `.md` was the
source of record for every word. Ry's review (#195) ended that: sentences were
rewritten for evidentiary correctness — headline consideration gaps are not
losses, a transaction timeline does not establish cause, an absence of public
evidence is not evidence of absence — and roughly a tenth of the prose was cut as
restatement. **Passages that exist in the `.md` and not on the page are now
expected.** Do not "restore" them.

What did NOT change is the rule about figures, which is why check 1 below still
guards the whole numeric surface: a report may be edited, but it may not quietly
lose a number. Every figure in the source is still on the page, and that is
asserted on every run. If a future edit legitimately retires a figure, delete it
from the vendored `.md` in the same commit and say why in the design plan — do
not weaken the check.

WHAT IT CHECKS, and why each one is the check worth having
----------------------------------------------------------
1. Every numeric token in the source appears on the page. Dollars, euros,
   percentages, thousands-separated counts. This is the check that matters: the
   currency parentheticals are a stated editorial standard, and a report whose
   figures drift is worse than no report because it is still believed. Prose
   gets edited legitimately — see the warning above — and a number does not.
   It survived a ~13% prose cut in #195 without a single figure going missing,
   which is exactly the property it exists to hold.
2. The Src gutter's arithmetic. 43 rows, 31 with a primary source, 12 with a
   dash. The link-versus-dash distinction is the page's load-bearing claim about
   its own evidence, and it is exactly the kind of thing a well-meaning edit
   quietly breaks by adding a row.
3. Every source link opens in a new tab, with `rel="noopener"`, a `title` and an
   `aria-label`. The visible label is an arrow glyph, so without an accessible
   name a screen reader announces thirty-one links called "link".
4. Every dash carries a visually-hidden sentence saying what it means, for the
   same reason.
5. The map dataset: the event count, and that every lane index and value bucket
   is in range.
6. Nothing in the page reaches a third-party host for a RESOURCE. Citations are
   links and are supposed to be external; a stylesheet, script, font or image is
   not.

FAILING LOUDLY WHEN THE ANCHOR MOVES
------------------------------------
Every structural check below asserts it found something before it asserts the
something is right. A check that silently matches zero rows is worse than no
check, because it reports success forever after the markup it was watching was
renamed. If you restructure the tables, this script should go red — that is the
feature, not the bug.

stdlib only. No Pillow, no network, no pip install.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = HERE.parent / "index.html"
MAP_PAGE = HERE.parent / "transaction-map.html"
SOURCE = HERE / "01-ma-landscape-2016-2026.md"
MAP_JS = HERE.parent.parent / "case-study-assets" / "js" / "map.js"

# The three counts the page states about itself, in the copy, in the stat tiles
# and in the Src explainer. They are asserted here so the prose and the markup
# cannot disagree.
ROWS = 43
LINKED = 31
DASHED = 12
EVENTS = 42


# --------------------------------------------------------------------------
# Normalisation
# --------------------------------------------------------------------------

DASHES = {
    "–": "-", "—": "-", "−": "-",   # en, em, minus
    "≈": "~", " ": " ", "×": "x",
    "“": '"', "”": '"', "‘": "'", "’": "'",
}


def norm(s: str) -> str:
    for a, b in DASHES.items():
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s)


def page_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    raw = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    raw = re.sub(r"<(script|style)\b.*?</\1>", " ", raw, flags=re.S)
    return norm(html.unescape(re.sub(r"<[^>]+>", "", raw)))


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

NUMERIC = [
    r"[$€]\s?\d[\d,\.]*\s?(?:bn|m|k)?",   # $8.2bn, €200m, $27.05
    r"\d+(?:\.\d+)?%",                          # 6.4%, 145%
    r"\b\d{1,3}(?:,\d{3})+\b",                  # 240,000
    r"\b\d+(?:\.\d+)?(?:bn|m)\b",               # 837m, 1.03bn
]


def check_numbers(errors: list[str]) -> None:
    source = norm(SOURCE.read_text(encoding="utf-8"))
    text = re.sub(r"\s+", "", page_text(PAGE))

    tokens: set[str] = set()
    for pattern in NUMERIC:
        tokens.update(re.sub(r"\s+", "", t) for t in re.findall(pattern, source))

    if len(tokens) < 150:
        errors.append(
            f"1. only {len(tokens)} numeric tokens found in {SOURCE.name} — the source "
            f"carried ~186 at build time, so either the document shrank drastically or "
            f"this check is now matching almost nothing"
        )
        return

    missing = sorted(t for t in tokens if t not in text)
    for t in missing:
        errors.append(
            f"1. the figure {t} is in {SOURCE.name} but not on the page — the copy is "
            f"frozen, so a figure that left is a defect, not an edit"
        )


def check_src_gutter(errors: list[str]) -> None:
    raw = PAGE.read_text(encoding="utf-8")
    cells = re.findall(r'<td class="src">(.*?)</td>', raw, flags=re.S)
    links = raw.count('class="srclink"')
    dashes = raw.count('class="nosrc"')

    if not cells:
        errors.append(
            '2. no <td class="src"> cells found at all — the Src gutter markup was '
            "renamed or removed, and this check is now guarding nothing"
        )
        return

    if len(cells) != ROWS:
        errors.append(f"2. {len(cells)} Src cells, expected {ROWS}")
    if links != LINKED:
        errors.append(f"2. {links} source links, expected {LINKED}")
    if dashes != DASHED:
        errors.append(f"2. {dashes} muted dashes, expected {DASHED}")
    if links + dashes != len(cells):
        errors.append(
            f"2. {links} links + {dashes} dashes != {len(cells)} cells — a row has "
            f"neither a source nor a dash, which reads as 'not yet filled in'"
        )


def check_link_accessibility(errors: list[str]) -> None:
    raw = PAGE.read_text(encoding="utf-8")
    anchors = re.findall(r"<a class=\"srclink\"[^>]*>", raw)
    if not anchors:
        errors.append('3. no <a class="srclink"> found — check 3 is guarding nothing')
        return
    for a in anchors:
        href = re.search(r'href="([^"]*)"', a)
        where = href.group(1)[:60] if href else a[:60]
        for attr in ('target="_blank"', 'rel="noopener"', "title=", "aria-label="):
            if attr not in a:
                errors.append(f"3. source link missing {attr.rstrip('=')} — {where}")

    cells = re.findall(r'<td class="src">(.*?)</td>', raw, flags=re.S)
    for cell in cells:
        if "nosrc" in cell and "visually-hidden" not in cell:
            errors.append(
                "4. a dash cell has no visually-hidden explanation — a screen reader "
                "gets an em dash and no idea it means 'no primary source verified'"
            )


def check_map(errors: list[str]) -> None:
    js = MAP_JS.read_text(encoding="utf-8")
    block = re.search(r"var EVENTS = \[(.*?)\n  \];", js, flags=re.S)
    if not block:
        errors.append(
            "5. could not find the EVENTS array in map.js — it was renamed or "
            "reformatted, and this check is now guarding nothing"
        )
        return

    rows = re.findall(r"\[\s*(\d{4}\.\d+),\s*(\d),\s*'(.*?)',\s*(\d)\s*\]", block.group(1))
    if len(rows) != EVENTS:
        errors.append(f"5. {len(rows)} map events, expected {EVENTS}")

    for year, lane, label, bucket in rows:
        if not 2014.0 <= float(year) <= 2026.9:
            errors.append(f"5. event outside the plotted axis: {year} — {label}")
        if not 0 <= int(lane) <= 3:
            errors.append(f"5. lane index {lane} out of range — {label}")
        if not 0 <= int(bucket) <= 4:
            errors.append(f"5. value bucket {bucket} out of range — {label}")

    # Both pages must state the same count as the dataset carries.
    for path in (PAGE, MAP_PAGE):
        text = page_text(path)
        if f"{EVENTS} events" not in text and f"{EVENTS} transactions" not in text:
            errors.append(
                f"5. {path.name} does not state the event count as {EVENTS} — the "
                f"dataset and the prose about it have to move together"
            )


def check_external_resources(errors: list[str]) -> None:
    for path in (PAGE, MAP_PAGE):
        raw = path.read_text(encoding="utf-8")
        for tag in re.findall(r"<(?:script|img)[^>]*>", raw):
            m = re.search(r'src="(https?:[^"]*)"', tag)
            if m:
                errors.append(f"6. {path.name} loads an external resource: {m.group(1)}")
        for tag in re.findall(r"<link[^>]*>", raw):
            if 'rel="canonical"' in tag:
                continue        # a canonical is a declaration, not a request
            m = re.search(r'href="(https?:[^"]*)"', tag)
            if m:
                errors.append(f"6. {path.name} loads an external resource: {m.group(1)}")
        if re.search(r"@import|url\(\s*[\"']?https?:", raw):
            errors.append(f"6. {path.name} contains an @import or a remote url()")
        if "<style" in raw:
            errors.append(
                f"6. {path.name} has an inline <style> block — every rule belongs in "
                f"case-study-assets/css/case-study.css so the next case study inherits it"
            )


def main() -> int:
    for path in (PAGE, MAP_PAGE, SOURCE, MAP_JS):
        if not path.is_file():
            print(f"FAIL: missing {path}", file=sys.stderr)
            return 1

    errors: list[str] = []
    check_numbers(errors)
    check_src_gutter(errors)
    check_link_accessibility(errors)
    check_map(errors)
    check_external_resources(errors)

    if errors:
        print(f"{len(errors)} problem(s):\n")
        for e in errors:
            print(f"  {e}")
        return 1

    print(
        "clean — every figure in the source is on the page; "
        f"{ROWS} Src cells ({LINKED} linked, {DASHED} dashed), all named; "
        f"{EVENTS} map events in range; no external resources."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
