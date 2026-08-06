# `github/` — the "this is my GitHub" page

One screen with one link on it. Ry sends this URL when a prospective partner, employer, or
collaborator wants to see the code, and it sends them to
[`github.com/wolfpackdata`](https://github.com/wolfpackdata).

| Folder | Public URL | Robots |
|---|---|---|
| `github/` | `https://intake.wolfstrategyllc.com/github/` | `noindex, nofollow` |

Built under issue [#155](https://github.com/wolfpackdata/wp-website/issues/155).

## Status

**Built, not yet deployed.** It reaches the public only by copying into
`wolfpackdata/ai-coaching-intake`. See *Deploying* below.

- [x] `fonts/` — 14 woff2 (Roboto + Montserrat), copied from `portfolio/fonts/`
- [x] `img/wolfpack-logo.png`
- [x] `css/fonts.css` (copied), `css/github.css`
- [x] `index.html`
- [ ] Deployed to `ai-coaching-intake`
- [ ] `CLAUDE.md` canonical-URL table row updated with a deploy date
- [ ] Notion **Web Property Map** given a row

Verified: zero external requests, `scrollWidth == clientWidth` at 320/360/390/414/480/560/
768/1024/1440/1920px, complete render with no JavaScript on the page at all, single `h1`.

## The one rule

**Exactly one outbound destination: `github.com/wolfpackdata`.**

This is a stricter version of the rule `portfolio/` carries, and it is stricter in a
specific way. There, the single destination is the intro call; here there is no intro call,
because **this page is not a funnel**. Ry's instruction was explicit: *"this is not to funnel
people to contact me, it is just a 'this is my GitHub' link."*

So the page carries **no calendar CTA, no intake-form link, no rates link, no résumé
download** — and, uniquely in this repo, **no `mailto:` in the footer**. Every other footer
here carries `ryan@wolfstrategyllc.com`. This one deliberately does not; an email address in
the footer is exactly how a not-a-contact-page becomes a contact page.

Two things that are **not** second destinations, both by the precedent `portfolio/` set
(#126): the header wordmark and the footer link to `wolfstrategyllc.com`. That is site
chrome, present on every page here, and it is how a reader gets back to the main site.

**Never link the two `hire/` pages.** Inherited unchanged from `portfolio/`. This page is
itself `noindex`, which makes the prohibition weaker but not void — `noindex` is not access
control, and one page pointing at the other still hands a reader both framings.

## Four things to know

**1. It states no repository count and links no individual repo.** This is the design
decision the page turns on. The profile link is self-updating: it stays correct as repos are
opened, renamed, archived, or made private, and the page never needs an edit to keep up. A
hardcoded list of repo cards is the version of this page that quietly goes wrong — it would
have been accurate on the day it shipped and wrong on the first day Ry opened a third repo.

Worth recording, because it is the context the decision was made in: at build time
`github.com/wolfpackdata` is a **User** account with **two public repos** — `setmaster` and
`wp-website` — against nineteen private ones. Nothing on the page depends on that ratio, so
nothing on the page breaks when it changes. **Whether to open more repos for a hiring
audience is a separate question and is not this page's job to answer.**

**2. `noindex, nofollow`, direct-link only.** Two reasons, and the second is load-bearing. A
one-link page is thin content under a brand whose other indexed pages are substantial; and
it would compete with `/portfolio/` for the same queries. `/portfolio/` is the page that
should win a search for Ryan Hickey's work, because it *shows* the work rather than pointing
at it. Don't add this page to a sitemap, and don't link it from Wix, `portfolio/`, or
`rates/`.

**3. There is no JavaScript, and no `js/` folder.** Every other long-form page here ships
`reveal.js`. Nothing on this page is below the fold to reveal, and a page whose entire job is
one link should not need a script to show it. This is the same principle `portfolio.css`
states when it scopes the hidden initial state to `.js` — applied here by deletion rather
than by scoping.

**4. Self-contained folder**, like `portfolio/`, `rates/`, and `ai-coaching/` and unlike
`hire/`. Its own `css/`, `fonts/`, `img/`. Nothing in it reaches outside itself, so it
deploys as a single folder copy with no path rewriting.

## Copy

The headline is Ry's own framing of the request, not a marketing rewrite of it. He described
what he wanted as *"just a 'this is my GitHub' link"*, and the `h1` is that sentence.

Copy on this page is Ry's to judge, against no written spec — the voice guide that used to
govern page copy was removed 2026-08-06 (#150). Match the other pages here rather than
reaching for a rulebook.

## Coral

**Four uses**, enumerated in the header comment of `css/github.css` — the smallest ration of
any page in this repo, which is what a page with one link should cost. Keep that comment
true. Where coral is a fill, text on it is navy (5.8:1), never white (fails AA); the GitHub
mark inside the button inherits navy through `fill: currentColor` rather than declaring its
own color, so there is no second value to keep in sync.

## The GitHub mark

Inlined as an `<svg>` in `index.html`, not fetched and not committed as a file, so the page
keeps its zero-external-requests property. It is GitHub's own mark, used to link to GitHub —
which is what it is for.

## Deploying

This repo **serves nothing.** The page goes live only by copying `github/` into
`wolfpackdata/ai-coaching-intake`, which owns `intake.wolfstrategyllc.com`. The folder name
here is already the URL slug, so it copies to that repo's root unchanged, the same as
`portfolio/` and unlike the two case studies.

**`README.md` does not deploy.** Internal build documentation, same exclusion `portfolio/`
carries (#129). Copy from `git ls-files github` minus this file.

**This repo stays the source of truth. Never edit the deployed copy; re-copy on change.**

After shipping, update the canonical-URL table in [`CLAUDE.md`](../CLAUDE.md) and give the
page a row on the Notion **Web Property Map** — a new page on `intake.` is one of that map's
explicit staleness triggers.
