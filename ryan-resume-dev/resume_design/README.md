# resume_design — on-brand header & footer package

Everything needed to put a **wolfstrategyllc.com-branded header and footer** on
Ryan Hickey's résumés. Built 2026-07-30 from the live Wix site and the three
off-Wix pages in this repo (`rates/`, `ai-coaching/`, `roi-calculator/`).

**If you only read one thing:** open `preview/page-proof-dark-eng.png` and
`preview/page-proof-light-music.png`. That's the system in context.

**If you're about to change the résumé itself:** read `ats-guidelines.md` first.
A parser reads this document before any person does, and that constraint has
already overruled one design decision here.

---

## What's here

```
resume_design/
├── README.md                  ← you are here
├── brand-reference.md         WHY: the extracted brand system + its sources
├── header-footer-spec.md      WHAT: geometry, type, colour, copy, Word recipes
├── ats-guidelines.md          WHO READS IT FIRST: parser constraints on the design
├── assets/
│   ├── wolfpack-logo.png      constellation wolf (navy field baked in, no alpha)
│   ├── rml-logo.png           RML mark, alpha-keyed — music résumé only
│   ├── rml-logo-crop.png      the raw crop rml-logo.png was keyed from
│   ├── _current-header-for-reference.png   the OLD banner, extracted from the .docx
│   └── fonts/                 Roboto 700 + Montserrat 400/500/600 (woff2)
├── templates/
│   ├── css/resume-brand.css   the implementation — every spec value lives here
│   ├── css/fonts.css          @font-face for the woff2 above
│   ├── export/                12 artboards, one file each
│   ├── index.html             browser gallery — flip between all variants
│   └── export-png.ps1         renders every artboard to preview/ at 300 DPI
└── preview/                   the finished PNGs (this is what goes into Word)
```

## The ready-to-use files

All in `preview/`, all exactly 300 DPI, all exactly 7.5in wide — which is the
Letter text column at 0.5in margins, so they drop into Word at 100% with no
resampling.

| File | Size | Use |
|---|---|---|
| `header-dark-music.png` | 7.5 × 1.33in | `eng_music_combo/` — screen PDF |
| `header-light-music.png` | 7.5 × 1.33in | `eng_music_combo/` — print / portal |
| `header-dark-eng.png` | 7.5 × 1.33in | `eng_only/` — screen PDF |
| `header-light-eng.png` | 7.5 × 1.33in | `eng_only/` — print / portal |
| `header-compact-*.png` | 7.5 × 1.00in | continuation pages, or a tight page 1 |
| `footer-dark.png` / `footer-light.png` | 7.5 × 0.27in | one-page résumés only — see below |
| `page-proof-*.png` | 8.5 × 11in | **review artefacts, not for pasting** |

> ⚠️ **Since v2.2 none of these PNGs go into a résumé.** The header ships as
> plain text on every build, because the picture version put Ryan's name and
> contact details out of reach of an ATS — `ats-guidelines.md` §2 has the
> evidence, `header-footer-spec.md` §9 has the decision. The banners remain the
> **design record** of the header, the source of the strings mirrored into
> `resume_build/resumekit/brand.py`, and usable artwork for anything that isn't
> a résumé.

One thing that has always been true and still is: **the footer is better built
as Word text than pasted as an image**, because the page number needs to be a
live field. The recipe is in `header-footer-spec.md` §7.

## Putting the header on the résumé

Nothing to do. `resume_build/build.py` renders the name, role line, contact line
and coral rule as the first three paragraphs of the document body, from
`brand.CONTACT` and `brand.ROLE_LINES`. There is no picture to insert and no
other kind of header to choose.

Change a header **string** and you change it in two places — the artboard HTML
in `templates/export/` and `brand.py` — then re-run the export. They no longer
share a file, so `verify_facts.py` check 4 is what stops them drifting.

## Changing something

The CSS is the implementation; the spec is the record; the PNGs are output.
Edit `templates/css/resume-brand.css` (or the copy strings in
`templates/export/*.html`), then:

```powershell
powershell -ExecutionPolicy Bypass -File .\templates\export-png.ps1
```

It finds Edge or Chrome, renders each artboard headless at
`--force-device-scale-factor=3.125` (96 CSS dpi × 3.125 = 300 DPI), and prints
the resulting dimensions so you can confirm nothing shifted. Then update
`header-footer-spec.md` to match — a spec that lies is worse than none.

`templates/index.html` opens all the variants side by side in a browser if you'd
rather compare live than flip between PNGs.

## Known gaps

- **The RML mark is salvaged, not original.** It was cut out of the flattened
  banner in the old `.docx` and its black field keyed to transparency. Clean at
  résumé size; not clean enough for anything bigger. If an SVG or an alpha PNG
  exists, replace `assets/rml-logo.png` and re-run the export.
- **The wolf mark has no transparency** — the navy field is part of the PNG. The
  light banner turns that into a deliberate navy chip, which works, but a
  transparent version would open up more layouts.
- **Roboto and Montserrat must be installed as system fonts for Word.** The
  `assets/fonts/` copies are woff2 (web only) and drive the HTML artboards, not
  Word. Install both from Google Fonts. If you won't: Arial substitutes for
  Roboto acceptably, Corbel or Century Gothic for Montserrat, and Consolas is
  already the monospace the design asks for.
