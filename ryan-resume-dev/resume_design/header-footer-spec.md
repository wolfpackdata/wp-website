# Résumé header & footer — specification

The buildable half of this package. Every value here is realized in
`templates/css/resume-brand.css` and rendered to `preview/`, so the spec and the
artifacts can't drift — if you change one, re-run the export and check the other.

Rationale for the colors, fonts, and marks lives in `brand-reference.md`.

> **v2.2 — the shipped résumé no longer embeds the banner.** The header is
> plain text on every build; see §9 for why. §§2–5 still describe the banner
> because the artboards remain the **design record** of what the header says
> and how it is composed, and because `resume_build/resumekit/brand.py` mirrors
> their strings — `verify_facts.py` check 4 fails if the two drift. Nothing in
> §§2–5 describes a file that ships.

---

## 1. Which variant goes where

Two résumés. The **only** differences are one phrase in the role line and,
in the artboards, the presence of the RML mark.

| Résumé folder | Aimed at | Artboard | Role line ends |
|---|---|---|---|
| `eng_music_combo/` | Music-adjacent companies | `*-music` | `… · COO · Professional Musician` |
| `eng_only/` | Everyone else | `*-eng` | `… · COO · Technical Operator` |

The artboards carry two further axes — **field** (dark navy / light white) and
**height** (standard 1.333in / compact 1.0in) — giving 8 headers pre-rendered in
`preview/`, plus 2 footers and 2 full-page proofs. Since v2.2 neither axis
reaches a résumé: the built document has one header and it is text. They survive
as the design record and as source material for anything else that needs a
Wolfpack masthead.

---

## 2. Header geometry (artboards)

Artboard: **7.5in × 1.3333in** (compact: **7.5in × 1.0in**), which is exactly the
Letter text column at 0.5in side margins. Exported at 300 DPI → **2250 × 400 px**
(compact **2250 × 300 px**).

Composition — two rows, because the contact line is the longest string in the
piece and forcing it into the same row as the marks pushes the type below
readable size:

```
 ┌─────────────────────────────────────────────────────────────────┐
 │  ┌────┐ │  RYAN HICKEY                              ┌────────┐  │
 │  │wolf│ │  AI Engineer · Data & AI Systems Arch…    │  RML   │  │   row 1
 │  └────┘ │                                           └────────┘  │
 │         ────────────────────────────────────────────────────    │   hairline
 │           ryan@… · linkedin.com/in/… · github.com/… · SF Bay   │   row 2
 ╞═════════════════════════ coral 3px ═════════════════════════════╡
```

| Element | Standard | Compact |
|---|---|---|
| Side padding | 0.28in | 0.26in |
| Wolf mark | 0.6in square, 3px radius | 0.42in square |
| Gap between row-1 items | 0.18in | 0.14in |
| Vertical hairline | 1px × 0.62in | 1px × 0.46in |
| Text-column indent (rows 1 & 2 share it) | 0.96in + 1px | 0.70in + 1px |
| Horizontal hairline | 1px, indented, 0.075in above / 0.065in below | 0.05in / 0.045in |
| RML mark height (dark) | 0.38in | 0.27in |
| RML chip (light) | 0.38in + 0.06in/0.08in padding, 3px radius | same, scaled |
| Coral rule | 3px, full bleed, bottom edge | 3px |

Row 2 is indented to align with the name, so the left edge of the type column is
one unbroken line from the name down through the contact string. That alignment
is the composition — don't break it to gain width.

## 3. Type

| Element | Family | Weight | Size | Tracking | Case |
|---|---|---|---|---|---|
| Name | Roboto | 700 | **27pt** (compact 21pt) | 0.005em | UPPERCASE |
| Role line | Montserrat | 600 | **8pt** (compact 7.5pt) | 0.03em | Title Case |
| Contact line | monospace | 400 | **6pt** | 0.015em | as typed |
| Footer | monospace | 400 | **6.5pt** | 0.06em | UPPERCASE |

Line-height on the name is 1.02 — tight, because a single uppercase line has no
descenders and default leading leaves it floating.

