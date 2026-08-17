#!/usr/bin/env python
"""Derive every published size of this case study's hero from the supplied master.

    python case_studies/consolidation_under_pressure/planning/hero/build_hero.py

Writes three files, all from one source image and none from each other:

    case-study-assets/img/consolidation-under-pressure-hero.jpg   1672x941  the page hero
    portfolio/img/case-consolidation.jpg                          1400x788  the portfolio card
    hire/assets/img/case-consolidation.jpg                        1400x788  the two hire cards

PROVENANCE: SUPPLIED, NOT GENERATED — and this script is the *derivation*, not
the art. `case_studies/README.md` names two first-class provenances; this is the
supplied one. The master is

    planning/hero/consolidation-under-pressure-hero-blue-neon.png

delivered by Ry on 2026-08-17 (1672x941, RGB), and it is the file that must
never be lost or edited in place. Everything above is re-derivable from it by
running this script, which is what "derivatives record the derivation command"
means for supplied art. Do not open any output in an editor.

DO NOT CONFUSE THE TWO MASTERS IN THIS CASE STUDY'S `planning/`.

    planning/consolidation-under-pressure-hero.png            the BLOG post's cover
    planning/hero/consolidation-under-pressure-hero-blue-neon.png   THIS, the page hero

The first is the blue-tree art Ry supplied on 2026-08-15. On 2026-08-16 he ruled
it was blog eye candy and that the case study page would ship no hero figure at
all. **That ruling was reversed on 2026-08-17** (wp-website#226) when he
commissioned and supplied the art this script reads — which is not decorative:
it shows twelve of the named companies being drawn into a single core beside a
declining market-share panel, which is the report's argument in one frame. The
tree remains the blog cover and keeps its own name; neither file replaces the
other.

NOTHING IS UPSCALED. The master is 1672x941 and the page hero ships at exactly
that size — no resample at all, just a JPEG encode. Its two sibling case studies
ship 2100px heroes, and matching that number would mean inventing 26% more
pixels than the master contains, which buys sharpness that is not in the source.
The figure renders at roughly 1040 CSS px, so 1672 is still better than 1.6x on
a retina display, and this is a dark render rather than a screenshot full of
6px type. Ship what exists.

The card size is a clean downscale: 1400x788 is 1.7766:1 against the master's
1.7768:1, so there is no crop and no letterbox — the whole frame survives, which
matters here because the composition reads left-to-right (brands, core, chart)
and cropping either end would remove half the argument.

Deterministic: fixed sizes, fixed quality, no timestamps.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]

SRC = HERE / "consolidation-under-pressure-hero-blue-neon.png"

# (path, width) — height is derived so the aspect ratio is never altered.
# None means "ship the master's own pixels", which only the page hero does.
OUTPUTS = [
    (REPO / "case_studies" / "case-study-assets" / "img"
          / "consolidation-under-pressure-hero.jpg", None),
    (REPO / "portfolio" / "img" / "case-consolidation.jpg", 1400),
    (REPO / "hire" / "assets" / "img" / "case-consolidation.jpg", 1400),
]

# Matches the two sibling heroes closely enough that the four case studies carry
# no visible difference in encoding. Checked at 100% for ringing on the neon
# edges, which is where a dark render with bright thin strokes shows it first.
QUALITY = 90


def main() -> int:
    master = Image.open(SRC).convert("RGB")

    for out, width in OUTPUTS:
        if width is None or width == master.width:
            img = master
        else:
            if width > master.width:
                raise SystemExit(
                    f"refusing to upscale {out.name}: {width}px requested from a "
                    f"{master.width}px master — see this file's header"
                )
            img = master.resize(
                (width, round(width * master.height / master.width)), Image.LANCZOS
            )
        out.parent.mkdir(parents=True, exist_ok=True)
        img.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        kb = out.stat().st_size / 1024
        print(f"wrote {out.relative_to(REPO)}  {img.width}x{img.height}  {kb:.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
