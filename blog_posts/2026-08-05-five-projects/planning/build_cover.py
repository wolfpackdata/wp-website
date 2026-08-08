"""
Build the hero image for the "five projects" blog post.

    python build_cover.py <out.jpg> [out_width]

The composition is a holographic projection deck: five constellation glyphs, one
per project, standing in a row above five columns of light whose heights are the
commit counts of the last thirty days. The glyph row is deliberately level --
all five are peers, which is the premise of the post -- so the only thing that
varies is the light under them.

The constellation vocabulary is not invented here. The Wolfpack mark is a wolf
drawn as a star chart: thin segments between nodes, four-point sparkles on the
nodes that carry the drawing. Every glyph below is built the same way, from a
node-and-edge list rather than a traced path, so the five marks are a family by
construction. That is also what supplies the futurism without a new visual
language: a star chart already reads as an instrument display.

Palette discipline follows case-study.css. Navy system only, plus the same
LIGHT_EDGE tint (#7C93D6) the beacon hero introduced for light in the navy
family. Coral appears once, as the deck baseline, mirroring .hero__stand's
border-bottom the way build_hero.py's rule does.

Text is set in the repo's own fonts, embedded as base64 so the render does not
depend on anything installed on the machine. The mono readouts use the --mono
stack from case-study.css and land on Consolas here.

Rendering is a two-stage pass. Chrome draws the SVG, because only a browser can
set the repo's woff2 faces and resolve the glow filters predictably; PIL then
adds the grain and vignette, because a gradient this wide bands without them.
"""

import base64
import io
import pathlib
import re
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

W, H = 2400, 1350                     # 16:9, same frame as the beacon hero

# Resolved from this file rather than from the working directory, so the
# generator runs from anywhere and from a fresh clone on any machine.
REPO = pathlib.Path(__file__).resolve().parents[3]
ASSETS = REPO / "case_studies" / "case-study-assets"

BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def browser():
    for path in BROWSERS:
        if pathlib.Path(path).exists():
            return path
    raise SystemExit("no Chrome or Edge found; both render this identically")

# --- colors, straight from case-study.css ----------------------------------
NAVY_TOP = "#000516"
NAVY_MID = "#000B29"                  # --navy
NAVY_BOT = "#000411"
CORAL    = "#F95954"                  # --coral, one use: the deck baseline
WHITE    = "#FFFFFF"
MUTED    = "#BFC2CA"                  # --muted
FAINT    = "#808594"                  # --faint, labels only
LINE     = "#222E52"                  # --line
LIGHT_CORE = "#FFF4F1"                # white carrying a trace of coral
LIGHT_EDGE = "#7C93D6"                # a tint of navy, not a new hue

# ==========================================================================
# The data. Measured, not estimated: every number is `git log --all --since`
# over the thirty days ending 2026-08-05, with node_modules, dist, release
# runtimes, lockfiles, minified bundles and binary assets excluded from the
# file counts. Repos are grouped where one project spans several.
# ==========================================================================

PROJECTS = [
    dict(name="SETMASTER 3",          commits=192, files=362, days=11, glyph="transition"),
    dict(name="GITHUB + NOTION SOP",  commits=49,  files=70,  days=11, glyph="sop"),
    dict(name="PDPD",                 commits=82,  files=709, days=12, glyph="lattice"),
    dict(name="WOLFPACK WEBSITE",     commits=169, files=151, days=10, glyph="sheets"),
    dict(name="AI COACHING",          commits=36,  files=59,  days=4,  glyph="transfer"),
]

TOTAL = sum(p["commits"] for p in PROJECTS)

# --- layout ----------------------------------------------------------------
COLS = [380, 790, 1200, 1610, 2020]   # column centers, 410 apart
GLYPH_CY = 372                        # every glyph centered here: the row is level
GLYPH_BOX = 200                       # glyphs are drawn in a 200x200 box
NAME_Y = 548
META_Y = 586
DROP_Y = 630                          # where the dashed run to the cap starts
BAR_BASE = 1068                       # the deck: where columns meet the floor
BAR_W = 58
DECK_X0, DECK_X1 = 132, 2268

