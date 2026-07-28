# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com), and this project adheres to
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

### Changed

### Fixed

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

[Unreleased]: https://github.com/wolfpackdata/wp-website/compare/v1.1.0...develop
[1.1.0]: https://github.com/wolfpackdata/wp-website/releases/tag/v1.1.0
