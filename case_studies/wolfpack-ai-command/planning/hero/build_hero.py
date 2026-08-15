#!/usr/bin/env python3
"""Compose the Wolfpack AI Command shield hero (wp-website #184).

A bold heater shield on a deep navy field, holding the four Notion database
icons in a 2x2 grid separated by X-Y axis hairlines. Reading order matches the
workspace-layer section of the page: Products (top-left), Projects (top-right),
Tasks (bottom-left), Clients (bottom-right). The icons keep their native Notion
hues -- Ry's ruling, 2026-08-15: the colors are the semantic system the page's
F6 figure already shows as figure content. No text anywhere on the graphic.

Style references: the constellation-engraving look of
blog_posts/2026-08-05-five-projects/cover.jpg (luminous line-work, glints,
perspective grid floor) and the connection traces of
portfolio/img/app-data-backbone.jpg.

The four icon paths are read from the committed SVGs in
case-study-assets/img/ (notion- prefix) so the hero can never drift from the
icons the page itself shows. If an icon changes in Notion, re-fetch the SVG
and re-run this script -- rebuild rather than retouch.

PLACEMENT IS RULED (Ry, 2026-08-15, outline D-021): the image is the case
study's hero figure, between the stat tiles and the document metadata. So the
default output is now the deployed path, case-study-assets/img/, and the
planning copy was deleted rather than kept in parallel -- one artifact, one
home. The build is deterministic: re-running it reproduced the approved JPEG
byte for byte (sha256 14f494c0...92d65c) before the embed landed, which is what
makes "rebuild rather than retouch" a safe instruction rather than a risky one.
planning/ itself still never deploys; only the finished image does.

Usage:
    python build_hero.py [out.jpg]      # default: the deployed asset path

Requires: Pillow, and Microsoft Edge for the headless SVG render at
2100x1181 (the ops_fin hero's dimensions).
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from PIL import Image

W, H = 2100, 1181
HERE = Path(__file__).resolve().parent
IMG = HERE / ".." / ".." / ".." / "case-study-assets" / "img"

# Reading order of the grid: TL, TR, BL, BR.
ICONS = [
    ("products", "notion-triangle-alternate_green.svg", "#448361"),
    ("projects", "notion-iterate_blue.svg", "#337ea9"),
    ("tasks", "notion-grid-wide-six_orange.svg", "#d9730d"),
    ("clients", "notion-meeting_brown.svg", "#9F6B53"),
]

# Shield geometry (canvas coordinates). Centre column x=1050.
SX, TOP, BOT = 1050, 205, 1000     # centre x, top edge y, tip y
HALF = 340                          # half-width at the shoulders
WAIST = 590                         # y where the sides start tapering


def icon_path_d(svg_file: Path) -> str:
    """Pull the path data out of a committed Notion icon SVG."""
    m = re.search(r'<path d="([^"]+)"', svg_file.read_text(encoding="utf-8"))
    if not m:
        raise SystemExit(f"no <path d=...> in {svg_file}")
    return m.group(1)


def shield_d() -> str:
    l, r = SX - HALF, SX + HALF
    return (
        f"M {l} {TOP + 55} "
        f"Q {l} {TOP} {l + 60} {TOP} "
        f"L {r - 60} {TOP} "
        f"Q {r} {TOP} {r} {TOP + 55} "
        f"L {r} {WAIST} "
        f"Q {r} {820} {SX} {BOT} "
        f"Q {l} {820} {l} {WAIST} Z"
    )


def glint(x: float, y: float, r: float, opacity: float) -> str:
    """A four-point star sparkle, the cover.jpg signature."""
    return (
        f'<path d="M {x} {y - r} Q {x + r * 0.12} {y - r * 0.12} {x + r} {y} '
        f'Q {x + r * 0.12} {y + r * 0.12} {x} {y + r} '
        f'Q {x - r * 0.12} {y + r * 0.12} {x - r} {y} '
        f'Q {x - r * 0.12} {y - r * 0.12} {x} {y - r} Z" '
        f'fill="#EAF0FF" opacity="{opacity}" filter="url(#softglow)"/>'
    )


def grid_floor() -> str:
    """Perspective grid floor under the shield, converging on the tip."""
    vx, vy, horizon = SX, 830, 905
    parts = []
    for i in range(-10, 11):
        x_far = vx + i * 300
        parts.append(
            f'<line x1="{vx + i * 90}" y1="{horizon}" x2="{x_far}" y2="{H}" '
            f'stroke="#3A4C86" stroke-width="1.5" opacity="0.16"/>'
        )
    y = horizon
    step = 14.0
    while y < H:
        parts.append(
            f'<line x1="0" y1="{y:.0f}" x2="{W}" y2="{y:.0f}" '
            f'stroke="#3A4C86" stroke-width="1.5" opacity="0.14"/>'
        )
        y += step
        step *= 1.45
    return "\n".join(parts)


def traces() -> str:
    """Backbone-style connection traces feeding the shield from both sides."""
    parts = []
    for y, x_in, x_out in ((430, SX - HALF - 12, 150), (560, SX - HALF - 4, 110),
                           (690, SX - HALF - 26, 190)):
        for sgn in (1, -1):
            a = SX + sgn * (SX - x_in)
            b = SX + sgn * (SX - x_out)
            parts.append(
                f'<line x1="{a}" y1="{y}" x2="{b}" y2="{y}" '
                f'stroke="#4A5C96" stroke-width="2" opacity="0.35"/>'
            )
            parts.append(
                f'<circle cx="{b}" cy="{y}" r="5" fill="none" '
                f'stroke="#7E92C8" stroke-width="2" opacity="0.5"/>'
            )
            parts.append(
                f'<circle cx="{(a + b) / 2}" cy="{y}" r="3" fill="#9FB4E8" '
                f'opacity="0.45"/>'
            )
    return "\n".join(parts)


def icon_halo(color: str, cx: float, cy: float, size: float) -> str:
    """The soft colored pool behind an icon. Emitted inside the shield clip so
    no glow leaks past the border — the armor contains the light."""
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{size * 0.78}" fill="{color}" '
        f'opacity="0.10" filter="url(#halo)"/>'
    )


def icon_group(name: str, d: str, color: str, cx: float, cy: float,
               size: float) -> str:
    """One icon: blurred color glow, then the sharp mark."""
    s = size / 20.0
    tx, ty = cx - size / 2, cy - size / 2
    tr = f'translate({tx} {ty}) scale({s})'
    return f"""
  <g transform="{tr}" filter="url(#iconglow)" opacity="0.85">
    <path d="{d}" fill="{color}"/>
  </g>
  <g transform="{tr}">
    <path d="{d}" fill="{color}"/>
  </g>
  <g transform="{tr}" opacity="0.35">
    <path d="{d}" fill="#FFFFFF" filter="url(#iconedge)"/>
  </g>"""


def build_svg() -> str:
    icons = {n: icon_path_d(IMG / f) for n, f, _ in ICONS}
    colors = {n: c for n, _, c in ICONS}
    sd = shield_d()

    # Icon scale and quadrant offsets leave clear margin between each icon,
    # the axes, and the rim band (#184 iteration 2: more air inside the plate).
    icon_size = 160
    qx, qy = 158, 168                     # quadrant offsets from the cross
    cross_y = 555
    positions = {
        "products": (SX - qx, cross_y - qy),
        "projects": (SX + qx, cross_y - qy),
        "tasks": (SX - qx, cross_y + qy),
        "clients": (SX + qx, cross_y + qy),
    }

    order = ("products", "projects", "tasks", "clients")
    halo_svg = "\n".join(
        icon_halo(colors[n], *positions[n], icon_size) for n in order
    )
    icon_svg = "\n".join(
        icon_group(n, icons[n], colors[n], *positions[n], icon_size)
        for n in order
    )

    corner = 60
    corners = "\n".join(
        f'<path d="M {x} {y + dy * corner} L {x} {y} L {x + dx * corner} {y}" '
        f'fill="none" stroke="#4A5A8E" stroke-width="2" opacity="0.5"/>'
        for x, y, dx, dy in (
            (70, 60, 1, 1), (W - 70, 60, -1, 1),
            (70, H - 60, 1, -1), (W - 70, H - 60, -1, -1),
        )
    )

    glints = "\n".join([
        glint(SX, TOP - 4, 30, 0.9),                 # crown of the shield
        glint(SX - HALF, WAIST, 22, 0.7),            # left shoulder-taper
        glint(SX + HALF, WAIST, 22, 0.7),            # right shoulder-taper
        glint(SX, BOT + 2, 24, 0.8),                 # the tip
        glint(SX, cross_y, 18, 0.9),                 # cross intersection
        glint(330, 210, 14, 0.5),
        glint(1815, 285, 12, 0.5),
        glint(245, 800, 10, 0.4),
        glint(1900, 760, 12, 0.4),
    ])

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
    <radialGradient id="crownlight" cx="50%" cy="0%" r="80%">
      <stop offset="0%" stop-color="#8FA6E0" stop-opacity="0.28"/>
      <stop offset="45%" stop-color="#8FA6E0" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#8FA6E0" stop-opacity="0"/>
    </radialGradient>
    <!-- The rim band's brushed-steel read: lit from above, darker toward the
         tip, with a mid-band sheen. Blue-leaning grays only - no new hue. -->
    <linearGradient id="rimmetal" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F0F4FF"/>
      <stop offset="30%" stop-color="#C2CEEC"/>
      <stop offset="55%" stop-color="#DDE6FA"/>
      <stop offset="100%" stop-color="#96A6CE"/>
    </linearGradient>
    <filter id="dropshadow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="26"/>
    </filter>
    <filter id="recess" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="5"/>
    </filter>
    <filter id="rimglow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="16"/>
    </filter>
    <filter id="axisglow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="6"/>
    </filter>
    <filter id="iconglow" x="-120%" y="-120%" width="340%" height="340%">
      <feGaussianBlur stdDeviation="13"/>
    </filter>
    <filter id="iconedge" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="1.1"/>
    </filter>
    <filter id="halo" x="-200%" y="-200%" width="500%" height="500%">
      <feGaussianBlur stdDeviation="34"/>
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
  </defs>

  <rect width="{W}" height="{H}" fill="url(#field)"/>
  {grid_floor()}
  {corners}
  {traces()}

  <!-- Shield. Iteration 2 (#184): the rim is a forged BAND, not a line -
       a wide brushed-steel stroke with thin specular edges on both sides,
       a soft recess shadow where the plate sits behind it, and a grounded
       drop shadow underneath. The plate fill and its transparency are
       untouched from iteration 1 (Ry: colors and transparency are right). -->
  <path d="{sd}" fill="#01040F" opacity="0.55" filter="url(#dropshadow)"
        transform="translate(14 24)"/>
  <path d="{sd}" fill="none" stroke="#6E8CFF" stroke-width="30"
        filter="url(#rimglow)" opacity="0.75"/>
  <path d="{sd}" fill="url(#plate)"/>
  <g clip-path="url(#shieldclip)">
    <rect x="{SX - HALF}" y="{TOP}" width="{HALF * 2}" height="330"
          fill="url(#crownlight)"/>
    {halo_svg}
    <!-- Recess: the plate reads as set back behind the rim band. -->
    <path d="{sd}" fill="none" stroke="#010613" stroke-width="12"
          filter="url(#recess)" opacity="0.55"
          transform="translate({SX} {cross_y}) scale(0.966) translate({-SX} {-cross_y})"/>
  </g>
  <!-- Band: light underlay wider than the metal stroke leaves a specular
       hairline on both edges of the band. -->
  <path d="{sd}" fill="none" stroke="#EAF0FF" stroke-width="27" opacity="0.95"/>
  <path d="{sd}" fill="none" stroke="url(#rimmetal)" stroke-width="21"/>
  <path d="{sd}" fill="none" stroke="#0A1330" stroke-width="1.5" opacity="0.35"
        transform="translate({SX} {cross_y}) scale(1.002) translate({-SX} {-cross_y})"/>
  <path d="{sd}" fill="none" stroke="#5F76B8" stroke-width="3"
        transform="translate({SX} {cross_y}) scale(0.94) translate({-SX} {-cross_y})"
        opacity="0.75"/>

  <!-- X-Y axes, clipped to the plate. -->
  <g clip-path="url(#shieldclip)">
    <line x1="{SX}" y1="{TOP}" x2="{SX}" y2="{BOT}" stroke="#9FB4E8"
          stroke-width="7" opacity="0.5" filter="url(#axisglow)"/>
    <line x1="{SX - HALF}" y1="{cross_y}" x2="{SX + HALF}" y2="{cross_y}"
          stroke="#9FB4E8" stroke-width="7" opacity="0.5"
          filter="url(#axisglow)"/>
    <line x1="{SX}" y1="{TOP}" x2="{SX}" y2="{BOT}" stroke="#C8D6F5"
          stroke-width="2.5" opacity="0.9"/>
    <line x1="{SX - HALF}" y1="{cross_y}" x2="{SX + HALF}" y2="{cross_y}"
          stroke="#C8D6F5" stroke-width="2.5" opacity="0.9"/>
  </g>

  {icon_svg}
  {glints}

  <rect width="{W}" height="{H}" fill="url(#vignette)"/>
</svg>"""


def find_edge() -> str:
    for env in ("ProgramFiles(x86)", "ProgramFiles"):
        base = os.environ.get(env)
        if base:
            p = Path(base) / "Microsoft" / "Edge" / "Application" / "msedge.exe"
            if p.exists():
                return str(p)
    raise SystemExit("msedge.exe not found")


def main() -> None:
    out = (Path(sys.argv[1]) if len(sys.argv) > 1
           else IMG / "wolfpack-ai-command-shield-hero.jpg")
    svg = build_svg()
    svg_path = HERE / "hero.svg"
    svg_path.write_text(svg, encoding="utf-8")

    # ignore_cleanup_errors: Edge can hold profile files open for a beat after
    # the screenshot lands, and a locked temp file must not fail the build.
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as td:
        host = Path(td) / "host.html"
        host.write_text(
            f"<!DOCTYPE html><html><head><style>*{{margin:0;padding:0}}"
            f"html,body{{overflow:hidden}}</style>"
            f"</head><body>{svg}</body></html>",
            encoding="utf-8",
        )
        png = Path(td) / "hero.png"
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