# The scale tops out at a round 200 rather than at the tallest column, so the
# axis carries labelled ticks and the columns are read against a ruler instead
# of only against each other. 192 lands just under the top tick, which is true.
SCALE_MAX = 200
SCALE_H = 330                         # pixels for those 200 commits
AXIS_X = 198


def bar_h(commits):
    return SCALE_H * commits / SCALE_MAX


# ==========================================================================
# Constellation glyphs
#
# Each is (edges, nodes, sparkles) in its own 200x200 space. Edges are
# polylines; nodes are (x, y, radius); sparkles are (x, y, arm) four-point
# stars, used only on the node that carries the drawing's meaning. Opacity on
# an edge or node is how a glyph shows depth without a second color.
# ==========================================================================

def glyph_transition():
    """SetMaster 3 -- two program lines crossing at the transition.

    The set editor's whole subject is the row where one track leaves and the
    next arrives, so the mark is that crossing and nothing else. The three
    ticks under it are transition rows.
    """
    out_line = [(14, 46), (58, 60), (100, 100), (142, 140), (186, 154)]
    in_line = [(14, 154), (58, 140), (100, 100), (142, 60), (186, 46)]
    edges = [(out_line, 1.0), (in_line, 0.72)]
    nodes = [(x, y, 3.0, 0.85) for x, y in out_line + in_line if (x, y) != (100, 100)]
    nodes.append((100, 100, 5.4, 1.0))
    for y in (172, 182, 192):                    # the transition rows themselves
        edges.append(([(62, y), (138, y)], 0.38))
    return edges, nodes, [(100, 100, 24)]


def glyph_sop():
    """GitHub + Notion SOP -- a branch and a document, held together.

    Two systems, one procedure between them. The fork is the repo, the ruled
    rectangle is the page, and the segmented span is the link the SOP makes.
    The bright node sits on the link, not on either system, because the
    procedure is the thing that was built.
    """
    edges = [
        ([(48, 172), (48, 104)], 1.0),          # trunk
        ([(48, 104), (18, 54)], 0.85),          # branch left
        ([(48, 104), (78, 54)], 0.85),          # branch right
        ([(124, 44), (182, 44), (182, 160), (124, 160), (124, 44)], 0.95),
    ]
    nodes = [(48, 172, 3.2, 0.8), (48, 104, 4.6, 1.0), (18, 54, 3.6, 0.9),
             (78, 54, 3.6, 0.9)]
    for cx, cy in ((124, 44), (182, 44), (182, 160), (124, 160)):
        nodes.append((cx, cy, 3.0, 0.85))
    for ry in (76, 102, 128):                    # ruled lines inside the page
        edges.append(([(138, ry), (168, ry)], 0.5))
        nodes.append((138, ry, 2.2, 0.55))
    edges += [([(86, 100), (94, 100)], 0.6), ([(108, 100), (116, 100)], 0.6)]
    nodes.append((101, 100, 4.6, 1.0))
    return edges, nodes, [(101, 100, 17)]


def glyph_lattice():
    """pdpd -- the catalog, and the one page being operated on.

    A product catalog that runs to millions of pages is a lattice that does not
    end at the frame, so the rules stop short of the box and the outer nodes
    fade rather than terminate. One node is lit and ringed: the page the tool is
    working, which is the product's whole claim.
    """
    xs = [16, 48, 80, 112, 144, 176]
    ys = [30, 62, 94, 126, 158]
    lit = (80, 94)
    edges, nodes = [], []
    for y in ys:
        edges.append(([(xs[0] - 8, y), (xs[-1] + 8, y)], 0.2))
    for x in xs:
        edges.append(([(x, ys[0] - 8), (x, ys[-1] + 8)], 0.2))
    for x in xs:
        for y in ys:
            if (x, y) == lit:
                continue
            # fade toward the edges, so the lattice reads as continuing past
            # the frame instead of being a five-by-six grid of anything
            d = (min(abs(x - 96) / 80.0, 1.0) * 0.6
                 + min(abs(y - 94) / 64.0, 1.0) * 0.4)
            nodes.append((x, y, 2.6, max(0.16, 0.9 - d)))
    nodes.append((lit[0], lit[1], 5.0, 1.0))
    # four short rays off the lit node: the operations the tool runs on a page
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        edges.append(([(lit[0] + dx * 27, lit[1] + dy * 27),
                       (lit[0] + dx * 34, lit[1] + dy * 34)], 0.75))
    return edges, nodes, [(lit[0], lit[1], 15)], (lit[0], lit[1], 22)


