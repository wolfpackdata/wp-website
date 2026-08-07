# Website work order — SetMaster 3 LinkedIn feature prep

**Requested by:** Ry
**Date:** 2026-08-07
**Findings verified:** 2026-08-06, against the live sites
**Why:** SetMaster 3 is going into the Featured section of Ry's personal LinkedIn profile and
behind the custom action button on the Wolfpack Data & Strategy company page. Both surfaces will
point at `wolfstrategyllc.com` pages rather than at GitHub, so the site is the funnel. Two things
on the site block that from working properly.

## Current state (verified, not assumed)

| Page | URL | Status |
|---|---|---|
| Product / download | `https://intake.wolfstrategyllc.com/setmaster3/` | Live. v3.0.4 Windows + macOS buttons. **Open Graph tags present and correct.** |
| Case study | `https://intake.wolfstrategyllc.com/setmaster3-case-study/` | Live. **No Open Graph tags at all.** |
| Portfolio index | `https://intake.wolfstrategyllc.com/portfolio/` | Live. Features SetMaster 3 as a card and links the case study. |
| Main site | `https://www.wolfstrategyllc.com` | **No mention of SetMaster anywhere.** |

Note for whoever picks this up: the two SetMaster pages live on the `intake.` subdomain, which
appears to be separate from the `www.` site. Confirm which system serves each before editing —
the fix location differs.

---

## Item 1 — Add Open Graph tags to the case study page

**Priority: blocking.** Do this before anything is posted to LinkedIn.

### Problem

`https://intake.wolfstrategyllc.com/setmaster3-case-study/` has zero `og:` and zero `twitter:`
meta tags. Confirmed by fetching the raw HTML and grepping for both prefixes — no matches.

When this URL is added to LinkedIn's Featured section or pasted into a post, LinkedIn will render
a bare card: no image, just a scraped title, possibly a truncated or wrong description. Against
the product page — which *does* have correct tags and renders a full-width image card — it will
look broken. This is the single highest-value page in the funnel (it's the one that sells Ry's
consulting capability, not just the free software), so it cannot be the one with the ugly card.

The page does already have a good `<title>` and `<meta name="description">`, so the copy work is
done. It just needs the social tags.

### Fix

Add to the `<head>` of the case study page:

```html
<meta property="og:type" content="article">
<meta property="og:url" content="https://intake.wolfstrategyllc.com/setmaster3-case-study/">
<meta property="og:title" content="SetMaster 3: From a Spreadsheet on a Plane to a Robust Application">
<meta property="og:description" content="A professional DJ built his own set preparation tool three times in three years. The third is a specified, tested, offline web application.">
<meta property="og:image" content="https://intake.wolfstrategyllc.com/sm3-assets/img/a02-set-editor.png">
<meta property="og:image:width" content="1904">
<meta property="og:image:height" content="904">
<meta name="twitter:card" content="summary_large_image">
```

Title and description above are lifted verbatim from the page's existing `<title>` and
`<meta name="description">` — intentionally, so the card matches the page. Change them only if
the page copy changes.

### On the image

Reusing `sm3-assets/img/a02-set-editor.png` (the set-editor screenshot) is the low-effort
option and is acceptable: 1904×904, ratio 2.11, ~369 KB. LinkedIn wants 1.91:1, so it renders
as a large-image card with minor edge cropping. It is already the `og:image` on the product page.

Optional improvement, if there's appetite: give the case study its **own** 1200×627 image rather
than sharing the product page's. Two Featured tiles side by side with the identical screenshot
reads as a duplicate. A purpose-built card — screenshot plus the case study title — would
differentiate them. Not blocking; the shared screenshot ships fine.

### Verification

1. Re-fetch the page and confirm the tags are in the served HTML (not just the source — check
   for any CDN/cache layer in front).
2. Run **both** URLs through the LinkedIn Post Inspector
   (`https://www.linkedin.com/post-inspector/`) and confirm the preview renders with image,
   title, and description:
   - `https://intake.wolfstrategyllc.com/setmaster3-case-study/`
   - `https://intake.wolfstrategyllc.com/setmaster3/`
3. **This step is not optional.** LinkedIn caches link previews aggressively — roughly a week.
   If it scrapes the page before the tags land, the bad card sticks and re-sharing won't fix it.
   The Post Inspector forces a re-scrape. Run it *after* the tags are live, and report back that
   the preview looks right before Ry posts.

---

## Item 2 — Surface SetMaster on the main `www` site

**Priority: high, not blocking.** Ship Item 1 first if they have to be sequenced.

### Problem

`www.wolfstrategyllc.com` does not mention SetMaster anywhere — not on the homepage, not in the
main navigation. The SetMaster pages are reachable only via the Portfolio page, which itself
lives on the `intake.` subdomain.

The consequence for the LinkedIn campaign: a visitor arrives from LinkedIn directly onto the case
study, reads it, is warm, and then clicks through to the company's actual homepage — where there
is no trace of the thing they just read about. The funnel dead-ends at the moment of highest
intent. It also means every visitor is landing on a subdomain that shares no navigation or visual
continuity with the main site, which weakens the "this is a real firm" signal the campaign exists
to create.

