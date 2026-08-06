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
see below), and the portfolio landing page (`portfolio/`, see below); more site pieces
land here as they're built. Verify by opening the page in a browser.

Three exceptions to "no build step", all Python that builds *inputs* rather than the site
itself: `ryan-resume-dev/` compiles résumé YAML to `.docx`/`.pdf` and stages the four
downloads the `hire/` pages link; `blog_posts/tools/` converts blog markdown to the Wix
payload format (`blog_posts/`, see below); and
`case_studies/ops_fin_model_support/planning/hero/build_hero.py` composes that case study's
hero image from a source screenshot. None produces a page in this repo — the pages
themselves are still hand-written static files.

GitHub Pages is **off** for this repo (turned off 2026-07-30, #74). It used to serve
`main` at `https://wolfpackdata.github.io/wp-website/`; those URLs now 404. Nothing linked
to them — the `/ai-coaching/` and `/rates/` copies both had canonical tags pointing at the
intake originals, and `/roi-calculator/` had been linked from nowhere since 2026-07-28.

**This repo serves nothing. Merging to `main` is not deploying.** Every page here reaches
the public only as a **manual copy into `wolfpackdata/ai-coaching-intake`**, which owns
`intake.wolfstrategyllc.com` — so a change is live only once that copy is re-made and
merged there. This repo stays the source of truth for all three; never edit a deployed
copy. The canonical public URLs:

| Folder here | Canonical public URL | Since |
|---|---|---|
| `roi-calculator/` | `https://intake.wolfstrategyllc.com/roi-calculator/` | 2026-07-28 |
| `rates/` | `https://intake.wolfstrategyllc.com/rates_public/` | 2026-07-28 (#59) |
| `ai-coaching/` | `https://intake.wolfstrategyllc.com/ai-coaching/` | 2026-07-28 |
| `hire/ryan-hickey/` | `https://intake.wolfstrategyllc.com/hire/ryan-hickey/` | 2026-07-31 (#76) |
| `hire/ryan-hickey-music/` | `https://intake.wolfstrategyllc.com/hire/ryan-hickey-music/` | 2026-07-31 (#76) |
| `case_studies/ops_fin_model_support/` | `https://intake.wolfstrategyllc.com/ops-fin-model-case-study/` | 2026-08-04 (#91) |
| `sm3-specific-pages/setmaster3-case-study/` | `https://intake.wolfstrategyllc.com/setmaster3-case-study/` — **indexed** (flipped from `noindex` 2026-08-04) | 2026-08-04 (#104) |
| `sm3-specific-pages/setmaster3/` | `https://intake.wolfstrategyllc.com/setmaster3/` — **indexed**; the product page, two real downloads | 2026-08-05 (#144) |
| `portfolio/` | `https://intake.wolfstrategyllc.com/portfolio/` | 2026-08-05 (#126) |

`sm3-specific-pages/` deploys as **two folders to the intake root** — the page folder and
`sm3-assets/` — and `planning/` never deploys. **Copy the git-tracked file list, not the
folder:** `sm3-assets/img/` holds one gitignored capture that leaks a Windows user directory,
and a folder mirror would publish it. `git ls-files sm3-specific-pages/…` is the safe source.

`hire/` deploys as **one folder**, not two — both pages share its `assets/`.

Pages can be turned back on if a page ever needs to serve from here — it was
`source: main /`, `build_type: legacy`, no CNAME, HTTPS enforced.

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

## `case_studies/` — long-form case studies
Client-facing long-form case studies sharing one stylesheet and one animation script.
**Deployed 2026-08-04** (#91). Folder README:
[`case_studies/README.md`](case_studies/README.md), which carries the full convention list.
The first one is **The Model Is Your Business Beacon** (`ops_fin_model_support/`), an
argument that an operational financial model belongs ahead of go-to-market product work.

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
- **The financial model hero is generated, and its generator ships with it.**
  `ops_fin_model_support/planning/hero/build_hero.py` composes
  `case-study-assets/img/fin-model-beacon-hero.jpg` from the source capture beside it.
  Generator and input sit under `planning/`, so neither deploys; only the finished image
  does. Rebuild rather than retouch.
- **Coral is rationed to six uses**, listed in the header comment of `case-study.css`, and
  the sheet introduces **no hues** beyond the navy system and a neutral figure ground.
- Copy follows [`docs/ryan-blog-tone.md`](docs/ryan-blog-tone.md). Its §9 checklist is
  runnable: strip head, comments, and scripts from the built page, then count em dashes,
  exclamation points, question marks, and contractions. All four should be zero.

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
  page and both `hire/` pages, reporting the exact divergence point on a mismatch. Do not
  tone-edit the ported blurbs; `docs/ryan-blog-tone.md` §8 exempts résumé-derived content
  precisely so a third wording cannot appear.
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
  left for it to point at. Both case cards carry a real image, the financial model one using
  the case study's beacon hero built at card width.
- **Self-contained folder** with its own `css/`, `fonts/`, `img/`, `js/`, like `rates/` and
  `ai-coaching/` and unlike `hire/`. `reveal.js` is copied byte-identical from
  `hire/assets/js/reveal.js` apart from its header comment.
- **One CTA and exactly one destination on the entire page: the 30-minute intro call.** No
  intake-form link, no résumé download, no rates link. A quiet `/rates_public/` coda band
  briefly existed and **Ry cut it** (2026-08-04, plan D-011), so this page is the book-first
  rule at its strictest. Don't re-add a second destination without asking. The header
  wordmark's link to `wolfstrategyllc.com` (#126) is **not** a second destination — it is
  site chrome, matching every other page here; it replaced a `#top` anchor that made sense
  only while the page was unpublished. Note the rates page now links *here* (spec R14), so
  the two pages are deliberately one-way: rates → portfolio, never back.

## `blog_posts/` — blog content, authored here, pushed to Wix
The blog runs on **Wix** and stays there. This folder hosts nothing; it moves *authoring*
into the repo so posts are written in markdown, reviewed in git, and pushed to the Wix Blog
through the API instead of pasted by hand. Folder README:
[`blog_posts/README.md`](blog_posts/README.md), which carries the full convention list,
front matter schema, and push procedure.

**This is the only folder here whose output does not go to `ai-coaching-intake`.** It
targets the Wix site directly, so the deployment table above does not apply to it.

Conventions this folder must keep:
- **One subfolder per post**, named `YYYY-MM-DD-slug`, containing exactly `post.md`, the
  cover image, and any post-specific assets. The folder name is **not** the URL — that comes
  from the `slug` front matter key. Start from `_template/post.md`.
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
- Post copy follows [`docs/ryan-blog-tone.md`](docs/ryan-blog-tone.md), whose §9 checklist
  runs directly against `post.md` — no head or scripts to strip first.

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
