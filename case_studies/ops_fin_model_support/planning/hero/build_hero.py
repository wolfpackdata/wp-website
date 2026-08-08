"""
Build the hero image for the financial model case study.

    python build_hero.py <source.png> <out.jpg> [out_width]

`out_width` defaults to 2100, the size the case study page loads. Pass a smaller
one for a derivative — the portfolio card and the blog post cover are both built
this way, from this composition, rather than by re-encoding the delivered JPEG.
One composition, several sizes, no generational loss.

The composition is a beacon: the operating model is the light source, the navy
field around it is the business you cannot see into yet, and the beams are the
golden paths the standfirst names. It is generated rather than drawn so it can
be rebuilt from the source capture, and so the glow is real light math instead
of a stack of soft brushes.

Palette discipline follows case-study.css. Navy system only. The light is white
with a trace of the brand coral at its very core and a navy tint at the fringe,
so nothing here is a hue the page does not already own. Coral appears once, as
the rule under the sheet, mirroring .hero__stand's border-bottom.

All the light is summed in LINEAR space and converted to sRGB at the end. That
is what keeps a wide gradient from going muddy or banding.
"""

import sys

import numpy as np
from PIL import Image, ImageFilter

W, H = 2400, 1350                    # 16:9 — .shot's aspect ratio exactly

# --- the sheet, and the mat it sits in -------------------------------------
SHEET_W = 1520
MAT_PAD = 16                         # 8px at 1x
BORDER = 2                           # 1px at 1x, matching .shot's border
SHEET_TOP = 320

# --- colors, sRGB 0-255 ----------------------------------------------------
NAVY_TOP = (0, 5, 22)
NAVY_MID = (0, 11, 41)               # --navy #000B29
NAVY_BOT = (0, 4, 17)
FIG_BG = (10, 10, 10)                # --fig-bg
FIG_LINE = (42, 42, 42)              # --fig-line
CORAL = (249, 89, 84)                # --coral
LIGHT_CORE = (255, 244, 241)         # white carrying a trace of coral
LIGHT_EDGE = (124, 147, 214)         # a tint of navy, not a new hue

# The team-member column of the source capture, in the capture's own pixels.
# Real first names sit there, and no case study here ever names a client, so the
# column is destroyed rather than trusted to be too small to read. THE COMMITTED
# SOURCE IS ALREADY REDACTED; this repeats the blur so that a fresh capture of
# the same workbook, dropped in unredacted, is covered too. Re-blurring an
# already-blurred patch changes nothing.
REDACT = (108, 616, 236, 740)


def srgb_to_linear(a):
    a = np.asarray(a, dtype=np.float32)
    return np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(a):
    a = np.clip(a, 0.0, 1.0)
    return np.where(a <= 0.0031308, a * 12.92, 1.055 * a ** (1.0 / 2.4) - 0.055)


def lin(rgb255):
    """An sRGB 0-255 triple as a linear-light float triple."""
    return srgb_to_linear(np.array(rgb255, dtype=np.float32) / 255.0)


def _box1d(a, axis, half):
    """Moving average of width 2*half+1 along one axis, edge-clamped."""
    if half < 1:
        return a
    a = np.moveaxis(a, axis, -1)
    pad = np.pad(a, [(0, 0)] * (a.ndim - 1) + [(half + 1, half)], mode="edge")
    c = np.cumsum(pad, axis=-1, dtype=np.float32)
    out = (c[..., 2 * half + 1:] - c[..., :-(2 * half + 1)]) / np.float32(2 * half + 1)
    return np.moveaxis(out, -1, axis)


