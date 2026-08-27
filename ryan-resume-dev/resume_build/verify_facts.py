#!/usr/bin/env python
"""Check the résumés against a single declared fact table.

Replaces verify_verbatim.py, retired at v2.0. v1's question was "did the wording
move away from the published v0?" — a valid question exactly once, for a round
that was a restyling and nothing else. From v2 on the wording is *supposed* to
move, and the question worth asking permanently is different:

    is anything on the page not true, and do the two résumés contradict
    each other?

Checks 1–4 run on the YAML rather than the .docx, so a failure points at the
line you would edit. Checks 5 and 6 are the exceptions and say why:

  1. every role's (title, org, dates) appears in EMPLOYERS
  2. every figure on either page appears in FIGURES
  3. every fact in SHARED that appears on one résumé appears on both
  4. the banner artboards, brand.CONTACT, and each meta.subject all agree
  5. the built .docx actually yields the name and contact details as text
  6. the website's HTML copies of the project blurbs still match the YAML

    python build.py && python verify_facts.py    # 5 reads what build.py wrote
    # exit 0 = clean, 1 = drift, and it says where
"""

from __future__ import annotations

import html
import re
import sys
import zipfile
from pathlib import Path

import yaml

from resumekit import brand

HERE = Path(__file__).resolve().parent
CONTENT = {
    "eng-music": HERE / "content" / "eng_music.yaml",
    "eng-only": HERE / "content" / "eng_only.yaml",
}
ARTBOARDS = HERE.parent / "resume_design" / "templates" / "export"
VERSION_FILE = HERE / "VERSION"

# Website pages that carry the project blurbs as hand-written HTML, and the
# résumé each one is copied from. Check 6 compares them; see its docstring.
REPO_ROOT = HERE.parent.parent
HTML_PAGES = {
    "portfolio/": (REPO_ROOT / "portfolio" / "index.html", "eng-only"),
    "hire/ryan-hickey/": (REPO_ROOT / "hire" / "ryan-hickey" / "index.html", "eng-only"),
    "hire/ryan-hickey-music/": (
        REPO_ROOT / "hire" / "ryan-hickey-music" / "index.html",
        "eng-music",
    ),
}


# --------------------------------------------------------------------------
# The fact table. This is the source of truth — the résumés are checked
# against it, never the other way round. Change a fact here first.
# --------------------------------------------------------------------------

# (title, org, dates). A role on either résumé must match a row exactly.
EMPLOYERS = {
    ("Head of Insights & Analytics", "Tromml Inc.", "2023–2026"),
    ("Founder & Principal Consultant", "Wolfpack Data & Strategy LLC", "2023–Present"),
    ("Chief Operating Officer & Partner", "Auto SOSS Inc. / Shock Surplus", "2015–2025"),
    ("Director of Marketing Science", "In4mation Insights", "2009–2012"),
    ("Founder & Owner", "Niceman Music Studio LLC", "2009–2016"),
    ("Founder & Producer", "RML Creative LLC", "2023–Present"),
}

# Every money amount, duration, year, and headcount allowed to appear.
FIGURES = {
    "$300K": "Auto SOSS revenue at the start of the growth run",
    "$30M": "Auto SOSS revenue at the end of it",
    "$20k": "Tromml platform MRR",
    # The four music spans are four different numbers and none of them is a
    # career length (D-009). Through v2.3 "36 years" covered a "36-year music
    # career" and "20+ years" covered DJ performance; both were wrong and both
    # are retired here.
    "20+ years": "coding experience; also studio production, recording, and audio engineering",
    "17 years": "leading tech/analytics/ops — In4mation 2009 to now (was '14+' through v1)",
    "36 years": "piano playing and study — a practice span, never a career span",
    "23 years": "paid music performance, since 2003",
    "10 years": "classical piano study with a university professor (D-010; the copy spells it 'Ten years', so this row documents the fact rather than matching a pattern)",
    # Distinct from "10 years" above, and deliberately a different string: this
    # one is the Shopify Plus tenure at Auto SOSS, whose dates (2015–2025) are
    # the ten-year floor it claims.
    "10+ years": "running the Shopify Plus storefront as COO at Auto SOSS",
    "up to 20 people": "team and vendor span at Auto SOSS",
    "2003": "paid music performance start",
    "2007": "Cornell B.S.",
    "2009": "In4mation and Niceman start; professional DJ work starts",
    "2012": "In4mation end",
    "2015": "Auto SOSS start",
    "2016": "Niceman end",
    "2023": "Tromml, Wolfpack, and RML Creative start",
    "2025": "Auto SOSS end",
    "2026": "Tromml end; the Current Technical Focus year; the CCA-F target",
}

