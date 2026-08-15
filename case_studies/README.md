# `case_studies/` — long-form case studies

Client-facing long-form case studies, sharing one stylesheet and one animation script so
they read as a set rather than as pages that happen to look similar.

| Case study | Folder | Planned public URL | Audience | Robots | Status |
|---|---|---|---|---|---|
| **The Model Is Your Business Beacon** | `ops_fin_model_support/` | `intake.wolfstrategyllc.com/ops-fin-model-case-study/` | Founders, directors, and management at startups and SMBs | **indexed** | **Deployed 2026-08-04** (#91), re-deployed same day with its figure placeholders hidden (#99) |
| **Consolidation Under Pressure** | `consolidation_under_pressure/` | `intake.wolfstrategyllc.com/consolidation-under-pressure/` | Founders, directors, and operating executives | **indexed** | **Built 2026-08-11** (#172). Not deployed |
| ↳ its transaction map | `consolidation_under_pressure/transaction-map.html` | `…/consolidation-under-pressure/transaction-map.html` | as above | **noindex** | as above |

Linked from the `.cases` grid on both `hire/` pages, where it replaced the
transaction-tracking placeholder, and from the portfolio page. As of 2026-08-04 it is no longer
the only live card there: the SetMaster 3 case study deployed the same day and its chip became a
link too, leaving one `In preparation` card of three on the `hire/` pages.

## Folder layout

```
case_studies/                ← NOT a deploy path; a workspace
├── README.md                ← this file                        (not deployed)
├── case-study-assets/       ← shared css, js, fonts, img        ┐
├── ops_fin_model_support/                                       │
│   ├── index.html                                               │
│   └── planning/            ← outline, decisions, source brief  │ (planning/
│       └── hero/            ← the hero generator + its source   ├─ never
└── consolidation_under_pressure/                                │  deploys)
    ├── index.html                                               │
    ├── transaction-map.html ← the same figure, full width       ┘
    └── planning/            ← the source document, the brief,   (not deployed)
        │                      and the copy guard
        └── card/            ← the social card's capture generator
```

**A case study may ship more than one page.** `consolidation_under_pressure/` is the first
that does: the report, and the standalone full-width transaction map it links out to. The
second page is `noindex` and carries no Open Graph block — it is reached from the report,
not from a search result or a paste, so there is no card to guard and nothing for
`check_meta.py`'s table to hold. Both pages load the shared stylesheet; neither has any CSS
of its own.

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
  that comment true. Where coral is a fill, text on it is navy, never white (AA). The list of
  *refusals* grew on 2026-08-11 (#172) and the count did not: a report full of source-link
  glyphs, deal-value steps, macro bands and highlighted rows added six new temptations and
  spent nothing.
- **No new hues.** The shared sheet introduces nothing beyond the navy system and a neutral
  figure ground. A table that needs to mark one row important does it with weight and a
  background lift. See the header comment for the reasoning and for how to add an accent
  properly if one is ever genuinely needed.
  - **Two consequences worth knowing before you reach for a colour**, both solved in the
    sheet and both re-usable. **Direction** — a metric up or down — is carried by the glyph
    (▲ ▼ ▬) and by weight, never by a green and a red; a semantic colour pair is atomic and
    neither half earns its way in alone. **Magnitude** — the transaction map's five-step
    deal-value scale — is carried by an ordered ramp built along the figure ground's own
    neutral axis, dark to light on a dark surface. That is a sequential scale in one hue,
    which is what a magnitude actually is; a categorical palette would make it unreadable.
- **A rendered chart sits on the figure ground, a table the reader reads sits on the page.**
  `.figframe` joined `.shot`, `.ph` and `.dtable` in the `--fig-*` scope on 2026-08-11, for
  the reason the ground exists: a chart drawn in HTML is the alternative to a screenshot *of*
  a chart, so it stands exactly where a captured image would. `.rtable` — the long-form
  report table — deliberately does not, because a page whose body is mostly near-black slabs
  stops looking like this site.
- **`overflow-x: auto` does not clip an absolutely positioned descendant.** Both table
  components declare `position: relative` and the reason is written out in the stylesheet. A
  `.visually-hidden` span inside a wide scrolling table escapes to the initial containing
  block and gives the whole document horizontal scroll, while every container still measures
  correctly. The tell is that putting `overflow: hidden` on an ancestor does not fix it.
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
- **Every case study carries the full Open Graph head block.** A case study is a page people
  paste into LinkedIn, so its link preview is part of the page. The block sits immediately
  after the `canonical`/`icon` links and carries, without omissions:
  - `og:type` `article` and `og:site_name` `Wolfpack Data & Strategy`.
  - `og:url`, **identical to the page's `<link rel="canonical">`** — not similar, identical.
  - `og:title`, the `<title>` **minus its `· Case Study` tab suffix**. The suffix is written
    for the browser tab and the SERP; a card headline is neither.
  - `og:description`, derived from the page's `<meta name="description">` — verbatim when it
    fits, trimmed to whole sentences when it does not. LinkedIn truncates around 200
    characters, and a SERP paragraph run through that cut lands mid-clause.
  - `og:image` as an **absolute** `https://intake.wolfstrategyllc.com/…` URL pointing at a
    committed image near 1.91:1, with `og:image:width`, `og:image:height`, and
    `og:image:alt`. Absolute because the card is fetched by a scraper that has no page to be
    relative to — and the URL has to survive the deploy rename, so it is
    `case-study-assets/…`, never the folder name used here.
  - `twitter:card` `summary_large_image`.

  **`social-cards/check_meta.py` guards all of it** and runs over every page that deploys —
  the block existed on neither case study until 2026-08-07 (#161) precisely because nothing
  was watching. **A new case study copies the block from an existing one** and edits the
  values; deriving it fresh from memory is how a page ends up with five of the eight tags.
  See [`docs/social-cards-and-linkedin-readiness-plan.md`](../docs/social-cards-and-linkedin-readiness-plan.md)
  for the sweep that added it and the reasoning behind each choice.
- **This repo serves nothing.** These pages reach the public only by copying into
  `wolfpackdata/ai-coaching-intake`. This repo stays the source of truth, never edit the
  deployed copy, re-copy on change.

## Voice

**Judged by Ry, against no written spec.** This repo carried a voice guide until 2026-08-06
(#150), when it was removed for not being good enough to bind anything. The case studies
already here are the reference: read one before writing the next.

### Tone direction (added 2026-08-15)

Still not a binding spec — but there are now two reference texts that sound like Ry, and
drafts should be checked against them rather than against a generic "polished essay"
register: the beginner DJ gear guide in the `rml-dj-beginner` repo (`index.html`), and
Ry's manual edit pass on the AI Command case study (the working-tree diff folded into the
2026-08-15 tone iteration — see git history). What they have in common:

- **Blunt verdict sentences, often bolded, opening or closing a paragraph.** *"Extremely
  boring."* *"Chaos."* *"Below that line, they're trash."* One or two per section, where
  the argument has actually earned them — not sprinkled as a tic.
- **Personal experience is the evidence.** Dates, own gear, own clients, own mistakes —
  "the first piece of pro audio gear I ever bought, back in 2008" — never abstract
  authority. Hedges are honest and casual: *"my own opinion, from my own experience."*
- **Everyday metaphors over literary ones.** TPS Reports, calling an audible, side
  quests, tanks. If a metaphor needs a humanities degree, swap it for one from an office,
  a stage, or a garage.
- **Plain statements of consequence beat polished aphorisms.** *"For the shareholders
  reading, these symptoms are very expensive"* — not an inverted-clause epigram. One
  clever line per section is plenty; when a draft has two, cut the second.
- **Direct reader address is welcome.** *"Trust me,"* *"I encourage you"* — the reader is
  a person Ry is talking to, not an audience being written at.
- **Enthusiasm is allowed and stated plainly.** Things are perfect, huge, tanks. The
  voice is confident and warm, not measured-at-all-costs.
