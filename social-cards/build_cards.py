"""
Build the Open Graph / LinkedIn social cards this site needs.

    python social-cards/build_cards.py

Run from the repo root. It rebuilds all of them, every time, into the folders
that deploy:

    case_studies/case-study-assets/img/og-consolidation-under-pressure.png
    case_studies/case-study-assets/img/og-wolfpack-ai-command.png
    sm3-specific-pages/sm3-assets/img/og-setmaster3-case-study.png
    portfolio/img/og-portfolio.png
    ai-coaching/img/og-ai-coaching.png
    hire/assets/img/og-ryan-hickey.png
    hire/assets/img/og-ryan-hickey-music.png
    social-cards/wix/og-wolfstrategyllc-home.png        (the Wix homepage, not this repo)

Every inset is now a file that already exists — a screenshot, a supplied hero, or
a generated emblem — so there is no capture step to run first. That was not true
until 2026-08-17 (#226): the music-gear card's inset was the transaction map,
which exists only as something a browser draws, and it had to be photographed by
case_studies/consolidation_under_pressure/planning/card/capture_map.py before
this script could compose it. That case study now has its own hero and the card
uses it. `capture_map.py` still exists for the map's own sake; nothing here reads
it any more.

These images are **generated, and their generator ships with them — rebuild
rather than retouch**, the same convention `fin-model-beacon-hero.jpg` already
carries. A card that gets hand-edited in an image editor is a card nobody can
change again: the next title tweak becomes a design session instead of a string
edit. Everything here is deterministic — no timestamps, one fixed RNG seed — so
the same checkout always produces the same set of PNGs.

`social-cards/` never deploys. Like `blog_posts/tools/` and the case study's
`planning/hero/`, it builds *inputs* to the site rather than any part of it.

THE HARD CONSTRAINT IS LEGIBILITY AT 360 PIXELS.
LinkedIn renders a Featured tile at roughly 360px wide — under a third of the
1200px the card is authored at. So the title is set enormous by the standards of
a page (72-96px on a 1200px canvas, i.e. 22-29px as seen), the screenshot inset
is treated as texture rather than as something to be read, and everything else on
the card is one wordmark line. The case-study convention already names this trap
from the other direction — *"too small to read" is a bet that nobody zooms* — and
a social card is the one surface where nobody can zoom.

Composition, one system across all of them:

  * A navy field, the page's own `--navy #000B29` with the same three-stop
    vertical gradient `build_hero.py` uses, summed in LINEAR light so a gradient
    this wide neither bands nor goes muddy.
  * The wordmark row at the top: the constellation wolf and WOLFPACK DATA &
    STRATEGY, set the way the page nav sets it — Roboto 700, uppercase, tracked.
  * The page's own title, auto-fitted to the largest size that still wraps inside
    its line budget. A short title is therefore bigger than a long one, which is
    what you want when the enemy is a 360px render.
  * One coral rule under it. Exactly one coral use per card, mirroring
    `.hero__stand`'s border-bottom — the same ration discipline the stylesheets
    carry, applied to an image.
  * A screenshot inset in the figure-ground frame the pages use (`--fig-bg`
    #0A0A0A mat, 1px #2A2A2A hairline, 8px radius), running off the bottom edge.
    The bleed is deliberate: it reads as a window into a running application
    rather than as a thumbnail parked on a background, and it lets the shot be
    shown at a scale where its structure survives the downscale.

No hues outside the navy system, apart from whatever colour the screenshots
themselves contain — that is the subject, not the chrome.

FONTS. Every font in this repo ships as `.woff2` only, and Pillow cannot read
woff2. Rather than commit a second copy of a typeface that would silently drift
from the one the pages actually serve, the woff2 the page loads is converted to a
TTF in a temp directory at build time and thrown away afterwards. No font binary
is committed here. The face is Roboto 700 (latin subset) — this repo's heading
face everywhere, per every stylesheet's `h1, h2, h3, h4` rule and the
`.nav__wordmark` rule. Montserrat is the *body* face here and is deliberately not
used: a card set in the body face would not match the headings it is quoting.
"""

import tempfile
from pathlib import Path

import numpy as np
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent

W, H = 1200, 627                     # LinkedIn's 1.91:1, at its large-card minimum

# --- colors, sRGB 0-255, all from the stylesheets ---------------------------
NAVY_TOP = (0, 5, 22)
NAVY_MID = (0, 11, 41)               # --navy #000B29
NAVY_BOT = (0, 4, 17)
FIG_BG = (10, 10, 10)                # --fig-bg
FIG_LINE = (42, 42, 42)              # --fig-line
CORAL = (249, 89, 84)                # --coral
WHITE = (255, 255, 255)              # --white
MUTED = (191, 194, 202)              # --muted
LIGHT_EDGE = (124, 147, 214)         # a tint of navy, not a new hue

# --- geometry ---------------------------------------------------------------
MARGIN = 64
COL_W = W - 2 * MARGIN               # 1072 — everything lines up on this column
LOGO = 44
WORDMARK_TOP = 44
WORDMARK_SIZE = 20
WORDMARK_TRACK = 2.6                 # ~0.12em, matching .nav__wordmark
TITLE_TOP = 140
TITLE_LEAD = 1.14                    # .15 in CSS; tightened, because these are
                                     # display sizes rather than page headings
