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
holds the ROI calculator (`roi-calculator/`); more site pieces land here as they're built.
Verify by opening the page in a browser.

GitHub Pages is **on** for this repo, serving `main` at
`https://wolfpackdata.github.io/wp-website/` (no custom domain, no root `index.html` — the
root 404s, which is expected). The ROI calculator is live at `/roi-calculator/` and is
linked from the Wix site's *AI Coaching* page. **Merging to `main` is deploying.**

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