def glyph_sheets():
    """Wolfpack website -- pages stacked, newest on top.

    Landing pages, case studies and blog posts are one body of work in layers,
    so the mark is three planes in the same plan view, the top one lit. The
    verticals are what makes it a stack instead of three separate diamonds.
    """
    edges, nodes = [], []
    plates = [(58, 1.0), (104, 0.62), (150, 0.4)]
    for cy, op in plates:
        pts = [(100, cy - 30), (160, cy), (100, cy + 30), (40, cy), (100, cy - 30)]
        edges.append((pts, op))
        for x, y in pts[:4]:
            nodes.append((x, y, 3.0, op * 0.95))
    for x in (40, 160):                          # the stack's own edges
        edges.append(([(x, 58), (x, 150)], 0.3))
    return edges, nodes, [(100, 28, 22)]


def glyph_transfer():
    """AI coaching -- one source, several people, and what passes between.

    Coaching is a transfer, so the mark is a source node with a ring and a fan
    of receivers chained to each other. The receivers are connected because a
    cohort teaches itself once it has the method.
    """
    src = (52, 100)
    recv = [(152, 40), (180, 80), (180, 124), (152, 164)]
    edges = [([src, r], 0.7 - i * 0.05) for i, r in enumerate(recv)]
    edges.append((recv, 0.42))                   # the cohort, chained
    nodes = [(src[0], src[1], 4.6, 1.0)] + [(x, y, 3.4, 0.9) for x, y in recv]
    nodes += [(24, 72, 2.0, 0.45), (26, 130, 2.0, 0.45)]
    return edges, nodes, [(src[0], src[1], 17)], (src[0], src[1], 21)


GLYPHS = {
    "transition": glyph_transition,
    "sop": glyph_sop,
    "lattice": glyph_lattice,
    "sheets": glyph_sheets,
    "transfer": glyph_transfer,
}


def render_glyph(kind, cx, cy):
    """Emit one glyph, translated so its 200x200 box is centered on (cx, cy)."""
    result = GLYPHS[kind]()
    edges, nodes, sparks = result[0], result[1], result[2]
    ring = result[3] if len(result) > 3 else None

    ox, oy = cx - GLYPH_BOX / 2, cy - GLYPH_BOX / 2
    out = [f'<g transform="translate({ox:.1f},{oy:.1f})" filter="url(#glyphGlow)">']

    if ring:
        rx, ry, rr = ring
        out.append(f'<circle cx="{rx}" cy="{ry}" r="{rr}" fill="none" '
                   f'stroke="{LIGHT_EDGE}" stroke-width="1.4" opacity="0.55"/>')

    for pts, op in edges:
        if op <= 0:
            continue
        d = " ".join(f"{x},{y}" for x, y in pts)
        out.append(f'<polyline points="{d}" fill="none" stroke="{LIGHT_EDGE}" '
                   f'stroke-width="1.9" stroke-linecap="round" '
                   f'stroke-linejoin="round" opacity="{op:.2f}"/>')

    for x, y, r, op in nodes:
        # every node is a soft disc with a hard bright center, which is how the
        # wolf mark's stars read at small sizes
        out.append(f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="{LIGHT_EDGE}" '
                   f'opacity="{op * 0.55:.2f}"/>')
        out.append(f'<circle cx="{x}" cy="{y}" r="{r * 0.45:.1f}" '
                   f'fill="{LIGHT_CORE}" opacity="{op:.2f}"/>')

    for x, y, arm in sparks:
        # four-point star: two tapered quads, the wolf mark's own sparkle
        out.append(
            f'<path d="M{x},{y - arm} L{x + arm * 0.16},{y} L{x},{y + arm} '
            f'L{x - arm * 0.16},{y} Z" fill="{LIGHT_CORE}" opacity="0.9"/>')
        out.append(
            f'<path d="M{x - arm},{y} L{x},{y - arm * 0.16} L{x + arm},{y} '
            f'L{x},{y + arm * 0.16} Z" fill="{LIGHT_CORE}" opacity="0.9"/>')

    out.append("</g>")
    return "\n".join(out)