FIGURE_PATTERNS = (
    r"\$\d[\d,]*(?:\.\d+)?\s*[KkMm]?",     # $300K, $30M, $20k
    r"\d+\+?\s*(?:years|yrs)",             # 20+ years, 17 years, 36 years
    r"up to \d+ people",                   # headcount span
    r"\b(?:19|20)\d{2}\b",                 # bare years
)

# Facts stated on both résumés, in deliberately different words. The regex is
# the invariant; the prose around it is free to differ by audience.
SHARED = {
    "Niceman ran commercially, with paying clients": r"working studio with paying clients",
    "Niceman music was published and licensed": r"published and licensed for use",
    "the flat-response acoustic build": r"flat-response acoustic recording environment",
    "the $300K → $30M growth run": r"\$300K to \$30M",
    "the Tromml MRR figure": r"\$20k",
    "the Auto SOSS algorithms were Python and SQL": r"pricing and inventory algorithms in\s+Python and SQL",
    "the Shopify Plus tenure": r"Shopify Plus storefront for 10\+ years",
    "SetMaster is at v3.0.4, not the prototype": r"v3\.0\.4",
    "the AI dev command center": r"command center",
    # v2.1: RML is named on both, so a reader who searches it finds the same
    # entity from either résumé. Dropping it from one would break that.
    "RML Creative LLC is named": r"RML Creative LLC",
    # v2.4 (D-010): the music training. Both Education panels state it, in
    # sentences Ry wrote and approved verbatim — the surrounding prose differs
    # by audience but these two clauses may not. Retiring "self-taught" only
    # held on one page; this makes it hold on both.
    "ten years of classical study, with a teacher": r"[Tt]en years of classical piano study with a university professor",
    "the engineering was taught too": r"Sound engineering and composition\s+learned through mentors, online programs, and practice",
}


# --------------------------------------------------------------------------

def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def all_strings(node) -> list[str]:
    """Every string anywhere in the parsed YAML."""
    if isinstance(node, str):
        return [node]
    if isinstance(node, dict):
        return [s for v in node.values() for s in all_strings(v)]
    if isinstance(node, list):
        return [s for v in node for s in all_strings(v)]
    return []


def flat_text(content: dict) -> str:
    """One whitespace-normalized blob, so a fact broken across YAML folded
    lines still matches a regex written the way a human would write it."""
    return re.sub(r"\s+", " ", " ".join(all_strings(content)))


def check_employers(name: str, content: dict, errors: list[str]) -> set[tuple]:
    seen = set()
    for sec in content["sections"]:
        if sec["type"] != "experience":
            continue
        for role in sec["roles"]:
            row = (role["title"], role.get("org", ""), role.get("dates", ""))
            seen.add(row)
            if row not in EMPLOYERS:
                errors.append(
                    f"{name}: role not in EMPLOYERS — {row!r}\n"
                    f"    either the résumé drifted, or the fact table needs the new row"
                )
    return seen


def check_figures(name: str, text: str, errors: list[str]) -> None:
    found: dict[str, int] = {}
    for pattern in FIGURE_PATTERNS:
        for raw in re.findall(pattern, text):
            figure = re.sub(r"\s+", " ", raw).strip()
            found[figure] = found.get(figure, 0) + 1
    # One error per distinct figure — a number repeated across three sections is
    # one problem to fix, not three.
    for figure, count in found.items():
        if figure not in FIGURES:
            times = "" if count == 1 else f" ({count}×)"
            errors.append(
                f"{name}: undeclared figure {figure!r}{times}\n"
                f"    add it to FIGURES with a note, or fix the wording"
            )


def check_shared(texts: dict[str, str], errors: list[str]) -> None:
    for label, pattern in SHARED.items():
        present = [n for n, t in texts.items() if re.search(pattern, t)]
        if present and len(present) != len(texts):
            missing = sorted(set(texts) - set(present))
            errors.append(
                f"shared fact on some résumés but not others — {label}\n"
                f"    present: {', '.join(sorted(present))}   missing: {', '.join(missing)}"
            )