### Fix

The goal is that a visitor can move between `www` and the SetMaster pages in both directions
without hitting a dead end. Suggested, in rough order of value:

1. **Homepage presence on `www`** — a portfolio/proof section or single highlight card for
   SetMaster 3, linking to the case study. This is the main ask.
2. **Navigation continuity** — make Portfolio reachable from `www` navigation in a way that
   doesn't feel like leaving the site, and give the SetMaster pages a path back to `www`
   (header/footer link home at minimum).
3. **Footer link on the SetMaster pages** back to the main site and to Contact.

Design and placement are the website project's call — the requirement is bidirectional
reachability, not a specific layout.

### Open question for the website project

Should the SetMaster pages move from `intake.wolfstrategyllc.com` to `www.wolfstrategyllc.com`
(e.g. `www.wolfstrategyllc.com/setmaster3/`) rather than being cross-linked across subdomains?

That would consolidate the funnel, the domain authority, and the analytics onto one host, and
would make Item 2 mostly moot. It is also more work and may not be possible depending on how the
two systems are hosted. **Flagging it as a decision, not recommending it blindly** — assess the
cost and come back to Ry with a recommendation. If a move is on the table at all, do it *before*
the LinkedIn Featured links go up, because the featured URLs are painful to change once posted
and any redirect will cost preview re-scrapes.

---

## Appendix — optional, same pages, cheap while you're in there

Not part of the two items. Ry's only current signal is the GitHub download counter (5 downloads
total as of 2026-08-06), which says nothing about where traffic came from.

If analytics are already in place on these pages, no site work is needed — Ry can append UTM
parameters himself on the LinkedIn side:

```
/setmaster3-case-study/?utm_source=linkedin&utm_medium=featured&utm_campaign=sm3&utm_content=personal
/setmaster3-case-study/?utm_source=linkedin&utm_medium=button&utm_campaign=sm3&utm_content=company
/setmaster3/?utm_source=linkedin&utm_medium=post&utm_campaign=sm3
```

What's worth confirming from the website side: that analytics are actually installed on **both**
the `intake.` subdomain and `www`, and that they're the same property — otherwise the cross-domain
journey shows up as two unrelated sessions and the campaign can't be measured end to end.

---

## Outcome (2026-08-07)

This work order is closed. It was assessed against the repo and the deployed copies, and the
result is [`docs/social-cards-and-linkedin-readiness-plan.md`](../../docs/social-cards-and-linkedin-readiness-plan.md),
which carries the full reasoning and a decisions ledger. Item by item:

- **Item 1 — done, and widened.** The case study's missing Open Graph tags were confirmed
  exactly as reported, and fixed. The optional improvement was taken: the page gets a
  **purpose-built 1200×627 card**, not the product page's set-editor screenshot, so the two
  Featured tiles don't read as duplicates. The same defect was then found on
  `case_studies/ops_fin_model_support/` and partially on `ai-coaching/` and `roi-calculator/`,
  so the fix became a **site-wide sweep** rather than a one-page patch — six pages edited
  (the guard's first run also caught `/setmaster3/` missing its image dimensions and alt
  text), three cards generated, and a `social-cards/check_meta.py` guard added so the gap
  can't reopen unnoticed. Tracked in wp-website #161; the deploy is ai-coaching-intake #57.
- **Item 2.3 — no work needed.** The footer/back-links it asks for already existed on both
  SetMaster pages before this work order was written: each has a nav wordmark to
  `wolfstrategyllc.com`, the case study has a footer link home and a "Contact Ryan" CTA, and
  the product page has a bare "Visit wolfstrategyllc.com" button above its footer (#144).
- **Items 2.1 and 2.2 — handed to Ry as a Wix work order.** They cannot be done from this
  repo at all: `www.wolfstrategyllc.com` is served by Wix, and nothing here can put anything
  on it. Captured as a Notion task — homepage presence for SetMaster 3, Portfolio in the `www`
  navigation, and the standing rule that neither the `hire/` pages nor `github/` may be linked
  from Wix.
- **The open question — ruled out.** The SetMaster pages do not move to `www`.
  `intake.wolfstrategyllc.com` is a **GitHub Pages custom domain bound to exactly one repo**
  (`wolfpackdata/ai-coaching-intake`), and `www` is Wix. So a "move" is not a copy; it is
  either rebuilding the pages inside Wix — abandoning the shared stylesheet, `reveal.js`, and
  version control — or taking `www` off Wix. That is a re-platform, not a pre-LinkedIn task.
- **The appendix was wrong in its premise.** It assumes analytics might already be in place.
  **There is no analytics on any page in this repo, on either host** — every HTML file was
  grepped for the usual tags and scripts, with zero hits. The UTM parameters it suggests
  would therefore be **recorded by nothing** today. Adding a tag manager is also an explicit
  exception to the no-external-requests rule that `CLAUDE.md` and four folder READMEs carry,
  so it is a real architecture decision rather than a cheap add-on: parked to wp-website #162
  and deliberately not blocking the tag fix. **The LinkedIn launch will be unmeasured** —
  an acceptable trade, but a known one.
