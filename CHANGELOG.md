# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com), and this project adheres to
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- The second case study, **Consolidation Under Pressure**
  (`case_studies/consolidation_under_pressure/`) — a ~6,000-word public-source
  market-intelligence report on M&A in music gear and pro audio, 2016–2026, rebuilt into this
  site's identity from two finished pages in `wolfpackdata/dj-gear-study`. Eleven numbered
  parts, ten data tables, four rendered figures, 43 cited transactions with a per-row source
  gutter, and an interactive transaction map. Public and indexed. Not deployed. (#172)
- `case_studies/consolidation_under_pressure/transaction-map.html` — the same map full width
  in its own tab, `noindex`, reached from the report's "Open full width" affordance. **The
  first case study to ship more than one page.** (#172)
- `case-study-assets/js/map.js` — the transaction map: four industry lanes, a linear
  2014–2026 axis, 42 events, two macro bands, and a real collision-free label-packing pass.
  **One script and one dataset serve both pages**, switched by a `data-fill` flag. The source
  this was rebuilt from shipped the map twice as two copies, and they had already drifted by
  one event — the standalone plotted the April 2025 tariffs and the embedded one did not,
  with nothing able to see it. Label widths are measured with canvas `measureText` rather
  than estimated from character count, because `--mono` is a *system* stack whose metrics are
  unknowable from the build machine. (#172)
- Long-form report components in the shared `case-study.css`, written to be inherited by the
  next report-shaped case study rather than re-derived: `.rtable` (the report table and its
  `Src` gutter), `.figframe` (a rendered chart on the figure ground), `.meters`, `.dumbs`,
  `.story`, `.map`, `.callout`, `.aside--warn`, `.cards`, `.numlist`, `.fx`, `.srclist`,
  `.docmeta`, `.trend`, and a promoted top-level `.chip`. **No per-page stylesheet and no
  inline `<style>`** — the folder rule, held. (#172)
- `--fig-ramp-1`…`-4` — an ordered sequential ramp along the figure ground's own neutral
  axis, dark to light, for the map's deal-value scale. An extension of an existing ramp, not
  a new hue, and contrast-measured against the lighter of the two lane surfaces (3.6 / 6.6 /
  10.6 / 16.7 : 1). "Undisclosed" is drawn as an unfilled ring *outside* the ramp, because an
  absent value is not a small one. (#172)
- `planning/verify_copy.py` — a guard for the report's copy, which now lives in two repos.
  Checks all 186 numeric tokens in the vendored source against the page, the `Src`
  arithmetic (43 rows = 31 links + 12 dashes), every source link's accessible name, the map
  dataset, and the external-resource stance. Fails loudly if its own anchors move. This is
  the fourth duplicated string set on the property and the first of them to be guarded.
  (#172)
- `planning/card/capture_map.py`, and a fourth entry in `social-cards/build_cards.py`. The
  case study's social card insets the transaction map, which exists only as something a
  browser draws — so the capture is generated from the real page and ships with its
  generator, per the repo's standing rebuild-rather-than-retouch rule. The three existing
  cards rebuild byte-identical. (#172)
- `docs/consolidation-case-study-design-plan.md` — the design plan and its 22-entry decision
  ledger, including three decisions flagged for Ry rather than settled. (#172)
- The third case study, **An AI Operating Layer for Streamlining Project Delivery**
  (`case_studies/wolfpack-ai-command/`) — the Wolfpack AI Command system: the project
  manager's role split into a record-keeping half and a judgment half, the first handed to
  governed AI operators under a written, versioned rulebook, with every consequential
  decision left human-gated. Public and indexed. Title and standfirst are Ry's verbatim copy;
  stat tiles carry artifact and method facts only, and the page states plainly that it has no
  measured outcomes. (#174, #176, #178, #180, #188)
- The shield hero (`case-study-assets/img/wolfpack-ai-command-shield-hero.jpg`) and its
  generator `planning/hero/build_hero.py` — a heater shield holding the four Notion database
  icons in a 2x2 grid, composed from the same committed icon SVGs the page's F6 chips
  display, so the emblem cannot drift from the icons the page shows. **The first case study
  hero here that is a generated emblem rather than a screenshot**, and the first figure to
  carry the four semantic hues as figure content under the ruling that keeps them out of the
  stylesheet. It ships as the hero figure between the stat tiles and the `.docmeta` colophon,
  carries no F number, and its build reproduces byte-identically. (#184, #186, #190)
- `og-wolfpack-ai-command.png`, the fifth entry in `social-cards/build_cards.py`, and the
  page's row in `check_meta.py`. The card's brief named the split diagram (F1) as its inset;
  F1 is still a placeholder, so it was built from the art that exists — the tiled shield
  print, cropped to one full row. At the 360px Featured tile this file's header names as the
  hard constraint, an allover monogram is texture in a way one centred shield in a 4:1 band
  is not. The four existing cards rebuild byte-identical. (#190)
- A third card in the portfolio page's `.cases` grid, linking the AI Command case study at its
  deployed URL, added the day it went live. It went in already linked rather than through the
  `.case__chip` "In preparation" device, because the study was published before the card
  existed. Its image is **generated at card width by that case study's own `build_hero.py`**,
  which grew the output-width argument its financial-model counterpart already had — one
  composition, several sizes, never a re-encode of the delivered file. The section lede stopped
  saying "Both are published", a sentence that went wrong the moment a third study existed.
  The page still has exactly one destination, the 30-minute intro call, and coral is still at
  six. (#192)

### Fixed

- `.rtable` and `.dtable` now declare `position: relative`. `overflow-x: auto` clips a wide
  table but does **not** clip an absolutely positioned descendant whose containing block is
  elsewhere — and with no positioned ancestor, "elsewhere" is the page. `.visually-hidden` is
  `position: absolute`, and the report puts one in every unsourced row's source cell; they
  took their static position ~640px into the table, escaped every scroller above them, and
  gave the whole document 269px of horizontal scroll at 390px wide while every container
  still measured correctly. Latent in `.dtable` since it shipped. (#172)
- **The transaction map's macro bands and gridlines were painting *under* the lane surfaces.**
  Every element in the figure is absolutely positioned inside one stacking context, so paint
  order was document order and an opaque lane hid whatever crossed it — a band spanning all
  four lanes was being drawn as stripes through the two lanes that happened to have no
  background. Survivable while half the lanes were transparent, fatal once all four carry a
  tint. The layers are now explicit and named in the sheet: lanes 0, bands and gridlines 1,
  events 2, lane names and year labels 3. Found while colouring the lanes, not reported. (#199)

### Changed

- **The transaction map is coloured by lane, and the shared sheet gained its first data
  hue.** The map has two variables on every dot and only one of them can take hue: a lane
  (macro / software / hardware / retail) is a **category**, so it takes the new
  `--map-l0`…`l3` on the dot's ring, the lane name, the lane's surface wash and its hairline;
  the deal value is a **magnitude** and stays on the neutral `--fig-ramp-1`…`4` fill, which is
  the whole reason that ramp exists. **The two never swap.** `case-study.css`'s "no new hues"
  rule is now "no new hues **in page chrome**" plus one scoped exception written into the
  header, `docs/site-brief.md` §1.6 and `case_studies/README.md`: a figure may spend hue when
  the variable is genuinely categorical, the hue is **redundant** with something already in
  the figure so nothing is its sole carrier, and it touches neither the coral ration nor the
  navy chrome nor a magnitude scale. This **extends** `wolfpack-ai-command`'s D-015 rather
  than breaking it — that ruling put hue in a committed image so the sheet stayed hue-free,
  which a chart drawn in HTML cannot do. **The coral ration is still six.** Every hue and ink
  carries its measured contrast ratio, floors of 7.1:1 and 10.9:1. (#199)
- **The map's year axis now runs along the top as well as the bottom.** The plot is 1600px
  wide at its narrowest and four lanes deep, so dating an event in the first lane meant
  tracking to the far edge of the figure and then all the way down. (#199)
- **Consolidation Under Pressure — three cuts from Ry's second pass.** The 145% China figure
  is out of the "Cut the tail" implication (now "High tariffs"), the "Rebuild deal capability"
  implication is gone, and the "Tariff schedule changes" row is out of the Part Nine watch
  table — with its accessible caption moved from "Eight open questions" to "Seven", a count
  that would otherwise have gone stale silently because nothing on screen contradicts it. Both
  figures survive elsewhere on the page and the cut row carried no `Src` cell, so
  `verify_copy.py`'s numeric check and the 43 / 31 / 12 gutter arithmetic are untouched. (#199)
- **Consolidation Under Pressure — evidentiary corrections from Ry's review.** Four passages
  claimed more than the sources carry, and all four are now stepped down rather than
  restated. **Purchase price minus sale price is a "headline purchase-to-sale consideration
  gap", not a loss** — the difference is $170m against the **$5.1m loss on sale** Etsy's
  FY2025 10-Q actually records, and Sonova, having no exit price, has neither a gap nor a
  loss; a note bolted to the Pattern 1 table now says so. **A transaction timeline
  establishes sequence, not cause** — Part Two no longer claims nearly every failure traces
  to the two macro shocks, and no longer rules out product or competitive factors. **The
  Native Instruments "balance-sheet failure" diagnosis is withdrawn**, along with the
  assertions about Kontakt's and Traktor's market position, because no administrator's
  report, filing or management statement in the sources identifies a cause and no adoption
  series exists — the page had been contradicting its own methodology appendix. **The
  pandemic-spike figures are marked press-reported at the point of use**, with the survey,
  sample and scope named as unknown, and the unquantified software "step-change" is cut. The
  same fault was corrected where it recurred outside the named sections. (#195)
- **`.rtable` is legible as a table.** Cell padding is now larger than the text's own
  leading, and a column hairline in `--line` gives the eye an edge to track along — the two
  faults behind "difficult to read and not recognizable as tables". Both came from a
  component that borrowed `.dtable`'s no-gridlines density without noticing `.dtable` is a
  *figure* of four numbers where this is a 43-row register with prose in two of five
  columns. `.dtable` is deliberately unchanged. New: `.rtable__note` and `.rtable--noted`,
  a note that attaches to a table and, being a sibling rather than a child of the scroller,
  does not slide out of view when the reader scrolls to the column it explains. (#195)
- **The vertical-rhythm ruling (#182) applied to this page.** Twenty inline `margin-top`
  declarations came out; `.k + .section__title` and `.plainlist`'s margins moved into the
  shared sheet, where spacing belongs. The geometry and swatch styles on the figures stay
  inline — those are data, not spacing. (#195)
- **The case study is ~13% shorter in prose** (6.8% net, against roughly 500 words the
  corrections above added). Everything cut was restatement: a duplicated Src explainer, a
  callout restating the pull quote three lines above it, the "money in gear" table whose
  four figures were all already on the page, the "money in music" table folded to a
  sentence, and the source list's trailing domains — 48 sources now hang their link on the
  title instead of a bare hostname, which also gives 48 links a real accessible name. No
  figure, source, caveat or recommendation was cut, and `verify_copy.py` proves it: all 186
  numeric tokens survive. (#195)
- `docs/site-brief.md` — the figure ground's scope now includes `.figframe`; the new
  sequential ramp is documented with its measured contrast; `case_studies/`'s audience and
  exclusions updated; the report-copy guard added to the guarded-strings table. The
  `case_studies/` coral ration is **still six** — the refusal list grew and the count did
  not. (#172)

## [1.3.0] - 2026-08-07

Adds the long-form case studies and the SetMaster 3 product page, then makes the
whole site presentable as a link: every page that deploys now carries an Open
Graph block. The site is about to be the funnel for a LinkedIn campaign, and a
link preview is the first thing anyone sees of it.

### Added

- `case_studies/` — a workspace for long-form, client-facing case studies, with a **shared**
  `case-study-assets/` (CSS, JS, fonts, image) so every case study inherits the same chrome
  and scroll animation rather than re-deriving it. The stylesheet is the generalized
  descendant of `sm3-assets/css/sm3-case.css`: same type scale, same six-use coral ration,
  same reveal timing, with SetMaster's product-specific magenta/cyan palette exception
  dropped and its transition-row table replaced by a reusable `.dtable`. (#91)
- The first case study, **The Model Is Your Business Beacon**
  (`case_studies/ops_fin_model_support/`), arguing that an operational financial model is an
  operating tool that belongs ahead of go-to-market product work. Public and indexed, one
  CTA to the 30-minute call plus a ghost link to the ROI calculator. Ships with `M-01`–`M-06`
  placeholders for the modeling screenshots Ry has yet to capture. (#91)

- `sm3-specific-pages/setmaster3/` — **the SetMaster 3 landing page**, the product page the
  folder has carried a spec for since 2026-07-31. A short hero, then a **two-column install
  band with Windows left and macOS right**, the transition-row explainer, three
  screenshot-led feature rows, four checkable claims, the roadmap band, and the origin story
  ending on the single link to the case study. **One solid CTA, the nav Download.** Both
  install columns are authored in HTML rather than promoted by platform detection, so the
  band is complete with JavaScript off and the page ships no download JavaScript at all.
  Not deployed: `/setmaster3/` still 404s until the folder is copied into
  `ai-coaching-intake`. (#85, #86)
- `sm3-assets/css/sm3-landing.css` — the second stylesheet in that folder, deliberately kept
  apart from `sm3-case.css`. SetMaster 3's own near-black palette on the repo's Roboto and
  Montserrat, with an enumerated accent ration in its header comment: four orange fills, two
  orange text uses, blue for focus only, purple on the section eyebrows and the wordmark
  numeral. (#85)

- `social-cards/` — a card generator and **three generated 1200×627 social cards**, for the
  SetMaster 3 case study, the portfolio page, and the AI coaching page. `build_cards.py`
  composes them from the navy design-system field, the page's own title, and a screenshot
  inset in the same figure-ground frame the pages use; the finished images are committed into
  the page folders that deploy, and the folder that builds them does not. That makes it the
  **fourth exception** to this repo's "no build step" rule, alongside `ryan-resume-dev/`,
  `blog_posts/tools/`, and the financial model hero generator — and it follows the same
  standing convention those set: rebuild rather than retouch, because an asset nobody can
  rebuild is an asset nobody can correct. The SetMaster card is deliberately **not** the
  product page's set-editor screenshot; two Featured tiles carrying the same image read as a
  duplicate. (#161)
- `social-cards/check_meta.py` — a guard over every `index.html` that deploys, asserting the
  required meta set is present, that `og:url` equals the page's canonical, and that every
  `og:image` is an absolute `intake.wolfstrategyllc.com` URL resolving to a committed file.
  Same shape and same reason as `verify_facts.py`: the Open Graph block was missing from two
  public case studies for months because nothing was watching for it. (#161)

### Changed

- **Open Graph tags swept across the site** (#161), so the pages render properly as link
  previews instead of as bare text cards. The blocking case was
  `sm3-specific-pages/setmaster3-case-study/`, which carried **zero** `og:` and `twitter:`
  tags on the eve of going into a LinkedIn Featured section; a sweep of all nine public pages
  found the identical gap on `case_studies/ops_fin_model_support/` and partial blocks
  elsewhere, so it was fixed everywhere at once rather than one page at a time. Six pages
  edited: both case studies gain a full block with a large image — SetMaster 3 a card built
  for it, the financial model its existing beacon hero, which is already purpose-built;
  `portfolio/` and `ai-coaching/` upgrade from a 200×200 logo and a text-only card to
  `summary_large_image`; and `roi-calculator/`, the one page with no `<link rel="canonical">`
  at all, gains one plus a logo card; and `sm3-specific-pages/setmaster3/`, whose block was
  already complete, gains the three `og:image` width/height/alt lines its large card was
  missing, surfaced by the new guard's first run (plan D-106). `rates/`, both `hire/` pages,
  and `github/` are untouched — already complete for their card class. `og:title` drops the `· Case Study` tab
  suffix, and `og:description` is the page's meta description sized to LinkedIn's ~200-character
  truncation. Reasoning and the decisions ledger:
  `docs/social-cards-and-linkedin-readiness-plan.md`.

- **Both SetMaster 3 pages carry the v3.0.4 macOS installer** (2026-08-05), which ships
  macOS as a signed, notarized `SetMaster.app` inside a drag-to-Applications `.dmg`, built
  and acceptance-tested on a Mac for the first time. The landing page's macOS column becomes
  a real download; the case study gains a **The Mac Installer** subsection and loses its
  "Windows is verified end to end, macOS is not" opening. **C-03 narrowed rather than
  lapsed** — both pages now claim Apple silicon, macOS 14 or later, no Intel, and say the
  suites have never run on macOS. **The download links 404 until v3.0.4 is published to the
  public mirror with both artifacts attached.** (#139)
- `blog_posts/2026-08-05-introducing-setmaster/post.md` — the *What Is Not Ready* section
  described the Mac build as waiting on a Mac, which v3.0.4 falsified. The post stays
  unpushed: its **Get SetMaster 3** CTA points at `/setmaster3/`, and its hold note gates the
  push on that URL returning 200. (#139)
- `hire/` — on both résumé pages, the second "In preparation" case-study placeholder is
  replaced by a real, linked card for the financial model case study. It is the only card of
  the three that is a live link, so it carries a button instead of a chip. (#91)
- **British spellings normalized to American** across 19 files, 71 replacements: page copy,
  CSS and JS comments, and planning docs in `case_studies/`, `hire/`, `rates/`,
  `sm3-specific-pages/`, `ryan-resume-dev/`, and `docs/`. Mostly `colour`, `grey`,
  `artefact`, `centrepiece`, `labelled`, and `behaviour`. Done with an explicit word-pair
  list rather than a blanket `-ise` → `-ize` regex, which would have corrupted `advertise`,
  `exercise`, `enterprise`, `analysis`, and a dozen others. `.srt` transcripts are excluded
  as verbatim records, and the `-wards` group is excluded as usage rather than spelling.
  (#93)

## [1.2.0] - 2026-07-31

Adds a fourth site piece — the résumé landing pages — and the build workbench
behind their downloads. Everything here ships to
`intake.wolfstrategyllc.com`; this repo still serves nothing itself.

### Added

- **Two résumé landing pages** at `hire/` (#76) —
  [`/hire/ryan-hickey/`](https://intake.wolfstrategyllc.com/hire/ryan-hickey/)
  (eng-only) and
  [`/hire/ryan-hickey-music/`](https://intake.wolfstrategyllc.com/hire/ryan-hickey-music/)
  (eng-music). Long-scroll pages carrying the full content of both résumés for
  hiring managers, with a career timeline, application portfolio, case studies,
  and `.docx`/`.pdf` downloads. They are **`noindex`, direct-link only** — two
  differently-framed résumés for the same person indexed side by side reads
  badly — and unlike the other page folders they share one `hire/assets/`
  directory rather than carrying their own font copies. Design plan, decisions
  ledger, and acceptance criteria in `docs/hire-pages-design-plan.md`.
- **The résumé build workbench** under `ryan-resume-dev/` (#72) — YAML content
  compiled to on-brand `.docx` by `build.py`, checked against a declared fact
  table by `verify_facts.py`, and exported to PDF and staged into
  `hire/assets/dl/` under their public names by `export_pdf.py`. The rename is
  scripted precisely so a rebuilt résumé can't leave a stale download behind.
- **Canonical tag on the AI Coaching page** (#5) pointing at
  `https://intake.wolfstrategyllc.com/ai-coaching/`, so the github.io copy and
  the intake deploy no longer compete as duplicate content. The tag carries over
  unchanged when the folder is copied into `wolfpackdata/ai-coaching-intake`,
  where it becomes a correct self-referential canonical.

### Fixed

- **The résumés overstated the music career and omitted that the training was
  formal** (#77, résumé v2.4). The landing pages had been corrected two feedback
  rounds earlier and the YAML behind them had not, so the downloads contradicted
  the page offering them — and nothing caught it, because `verify_facts.py`
  reads the YAML rather than the pages. Retired *"a 36-year music career"*
  (which collapsed four different spans and picked the study one) and *"20+
  years of DJ performance"* (four years early); added the training facts to both
  résumés, which had carried none of them. The fact table gained rows for the
  new spans and two `SHARED` guards so the shared sentences can't drift apart on
  one résumé alone.

## [1.1.0] - 2026-07-28

The first tagged version — it marks the site as it stands live today. Everything
below shipped before the repo carried a version, and is recorded here in one
entry so the history isn't lost. Numbers in parentheses are the pull requests
that landed each change in
[wolfpackdata/wp-website](https://github.com/wolfpackdata/wp-website/pulls).

### Added

- **AI Tool ROI calculator** at `roi-calculator/`, the repo's first page, moved
  into its own subfolder so the repo could hold more than one site piece.
- **AI Coaching for Professionals landing page** at `ai-coaching/` (#3) —
  replaces the Wix page at `wolfstrategyllc.com/general-7`. Ships to
  `intake.wolfstrategyllc.com/ai-coaching` by copying the folder into
  `wolfpackdata/ai-coaching-intake`; this repo stays the source of truth.
- **Public, evergreen rates page** at `rates/` (#7) — the indexable sibling of
  the direct-link Q3 page in `wolfpackdata/wp-rates-page`, derived from it under
  `docs/public-rates-consistency-contract.md`.
- **Two "ways to work with Wolfpack" path tiles** on the rates page, first as
  16:9 placeholder slots (#12), then carrying Ry's images (#16).
- **ROI calculator entry points** from both marketing pages — a link in the
  ai-coaching pricing section (#43) and a navy-ghost button in the rates page
  coaching section (#47).
- **Negative results in the ROI calculator** (#41), so the math can tell a
  visitor when a tool doesn't pay for itself.
- Repo bootstrapped to the Wolfpack GitHub SOP, and `CLAUDE.md` grown to record
  page conventions, deploy paths, the Web Property Map session-start staleness
  check, and phone-width verification (#1, #4, #14, #17).

### Changed

- **Same-domain links open in the same tab** across all three pages (#66) —
  links to `wolfstrategyllc.com` and `intake.wolfstrategyllc.com` no longer
  open a new tab, so the browser back button works. Calendar booking CTAs and
  third-party LinkedIn links deliberately still open a new tab.
- **Canonical URLs repointed to the intake domain** — the public rates page
  (#60) and the ai-coaching ROI calculator link (#53), following the ROI
  calculator's move to `intake.wolfstrategyllc.com/roi-calculator/`.
- **Booking CTAs repointed to the intro-call calendar** — the ROI calculator's
  CTA (#35) and, earlier, a correction across pages to the right booking
  calendar (#13).
- **ROI calculator restyled to the Wolfpack design system** (#39) with defaults
  updated to realistic coaching-client numbers (#37).
- **Rates page hero reworked** from Ry's draft-1 feedback (#9), with the lede
  rewritten to invite an exploratory call (#10), and the path cards made to
  scroll to their sections (#63).
- **Rates page synced to the 2026-07-28 Q3 direct-link updates** (#33), with the
  design spec's R9 calendar URL and 3.1 nav brought in line with the same
  rulings (#57).
- **AI coaching page polish** — square headshot in place of the rectangular bio
  portrait (#19), student reviews section hidden until real reviews land (#21),
  pricing card pack line anchored on "save up to 20%" (#25), and the nav CTA
  renamed to "Book an intro" (#27).
- **Skeptic-framing copy dropped** from the rates coaching section (#51) and the
  ai-coaching pricing aside (#54).

### Fixed

- Ability-ladder bars and tier names now anchor to shared rows on the
  ai-coaching page, instead of drifting out of alignment (#23).
- The ROI calculator header uses the Wolfpack logo (#45).
- The 30-minute-call CTAs pointed at the wrong booking calendar (#13).

[Unreleased]: https://github.com/wolfpackdata/wp-website/compare/v1.3.0...develop
[1.3.0]: https://github.com/wolfpackdata/wp-website/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/wolfpackdata/wp-website/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/wolfpackdata/wp-website/releases/tag/v1.1.0
