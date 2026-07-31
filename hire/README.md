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

**First draft complete, not deployed.** Issue #76, branch `feat/76-hire-pages`.

- [x] `assets/fonts/` — 14 woff2 (Roboto + Montserrat)
- [x] `assets/img/` — 8 app screenshots, wolf mark, RML mark, 2 portraits
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
- **Two deliberate exceptions, both music.** **Tenure:** the pages say *36 years
  at the piano · 23 years paid to perform (since 2003) · professional DJ since
  2009*, where `eng_music.yaml` still says *"a 36-year music career"* and *"20+
  years of DJ performance"* (D-009). **Training:** the pages say ten years of
  classical piano study with a university professor and sound engineering
  learned from mentors and paid online programs; neither YAML says any of it,
  and eng-only's panel used to be labelled *"self-taught"* (D-010). **The pages
  are right and the YAMLs are stale** — don't sync them backwards. Fixing the
  résumé is a build round Ry has to open; the exact edits are in the plan's
  §6(c).
- **The two YAMLs file music differently on purpose** — `eng_only` puts RML and
  Niceman *inside* Professional Experience so they read as businesses he runs;
  `eng_music` gives music its own section. Don't flatten that into one template.
- **The coral ration is enumerated in the header comment of `assets/css/hire.css`.**
  Keep that comment true. Where coral is a fill, text on it is navy, never white.
- **The RML mark appears in exactly one place** — the music page's Music &
  Creative Technology section, at ~44px. It's a recovered raster and is not clean
  at larger sizes.
- **Image format is chosen by content, not by habit.** Photographic and rendered
  illustrations are **JPEG** (`app-bql`, `app-data-backbone`,
  `app-ecommerce-intelligence`, the portrait); UI screenshots stay **PNG**,
  because JPEG smears small text. The originals in `wp-rates-page/img/` are all
  PNG — converting the four photographic ones took this folder from 11 MB to
  1.4 MB with no visible difference. If you re-copy an image from that repo,
  re-apply the split.

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
