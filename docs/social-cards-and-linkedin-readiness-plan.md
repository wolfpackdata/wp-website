# Social cards & LinkedIn readiness — execution plan

**Status:** executed 2026-08-07 — see Execution notes at the end
**Written:** 2026-08-07
**Source:** [`sm3-specific-pages/planning/sm3-website-handoff.md`](../sm3-specific-pages/planning/sm3-website-handoff.md)
(work order, 2026-08-07), verified against this repo and the deployed copies on 2026-08-07
**Trigger:** SetMaster 3 is going into the Featured section of Ry's personal LinkedIn profile
and behind the custom action button on the Wolfpack Data & Strategy company page. Both point
at site pages, so the site is the funnel and its link previews are the first thing anyone sees.

---

## 1. What the work order got right, wrong, and missed

The work order is a good piece of research and its headline finding is correct. Three
corrections and one addition changed the shape of this plan, so they are recorded before the
work rather than buried in it.

### Confirmed

`sm3-specific-pages/setmaster3-case-study/index.html` carries **zero** `og:` and **zero**
`twitter:` meta tags. Verified in the repo source and in the deployed copy at
`wolfpackdata/ai-coaching-intake` `setmaster3-case-study/index.html` — the two are
byte-identical in the `<head>`, so there is no drift to reconcile first. The product page's
tags are present and correct. The page's `<title>` and `<meta name="description">` are good,
so this is a tag-only fix, exactly as the work order says.

### Already done — work order item 2.3 needs no work

Item 2.3 asks for "footer link on the SetMaster pages back to the main site and to Contact."
Both already exist, and have since before the work order was written:

