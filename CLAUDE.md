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
(`ai-coaching/`, see below), and the public rates page (`rates/`, see below); more site
pieces land here as they're built. Verify by opening the page in a browser.

GitHub Pages is **on** for this repo, serving `main` at
`https://wolfpackdata.github.io/wp-website/` (no custom domain, no root `index.html` — the
root 404s, which is expected). The ROI calculator is live at `/roi-calculator/` and is
linked from the Wix site's *AI Coaching* page; the public rates page is live at `/rates/`.
**Merging to `main` is deploying.**

## `rates/` — public rates page
The **public, indexable, evergreen** rates page — live at
`https://wolfpackdata.github.io/wp-website/rates/` (deployed 2026-07-23; Wix links to it,
Ry manages the Wix side). It is the public sibling of the **direct-link Q3 page** in
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
- **Book-first, one CTA:** every CTA is the 30-minute-call calendar link (#8) — no
  intake-form links.
- **No external requests**; fonts/images self-hosted in the subfolder. Coral is rationed —
  the allowed uses are listed in the header comment of `rates/css/rates.css`; keep it true.
- The two "Two ways to work with Wolfpack" tiles carry Ry's images
  (`img/path-engineering.png` / `img/path-coaching.png`, #11) in fixed 16:9 `.path__shot`
  frames (`object-fit: cover`).

## `ai-coaching/` — AI Coaching for Professionals landing page
Replaces the Wix page at `wolfstrategyllc.com/general-7` (Ry repoints the Wix nav link
himself). Like the rates page, it ships by **copying the folder into
`wolfpackdata/ai-coaching-intake`** (which owns `intake.wolfstrategyllc.com`) — target URL
`intake.wolfstrategyllc.com/ai-coaching` — only after Ry approves it locally. **Not yet
deployed as of 2026-07-22.** When it ships, update the Web Property Map *and* this file.
(Merging this repo to `main` also publishes it at the github.io path — fine, same policy
as `roi-calculator/`.)

Conventions the page must keep:
- **Design system inherited from `wolfpackdata/wp-rates-page`** (`css/rates.css` there is
  the pattern library). Coral `#F95954` is strictly rationed; the allowed uses are listed
  in the header comment of `ai-coaching/css/coaching.css` — keep that comment true. Where
  coral is a fill, text on it is navy, never white (AA).
- **Public and indexable** (unlike the noindex rates page), and **no external requests** —
  fonts and images are self-hosted in the subfolder.
- **The one correct booking link for 30-minute-call CTAs is
  `https://calendar.app.google/WUQnihH9GEEJRMARA`** (#8). The old link
  (`…/13EANJ63HKqMc76z6`) is the **45-minute tutoring-engagements calendar** — valid for
  tutoring only, never for the call funnel. (History: the rates page once shipped a third,
  wrong link — `wolfpackdata/wp-rates-page#21`.) The funnel is book-first: the intake link
  is sent after booking, so this page deliberately does not link the intake form.
- The reviews section holds **dashed placeholder cards** until Ry inserts real student
  reviews (instructions live in an HTML comment above that section — don't remove it
  until real reviews are in).
- Approved assets only: the `claude-memory-by-surface` infographic, Ryan's portrait, and
  the logo. The other coaching infographics (mentality shift, prompting tips) are
  **reserved for live sessions** — don't add them to public pages.

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
