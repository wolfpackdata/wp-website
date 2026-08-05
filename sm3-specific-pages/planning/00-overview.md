# SetMaster 3 pages — overview

The shared brief for the two pages in `sm3-specific-pages/`. Read this first,
then the per-page doc.

Source: Ry's 2026-07-31 transcript (`planning/transcript Setmaster 3 Case Study
and Landing Page.srt`), plus the `wolfpackdata/setmaster3` repo, which is the
factual ground truth for everything the pages claim about the product.

**Status: planning. Nothing built.** The transcript's instruction is explicit —
*"You're not going to write the whole case study yet. We're going to iterate on
an outline first."* That constraint governs this whole round: it produces
documents, not pages.

---

## 1. The two pages

| | Landing page | Case study |
|---|---|---|
| Nickname | "hype page" | — |
| Folder | `setmaster3/` | `setmaster3-case-study/` |
| URL | `intake.wolfstrategyllc.com/setmaster3/` | `intake.wolfstrategyllc.com/setmaster3-case-study/` |
| Primary audience | People who might hire Ry | People who might hire Ry |
| Secondary audience | Advanced / technical DJs — **not beginners** | none |
| Job | Make SetMaster 3 look like a real product, and get it downloaded | Prove how it was conceived, built, and shipped |
| Register | Product marketing. Confident, dense, visual | Engineering-document voice. Evidence over adjectives |
| Robots | **indexed** | **noindex, nofollow** |
| Design system | SetMaster 3's own dark NI-inspired palette | Wolfpack navy/coral, shared with `hire/` |
| Depth | Highlights, drawn from the case-study material | The full story |

Ry's framing, verbatim: the landing page keeps *"the history just being
interesting"* while the case study carries the depth. The two are not long and
short versions of one text — they have different jobs and different voices.

---

## 2. Decisions ledger

Settled with Ry 2026-07-31. These are inputs, not proposals.

| # | Decision | Consequence |
|---|---|---|
| D-001 | **Two sibling top-level URLs** — `/setmaster3/` and `/setmaster3-case-study/`. | The workspace folder is not a deploy path; deploy copies its three inner folders. §6. |
| D-002 | **Shared `sm3-assets/`, namespaced.** Both pages share one fonts/img/video/css folder. | Pages reference `../sm3-assets/…`, which resolves identically here and deployed. Not `assets/` — that name lands at the intake root beside the intake form's own generic `css/`, `img/`, `js/`. |
| D-003 | **Landing page is indexed; case study is `noindex, nofollow`.** | The landing page is a public product page for a public repo and should be findable. The case study speaks to the same audience as `hire/`, is linked from it, and inherits its direct-link posture. Landing page gets real SEO work (§7 of `02-landing-page-design.md`); the case study gets none. |
| D-004 | **The landing page uses SetMaster 3's own design system**, not Wolfpack navy — near-black surfaces, orange/blue signal accents, magenta/cyan Out/In identity, the RML mark. Ry's brief: *"more like if Native Instruments owned SetMaster 3 and had a landing page for it."* | The page looks like the product. Tokens are ported from `setmaster3/planning/03-ui-design.md` §3, not invented. §4 below governs the seam with the case study. |
| D-005 | **OS-detected download with an honest macOS state.** One primary button resolves to the visitor's platform asset; macOS shows a truthful "not yet built" state; a repo button sits beside it. Degrades to a platform chooser with JS off. | Satisfies the transcript's *"two buttons, one to the public repo in a new tab and another one just to download in one click"* while staying truthful — see C-03. Full component spec: `02-landing-page-design.md` §6. |
| D-006 | **"As if Native Instruments owned it" is a visual brief and nothing more.** | No NI/Traktor logo, icon, screenshot, or lifted asset ever ships. ® on every visible Traktor / Native Instruments / Spotify; "Exportify" plain. Both pages carry the unaffiliated line. Inherited from `setmaster3/planning/03-ui-design.md` §1.3 and **hardened here**, because that rule was written for a local app and these pages are public marketing, where an implied endorsement is a materially bigger problem. |
| D-007 | **Video and imagery ship as designed placeholders**, sized as though the content were there, and Ry fills them. | Ry's brief asked for placeholders for videos "of me showing the app" and for screenshots. The placeholder contract — so an unfilled page never looks broken — is `03-assets-and-capture-list.md` §4. |
| D-008 | **The case study fills the `#case-setmaster` placeholder already standing on both `hire/` pages.** | `hire/` ships three numbered case-study frames with `IN PREPARATION` chips; frame 03 is *"SetMaster 3 — from problem, to prototype, to a shipped web app."* Shipping this page turns that chip into a link. That edit is in scope for this work — see §6. |