## 4. Color and the coral ration

| Element | Dark banner | Light banner |
|---|---|---|
| Field | `#000B29` | `#FFFFFF` |
| Name | `#FFFFFF` | `#000B29` |
| Role line | `#BFC2CA` | `#4A5068` |
| Contact line | `#BFC2CA` | `#6B7186` |
| `·` separators | `#808594` | `#9AA0B0` |
| Hairlines | `#222E52` | `#D8DBE4` |
| The rule | `#F95954` | `#F95954` |

**Coral appears in exactly three places across the whole résumé**, and no single
artboard uses more than two:

1. the rule under the header — 3px at the bottom of a banner artboard,
   2.25pt as the contact line's bottom border on the shipped résumé
2. the 0.75pt hairline at the top of the footer
3. the 2.25pt rule under a body section heading

Since v2.2 all three are Word paragraph borders and the generator emits every
one of them — see `resume_build/resumekit/brand.py`. Through v2.1 slot 1 was
baked into the banner PNG.

Not the name. Not the role line. Not a bullet, a date, or a job title. If a
fourth use appears, one of these three has to give it up.

Where coral is ever used as a **fill**, the text on it is navy, never white.

## 5. The marks

- **Wolf** — `assets/wolfpack-logo.png`. Navy field is baked into the PNG, so on
  the dark banner it disappears into the field (intended) and on the light banner
  it reads as a navy chip (also intended, hence the 3px radius). Never recolour
  it, never place it on coral.
- **RML** — `assets/rml-logo.png`, music variant only. White letterforms, so it
  always needs a dark ground: bare on the dark banner, on a navy chip on the
  light one. It is the **only** place a third color family (the orange→violet
  sun) is allowed, and it never shares an artboard with a coral fill.

## 6. Exact content strings

Copy these verbatim. `·` is U+00B7 MIDDLE DOT with a thin space either side — the
site's separator. The current résumé uses `|`; this is a deliberate change.

**Name (both variants)**

```
RYAN HICKEY
```

**Role line — music**

```
AI Engineer · Data & AI Systems Architect · COO · Professional Musician
```

**Role line — engineering**

```
AI Engineer · Data & AI Systems Architect · COO · Technical Operator
```

> **v2 added `COO`** (Ry, 2026-07-30), matching how the public rates page
> introduces him. Each variant carries the shared three plus the one that earns
> its place with that audience. The v1 note here said four titles would not fit —
> that was measured against v0's pairing of two *long* titles (`Technical
> Operator` + `Professional Musician`); `COO` is three characters and the line
> still clears the text column at 8pt with room. Adding a fifth would not.

**Contact line (both variants)**

```
ryan@wolfstrategyllc.com · linkedin.com/in/ryan-hickey-626b2798 · github.com/wolfpackdata · San Francisco Bay Area
```

> **v2 added the GitHub URL** and dropped the contact line from 6.5pt to **6pt**
> to pay for it — four run-in items at 6.5pt overran the right padding, and the
> row is `nowrap` + `overflow:hidden`, so it clipped rather than wrapped. 6pt was
> already the compact banner's contact size, so no new value entered the system.

**Footer**

```
RYAN HICKEY · RYAN@WOLFSTRATEGYLLC.COM · WOLFPACK DATA & STRATEGY        PAGE n OF m
```

On the music résumé, swap the trailing org for `RML CREATIVE` if the piece is
going somewhere the music identity leads.

---

## 7. The footer — build this as Word text, not as an image

The footer artboards exist so the typography is unambiguous, and they are usable
as-is on a one-page résumé where "Page 1 of 1" is noise anyway. **For anything
multi-page, rebuild the strip as native Word text** so the page number is a live
field.

Word recipe:

1. Insert → Footer → Blank. Set the footer distance from edge to **0.42in**.
2. One paragraph. Clear the default tab stops; add a **right-aligned tab stop at
   7.5in**.
3. Paragraph → Borders → **Top border**: color `#F95954`, width **0.75pt**.
   Border options → spacing from text **6pt**.