MAX_TITLE_H = 250                    # see fit_title — the inset's floor, really
RULE_W, RULE_H = 132, 4              # one coral use, per .hero__stand
# The optional subtitle line. See build()'s `subtitle` handling for why it
# exists; these are its whole geometry.
SUB_HI, SUB_LO = 48, 28              # 48px is 14px at a 360px Featured tile
SUB_MAX_LINES = 2
SUB_LEAD = 1.30                      # looser than the title's, because this is
                                     # a reading line rather than a display one
SUB_GAP_ABOVE = 18
SUB_SEP = " · "                      # the role-line separator, as .hero__role
                                     # sets it (a <span class="sep">)
RULE_GAP_ABOVE = 34
RULE_GAP_BELOW = 44
MAT_PAD = 10
BORDER = 1
PANEL_GAP = 28
BLEED = 110                          # how far each frame runs past the bottom edge


# ==========================================================================
# Linear-light helpers, lifted from build_hero.py so the two generators do
# their light math the same way. Anything summed (gradient, glow, grain) is
# summed in linear space and converted to sRGB once, at the end.
# ==========================================================================

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

    Three box passes. Written out rather than handed to PIL because PIL's
    GaussianBlur rejects mode "F" outright, and blurring a uint8 copy quantizes
    a glow that has to stay smooth across hundreds of pixels.
    """
    half = max(1, int(round(np.sqrt(12.0 * sigma * sigma / passes + 1.0) - 1.0) // 2))
    out = np.ascontiguousarray(arr, dtype=np.float32)
    for _ in range(passes):
        out = _box1d(out, 0, half)
        out = _box1d(out, 1, half)
    return out


# ==========================================================================
# Fonts: woff2 -> TTF in a temp dir, never committed
# ==========================================================================

# The latin subset, picked off the `unicode-range` comments in each folder's
# fonts.css: U+0000-00FF etc. Every string on these cards is latin, so the other
# eight subsets are irrelevant. Sourced from portfolio/ because all four font
# folders in this repo hold byte-identical copies of the same Google files.
ROBOTO_700_LATIN = ROOT / "portfolio" / "fonts" / \
    "KFOMCnqEu92Fr1ME7kSn66aGLdTylUAMQXC89YmC2DPNWuYjalmUiAo.woff2"


def unwoff(woff2_path, out_path):
    """Rewrite a woff2 as a plain TTF.

    fontTools decompresses woff2 (via brotli) on load; clearing `flavor` and
    saving writes the same glyph data back out uncompressed, which is all Pillow
    needs. The point of doing this at build time instead of committing a TTF is
    that the card is then guaranteed to be set in the exact file the page serves
    — if the page's font is ever replaced, the card follows it automatically
    rather than quietly keeping an old copy.
    """
    font = TTFont(str(woff2_path))
    font.flavor = None
    font.save(str(out_path))
    return str(out_path)


# ==========================================================================
# Text helpers
# ==========================================================================

def wrap(draw, text, font, max_w):
    """Greedy word wrap against measured pixel widths."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if cur and draw.textlength(trial, font=font) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def fit_title(draw, text, ttf, max_w, max_lines, hi=96, lo=56):
    """Largest size, in 2px steps, that wraps inside the line *and height* budget.

    Sizing per card rather than per system is the whole trick behind the 360px
    constraint: "Portfolio & Case Studies" gets to be enormous, and the SetMaster
    title — three times the length — only gives up as much as it has to.

    MAX_TITLE_H is what stops a long title from eating the card. Fitting purely
    to the line count set the SetMaster title at 96px across three lines, which
    left the screenshot an eighty-pixel sliver showing nothing but a toolbar —
    technically a bleed, visually a mistake. The height cap is really a floor
    under the inset, expressed from the other end.
    """
    for size in range(hi, lo - 1, -2):
        font = ImageFont.truetype(ttf, size)
        lines = wrap(draw, text, font, max_w)
        if len(lines) <= max_lines and round(size * TITLE_LEAD) * len(lines) <= MAX_TITLE_H:
            return font, lines
    font = ImageFont.truetype(ttf, lo)
    return font, wrap(draw, text, font, max_w)


def wrap_parts(draw, parts, font, max_w):
    """Greedy-wrap whole phrases, re-joining each line's phrases with SUB_SEP.

    Word-wrapping a role line — `A · B · C` — lets a line end on the separator:
    the music card's first pass read "AI Engineer · Data & AI Systems Architect ·"
    and then dropped "Professional Musician" onto the next line, which looks
    like a typo rather than like a list. Wrapping the PHRASES and re-adding the
    separator per line means it can only ever appear BETWEEN two phrases that
    share a line, never at a line's start or end.

    It also keeps a phrase whole, which is the more important half: "Data & AI
    Systems Architect" is one job title and splitting it across two lines reads
    as two.

    Returns None when a single phrase cannot fit on a line by itself — the
    caller steps the size down instead of shipping an overflowing line.
    """
    lines, cur = [], []
    for part in parts:
        if draw.textlength(part, font=font) > max_w:
            return None
        if cur and draw.textlength(SUB_SEP.join(cur + [part]), font=font) > max_w:
            lines.append(SUB_SEP.join(cur))
            cur = [part]
        else:
            cur.append(part)
    if cur:
        lines.append(SUB_SEP.join(cur))
    return lines