---

## 3. What the pages are actually about

Ry's thesis, in his own words, is one sentence and everything else serves it:

> This tool **takes out the tedious catalog filtering part so you can connect your
> brain's idea with the tracks you have that fit that idea faster** — leaving more
> time for DJing and more time for music discovery.

Four supporting claims, all from the transcript:

1. **It gives hours back.** Hours out of catalog filtering and Spotify®-vs-Traktor®
   comparison; hours back into DJing and discovery.
2. **Set prep becomes fun and interactive.** You stop fighting Traktor® or
   Rekordbox® filtering. SetMaster becomes *your own source of truth* — your emoji
   palette, your workflow, the mix timer.
3. **It teaches.** For intermediate DJs — past beginner, already understand
   transitions and song composition — a set page is a legible artifact for
   learning how to cue, and how to line up key, BPM, and cue points.
4. **It is a work in progress and says so.** Rekordbox® collection import is
   planned with no timeline. Part of Ry's Anthropic portfolio (see C-05 on how to
   phrase that).

The one competitor named is **Lexicon**, and Ry named it *generously*: its
comparison tool is *"really powerful,"* it didn't do the bulk list filtering he
wanted, and SetMaster *"isn't supposed to compete with it."* That posture is a
content rule, not a nicety — see `01-case-study-outline.md` §9 and C-04.

---

## 4. Two design systems in one deploy unit

This is the sharpest structural decision in the set, and left implicit it will
rot, so it is stated once as a rule.

**The landing page is a product page. The case study is a portfolio document.**
They share a folder and a deploy unit; they do not share a look.

| | Landing page | Case study |
|---|---|---|
| Surfaces | `--bg-app #0A0A0A`, `--bg-panel #141414` | `--navy #000B29`, `--surface #0A1435` |
| Accents | `--accent-orange #FF6A00`, `--accent-blue #3D7BFD`, `--brand-magenta #FF4FD8`, `--brand-cyan #4DE8E8` | `--coral #F95954`, rationed |
| Type | SM3's web stack (§3.2 of the app UI spec) | Roboto 700 / Montserrat 400–600 |
| Mark | RML | Wolfpack |
| Stylesheet | `sm3-assets/css/sm3-landing.css` | `sm3-assets/css/sm3-case.css` |

**What is shared:** fonts, screenshots, video, the reveal script, and the
trademark/disclaimer footer block. Nothing else. **Two stylesheets, never one**
— a single stylesheet holding both palettes is how the ration gets spent by
accident, which is the failure mode `rates/css/rates.css` and
`hire/assets/css/hire.css` each solved with an enumerated-allowance comment. Both
files here get the same treatment.

**The seam, handled deliberately.** A visitor clicking from the dark product page
into a navy portfolio document experiences a hard cut. That is correct — they
have moved from *the product* to *a document about the product*, and the case
study is chrome-consistent with the `hire/` pages that link to it. The bridge is
**not** a gradient of one system into the other; it is a single explicit device:
the case study's screenshot frames render on the product's near-black surface
with its magenta/cyan column-group identity intact, so SetMaster 3 looks like
itself wherever it is pictured. Everything around those frames stays Wolfpack.

**Open for Ry** — this is the one D-decision made on my recommendation rather
than his instruction: he chose the landing page's palette, and the case study's
followed from where it is linked. If he would rather the case study also run
dark, it is a stylesheet swap and nothing else changes. Flagged in §9.

---

## 5. How the two pages reference each other

A small graph, stated so no page invents a link that doesn't exist:

```
hire/ryan-hickey/#case-setmaster ──┐
hire/ryan-hickey-music/#case-setmaster ──┤
                                   └──▶ /setmaster3-case-study/  ◀──┐
                                                    │               │
                                                    ▼               │
                                          "Try it" ──▶ /setmaster3/ ┘
                                                          │  "The full story" ─┘
                                                          ▼
                                          github.com/wolfpackdata/setmaster
                                          calendar.app.google/zHNd1NA9wzb4VRLw5
                                          wolfstrategyllc.com
```

Rules:

- **The landing page links out to three destinations**, all from the transcript:
  the public repo (new tab), the one-click download, an intro call, and the main
  website. It links *in* to the case study once, low on the page, as *the full
  story* — never as a primary CTA.
- **The case study links to the landing page** rather than to the repo directly,
  so the download flow has exactly one front door.
