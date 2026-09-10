"""
Build the cover for "How to Restrict What Your IC Can Touch".

    python blog_posts/2026-09-10-restrict-what-your-ic-can-touch/planning/hero/build_hero.py

Run from the repo root. Writes ../../cover.jpg (1600 x 900, 16:9, JPEG q95).

The image is GENERATED, and this script is its master — rebuild rather than
retouch, the same convention the AI Command emblem and the social cards carry.
Everything is deterministic: no timestamps, no randomness, so the same checkout
always produces the same bytes. It reads no fonts and draws no text.

The picture: a floor of dark, locked cells seen from a three-quarter elevated
camera, and through it one corridor of cells lit in icy blue, running from the
left edge to a single bright destination panel. Small warm amber points mark the
turns. That is the post's argument in one frame — the contractor can reach the
work, and only the work.

Palette, taken from the existing blog covers and the site's own values: the
`--navy #000B29` field the social cards use, cool icy blue and silver-white
highlights, and a rationed handful of warm amber joints. No text, no logo.

Pillow only, no other dependency, consistent with this repo's no-build-step
convention (Pillow is already required by social-cards/build_cards.py).
"""

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "cover.jpg"

# Output size and supersampling factor (rendered at 2x, downsampled for AA).
W, H = 1600, 900
S = 2

# Palette
NAVY_TOP = (2, 14, 48)
NAVY_MID = (0, 11, 41)
NAVY_BOT = (0, 6, 22)
FLOOR = (4, 15, 44)
CELL_FILL = (6, 20, 55)
CELL_LINE = (18, 38, 82)
CELL_MARK = (24, 48, 96)
ICE = (120, 190, 245)
ICE_DEEP = (34, 96, 176)
SILVER = (230, 240, 255)
AMBER = (255, 179, 71)

# The grid and the corridor through it (column, row), origin top-left.
COLS, ROWS = 14, 9
PATH = [
    (0, 6), (1, 6), (2, 6), (2, 5), (3, 5), (4, 5), (4, 4), (5, 4), (6, 4),
    (7, 4), (7, 3), (8, 3), (9, 3), (9, 2), (10, 2), (11, 2),
]
DEST = PATH[-1]


def find_coeffs(target, source):
    """Perspective coefficients mapping `source` quad onto `target` quad."""
    import numpy as np  # local import: only needed for the 8x8 solve

    matrix = []
    for (tx, ty), (sx, sy) in zip(target, source):
        matrix.append([sx, sy, 1, 0, 0, 0, -tx * sx, -tx * sy])
        matrix.append([0, 0, 0, sx, sy, 1, -ty * sx, -ty * sy])
    a = np.array(matrix, dtype=float)
    b = np.array([c for pt in target for c in pt], dtype=float)
    res = np.linalg.solve(a, b)
    return [float(v) for v in res]


def gradient_field(w, h):
    """Three-stop vertical navy gradient, summed in linear light."""
    def lin(c):
        return [(v / 255.0) ** 2.2 for v in c]

    def srgb(c):
        return tuple(int(round(max(0.0, min(1.0, v)) ** (1 / 2.2) * 255)) for v in c)

    top, mid, bot = lin(NAVY_TOP), lin(NAVY_MID), lin(NAVY_BOT)
    img = Image.new("RGB", (1, h))
    px = img.load()
    for y in range(h):
        t = y / (h - 1)
        if t < 0.45:
            u = t / 0.45
            c = [top[i] * (1 - u) + mid[i] * u for i in range(3)]
        else:
            u = (t - 0.45) / 0.55
            c = [mid[i] * (1 - u) + bot[i] * u for i in range(3)]
        px[0, y] = srgb(c)
    return img.resize((w, h))