# ==========================================================================
# The deck, the columns, and the type
# ==========================================================================

def render_floor():
    """Perspective floor below the baseline.

    The vanishing point sits on the baseline at frame center, so the deck reads
    as a plane the columns stand on rather than as a gradient behind them.
    Spacing of the horizontals grows geometrically going down, which is what
    makes it a floor and not a ladder.
    """
    vx, vy = W / 2, BAR_BASE
    out = ['<g>']
    for i in range(-16, 17):                     # rays fanning from the VP
        if i == 0:
            continue
        fx = vx + i * 290
        op = 0.85 * (1 - min(abs(i) / 18.0, 1.0) * 0.6)
        out.append(f'<line x1="{vx}" y1="{vy}" x2="{fx:.0f}" y2="{H}" '
                   f'stroke="{LINE}" stroke-width="1.7" opacity="{op:.2f}"/>')
    y, step = vy + 8, 8.0
    while y < H:
        op = 0.9 * min((y - vy) / 120.0, 1.0)
        out.append(f'<line x1="0" y1="{y:.1f}" x2="{W}" y2="{y:.1f}" '
                   f'stroke="{LINE}" stroke-width="1.5" opacity="{op:.2f}"/>')
        y += step
        step *= 1.33
    out.append("</g>")
    # The deck is the floor of the picture, not its subject, so the near edge
    # is dimmed back toward the field. Without this the densest, brightest part
    # of the grid is the bottom of the frame and the eye goes there first.
    out.append(f'<rect x="0" y="{vy}" width="{W}" height="{H - vy}" '
               f'fill="url(#deckFade)"/>')
    return "\n".join(out)


def render_drops():
    """The dashed run from each label block down to its column cap.

    The glyph row is level and the columns are not, so without this the top half
    and the bottom half of the picture read as two separate charts. The drop is
    what makes one project one vertical object.
    """
    out = []
    for p, cx in zip(PROJECTS, COLS):
        top = BAR_BASE - bar_h(p["commits"])
        out.append(f'<line x1="{cx}" y1="{DROP_Y}" x2="{cx}" y2="{top - 62:.1f}" '
                   f'stroke="{LIGHT_EDGE}" stroke-width="1.5" opacity="0.4" '
                   f'stroke-dasharray="2 9"/>')
    return "\n".join(out)


def render_emitters():
    """Concentric footprints on the deck under each column.

    A beam that simply stops at a line reads as a bar chart with a glow on it.
    Rings in the deck's own perspective make the surface something the light is
    coming out of, which is the whole difference between a chart and a device.
    They stay faint: this is the floor, not a sixth thing to read.
    """
    out = []
    for cx in COLS:
        for i, rx in enumerate((70, 112, 158)):
            # Drawn over the coral rule and dropped onto the floor rather than
            # sitting on the baseline. Underneath it, a thin blue ring inside
            # the rule's glow just tints coral, which quietly turns one coral
            # use into five coral-washed ovals.
            out.append(f'<ellipse cx="{cx}" cy="{BAR_BASE + 19}" rx="{rx}" '
                       f'ry="{rx * 0.125:.1f}" fill="none" stroke="{LIGHT_EDGE}" '
                       f'stroke-width="1.5" opacity="{0.3 - i * 0.08:.2f}"/>')
    return "\n".join(out)


