#!/usr/bin/env python3
"""Compose the Wolfpack AI Command shield PRINT (wp-website #184 follow-on).

An allover tiled monogram of the approved shield hero, in the manner of a
luxury-bag print: the shield motif repeated on a staggered diamond grid over
exactly the hero's field (same 2100x1181 canvas, same radial navy background,
same vignette), with small four-point glints in the interstices the way a
monogram alternates its secondary marks. Motifs crop at the canvas edges, as
an allover print should. No text anywhere.

Everything geometric is imported from build_hero.py -- the shield path, the
icon paths (read from the committed notion-*.svg files), the hue set, and the
metal-band treatment -- so the print can never drift from the hero it tiles.
Ry's intended use: product support material, separate from the case study page.

Usage:
    python build_print.py [out.jpg]
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import time
from pathlib import Path

from PIL import Image

from build_hero import (
    H, HERE, ICONS, IMG, SX, TOP, BOT, W,
    find_edge, icon_path_d, shield_d,
)

CROSS_Y = 555
CENTER_Y = (TOP + BOT) / 2          # the motif's own vertical centre

# Tile layout: staggered rows, generous air, motifs cropping at the edges.
SCALE = 0.28
PITCH_X = 380
PITCH_Y = 330


def motif() -> str:
    """The approved shield, compacted for tile scale: band, plate, axes,
    icons. Halos, recess and drop shadow read as mud at 28% -- omitted."""
    icons = {n: icon_path_d(IMG / f) for n, f, _ in ICONS}
    colors = {n: c for n, _, c in ICONS}
    sd = shield_d()

    icon_size, qx, qy = 160, 158, 168
    positions = {
        "products": (SX - qx, CROSS_Y - qy),
        "projects": (SX + qx, CROSS_Y - qy),
        "tasks": (SX - qx, CROSS_Y + qy),
        "clients": (SX + qx, CROSS_Y + qy),
    }
    marks = []
    for n in ("products", "projects", "tasks", "clients"):
        cx, cy = positions[n]
        s = icon_size / 20.0
        tr = f'translate({cx - icon_size / 2} {cy - icon_size / 2}) scale({s})'
        marks.append(f'<g transform="{tr}"><path d="{icons[n]}" fill="{colors[n]}"/></g>')
    marks_svg = "\n    ".join(marks)

    return f"""<g id="motif" transform="translate({-SX} {-CENTER_Y})">
    <path d="{sd}" fill="none" stroke="#6E8CFF" stroke-width="30"
          filter="url(#rimglow)" opacity="0.55"/>
    <path d="{sd}" fill="url(#plate)"/>
    <g clip-path="url(#shieldclip)">
      <line x1="{SX}" y1="{TOP}" x2="{SX}" y2="{BOT}" stroke="#C8D6F5"
            stroke-width="4" opacity="0.8"/>
      <line x1="{SX - 340}" y1="{CROSS_Y}" x2="{SX + 340}" y2="{CROSS_Y}"
            stroke="#C8D6F5" stroke-width="4" opacity="0.8"/>
    </g>
    <path d="{sd}" fill="none" stroke="#EAF0FF" stroke-width="27" opacity="0.95"/>
    <path d="{sd}" fill="none" stroke="url(#rimmetal)" stroke-width="21"/>
    {marks_svg}
  </g>"""


def build_svg() -> str:
    uses, glints = [], []
    row = 0
    y = 60.0
    while y < H + PITCH_Y:
        x0 = 90 if row % 2 == 0 else 90 + PITCH_X / 2
        x = x0
        while x < W + PITCH_X:
            uses.append(
                f'<use href="#motif" transform="translate({x:.0f} {y:.0f}) '
                f'scale({SCALE})"/>'
            )
            # Interstitial glint, the print's secondary mark: centred in the
            # diamond between four neighbouring shields.
            gx, gy = x + PITCH_X / 2, y + PITCH_Y / 2
            glints.append(
                f'<path d="M {gx} {gy - 16} Q {gx + 2} {gy - 2} {gx + 16} {gy} '
                f'Q {gx + 2} {gy + 2} {gx} {gy + 16} '
                f'Q {gx - 2} {gy + 2} {gx - 16} {gy} '
                f'Q {gx - 2} {gy - 2} {gx} {gy - 16} Z" '
                f'fill="#8FA6E0" opacity="0.5" filter="url(#softglow)"/>'
            )
            x += PITCH_X
        y += PITCH_Y
        row += 1

    sd = shield_d()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"
     viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="field" cx="50%" cy="44%" r="75%">
      <stop offset="0%" stop-color="#0A1435"/>
      <stop offset="55%" stop-color="#071028"/>
      <stop offset="100%" stop-color="#03071A"/>
    </radialGradient>
    <linearGradient id="plate" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#111F4A"/>
      <stop offset="55%" stop-color="#0C1738"/>
      <stop offset="100%" stop-color="#081128"/>
    </linearGradient>
    <linearGradient id="rimmetal" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F0F4FF"/>
      <stop offset="30%" stop-color="#C2CEEC"/>
      <stop offset="55%" stop-color="#DDE6FA"/>
      <stop offset="100%" stop-color="#96A6CE"/>
    </linearGradient>
    <filter id="rimglow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="16"/>
    </filter>
    <filter id="softglow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="2.4"/>
    </filter>
    <clipPath id="shieldclip"><path d="{sd}"/></clipPath>
    <radialGradient id="vignette" cx="50%" cy="50%" r="72%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="78%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.55"/>
    </radialGradient>
    {motif()}
  </defs>

  <rect width="{W}" height="{H}" fill="url(#field)"/>
  {chr(10).join(uses)}
  {chr(10).join(glints)}
  <rect width="{W}" height="{H}" fill="url(#vignette)"/>
</svg>"""


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "wolfpack-ai-command-shield-print.jpg"
    svg = build_svg()
    svg_path = HERE / "print.svg"
    svg_path.write_text(svg, encoding="utf-8")

    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as td:
        host = Path(td) / "host.html"
        host.write_text(
            f"<!DOCTYPE html><html><head><style>*{{margin:0;padding:0}}"
            f"html,body{{overflow:hidden}}</style>"
            f"</head><body>{svg}</body></html>",
            encoding="utf-8",
        )
        png = Path(td) / "print.png"
        subprocess.run(
            [find_edge(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
             f"--user-data-dir={td}\\prof", f"--window-size={W},{H}",
             f"--screenshot={png}", host.as_uri()],
            check=False, capture_output=True,
        )
        for _ in range(20):
            if png.exists() and png.stat().st_size > 0:
                break
            time.sleep(0.5)
        if not png.exists():
            raise SystemExit("Edge produced no screenshot")
        im = Image.open(png).convert("RGB")
        if im.size != (W, H):
            im = im.crop((0, 0, W, H))
        im.save(out, "JPEG", quality=92, optimize=True)
    print(f"wrote {out} ({W}x{H}) and {svg_path}")


if __name__ == "__main__":
    main()
