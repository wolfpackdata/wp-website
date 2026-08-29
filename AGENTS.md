# AGENTS.md — wp-website

Codex reads this file automatically at the repo root. It is the **repo-level** contract. The
**global** contract — the one that binds Codex in *every* Wolfpack repo — lives at
`~/.codex/AGENTS.md` and is maintained in
[`wolfpackdata/wp-codex-sop`](https://github.com/wolfpackdata/wp-codex-sop). Where the two
disagree, **this file wins** (it is nearer the work).

Keep this file thin. It carries **pointers, not copies**: Codex truncates instruction files
past `project_doc_max_bytes` with no warning, and a stale copy of an SOP silently overrides
the good one.

## Canonical repository
**`wolfpackdata/wp-website`** — always target this `owner/repo` for issues, PRs, and labels.
Resolve it from git (`gh repo view --json nameWithOwner`), never from the selected subfolder
name.

## GitHub workflow
This repo follows the Wolfpack GitHub SOP —
[`wolfpackdata/wp-github-sop`](https://github.com/wolfpackdata/wp-github-sop), authoritative
text in that repo's `docs/sop/`. **Read it before the first git or GitHub action of a
session**; nothing here overrides it. Risk-tiered changes — auth, data migration, security,
release tooling, CI/rulesets, or the SOP and skills other agents obey — and **every** release
PR take the **AI-review stage** before merge, with Codex as the AI Reviewer: see
`docs/sop/10-ai-review.md` and `docs/sop/runbooks/ai-review.md` in that repo, and
`docs/sop/09-roles-and-permissions.md` for what the AI Reviewer may and may not do (it
reviews; its approval never satisfies the `main` gate).

## Notion workspace
Work that touches the Notion team space follows the Wolfpack Notion SOP —
[Wolfpack Notion SOP](https://app.notion.com/p/39dc70e5c7b481078ab8e2f2de4603b8) (mirror:
`wolfpackdata/wp-notion-team` → `docs/notion-sop/`). **Read it before the first Notion write
of a session**, and before that write confirm via `self` that the identity is **Main**
(`main@wolfstrategyllc.com`, `39cd872b-594c-817a-8412-00023f0d7dc8`) — any other identity is
a hard stop. Codex and Claude both act as Main, so **Codex suffixes every Notion comment it
writes with ` [codex]`**; Claude's are unmarked. If the SOP link doesn't resolve, warn the
Requester it's dead, then search the Notion teamspace for the *Wolfpack Notion SOP* page
(Wolfpack Document Hub) to recover the current URL.

## What this repo is
The **wolfstrategyllc.com website repo** — static HTML/CSS/JS, no build step. Currently
holds the ROI calculator (`roi-calculator/`), the AI Coaching landing page
(`ai-coaching/`, see below), the public rates page (`rates/`, see below), the two
résumé landing pages (`hire/`, see below), the long-form case studies (`case_studies/`,
see below), the portfolio landing page (`portfolio/`, see below), the GitHub link page
(`github/`, see below), and the pilot-project offer page (`pilot-project/`, see
below); more site pieces land here as they're built. Verify by opening the
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
| `hire/recruiter-brief/` | `https://intake.wolfstrategyllc.com/hire/recruiter-brief/` — **`noindex`**; the engineering recruiter brief | 2026-08-24 (#250) |
| `hire/recruiter-brief-music/` | `https://intake.wolfstrategyllc.com/hire/recruiter-brief-music/` — **`noindex`**; the music / audio / creator-tools recruiter brief | 2026-08-24 (#250) |
| `case_studies/ops_fin_model_support/` | `https://intake.wolfstrategyllc.com/ops-fin-model-case-study/` | 2026-08-04 (#91) |
| `case_studies/consolidation_under_pressure/` | `https://intake.wolfstrategyllc.com/consolidation-under-pressure/` — ships **two pages**, the report and a `noindex` full-width `transaction-map.html`; copy both or neither | 2026-08-15 (`ai-coaching-intake#74`) |
| `case_studies/wolfpack-ai-command/` | `https://intake.wolfstrategyllc.com/wolfpack-ai-command/` | 2026-08-15 (#190) |
| `sm3-specific-pages/setmaster3-case-study/` | `https://intake.wolfstrategyllc.com/setmaster3-case-study/` — **indexed** (flipped from `noindex` 2026-08-04) | 2026-08-04 (#104) |
| `sm3-specific-pages/setmaster3/` | `https://intake.wolfstrategyllc.com/setmaster3/` — **indexed**; the product page, two real downloads | 2026-08-05 (#144) |
| `portfolio/` | `https://intake.wolfstrategyllc.com/portfolio/` | 2026-08-05 (#126) |
| `github/` | `https://intake.wolfstrategyllc.com/github/` — **`noindex`**, direct-link only; one link, to `github.com/wolfpackdata` | 2026-08-07 (#155) |
| `pilot-project/` | `https://intake.wolfstrategyllc.com/pilot-project/` — **`noindex`**, direct-link only; the $5,000 fixed-fee pilot offer | 2026-08-18 (#236) |

`sm3-specific-pages/` deploys as **two folders to the intake root** — the page folder and
`sm3-assets/` — and `planning/` never deploys. **Copy the git-tracked file list, not the
folder:** `sm3-assets/img/` holds one gitignored capture that leaks a Windows user directory,
and a folder mirror would publish it. `git ls-files sm3-specific-pages/…` is the safe source.

`hire/` deploys as **one folder**, not two — both pages share its `assets/`.

Pages can be turned back on if a page ever needs to serve from here — it was
`source: main /`, `build_type: legacy`, no CNAME, HTTPS enforced.