def check_header(contents: dict[str, dict], errors: list[str]) -> None:
    """The header ships as text built from brand.CONTACT. The banner artboards
    in resume_design are no longer embedded — v2.2 removed the image header —
    but they remain the design record of what the header says, and brand.py
    mirrors them. Nothing forces the two to agree, so check it."""
    for name, content in contents.items():
        variant = content["meta"]["variant"]
        expected = brand.ROLE_LINES[variant]
        actual = content["meta"].get("subject", "")
        if actual != expected:
            errors.append(
                f"{name}: meta.subject does not match brand.ROLE_LINES[{variant!r}]\n"
                f"    subject: {actual!r}\n    expected: {expected!r}"
            )

    for variant in ("eng", "music"):
        art = ARTBOARDS / f"header-dark-{variant}.html"
        if not art.exists():
            errors.append(f"artboard missing: {art}")
            continue
        html = art.read_text(encoding="utf-8")
        role_plain = re.sub(r"<[^>]+>", "", html)
        role_plain = role_plain.replace("&amp;", "&").replace("&middot;", "·")
        role_plain = re.sub(r"\s+", " ", role_plain)

        for title in brand.ROLE_LINES[variant].split(" · "):
            if title not in role_plain:
                errors.append(
                    f"banner {variant}: artboard is missing the title {title!r} "
                    f"— re-run resume_design/templates/export-png.ps1 after fixing"
                )
        for key in ("email", "linkedin", "github", "location"):
            if brand.CONTACT[key] not in role_plain:
                errors.append(
                    f"banner {variant}: artboard is missing CONTACT[{key!r}] = "
                    f"{brand.CONTACT[key]!r}"
                )


def docx_text(path: Path) -> str:
    """The document body as a naive parser sees it: every <w:t> in reading
    order, whitespace-normalized. Deliberately ignores images and the Word
    header/footer parts, because a good number of ATS parsers do too."""
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    runs = re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml, re.S)
    # Word escapes & < > in run text, so "Software Engineering & Architecture"
    # is stored as "Software Engineering &amp; …". Unescape or every check on
    # an ampersand fails.
    return re.sub(r"\s+", " ", html.unescape(" ".join(runs)))


def check_parseable(contents: dict[str, dict], errors: list[str]) -> None:
    """The one check that reads the built .docx instead of the YAML, because
    the property it guards is invisible in the YAML.

    Through v2.1 the header was a PNG, so the first extractable string in the
    document was 'Professional Summary' — the name, email, LinkedIn, GitHub,
    and location existed only as pixels, and a parser built a candidate record
    with no name and no way to make contact. That shipped for three versions
    without anything noticing. v2.2 made the header text; this stops it
    silently going back.
    """
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    for name, content in contents.items():
        meta = content["meta"]
        built = (HERE / meta["output_dir"]).resolve() / (
            f"Ryan_Hickey_Resume_{meta['slug']}_v{version}.docx"
        )
        if not built.exists():
            errors.append(
                f"{name}: no v{version} build to check — run `python build.py` first\n"
                f"    expected {built}"
            )
            continue

        text = docx_text(built)
        for key in ("name", "email", "linkedin", "github", "location"):
            if brand.CONTACT[key] not in text:
                errors.append(
                    f"{name}: {built.name} has no extractable "
                    f"CONTACT[{key!r}] = {brand.CONTACT[key]!r}\n"
                    f"    an ATS would file this résumé without it"
                )
        if brand.ROLE_LINES[meta["variant"]] not in text:
            errors.append(
                f"{name}: {built.name} has no extractable role line"
            )
        # The name must be the *first* thing, not merely present somewhere.
        if not text.lstrip().startswith(brand.CONTACT["name"]):
            errors.append(
                f"{name}: {built.name} does not open with the name — it opens "
                f"{text.lstrip()[:40]!r}"
            )


def plain(markup: str) -> str:
    """HTML (or plain YAML text) reduced to comparable prose: tags dropped,
    entities resolved, whitespace collapsed. `&amp;` and `&rsquo;` in the pages
    are the same characters as `&` and `’` in the YAML, and a YAML folded block
    is the same sentence as a long HTML line — both differences are encoding,
    not content, so neither may register as drift."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", markup))).strip()


def project_items(content: dict) -> dict[str, str]:
    """name -> body for every item in the résumé's `projects` section."""
    out: dict[str, str] = {}
    for sec in content["sections"]:
        if sec.get("type") != "projects":
            continue
        for item in sec.get("items", []):
            out[plain(item["name"])] = plain(item["body"])
    return out


