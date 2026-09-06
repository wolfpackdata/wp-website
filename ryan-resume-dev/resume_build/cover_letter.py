#!/usr/bin/env python
"""Build a cover letter from a letter YAML, on the résumé's stationery.

    python cover_letter.py ../cover_letters/2026-08-18-acme.yaml
    python cover_letter.py ../cover_letters/2026-08-18-acme.yaml --pdf
    python cover_letter.py --template          # rebuild the committed template DOCX

Writes Ryan_Hickey_Cover_Letter_<Company>.docx next to the YAML (override with
--out). The letter carries the same header, footer, fonts, and palette as the
résumés — resumekit/letter.py reuses the résumé builder's own stationery
functions, so the two cannot drift apart.

The workflow this exists for: Ry hands over cover-letter text; a session drops
it into a YAML copied from ../cover_letters/_template.yaml, runs this, and the
application-ready .docx (and --pdf, through Word, same engine as the résumé
PDFs) comes out matching the résumé it will travel with. The sign-off is always
"Warmly," / Ryan — the builder's default, so the YAML never has to say it.

Letters are one-offs, so nothing here reads ./VERSION and the filename carries
the company, not a version.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

from build import warn_missing_fonts
from resumekit import brand, build_cover_letter

HERE = Path(__file__).resolve().parent
LETTERS_DIR = HERE.parent / "cover_letters"
TEMPLATE_YAML = LETTERS_DIR / "_template.yaml"


def slugify(company: str) -> str:
    """Acme Corp, Inc. -> Acme_Corp_Inc — filename-safe, recruiter-readable."""
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", company).strip("_")
    return cleaned or "Letter"


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        content = yaml.safe_load(f)
    for key in ("meta", "letter"):
        if key not in content:
            raise ValueError(f"{path.name} is missing top-level '{key}'")
    return content


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("letter_yaml", nargs="?", type=Path,
                    help="the letter content file (see ../cover_letters/_template.yaml)")
    ap.add_argument("--template", action="store_true",
                    help="build ../cover_letters/_template.yaml (the committed sample)")
    ap.add_argument("--out", type=Path,
                    help="output directory (default: next to the YAML)")
    ap.add_argument("--fonts", choices=sorted(brand.FONT_SETS), default="brand",
                    help="brand = Roboto/Montserrat; safe = installed substitutes")
    ap.add_argument("--pdf", action="store_true",
                    help="also export a PDF through Word (needs pywin32 + Word)")
    args = ap.parse_args(argv)

    if args.template:
        yaml_path = TEMPLATE_YAML
    elif args.letter_yaml:
        yaml_path = args.letter_yaml.resolve()
    else:
        ap.error("give a letter YAML, or --template")

    if not yaml_path.exists():
        print(f"  x {yaml_path} not found", file=sys.stderr)
        return 1

    fonts = brand.FONT_SETS[args.fonts]
    warn_missing_fonts(fonts)

    content = load(yaml_path)
    company = content["meta"].get("company", "")
    out_dir = (args.out.resolve() if args.out else yaml_path.parent)
    out = out_dir / f"Ryan_Hickey_Cover_Letter_{slugify(company)}.docx"

    written = build_cover_letter(content, out, fonts=fonts)
    print(f"  + {written.name}  ({written.stat().st_size / 1024:,.0f} KB)")

    if args.pdf:
        from export_pdf import export   # deferred: only this path needs pywin32
        pdf = written.with_suffix(".pdf")
        export([(written, pdf)])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