def fit_subtitle(draw, text, ttf, max_w, max_lines):
    """fit_title's logic for the subtitle, over phrases rather than words.

    Steps down from SUB_HI so both hire cards land on the same size whatever
    their role lines cost — a pair of cards for one person that set their role
    lines at two different sizes reads as two unrelated templates.
    """
    parts = [p.strip() for p in text.split("·") if p.strip()] or [text]
    for size in range(SUB_HI, SUB_LO - 1, -2):
        font = ImageFont.truetype(ttf, size)
        lines = wrap_parts(draw, parts, font, max_w)
        if lines is not None and len(lines) <= max_lines:
            return font, lines
    # Nothing fit the budget. Fall back to a plain word wrap at the floor size
    # rather than returning None — a card with a cramped subtitle is still a
    # card; a traceback is not.
    font = ImageFont.truetype(ttf, SUB_LO)
    return font, wrap_parts(draw, parts, font, max_w) or wrap(draw, text, font, max_w)


def tracked(draw, xy, text, font, fill, track):
    """Draw text with letter-spacing, which Pillow has no concept of.

    Only the wordmark needs it, and it needs it badly — .nav__wordmark is
    uppercase at 0.12em, and uppercase at zero tracking reads as a different
    piece of branding.
    """
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + track
    return x


# ==========================================================================
# The pieces of the composition
# ==========================================================================

