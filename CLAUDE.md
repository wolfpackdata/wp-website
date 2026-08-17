# CLAUDE.md — wp-website

## Canonical repository
**`wolfpackdata/wp-website`** — always target this `owner/repo` for issues, PRs,
and labels. Resolve it from git (`gh repo view --json nameWithOwner`), never from the
selected subfolder name.

## GitHub workflow
This repo follows the Wolfpack GitHub SOP (the `github-gitflow` and `create-github-issue`
skills + the [`wolfpackdata/wp-github-sop`](https://github.com/wolfpackdata/wp-github-sop)
repo). Nothing here overrides it — see those for branching, commits, PRs, labels,
versioning, and releases. Sessions that can't load the skills (e.g. the mobile app) read
the SOP from that repo's `docs/sop/`.

## Notion workspace
Work that touches my Notion team space follows the Wolfpack Notion SOP (the
`notion-create-project` / `-task` / `-product` / `-client` and `notion-link-task-github`
skills + the `wolfpackdata/wp-notion-team` repo's `docs/notion-sop/`). Nothing here
overrides it — the live Notion team space is authoritative for icons, templates, and schema.
Full SOP page (readable from any session, mobile included):
[Wolfpack Notion SOP](https://app.notion.com/p/39dc70e5c7b481078ab8e2f2de4603b8). If that
link doesn't resolve, warn Ry it's dead, then search the Notion teamspace for the
*Wolfpack Notion SOP* page (Wolfpack Document Hub) to recover the current URL.

## What this repo is
The **wolfstrategyllc.com website repo** — static HTML/CSS/JS, no build step. Currently
holds the ROI calculator (`roi-calculator/`), the AI Coaching landing page
(`ai-coaching/`, see below), the public rates page (`rates/`, see below), the two
résumé landing pages (`hire/`, see below), the long-form case studies (`case_studies/`,
see below), the portfolio landing page (`portfolio/`, see below), and the GitHub link page
(`github/`, see below); more site pieces land here as they're built. Verify by opening the
page in a browser.

Four exceptions to "no build step", all Python that builds *inputs* rather than the site
itself: `ryan-resume-dev/` compiles résumé YAML to `.docx`/`.pdf` and stages the four
downloads the `hire/` pages link; `blog_posts/tools/` converts blog markdown to the Wix
payload format (`blog_posts/`, see below);
`case_studies/ops_fin_model_support/planning/hero/build_hero.py` composes that case study's
hero image from a source screenshot; and `social-cards/build_cards.py` composes the three
1200×627 social card images, which are committed under the page folders that use them
(`social-cards/` itself never deploys). None produces a page in this repo — the pages
themselves are still hand-written static files.

GitHub Pages is **off** for this repo (turned off 2026-07-30, #74). It used to serve
`main` at `https://wolfpackdata.github.io/wp-website/`; those URLs now 404. Nothing linked
to them — the `/ai-coaching/` and `/rates/` copies both had canonical tags pointing at the
intake originals, and `/roi-calculator/` had been linked from nowhere since 2026-07-28.

**This repo serves nothing. Merging to `main` is not deploying.** Every page here reaches
the public only as a **manual copy into `wolfpackdata/ai-coaching-intake`**, which owns
`intake.wolfstrategyllc.com` — so a change is live only once that copy is re-made and
merged there. This repo stays the source of truth for all three; never edit a deployed
copy. Every page that deploys carries an Open Graph / social card block in its `<head>` per
[`docs/social-cards-and-linkedin-readiness-plan.md`](docs/social-cards-and-linkedin-readiness-plan.md),
guarded by `social-cards/check_meta.py`. The canonical public URLs:

| Folder here | Canonical public URL | Since |
|---|---|---|
| `roi-calculator/` | `https://intake.wolfstrategyllc.com/roi-calculator/` | 2026-07-28 |
| `rates/` | `https://intake.wolfstrategyllc.com/rates_public/` | 2026-07-28 (#59) |
| `ai-coaching/` | `https://intake.wolfstrategyllc.com/ai-coaching/` | 2026-07-28 |
| `hire/ryan-hickey/` | `https://intake.wolfstrategyllc.com/hire/ryan-hickey/` | 2026-07-31 (#76) |
| `hire/ryan-hickey-music/` | `https://intake.wolfstrategyllc.com/hire/ryan-hickey-music/` | 2026-07-31 (#76) |
| `case_studies/ops_fin_model_support/` | `https://intake.wolfstrategyllc.com/ops-fin-model-case-study/` | 2026-08-04 (#91) |
| `case_studies/consolidation_under_pressure/` | `https://intake.wolfstrategyllc.com/consolidation-under-pressure/` — ships **two pages**, the report and a `noindex` full-width `transaction-map.html`; copy both or neither | 2026-08-15 (`ai-coaching-intake#74`) |
| `case_studies/wolfpack-ai-command/` | `https://intake.wolfstrategyllc.com/wolfpack-ai-command/` | 2026-08-15 (#190) |
| `sm3-specific-pages/setmaster3-case-study/` | `https://intake.wolfstrategyllc.com/setmaster3-case-study/` — **indexed** (flipped from `noindex` 2026-08-04) | 2026-08-04 (#104) |
| `sm3-specific-pages/setmaster3/` | `https://intake.wolfstrategyllc.com/setmaster3/` — **indexed**; the product page, two real downloads | 2026-08-05 (#144) |
| `portfolio/` | `https://intake.wolfstrategyllc.com/portfolio/` | 2026-08-05 (#126) |
| `github/` | `https://intake.wolfstrategyllc.com/github/` — **`noindex`**, direct-link only; one link, to `github.com/wolfpackdata` | 2026-08-07 (#155) |

`sm3-specific-pages/` deploys as **two folders to the intake root** — the page folder and
`sm3-assets/` — and `planning/` never deploys. **Copy the git-tracked file list, not the
folder:** `sm3-assets/img/` holds one gitignored capture that leaks a Windows user directory,
and a folder mirror would publish it. `git ls-files sm3-specific-pages/…` is the safe source.

`hire/` deploys as **one folder**, not two — both pages share its `assets/`.

Pages can be turned back on if a page ever needs to serve from here — it was
`source: main /`, `build_type: legacy`, no CNAME, HTTPS enforced.

## Social readiness — verify it, never assume it

**Every published page must be ready to be pasted into LinkedIn, and a session confirms that
rather than trusting it.** The guard exists, so running it is cheap; the failure mode is a
session reading *"guarded by `check_meta.py`"* above and concluding the check has already
happened. It has not. Run it:

```
python social-cards/check_meta.py     # from the repo root; exit 0 = clean, 1 = drift
```

**Run it before any PR that touches a page `<head>`, before generating or replacing a card
image, and again before a deploy copy into the intake repo.** The full verification sequence
is `docs/social-cards-and-linkedin-readiness-plan.md` §9.

- **A new page folder ships → add its row to `PAGES` in `check_meta.py`, in the same PR.**
  A page missing from that table is a page nothing is guarding, and it will pass silently
  forever. The row is `(repo path, deployed URL path)` — and for four pages those two differ,
  which is half of what the script is for.
- **`git ls-files`, not the folder.** The guard tests *tracked*-ness deliberately, because
  the deploy copies the tracked file list; an untracked image passes a local eyeball and 404s
  on the live card.

### Three things the guard cannot see — check these by hand

1. **The deployed copy.** `check_meta.py` reads *this repo*; a card is scraped from
   `ai-coaching-intake`. A page can pass here and be stale live. **After every deploy, fetch
   the live page and compare its OG block to this repo's** — passing locally is not evidence
   the card is right.
2. **Card quality, as against card presence.** Check 5 only fires for
   `twitter:card: summary_large_image`, so the 1200×627 floor is never applied to a `summary`
   page. That is correct under **D-004** (below), but it means the guard is deliberately
   silent about five pages — don't read their PASS as "the card looks good."
3. **Whether LinkedIn has ever scraped the URL.** Nothing in this repo can know that, and it
   is the one that bites (below).

### After a deploy, prime the scrape — the Featured-link trap (2026-08-17)

**Run every newly deployed or newly card-bearing URL through the
[LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) before sharing it.** It
both forces a re-scrape and prints the real reason on failure.

This is not tidiness. Adding `/portfolio/` as a **Featured link on a personal profile** failed
with a bare **"invalid URL"** while the page was provably healthy — 200 to the `LinkedInBot`
UA, valid cert, correct DNS, self-referential canonical, complete OG block, `og:image` 200 at
1200×627. **The cause was that LinkedIn had no cached scrape for the URL**, which its
Featured-link validator reports as "invalid URL" rather than as a cache miss. Post Inspector,
then retry, and it is accepted. LinkedIn also caches a *failure* for about a week, so a URL
scraped while it was briefly wrong stays wrong past the moment it mattered.

**Two red herrings in that output, recorded so they are not re-investigated:**

- **"206 Success"** in the redirect trail is benign and expected. LinkedInBot sends
  `Range: bytes=0-16383`; GitHub Pages honors it with a 206. Every page here closes `</head>`
  inside the first ~2KB, so the OG block is always in the first chunk.
- **"No author found" / "No publication date found"**, shown in red, are **optional**. Neither
  appears on a rendered card. Adding `article:published_time` or an author tag to clear them
  means editing a deployed page for zero benefit — don't.

### The small-card pages are a ruling, not a defect

**D-004** (Ry, 2026-08-07, in the plan's ledger) keeps `rates/`, both `hire/` pages,
`github/`, and `roi-calculator/` on the 200×200 logo with `twitter:card: summary`, on the
reasoning that they "are not primarily share targets." **A session that finds these and
"upgrades" them has reversed a decision.** If featuring them on LinkedIn has changed that
premise, that is a question for Ry, not a fix. Same for **D-003** (the ops-fin case study
reuses its 2100×1181 beacon hero at ratio 1.78 rather than getting a built card) and **D-013**
(`og:site_name` is not retro-added to pages a PR does not otherwise touch).

## Design system — read the site brief before touching CSS

> **Precedence: this `CLAUDE.md` wins over the web skills wherever they conflict.** The skills
> are generic by design; this file is specific. *"Coral is rationed to six uses, enumerated in
> `portfolio.css`'s header, and the count only goes down"* beats *"the accent is rationed"*
> every time. A session that follows the generic skill over the specific file here has been
> actively degraded. The skills arrive in every session automatically once junctioned, so this
> line is what makes that safe rather than ambiguous.

The design rules for this site live **outside this repo**, in
[`wolfpackdata/wp-web-sop`](https://github.com/wolfpackdata/wp-web-sop): the
`web-design-language` skill carries the rules, `docs/rules-ledger.md` carries why each one
exists and what it cost to learn. The skill deliberately holds **no colours, fonts, measures,
or URLs** — those all live here, in **[`docs/site-brief.md`](docs/site-brief.md)**.

**Read the brief before any CSS work.** It is the authoritative record of this site's palette,
per-page accent rations, type, spacing, destination policy, audiences, and what is
deliberately not specified. The skill is written to **refuse to run without it**.

- **Keep the two in sync in the same PR.** A value changed in a stylesheet and not in the
  brief — or the reverse — makes the brief worse than useless, because it will still be
  trusted. Three of its value sets (the master palette across seven sheets, the figure ground
  across two, the calendar URL across four) are **unguarded until #169 lands**.
- The per-page coral rations, and the rule that **the count never moves silently**, are
  recorded in the brief's §2 with the date each count last moved.
- Ration counts are also enumerated in each stylesheet's own header comment — those comments
  are the contract, not documentation of one. Keep them true.

## `rates/` — public rates page
The **public, indexable, evergreen** rates page — **canonical public URL
`https://intake.wolfstrategyllc.com/rates_public/`** since 2026-07-28 (#59; deployed copy
in `wolfpackdata/ai-coaching-intake` `rates_public/`, `ai-coaching-intake#34` — this repo
stays the source of truth; never edit the deployed copy, re-copy on change, same policy as
`ai-coaching/` and `roi-calculator/`). It also served at
`https://wolfpackdata.github.io/wp-website/rates/` from 2026-07-23 until Pages was turned
off on 2026-07-30 (#74); the intake copy is now the only live one. Ry manages the Wix
side. It is the public sibling of the **direct-link Q3 page** in
`wolfpackdata/wp-rates-page` (`intake.wolfstrategyllc.com/rates_2026Q3/`, noindex), and is
**derived from it** under `docs/public-rates-consistency-contract.md` — the operating rule
is *depth may differ, facts may not*. Planning set: `docs/public-rates-design-brief.md`
(Ry's strategy), `docs/public-rates-design-spec.md` (blueprint + rulings ledger).

Conventions the page must keep:
- **Sync is prompted, not automatic:** when the Q3 page changes, Ry prompts a session here
  to port the change per the contract (mirror set vs. enumerated deltas). A change that
  fits no rule is a new ruling — ask Ry, then record it in the contract. Update the
  *"rates last reviewed"* line (hero kicker + footer) whenever a sync lands.
- **Evergreen:** no version stamp or quarter in the URL, headline, or framing.
- **Book-first, one CTA:** every CTA is the 30-minute-call calendar link (#8; current
  URL per #32 — see the booking-link note in the `ai-coaching/` section) — no
  intake-form links. **Two exceptions that aren't one**, both navy-ghost, both
  consideration-stage links rather than funnel forks, and neither displacing the calendar
  CTA as primary: the coaching section's link to the ROI calculator (spec R11, mirrors
  `wp-rates-page#39`), and the closing `#work` section's *"See recent projects"* link to
  the portfolio (spec R14 / contract D15, #127 — this is how contract D9 resolves).
  **Neither may become coral**; the ration in `rates/css/rates.css` is fully spent.
- **No external requests**; fonts/images self-hosted in the subfolder. Coral is rationed —
  the allowed uses are listed in the header comment of `rates/css/rates.css`; keep it true.
- The two "Two ways to work with Wolfpack" tiles carry Ry's images
  (`img/path-engineering.png` / `img/path-coaching.png`, #11) in fixed 16:9 `.path__shot`
  frames (`object-fit: cover`).

## `ai-coaching/` — AI Coaching for Professionals landing page
Replaces the Wix page at `wolfstrategyllc.com/general-7` (Ry repoints the Wix nav link
himself). Like the Q3 rates page, it ships by **copying the folder into
`wolfpackdata/ai-coaching-intake`** (which owns `intake.wolfstrategyllc.com`).
**Deployed 2026-07-23** at `intake.wolfstrategyllc.com/ai-coaching`
(`ai-coaching-intake#14`/PR #15) — this repo remains the **source of truth**; never edit
the deployed copy, re-copy on change. It also served at the github.io path from that same
day's `main` release until Pages was turned off on 2026-07-30 (#74); the intake copy is
now the only live one.

Conventions the page must keep:
- **Design system inherited from `wolfpackdata/wp-rates-page`** (`css/rates.css` there is
  the pattern library). Coral `#F95954` is strictly rationed; the allowed uses are listed
  in the header comment of `ai-coaching/css/coaching.css` — keep that comment true. Where
  coral is a fill, text on it is navy, never white (AA).
- **Public and indexable** (unlike the noindex rates page), and **no external requests** —
  fonts and images are self-hosted in the subfolder.
- **30-minute-call CTAs use the intro calendar — current URL
  `https://calendar.app.google/zHNd1NA9wzb4VRLw5`** (#32, 2026-07-28; supersedes
  `WUQnihH9GEEJRMARA`, #8). Google periodically regenerates share URLs for the *same*
  calendar, so older intro-call URLs (like `WUQ…`) still resolve to the same booking page
  — this page deliberately stays on `WUQ…` for now (Ry, 2026-07-28); use the current URL
  for new/edited CTAs. The `…/13EANJ63HKqMc76z6` link is genuinely different — the
  **45-minute tutoring-engagements calendar**, valid for tutoring only, never for the call
  funnel. (History: the rates page once shipped a third, wrong link —
  `wolfpackdata/wp-rates-page#21`.) The funnel is book-first: the intake link
  is sent after booking, so this page deliberately does not link the intake form.
- The reviews section holds **dashed placeholder cards** until Ry inserts real student
  reviews (instructions live in an HTML comment above that section — don't remove it
  until real reviews are in).
- Approved assets only: the `claude-memory-by-surface` infographic, Ryan's portrait, and
  the logo. The other coaching infographics (mentality shift, prompting tips) are
  **reserved for live sessions** — don't add them to public pages.

## `hire/` — the two résumé landing pages
Long-scroll landing pages carrying the full content of Ryan's two résumés, aimed at
**hiring managers** (not clients — that's `rates/` and `ai-coaching/`).
**Deployed 2026-07-31** with v1.2.0 (#76) to
`intake.wolfstrategyllc.com/hire/ryan-hickey/` and `…/hire/ryan-hickey-music/`
(`ai-coaching-intake#44`) — same policy as every other page here: this repo is the source
of truth, never edit the deployed copy, re-copy on change. Folder README:
[`hire/README.md`](hire/README.md); full design plan and decisions ledger:
[`docs/hire-pages-design-plan.md`](docs/hire-pages-design-plan.md).

Conventions the pages must keep:
- **`noindex, nofollow`, direct-link only.** Ry sends the URL. Two differently-framed
  résumés for the same person indexed side by side reads badly — that is the whole
  reason. Don't add them to a sitemap and don't link them from `rates/`,
  `ai-coaching/`, or Wix.
- **They make a time-sensitive claim.** The hero says Ry is actively seeking a role.
  **When he lands one, these pages need editing or unpublishing** — they will not
  quietly age into being harmless.
- **One shared `assets/` folder**, unlike the other page folders, which each carry their
  own font copies. `hire/` deploys as a single unit; the pages reference `../assets/…`.
- **Content comes from the résumé YAML, verbatim.** Experience bullets and project blurbs
  are guarded by `ryan-resume-dev/resume_build/verify_facts.py`; retyping them into the
  HTML creates a second, unguarded copy that will drift. Copy, don't paraphrase — and
  when a fact changes, change it in **both** places. v2.4 (#77) exists because a
  correction landed on the pages and not in the YAML, and nothing could see the gap.
- **The four downloads in `assets/dl/` are owned by `export_pdf.py`** — never rename or
  replace them by hand. Rebuild with
  `python build.py ; python verify_facts.py ; python export_pdf.py`.
- **The case studies section is the published set in Ry's order, identical on both pages**
  (2026-08-17, #218): AI Command → SetMaster 3 → Consolidation Under Pressure → financial
  model. **The order re-derives from nothing** — not alphabetical, chronological, or by
  publication date — so don't sort it, and the four cards are byte-identical across the two
  files: **change both or neither.** No placeholders remain; the `$30M` card was removed
  because its study is unwritten, and it returns as a normal card when it exists. The section
  head deliberately **states no count**. Consolidation's card image is the only one that is not
  a case study hero — that page ships none — so it is the transaction map, composed at card
  width by `consolidation_under_pressure/planning/card/build_card_image.py`. Rebuild rather
  than retouch.
- **Two application tiles carry an in-tile case-study CTA**, the only two whose system has a
  published write-up: SetMaster 3 (which also links the `/setmaster3/` product page) and the
  Notion–GitHub AI Dev Command Center → `/wolfpack-ai-command/`. **They go after
  `.app__blurb`, never between the name and the blurb** — `verify_facts.py` check 6 matches
  those two as adjacent siblings, so anything between them unguards a résumé string *without
  failing the check*. Same pair on `portfolio/`.

## `case_studies/` — long-form case studies
Client-facing long-form case studies sharing one stylesheet and one animation script.
**Deployed 2026-08-04** (#91). Folder README:
[`case_studies/README.md`](case_studies/README.md), which carries the full convention list.
The first one is **The Model Is Your Business Beacon** (`ops_fin_model_support/`), an
argument that an operational financial model belongs ahead of go-to-market product work.
The second is **Consolidation Under Pressure** (`consolidation_under_pressure/`, see below).
The third is **An AI Operating Layer for Streamlining Project Delivery**
(`wolfpack-ai-command/`, see below) — the Wolfpack AI Command system, and the first case
study here to carry a **generated emblem** as its hero rather than a screenshot.

Conventions these pages must keep:
- **The shared stylesheet is the point.** Every case study loads
  `case-study-assets/css/case-study.css`. No per-page stylesheet, no inline `<style>`. If a
  page needs something the shared sheet lacks, add it to the shared sheet so the next case
  study inherits it. `reveal.js` is copied byte-identical from `sm3-assets/`, never
  rewritten, so reveal timing and scroll-spy match every other long-form page here.
- **Folder name is not the URL path**, like `sm3-specific-pages/` and unlike `hire/`.
  Deploying copies `case-study-assets/` and the case study's own folder to the intake repo
  **root**, renaming the page folder to its URL slug. `planning/` never deploys.
- **Public and indexed**, unlike the SetMaster 3 case study. Different audience: these speak
  to founders and SMB directors, not hiring managers, so being found is the point.
- **No client named, no testimonial invented.** Anonymize by shape. Illustrative figures are
  labeled illustrative inside the figure itself, not in a footnote. A screenshot of real
  client work is anonymized **in the pixels** — the financial model hero's source workbook
  lists team members by first name, and that column is blurred in the committed source *and*
  again at build time. "Too small to read" is a bet that nobody zooms; check new captures at
  5x or 6x.
- **Every hero commits its master under `planning/`, and no image is retouched where it
  sits.** **The rule is provenance, not generation** — art reaches these pages by more than
  one route and always will, so a hero Ry supplies is as legitimate as one a script composes.
  Two first-class classes, neither an exception: **generated**, where the generator and its
  input are the master and you *rebuild rather than retouch*
  (`ops_fin_model_support/planning/hero/build_hero.py` → `fin-model-beacon-hero.jpg`; the AI
  Command shield likewise); and **supplied**, where the delivered original is the master, it
  must never be lost, and derivatives record the *derivation* command that produced them
  (Consolidation Under Pressure). Full statement in
  [`case_studies/README.md`](case_studies/README.md). Don't write a generator to retro-fit
  supplied art into the other pattern, and don't read a missing `build_hero.py` as an omission.
- **Coral is rationed to six uses**, listed in the header comment of `case-study.css`, and
  the sheet introduces **no hues in page chrome** beyond the navy system and a neutral figure
  ground. **One scoped exception, made 2026-08-15 (#199): hue may encode a category inside a
  figure** — the transaction map's four lanes carry `--map-l0`…`l3`. Three conditions, all
  required: the variable is genuinely categorical, the hue is **redundant** with something
  already in the figure so nothing is the sole carrier of a fact, and it touches neither the
  coral ration nor the navy chrome nor a magnitude scale. Declared in the sheet with a
  measured contrast ratio, never inline in a page. Full ruling: `docs/site-brief.md` §1.6.
- **Copy is judged by Ry, against no written spec.** The repo carried a voice guide until
  2026-08-06 (#150); it was removed because it was not good enough to be binding. Match the
  voice of the case studies already here rather than reaching for a rulebook.

## `consolidation_under_pressure/` — the music-gear M&A case study
A ~6,000-word public-source market-intelligence report on M&A in music gear and pro audio,
2016–2026, rebuilt into this site's identity from two finished pages in
`wolfpackdata/dj-gear-study` (`docs/strategy/`). Eleven numbered parts, eight data tables, four
rendered figures, 43 cited transactions, and an interactive transaction map that ships twice.
**Built 2026-08-11 (#172); revised three times on Ry's review, 2026-08-15 (#197, #200, #206);
deployed 2026-08-15 (`ai-coaching-intake#74`).** Full design plan and decisions ledger:
[`docs/consolidation-case-study-design-plan.md`](docs/consolidation-case-study-design-plan.md).

Conventions this case study must keep, on top of the folder's:

- **The FIGURES are frozen and guarded; the prose is not, and has not been since #197.**
  Ry's reviews rewrote sentences for evidentiary correctness and cut restatement, so passages
  that exist in the vendored `.md` and not on the page are **expected — do not "restore" them**,
  and the upstream `dj-gear-study` `.md` is now wrong in the places #197 corrected. What did
  not change is the numeric surface: every figure carries both currency parentheticals, and
  every caption, footnote, confidence label and methodology note ships.
  `planning/verify_copy.py` checks every numeric token in the vendored source `.md` against
  the page, plus the `Src` arithmetic, the source links' accessible names, the map dataset,
  and the external-request stance. **Run it before merging any edit to this page.** A figure
  may be legitimately retired — delete it from the vendored `.md` in the same commit and say
  why in the design plan; never weaken the check.
- **The `Src` gutter is load-bearing and is never merged, hidden or dropped.** 43 rows: 31
  link a primary source, 12 show a dash meaning none was verified. That distinction is the
  page's claim about its own evidence. Every link keeps `title` + `aria-label` because the
  visible label is an arrow; every dash keeps a visually-hidden sentence.
- **The map is one script and one dataset** (`case-study-assets/js/map.js`), rendered at a
  fixed width in the report and full width in `transaction-map.html`, switched by one
  `data-fill` flag. **Do not fork it.** The source it came from shipped the map twice as two
  copies and they had already drifted by one event — the standalone plotted the 2025 tariffs
  and the embedded one did not. Nothing could see it.
- **Nothing on the map is hand-placed.** Labels are packed into the lowest free track in
  their lane, measured with canvas `measureText` because `--mono` is a *system* stack whose
  metrics are unknowable from the build machine. If a label ever collides, fix the packing
  pass, never the label.
- **The map runs two encodings on one dot, and they never swap** (#199): the ring is its
  **lane** (a category, so it takes hue — `--map-l0`…`l3`, the exception above), the fill is
  its **deal value** (a magnitude, so it stays on the neutral `--fig-ramp-1`…`4`). Colouring
  the value as well would leave the figure with two categorical-looking scales and no readable
  magnitude. The macro bands and the year axis stay neutral because neither is a lane. `map.js`
  names **no colour** — it stamps `data-lane` and the stylesheet does the rest.
- **The year axis runs along the top as well as the bottom** (#199, Ry). The plot is 1600px
  wide at its narrowest and four lanes deep, so dating an event in the first lane meant
  tracking to the far edge and then all the way down.
- **42 events, not 41.** The brief and the source page both said 41; the dataset holds 42.
  See the design plan D-009 — this is flagged for Ry, not settled.
- **No invented outcome, and no results section.** There is no instrumented result behind
  this document. The stat tiles carry artifact and method facts, the same rule the financial
  model case study set. The client is anonymised by shape — *"a music-technology
  manufacturer"* — and stays that way.
- **One destination: the 30-minute intro call.** The 82 source links are citations, not
  destinations. That reading is a **new ruling Ry has not made yet** (design plan D-006).
- **`transaction-map.html` is `noindex` and carries no Open Graph block**, and is correctly
  absent from `check_meta.py`'s page table. It is reached from the report, never from a
  search result.
- **The social card's inset is the map itself**, captured by
  `planning/card/capture_map.py` and composed by `social-cards/build_cards.py`. Rebuild
  rather than retouch, and re-run the capture *before* the card whenever the figure changes.
- **The map is also this study's CARD image**, for the same reason and by a second generator
  beside the first: `planning/card/build_card_image.py` writes
  `hire/assets/img/case-consolidation.jpg` (2026-08-17, #218). The other three case cards take
  their image from their case study's hero; **this one has no hero to take**, so the signature
  figure stands in. Both generators read the one `map-capture.png`, so re-run `capture_map.py`
  first and then both consumers whenever the figure changes. The card crop is **not** the social
  card's crop — that one takes the dense 2020–2026 half, which here would slice the lane labels
  off the category axis. The reasoning for both is written in the scripts.
- **Its hero art is supplied rather than generated — one of the two normal provenances, not
  an exception.** `planning/consolidation-under-pressure-hero.png` (1337×752, RGBA, provided
  by Ry 2026-08-15) **is the master**, so it is the file that must never be lost, and anything
  derived from it records its *derivation* command. There is no `build_hero.py` beside it and
  there should not be; don't read the absence as an omission and don't write one to make this
  hero match the other two.
- **It is deliberately not on the case study page. Ry's ruling, 2026-08-16.** The page ships
  no hero figure and is not getting one — the art is **blog eye candy**, and the blog post's
  cover is its only public surface. This is a made decision, so **adding it to the page is a
  reversal to take to Ry, never a tidy-up**, and the gap between *this case study has hero
  art* and *this case study page shows hero art* is the intended state.

## `wolfpack-ai-command/` — the AI operating layer case study
The third case study: how **Wolfpack AI Command** splits the project manager's role, hands
the record-keeping half to governed AI operators, and leaves every consequential decision
human-gated. **Built 2026-08-13 (#174); hero, social card and deploy 2026-08-15 (#190).**
Full outline and decisions ledger:
[`planning/outline.md`](case_studies/wolfpack-ai-command/planning/outline.md).

Conventions this case study must keep, on top of the folder's:

- **The hero is a generated emblem, not a screenshot** — the first one here that is, and an
  instance of the folder's generated provenance rather than a rule of its own.
  `planning/hero/build_hero.py` composes the shield from the four **committed Notion icon
  SVGs** in `case-study-assets/img/`, the same files the F6 icon chips display, so the emblem
  and the chips cannot disagree. **Rebuild rather than retouch**; the build is deterministic
  and was verified byte-identical on re-run. The generator, the SVG intermediates and the
  tiled print variant all live under `planning/` and never deploy — the finished JPEG in
  `case-study-assets/img/` is the only copy, deliberately, so there is no second one to drift.
- **The hero carries no F number** (outline D-021). F1–F6 explain a passage and sit beside
  it; the hero carries the title. Do not renumber the figures to absorb it.
- **The four icon hues are figure content, and that is a made ruling** (D-015, Ry
  2026-08-13). They live in the committed SVGs and in a JPEG, never in the stylesheet, and the
  coral ration is untouched. This is the ruling a future case study cites when it needs a
  hue: put it in the figure, not in the chrome. **#199 extended it rather than breaking it** —
  a chart drawn in HTML has no image to put its hue in, so the map's lane hues are declared in
  the sheet under three written conditions (`docs/site-brief.md` §1.6). Both rulings say the
  same thing: hue is figure content. Only the storage differs.
- **The social card's inset is the tiled print, not the brief's F1.** The original card brief
  named the split diagram, which is still a placeholder — so the card was built from the art
  that exists. The reasoning is in `social-cards/build_cards.py` beside the card; the short
  version is that a 360px LinkedIn tile treats the inset as texture, and an allover monogram
  is texture in a way one centred shield in a 4:1 band is not.
- **The name is rationed to ~three uses in the body** (D-011): the hero standfirst, the Part 5
  introduction, and the closing plug. Running copy uses common nouns — *the system*, *the
  command center*, *the operating layer*. The full branded name lives in the `<title>`, the
  card, and off-page sales surfaces. **The h1 and the standfirst are Ry's verbatim copy**
  (D-019, revised by him 2026-08-15 under D-020) — not drafted copy, and not rewordable
  without him.
- **No measured outcome, and the tiles say so.** Every stat tile carries an artifact or
  method fact counted in the system's own repositories on 13 Aug 2026, and the `.docmeta`
  states *Measured outcomes: None*. There is no instrumented result behind this system; a
  tile reading "40% faster delivery" would be the single most damaging thing the page could
  carry. **Pre-deploy gate that is still live:** the "54 rules" count is the repo mirror's,
  and the planning notes record that the live rulebook page has drifted ahead of that mirror.
  Re-count before any re-deploy that touches the number.
- **It empowers project managers; it never replaces them** (D-013). Copy must not imply the
  role's elimination or a headcount saving — a working PM should read this and want it.

## `portfolio/` — portfolio & case study landing page
One page presenting the case studies written so far and the applications and workflows in
the portfolio, at `https://intake.wolfstrategyllc.com/portfolio/`. **Built 2026-08-04
(#95), deployed 2026-08-05 (#126).** Folder README: [`portfolio/README.md`](portfolio/README.md);
full design plan and decisions ledger:
[`docs/portfolio-page-design-plan.md`](docs/portfolio-page-design-plan.md).

Conventions the page must keep:
- **Its audience is clients *and* hiring companies — that is the whole design constraint.**
  Every other page here serves one or the other. It is also why the page carries the
  applications and case studies but none of the résumé apparatus (no timeline, experience
  bullets, expertise matrix, education, or downloads): work evidence reads the same to both
  audiences, career narrative does not.
- **Public and indexed, and it must never link the `hire/` pages.** Those are `noindex`,
  direct-link only, deliberately linked from nothing; a public indexed page linking them
  defeats that in one step. Hiring managers get the résumé from Ry directly.
- **Application names and blurbs are verbatim from `eng_only.yaml`** — the same strings the
  `hire/` pages carry, using the `eng_only` framing throughout (so `SetMaster 3`, never
  `eng_music`'s `RML SetMaster 3`). **`verify_facts.py` check 6 enforces this** across this
  page and both `hire/` pages, reporting the exact divergence point on a mismatch. **Do not
  tone-edit the ported blurbs** — they are résumé-derived, and rewording them here creates a
  third wording that check 6 then fails on.
- **The hero copy is Ry's** (written 2026-08-04, resolving the placeholder it shipped with):
  *Systems, apps, and projects* over *"Selected examples of recent applications, data systems,
  and AI workflows built and evolving, with some case studies below."* It addresses **neither
  audience directly** — it names the work, which reads the same to a client and an employer.
  Don't re-point it at one of them. Coral is down to **six** uses.
- **The page ends on the case studies, then a bare intro-call button.** The closing
  "Start with a call" section was cut 2026-08-04 (#115, plan D-013), the same day its copy was
  rewritten — the rewrite was fine, the block was not wanted. **Don't re-add a closing
  *section*.** But a closing *button* is now correct: on 2026-08-05 (#130) Ry moved the hero's
  "Book an intro call" button to just above the footer, deliberately bare — no heading, no
  lede, no section chrome — so the reader meets the work before the ask. **That button is not
  a D-013 violation; leave it there.** `.hero__ctas` left with it, and the coral ration is
  still six because the button moved rather than being duplicated. The intro call still
  reaches the reader twice, through the nav CTA and this button, so the one-destination rule
  below is untouched. Don't restore the `#contact` nav item; there is no `#contact` section
  left for it to point at. All three case cards carry a real image — the grid went from two to
  three on 2026-08-15 (#192), the day the AI Command case study deployed. Two of them are
  built at card width by their case study's own hero generator rather than re-encoded from
  the page-sized file; rebuild rather than scale.
- **Self-contained folder** with its own `css/`, `fonts/`, `img/`, `js/`, like `rates/` and
  `ai-coaching/` and unlike `hire/`. `reveal.js` is copied byte-identical from
  `hire/assets/js/reveal.js` apart from its header comment.
- **One accented CTA — the 30-minute intro call — and exactly one subordinate destination,
  the `/setmaster3/` product page** (2026-08-17, plan D-015, #218), navy-ghost and one size
  down in the SetMaster tile. Case-study links don't count against this; D-014 settled that
  they are navigation within the work. Still no intake-form link, no résumé download, no rates
  link: a quiet `/rates_public/` coda band briefly existed and **Ry cut it** (2026-08-04, plan
  D-011). Don't add a third destination without asking. The header
  wordmark's link to `wolfstrategyllc.com` (#126) is **not** a second destination — it is
  site chrome, matching every other page here; it replaced a `#top` anchor that made sense
  only while the page was unpublished. Note the rates page now links *here* (spec R14), so
  the two pages are deliberately one-way: rates → portfolio, never back.

## `github/` — the GitHub link page
One screen with one link on it, at `https://intake.wolfstrategyllc.com/github/`. Ry sends
this URL when a prospective partner, employer, or collaborator wants to see the code, and it
sends them to `github.com/wolfpackdata`. **Built 2026-08-06 (#155), simplified 2026-08-07
(#158), deployed 2026-08-07** (`ai-coaching-intake#56`). Folder README:
[`github/README.md`](github/README.md), which carries the full convention list.

Conventions the page must keep:
- **One centered card holding a heading and one button, and nothing else.** Ry's reference
  was `rustdesk.com`'s closing block (#158). The page has **two strings on it** — the heading
  and the button label — and that is the point rather than an unfinished state. **Do not add
  a line of prose under the heading:** *Show me the code.* above a button labeled
  `github.com/wolfpackdata` has already said it, and a sentence under it is copy explaining
  copy. **The heading is the reader's line, not Ry's** (his pick, 2026-08-07) — it is what the
  visitor came to say and the button is the answer, so rewording it to the first person
  (*Here's my code*) breaks the exchange and leaves the button answering nothing. The kicker, standfirst, "opens in a new tab" note, and watermark it shipped with on
  2026-08-06 were all removed the next day. The **header stays left-aligned** while the card
  centers — the centering is of the content block, and a centered logo reads as a brand
  landing page rather than a page with one job.
- **Exactly one outbound destination: the GitHub profile — and it is not a funnel.** Ry's
  instruction was explicit: *"this is not to funnel people to contact me, it is just a 'this
  is my GitHub' link."* So no calendar CTA, no intake-form link, no rates link, no résumé
  download, and — **uniquely in this repo — no `mailto:` in the footer.** Every other footer
  here carries the email address; this one deliberately does not, because that is precisely
  how a not-a-contact-page becomes a contact page. This is `portfolio/`'s one-destination
  rule made stricter: there the destination is the intro call, here there is no intro call at
  all. The header wordmark and footer link to `wolfstrategyllc.com` are **site chrome, not a
  second destination**, by the precedent `portfolio/` set (#126).
- **It states no repository count and links no individual repo.** The profile link is
  self-updating — correct as repos are opened, renamed, archived, or made private, and the
  page never needs an edit to keep up. A hardcoded list of repo cards is the version of this
  page that quietly goes wrong. Context, not a dependency: at build time the account is a
  **User** account with **two public repos** (`setmaster`, `wp-website`) against nineteen
  private. Nothing on the page breaks when that ratio changes.
- **`noindex, nofollow`, direct-link only**, like `hire/`. A one-link page is thin content
  under a brand whose other indexed pages are substantial, and it would compete with
  `/portfolio/` for the same queries — and `/portfolio/` should win those, because it *shows*
  the work rather than pointing at it. Don't add it to a sitemap, and don't link it from Wix,
  `portfolio/`, or `rates/`.
- **Never link the two `hire/` pages**, inherited unchanged from `portfolio/`. Weaker here
  since this page is itself `noindex`, but not void — `noindex` is not access control.
- **No JavaScript and no `js/` folder**, unlike every other long-form page here. Nothing is
  below the fold to reveal, and a page whose whole job is one link should not need a script
  to show it.
- **Self-contained folder** with its own `css/`, `fonts/`, `img/`, like `portfolio/` and
  unlike `hire/`. Folder name is already the URL slug, so it copies to the intake root
  unchanged. **`README.md` does not deploy** (same exclusion `portfolio/` carries, #129).
- **Coral is rationed to three uses** — the smallest ration in this repo — enumerated in the
  header comment of `css/github.css`. It was four until 2026-08-07, when the hero rule left
  with the standfirst it underlined (#158); as everywhere else here, the count only ever goes
  down. The GitHub mark is inlined as SVG and takes navy through `fill: currentColor`, so
  there is no second color value to keep in sync with the AA rule.
- **The button's width is the one fragile dimension.** Its label is a URL in `var(--mono)`, a
  *system* font stack, so its rendered width is not knowable from the build machine. The
  first pass fit it at 320px with two pixels to spare — a coincidence, not a fit. Breakpoints
  at 480px and 360px now step padding and type down; worst case is 375px at 16% headroom.
  **Re-measure after any change to that label, its padding, or its font — a screenshot cannot
  show you the remaining slack.**

## `blog_posts/` — blog content, authored here, pushed to Wix
The blog runs on **Wix** and stays there. This folder hosts nothing; it moves *authoring*
into the repo so posts are written in markdown, reviewed in git, and pushed to the Wix Blog
through the API instead of pasted by hand. Folder README:
[`blog_posts/README.md`](blog_posts/README.md), which carries the full convention list,
front matter schema, and push procedure.

**This is the only folder here whose output does not go to `ai-coaching-intake`.** It
targets the Wix site directly, so the deployment table above does not apply to it.

**The workflow is a skill.** `wp-blog-writing-workflow` (in `.claude/skills/`, repo-local)
runs a post from Ry's raw prompt or transcript through to a published Wix post and the site
links that should point at it — four phases across separate sessions, resumed from a committed
ledger at `blog_posts/<folder>/planning/workflow.md`. Prefer it over ad-hoc post creation, and
read it before pushing anything to Wix by hand.

Conventions this folder must keep:
- **One subfolder per post**, named `YYYY-MM-DD-slug`, containing exactly `post.md`, the
  cover image, and any post-specific assets. The folder name is **not** the URL — that comes
  from the `slug` front matter key. Start from `_template/post.md`.
- **The Wix draft ID lives in the ledger.** A push without it creates a second post instead of
  updating the first. This is not hypothetical: the SetMaster post's markdown was edited to
  link `/setmaster3/` and the v3.0.4 tag (#147) and the live post carries neither, because the
  ID was recorded nowhere and nothing tracked that a re-push was owed.
- **`planning/` is public.** This repo is public, so a source transcript or brief committed
  there is world-readable. Nothing lands in it that Ry would not publish.
- **A post that has a case study carries the case study's title, verbatim** (Ry, 2026-08-04,
  #119). One piece of work, one name. Take the case study's `h1`, not its `<title>` tag, which
  carries a subtitle and a `· Case Study` suffix meant for the tab and the SERP. Retitling
  never touches the `slug`, so the URL stays put, and a title containing a colon has to be
  quoted in the front matter.
- **Wix does not accept markdown.** The body field is `richContent` (Ricos, a node tree), so
  `blog_posts/tools/md_to_ricos.py` is the deterministic transform between them. Same
  markdown always yields the same post, which is what makes re-pushing an edit safe. Run its
  tests (`python -m unittest discover blog_posts/tools`) before merging a converter change.
- **Blank lines between paragraphs are inserted by the converter, never by hand.** Ricos does
  not carry markdown's blank line, so Wix renders consecutive paragraphs butted together;
  `space_blocks()` puts an empty `PARAGRAPH` between every pair of adjacent blocks to restore
  the gap (#109). Authoring a blank paragraph in `post.md` to force spacing arrives doubled.
- **The converter never talks to Wix.** It reads files and writes JSON; the push is a
  separate step through the already-authenticated Wix connector, so **no API key lives in
  this repo.** Images and tags are resolved to Wix IDs and passed in as maps.
- **Posts land as unpublished drafts.** Ry reviews in the Wix dashboard and publishes. The
  converter has `--publish`, deliberately not the default.
- **Three verified fidelity limits**, documented in the README and not to be re-litigated
  from the docs: Wix strips `FONT_FAMILY` so inline code has no styling; the `hashtags`
  field is not settable and tags must go through the Tags API as `tagIds`; a draft's `url`
  preview is title-derived even when `seoSlug` is set correctly.
- **The voice comes from the copywriter, not from a spec in this repo.** The guide that used
  to govern post copy was removed 2026-08-06 (#150). A brief written here carries facts,
  structure, and constraints; it does not dictate how sentences are built.

## Verifying pages at phone width
Headless Edge/Chrome clamps its window to a ~492px minimum and then crops the screenshot
to the requested width, which fakes horizontal overflow on "mobile" captures. For a true
phone-width render, embed the page in a 390px-wide `<iframe>` inside a wider host page and
screenshot that — media queries respond to the iframe's own viewport.

## Web Property Map — check it every session
The brand's public pages are spread across a Wix site and three repos. The source of truth
for that layout is the Notion page
**[wolfstrategyllc.com — Web Property Map](https://app.notion.com/p/3a5c70e5c7b48156be95db3a256a8250)**
(Wolfpack Document Hub). Read it before adding, moving, or deploying any page — in
particular, a **GitHub Pages custom domain binds to exactly one repo**, which is why
everything on `intake.wolfstrategyllc.com` must physically live in `ai-coaching-intake`.

**At the start of every session in this repo, check whether the map has gone stale and tell
Ry** — don't silently edit it, and don't wait to be asked. It's stale if, since its
"last verified" date, any of these changed: a repo's Pages setting or `CNAME`; a new
page/subfolder shipped or a URL moved; a Wix link to a GitHub-hosted page; or one of the
open rates-consolidation to-dos in its Implementation section got actioned. Cheap check:
`gh api repos/wolfpackdata/<repo>/pages` and `.../contents` across `wp-website`,
`ai-coaching-intake`, and `wp-rates-page`. Wix isn't in git — fetch the page to check it.

If the Notion link is dead, warn Ry, then search the teamspace for *Web Property Map* to
recover the URL.