4. Type: `RYAN HICKEY · RYAN@WOLFSTRATEGYLLC.COM · WOLFPACK DATA & STRATEGY`
   → Tab → `PAGE ` → Insert → Field → **Page** → ` OF ` → Insert → Field →
   **NumPages**.
5. Select all of it: **Consolas 6.5pt**, All Caps on, Font → Advanced →
   **Spacing: Expanded by 0.4pt**. Color `#4A5068`; recolour the page-number run
   to `#6B7186`.

`0.75pt` and `2.25pt` are the print equivalents of the 1px and 3px rules — CSS
px are 1/96in, Word points are 1/72in.

## 8. Placing the header in Word

1. **Page margins must be 0.5in left and right.** The design is drawn on a 7.5in
   text column: the core-expertise table and the footer's right tab stop are both
   measured off it. `builder._setup_page` asserts it.
2. The header is the **first three paragraphs of the document body** — name,
   role line, contact line — not a Word header. Word header/footer content is
   skipped by a good number of parsers (§9), and the footer is deliberately the
   only thing that lives there.
3. Spacing after the contact paragraph: **4pt** to **8pt** before the first
   section heading (`METRICS.header_space_after_pt`, 6pt at default density).

`build.py` does all of this. There is no manual step and no picture to insert.

## 9. The header is text — read this before changing it

This section is the header-specific case of `ats-guidelines.md`, which covers
the same constraint across the whole document. Read that one before changing
anything structural; read this one before changing the header.

**Many applicant tracking systems ignore images entirely, and a good number
ignore Word headers and footers too.** A résumé whose name and contact details
exist *only* inside a banner image parses as a document with no candidate name.

Through v2.1 the résumé had exactly that exposure, and it was not theoretical.
Extracting the text from `Ryan_Hickey_Resume_eng-only_v2.1.docx` — every `<w:t>`
in `word/document.xml`, which is roughly what a parser sees — gave this as the
first string in the document:

```
Professional Summary
```

No name. No email. No LinkedIn, GitHub, or location anywhere in the text stream.
All of it was pixels. A plain-text header existed behind `--header text`, and the
theory was *image banner for a human, text header for a portal* — but that
theory requires remembering, every time, and a résumé that is only sometimes
parseable is one wrong export away from being unparseable.

So since **v2.2 there is one header and it is text**, on every build:

| Line | Format |
|---|---|
| `RYAN HICKEY` | Roboto Bold, 26pt, `#000B29`, All Caps, spacing Expanded 0.3pt |
| Role line | Montserrat SemiBold, 9pt, `#4A5068` |
| Contact line | Consolas, 7.5pt, `#6B7186`, spacing Expanded 0.2pt |
| — | Bottom border on the contact paragraph: `#F95954`, **2.25pt**, 6pt from text |

It carries the banner's design cues — same navy, same coral rule, same mono
contact line — in real, selectable, parseable text.

`verify_facts.py` **check 5** reads the built `.docx` and fails unless the name,
email, LinkedIn, GitHub, and location all extract as text *and* the document
opens with the name. It is the only check that reads the artifact rather than
the YAML, because this is the one property the YAML cannot show.

**Optional, and not currently shipped:** the wolf mark at 0.55in square, **In
Line with Text**, at the start of the name line. An image the parser skips costs
nothing when the text beside it is real. It is the one way to put a mark back on
the page without reopening any of the above.

## 10. Rebuilding after a change

The résumé:

```powershell
cd ..\resume_build ; python build.py ; python verify_facts.py
```

The artboards, when a header string changes (they no longer ship, but §6 and
`brand.py` must keep agreeing with them — check 4):

```powershell
powershell -ExecutionPolicy Bypass -File .\templates\export-png.ps1
```

Renders every artboard in `templates/export/` to `preview/` at 300 DPI.

When the change is to a value in this spec, change it in
`templates/css/resume-brand.css` — the CSS is the implementation, this document
is the record. Changing one without the other is how a design system dies.