def render_corners():
    """Corner brackets. An instrument display has a frame; a poster does not."""
    out = []
    a, m = 62, 44                                # inset, arm length
    for sx, sy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        x = a if sx > 0 else W - a
        y = a if sy > 0 else H - a
        out.append(f'<path d="M{x + sx * m},{y} L{x},{y} L{x},{y + sy * m}" '
                   f'fill="none" stroke="{LINE}" stroke-width="2.2" '
                   f'opacity="0.85"/>')
    return "\n".join(out)


def render_axis():
    """The ruler the columns are read against.

    Without it the columns are only comparable to each other, which is the usual
    way a picture like this quietly stops being a measurement. Major ticks every
    fifty, minor every twenty-five, and the same twenty-five spacing is used for
    the rungs inside the columns so the two line up exactly.
    """
    out = [f'<line x1="{AXIS_X}" y1="{BAR_BASE}" x2="{AXIS_X}" '
           f'y2="{BAR_BASE - SCALE_H - 16}" stroke="{LINE}" stroke-width="1.8" '
           f'opacity="0.9"/>']
    for v in range(0, SCALE_MAX + 1, 25):
        y = BAR_BASE - bar_h(v)
        major = v % 50 == 0
        out.append(f'<line x1="{AXIS_X}" y1="{y:.1f}" '
                   f'x2="{AXIS_X + (13 if major else 7)}" y2="{y:.1f}" '
                   f'stroke="{LINE}" stroke-width="1.8" '
                   f'opacity="{0.95 if major else 0.6}"/>')
        # The zero tick is drawn but not labelled: its label would land on the
        # coral baseline, and the baseline already says where zero is.
        if major and v:
            out.append(f'<text x="{AXIS_X - 12}" y="{y + 7:.1f}" class="tick">'
                       f'{v}</text>')
    return "\n".join(out)