- **`hire/`'s frame 03 becomes a real link.** Both pages, same edit. Its
  `IN PREPARATION` chip is removed when it does.
- **Nothing links to these pages from `rates/` or `ai-coaching/`.** Different
  funnel, different audience.
- **The intro-call CTA is `https://calendar.app.google/zHNd1NA9wzb4VRLw5`** — the
  current 30-minute intro calendar per the repo `CLAUDE.md`. The
  `…/13EANJ63HKqMc76z6` link is the 45-minute *tutoring* calendar and must never
  appear on either page.

---

## 6. Deployment

**This repo serves nothing** — GitHub Pages is off (#74, 2026-07-30). These pages
reach the public only by copying into `wolfpackdata/ai-coaching-intake`, which
owns `intake.wolfstrategyllc.com`. This repo stays the source of truth; never
edit the deployed copy; re-copy on change.

Because the workspace folder is not a deploy path (D-001), shipping copies its
**three inner folders** to the intake repo root:

```
sm3-specific-pages/setmaster3/            →  <intake root>/setmaster3/
sm3-specific-pages/setmaster3-case-study/ →  <intake root>/setmaster3-case-study/
sm3-specific-pages/sm3-assets/            →  <intake root>/sm3-assets/
```

`planning/` and `README.md` stay behind. No path rewriting is needed in either
direction, which is the whole point of D-002.

Follow-ups this creates, none optional:

- **Two new rows in this repo's `CLAUDE.md` canonical-URL table.**
- **`CHANGELOG.md` entry** and a version bump — a fifth site piece is a minor
  bump by the SOP's highest-impact rule, but **the bump waits on Ry's explicit
  confirmation.**
- **The Web Property Map goes stale the moment this deploys** — two new URLs on
  `intake.wolfstrategyllc.com`. Update it in the same round.
- **`hire/`'s two case-study frames** get the real link (D-008).
- **The public repo's `homepage` field is empty** — setting it to the landing page
  URL is a one-line `gh` call and is the highest-leverage inbound link the page
  will get.

---

## 7. Build order and tracking

Docs first, then pages. The transcript is explicit that the outline gets iterated
before any prose is written.

**Phase 1 — planning: complete.** This overview, the case-study outline, the
landing-page design spec, the asset capture list, and the claims ledger all exist.
Ry iterates from here.

Every remaining step is tracked as a GitHub issue in `wolfpackdata/wp-website` and
a matching Wolfpack Task, both created 2026-07-31. The tasks are numbered because
the order matters (Notion SOP rule 5); all sit at **Not started**.

| # | Work | Issue | Notion task | Blocked by |
|---|---|---|---|---|
| 1 | Resolve the claim-ledger conflicts; approve the outline | [#82](https://github.com/wolfpackdata/wp-website/issues/82) | [task](https://app.notion.com/p/3aec70e5c7b48145846cecac6bc227a3) | — |
| 2 | Capture the screenshots and hero video | [#83](https://github.com/wolfpackdata/wp-website/issues/83) | [task](https://app.notion.com/p/3aec70e5c7b481f788a7dd0c489122dc) | — |
| 3 | Build the shared `sm3-assets/` foundation | [#84](https://github.com/wolfpackdata/wp-website/issues/84) | [task](https://app.notion.com/p/3aec70e5c7b481e290d3df61c69364a6) | — |
| 4 | Build the landing page | [#85](https://github.com/wolfpackdata/wp-website/issues/85) | [task](https://app.notion.com/p/3aec70e5c7b481ec8166cb74b2adffaa) | 3 |
| 5 | Build the OS-detecting download component | [#86](https://github.com/wolfpackdata/wp-website/issues/86) | [task](https://app.notion.com/p/3aec70e5c7b481be95f9eeb359aa57a5) | 3, lands in 4 |
| 6 | Write the case-study prose | [#87](https://github.com/wolfpackdata/wp-website/issues/87) | [task](https://app.notion.com/p/3aec70e5c7b4818eb9dbe505c98e2c94) | 1 |
| 7 | Build the case-study page | [#88](https://github.com/wolfpackdata/wp-website/issues/88) | [task](https://app.notion.com/p/3aec70e5c7b48193b31ad18c44501cec) | 3, 6 |
| 8 | Ship to intake and record it | [#89](https://github.com/wolfpackdata/wp-website/issues/89) | [task](https://app.notion.com/p/3aec70e5c7b481b8bbb1c0784239a41e) | 4, 7 |

**Three of the eight are unblocked and can start in parallel** — 1 (Ry's
decisions), 2 (Ry's captures), and 3 (the asset foundation).

**The critical path runs 1 → 6 → 7 → 8**, and its first link is Ry's. The landing
page (4, 5) is *not* on it: the page is buildable with placeholders, so media
lands as it arrives rather than gating the build.

Per the GitHub SOP, each issue gets its own `prefix/<issue>-<slug>` branch off
`develop`, one PR each, squash-merged, and stays open until Ry verifies it.

**Ship gate (issue 8):** verify both pages at desktop, tablet, and **true 390px
phone width via the iframe method** in the repo `CLAUDE.md` — headless Chrome
fakes overflow below ~492px — then the accessibility and trademark pass, then
the copy and the four records in §6.

---

## 8. Acceptance criteria — both pages

Same shape as the `hire/` round, because the same failure modes apply.

- [ ] Every factual claim on either page traces to a row in `04-claims-ledger.md`,
      and no row is marked ⚠️ unresolved.
- [ ] **Zero external network requests** — verified by grep over HTML/CSS/JS. The
      only absolute URLs are the GitHub repo, the release asset, the calendar, and
      `wolfstrategyllc.com`. No `@import`, no `url(https:…)`, no third-party video
      embed.
- [ ] Every visible "Traktor" / "Native Instruments" / "Spotify" carries **®**;
      "Exportify" carries none; **zero** NI-derived assets; both pages carry the
      unaffiliated-software line.
- [ ] No page claims macOS support (C-03).
- [ ] Landing page: indexed, canonical, OG/Twitter cards, `SoftwareApplication`
      structured data. Case study: `noindex, nofollow` + self-referential canonical.
- [ ] Both render complete and readable with **JavaScript disabled** — including
      the download block, which falls back to a platform chooser.
- [ ] `prefers-reduced-motion: reduce` bypasses all motion; every video is
      `muted playsinline` and **never autoplays with sound**.
- [ ] No horizontal scroll — `scrollWidth − clientWidth = 0` at 320 / 390 / 768 /
      1024 / 1440 px on both pages.
- [ ] Accent ration honoured: each stylesheet's header comment enumerates its
      allowed accent uses and is true.
- [ ] Total page weight budget met: landing ≤ 6 MB with video, case study ≤ 2.5 MB.

---

## 9. Open items for Ry

**All nine claim conflicts are closed** (Ry, 2026-07-31 — `04-claims-ledger.md`
§2). The one with teeth was **C-07**: the first SetMaster is **2023**, not eight
years ago, which retired an unsourced figure and reshaped the case study's central
argument from *"three times over eight years"* to *"three times in three years."*
The three-year version is the better story — it reads as pace rather than tenure.

Remaining:

1. **The case study's design system** (§4) — Wolfpack navy as specced, or dark
   like the landing page? Recommendation: navy. It is linked from `hire/` and
   reads as a portfolio document, not a product surface.
2. **The SM2 year** (C-08) — "~2024" is derived from *"used it for like a year"*,
   not stated. Confirm it, or the origin-story panel drops its year row. The only
   soft fact left in the set.
3. **Video scope** (`03-…` §3) — how many videos, how long, and whether he wants
   voiceover. The critical-path blocker for the landing page, and the only thing
   on it Claude cannot produce.
4. **Whether the landing page names Ry at all**, or presents SetMaster 3 as a
   product with a quiet "built by" line. His brief points both ways: the audience
   is *"people who want to hire me"*, but the aesthetic is *"if Native Instruments
   owned it."* Recommendation: product-first page, one authored moment low on it,
   linking the case study and `hire/`.
5. ~~**Which version of SetMaster the flight-to-LA anecdote used**~~ —
   **CLOSED (Ry, 2026-07-31): SetMaster 2.** It anchors the case study's S8, where
   it now argues *for* the deferred Perform Mode. On the landing page it stays,
   naming no version, because the story does not depend on one (`02-…` §4.4).
6. **Titles and headlines.** The **case study title is closed** (`01-…` §10):
   *"SetMaster 3: From a Spreadsheet on a Plane to a Robust Application."* The
   **landing headline is still open** (`02-…` §10).
7. **Which favicon the landing page carries.** Ry's instruction of 2026-07-31 was
   the Wolfpack mark on every page in this repo, and it is now on all six built
   pages. The landing page is not built yet, and `03-…` §6 specifies the
   **application's own** favicon for it, so that the browser tab matches the running
   app. Both readings are defensible and they cannot both apply. Ry decides before
   the landing page ships.
