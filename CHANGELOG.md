# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com), and this project adheres to
[Semantic Versioning](https://semver.org/).

## [Unreleased]

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

### Changed

- `hire/` — on both résumé pages, the second "In preparation" case-study placeholder is
  replaced by a real, linked card for the financial model case study. It is the only card of
  the three that is a live link, so it carries a button instead of a chip. (#91)

### Fixed

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

[Unreleased]: https://github.com/wolfpackdata/wp-website/compare/v1.2.0...develop
[1.2.0]: https://github.com/wolfpackdata/wp-website/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/wolfpackdata/wp-website/releases/tag/v1.1.0
