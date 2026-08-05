# Portfolio & case study landing page — design plan

**Folder:** [`portfolio/`](../portfolio/) · **Public URL:** `https://intake.wolfstrategyllc.com/portfolio/`
**Issue:** [#95](https://github.com/wolfpackdata/wp-website/issues/95) ·
**Notion project:** [Portfolio & Case Study Landing Page](https://app.notion.com/p/3b2c70e5c7b48026a50edce174ad25ee)

---

## 1. What this page is

One page that presents the case studies written so far and the applications and workflows
in the portfolio. It is the page Ry sends, or the Wix nav points at, when someone wants to
see the work rather than read a resume or a rate card.

**The audience is two audiences at once:** prospective clients evaluating Wolfpack, and
companies considering hiring Ry. That is the page's defining constraint. Every other page
in this repo serves exactly one of those groups, which is why none of them can do this job:

| Page | Audience | Robots |
|---|---|---|
| `rates/` | Clients | indexed |
| `ai-coaching/` | Clients, coaching specifically | indexed |
| `hire/` | Hiring managers | **noindex** |
| **`portfolio/`** | **Both** | **indexed** |

Serving both is what forces the content selection. Work evidence reads the same to a
client and to a hiring manager: a shipped application is a shipped application. Career
narrative does not. So the applications and case studies come across, and the resume
apparatus around them stays behind.

## 2. Content rule: draw, do not invent

**Every application card is verbatim from
[`ryan-resume-dev/resume_build/content/eng_only.yaml`](../ryan-resume-dev/resume_build/content/eng_only.yaml)** —
the same strings the `hire/` pages carry, from the same `projects` section. No card is
rewritten, retitled, or re-ordered into a new argument. This page writes almost no prose of
its own.

**What is deliberately stripped** relative to a `hire/` page: the career timeline,
professional experience bullets, the expertise matrix, current technical focus, education,
the resume downloads, and the contact grid. Those are the resume. This page is the
portfolio.

**Why verbatim rather than tone-edited.** [`docs/ryan-blog-tone.md`](ryan-blog-tone.md) §8
already carves this out: for resume-derived content, "Copy, do not paraphrase. Tone
guidance applies only to the connective page copy around them." The blurbs are dense with
em dashes, which §3 bans everywhere else. Tone-editing them here would create a third
wording of each blurb, differing from both the YAML and the `hire/` pages, guarded by
nothing. Drift is the larger risk, so the tone rules bind only the section kickers, ledes,
and the closing block.

## 3. Structure

```
nav (sticky, scroll-spy)
hero            ← PLACEHOLDER, Ry writes this (D-004)
applications    ← 8 cards, verbatim from eng_only.yaml
case studies    ← 1 live card + 1 in-preparation
close           ← one CTA: 30-minute intro call
footer
```

Section order puts applications before case studies deliberately. The applications gallery
is the denser, more immediately scannable evidence, and it is the section Ry pointed at as
the model for the whole page. The case studies are the deeper read, so they follow, and the
CTA sits under them where a reader who has gone that far is closest to booking.

## 4. Visual system

**Derived from [`hire/assets/css/hire.css`](../hire/assets/css/hire.css)**, which is itself
derived from `rates/css/rates.css` and `ai-coaching/css/coaching.css` — the pattern library.
Same navy `#000B29`, same rationed coral `#F95954`, same Roboto 700 / Montserrat pairing,
same `.apps` gallery geometry, same `.case` row geometry.

**Self-contained folder**, like `rates/` and `ai-coaching/` and unlike `hire/`: its own
`css/`, `fonts/`, `img/`, `js/`. `portfolio/` deploys as one directory to the intake repo
root, so nothing in it reaches outside itself. `hire/`'s shared-`assets/` arrangement exists
because two pages ship as one folder; this is one page.

**`reveal.js` is copied byte-identical** from `hire/assets/js/reveal.js`, per the same rule
`case_studies/README.md` states: reveal timing and scroll-spy are supposed to match every
other long-form page here, and a rewrite is how two pages quietly stop matching.

**Coral ration**, enumerated in the header comment of `css/portfolio.css` and kept true:

1. nav CTA · 2. hero CTA · 3. hero rule · 4. in-preparation chip · 5. closing CTA · 6. link hover · 7. focus ring

Where coral is a fill, text on it is navy (5.8:1), never white.

## 5. Decisions ledger

| # | Decision | Why |
|---|---|---|
| **D-001** | Slug is `portfolio/`, not `case-studies/` or `work/` | The page is wider than case studies alone: it carries the app gallery too. `portfolio/` describes the whole scope, and does not go stale as case studies are added. |
| **D-002** | Public and **indexed** | Unlike `hire/`. Being found is the point for both audiences, and this page has no differently-framed twin to collide with in search results. |
| **D-003** | **No links to the `/hire/` pages** — and **this rule is about the résumés specifically, not about `noindex`** | Those two pages carry Ry's résumé and a time-sensitive claim that he is actively seeking a role. Linking that from a public client-facing page tells every prospective client he is job-hunting, and puts both framings of one résumé a click apart. Hiring managers get the résumé from Ry directly. Ruling: Ry, 2026-08-04. **Scope corrected 2026-08-04 — see D-010. `noindex` is a symptom of this rule, never its cause**, so do not generalise it to every noindex page. |
| **D-010** | **Linking the SetMaster 3 case study is fine, and the card is a live link** | The card was briefly held back on the theory that D-003 extended to any `noindex`, direct-link-only page, and that case study was one. **That was wrong** (Ry, 2026-08-04). What settles it: the case study contains **no link to `hire/`** — the only `hire/` string in that file is an HTML comment — so linking it creates no path to the résumés, and it is a **case study, not a résumé**, so none of D-003's actual harm applies. A public blog post (#103) already linked it, so it was not new exposure either. **Correction, same day:** this entry first claimed the case study's `noindex` protected it against the planned `/setmaster3/` landing page. That was an inference and it was wrong — `sm3-specific-pages/planning/00-overview.md` D-003 records the real reason, which was that it inherited `hire/`'s direct-link posture. **Moot now:** Ry flipped the case study to **indexed** on 2026-08-04, so both linked case studies are indexed and this page links nothing `noindex` at all. |
| **D-004** | Hero copy ships as a **marked placeholder** | The hero has to speak to a client and a hiring manager in the same breath, which is a positioning judgment, not a copy task. Ry writes it. The placeholder is visually obvious and carries an HTML comment stating what it needs. Ruling: Ry, 2026-08-04. |
| **D-005** | SetMaster 3 uses the **engineering framing** | `eng_only.yaml` says `SetMaster 3`; `eng_music.yaml` says `RML SetMaster 3` with different emphasis. One source YAML for all eight cards keeps the page internally consistent and the drift check single-sourced. Ruling: Ry, 2026-08-04. |
| **D-006** | `verify_facts.py` gains **check 6**, comparing app blurbs in the HTML against the YAML | This page is the third copy of those strings. Until now nothing compared any HTML copy to the YAML, so the `hire/` pages were unguarded too. Check 6 closes both gaps at once. Ruling: Ry, 2026-08-04. |
| **D-007** | One CTA, the 30-minute intro call | The repo-wide book-first rule. No intake-form link, no resume download, no second funnel. |
| **D-008** | ~~Case studies section ships with one live card and one in-preparation card~~ → **both cards are live links** | Written when only the financial model study was published. The SetMaster 3 study **deployed 2026-08-04** (#104), so its chip became a link per D-010. The `.case__chip` device did its job: swapping it for a `.btn--ghost` changed one element and moved no layout. The device stays in the stylesheet for the next unpublished study. |
| **D-009** | Screenshots are **copied** into `portfolio/img/`, not referenced across folders | A relative path into `hire/assets/` would resolve here but break on deploy, where `portfolio/` lands at the intake repo root beside `hire/`. Self-contained is also the rule every other page folder keeps. The JPEG/PNG split from `hire/README.md` is preserved. |

## 6. Acceptance criteria

- [ ] Zero external requests. Fonts, images, CSS, JS all local to `portfolio/`.
- [ ] Zero horizontal overflow at 320 / 390 / 768 / 1024 / 1440 px.
- [ ] Page renders complete with JavaScript disabled.
- [ ] `index, follow` plus canonical and OG tags pointing at the deployed URL.
- [ ] All eight app blurbs byte-identical to `eng_only.yaml`; `verify_facts.py` check 6 passing.
- [ ] Exactly one CTA destination, the intro calendar.
- [ ] No link to either `hire/` page.
- [ ] Coral used only for the seven placements in §4.
- [ ] Connective copy passes the `ryan-blog-tone.md` §9 checklist; ported blurbs exempt per §2.
- [ ] Hero placeholder visibly marked, not mistakable for finished copy.

## 7. Entry points

The page is reached by hand-placed links, since nothing in this repo links pages
structurally. Ry's instruction was *less is more*, so the proposed set is **two links**:

1. **The Wix nav**, top level, labeled `Portfolio`, pointing at the deployed URL. The primary
   discovery path and the reason the page is indexed. **Ry's hands only** — Wix is not in git
   and no session here can change it.
2. **The ops financial model case study**, in its closing area, linking back to this page
   using the `.softcta` coda device. A reader who finishes the one published case study is the
   warmest audience this page has. **Deliberately not implemented in #95:** editing that page
   means re-deploying `case_studies/` alongside `portfolio/`, doubling the round's deploy
   surface, which is a cost Ry should choose rather than absorb.

**Recommended against, and why:** `rates/` and `ai-coaching/` are governed by the book-first
single-CTA rule, whose one existing exception (the ROI calculator link, spec R11) took a
written ruling — a portfolio link is defensible by the same reasoning but neither page is a
strong discovery path for work evidence, so it is not worth spending the exception. Both
`hire/` pages already carry the full application gallery inline, so a link there would send a
hiring manager to a page they have effectively already read. No sitemap entry: this repo has
no sitemap and the page is indexable without one.

**The reverse direction** is already built: `portfolio/` links out to `/rates_public/` in a
quiet coda band, serving the client half of the audience without becoming a second funnel CTA.
That is an outbound link on a new page rather than an amendment to an existing one, so it
needed no ruling.

## 8. Deploying

This repo serves nothing. The page goes live only by copying `portfolio/` into
`wolfpackdata/ai-coaching-intake`, which owns `intake.wolfstrategyllc.com`. The folder here
mirrors the deploy path, so it is a single copy into that repo's root with no path
rewriting. **This repo stays the source of truth; never edit the deployed copy, re-copy on
change.** After shipping, update the canonical-URL table in [`CLAUDE.md`](../CLAUDE.md) and
the Notion Web Property Map.
