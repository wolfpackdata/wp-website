# `sm3-specific-pages/` — the two SetMaster 3 pages

Two pages about **SetMaster 3**, the offline DJ set-preparation and catalog-analysis
web app whose private source is [`wolfpackdata/setmaster3`](https://github.com/wolfpackdata/setmaster3)
and whose public, downloadable mirror is
[`wolfpackdata/setmaster`](https://github.com/wolfpackdata/setmaster).

| Page | Folder | Public URL | Audience | Robots |
|---|---|---|---|---|
| **Landing page** ("hype page") | `setmaster3/` | `intake.wolfstrategyllc.com/setmaster3/` | Hiring managers first, advanced/technical DJs second | **indexed** |
| **Case study** | `setmaster3-case-study/` | `intake.wolfstrategyllc.com/setmaster3-case-study/` | Hiring managers, plus clients reaching it from the portfolio page | **indexed** since 2026-08-04 (was `noindex, nofollow`) |

**Case study deployed 2026-08-04** at
`https://intake.wolfstrategyllc.com/setmaster3-case-study/` (#104, re-deployed the same day
with #108 for the indexing flip).

**Landing page deployed 2026-08-05 (#144).** `/setmaster3/` returns 200 and serves
`index, follow`, so **both** SetMaster 3 pages are now live and indexed. It shipped the same
day `v3.0.4` published the first macOS artifact, and the page carries two real downloads:
the Windows zip and the signed, notarized Apple silicon `.dmg`.

One of the two things that waited on this deploy is done: the case study's "Where to Find
It" block has its **download button back**, pointing at `../setmaster3/`, verified 200
before it went in. **The public repo's `homepage` field is still empty** and is the highest
value inbound link available to the landing page — see the open item at the end of this file.

⚠️ **Three claims went stale or false the day `v3.0.4` shipped**, and all three were fixed in
#144: the test total (867 → **897**), the round count (four rounds / 74 issues → **five /
93**), and a **SHA-256 claim that was simply false** — six places said a hash ships with
every release artifact, and `v3.0.4` publishes none. See `planning/04-claims-ledger.md`
C-10 and C-11. **The lesson is procedural, not factual:** these pages have no automated
fact check, the ledger is the only control, and a release changed the facts without anyone
touching a word of copy. Re-read the ledger against the live release on every release.

**Deploying this folder: copy the git-tracked file list, never mirror the folder.**
`sm3-assets/img/` holds one gitignored capture that leaks a Windows user directory, and a
folder mirror would publish it. Use `git ls-files sm3-specific-pages/…` as the source.
`planning/` never deploys.

**Status: both pages built and both deployed.** The eight execution steps are tracked as
issues [#82–#89](https://github.com/wolfpackdata/wp-website/issues) with matching Wolfpack
Tasks — the table in [`planning/00-overview.md`](planning/00-overview.md) §7 maps them. Step
8, the ship to intake, closed for the landing page on 2026-08-05 (#144).

**Open, and worth doing:** the public repo's `homepage` field
(`github.com/wolfpackdata/setmaster`) is empty. Pointing it at
`https://intake.wolfstrategyllc.com/setmaster3/` is the single highest-value inbound link
the landing page can get, and it costs one API call. It is deliberately not done in #144:
it writes to the public repo rather than this one.

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
- **The landing page's job is the download, and the install band is where it
  happens** (Ry, 2026-08-05). Windows left, macOS right, side by side above the
  fold on a laptop, authored in HTML so both columns are complete with JavaScript
  off. The hero is deliberately short for the same reason.
- **The landing page carries exactly one solid CTA, the Download button in its
  header** (Ry, 2026-08-05). **No intro call, no rates, no portfolio, no "who made
  this" block** — do not re-add the intro call that `02-landing-page-design.md`
  §4.10 specced. Four outbound destinations, all of them ghost links or the
  download itself: the release artifacts, the public repo, one link to the case
  study low on the page, and a bare **`wolfstrategyllc.com`** button above the
  footer (Ry, 2026-08-05, same shape the portfolio page uses). The main-site button
  is site chrome and does not open the page to funnel CTAs; the intro-call
  prohibition is unchanged.
- **Both pages use the repo's Roboto 700 / Montserrat stack** and a system mono,
  not the Inter and JetBrains Mono the design spec named. The two families are
  already self-hosted in `sm3-assets/fonts/`, and adopting two more would have
  made the landing page the only page in this repo with its own typography. The
  dark palette, the label style, and the density are what carry the product look.
- **No external network requests**, same as every other page here. Fonts, images,
  **and video** are self-hosted in `assets/`. This is why the video budget in
  `03-assets-and-capture-list.md` §3 exists.
- **Trademark discipline is inherited from the app** (`setmaster3`
  `planning/03-ui-design.md` §1.3) and is non-negotiable on a *public* page: every
  visible "Traktor" / "Native Instruments" / "Spotify" carries **®**, "Exportify"
  renders plain, **no Native Instruments asset ever ships**, and both pages carry
  the unaffiliated-software line. "Designed as if Native Instruments owned it" is a
  *visual brief*, never a claim of affiliation.
- **The Mac build exists as of v3.0.4 (2026-08-05), and the claim is now bounded
  rather than forbidden.** C-03's condition was met: SetMaster 3 was built and
  acceptance-tested on a Mac, and it ships as a signed, notarized `.app` inside a
  `.dmg`. What replaced the old prohibition is a **narrower** claim both pages must
  keep true: **Apple silicon, macOS 14 (Sonoma) or later, Intel not supported**, and
  the end-to-end and golden-master suites have never been run on macOS. Do not round
  that up to "macOS support" in a later edit.
- **The download links point at the public mirror, which lags the private repo.** A
  version bump in `wolfpackdata/setmaster3` is not a published artifact. Before
  deploying, check that the release exists at `wolfpackdata/setmaster` **with both
  artifacts attached** — the landing page links a `.zip` and a `.dmg` by exact
  filename, and a mirror one release behind makes both buttons 404.
- **This repo serves nothing.** These pages reach the public only by copying
  `sm3-specific-pages/` into `wolfpackdata/ai-coaching-intake`. Same policy as
  every other page here: this repo is the source of truth, never edit the deployed
  copy, re-copy on change.