def check_html_blurbs(contents: dict[str, dict], errors: list[str]) -> None:
    """The second check that reads something other than the YAML, and the only
    one that leaves ryan-resume-dev entirely.

    The hire/ and portfolio/ pages retype the project names and blurbs as HTML
    by hand. Three copies of each string now exist and nothing forced them to
    agree: through v2.4 this checker validated the YAML against itself and never
    opened a web page, so a hire/ blurb could have been edited in place and no
    check would have noticed. The portfolio page made that a third copy, which
    is what prompted closing the gap (wp-website#95, design plan D-006).

    Every .app__name and .app__blurb on each page must appear verbatim in that
    page's source résumé. The comparison is one-directional on purpose: a page
    may show a SUBSET of the résumé's projects (the music résumé carries seven,
    the eng-only one eight), but it may not show a string the résumé does not.

    Cards are matched by NAME so a failing blurb can be reported against its
    expected text with the point of divergence marked. Reporting only "this
    string is not in the YAML" is technically complete and practically useless
    on a 90-word blurb.
    """
    for label, (path, variant) in HTML_PAGES.items():
        if not path.exists():
            errors.append(
                f"{label}: HTML_PAGES names a page that does not exist — {path}\n"
                f"    if the page was removed or moved, remove or update its row"
            )
            continue

        page = path.read_text(encoding="utf-8")
        items = project_items(contents[variant])

        # (name, blurb) per card, in document order. Anchored to the <article>
        # so a card missing one of the two is a parse failure, not a silent skip.
        cards = re.findall(
            r'<h3 class="app__name">(.*?)</h3>\s*'
            r'<p class="app__blurb">(.*?)</p>',
            page,
            re.S,
        )
        if not cards:
            errors.append(
                f"{label}: no .app__name / .app__blurb pairs found — the markup "
                f"changed, and this check is now silently guarding nothing"
            )
            continue

        for raw_name, raw_blurb in cards:
            name, blurb = plain(raw_name), plain(raw_blurb)
            if name not in items:
                errors.append(
                    f"{label}: .app__name is not in {CONTENT[variant].name} — "
                    f"{name!r}\n"
                    f"    add the project to the YAML, or fix the name on the page"
                )
                continue
            expected = items[name]
            if blurb != expected:
                at = next(
                    (i for i, (a, b) in enumerate(zip(blurb, expected)) if a != b),
                    min(len(blurb), len(expected)),
                )
                errors.append(
                    f"{label}: .app__blurb for {name!r} is not verbatim from "
                    f"{CONTENT[variant].name}\n"
                    f"    diverges at character {at}\n"
                    f"    page: …{blurb[max(0, at - 30):at + 50]!r}\n"
                    f"    yaml: …{expected[max(0, at - 30):at + 50]!r}\n"
                    f"    fix the page to match the YAML, or change the YAML "
                    f"first and re-copy"
                )


def main() -> int:
    errors: list[str] = []
    contents = {n: load(p) for n, p in CONTENT.items()}
    texts = {n: flat_text(c) for n, c in contents.items()}

    seen: set[tuple] = set()
    for name, content in contents.items():
        seen |= check_employers(name, content, errors)
        check_figures(name, texts[name], errors)
    check_shared(texts, errors)
    check_header(contents, errors)
    check_parseable(contents, errors)
    check_html_blurbs(contents, errors)

    unused = EMPLOYERS - seen
    if unused:
        errors.append(
            "EMPLOYERS rows on no résumé — stale fact table?\n"
            + "".join(f"    {row!r}\n" for row in sorted(unused)).rstrip()
        )

    if errors:
        print(f"FAIL — {len(errors)} problem(s)\n", file=sys.stderr)
        for e in errors:
            print(f"  x {e}", file=sys.stderr)
        return 1

    print(
        f"OK — {len(EMPLOYERS)} roles, {len(FIGURES)} figures, "
        f"{len(SHARED)} shared facts, headers consistent, contact block parseable, "
        f"{len(HTML_PAGES)} HTML pages verbatim."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