def render_column(p, cx):
    """One volumetric column of light. Height is the commit count, linearly.

    Linear on a round scale, not compressed: the smallest project is 19 percent
    of the largest and the picture should say so rather than flattering it. The
    rungs are a reading aid, one per twenty-five commits, aligned to the axis
    ticks so a viewer can count instead of trusting the eye.
    """
    h = bar_h(p["commits"])
    top = BAR_BASE - h
    x0, x1 = cx - BAR_W / 2, cx + BAR_W / 2
    out = ['<g>']

    # the beam itself: bright at the cap, dissolving into the deck
    out.append(f'<rect x="{x0}" y="{top:.1f}" width="{BAR_W}" height="{h:.1f}" '
               f'fill="url(#beam)" filter="url(#beamGlow)"/>')
    out.append(f'<rect x="{x0}" y="{top:.1f}" width="{BAR_W}" height="{h:.1f}" '
               f'fill="url(#beamCore)"/>')

    # rungs, on the axis's own twenty-five spacing
    for k in range(1, int(p["commits"] // 25) + 1):
        ry = BAR_BASE - bar_h(k * 25)
        out.append(f'<line x1="{x0 + 7:.1f}" y1="{ry:.1f}" x2="{x1 - 7:.1f}" '
                   f'y2="{ry:.1f}" stroke="{LIGHT_CORE}" stroke-width="1.2" '
                   f'opacity="0.24"/>')

    # Cap: a hard rule with brackets, so the top of the column is a measurement
    # and not just where the light gives out. Drawn as a rect rather than a
    # line because a horizontal line has a zero-height bounding box, and a
    # filter region given in percent of that box is zero-height too, which
    # silently deletes the glow.
    out.append(f'<rect x="{x0 - 13:.1f}" y="{top - 1.3:.1f}" '
               f'width="{BAR_W + 26}" height="2.6" fill="{LIGHT_CORE}" '
               f'filter="url(#capGlow)"/>')
    for bx in (x0 - 13, x1 + 13):
        out.append(f'<line x1="{bx:.1f}" y1="{top - 7:.1f}" x2="{bx:.1f}" '
                   f'y2="{top + 7:.1f}" stroke="{LIGHT_CORE}" stroke-width="2.2" '
                   f'opacity="0.8"/>')

    # the pool where the column lands on the deck
    out.append(f'<ellipse cx="{cx}" cy="{BAR_BASE}" rx="{BAR_W * 1.5:.0f}" ry="9" '
               f'fill="url(#pool)" filter="url(#poolGlow)"/>')

    # reflection: the column continues below the deck, compressed and fading
    out.append(f'<rect x="{x0}" y="{BAR_BASE}" width="{BAR_W}" '
               f'height="{h * 0.42:.1f}" fill="url(#reflect)" opacity="0.5"/>')

    out.append(f'<text x="{cx}" y="{top - 30:.1f}" class="num">{p["commits"]}</text>')
    out.append("</g>")
    return "\n".join(out)


def fonts_css():
    """The repo's own faces, inlined as data URIs so the render is portable."""
    css = (ASSETS / "css" / "fonts.css").read_text(encoding="utf-8")

    def swap(m):
        data = (ASSETS / "fonts" / m.group(1)).read_bytes()
        return "url(data:font/woff2;base64," + base64.b64encode(data).decode() + ")"

    return re.sub(r"url\(\.\./fonts/([^)]+)\)", swap, css)


def logo_uri():
    """The Wolfpack mark, lifted off its own navy plate and recolored as light.

    The shipped PNG is stars on a navy tile. Dropping the tile has to happen at
    the mark's native 200 pixels: the constellation segments are one pixel wide
    and sit at about 0.33 luminance against a 0.05 plate, so any downscale first
    averages them most of the way back into the plate and a luminance key then
    keeps only the star cores. That is a wolf reduced to loose confetti.

    Keying at native size instead, the segments survive as partial alpha, which
    is what a thin line is supposed to become. The recolor puts the mark in the
    same LIGHT_EDGE-to-LIGHT_CORE ramp as the five glyphs below, so the corner
    mark and the row of project marks are lit by the same source.
    """
    src = np.asarray(
        Image.open(ASSETS / "img" / "wolfpack-logo.png").convert("RGB"),
        dtype=np.float32) / 255.0
    lum = 0.30 * src[:, :, 0] + 0.56 * src[:, :, 1] + 0.14 * src[:, :, 2]

    alpha = np.clip((lum - 0.055) / 0.18, 0.0, 1.0)
    warm = np.clip((lum - 0.30) / 0.60, 0.0, 1.0)[:, :, None]

    edge = np.array([124, 147, 214], dtype=np.float32)
    core = np.array([255, 244, 241], dtype=np.float32)
    rgb = edge * (1.0 - warm) + core * warm

    out = np.dstack([rgb, alpha[:, :, None] * 255.0])
    img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), mode="RGBA")

    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def build_svg():
    glyphs = "\n".join(render_glyph(p["glyph"], cx, GLYPH_CY)
                       for p, cx in zip(PROJECTS, COLS))
    columns = "\n".join(render_column(p, cx) for p, cx in zip(PROJECTS, COLS))

    labels = []
    for p, cx in zip(PROJECTS, COLS):
        labels.append(f'<text x="{cx}" y="{NAME_Y}" class="name">{p["name"]}</text>')
        labels.append(f'<text x="{cx}" y="{META_Y}" class="meta">'
                      f'{p["files"]} FILES &#183; {p["days"]} ACTIVE DAYS</text>')
    labels = "\n".join(labels)

    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <style>
    {fonts_css()}
    .kick {{ font-family: Consolas, monospace; font-size: 25px; fill: {MUTED};
             letter-spacing: 4.2px; }}
    .name {{ font-family: Roboto, sans-serif; font-weight: 700; font-size: 25px;
             fill: {WHITE}; letter-spacing: 2.1px; text-anchor: middle; }}
    .meta {{ font-family: Consolas, monospace; font-size: 19px; fill: {FAINT};
             letter-spacing: 1.7px; text-anchor: middle; }}
    .num  {{ font-family: Roboto, sans-serif; font-weight: 700; font-size: 46px;
             fill: {WHITE}; text-anchor: middle; }}
    .leg  {{ font-family: Consolas, monospace; font-size: 20px; fill: {FAINT};
             letter-spacing: 2.4px; }}
    .legr {{ text-anchor: end; }}
    .tick {{ font-family: Consolas, monospace; font-size: 18px; fill: {FAINT};
             letter-spacing: 1.4px; text-anchor: end; }}
  </style>

  <linearGradient id="field" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"    stop-color="{NAVY_TOP}"/>
    <stop offset="0.62" stop-color="{NAVY_MID}"/>
    <stop offset="1"    stop-color="{NAVY_BOT}"/>
  </linearGradient>

  <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"   stop-color="{LIGHT_CORE}" stop-opacity="0.92"/>
    <stop offset="0.4" stop-color="{LIGHT_EDGE}" stop-opacity="0.5"/>
    <stop offset="1"   stop-color="{LIGHT_EDGE}" stop-opacity="0.12"/>
  </linearGradient>
  <linearGradient id="beamCore" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0"    stop-color="{LIGHT_CORE}" stop-opacity="0"/>
    <stop offset="0.5"  stop-color="{LIGHT_CORE}" stop-opacity="0.4"/>
    <stop offset="1"    stop-color="{LIGHT_CORE}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="reflect" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{LIGHT_EDGE}" stop-opacity="0.30"/>
    <stop offset="1" stop-color="{LIGHT_EDGE}" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="pool">
    <stop offset="0" stop-color="{LIGHT_CORE}" stop-opacity="0.75"/>
    <stop offset="1" stop-color="{LIGHT_EDGE}" stop-opacity="0"/>
  </radialGradient>
  <!-- The baseline runs the width of the deck but arrives and leaves as light
       rather than as a ruled edge. At full strength end to end it stops being
       a horizon and becomes a divider that cuts the frame in half. -->
  <linearGradient id="coralRule" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0"    stop-color="{CORAL}" stop-opacity="0"/>
    <stop offset="0.13" stop-color="{CORAL}" stop-opacity="0.62"/>
    <stop offset="0.5"  stop-color="{CORAL}" stop-opacity="0.88"/>
    <stop offset="0.87" stop-color="{CORAL}" stop-opacity="0.62"/>
    <stop offset="1"    stop-color="{CORAL}" stop-opacity="0"/>
  </linearGradient>

  <linearGradient id="deckFade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0"    stop-color="{NAVY_BOT}" stop-opacity="0"/>
    <stop offset="0.55" stop-color="{NAVY_BOT}" stop-opacity="0.16"/>
    <stop offset="1"    stop-color="{NAVY_BOT}" stop-opacity="0.5"/>
  </linearGradient>
  <radialGradient id="haze" cx="0.5" cy="0.5">
    <stop offset="0" stop-color="{LIGHT_EDGE}" stop-opacity="0.19"/>
    <stop offset="1" stop-color="{LIGHT_EDGE}" stop-opacity="0"/>
  </radialGradient>

  <filter id="glyphGlow" x="-70%" y="-70%" width="240%" height="240%">
    <feGaussianBlur stdDeviation="7" result="b1"/>
    <feGaussianBlur stdDeviation="20" result="b2"/>
    <feMerge>
      <feMergeNode in="b2"/><feMergeNode in="b1"/><feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <filter id="beamGlow" x="-260%" y="-30%" width="620%" height="160%">
    <feGaussianBlur stdDeviation="22"/>
  </filter>
  <filter id="capGlow" x="-90%" y="-900%" width="280%" height="1900%">
    <feGaussianBlur stdDeviation="9" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="poolGlow" x="-90%" y="-700%" width="280%" height="1500%">
    <feGaussianBlur stdDeviation="13" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="coralGlow" x="-4%" y="-2600%" width="108%" height="5300%">
    <feGaussianBlur stdDeviation="6" result="near"/>
    <feGaussianBlur stdDeviation="24" result="far"/>
    <feMerge>
      <feMergeNode in="far"/><feMergeNode in="near"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>