def blur(arr, sigma, passes=3):
    """Gaussian blur of a single-channel float field, at full resolution.

    Three box passes, which is the standard approximation and is smooth enough
    that nothing downstream can tell. Written out rather than handed to PIL for
    two reasons: PIL's GaussianBlur rejects mode "F" outright, and blurring a
    uint8 copy quantizes a glow that has to stay smooth over hundreds of pixels.
    Blurring a DOWNSAMPLED copy was the first thing tried and is the trap — the
    box downsample turns the sheet's hard rectangular edge into stair steps that
    survive the blur and show up as a visibly polygonal halo.
    """
    half = max(1, int(round(np.sqrt(12.0 * sigma * sigma / passes + 1.0) - 1.0) // 2))
    out = np.ascontiguousarray(arr, dtype=np.float32)
    for _ in range(passes):
        out = _box1d(out, 0, half)
        out = _box1d(out, 1, half)
    return out


# ==========================================================================
# 1. The sheet: load, redact, and place it on the canvas
# ==========================================================================

src_path, out_path = sys.argv[1], sys.argv[2]
src = Image.open(src_path).convert("RGB")

region = src.crop(REDACT).filter(ImageFilter.GaussianBlur(4))
src.paste(region, (REDACT[0], REDACT[1]))

scale = SHEET_W / src.width
sheet_h = int(round(src.height * scale))
sheet = src.resize((SHEET_W, sheet_h), Image.LANCZOS)

sx0 = (W - SHEET_W) // 2
sy0 = SHEET_TOP
sx1, sy1 = sx0 + SHEET_W, sy0 + sheet_h

# The sheet's own luminance, on the canvas, is what drives its bloom. A bright
# spreadsheet on a dark field should light the field up; that is the whole
# conceit of the page title.
sheet_lum = np.zeros((H, W), dtype=np.float32)
lum = np.asarray(sheet.convert("L"), dtype=np.float32) / 255.0
sheet_lum[sy0:sy1, sx0:sx1] = srgb_to_linear(lum)

# ==========================================================================
# 2. The navy field
# ==========================================================================

yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
t = (yy / (H - 1))[:, :, None]

top, mid, bot = lin(NAVY_TOP), lin(NAVY_MID), lin(NAVY_BOT)
upper = top + (mid - top) * np.clip(t / 0.62, 0, 1)
lower = mid + (bot - mid) * np.clip((t - 0.62) / 0.38, 0, 1)
canvas = np.where(t < 0.62, upper, lower).astype(np.float32)

# ==========================================================================
# 3. The beacon: a crown of beams, computed as a polar field
# ==========================================================================

# Origin sits inside the sheet, roughly at its middle. Two things follow: the
# sheet occludes the convergence point, so no hot dot is ever visible, and the
# fan above the sheet is wide rather than a point-source starburst.
ox, oy = W / 2.0, sy0 + sheet_h * 0.52

dx = xx - ox
dy = oy - yy                                   # y up
r = np.hypot(dx, dy)
ang = np.degrees(np.arctan2(dy, dx))

# (center angle, half-width in degrees, amplitude). Deliberately asymmetric and
# unevenly spaced: a symmetrical evenly-spaced sunburst reads as clip art. Wide
# soft lobes carry the light, narrow ones give it structure. Nothing sits near
# the horizontal, because a beam parallel to the frame edge reads as a lens
# streak rather than as light leaving a source.
LOBES = [
    (90, 9.0, 0.55), (90, 3.2, 0.55),         # the axis: soft body, hard core
    (72, 5.5, 0.42), (108, 6.5, 0.46),
    (57, 2.2, 0.34), (126, 2.6, 0.30),
    (44, 9.5, 0.38), (137, 10.5, 0.40),
    (31, 3.0, 0.22), (152, 2.6, 0.20),
    (20, 6.0, 0.15), (163, 6.5, 0.14),
]

beams = np.zeros((H, W), dtype=np.float32)
for center, half, amp in LOBES:
    d = np.abs(((ang - center + 180.0) % 360.0) - 180.0)
    beams += amp * np.exp(-(d / half) ** 2)

# Two lobes aimed down and out, which exist only to land on the ground below
GROUND_LOBES = [(-24, 7.0, 0.30), (203, 7.5, 0.28)]
rake = np.zeros((H, W), dtype=np.float32)
for center, half, amp in GROUND_LOBES:
    d = np.abs(((ang - center + 180.0) % 360.0) - 180.0)
    rake += amp * np.exp(-(d / half) ** 2)

# Beams are brightest just off the source and gone before the frame edge. The
# r**0.6 term stops the origin from becoming a hard hot dot if it ever shows.
falloff = np.exp(-(r / 900.0) ** 1.45) * np.clip(r / 260.0, 0, 1) ** 0.6
beams *= falloff
rake *= falloff

# Atmosphere. Volumetric light needs something to be volumetric in, and a broad
# haze above the source is what stops the beams looking like drawn triangles.
haze = 0.24 * np.exp(-(r / 560.0) ** 1.8)

core = 0.85 * np.exp(-(r / 300.0) ** 2)

light = beams * 0.95 + haze + core

# Fringe color: the further from the source, the more the light sits in the
# navy family. Mixing on the intensity field, not per pixel, keeps it smooth.
mix = np.clip(1.0 - light * 0.55, 0.0, 1.0)[:, :, None]
light_rgb = lin(LIGHT_CORE) * (1.0 - mix) + lin(LIGHT_EDGE) * mix
canvas += light[:, :, None] * light_rgb * 0.62

# ==========================================================================
# 4. Ground: a reflection and the streaks the rake beams leave on it
# ==========================================================================

HORIZON = sy1 + 27

refl = np.zeros((H, W, 3), dtype=np.float32)

# A reflection on a ground plane compresses toward the horizon, so the mirror is
# squashed before it is placed. Skipping the squash was the version that looked
# like a fog bank parked under the sheet instead of like ground.
REFL_SQUASH = 0.38
mirror = sheet.transpose(Image.FLIP_TOP_BOTTOM).resize(
    (SHEET_W, int(sheet_h * REFL_SQUASH)), Image.LANCZOS)
mirror = np.asarray(mirror, dtype=np.float32) / 255.0
mh = min(mirror.shape[0], H - HORIZON)
refl[HORIZON:HORIZON + mh, sx0:sx1] = srgb_to_linear(mirror[:mh])

refl_img = Image.fromarray((linear_to_srgb(refl) * 255).astype(np.uint8))
refl_img = refl_img.filter(ImageFilter.GaussianBlur(27))
refl = srgb_to_linear(np.asarray(refl_img, dtype=np.float32) / 255.0)

# Fade with distance from the horizon, and feather the sides, so the reflection
# has no edge of its own anywhere.
fade = np.clip(1.0 - (yy - HORIZON) / (mh * 1.35), 0.0, 1.0)
fade = np.where(yy > HORIZON, fade, 0.0) ** 1.9
hmask = np.clip(1.0 - (np.abs(xx - W / 2) - SHEET_W * 0.32) / (SHEET_W * 0.30), 0, 1)
# Kept deliberately faint. At full strength this is a legible second copy of
# the sheet, which reads as a duplicate object rather than as light on ground.
canvas += refl * (fade * hmask)[:, :, None] * 0.13

# The rake lobes, clipped to below the horizon, so the light that leaves the
# sheet sideways lands on something.
ground = np.where(yy > HORIZON, np.clip((yy - HORIZON) / 130.0, 0, 1), 0.0)
canvas += (rake * ground * 0.95)[:, :, None] * lin(LIGHT_EDGE)

# A thin horizon glow, so the ground has an edge without a drawn line
canvas += (np.exp(-((yy - HORIZON) / 26.0) ** 2) * 0.034)[:, :, None] * lin(LIGHT_EDGE)

# ==========================================================================
# 5. The sheet's bloom, then the sheet itself
# ==========================================================================

for radius, amount in ((170, 0.26), (60, 0.20), (18, 0.16), (6, 0.10)):
    b = blur(sheet_lum, radius)
    canvas += (b * amount)[:, :, None] * lin(LIGHT_CORE)

canvas_srgb = linear_to_srgb(canvas)
out = Image.fromarray((np.clip(canvas_srgb, 0, 1) * 255).astype(np.uint8))

# Mat and hairline, drawn with the figure-ground tokens so the frame here and
# the frame around a .shot on the page are the same object.
from PIL import ImageDraw  # noqa: E402  (only needed from here down)

mat = Image.new("RGB", (SHEET_W + 2 * MAT_PAD, sheet_h + 2 * MAT_PAD), FIG_BG)
mat.paste(sheet, (MAT_PAD, MAT_PAD))
box = [0, 0, mat.size[0] - 1, mat.size[1] - 1]
ImageDraw.Draw(mat).rounded_rectangle(box, radius=8, outline=FIG_LINE, width=BORDER)

mask = Image.new("L", mat.size, 0)
ImageDraw.Draw(mask).rounded_rectangle(box, radius=8, fill=255)

out.paste(mat, (sx0 - MAT_PAD, sy0 - MAT_PAD), mask)

# ==========================================================================
# 6. Coral rule under the sheet, and its glow. One coral use, mirroring
#    .hero__stand's 3px border-bottom.
# ==========================================================================

canvas = srgb_to_linear(np.asarray(out, dtype=np.float32) / 255.0)

# Rim light. The source capture is mostly black, so without this the sheet reads
# as a hole punched in a lit field rather than as an object with light behind it.
# Brightest along the top edge, dying out a third of the way down each side.
mx0, my0 = sx0 - MAT_PAD, sy0 - MAT_PAD
mx1, my1 = sx1 + MAT_PAD, sy1 + MAT_PAD
rim = np.zeros((H, W), dtype=np.float32)
# top edge, brightest at the middle and gone before the corners
span = np.linspace(-1.0, 1.0, mx1 - mx0, dtype=np.float32)
rim[my0:my0 + 2, mx0:mx1] = np.exp(-(span / 0.62) ** 2)
# upper thirds of the two sides
side = np.linspace(1.0, 0.0, (my1 - my0) // 3, dtype=np.float32) ** 2.2
rim[my0:my0 + len(side), mx0:mx0 + 2] = np.maximum(
    rim[my0:my0 + len(side), mx0:mx0 + 2], side[:, None] * 0.7)
rim[my0:my0 + len(side), mx1 - 2:mx1] = np.maximum(
    rim[my0:my0 + len(side), mx1 - 2:mx1], side[:, None] * 0.7)
rim = blur(rim, 1.4) * 0.30 + blur(rim, 9.0) * 0.34
canvas += rim[:, :, None] * lin(LIGHT_CORE)

# Light spilling from behind onto the sheet's own surface. The capture is mostly
# black, and without this the top of it stays a flat dead field while the air
# around it is lit, which is the tell that an image was pasted onto a background.
spill = np.zeros((H, W), dtype=np.float32)
grad = np.clip(1.0 - np.linspace(0, 1, sheet_h, dtype=np.float32) / 0.55, 0, 1) ** 1.6
spill[sy0:sy1, sx0:sx1] = grad[:, None]
spill *= 1.0 - np.clip(np.asarray(sheet.convert("L"), dtype=np.float32).mean() * 0, 0, 1)
canvas += (blur(spill, 6.0) * 0.030)[:, :, None] * lin(LIGHT_EDGE)

rule_y0, rule_y1 = sy1 + MAT_PAD + 9, sy1 + MAT_PAD + 15
rule_x0, rule_x1 = sx0 - MAT_PAD, sx1 + MAT_PAD
rule = np.zeros((H, W), dtype=np.float32)
rule[rule_y0:rule_y1, rule_x0:rule_x1] = 1.0
glow = blur(rule, 54) * 0.55 + blur(rule, 15) * 0.45
canvas += glow[:, :, None] * lin(CORAL) * 0.75
canvas = np.where(rule[:, :, None] > 0, lin(CORAL)[None, None, :], canvas)

# ==========================================================================
# 7. Vignette, grain, out
# ==========================================================================

vx = (xx - W / 2) / (W / 2)
vy = (yy - H / 2) / (H / 2)
# Sized so the corners land on the page's own --navy. A figure whose edges are
# lighter than the page reads as a panel laid on top of the page rather than as
# a window into it, which is the single thing most likely to make this look
# pasted in. Checked against #000B29 with the in-page screenshot, not by eye.
vig = 1.0 - 0.52 * np.clip(np.hypot(vx * 0.86, vy * 0.80) - 0.30, 0, 2) ** 1.35
# A touch more off the bottom edge than the top, so the frame closes under the
# ground rather than fading out into a band of haze
vig *= 1.0 - 0.16 * np.clip((yy - H * 0.80) / (H * 0.20), 0, 1) ** 1.4
canvas *= vig[:, :, None]

final = linear_to_srgb(canvas)

# Grain at 0.35/255 kills the banding a gradient this wide would otherwise show
rng = np.random.default_rng(7)
final += rng.normal(0.0, 0.35 / 255.0, final.shape).astype(np.float32)

img = Image.fromarray((np.clip(final, 0, 1) * 255 + 0.5).astype(np.uint8))

# Composed at 2400 and delivered at OUT_W. The case study figure is never wider
# than about 1050 CSS pixels inside .wrap, so the 2100 default covers a 2x
# display with room to spare, and the downsample costs nothing visible while
# taking a quarter off the file. The composition is tuned in 2400-pixel
# coordinates, so this is a final resize rather than a smaller canvas; changing W
# would move every constant above.
OUT_W = int(sys.argv[3]) if len(sys.argv) > 3 else 2100
img = img.resize((OUT_W, round(OUT_W * H / W)), Image.LANCZOS)

if out_path.lower().endswith((".jpg", ".jpeg")):
    # 4:4:4. Chroma subsampling smears the coral rule and the yellow cells in the
    # sheet, both of which are one or two pixels tall at this size.
    img.save(out_path, quality=88, subsampling=0, optimize=True, progressive=True)
else:
    img.save(out_path, optimize=True)
print("wrote", out_path, img.size)