| Page | Path back to `www` | Contact |
|---|---|---|
| `setmaster3-case-study/` | nav wordmark → `wolfstrategyllc.com`, **and** a footer link → `wolfstrategyllc.com` | "Contact Ryan" is the page's only solid CTA |
| `setmaster3/` | nav wordmark, **and** a bare "Visit wolfstrategyllc.com" button above the footer (added 2026-08-05, #144) | — (deliberate: this page's CTA is the download) |

Nothing to do. Item 2.3 is closed as already satisfied.

### Wrong — the analytics appendix

The appendix says "if analytics are already in place on these pages, no site work is needed —
Ry can append UTM parameters himself." **There is no analytics on any page in this repo.** Every
HTML file was grepped for `gtag`, `googletagmanager`, `plausible`, `umami`, `fathom`,
`clarity.ms`, and any external `<script src="http…">`. Zero hits. The only external-script hit
in the whole repo is the word "plausible" appearing in prose in a résumé template.

So the UTM parameters in the appendix would be recorded by nothing, on either host. Worse, the
fix is not free: every page folder here is documented as making **no external requests**, with
fonts and images self-hosted per folder. Adding a tag manager is an exception to a rule that
appears in `CLAUDE.md` and in four folder READMEs.

**Ruling (Ry, 2026-08-07): file it separately, do not block on it.** See §7.

### Missed — the same defect on another page, and two partial ones

The work order looked only at the two SetMaster pages. A sweep of all nine public HTML pages
found the identical gap elsewhere:

| Page | robots | canonical | og | twitter | og:image |
|---|---|---|---|---|---|
| `sm3-specific-pages/setmaster3/` | index | ✅ | full | `summary_large_image` | set-editor shot |
| `sm3-specific-pages/setmaster3-case-study/` | index | ✅ | **none** | **none** | **none** |
| `case_studies/ops_fin_model_support/` | index | ✅ | **none** | **none** | **none** |
| `portfolio/` | index | ✅ | full | `summary` | logo, 200×200 |
| `ai-coaching/` | — | ✅ | **partial** — no `og:url`, no `og:image` | **none** | **none** |
| `rates/` | — | ✅ | full | `summary` | logo, 200×200 |
| `hire/ryan-hickey/` | noindex | ✅ | full | `summary` | logo, 200×200 |
| `hire/ryan-hickey-music/` | noindex | ✅ | full | `summary` | logo, 200×200 |
| `github/` | noindex | ✅ | full | `summary` | logo, 200×200 |
| `roi-calculator/` | — | **none** | **none** | **none** | **none** |

`case_studies/ops_fin_model_support/` is public, indexed, and client-facing — the same class of
page as the SetMaster case study and the same defect. Fixing one and not the other would leave
the bug to be rediscovered. `ai-coaching/` currently renders a **text-only** card because it has
`og:title`/`og:description`/`og:type` but no image. `roi-calculator/` has no canonical either.

**Ruling (Ry, 2026-08-07): full sweep, SM3 first.**

### The `www` question, settled on facts

The work order flags moving the SetMaster pages to `www.wolfstrategyllc.com` as an open
decision. Two facts close it:

1. `intake.wolfstrategyllc.com` is a **GitHub Pages custom domain bound to
   `wolfpackdata/ai-coaching-intake`** (`gh api repos/wolfpackdata/ai-coaching-intake/pages`
   → `cname: intake.wolfstrategyllc.com`, `source: main /`, `status: built`). A Pages custom
   domain binds to **exactly one repo** — which is the whole reason everything on that host
   physically lives in that repo.
2. `www.wolfstrategyllc.com` is served by **Wix**, which owns routing for that host.

Therefore `www.wolfstrategyllc.com/setmaster3/` **cannot serve this repo's HTML at all**. A
"move" is not a copy — it is either rebuilding the pages inside Wix (abandoning the shared
stylesheet, `reveal.js`, the design system, and git history for pages that would then live
outside version control) or moving `www` off Wix. Neither is a pre-LinkedIn task, and the work
order is right that changing a Featured URL after posting is painful.

**Ruling (Ry, 2026-08-07): do not move.** Work order items 2.1 and 2.2 cannot be done from this
repo and are handed back as a Wix work order — see §8.

---

## 2. Decisions ledger

| # | Decision | Rationale |
|---|---|---|
| D-001 | **Full OG sweep**, not the single page the work order asked for. Sequenced so the SM3 case study can ship alone if LinkedIn timing demands it. | Ry, 2026-08-07. The identical defect exists on the other case study; fixing one leaves the other to be found again. |
| D-002 | **SM3 case study gets a purpose-built 1200×627 card**, not the product page's screenshot. | Ry, 2026-08-07. Two Featured tiles carrying the identical set-editor screenshot reads as a duplicate. |
| D-003 | **Ops-fin case study reuses its existing beacon hero** (`fin-model-beacon-hero.jpg`, 2100×1181) rather than getting its own built card. | Ry, 2026-08-07. Already a purpose-built image, already distinctive, ratio 1.78 vs LinkedIn's 1.91 → light side crop only. Zero build cost. |
| D-004 | **`portfolio/` and `ai-coaching/` upgrade to large image cards.** `rates/`, both `hire/` pages, `github/`, and `roi-calculator/` stay on the 200×200 logo with `twitter:card summary`. | Ry, 2026-08-07. Portfolio is a likely LinkedIn landing page; ai-coaching currently renders text-only. The rest are not primarily share targets. **PARTLY REVERSED 2026-08-18 by D-015 — the two `hire/` pages now carry built 1200×627 cards.** `rates/`, `github/`, and `roi-calculator/` are untouched and this decision still governs them. |
| D-005 | **No back-link from the SM3 case study to `/portfolio/`.** | Ry, 2026-08-07. `portfolio → case study` stays deliberately one-way, matching the `rates → portfolio` precedent (portfolio conventions, #127). The case study already has four outbound destinations. |
| D-006 | **Analytics parked to its own issue**, not scoped here. | Ry, 2026-08-07. It is a real architecture decision against a documented no-external-requests rule; it should not ride along on a blocking tag fix. |
| D-007 | **No move to `www`.** Items 2.1/2.2 become a Wix work order. | Ry, 2026-08-07, on the hosting facts in §1. |
| D-008 | **Work order item 2.3 closed as already satisfied** — no code change. | Verified 2026-08-07; the links it asks for are already on both pages. |
| D-009 | **The card generator is a committed script**, not hand-made images, living in a folder that does not deploy. | Matches the standing convention for `fin-model-beacon-hero.jpg`: *"The financial model hero is generated, and its generator ships with it… Rebuild rather than retouch."* One more card later should be a script invocation, not a design session. **Note, 2026-08-16 (#216):** the hero convention quoted here has since been generalized — a hero may be *generated* or *supplied*, and provenance rather than generation is the rule. **This decision is unaffected: social cards are still always generated**, because a card is composed from page material rather than delivered as art. Read the quote as history, and `case_studies/README.md` as current. |
| D-010 | **`og:description` is the page's `<meta name="description">` verbatim on the SM3 case study**, including the "Data engineering meets DJ engineering." opener — a deviation from the work order's suggested text, which drops it. | The opener is the strongest hook in the string and sits inside LinkedIn's visible truncation window. The work order's own stated principle is "lifted verbatim so the card matches the page"; this applies that principle more faithfully than its own snippet does. |
| D-011 | **`og:description` on the ops-fin case study is trimmed** to its first two sentences rather than used verbatim. | Its `<meta name="description">` is 359 characters — a paragraph written for the SERP. LinkedIn truncates around 200 and would cut mid-clause. Single deliberate exception to D-010's verbatim rule, flagged here so it is a choice rather than a drift. |
| D-012 | **`og:title` drops the `· Case Study` / tab suffix** on both case studies. | Same reasoning the blog convention already carries: the `<title>` suffix is written for the browser tab and the SERP, not for a card headline. |
| D-013 | **`og:site_name` and `og:image:alt` are added to every page this plan touches**, and not retro-added to pages it does not touch. | Cheap on a page already being edited; widening to untouched pages would be scope creep. Listed as an optional extra in §6 if Ry wants uniformity. |
| D-014 | **A generated card image does not count against a folder's coral ration.** | The rations are documented in CSS header comments and govern the stylesheet. The beacon hero already contains one coral use without being counted. Flagged rather than assumed — overturnable. |
| D-015 | **Both `hire/` pages upgrade to built 1200×627 cards, reversing D-004 for those two pages only** — and **neither card carries Ryan's portrait**. `rates/`, `github/`, and `roi-calculator/` stay exactly as D-004 left them. Ruling: Ry, 2026-08-18 (#230). | **On the reversal:** D-004's premise was that these "are not primarily share targets", which had it backwards. Every other page here is *found* — indexed, linked, arrived at. The `hire/` pages are `noindex` and direct-link only, which means the **only** way anyone reaches one is Ry pasting the URL into a LinkedIn message, an email, or an application form — so the preview is not incidental to the visit, it *is* the first impression, on the two pages where a first impression is the entire product. A 200×200 logo tile was the weakest card on the most-pasted URLs. **On the portrait:** Ry's instruction, and it turned out to be the design constraint that made the cards good — with no face to lead on, each card argues from the work. **On the two insets:** neither uses either of the portfolio card's panels, so the two never read as one duplicated post (D-002's rule, applied outward); the engineering card pairs a render with a shipped-application screenshot because that pairing *is* the page's claim; the music card runs a single full-width SetMaster panel, because two cards for two framings of one person must be separable at 360px by structure and not only by a role line. **On the subtitle:** see D-016. |
| D-016 | **`build_cards.py` grows an optional `subtitle` line**, set in `--muted` under the title and above the coral rule. Cards that do not ask for one render byte-identical. | These two are the only cards here whose subject is a **person**. A thing needs one string; a person needs two — the name, which is the identity, and the role line, which is the only thing telling two framings of one résumé apart. Folding both into one auto-fitted title sets them at the same size, which buries the name and leaves the two cards differing only in the tail of a wrapped line. Verified by rebuild: all five pre-existing cards came back byte-identical, the same discipline `framed()`'s `vfocus` argument was added under. The subtitle wraps on **phrases**, not words, so the `·` separator can never end a line and a job title is never split across two. |

---

## 3. Prerequisite — sequencing against the in-flight `github/` work

The current branch `feat/158-simplify-github-page` has **uncommitted** changes to
`github/index.html` and `github/css/github.css`. `github/` is also the one page folder that is
**built but not yet deployed** to the intake repo.

Two consequences:

1. **Do not start this work on that branch.** It lands on its own branch off `develop` after
   the github page work merges.
2. **The intake deploy can be bundled.** The github page's first deploy and this sweep's
   re-copy can be one PR in `ai-coaching-intake` instead of two. That is the cheaper path and
   the recommendation, but it couples the two — if the github page slips, this sweep should
   deploy alone rather than wait, because §5 is the blocking item.

`github/index.html` already carries a complete OG block and is **not** edited by this plan.

---

## 4. Phase 1 — the card generator and three card images

### 4.1 Where it lives

New folder at the repo root:

```
social-cards/
  build_cards.py        the generator
  README.md             what it makes, how to rebuild, why it exists
  src/                  source captures and any font the generator needs
```

`social-cards/` **never deploys** — it produces inputs, like `blog_posts/tools/` and
`ops_fin_model_support/planning/hero/`. This makes it the **fourth** exception to this repo's
"no build step" rule, so `CLAUDE.md`'s exceptions paragraph is updated in Phase 3 to say so.

Outputs are written into the page folders that deploy, and are committed:

| Output | Consumer |
|---|---|
| `sm3-specific-pages/sm3-assets/img/og-setmaster3-case-study.png` | SM3 case study |
| `portfolio/img/og-portfolio.png` | portfolio |
| `ai-coaching/img/og-ai-coaching.png` | ai-coaching |

All three at **1200×627** — LinkedIn's stated 1.91:1, and comfortably above its 1200×627
minimum for a large card.

### 4.2 Composition

Navy field from the design system (`--navy #000B29`, the same gradient `build_hero.py` uses),
the page's own title set in the brand face, the Wolfpack wordmark and logo, and a screenshot
inset in the same figure-ground frame (`--fig-bg`, `--fig-line`, 8px radius, 1px hairline) the
pages use. No new hues. Source screenshots, all already in the repo:

| Card | Inset |
|---|---|
| SM3 case study | `sm3-assets/img/a01-track-playlist-matrix.png` (1908×907) — deliberately **not** `a02-set-editor.png`, which is the product page's `og:image` |
| portfolio | to pick at build time from `portfolio/img/` — likely a composite of two app shots rather than one, so the card reads as *a body of work* rather than as one application |
| ai-coaching | approved assets only — the `claude-memory-by-surface` infographic, Ryan's portrait, the logo. The other coaching infographics are reserved for live sessions and must not appear on a public card. |

### 4.3 Known wrinkle — the fonts are woff2, and Pillow cannot read woff2

Every font in this repo ships as `.woff2` only (Montserrat and Roboto, Google-hosted files
self-hosted per folder). **Pillow's `ImageFont.truetype` does not accept woff2.** Two ways
through, decide at implementation:

- **(a) Convert at build time** — `fonttools[woff]` + `brotli`, woff2 → ttf in a temp file. No
  new committed binary, one more dependency, and the generator stays sourced from the exact
  files the pages load.
- **(b) Commit a TTF under `social-cards/src/`** — simplest, no conversion step, but it is a
  second copy of a font that could drift from the woff2 the pages actually serve.

Recommendation: **(a)**, because "the card uses the same font file the page uses" is a property
worth keeping, and a build-time conversion keeps it true automatically.

### 4.4 Deliverable check

Each card must be under 5 MB (LinkedIn's limit), exactly 1200×627, and legible at the ~360px
width LinkedIn renders a Featured tile at. The last one is the real constraint: **set the title
large and check it at 360px**, not at 1200. This is the same trap the case-study convention
already names — *"too small to read" is a bet that nobody zooms* — applied in reverse.

---

## 5. Phase 2 — the head edits (5 files)

Ordered so the blocking page is first. Each block goes immediately after the existing
`<link rel="canonical">` / `<link rel="icon">` lines.

### 5.1 `sm3-specific-pages/setmaster3-case-study/index.html` — **blocking**

```html
<meta property="og:type" content="article">
<meta property="og:site_name" content="Wolfpack Data &amp; Strategy">
<meta property="og:url" content="https://intake.wolfstrategyllc.com/setmaster3-case-study/">
<meta property="og:title" content="SetMaster 3: From a Spreadsheet on a Plane to a Robust Application">
<meta property="og:description" content="Data engineering meets DJ engineering. A professional DJ built his own set preparation tool three times in three years. The third is a specified, tested, offline web application.">
<meta property="og:image" content="https://intake.wolfstrategyllc.com/sm3-assets/img/og-setmaster3-case-study.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta property="og:image:alt" content="SetMaster 3's track and playlist matrix on a navy field, titled with the case study name.">
<meta name="twitter:card" content="summary_large_image">
```

Title is the `<title>` minus its `· Case Study` suffix (D-012); description is the page's
`<meta name="description">` verbatim (D-010). If the page copy changes, change these with it.

### 5.2 `case_studies/ops_fin_model_support/index.html`

```html
<meta property="og:type" content="article">
<meta property="og:site_name" content="Wolfpack Data &amp; Strategy">
<meta property="og:url" content="https://intake.wolfstrategyllc.com/ops-fin-model-case-study/">
<meta property="og:title" content="The Model Is Your Business Beacon: A Financial Model Is an Operating Tool">
<meta property="og:description" content="A common mistake is treating the financial model like paperwork for the accountant or a prop for the raise, then waiting until the business is already in motion to build it. Built early, it becomes a practical tool for making smarter decisions from day one.">
<meta property="og:image" content="https://intake.wolfstrategyllc.com/case-study-assets/img/fin-model-beacon-hero.jpg">
<meta property="og:image:width" content="2100">
<meta property="og:image:height" content="1181">
<meta property="og:image:alt" content="A financial model lit like a beacon on a navy field, its beams reading as the golden paths the page names.">
<meta name="twitter:card" content="summary_large_image">
```

Note the image path is `case-study-assets/…`, **not** `ops-fin-model-case-study/…` — the shared
asset folder deploys to the intake root as its own folder, beside the renamed page folder.

### 5.3 `ai-coaching/index.html`

Existing `og:title` / `og:description` / `og:type` stay. Add:

```html
<meta property="og:site_name" content="Wolfpack Data &amp; Strategy">
<meta property="og:url" content="https://intake.wolfstrategyllc.com/ai-coaching/">
<meta property="og:image" content="https://intake.wolfstrategyllc.com/ai-coaching/img/og-ai-coaching.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta property="og:image:alt" content="…">
<meta name="twitter:card" content="summary_large_image">
```

### 5.4 `portfolio/index.html`

Add `og:site_name`; **replace** the logo `og:image` and upgrade the card type:

```html
<meta property="og:image" content="https://intake.wolfstrategyllc.com/portfolio/img/og-portfolio.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta property="og:image:alt" content="…">
<meta name="twitter:card" content="summary_large_image">
```

The old `img/wolfpack-logo.png` reference goes; the file stays — it is the favicon.

### 5.5 `roi-calculator/index.html`

The only page with **no canonical at all**. Add the canonical plus a logo-card OG block
(D-004 keeps it on `summary`):

```html
<link rel="canonical" href="https://intake.wolfstrategyllc.com/roi-calculator/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Wolfpack Data &amp; Strategy">
<meta property="og:url" content="https://intake.wolfstrategyllc.com/roi-calculator/">
<meta property="og:title" content="AI Tool ROI Calculator | Wolfpack">
<meta property="og:description" content="Estimate the real dollar value of adopting an AI tool based on your pay, how much of your work it touches, and how much faster or better that work gets.">
<meta property="og:image" content="https://intake.wolfstrategyllc.com/roi-calculator/img/wolfpack-logo.png">
<meta name="twitter:card" content="summary">
```

### 5.6 Not touched

`rates/`, `hire/ryan-hickey/`, `hire/ryan-hickey-music/`, `github/` — all already complete for
their card class, and `github/` has in-flight work on another branch.

---

## 6. Phase 3 — write the convention down, so the next page inherits it

The reason this defect existed on two case studies is that nothing recorded that a page needs
an OG block. Three documentation edits, and one optional guard:

1. **`case_studies/README.md`** — add the head block to its convention list, alongside "the
   shared stylesheet is the point." A new case study should copy the block, not rediscover it.
2. **`CLAUDE.md`** — add `social-cards/` to the "three exceptions to no build step" paragraph,
   making it four; note the OG requirement in the deployment table's preamble.
3. **`sm3-specific-pages/planning/sm3-website-handoff.md`** — append a short outcome note
   pointing at this plan, so the work order does not read as still-open.

**Optional guard (recommended):** `social-cards/check_meta.py` — walks every `index.html` that
deploys and asserts the required meta set is present, `og:url` matches the canonical, and every
`og:image` is an absolute `https://intake.wolfstrategyllc.com/…` URL that resolves to a
committed file. This is the same shape as `verify_facts.py`, which exists because a correction
landed in one place and not the other and nothing could see the gap. Same failure mode here.

**Optional extra (D-013):** retro-add `og:site_name` + `og:image:alt` to `rates/`, both `hire/`
pages, and `github/` so all nine pages carry an identical block shape. Not needed for the
campaign; ask before doing it, since it widens the diff and touches the in-flight `github/`.

---

## 7. Parked — the analytics decision (its own issue, D-006)

**File a standalone `enhancement` issue and do nothing in this plan.** What it must record:

- There is **no analytics on any page** in this repo, on either host. Verified 2026-08-07.
- Consequently the work order's UTM parameters are **inert** — nothing records them, so the
  LinkedIn campaign will be measurable only by GitHub's download counter (5 as of 2026-08-06),
  which says nothing about traffic source.
- Adding any tag manager is an **explicit exception** to the no-external-requests rule
  documented in `CLAUDE.md` and four folder READMEs. If taken, it must be written into all of
  them, not just applied.
- The cross-host problem is real and separate: `intake.` and `www.` are different hosts running
  different platforms. Measuring the journey end to end needs **one property across both**,
  which means the Wix side too — not a wp-website-only decision.
- Options worth costing: a privacy-light self-hostable option vs. GA4; per-page vs. site-wide;
  or a deliberate "no analytics, by design" that closes the question for good.

**State plainly to Ry before the campaign goes up: this launch will be unmeasured.** That is an
acceptable trade, but it should be a known one.

---

## 8. Handed back — the Wix work order (items 2.1 and 2.2, D-007)

**Cannot be done from this repo.** `www.wolfstrategyllc.com` is Wix; nothing here can put
anything on it. These are Ry's to action in Wix, and they are the actual substance of work
order item 2:

1. **Homepage presence for SetMaster 3** — a proof/portfolio section or a single highlight card
   linking `https://intake.wolfstrategyllc.com/setmaster3-case-study/`. This is the work order's
   main ask and the fix for its "funnel dead-ends at the moment of highest intent" finding.
2. **Portfolio in the `www` navigation** — pointing at
   `https://intake.wolfstrategyllc.com/portfolio/`.
3. **Do not link the two `hire/` pages** from anywhere on Wix — they are `noindex`,
   direct-link only, deliberately linked from nothing.
4. **Do not link `github/`** from Wix either, for the same reason.

The reverse direction — a path from the SetMaster pages back to `www` — is **already done**
(§1), so bidirectional reachability needs only the Wix half.

---

## 9. Verification

### Local, before the PR

1. Every edited page renders unchanged (the edits are `<head>`-only; nothing visual should move).
2. Each card image is exactly 1200×627, under 5 MB, and legible at 360px width.
3. Every `og:image` URL resolves to a file that exists at the path it claims **after** the
   deploy mapping — note the folder renames: `sm3-specific-pages/setmaster3-case-study/` → intake
   `/setmaster3-case-study/`, `case_studies/case-study-assets/` → intake `/case-study-assets/`.
   A relative-path habit is the easy way to get this wrong; `og:image` must be absolute.
4. `og:url` on each page equals that page's `<link rel="canonical">`.
5. **Run the guard — it is built, so this is no longer conditional:**
   `python social-cards/check_meta.py` from the repo root (exit 0 = clean, 1 = drift). It
   covers checks 3 and 4 above mechanically, plus canonical correctness, tag uniqueness, and
   declared-vs-actual image dimensions. **A new page folder adds its row to `PAGES` in the
   same PR** — a page missing from that table is guarded by nothing.

### After the deploy

6. Re-fetch each page from `intake.wolfstrategyllc.com` and confirm the tags are in the
   **served** HTML, and that each `og:image` URL returns 200.
7. **LinkedIn Post Inspector** (`https://www.linkedin.com/post-inspector/`) on, at minimum:
   - `https://intake.wolfstrategyllc.com/setmaster3-case-study/`
   - `https://intake.wolfstrategyllc.com/setmaster3/`
   - `https://intake.wolfstrategyllc.com/portfolio/`
   - `https://intake.wolfstrategyllc.com/ops-fin-model-case-study/`

   **This step is Ry's** — the Post Inspector requires a signed-in LinkedIn session and cannot
   be driven from here. The work order is right that it is not optional: LinkedIn caches
   previews for roughly a week, so if it scrapes before the tags land, the bad card sticks and
   re-sharing will not clear it. Run it **after** the tags are live, **before** posting.

   **Widened 2026-08-17 (#220): run it on *every* deployed URL, not just these four**, and run
   it *before* the URL is used anywhere — see step 8 for why.

8. **Prime the scrape before using a URL as a profile Featured link.** Adding `/portfolio/`
   to the Featured section failed with a bare **"invalid URL"** while the page was provably
   healthy: 200 to the `LinkedInBot` UA, valid Let's Encrypt cert, correct `CNAME`,
   self-referential canonical, complete OG block, `og:image` 200 at 1200×627, and the whole
   `<head>` closing at byte 2,009. **The cause was simply that LinkedIn held no cached scrape
   for the URL** — its Featured-link validator reports a cache miss as "invalid URL". Post
   Inspector, then retry, and it is accepted immediately.

   Two things in that output that look like faults and are not:

   - **"206 Success"** in the redirect trail. LinkedInBot sends `Range: bytes=0-16383` and
     GitHub Pages honors it with a 206 Partial Content. Benign, and the OG block is inside the
     first chunk on every page here.
   - **"No author found" / "No publication date found"**, in red. Both are optional and
     neither renders on a card. Chasing them means editing a deployed page for no benefit.

---

## 10. Deploy

Standard manual copy into `wolfpackdata/ai-coaching-intake` — this repo serves nothing, and
merging to `main` here is not deploying. Folders in scope:

| From | To (intake root) |
|---|---|
| `sm3-specific-pages/setmaster3-case-study/` | `setmaster3-case-study/` |
| `sm3-specific-pages/sm3-assets/` | `sm3-assets/` |
| `case_studies/ops_fin_model_support/` | `ops-fin-model-case-study/` |
| `ai-coaching/` | `ai-coaching/` |
| `portfolio/` | `portfolio/` |
| `roi-calculator/` | `roi-calculator/` |
| *(optionally bundled)* `github/` | `github/` — first deploy, per §3 |

⚠️ **Copy the git-tracked file list, not the folder,** for `sm3-assets/`. That folder holds a
gitignored capture (`sm2 launchpad screenshot.png`) showing `C:\Users\ryanp\…` paths; a folder
mirror would publish it. Use `git ls-files sm3-specific-pages/sm3-assets/` as the source.
`README.md` files do not deploy. `planning/` never deploys.

---

## 11. Issues and branches (Wolfpack GitHub SOP)

| # | Repo | Title | Labels |
|---|---|---|---|
| 1 | `wp-website` | Add Open Graph / social card tags across the site, and generate three cards | `enhancement` |
| 2 | `wp-website` | Decide whether the site should carry analytics | `enhancement` |
| 3 | `ai-coaching-intake` | Deploy the social card sweep *(and the github page, if bundled)* | `enhancement` |

Issue 1 → one branch off `develop` → one PR → squash-merge → label `fixed-on-develop`. Issue 2
is filed and left alone — no branch. Issue 3 is the intake-side deploy.

**Not labeled `critical`.** It blocks a marketing launch, not a core workflow, and risks no
data. Flagging the call — if Ry reads a stalled LinkedIn campaign as blocking, it is his to
promote.

---

## 12. Not done, and why

- **No analytics** — parked, §7. The launch will be unmeasured.
- **No Wix changes** — impossible from here, §8. Handed back as four items.
- **No move to `www`** — a re-platform, not a copy, §1.
- **No back-link** from the SM3 case study to `/portfolio/` — D-005.
- **No purpose-built card for the ops-fin case study** — D-003, it reuses its beacon hero.
- **No card upgrade** for `rates/`, `github/`, `roi-calculator/` — D-004. The two `hire/`
  pages were carved out of this on 2026-08-18 and now carry built cards — D-015.
- **No Notion work** — explicitly out of scope for this pass.

## 13. Note on the Web Property Map

Per `CLAUDE.md`, the [Web Property Map](https://app.notion.com/p/3a5c70e5c7b48156be95db3a256a8250)
needs a staleness check each session, and it has not been read this session (Notion was out of
scope). **This plan does not itself make it stale** — it ships no new page and moves no URL. But
the pending `github/` deploy (§3) does: a new subfolder at a new public URL is exactly one of the
map's stated staleness triggers, and `github/` is still listed as "not yet deployed". Worth a
read before or with that deploy.

---

## 14. Execution notes (2026-08-07)

**Issues filed.** `wp-website` **#161** — this work, one branch off `develop`, one PR.
`wp-website` **#162** — the analytics decision, filed and left alone per §7 and D-006.
`ai-coaching-intake` **#57** — the intake-side deploy of the sweep (§10).

**Rulings taken before the work started** (Ry, 2026-08-07), all already recorded in §2 and
confirmed here as executed rather than merely proposed:

- **Full sweep**, not the single page the work order asked for (D-001).
- **SM3 case study gets a purpose-built card**; the ops-fin case study **reuses its beacon
  hero** rather than getting one built (D-002, D-003).
- **`portfolio/` and `ai-coaching/` upgrade to large image cards**; the rest stay on the logo
  and `summary` (D-004).
- **The `check_meta.py` guard is in scope**, not optional — §6's recommended guard is built
  and lands with this branch.
- **D-013's optional extra is declined.** `og:site_name` and `og:image:alt` are **not**
  retro-added to `rates/`, the two `hire/` pages, or `github/`. The pages this plan touches
  carry them; the pages it does not, do not.
- **Analytics parked to #162**, unchanged from D-006.
- **Version bump to v1.3.0 approved**, recorded in `CHANGELOG.md` as the release cut for this
  round.

**D-105 — the §3 prerequisite dissolved mid-run.** §3 was written while
`feat/158-simplify-github-page` had uncommitted changes and told this work to wait for it.
That branch's issue (**#160**) merged to `develop` before this branch was cut, so the
sequencing constraint is gone: this branch is off **`develop`@5b851f4** and there is nothing
to wait on. `github/` is still **excluded** from this deploy — its first-deploy status is
owned by a parallel `docs/155` session — so the bundling option §3 floats is not taken here,
and §10's optional `github/` row stays optional.

**D-106 — a sixth head edit, `sm3-specific-pages/setmaster3/index.html`.** The guard's first
run found the one page §5 didn't touch failing check 5: it declares
`twitter:card summary_large_image` but carried no `og:image:width`, `og:image:height`, or
`og:image:alt`. §5.6 left it alone because its block looked complete; it wasn't. Three lines
added (1904×904 + alt text) rather than weakening check 5 with an exemption — D-013's decline
covered the logo-card pages, not a page that is itself one of the two LinkedIn Featured URLs.
So the sweep edited **six** pages, not five.

**D-107 — the cards set their titles in Roboto 700, not Montserrat.** The build brief said
Montserrat "to match the site's heading face," but in this design system Roboto 700 *is* the
heading and wordmark face (`portfolio.css`, `case-study.css`); Montserrat is the body. The
generator follows the stated intent over the stated name, and the repo's Montserrat is a
variable font defaulting to Thin, which Pillow could not have used without instancing.

---

## 15. Execution note (2026-08-18) — the two `hire/` cards, #230

Ry asked for social cards on both `hire/` pages, with one constraint: **no headshot.**
Rulings D-015 and D-016 above; what actually shipped:

| Page | Card | Inset(s) |
|---|---|---|
| `hire/ryan-hickey/` | `hire/assets/img/og-ryan-hickey.png` | `app-data-backbone.jpg` + `app-pdpd.png` |
| `hire/ryan-hickey-music/` | `hire/assets/img/og-ryan-hickey-music.png` | `app-setmaster.png`, full width |

Both live in `hire/assets/img/`, which makes them the only two cards here sharing a folder —
`hire/` is the one page folder that deploys as a single unit with one shared `assets/`.

**Things a later session should not re-derive:**

- **`og:site_name` is still not on these pages.** §14's decline of D-013's optional extra
  stands; this PR touched their heads for the card and deliberately did not widen past it.
  `check_meta.py` does not check `og:site_name` for exactly this reason.
- **The engineering card's left panel contains the Shopify mark**, dead centre in the
  `$30M` backbone render. It is the only non-navy hue on either card and it is *subject*,
  not chrome — the generator's stated rule — and the same render is already on the page. At
  360px it is a green dot reading as "e-commerce at scale", which is the claim that panel is
  there to make. Flagged so it reads as considered rather than missed.
- **Rejected: pairing the two dark renders.** `app-ecommerce-intelligence.jpg` is so close
  in composition to `app-data-backbone.jpg` — inputs left, lit core centre, chart panel
  right — that side by side they read as one image printed twice. It is also the portfolio
  card's right panel.
- **These pages are `noindex`, and that is untouched.** A card is not indexing; it is what
  a scraper renders when the URL is pasted. D-002 of the hire design plan is unaffected.
- **LinkedIn has never scraped either URL.** Run both through the Post Inspector after the
  intake deploy, or the Featured-link validator will report "invalid URL" for what is
  really a cache miss — the trap `CLAUDE.md` records from 2026-08-17.