<rect width="{W}" height="{H}" fill="url(#field)"/>

<!-- atmosphere above the deck, so the beams are volumetric in something -->
<ellipse cx="{W/2}" cy="{BAR_BASE - 175}" rx="1210" ry="520" fill="url(#haze)"/>

{render_floor()}
{render_axis()}
{render_drops()}
{columns}

<!-- The deck baseline, drawn over the columns so the pools do not swallow it.
     THE ONE CORAL USE on this graphic, mirroring .hero__stand's border-bottom
     the way build_hero.py's rule does. -->
<rect x="{DECK_X0}" y="{BAR_BASE - 1.4}" width="{DECK_X1 - DECK_X0}" height="2.8"
      fill="url(#coralRule)" filter="url(#coralGlow)"/>
{render_emitters()}

{glyphs}
{labels}
{render_corners()}

<text x="{DECK_X0}" y="128" class="kick">FIVE PROJECTS &#183; THIRTY DAYS &#183; {TOTAL} COMMITS</text>
<image xlink:href="{logo_uri()}" x="{DECK_X1 - 146}" y="42" width="146"
       height="146" opacity="0.78"/>

<text x="{DECK_X0}" y="1268" class="leg">COLUMN HEIGHT &#61; COMMITS</text>
<text x="{DECK_X1}" y="1268" class="leg legr">2026-07-05 TO 2026-08-05</text>
</svg>
"""


# ==========================================================================
# Render, then finish
# ==========================================================================

def main():
    out_path = sys.argv[1]
    out_w = int(sys.argv[2]) if len(sys.argv) > 2 else 2100

    tmp = pathlib.Path(tempfile.mkdtemp())
    svg = tmp / "cover.svg"
    svg.write_text(build_svg(), encoding="utf-8")

    png = tmp / "shot.png"
    subprocess.run([
        browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
        f"--screenshot={png}", f"--window-size={W},{H}",
        "--default-background-color=00000000", "--force-device-scale-factor=1",
        "--virtual-time-budget=6000", svg.as_uri(),
    ], check=True, capture_output=True)

    img = Image.open(png).convert("RGB")
    arr = np.asarray(img, dtype=np.float32) / 255.0

    # Vignette, sized so the corners land on the page's own --navy. Same reason
    # as build_hero.py: a figure whose edges outshine the page reads as a panel
    # laid on the page instead of a window into it.
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    vx = (xx - W / 2) / (W / 2)
    vy = (yy - H / 2) / (H / 2)
    vig = 1.0 - 0.44 * np.clip(np.hypot(vx * 0.84, vy * 0.80) - 0.34, 0, 2) ** 1.4
    arr *= vig[:, :, None]

    # Grain, which is what stops a gradient this wide from banding
    rng = np.random.default_rng(11)
    arr += rng.normal(0.0, 0.38 / 255.0, arr.shape).astype(np.float32)

    img = Image.fromarray((np.clip(arr, 0, 1) * 255 + 0.5).astype(np.uint8))
    img = img.resize((out_w, round(out_w * H / W)), Image.LANCZOS)

    if out_path.lower().endswith((".jpg", ".jpeg")):
        # 4:4:4. The cap lines and the coral rule are two or three pixels tall,
        # and chroma subsampling smears both.
        img.save(out_path, quality=90, subsampling=0, optimize=True, progressive=True)
    else:
        img.save(out_path, optimize=True)
    print("wrote", out_path, img.size)


if __name__ == "__main__":
    main()
