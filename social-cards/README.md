# `social-cards/` — the Open Graph card generator

This folder builds the three social cards the site's `og:image` tags point at. It is a
generator, not a page: **`social-cards/` never deploys.** Like `blog_posts/tools/` and
`case_studies/ops_fin_model_support/planning/hero/`, it produces *inputs* to the site rather
than any part of it, which makes it the fourth exception to this repo's "no build step" rule.

The cards themselves are committed, and they live in the page folders that deploy:

| Output | Consumer page |
|---|---|
| `sm3-specific-pages/sm3-assets/img/og-setmaster3-case-study.png` | the SetMaster 3 case study |
| `portfolio/img/og-portfolio.png` | `portfolio/` |
| `ai-coaching/img/og-ai-coaching.png` | `ai-coaching/` |

All three are exactly **1200×627** — LinkedIn's 1.91:1, at its stated minimum for a large
card — and well under its 5 MB limit.

## Rebuild

```
python social-cards/build_cards.py
```

Run it from the repo root. It rebuilds all three every time, and it is deterministic: no
timestamps, one fixed RNG seed, so the same checkout always produces the same three PNGs.

**These images are generated, and their generator ships with them — rebuild rather than
retouch.** That is the standing convention `fin-model-beacon-hero.jpg` already carries, and
the reason for it is the same: a card that gets hand-edited in an image editor is a card
nobody can change again. Changing a title should be a string edit in `build_cards.py`, not a
design session. If a card needs something the script cannot do, add it to the script.

## What it makes, and the constraint that shapes it

One system across all three cards: the navy field (`--navy #000B29`, the same three-stop
gradient `build_hero.py` uses, summed in linear light), the wordmark row set the way the page
nav sets it, the page's own title, **one** coral rule under it, and a screenshot inset in the
`--fig-bg` / `--fig-line` / 8px-radius frame the pages use, running off the bottom edge.

**The hard constraint is legibility at 360 pixels.** LinkedIn renders a Featured tile at
roughly 360px wide, under a third of the size the card is authored at, and nobody can zoom a
social card. So titles are set at 72–96px on a 1200px canvas and auto-fitted per card — a
short title gets to be enormous, a long one gives up only as much as it has to — and the
screenshot inset is treated as texture rather than as something anyone will read. To check a
change, downscale before you judge it:

```
python -c "from PIL import Image; im=Image.open('portfolio/img/og-portfolio.png'); im.resize((360,188)).save('preview-360.png')"
```

## Fonts

Every font in this repo ships as `.woff2` only, and Pillow cannot read woff2. The script
converts the exact file the page serves to a TTF in a temp directory at build time, with
fontTools, and throws it away. **No font binary is committed here** — a committed copy would
silently drift from the one the pages actually load. The face is Roboto 700 (latin subset),
this repo's heading face in every stylesheet; Montserrat is the body face here and is
deliberately not used.

## Related

`check_meta.py`, beside this file, is the guard that walks every deploying `index.html` and
asserts its Open Graph block is present, absolute, and consistent with the page's canonical —
so a card that exists but is never referenced, or referenced at a path that does not deploy,
fails loudly instead of quietly rendering a blank preview.

One sharp edge: the guard requires every `og:image` to be **git-tracked**, not merely on
disk — that is deliberate (the `sm3-assets/` folder holds a gitignored capture that must
never deploy, and "exists on disk" would wave it through). So after generating a new card,
`git add` it before running the guard, or the guard will correctly refuse it as untracked.