def draw_floor(cs):
    """The flat, un-warped floor: locked cells, the lit corridor, the walls.

    Returns (base, glow): the floor itself, and a black image carrying only the
    luminous parts, which is blurred later to make the bloom.
    """
    fw, fh = COLS * cs, ROWS * cs
    base = Image.new("RGB", (fw, fh), FLOOR)
    glow = Image.new("RGB", (fw, fh), (0, 0, 0))
    d = ImageDraw.Draw(base)
    g = ImageDraw.Draw(glow)
    on_path = set(PATH)
    gap = cs // 14          # gutter between cells
    hair = max(1, cs // 90)

    # Locked cells: recessed squares with a hairline and a small closed bar.
    for r in range(ROWS):
        for c in range(COLS):
            if (c, r) in on_path:
                continue
            x0, y0 = c * cs + gap, r * cs + gap
            x1, y1 = (c + 1) * cs - gap, (r + 1) * cs - gap
            k = ((c * 7 + r * 13) % 5) - 2          # -2..2, deterministic by position
            fill = tuple(max(0, v + 2 * k) for v in CELL_FILL)
            d.rectangle([x0, y0, x1, y1], fill=fill, outline=CELL_LINE, width=hair)
            # a short dim bar, the "closed" mark, centred in the cell
            bw, bh = (x1 - x0) * 0.22, max(2, cs // 40)
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            d.rectangle([cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2], fill=CELL_MARK)

    # Corridor cells: a lit fill that brightens toward the destination.
    n = len(PATH)
    for i, (c, r) in enumerate(PATH):
        t = i / (n - 1)
        col = tuple(int(ICE_DEEP[k] * (1 - t) + ICE[k] * t) for k in range(3))
        x0, y0 = c * cs + gap, r * cs + gap
        x1, y1 = (c + 1) * cs - gap, (r + 1) * cs - gap
        d.rectangle([x0, y0, x1, y1], fill=col)
        lift = tuple(min(255, int(v * 1.18)) for v in col)
        ins = cs * 0.16
        d.rectangle([x0 + ins, y0 + ins, x1 - ins, y1 - ins], fill=lift)
        dim = tuple(int(v * (0.35 + 0.35 * t)) for v in col)
        g.rectangle([x0, y0, x1, y1], fill=dim)

    # Bridge the gutters between consecutive corridor cells so it reads as one
    # continuous passage rather than a row of tiles.
    for (c0, r0), (c1, r1) in zip(PATH, PATH[1:]):
        ax, ay = c0 * cs + cs / 2, r0 * cs + cs / 2
        bx, by = c1 * cs + cs / 2, r1 * cs + cs / 2
        half = cs / 2 - gap
        if r0 == r1:
            box = [min(ax, bx), ay - half, max(ax, bx), ay + half]
        else:
            box = [ax - half, min(ay, by), ax + half, max(ay, by)]
        i = PATH.index((c1, r1))
        t = i / (n - 1)
        col = tuple(int(ICE_DEEP[k] * (1 - t) + ICE[k] * t) for k in range(3))
        d.rectangle(box, fill=col)
        g.rectangle(box, fill=tuple(int(v * (0.35 + 0.35 * t)) for v in col))

    # Walls: the corridor's outer edge, a bright hairline where a lit cell
    # borders a locked one. This is what makes it a corridor and not a stain.
    wall = max(2, cs // 28)
    for (c, r) in PATH:
        x0, y0 = c * cs + gap, r * cs + gap
        x1, y1 = (c + 1) * cs - gap, (r + 1) * cs - gap
        for (dc, dr), seg in (
            ((0, -1), [x0, y0, x1, y0]),
            ((0, 1), [x0, y1, x1, y1]),
            ((-1, 0), [x0, y0, x0, y1]),
            ((1, 0), [x1, y0, x1, y1]),
        ):
            nb = (c + dc, r + dr)
            if nb in on_path:
                continue
            if nb[0] < 0:            # the corridor enters from the left edge: open
                continue
            d.line(seg, fill=SILVER, width=wall)
            g.line(seg, fill=SILVER, width=wall)

    # Destination: a brighter panel with a silver core.
    c, r = DEST
    x0, y0 = c * cs + gap, r * cs + gap
    x1, y1 = (c + 1) * cs - gap, (r + 1) * cs - gap
    d.rectangle([x0, y0, x1, y1], fill=ICE)
    inset = cs * 0.22
    d.rectangle([x0 + inset, y0 + inset, x1 - inset, y1 - inset], fill=SILVER)
    g.rectangle([x0, y0, x1, y1], fill=(120, 170, 220))
    g.rectangle([x0 + inset, y0 + inset, x1 - inset, y1 - inset], fill=SILVER)

    # Amber joints at each turn — the only warm colour, rationed to the corners.
    rad = max(3, cs // 13)
    for prev, cur, nxt in zip(PATH, PATH[1:], PATH[2:]):
        if (cur[0] - prev[0], cur[1] - prev[1]) == (nxt[0] - cur[0], nxt[1] - cur[1]):
            continue
        cx, cy = cur[0] * cs + cs / 2, cur[1] * cs + cs / 2
        d.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=AMBER)
        g.ellipse([cx - rad * 1.6, cy - rad * 1.6, cx + rad * 1.6, cy + rad * 1.6], fill=AMBER)

    return base, glow


def warp(img, size, quad):
    """Perspective-warp the whole of `img` onto `quad` (4 points, TL TR BR BL)."""
    fw, fh = img.size
    src = [(0, 0), (fw, 0), (fw, fh), (0, fh)]
    coeffs = find_coeffs(src, quad)  # PIL wants target->source coefficients
    fill = 0 if img.mode == "L" else (0, 0, 0)
    return img.transform(size, Image.PERSPECTIVE, coeffs, Image.BICUBIC, fillcolor=fill)


def vignette(size, strength=0.55):
    w, h = size
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([-w * 0.15, -h * 0.35, w * 1.15, h * 1.35], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(w * 0.18))
    return m.point(lambda v: int(255 - (255 - v) * strength))


def build():
    w, h = W * S, H * S
    cs = 220 * S
    canvas = gradient_field(w, h)

    base, glow = draw_floor(cs)

    # Three-quarter elevated camera: the far edge (top) is narrow and high,
    # the near edge (bottom) runs off the frame. Slight left-to-right tilt.
    quad = [
        (w * 0.14, h * 0.20),
        (w * 0.92, h * 0.14),
        (w * 1.16, h * 1.06),
        (w * -0.22, h * 1.14),
    ]
    floor = warp(base, (w, h), quad)
    lit = warp(glow, (w, h), quad)

    # Where the floor is black (outside the quad) keep the gradient; otherwise
    # the floor. A mask from the warped floor's own coverage does that.
    cover = warp(Image.new("L", base.size, 255), (w, h), quad).filter(ImageFilter.GaussianBlur(S))
    canvas = Image.composite(floor, canvas, cover)

    # Fade the far edge of the floor into the field so it reads as depth.
    fade = Image.new("L", (w, h), 255)
    fd = ImageDraw.Draw(fade)
    for y in range(int(h * 0.12), int(h * 0.46)):
        t = (y - h * 0.12) / (h * 0.34)
        fd.line([(0, y), (w, y)], fill=int(255 * min(1.0, max(0.0, t)) ** 1.4))
    fd.rectangle([0, 0, w, int(h * 0.12)], fill=0)
    canvas = Image.composite(canvas, gradient_field(w, h), fade)

    # Bloom: two blur radii, added in screen-ish light.
    soft = lit.filter(ImageFilter.GaussianBlur(28 * S))
    tight = lit.filter(ImageFilter.GaussianBlur(6 * S))
    soft = ImageChops.multiply(soft, Image.new("RGB", (w, h), (150, 150, 150)))
    tight = ImageChops.multiply(tight, Image.new("RGB", (w, h), (120, 120, 120)))
    canvas = ImageChops.add(canvas, soft)
    canvas = ImageChops.add(canvas, tight)

    # Vignette and a whisper of top-left key light.
    canvas = Image.composite(canvas, Image.new("RGB", (w, h), NAVY_BOT), vignette((w, h)))

    out = canvas.resize((W, H), Image.LANCZOS)
    out.save(OUT, "JPEG", quality=95, optimize=True, subsampling=0)
    print(f"wrote {OUT.relative_to(Path.cwd())} ({W} x {H})")


if __name__ == "__main__":
    build()