def navy_field():
    """The gradient field, in linear light, plus its vignette."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    t = (yy / (H - 1))[:, :, None]

    top, mid, bot = lin(NAVY_TOP), lin(NAVY_MID), lin(NAVY_BOT)
    upper = top + (mid - top) * np.clip(t / 0.62, 0, 1)
    lower = mid + (bot - mid) * np.clip((t - 0.62) / 0.38, 0, 1)
    canvas = np.where(t < 0.62, upper, lower).astype(np.float32)

    # A wide, very faint wash from the upper left, so the field has a direction
    # to it. Without something like this a flat navy at card size reads as a
    # placeholder swatch rather than as a lit scene.
    r = np.hypot((xx - W * 0.16) / (W * 0.75), (yy - H * 0.02) / (H * 0.95))
    canvas += (0.055 * np.exp(-r ** 1.6))[:, :, None] * lin(LIGHT_EDGE)

    # Corners are pulled back toward --navy, so the card's own edges are never
    # lighter than the page it will sit beside.
    vx, vy = (xx - W / 2) / (W / 2), (yy - H / 2) / (H / 2)
    vig = 1.0 - 0.42 * np.clip(np.hypot(vx * 0.88, vy * 0.82) - 0.34, 0, 2) ** 1.35
    canvas *= vig[:, :, None]
    return canvas


def framed(src, frame_w, inner_h, focus=0.5, vfocus=0.0):
    """A source image in the pages' figure-ground frame, at a given size.

    Mat, 1px hairline, 8px radius — the same three tokens `.shot` uses, so the
    frame on the card and the frame around a screenshot on the page are visibly
    the same object.

    The shot is fitted the way `.path__shot` fits its images — `object-fit:
    cover` — except anchored to the top rather than the middle, because the top
    of an application screenshot is the part that identifies it. Covering rather
    than merely scaling to width is what guarantees the frame actually reaches
    past the bottom edge: scaling to width alone left the two portfolio frames
    ending eight pixels below the canvas, which reads as clipped corners rather
    than as a deliberate bleed.

    `focus` is where the horizontal crop is taken from, 0 for the left edge and
    0.5 for the middle. It exists because an application with a navigation rail
    down its left side has to keep that rail: cropping the SetMaster shot from
    the centre sliced the sidebar through the middle of a word, which reads as a
    broken image rather than as a crop.

    `vfocus` is the same thing vertically, and it DEFAULTS TO 0.0 — the top
    anchor every screenshot inset here has always used, and wants, because the
    top of an application window is what identifies it. It exists for the one
    case that is not a screenshot: a 16:9 piece of art fitted into this wide
    shallow band, where cover-scaling to the width and then taking the top
    strip returns the empty sky above the subject. That trap is real and
    already cost this file once — the AI Command card sidesteps it by feeding a
    4:1 tiled print instead of its 16:9 hero. Setting `vfocus=0.5` centres the
    band on the subject instead, and leaves every existing card untouched.
    """
    inner_w = frame_w - 2 * MAT_PAD
    scale = max(inner_w / src.width, inner_h / src.height)
    big = src.resize((max(inner_w, round(src.width * scale)),
                      max(inner_h, round(src.height * scale))), Image.LANCZOS)
    left = round((big.width - inner_w) * focus)
    top = round((big.height - inner_h) * vfocus)
    shot = big.crop((left, top, left + inner_w, top + inner_h))

    mat = Image.new("RGB", (frame_w, inner_h + 2 * MAT_PAD), FIG_BG)
    mat.paste(shot, (MAT_PAD, MAT_PAD))
    box = [0, 0, mat.size[0] - 1, mat.size[1] - 1]
    ImageDraw.Draw(mat).rounded_rectangle(box, radius=8, outline=FIG_LINE, width=BORDER)

    mask = Image.new("L", mat.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(box, radius=8, fill=255)
    return mat, mask


def logo_alpha(path, size):
    """The constellation wolf keyed off its own navy plate.

    The committed logo is a navy square, and pasting a navy square onto a navy
    gradient shows its seam. Its luminance is used as an alpha instead, so the
    constellation floats on whatever the field happens to be doing behind it.
    The 0.10 floor is above the plate's own luminance and below the faintest
    line in the mark.
    """
    a = np.asarray(Image.open(path).convert("L").resize((size, size), Image.LANCZOS),
                   dtype=np.float32) / 255.0
    return np.clip((a - 0.10) / 0.90, 0.0, 1.0) ** 0.85


# ==========================================================================
# One card
# ==========================================================================

def build(card, ttf):
    out_path = ROOT / card["out"]
    canvas = navy_field()

    # Text is measured on a scratch RGB image; nothing is drawn to the real
    # canvas until the light math below is finished.
    scratch = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(scratch)

    title_font, lines = fit_title(draw, card["title"], ttf, COL_W, card["max_lines"])
    lead = round(title_font.size * TITLE_LEAD)
    title_h = lead * len(lines)

    # An OPTIONAL second line under the title, in --muted, above the coral rule.
    #
    # WHY THIS EXISTS, and why it is optional rather than standard. Every card
    # above this one has a subject that is a thing — a document, a product, a
    # program — and one string names it. The two hire/ cards are the only ones
    # whose subject is a PERSON, and a person needs two strings: the name, which
    # is the identity, and the role line, which is the only thing distinguishing
    # two cards for two framings of the same résumé. Folding both into one
    # auto-fitted title sets them at the same size, which buries the name; and
    # at a 360px tile the two hire cards would then differ only in the tail of a
    # wrapped line. So the name gets the display size and the roles get a
    # reading line, exactly the way .hero__name over .hero__role sets them on
    # the page this card is quoting.
    #
    # A card that does not ask for one is untouched — the five above still
    # render byte-identical, the same discipline framed()'s `vfocus` argument
    # was added under.
    sub_font, sub_lines, sub_lead, sub_h = None, [], 0, 0
    if card.get("subtitle"):
        sub_font, sub_lines = fit_subtitle(
            draw, card["subtitle"], ttf, COL_W, SUB_MAX_LINES)
        sub_lead = round(sub_font.size * SUB_LEAD)
        sub_h = SUB_GAP_ABOVE + sub_lead * len(sub_lines)

    rule_y = TITLE_TOP + title_h + sub_h + RULE_GAP_ABOVE
    inset_y = rule_y + RULE_H + RULE_GAP_BELOW

    # --- the insets, laid out across the same column the text uses ----------
    n = len(card["insets"])
    frame_w = (COL_W - PANEL_GAP * (n - 1)) // n
    inner_h = (H - inset_y) + BLEED - MAT_PAD
    frames = []
    # A spec is (path, crop, focus) or (path, crop, focus, vfocus). The fourth
    # element is optional so that every card written before vfocus existed keeps
    # its top-anchored crop without being touched.
    for i, spec in enumerate(card["insets"]):
        rel, crop, focus = spec[:3]
        vfocus = spec[3] if len(spec) > 3 else 0.0
        src = Image.open(ROOT / rel).convert("RGB")
        if crop:
            src = src.crop(crop)
        mat, mask = framed(src, frame_w, inner_h, focus, vfocus)
        frames.append((mat, mask, MARGIN + i * (frame_w + PANEL_GAP)))

    # A rim of light along each frame's top edge and upper sides. The screenshots
    # are near-black, so without this they read as holes punched in the field
    # rather than as objects sitting in front of it — the single tell that most
    # gives away an image pasted onto a background.
    rim = np.zeros((H, W), dtype=np.float32)
    for mat, _mask, fx in frames:
        x0, x1 = fx, fx + mat.size[0]
        span = np.linspace(-1.0, 1.0, x1 - x0, dtype=np.float32)
        rim[inset_y:inset_y + 2, x0:x1] = np.exp(-(span / 0.70) ** 2)
        depth = min(H - inset_y, 170)
        side = np.linspace(1.0, 0.0, depth, dtype=np.float32) ** 2.0
        for sx in (x0, x1 - 2):
            reg = rim[inset_y:inset_y + depth, sx:sx + 2]
            rim[inset_y:inset_y + depth, sx:sx + 2] = np.maximum(reg, side[:, None] * 0.65)
    canvas += (blur(rim, 1.6) * 0.26 + blur(rim, 11.0) * 0.30)[:, :, None] * lin(WHITE)

    # --- the coral rule and its glow. One coral use. ------------------------
    rule = np.zeros((H, W), dtype=np.float32)
    rule[rule_y:rule_y + RULE_H, MARGIN:MARGIN + RULE_W] = 1.0
    canvas += (blur(rule, 40) * 0.55 + blur(rule, 12) * 0.45)[:, :, None] * lin(CORAL) * 0.60

    # --- the wolf, keyed onto the field -------------------------------------
    la = logo_alpha(ROOT / card["logo"], LOGO)
    ly, lx = WORDMARK_TOP, MARGIN
    region = canvas[ly:ly + LOGO, lx:lx + LOGO]
    canvas[ly:ly + LOGO, lx:lx + LOGO] = (
        region * (1.0 - la[:, :, None]) + lin(WHITE) * la[:, :, None])

    # --- linear light is done; everything from here is flat paint -----------
    out = Image.fromarray((np.clip(linear_to_srgb(canvas), 0, 1) * 255 + 0.5).astype(np.uint8))
    draw = ImageDraw.Draw(out)

    draw.rectangle([MARGIN, rule_y, MARGIN + RULE_W - 1, rule_y + RULE_H - 1], fill=CORAL)

    wm_font = ImageFont.truetype(ttf, WORDMARK_SIZE)
    tracked(draw, (MARGIN + LOGO + 18, WORDMARK_TOP + (LOGO - WORDMARK_SIZE) // 2 - 3),
            "WOLFPACK DATA & STRATEGY", wm_font, MUTED, WORDMARK_TRACK)

    for i, line in enumerate(lines):
        draw.text((MARGIN, TITLE_TOP + i * lead), line, font=title_font, fill=WHITE)

    # --muted on the navy field, the same pairing .hero__role uses, and the same
    # colour the wordmark row above already carries — so the card gains a line
    # of text without gaining a value.
    sub_top = TITLE_TOP + title_h + SUB_GAP_ABOVE
    for i, line in enumerate(sub_lines):
        draw.text((MARGIN, sub_top + i * sub_lead), line, font=sub_font, fill=MUTED)

    for mat, mask, fx in frames:
        out.paste(mat, (fx, inset_y), mask)

    # --- grain, and out ------------------------------------------------------
    # A gradient this wide bands visibly in 8-bit without it, and LinkedIn's own
    # re-encode makes the banding worse rather than better. Fixed seed, so the
    # file is byte-reproducible.
    rng = np.random.default_rng(11)
    final = np.asarray(out, dtype=np.float32) / 255.0
    final += rng.normal(0.0, 0.45 / 255.0, final.shape).astype(np.float32)
    out = Image.fromarray((np.clip(final, 0, 1) * 255 + 0.5).astype(np.uint8))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_path, optimize=True)
    kb = out_path.stat().st_size / 1024
    sub = f"  sub {sub_font.size}px x{len(sub_lines)}" if sub_lines else ""
    print(f"wrote {card['out']}  {out.size[0]}x{out.size[1]}  {kb:.0f} KB  "
          f"title {title_font.size}px x{len(lines)}{sub}")


# ==========================================================================
# The cards
# ==========================================================================

CARDS = [
    {
        # The music-gear M&A case study. THE INSET CHANGED ON 2026-08-17 (#226),
        # from the transaction map to the page's new hero art, and the old
        # reasoning is worth keeping because it was right at the time.
        #
        # It ran on the map because the map was the best art this case study
        # owned: at a 360px Featured tile the inset is TEXTURE, and forty-two
        # labelled events across four lanes reads unmistakably as a dense
        # research document, where a crop of the report's prose would read as any
        # page of any website. That argument was never about the map — it was
        # about density. The hero wins on the same test and then some: twelve
        # lit brand tiles converging on a core is legible as a SUBJECT at 360px,
        # which the map's four-lane scatter is not.
        #
        # The map has not been demoted anywhere else. It is still the figure the
        # report is built around, still rendered live by map.js, and
        # planning/card/capture_map.py still exists to photograph it — nothing
        # here reads that capture any more, so re-run it only for the map's own
        # sake.
        #
        # ONE THING NOT TO DO WITH THIS CARD: the hero contains a rendered
        # market-share panel whose percentages are invented art. They must never
        # be quoted in the title, in a post that shares this card, or anywhere
        # else. The case study labels the figure an illustration inside the
        # figure itself for exactly this reason.
        "out": "case_studies/case-study-assets/img/og-consolidation-under-pressure.png",
        "logo": "case_studies/case-study-assets/img/wolfpack-logo.png",
        "title": "Consolidation Under Pressure",
        "max_lines": 2,
        # Centred BOTH ways, and the vertical half is the load-bearing one. The
        # composition reads left-to-right — brands, core, chart — so a
        # horizontal focus off 0.5 would drop either the inputs or the outcome.
        # The 0.5 VERTICAL focus is what puts the core in the band at all: this
        # is 16:9 art in a roughly 4:1 slot, so the default top anchor returned
        # the empty upper third with the octagon cropped away entirely, and the
        # one thing it did show large was the render's invented -23.6%. Centring
        # fixes both — see framed()'s docstring.
        "insets": [("case_studies/consolidation_under_pressure/planning/hero/"
                    "consolidation-under-pressure-hero-blue-neon.png", None, 0.5, 0.5)],
    },
    {
        # The Wolfpack AI Command case study. THE INSET IS NOT WHAT THE PAGE'S
        # OWN HEAD COMMENT BRIEFED — that brief named F1, the split diagram, and
        # F1 is still a `.ph` placeholder. Briefing a card against art that does
        # not exist is how a card never gets built, so it is built from the art
        # that does: the shield.
        #
        # Specifically the TILED PRINT rather than the single shield hero, and
        # the reason is this file's own 360px constraint. The inset is a wide,
        # shallow band running off the bottom edge — roughly 4:1. The hero is a
        # single centred shield on a mostly empty field: crop it to 4:1 and you
        # get either a sliver of shield or a band of empty navy. The print is an
        # allover monogram, so a band of it is full of whole shields at any crop,
        # and at a 360px Featured tile it reads unmistakably as one brand's mark
        # repeating — which is exactly the "treat the inset as texture" rule.
        #
        # The crop takes one full row of shields with the row below entering, in
        # the print's own pixels (2100x1181). framed() anchors to the top, so the
        # top row stays whole and the partial row does the bleeding.
        #
        # The source lives under planning/ and never deploys, like the map
        # capture above — social-cards/ builds inputs, and an input is allowed to
        # come from a folder the site does not publish.
        "out": "case_studies/case-study-assets/img/og-wolfpack-ai-command.png",
        "logo": "case_studies/case-study-assets/img/wolfpack-logo.png",
        "title": "An AI Operating Layer for Streamlining Project Delivery",
        "max_lines": 3,
        "insets": [("case_studies/wolfpack-ai-command/planning/hero/"
                    "wolfpack-ai-command-shield-print.jpg", (0, 236, 2100, 800), 0.5)],
    },
    {
        # The SetMaster 3 case study. The inset is the track-playlist matrix and
        # deliberately NOT the set editor: the set editor is already the product
        # page's og:image, and two LinkedIn Featured tiles carrying the identical
        # screenshot read as one duplicated post (plan D-002).
        "out": "sm3-specific-pages/sm3-assets/img/og-setmaster3-case-study.png",
        "logo": "sm3-specific-pages/sm3-assets/img/wolfpack-logo.png",
        "title": "SetMaster 3: From a Spreadsheet on a Plane to a Robust Application",
        "max_lines": 3,
        "insets": [("sm3-specific-pages/sm3-assets/img/a01-track-playlist-matrix.png",
                    None, 0.5)],
    },
    {
        # Two applications side by side rather than one, so the card reads as a
        # body of work rather than as a single product — which is the entire
        # difference between this page and the SetMaster pages.
        "out": "portfolio/img/og-portfolio.png",
        "logo": "portfolio/img/wolfpack-logo.png",
        "title": "Portfolio & Case Studies",
        "max_lines": 2,
        # SetMaster is cropped from its left edge so its navigation rail survives;
        # the e-commerce render is a symmetrical illustration and crops centrally.
        "insets": [("portfolio/img/app-setmaster.png", None, 0.0),
                   ("portfolio/img/app-ecommerce-intelligence.jpg", None, 0.5)],
    },
    {
        # The claude-memory-by-surface infographic is the only coaching graphic
        # approved for public use; the others are reserved for live sessions.
        # It is cropped to its four panels because the full graphic carries its
        # own wordmark and its own title, and a card with two of each reads as a
        # screenshot of a poster rather than as a card. The crop is in the
        # source's own pixels (1694x929).
        "out": "ai-coaching/img/og-ai-coaching.png",
        "logo": "ai-coaching/img/wolfpack-logo.png",
        "title": "AI Coaching for Professionals",
        "max_lines": 2,
        "insets": [("ai-coaching/img/claude-memory-by-surface.png",
                    (44, 186, 1650, 815), 0.5)],
    },

    # ----------------------------------------------------------------------
    # The two hire/ résumé pages (#230). THESE TWO REVERSE D-004 of
    # docs/social-cards-and-linkedin-readiness-plan.md, which kept them on the
    # 200x200 logo and `twitter:card: summary` because they "are not primarily
    # share targets". Ry reversed that on 2026-08-18 for these two pages ONLY —
    # `rates/`, `github/` and `roi-calculator/` still stand under D-004, and a
    # session that finds those and "upgrades" them has reversed a decision
    # nobody made. The reasoning for the reversal is that these are the pages Ry
    # SENDS: pasted into a LinkedIn message, an email, or an application form,
    # the preview is the first thing a hiring manager sees, which makes them the
    # most share-targeted pages here rather than the least.
    #
    # RY'S CONSTRAINT, and it is the design constraint on both: NO HEADSHOT.
    # hire/assets/img/ryan-hickey-portrait.jpg is on both pages and is not on
    # either card. So the cards argue from the work instead of from the face —
    # which is also why they carry a subtitle: with no portrait, the role line
    # is the only thing telling a reader which of the two résumés this is.
    #
    # They are the only cards here that share a folder, because hire/ is the one
    # page folder that deploys as a single unit with one shared assets/. The
    # other cards each sit in their own page folder or in a shared asset folder
    # that deploys beside it.
    {
        # The engineering framing. Two panels, the same "body of work rather
        # than a single product" reasoning the portfolio card carries — and
        # deliberately NEITHER of the portfolio card's two panels, so the two
        # never read as one duplicated post if both are ever shared.
        #
        # The pairing is doing work: the $30M backbone render is architecture
        # and the pdpd screenshot is shipped software, which is the claim this
        # page makes about him. A second dark render instead of the screenshot
        # was tried on paper and rejected — app-ecommerce-intelligence.jpg is
        # so close in composition to app-data-backbone.jpg (inputs left, lit
        # core centre, chart panel right) that side by side they read as one
        # image printed twice.
        "out": "hire/assets/img/og-ryan-hickey.png",
        "logo": "hire/assets/img/wolfpack-logo.png",
        "title": "Ryan Hickey",
        "subtitle": "AI Engineer · Data & AI Systems Architect · COO",
        "max_lines": 1,
        # The backbone render is 16:9 art, not a screenshot, so it takes
        # vfocus=0.5 for the reason framed()'s docstring gives: top-anchoring a
        # wide shallow crop of 16:9 art returns the empty sky above the subject.
        # pdpd is a screenshot and keeps the top anchor, cropped from its LEFT
        # edge so the "pdpd." wordmark and the nav survive — the same reason the
        # portfolio card left-crops SetMaster for its rail.
        "insets": [("hire/assets/img/app-data-backbone.jpg", None, 0.5, 0.5),
                   ("hire/assets/img/app-pdpd.png", None, 0.0)],
    },
    {
        # The music framing. ONE full-width panel against its sibling's two, and
        # the difference in structure is deliberate: these are two cards for two
        # framings of one person, so they have to be told apart at a glance and
        # a subtitle alone does not do that at 360px.
        #
        # SetMaster is the whole reason this framing exists — it is the music
        # page's first application and the only one of the eight that is music
        # technology. There is no other music asset in hire/assets/img/ that
        # can carry a wide shallow band: the RML mark is 298x115 and is a
        # lockup, not a subject.
        #
        # The top-anchored crop lands on the Playlist Compare Tool header, which
        # is the most legible-as-music band in the shot: the RML SetMaster title
        # bar, DJ set names down the rail, and TRAKTOR / SPOTIFY column heads.
        # It is a third distinct SetMaster screen — the product page's card uses
        # the set editor and the case study's uses the track-playlist matrix —
        # so nothing here duplicates a card that already exists.
        "out": "hire/assets/img/og-ryan-hickey-music.png",
        "logo": "hire/assets/img/wolfpack-logo.png",
        "title": "Ryan Hickey",
        "subtitle": "AI Engineer · Data & AI Systems Architect · Professional Musician",
        "max_lines": 1,
        "insets": [("hire/assets/img/app-setmaster.png", None, 0.0)],
    },

    {
        # The pilot project offer page (#236). Two panels, the portfolio card's
        # "a body of work rather than a single product" reasoning applied to a
        # different claim: these are the TWO SYSTEMS THE PILOT INCLUDES, so the
        # card shows what the fee buys beyond the weeks rather than illustrating
        # the consultancy in general.
        #
        # NEITHER PANEL APPEARS ON ANY OTHER CARD, and that is checked rather
        # than assumed — the portfolio card runs SetMaster + e-commerce, the two
        # hire/ cards run the backbone, pdpd and SetMaster, and the three case
        # studies run their own heroes. Two Featured tiles carrying the same
        # screenshot read as one duplicated post (plan D-002), and this page is
        # one Ry will paste beside the others.
        #
        # The AI Command panel is app-notion-system.png rather than the shield
        # print, DESPITE the print being the better-behaved 4:1 band: the print
        # is already the AI Command case study's inset, and that case study is
        # linked from this very page. Two tiles, one monogram, one post — the
        # exact failure the paragraph above exists to prevent. The screenshot is
        # 543x506, the smallest source any card here uses, and it fits the 502px
        # inner width with 8% to spare; it does NOT upscale, but it has no room
        # to lose either, so re-check the scale before changing panel geometry.
        #
        # NO PRICE IN THE IMAGE (plan A-5, Ry 2026-08-18). The subtitle says
        # "fixed fee" and the page says $5,000, so a fee change is a one-line
        # HTML edit and never a card rebuild.
        "out": "pilot-project/img/og-pilot-project.png",
        "logo": "pilot-project/img/wolfpack-logo.png",
        "title": "Let’s talk pilot project.",
        "subtitle": "Fixed fee · Two to three weeks · Two systems you keep",
        "max_lines": 2,
        # Both are screenshots and keep framed()'s top anchor — the top of an
        # application window is what identifies it. BQL crops centrally (its
        # console is symmetrical); the Notion board crops from its LEFT edge so
        # the board's first column and its titles survive, the same reason the
        # portfolio card left-crops SetMaster for its rail.
        "insets": [("portfolio/img/app-bql.jpg", None, 0.5),
                   ("portfolio/img/app-notion-system.png", None, 0.0)],
    },
]


# ==========================================================================
# The emblem card — a different composition, for a card with no screenshot
# ==========================================================================

# Geometry for the emblem layout. The emblem is right-aligned and the text
# block is centred against it, rather than the text-then-inset stack the
# screenshot cards use.
EMBLEM = 400
EMBLEM_GAP = 48                      # clear space between text column and emblem


def build_emblem(card, ttf):
    """A card whose subject is a brand mark rather than a screenshot.

    WHY THIS IS NOT `build()`. Every card above ends in a framed screenshot
    bleeding off the bottom edge, and `framed()` puts the pages' figure-ground
    frame around it — a #0A0A0A mat and a 1px hairline. That frame is right for
    a screenshot, which is a picture *of* something and reads as a window. It is
    wrong for the constellation, which is a mark on a navy plate: framing it
    would draw a box around the one element whose whole behaviour is to float on
    the field. `logo_alpha()` already keys this exact mark off its own plate for
    the 44px wordmark — this is that, at 400px.

    Everything else is deliberately shared with `build()`: the same navy field,
    the same wordmark row, the same auto-fitted Roboto 700 title, exactly one
    coral rule, the same grain and the same fixed seed. A reader seeing this
    card beside the other seven should not be able to say which generator drew
    which.

    The text block is centred vertically instead of hanging from TITLE_TOP.
    With no inset to sit above, a top-anchored title leaves a third of the card
    as empty navy under the rule, which reads as a card that failed to finish
    loading rather than as a composition.
    """
    out_path = ROOT / card["out"]
    canvas = navy_field()

    scratch = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(scratch)

    col_w = W - MARGIN - EMBLEM - EMBLEM_GAP - MARGIN
    title_font, lines = fit_title(draw, card["title"], ttf, col_w, card["max_lines"])
    lead = round(title_font.size * TITLE_LEAD)
    title_h = lead * len(lines)

    # Centre title + rule in the band below the wordmark, above the bottom margin.
    block_h = title_h + RULE_GAP_ABOVE + RULE_H
    band_top, band_bot = WORDMARK_TOP + LOGO + 40, H - MARGIN
    title_top = band_top + ((band_bot - band_top) - block_h) // 2
    rule_y = title_top + title_h + RULE_GAP_ABOVE

    # --- the emblem, keyed onto the field ----------------------------------
    ex, ey = W - MARGIN - EMBLEM, (H - EMBLEM) // 2
    ea = logo_alpha(ROOT / card["emblem"], EMBLEM)

    # A wide, faint wash behind it, so the mark sits in the field rather than on
    # it. Same reason build() rims its frames: a near-black subject on a
    # near-black ground otherwise reads as a hole rather than as an object.
    halo = np.zeros((H, W), dtype=np.float32)
    halo[ey:ey + EMBLEM, ex:ex + EMBLEM] = ea
    canvas += (blur(halo, 34.0) * 0.20)[:, :, None] * lin(LIGHT_EDGE)

    region = canvas[ey:ey + EMBLEM, ex:ex + EMBLEM]
    canvas[ey:ey + EMBLEM, ex:ex + EMBLEM] = (
        region * (1.0 - ea[:, :, None]) + lin(WHITE) * ea[:, :, None])

    # --- the coral rule and its glow. One coral use. ------------------------
    rule = np.zeros((H, W), dtype=np.float32)
    rule[rule_y:rule_y + RULE_H, MARGIN:MARGIN + RULE_W] = 1.0
    canvas += (blur(rule, 40) * 0.55 + blur(rule, 12) * 0.45)[:, :, None] * lin(CORAL) * 0.60

    # --- the wordmark wolf --------------------------------------------------
    la = logo_alpha(ROOT / card["logo"], LOGO)
    ly, lx = WORDMARK_TOP, MARGIN
    region = canvas[ly:ly + LOGO, lx:lx + LOGO]
    canvas[ly:ly + LOGO, lx:lx + LOGO] = (
        region * (1.0 - la[:, :, None]) + lin(WHITE) * la[:, :, None])

    # --- linear light is done; flat paint from here -------------------------
    out = Image.fromarray((np.clip(linear_to_srgb(canvas), 0, 1) * 255 + 0.5).astype(np.uint8))
    draw = ImageDraw.Draw(out)

    draw.rectangle([MARGIN, rule_y, MARGIN + RULE_W - 1, rule_y + RULE_H - 1], fill=CORAL)

    wm_font = ImageFont.truetype(ttf, WORDMARK_SIZE)
    tracked(draw, (MARGIN + LOGO + 18, WORDMARK_TOP + (LOGO - WORDMARK_SIZE) // 2 - 3),
            "WOLFPACK DATA & STRATEGY", wm_font, MUTED, WORDMARK_TRACK)

    for i, line in enumerate(lines):
        draw.text((MARGIN, title_top + i * lead), line, font=title_font, fill=WHITE)

    rng = np.random.default_rng(11)
    final = np.asarray(out, dtype=np.float32) / 255.0
    final += rng.normal(0.0, 0.45 / 255.0, final.shape).astype(np.float32)
    out = Image.fromarray((np.clip(final, 0, 1) * 255 + 0.5).astype(np.uint8))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_path, optimize=True)
    kb = out_path.stat().st_size / 1024
    print(f"wrote {card['out']}  {out.size[0]}x{out.size[1]}  {kb:.0f} KB  "
          f"title {title_font.size}px x{len(lines)}")


EMBLEM_CARDS = [
    {
        # The wolfstrategyllc.com HOMEPAGE card — and the only card here whose
        # destination is not this repo. The homepage is a Wix page, so this file
        # does not deploy through ai-coaching-intake like the other seven; it is
        # uploaded to the Wix Media Manager and set as the site's default social
        # share image. That is why it lives under social-cards/, which never
        # deploys, rather than in a page folder: there is no page folder.
        #
        # It exists because the Wix homepage declared `summary_large_image` and
        # supplied no `og:image` at all, so every share of the site's front door
        # rendered a broken-image placeholder (found 2026-08-17 on a LinkedIn
        # profile Featured tile).
        #
        # THE SOURCE IS SUPPLIED ART, NOT GENERATED. Ry provided
        # wolfpack-constellation-3d-square.png (661x661) on 2026-08-17. It is the
        # master and must not be lost or retouched in place — the same provenance
        # rule the case studies carry, where a supplied hero is as legitimate as
        # a composed one and the delivered original is the thing that is kept.
        #
        # The title is the homepage's own <h1>, verbatim, not copy written here.
        # The same rule the other cards follow — the page's own title — which is
        # also why it is not "Home | WolfStrategyLLC", the Wix <title> written
        # for a browser tab.
        "out": "social-cards/wix/og-wolfstrategyllc-home.png",
        "logo": "portfolio/img/wolfpack-logo.png",
        "emblem": "social-cards/wix/wolfpack-constellation-3d-square.png",
        "title": "Transform Your Data Into Decisions",
        "max_lines": 3,
    },
]


def main():
    with tempfile.TemporaryDirectory() as tmp:
        ttf = unwoff(ROBOTO_700_LATIN, Path(tmp) / "roboto-700-latin.ttf")
        for card in CARDS:
            build(card, ttf)
        for card in EMBLEM_CARDS:
            build_emblem(card, ttf)


if __name__ == "__main__":
    main()
