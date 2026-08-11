#!/usr/bin/env python
"""Capture the transaction map for the case study's social card.

    python case_studies/consolidation_under_pressure/planning/card/capture_map.py

Writes `map-capture.png` beside this file. That capture is the inset
`social-cards/build_cards.py` composes into
`case-study-assets/img/og-consolidation-under-pressure.png`.

WHY A CAPTURE AND NOT THE PAGE ITSELF
-------------------------------------
The map is drawn in a browser from `map.js`, so there is no image of it sitting
anywhere to point a card at. A card needs a raster, and the honest way to get one
is to render the real page and photograph it — never to redraw an approximation
of the figure in Pillow, which is how a card and the thing it advertises quietly
stop being the same picture.

The generator lives under `planning/`, so it does not deploy; only the finished
card does. Same convention `ops_fin_model_support/planning/hero/build_hero.py`
carries: **rebuild rather than retouch.** If the map's data, palette or packing
changes, re-run this and then re-run `build_cards.py` — do not open the PNG in an
editor.

THE CROP IS DELIBERATE. It takes the 2020-2026 half of the plot, where the four
lanes are all populated and the pandemic band is visible behind them. The empty
left half is honest about the data and useless as a card: a LinkedIn Featured
tile renders at roughly 360px, at which point the inset is texture, and texture
made of blank lanes is a card that looks unfinished.

Needs Microsoft Edge or Google Chrome installed. Deterministic: fixed window
size, fixed scroll offset, no timestamps.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP_PAGE = (HERE.parent.parent / "transaction-map.html").resolve()
OUT = HERE / "map-capture.png"

# Wide enough that the plot spreads past its 1600px floor, tall enough that all
# four lanes and the year axis are in frame.
WIN_W, WIN_H = 2000, 1180
SCROLL_FRACTION = 0.46          # only bites if the plot is wider than the window

# The plot, trimmed out of the page it was rendered on. Everything above and
# below this box is page chrome — nav bar, headings, standfirst, footer — and a
# card whose inset shows a navigation bar reads as a screenshot of a website
# rather than as a picture of the work. Left/right/top/bottom in capture pixels.
CROP = (40, 58, 1972, 900)

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
]

# The map is loaded in an iframe rather than screenshotted directly, because the
# scroller has to be driven to SCROLL_FRACTION before the shot and there is no
# command-line flag for "scroll this element".
HARNESS = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
  html,body{{margin:0;background:#000B29;overflow:hidden}}
  iframe{{border:0;display:block}}
</style></head><body>
<iframe id="f" src="{url}" width="{w}" height="{h}"></iframe>
<script>
var f = document.getElementById('f');
f.onload = function(){{
  setTimeout(function(){{
    var d = f.contentDocument;
    var s = d.querySelector('.map__scroll');
    if (s) s.scrollLeft = (s.scrollWidth - s.clientWidth) * {frac};
    // Lift the figure to the top of the frame so the crop is all plot.
    var fig = d.querySelector('.figframe');
    if (fig) fig.scrollIntoView({{block: 'start'}});
    d.documentElement.style.scrollBehavior = 'auto';
    d.defaultView.scrollBy(0, -14);
  }}, 350);
}};
</script></body></html>
"""


def find_browser() -> str:
    for candidate in BROWSERS:
        if Path(candidate).is_file():
            return candidate
    sys.exit("no Chromium-based browser found — edit BROWSERS in this file")


def main() -> int:
    if not MAP_PAGE.is_file():
        sys.exit(f"missing {MAP_PAGE}")

    browser = find_browser()
    with tempfile.TemporaryDirectory() as tmp:
        harness = Path(tmp) / "capture.html"
        harness.write_text(
            HARNESS.format(
                url=MAP_PAGE.as_uri(), w=WIN_W, h=WIN_H, frac=SCROLL_FRACTION
            ),
            encoding="utf-8",
        )
        subprocess.run(
            [
                browser,
                "--headless=new",
                "--disable-gpu",
                "--allow-file-access-from-files",
                "--hide-scrollbars",
                f"--window-size={WIN_W},{WIN_H}",
                "--virtual-time-budget=8000",
                f"--screenshot={OUT}",
                harness.as_uri(),
            ],
            check=True,
            capture_output=True,
        )

    if not OUT.is_file():
        sys.exit("the browser produced no screenshot")

    # Pillow only for the crop. It is already a dependency of build_cards.py,
    # which is the only consumer of this file.
    from PIL import Image

    with Image.open(OUT) as shot:
        shot.load()
        cropped = shot.crop(CROP)
    cropped.save(OUT)

    print(f"wrote {OUT}  {cropped.width}x{cropped.height}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
