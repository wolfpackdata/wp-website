# `hire/` — résumé landing pages

Two long-scroll landing pages carrying the full content of Ryan Hickey's two
résumés, aimed at **hiring managers** (not clients — that's `rates/` and
`ai-coaching/`).

| Folder | Source résumé | Public URL |
|---|---|---|
| `ryan-hickey/` | `../ryan-resume-dev/resume_build/content/eng_only.yaml` | `https://intake.wolfstrategyllc.com/hire/ryan-hickey/` |
| `ryan-hickey-music/` | `…/eng_music.yaml` | `https://intake.wolfstrategyllc.com/hire/ryan-hickey-music/` |

The full design plan — concept, IA, decisions ledger, acceptance criteria —
is [`docs/hire-pages-design-plan.md`](../docs/hire-pages-design-plan.md).

## Status

**Deployed 2026-07-31** with wp-website **v1.2.0** (#76, #77) to
`https://intake.wolfstrategyllc.com/hire/…` via `ai-coaching-intake#44`. This repo stays
the source of truth — never edit the deployed copy; re-copy the whole `hire/` folder on
change.

- [x] `assets/fonts/` — 14 woff2 (Roboto + Montserrat)
- [x] `assets/img/` — 8 app screenshots, 3 case-study cards, wolf mark, RML mark,
      portrait, and the 2 built social cards (`og-*.png`, added 2026-08-18, #230)
- [x] `assets/dl/` — both `.docx` and both `.pdf`
- [x] `assets/css/hire.css`
- [x] `assets/js/reveal.js`
- [x] `ryan-hickey/index.html`
- [x] `ryan-hickey-music/index.html`

Verified: zero external requests, zero horizontal overflow at 320/390/768/1024/
1440px, complete render with JS disabled, `verify_facts.py` passing. Full
acceptance list in the plan's §12.

## Three things to know

**1. These pages are `noindex`, direct-link only.** Ry sends the URL; search
engines don't index them. Two differently-framed résumés for the same person
showing up side by side in search results reads badly, which is the whole reason.
Don't add them to a sitemap and don't link them from `rates/`, `ai-coaching/`, or
Wix.

**2. They make a time-sensitive claim.** The hero states that Ry is actively
seeking a role. **When he lands one, these pages need editing or unpublishing** —
they will not quietly age into being harmless.

**3. Shared assets, unlike the other page folders.** `rates/` and `ai-coaching/`
are independent deployments and each carry their own font copies. These two pages
ship as one `hire/` folder, so they share `assets/` and reference it as
`../assets/…`. Keeps them from drifting apart and saves ~8 MB of duplication.

## Content rules

- **Experience bullets and project blurbs are verbatim from the YAML.** Those
  strings are guarded by `resume_build/verify_facts.py`; retyping them here
  creates a second, unguarded copy that will drift. Copy, don't paraphrase.
  **Since `wp-website#95` that guard is real for these pages, not just for the
  YAML:** `verify_facts.py` **check 6** compares every `.app__name` and
  `.app__blurb` in both `index.html` files against the source résumé and reports
  the exact point of divergence. Through v2.4 the checker never opened a web
  page, so an app blurb could be edited here and nothing would notice — the
  `portfolio/` page becoming a third copy is what prompted closing the gap. Note
  the split it enforces: `ryan-hickey/` is checked against `eng_only.yaml`,
  `ryan-hickey-music/` against `eng_music.yaml`.
- **No exceptions left.** These pages ran ahead of the YAML on two music facts
  for two rounds — the tenure split (D-009) and the training (D-010) — and the
  résumé v2.4 round (#77) brought the YAML up to them. Both files now say the
  same thing, so the verbatim rule above holds without a carve-out. The four
  music spans are **four numbers, not one**: 36 years at the piano · 23 years
  paid to perform, since 2003 · 20+ years of studio production · professional DJ
  since 2009. Never collapse them into a single "music career" figure, on either
  side; `verify_facts.py`'s `FIGURES` ledger annotates each one to say so.
- **The two YAMLs file music differently on purpose** — `eng_only` puts RML and
  Niceman *inside* Professional Experience so they read as businesses he runs;
  `eng_music` gives music its own section. Don't flatten that into one template.
- **The case studies section carries the published set, in Ry's order, on both
  pages** (#218, design plan **D-011**): AI Command → SetMaster 3 → Consolidation
  Under Pressure → financial model. **That order is Ry's and re-derives from
  nothing** — not alphabetical, chronological, or by publication date. Don't sort
  it. The four cards are byte-identical across the two pages: unlike the
  applications gallery, this section has no music-vs-engineering framing to keep
  apart, so **change both files or neither**. Nothing here is a placeholder any
  more — the `$30M software spine` card was removed because its study is still
  unwritten, and an `IN PREPARATION` chip on a résumé page reads as an IOU. It
  comes back as a normal card when the study exists. **Neither string in the
  section head counts the cards**, deliberately: the old *"Three builds"* /
  *"Two are published"* pair went stale silently every time a study shipped.
- **Two application tiles link their case study**, the only two whose system has a
  published one: `SetMaster 3` / `RML SetMaster 3` and `Notion–GitHub AI Dev
  Command Center`. The SetMaster tile also links the `/setmaster3/` product page.
  Put these **after `.app__blurb`, never between the name and the blurb** —
  check 6 matches those two as adjacent siblings, so anything between them
  unguards a résumé string *without failing the check*.
- **The coral ration is enumerated in the header comment of `assets/css/hire.css`.**
  Keep that comment true. Where coral is a fill, text on it is navy, never white.
  **Use 5, the `IN PREPARATION` chip, is live but unused since #218** — the
  allowance stays for the next unpublished study, and as everywhere on this site
  the count only ever goes down.
- **The RML mark appears in exactly one place** — the music page's Music &
  Creative Technology section, at ~44px. It's a recovered raster and is not clean
  at larger sizes.
- **Image format is chosen by content, not by habit.** Photographic and rendered
  illustrations are **JPEG** (`app-bql`, `app-data-backbone`,
  `app-ecommerce-intelligence`, the portrait); UI screenshots stay **PNG**,
  because JPEG smears small text. **The two `og-*.png` social cards are PNG
  regardless** — they are mostly a flat navy gradient with large type over it,
  which is what JPEG is worst at, and the generator writes PNG for every card
  on the site. The originals in `wp-rates-page/img/` are all
  PNG — converting the four photographic ones took this folder from 11 MB to
  1.4 MB with no visible difference. If you re-copy an image from that repo,
  re-apply the split.

## Social cards — and why neither one shows Ryan's face

**Added 2026-08-18 (#230).** Each page carries a built 1200×627 card in `assets/img/`:

| Page | Card | What's in it |
|---|---|---|
| `ryan-hickey/` | `og-ryan-hickey.png` | Two panels — the `$30M` backbone render and the pdpd console |
| `ryan-hickey-music/` | `og-ryan-hickey-music.png` | One full-width panel — RML SetMaster 3's Playlist Compare Tool |

- **No portrait, on Ry's instruction**, and `ryan-hickey-portrait.jpg` stays off both. It
  turned out to be the constraint that made them good: with no face to lead on, each card
  argues from the work.
- **They reverse D-004** of `../docs/social-cards-and-linkedin-readiness-plan.md`, which had
  kept both pages on the 200×200 logo because they "are not primarily share targets." That
  had it backwards. These pages are `noindex` — the **only** way anyone reaches one is Ry
  pasting the URL into a message, an email, or an application form, so the preview isn't
  incidental to the visit, it's the first impression. Rulings **D-015** and **D-016** in that
  plan. The carve-out is these two pages; `rates/`, `github/`, and `roi-calculator/` are
  still D-004's.
- **Built by `../social-cards/build_cards.py` — rebuild rather than retouch.** A hand-edited
  card is a card nobody can change again. Re-run it and `python ../social-cards/check_meta.py`
  after any change to a title, a role line, or an inset.
- **These two are the only cards on the site that share a folder**, because `hire/` is the
  only page folder that deploys as a single unit.
- **Neither reuses a `portfolio/` card panel**, so the three never read as one duplicated
  post — D-002's rule, applied outward.
- **A card is not indexing.** `noindex, nofollow` above is untouched; adding a card did not
  make these pages findable, it only changed what a scraper renders when Ry pastes the link.
- **After the intake deploy, run both URLs through the
  [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)** before sharing
  either. LinkedIn reports a URL it has never scraped as "invalid URL" rather than as a
  cache miss — the trap `CLAUDE.md` records from 2026-08-17.

## Deploying

This repo **serves nothing**. These pages go live only by copying `hire/` into
`wolfpackdata/ai-coaching-intake`, which owns `intake.wolfstrategyllc.com`.

The folder here mirrors the deploy path, so it's a single copy of `hire/` into
that repo's root — no path rewriting needed. **This repo stays the source of
truth. Never edit the deployed copy; re-copy on change.**

After shipping, update the Notion **Web Property Map** (linked from `CLAUDE.md`)
and the canonical-URL table in `CLAUDE.md`.

## Rebuilding the downloads

```powershell
cd ..\ryan-resume-dev\resume_build
python build.py ; python verify_facts.py ; python export_pdf.py
```

`export_pdf.py` converts via Word COM and copies all four artifacts into
`assets/dl/` under their public names. Never rename them by hand — the script
owns that mapping so a rebuilt résumé can't leave a stale download behind.
