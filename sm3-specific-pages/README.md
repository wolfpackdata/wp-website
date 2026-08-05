# `sm3-specific-pages/` — the two SetMaster 3 pages

Two pages about **SetMaster 3**, the offline DJ set-preparation and catalog-analysis
web app whose private source is [`wolfpackdata/setmaster3`](https://github.com/wolfpackdata/setmaster3)
and whose public, downloadable mirror is
[`wolfpackdata/setmaster`](https://github.com/wolfpackdata/setmaster).

| Page | Folder | Public URL | Audience | Robots |
|---|---|---|---|---|
| **Landing page** ("hype page") | `setmaster3/` | `intake.wolfstrategyllc.com/setmaster3/` | Hiring managers first, advanced/technical DJs second | **indexed** |
| **Case study** | `setmaster3-case-study/` | `intake.wolfstrategyllc.com/setmaster3-case-study/` | Hiring managers, plus clients reaching it from the portfolio page | **indexed** since 2026-08-04 (was `noindex, nofollow`) |

**Status: planning only.** No page has been built. The eight execution steps are
tracked as issues [#82–#89](https://github.com/wolfpackdata/wp-website/issues) with
matching Wolfpack Tasks — the table in
[`planning/00-overview.md`](planning/00-overview.md) §7 maps them.

The plan set lives in [`planning/`](planning/) and is the thing to read first:

| Doc | What it settles |
|---|---|
| [`planning/00-overview.md`](planning/00-overview.md) | The pair: decisions ledger, audiences, deployment, build order |
| [`planning/01-case-study-outline.md`](planning/01-case-study-outline.md) | The case study **outline** — section-by-section beats, not prose |
| [`planning/02-landing-page-design.md`](planning/02-landing-page-design.md) | Creative direction and full design spec for the landing page |
| [`planning/03-assets-and-capture-list.md`](planning/03-assets-and-capture-list.md) | Every screenshot and video Ry has to capture, and the placeholders that ship until he does |
| [`planning/04-claims-ledger.md`](planning/04-claims-ledger.md) | Every factual claim, its source, and the nine conflicts (all resolved 2026-07-31) |
| [`planning/05-case-study-copy.md`](planning/05-case-study-copy.md) | **The case study, written.** Draft 1 of the full prose in the house voice, plus its tone-compliance check |
| `planning/transcript Setmaster 3 Case Study and Landing Page.srt` | Ry's source brief (2026-07-31) |

## Folder layout — and why it looks like this

```
sm3-specific-pages/          ← NOT a deploy path; a workspace
├── README.md                ← this file            (not deployed)
├── planning/                ← the plan set          (not deployed)
├── sm3-assets/              ← shared css, js, fonts, img, video   ┐
├── setmaster3/index.html                                          ├─ deployed
└── setmaster3-case-study/index.html                               ┘
```

Unlike `hire/`, **this folder's name is not the URL path** — the two pages sit at
two sibling top-level paths. Deploying is therefore a copy of the **three inner
folders** into the `ai-coaching-intake` repo root, not a copy of
`sm3-specific-pages/` itself.

The shared folder is `sm3-assets/`, not `assets/`, because it lands at the intake
repo **root**, which already carries a generic `css/`, `fonts/`, `img/`, and `js/`
belonging to the intake form. A root-level `assets/` would read as site-wide
shared assets and would be a standing invitation for a future page to write into
it. Namespacing it means `../sm3-assets/…` resolves identically in this repo and
in the deployed site — the paths are never rewritten.

## Conventions these pages must keep

- **`sm3-assets/` is shared by both pages**, like `hire/assets/` and unlike
  `rates/` / `ai-coaching/`, which each carry their own font copies. Pages
  reference `../sm3-assets/…`.
- **Two design systems, deliberately** — the landing page uses SetMaster 3's own
  dark NI-inspired palette, the case study uses the Wolfpack navy/coral system it
  shares with `hire/`. `00-overview.md` §4 is the rule that keeps that from
  becoming an accident.
- **No external network requests**, same as every other page here. Fonts, images,
  **and video** are self-hosted in `assets/`. This is why the video budget in
  `03-assets-and-capture-list.md` §3 exists.
- **Trademark discipline is inherited from the app** (`setmaster3`
  `planning/03-ui-design.md` §1.3) and is non-negotiable on a *public* page: every
  visible "Traktor" / "Native Instruments" / "Spotify" carries **®**, "Exportify"
  renders plain, **no Native Instruments asset ever ships**, and both pages carry
  the unaffiliated-software line. "Designed as if Native Instruments owned it" is a
  *visual brief*, never a claim of affiliation.
- **The Mac build does not exist yet.** No page may claim macOS support until an
  artifact ships and `build-notes/macos-release-verification.md` passes. See
  `04-claims-ledger.md` C-03.
- **This repo serves nothing.** These pages reach the public only by copying
  `sm3-specific-pages/` into `wolfpackdata/ai-coaching-intake`. Same policy as
  every other page here: this repo is the source of truth, never edit the deployed
  copy, re-copy on change.
