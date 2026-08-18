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
and the case-study blurbs Ry wrote. The closing block was the fourth thing they bound until
that block was cut (D-013).

## 3. Structure

```
nav (sticky, scroll-spy)
hero            ← PLACEHOLDER, Ry writes this (D-004)
applications    ← 8 cards, verbatim from eng_only.yaml
case studies    ← 2 live cards, both with a real image (D-013)
footer          ← the page ends on the case studies; close block cut (D-013)
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

1. nav CTA · 2. hero CTA · 3. hero rule · 4. in-preparation chip · 5. link hover · 6. focus ring

Six since 2026-08-04, when the closing CTA went with its block (D-013). Use 4 is unused today
because both case cards are live links with real images; the chip stays for the next study.

Where coral is a fill, text on it is navy (5.8:1), never white.

## 5. Decisions ledger

| # | Decision | Why |
|---|---|---|
| **D-001** | Slug is `portfolio/`, not `case-studies/` or `work/` | The page is wider than case studies alone: it carries the app gallery too. `portfolio/` describes the whole scope, and does not go stale as case studies are added. |
| **D-002** | Public and **indexed** | Unlike `hire/`. Being found is the point for both audiences, and this page has no differently-framed twin to collide with in search results. |
| **D-003** | **No links to the `/hire/` pages** — and **this rule is about the résumés specifically, not about `noindex`** | Those two pages carry Ry's résumé and a time-sensitive claim that he is actively seeking a role. Linking that from a public client-facing page tells every prospective client he is job-hunting, and puts both framings of one résumé a click apart. Hiring managers get the résumé from Ry directly. Ruling: Ry, 2026-08-04. **Scope corrected 2026-08-04 — see D-010. `noindex` is a symptom of this rule, never its cause**, so do not generalise it to every noindex page. |
| **D-010** | **Linking the SetMaster 3 case study is fine, and the card is a live link** | The card was briefly held back on the theory that D-003 extended to any `noindex`, direct-link-only page, and that case study was one. **That was wrong** (Ry, 2026-08-04). What settles it: the case study contains **no link to `hire/`** — the only `hire/` string in that file is an HTML comment — so linking it creates no path to the résumés, and it is a **case study, not a résumé**, so none of D-003's actual harm applies. A public blog post (#103) already linked it, so it was not new exposure either. **Correction, same day:** this entry first claimed the case study's `noindex` protected it against the planned `/setmaster3/` landing page. That was an inference and it was wrong — `sm3-specific-pages/planning/00-overview.md` D-003 records the real reason, which was that it inherited `hire/`'s direct-link posture. **Moot now:** Ry flipped the case study to **indexed** on 2026-08-04, so both linked case studies are indexed and this page links nothing `noindex` at all. |
| **D-004** | ~~Hero copy ships as a marked placeholder~~ → **RESOLVED 2026-08-04, Ry wrote it** | The hero had to speak to a client and a hiring manager in the same breath, which is a positioning judgment rather than a copy task, so it shipped as a visibly-marked placeholder. Ry's copy: **"Systems, apps, and projects"** over *"Selected examples of recent applications, data systems, and AI workflows built and evolving, with some case studies below."* The `.ph-copy` block and its CSS are deleted, which is also what returned the coral ration to seven. Note his framing solved the two-audience problem by **not addressing either audience directly** — it just names the work, which reads the same to a client and to an employer. |
| **D-011** | **No rates link on this page.** The `.softcta` coda band is removed | It carried a quiet `/rates_public/` link, argued for on the grounds that half the audience is a prospective client and the honest next step after seeing work is what it costs. **Ry cut it, 2026-08-04.** The closing block is now the last thing on the page and the intro call is the only destination anywhere on it, which is the book-first rule at its strictest. The `.softcta` and `.section--coda` rules came out of the stylesheet with the section; the device still lives in `hire.css`. |
| **D-012** | The closing header and lede are **rewritten** | They read *"The smallest next step is a conversation."* over *"…whether any of the work above maps onto it."* Ry's verdict was that both were terrible, and he was right: the header took a structural instruction from [`ryan-blog-tone.md`](ryan-blog-tone.md) §7 (*close on the smallest next step*) and used it as a headline, which is consultant-speak, and *"maps onto"* was doing the same. Now **"Start with a call"** over *"Thirty minutes on what you are building and what is in the way. If nothing above fits the problem, I will say so on the call rather than talk around it."* **The CTA itself is unchanged** — that was Ry's explicit instruction, and the §4.4 immediate-caveat is kept because it is the most honest line in the block. |
| **D-013** | **The closing block is cut entirely, and the financial model card gets a real image** | Two changes Ry asked for in the same breath, hours after D-012 rewrote that block's copy. **The rewrite was not the problem; the block was.** Cutting it does not weaken the funnel: the intro call still reaches the reader twice, in the nav CTA and the hero CTA, both on the same 30-minute calendar, so *exactly one destination on the whole page* survives untouched and this remains the book-first rule at its strictest. What changes is where the reader lands at the end — on a case study and a button to read it, which is the strongest thing the page has to close on. Three tidy-ups follow mechanically: the nav's `#contact` item would have been a dead anchor and is gone, `.close`/`.close__title`/`.close__lede` left the stylesheet the way `.softcta` left with D-011, and the coral ration drops from **seven to six**. Second half of the same decision: the financial model card's `Figures in preparation` panel is replaced with the case study's new beacon hero (#113), generated at card width from the same composition rather than re-encoded from the page-sized file. Every case card now carries a real image, so use 4 of the coral ration (the IN PREPARATION chip) is live-but-unused and stays for the next study. |
| **D-005** | SetMaster 3 uses the **engineering framing** | `eng_only.yaml` says `SetMaster 3`; `eng_music.yaml` says `RML SetMaster 3` with different emphasis. One source YAML for all eight cards keeps the page internally consistent and the drift check single-sourced. Ruling: Ry, 2026-08-04. |
| **D-006** | `verify_facts.py` gains **check 6**, comparing app blurbs in the HTML against the YAML | This page is the third copy of those strings. Until now nothing compared any HTML copy to the YAML, so the `hire/` pages were unguarded too. Check 6 closes both gaps at once. Ruling: Ry, 2026-08-04. |
| **D-007** | One CTA, the 30-minute intro call | The repo-wide book-first rule. No intake-form link, no resume download, no second funnel. |
| **D-008** | ~~Case studies section ships with one live card and one in-preparation card~~ → **both cards are live links** | Written when only the financial model study was published. The SetMaster 3 study **deployed 2026-08-04** (#104), so its chip became a link per D-010. The `.case__chip` device did its job: swapping it for a `.btn--ghost` changed one element and moved no layout. The device stays in the stylesheet for the next unpublished study. |
| **D-014** | **The `.cases` grid goes to three cards**, the AI Command case study added already linked | It deployed to `/wolfpack-ai-command/` on 2026-08-15 (#190, `ai-coaching-intake#68`) and is **indexed**, so it never needed the `.case__chip` device — it went straight in as a `.btn--ghost`, which is D-008's device proving the layout absorbs an addition either way. Three consequences worth recording. **The lede had to change**: it said *"Both are published and both are a click away"*, a sentence that silently goes wrong every time a case study is added, and now says *all three*. **The card image is generated, not scaled**: that case study's `build_hero.py` grew the same output-width argument the financial model's already had, and composed `img/case-ai-command.jpg` at card width from the same source — one composition, several sizes, no generational loss (D-013's second half set this rule; this is the first time it was reused). **Nothing about the destination count moves**: a case-study link is navigation within the work, exactly like the two beside it, so D-007 stands and the coral ration stays at six. Ruling: Ry, 2026-08-15. |
| **D-016** | **The `.cases` grid goes to four: Consolidation Under Pressure is added, appended.** Ruling: Ry, 2026-08-17 (#222), reversing his own call of two days earlier. | #218 asked whether this grid should take the fourth card and **he said no** — the hire pages took it, this page kept three, and the two page types differed by one card on purpose. He reversed that specific choice the same week, so this entry records a **decision revisited, not a gap closed**; do not read the #218 state as an oversight. **Appended rather than inserted**: new cards have joined at the end since #192, and the AI-Command-first order Ry named in #218 was an instruction about *those* pages — re-sorting here would silently re-open a choice rather than implement one. **The image is the transaction map, not a hero**, because that case study ships no hero figure (Ry, 2026-08-16) and its supplied art belongs to the blog post. `build_card_image.py` gained a second output and now writes this folder's copy and `hire/`'s from one composition — byte-identical by construction, which is D-009's copy-don't-cross-reference rule and D-013's one-composition-several-sizes rule meeting on the same file. **The lede loses its count**: *"All three are published and all three are a click away"* is the sentence D-014 already identified as going stale on every addition, and it did. Nothing moves on destinations or the coral ration — a case-study link is navigation within the work (D-014), and the button is navy-ghost. |
| **D-015** | **In-tile case-study CTAs, and a SECOND destination on this page: the `/setmaster3/` product landing page.** The two application tiles whose system has a published case study (`SetMaster 3`, `Notion–GitHub AI Dev Command Center`) gain a `Read the case study` button; the SetMaster tile gains a second button to the product page. Ruling: Ry, 2026-08-17 (#218). | **This is the entry D-007 requires**, and it is deliberately not filed as a tidy-up. Site brief §6 sets this page at exactly one destination and says adding one takes *"a written ruling, recorded in the page's design plan"* — so here it is. **What is and isn't new:** the case-study buttons are not a second destination at all. D-014 already settled that a case-study link is navigation *within the work*, identical in kind to the three case cards below; these two just put the same link where the reader forms the question. The `/setmaster3/` link **is** genuinely new — a product surface with real downloads, a place a reader can go and stay. **Why it is defensible rather than a leak:** it is the only tile on the page naming a product a reader can actually get, and burying that behind "find the case study, then find its product link" serves the rule instead of the reader. The brief's own navigation principle (X-8) makes user-first the default and one-way the exception. **What holds it subordinate:** navy-ghost, never coral, and one size down (`.btn--sm`) — both halves of the §6 subordination rule, so the coral ration stays at **six** and the intro call is still the only accented ask anywhere on the page. **What does not change:** no intake-form link, no résumé download, no rates link, and still no link to either `hire/` page (D-003). The count in site-brief §6 moves from `1` to `1 + 1 subordinate`, which is the shape `rates/` has carried since R11/R14. |
| **D-009** | Screenshots are **copied** into `portfolio/img/`, not referenced across folders | A relative path into `hire/assets/` would resolve here but break on deploy, where `portfolio/` lands at the intake repo root beside `hire/`. Self-contained is also the rule every other page folder keeps. The JPEG/PNG split from `hire/README.md` is preserved. |

## 6. Acceptance criteria

- [ ] Zero external requests. Fonts, images, CSS, JS all local to `portfolio/`.
- [ ] Zero horizontal overflow at 320 / 390 / 768 / 1024 / 1440 px.
- [ ] Page renders complete with JavaScript disabled.
- [ ] `index, follow` plus canonical and OG tags pointing at the deployed URL.
- [ ] All eight app blurbs byte-identical to `eng_only.yaml`; `verify_facts.py` check 6 passing.
- [ ] Exactly one CTA destination, the intro calendar.
- [ ] No link to either `hire/` page.
- [ ] Coral used only for the six placements in §4.
- [ ] Connective copy passes the `ryan-blog-tone.md` §9 checklist; ported blurbs exempt per §2.
- [x] Hero copy written by Ry, placeholder and its CSS removed (D-004 resolved).
- [x] ~~Exactly one destination on the whole page: the intro call~~ → **one destination plus one
  subordinate**, the `/setmaster3/` product page (D-015, Ry 2026-08-17). D-011 removed the rates
  coda and D-013 the closing block without touching the count; D-015 is the first ruling that
  moves it, and it moves it by one, navy-ghost and one size down.
- [x] Every case card carries a real image; no `Figures in preparation` panel remains (D-013).

## 7. Entry points

The page is reached by hand-placed links, since nothing in this repo links pages
structurally. Ry's instruction was *less is more*, so the proposed set is **two links**:

1. **The Wix nav**, top level, labeled `Portfolio`, pointing at the deployed URL. The primary
   discovery path and the reason the page is indexed. **Ry's hands only** — Wix is not in git
   and no session here can change it.
2. **The ops financial model case study**, in its closing area, linking back to this page
   using `hire.css`'s `.softcta` coda device. A reader who finishes a published case study is the
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

**The reverse direction was built and then cut.** `portfolio/` briefly linked out to
`/rates_public/` in a quiet coda band, on the argument that it served the client half of the
audience without becoming a second funnel CTA. **Ry removed it on 2026-08-04** (D-011), so the
page now has exactly one destination anywhere on it: the intro call.

## 8. Deploying

This repo serves nothing. The page goes live only by copying `portfolio/` into
`wolfpackdata/ai-coaching-intake`, which owns `intake.wolfstrategyllc.com`. The folder here
mirrors the deploy path, so it is a single copy into that repo's root with no path
rewriting. **This repo stays the source of truth; never edit the deployed copy, re-copy on
change.** After shipping, update the canonical-URL table in [`CLAUDE.md`](../CLAUDE.md) and
the Notion Web Property Map.
