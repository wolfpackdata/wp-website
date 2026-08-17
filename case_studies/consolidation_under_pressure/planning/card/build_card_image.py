#!/usr/bin/env python
"""Compose this case study's CARD image from the transaction map capture.

    python case_studies/consolidation_under_pressure/planning/card/build_card_image.py

Writes `hire/assets/img/case-consolidation.jpg` — the 16:9 image the two hire/
pages' case card shows (wp-website#218). It is a sibling of `capture_map.py`,
which produces the `map-capture.png` this reads, and it deliberately does not
touch that file.

WHY THIS EXISTS AT ALL
----------------------
The other three case cards take their image from the case study's own hero.
This one cannot: Consolidation Under Pressure ships **no hero figure on the
page**, by Ry's ruling of 2026-08-16, and its supplied hero art is blog eye
candy whose only public surface is the blog post's cover. So the card needs an
image that is genuinely *of this case study*, and the transaction map is the
page's signature figure — 42 events across four lanes, the one thing a reader
remembers about the document.

Provenance, per `case_studies/README.md`: this is the GENERATED pattern. The
master is `capture_map.py` plus the page it photographs; `map-capture.png` is
its output and this script's input; this file is the recorded derivation. If the
map's data, palette or packing changes, re-run `capture_map.py` and then re-run
this. **Rebuild rather than retouch** — do not open the JPEG in an editor.

THE COMPOSITION, AND THE TWO IT BEAT
------------------------------------
The card frame is 300px wide (`.case__shot`, 16:9, `object-fit: cover`), at which
size every label in this figure is texture rather than text. That is true of the
two sibling cards as well, so the question is not legibility — it is whether the
tile reads as a deliberate figure or as a screenshot someone cropped badly.

What ships: the WHOLE plot, scaled to the card's width and centered on the
figure's own ground. All four lane bands, their labels, the year axis and the
value legend survive, so the tile reads as a wide timeline chart, which is what
it is.

Rejected, and why, so neither gets re-proposed:

  * **The full capture, uncropped.** Carries the map page's heading and its
    three lines of standfirst copy above the plot. At card scale that is a
    blurred grey smear that reads as a rendering fault.
  * **A cover-crop of the dense 2020-2026 half** — the crop `capture_map.py`
    uses for the social card, and correct there. Here it slices the lane labels
    off the left edge, taking the figure's category axis with them, and it cuts
    the standfirst mid-word along the top. A card whose art is a sentence
    chopped in half looks like a mistake regardless of how dense the rest is.

Deterministic: fixed crop, fixed output size, fixed quality, no timestamps.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]

SRC = HERE / "map-capture.png"
OUT = REPO / "hire" / "assets" / "img" / "case-consolidation.jpg"

# Card width and 16:9, matching portfolio/img/case-fin-model.jpg (1400x788) and
# case-ai-command.jpg (1400x787) — the two images this one sits beside.
CARD_W, CARD_H = 1400, 788

# Everything above this row in the capture is the map PAGE's copy — its heading
# and standfirst — not the figure. The first lane band begins just below it.
PLOT_TOP = 124

# Matches the siblings closely enough that the three cards carry no visible
# difference in encoding. Verified: no banding in the lane bands at card scale.
QUALITY = 90


def main() -> int:
    src = Image.open(SRC).convert("RGB")
    plot = src.crop((0, PLOT_TOP, src.width, src.height))

    scaled = plot.resize(
        (CARD_W, round(CARD_W * plot.height / plot.width)), Image.LANCZOS
    )

    # The pad color is sampled from the capture rather than hardcoded, so the
    # letterbox cannot drift away from --fig-bg if that variable ever moves.
    card = Image.new("RGB", (CARD_W, CARD_H), src.getpixel((5, 5)))
    card.paste(scaled, (0, (CARD_H - scaled.height) // 2))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    card.save(OUT, "JPEG", quality=QUALITY, optimize=True)
    print(f"wrote {OUT.relative_to(REPO)}  {CARD_W}x{CARD_H}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
