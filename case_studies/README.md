# `case_studies/` — long-form case studies

Client-facing long-form case studies, sharing one stylesheet and one animation script so
they read as a set rather than as pages that happen to look similar.

| Case study | Folder | Planned public URL | Audience | Robots | Status |
|---|---|---|---|---|---|
| **The Model Is Your Business Beacon** | `ops_fin_model_support/` | `intake.wolfstrategyllc.com/ops-fin-model-case-study/` | Founders, directors, and management at startups and SMBs | **indexed** | **Deployed 2026-08-04** (#91), re-deployed same day with its figure placeholders hidden (#99) |

Linked from the `.cases` grid on both `hire/` pages, where it replaced the
transaction-tracking placeholder, and from the portfolio page. As of 2026-08-04 it is no longer
the only live card there: the SetMaster 3 case study deployed the same day and its chip became a
link too, leaving one `In preparation` card of three on the `hire/` pages.

## Folder layout

```
case_studies/                ← NOT a deploy path; a workspace
├── README.md                ← this file                        (not deployed)
├── case-study-assets/       ← shared css, js, fonts, img        ┐
└── ops_fin_model_support/                                       ├─ deployed
    ├── index.html                                               ┘
    └── planning/            ← outline, decisions, source brief  (not deployed)
        └── hero/            ← the hero image generator + its source capture
```

Like `sm3-specific-pages/`, **this folder's name is not the URL path.** Deploying is a copy
of `case-study-assets/` and the case study's own folder into the `ai-coaching-intake` repo
root, not a copy of `case_studies/` itself. The folder is named `case-study-assets/` rather
than `assets/` for the same reason `sm3-assets/` is: it lands at the intake repo **root**,
which already carries a generic `css/`, `fonts/`, `img/`, and `js/` belonging to the intake
form. Namespacing it means `../case-study-assets/…` resolves identically here and on the
deployed site, so paths are never rewritten.

## Conventions these pages must keep

- **One shared stylesheet, and it is the whole point.** Every case study loads
  `case-study-assets/css/case-study.css`. Do not add a per-page stylesheet and do not write
  inline `<style>`. If a page needs something the shared sheet lacks, add it to the shared
  sheet with a comment explaining why, so the next case study inherits it.
- **`reveal.js` is copied, never rewritten.** It is byte-identical to
  `sm3-assets/js/reveal.js` and `hire/assets/js/reveal.js` apart from its header comment. The
  reveal timing and scroll-spy behavior are supposed to match every other long-form page in
  this repo, and a rewrite is how two pages quietly stop matching.
- **Coral is rationed to six uses**, listed in the header comment of `case-study.css`. Keep
  that comment true. Where coral is a fill, text on it is navy, never white (AA).
- **No new hues.** The shared sheet introduces nothing beyond the navy system and a neutral
  figure ground. A table that needs to mark one row important does it with weight and a
  background lift. See the header comment for the reasoning and for how to add an accent
  properly if one is ever genuinely needed.
- **No external requests.** Fonts and images are self-hosted in `case-study-assets/`, the
  same rule every other page folder in this repo keeps.
- **Placeholders ship, gray boxes do not.** Unshot assets use the `.ph` device, sized at the
  exact final aspect ratio, carrying an ID and a description of what to capture. Dropping the
  real file in changes nothing about the layout.
  - **Exception in force on the financial model page since 2026-08-04 (#99).** Its six `M-nn`
    figures are **commented out** in `index.html`, so the live page shows no unfilled figure
    at all. Ry's call while the captures are outstanding. The rule above answers *what an
    unfilled slot should look like*; this answers *whether one should appear*, and on a public
    page awaiting captures the answer was no. **The markup is commented, never deleted** — the
    ids and descriptions are the capture brief and the layout is already built to take the
    real image. Restoring one is an uncomment; filling one is the `.ph` to `.shot` swap. Do
    not "tidy" these blocks away, and do not restore them without asking. Tracked in the
    Notion task *10. Capture and insert the six financial model case study figures*.
- **The page renders complete with JavaScript off.** The hidden initial state is scoped to a
  `.js` class that `reveal.js` adds. A document that needs JavaScript to be readable is a
  broken document.
- **No client is ever named, and no testimonial is ever invented.** Anonymize by shape.
  Illustrative figures are labeled as illustrative, in the figure itself, not in a footnote.
  - **A screenshot of real client work is anonymized in the pixels, not by being small.**
    The financial model hero was the first case: its source workbook lists team members by
    first name, and "the text is only two pixels tall" is not anonymization, it is a bet
    that nobody will zoom. That column is blurred in the committed source capture *and*
    again at build time, and the figcaption says identifying details are obscured. Check any
    new capture at 5x or 6x before it ships, not at page scale.
- **A generated figure ships with the thing that generated it.** The financial model hero is
  composed, not shot: `ops_fin_model_support/planning/hero/build_hero.py` takes the source
  capture in the same folder and writes
  `case-study-assets/img/fin-model-beacon-hero.jpg`. The generator and its input live under
  `planning/`, so neither deploys, and only the finished image does. An asset nobody can
  rebuild is an asset nobody can correct.
  - Anything generated still answers to the palette rules above. The hero's light is white
    carrying a trace of coral, its fringes are a tint of the navy, and its one coral element
    mirrors the coral border on `.hero__stand` immediately above it on the page. Coral drawn
    inside a JPEG does not spend a use from the stylesheet's ration of six, but it does have
    to look like it belongs to the same system.
- **This repo serves nothing.** These pages reach the public only by copying into
  `wolfpackdata/ai-coaching-intake`. This repo stays the source of truth, never edit the
  deployed copy, re-copy on change.

## Voice

**Judged by Ry, against no written spec.** This repo carried a voice guide until 2026-08-06
(#150), when it was removed for not being good enough to bind anything. The case studies
already here are the reference: read one before writing the next.
