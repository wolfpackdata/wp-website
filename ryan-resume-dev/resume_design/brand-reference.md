# Brand reference — what the résumé is inheriting from

The single source for everything in `header-footer-spec.md`. Read this first if
you're wondering *why* a value is what it is; read the spec if you just need to
build the thing.

Assembled 2026-07-30 from the live Wix site plus the three off-Wix pages in this
repo. Where the site and the pages disagree, **the pages in this repo win** —
they are the newer, hand-built expression of the brand, and their CSS states its
own rules explicitly.

---

## 1. Sources

| Source | What was taken from it |
|---|---|
| [www.wolfstrategyllc.com](https://www.wolfstrategyllc.com) (Wix) | Legal name, wordmark, positioning language, contact address |
| [`rates/css/rates.css`](../../rates/css/rates.css) | Palette, type stack, coral-ration doctrine, hairline/rule system, footer pattern |
| [`ai-coaching/css/coaching.css`](../../ai-coaching/css/coaching.css) | Same system, second confirmation; kicker + `.k` micro-label treatment |
| [`rates/index.html`](../../rates/index.html) · [`ai-coaching/index.html`](../../ai-coaching/index.html) | Nav/brand lockup, footer copy, real contact details |
| [`roi-calculator/`](../../roi-calculator/) | Third confirmation of the same tokens |
| `eng_music_combo/…docx` | The existing header banner (extracted to `assets/_current-header-for-reference.png`) and the RML mark |

Both `rates.css` and `coaching.css` open with the same declaration, which is the
closest thing the brand has to a written standard:

> Navy `#000B29` · coral `#F95954` (rationed) · Roboto 700 headings · Montserrat body

---

## 2. Palette

| Token | Hex | RGB | Role |
|---|---|---|---|
| Navy | `#000B29` | 0, 11, 41 | The brand field. Backgrounds, and the ink colour on white. |
| Coral | `#F95954` | 249, 89, 84 | **Rationed accent.** See §3. |
| White | `#FFFFFF` | 255, 255, 255 | Type on navy. |
| Muted | `#BFC2CA` | 191, 194, 202 | Secondary type on navy — 10.9:1, safe at small sizes. |
| Faint | `#808594` | 128, 133, 148 | 5.3:1 on navy. Separators and micro-labels **only**. |
| Surface | `#0A1435` | 10, 20, 53 | Card fill one step up from navy. |
| Line | `#222E52` | 34, 46, 82 | Hairline dividers inside a navy field. |

The site is dark-only, so it has no on-white greys. These are **added for print**
and are the only tokens in this package that aren't lifted verbatim:

| Token | Hex | Contrast on white | Role |
|---|---|---|---|
| `--ink` | `#000B29` | 19.4:1 | The name. Same navy, used as ink. |
| `--ink-70` | `#4A5068` | 7.9:1 | Role line, footer text, body copy. |
| `--ink-45` | `#6B7186` | 4.8:1 | The smallest grey that still clears WCAG AA. |
| `--ink-sep` | `#9AA0B0` | 3.0:1 | **Decorative separators only** — below AA, never words. |
| `--rule` | `#D8DBE4` | — | Hairline dividers on white. |

### Colours that are NOT in the brand

The current résumé banner uses a yellow-green (`#DADA60` in the contact line and
the baseline stripe) on a near-black field (`#07080B`). Neither appears anywhere
on the website. Sampled from `assets/_current-header-for-reference.png` at
(1000, 555) and (600, 290). **The new system drops both**: near-black becomes
navy `#000B29`, and yellow becomes coral `#F95954` — which restores the tie to
every other Wolfpack surface.

---

## 3. The coral ration — the one rule that matters most

Coral is the brand's only saturated colour, and both stylesheets go out of their
way to enumerate where it may appear so it can't creep. `rates.css` allows it on
the nav CTA, the hero CTA, the featured tier, the call CTA, the coaching ghost
CTA, the contact CTA, link hover, and the focus ring. Nothing else.

**A résumé has no CTAs, so the ration has to be re-derived rather than copied.**
The spec allocates three slots (see `header-footer-spec.md` §3):

1. the 3px rule along the bottom edge of the header banner
2. the 1px hairline along the top edge of the footer
3. the rule under a body section heading

Two hard constraints carry over unchanged:

- **Where coral is a fill, text on it is navy — never white.** White on coral
  fails AA; navy on coral passes. Both stylesheets say so in their header comment.
- **Coral is never a type colour** for anything longer than a label.

---

## 4. Typography

| Use | Family | Weight | Notes |
|---|---|---|---|
| Headings, name, wordmark | **Roboto** | 700 | The only Roboto weight the site self-hosts. |
| Body, role lines, labels | **Montserrat** | 400 / 500 / 600 | 600 is the site's "emphasis" weight. |
| Micro-labels, contact, footer | **monospace** | — | `ui-monospace, "Cascadia Mono", "Roboto Mono", Consolas, monospace`. |

The monospace stack is doing real work: `rates.css` calls it *"the engineering
document voice"*, and it is the whole reason the pages read as technical rather
than as marketing. Every kicker, stat, and footer line on the site is mono,
uppercase, and letterspaced. That is the single most transferable idea for a
résumé, and the spec leans on it for the contact line and the footer.

Recurring type treatments worth keeping:

- **Uppercase + `letter-spacing: 0.12–0.18em`** on wordmarks and kickers.
- **`▸` as the list bullet** (`.hero__stats li::before`), in `--faint`.
- **`·` as the run-in separator** in footers. The current résumé uses `|`; the
  site uses `·`, and the spec switches to it deliberately.

## 5. Marks

| Mark | File | Notes |
|---|---|---|
| Constellation wolf | `assets/wolfpack-logo.png` | 200×200, **navy field baked in — no alpha**. The site's favicon and nav logo. On white it therefore renders as a navy chip; the spec makes that intentional with a 3px radius. |
| RML Creative | `assets/rml-logo.png` | 298×115 **with alpha**, salvaged from the old banner (`assets/rml-logo-crop.png` is the raw crop). White letterforms + orange→violet sun. |

Two things to know about the RML mark:

1. **It is a recovered raster, not an original.** It was cut out of a flattened
   PNG and its dark field keyed to transparency. It's clean at résumé size and
   nowhere near clean enough for anything larger. If an original (SVG, or PNG
   with alpha) exists, drop it in as `assets/rml-logo.png` and re-run the export.
2. **Its letterforms are white**, so it always needs a dark ground. On the light
   banner the spec gives it an explicit navy chip, which also rhymes with the
   wolf chip on the opposite side.

The RML sun is orange/violet and sits outside the two-colour brand. That is
accounted for in the spec: on any artboard carrying the RML mark, it is the sole
place a third colour family is permitted, and it never appears alongside a coral
fill — only alongside the coral hairline rules.

## 6. Other structural motifs carried over

| Motif | Site value | Résumé translation |
|---|---|---|
| Measure | `--measure: 1100px` | 7.5in — the Letter text column at 0.5in margins |
| Corner radius | `--radius: 4px` | 3px on the logo chips (4px reads heavy at print scale) |
| Section rule | `.section--line` — 1px `--line` top border | 2pt coral rule under section headings |
| Footer | wordmark left, mono meta right, hairline above | identical structure, at 6.5pt |
| Voice | "engineering document" — mono labels, quiet greys, one accent | unchanged |

---

## 7. Verified facts (use these, don't retype from memory)

- Legal name: **Wolfpack Data & Strategy LLC**
- Wordmark as set on every page: **Wolfpack Data & Strategy**
- Email on the site and in the current résumé footer: **main@wolfstrategyllc.com**
  (company) / **ryan@wolfstrategyllc.com** (personal — what the résumé uses)
- Phone on the coaching page: **415-371-9613**
- LinkedIn: **linkedin.com/in/ryan-hickey-626b2798**
- Site: **wolfstrategyllc.com**
- Business address: 333 Gellert Blvd, STE 210B, Daly City, CA 94015 — *on the
  Wix site; deliberately not on the résumé, where "San Francisco Bay Area" is
  the right level of precision.*
