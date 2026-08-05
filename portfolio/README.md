# `portfolio/` — portfolio & case study landing page

One page presenting the case studies written so far and the applications and workflows in
the portfolio. The page Ry sends, or the Wix nav points at, when someone wants to see the
work rather than read a résumé or a rate card.

| Folder | Source content | Public URL |
|---|---|---|
| `portfolio/` | `../ryan-resume-dev/resume_build/content/eng_only.yaml` (`projects` section) | `https://intake.wolfstrategyllc.com/portfolio/` |

Full design plan, decisions ledger, and acceptance criteria:
[`docs/portfolio-page-design-plan.md`](../docs/portfolio-page-design-plan.md). Built under
issue [#95](https://github.com/wolfpackdata/wp-website/issues/95).

## Status

**Built, not yet deployed.** The folder is complete and verified; it reaches the public only
by copying into `wolfpackdata/ai-coaching-intake`. See *Deploying* below.

- [x] `fonts/` — 14 woff2 (Roboto + Montserrat), copied from `hire/assets/fonts/`
- [x] `img/` — 8 app screenshots + the wolf mark
- [x] `css/portfolio.css`, `css/fonts.css`
- [x] `js/reveal.js`
- [x] `index.html`
- [ ] Hero copy — **placeholder, awaiting Ry** (see below)
- [ ] Deployed to `ai-coaching-intake`

Verified: zero external requests, zero horizontal overflow at 320/360/390/414/768/1024/
1440px, complete render with JavaScript disabled, single H1 with clean heading order,
`verify_facts.py` check 6 passing.

## Four things to know

**1. The hero copy is a placeholder, on purpose.** It has to address a prospective client and
a hiring company in the same breath, which is a positioning judgment rather than a copy task
(design plan D-004). The `.ph-copy` block in `index.html` says so on the page itself, and the
headline and standfirst under it are deliberately plain and factual so nothing false ships if
the page goes live first. **When the real copy lands, delete the `.ph-copy` block and its rule
in `css/portfolio.css`** — that also returns the coral ration to seven uses.

**2. Audience is both clients and hiring companies, and that is the whole design
constraint.** Every other page here serves one or the other, which is why none of them could
do this job. It is also why the page carries the applications and case studies but none of
the résumé apparatus: work evidence reads the same to both audiences, career narrative does
not.

**3. It is indexed, and it must not link the `hire/` pages.** Those are `noindex`,
direct-link only, deliberately linked from nothing. A public indexed page linking them
defeats that in one step (design plan D-003). Hiring managers get the résumé from Ry directly.

**4. Self-contained folder, unlike `hire/`.** Its own `css/`, `fonts/`, `img/`, `js/`, the
same as `rates/` and `ai-coaching/`. `hire/`'s shared-`assets/` arrangement exists because two
pages ship as one folder; this is one page, and nothing in it reaches outside itself.

## Content rules

- **Application names and blurbs are verbatim from `eng_only.yaml`**, the same strings the
  `hire/` pages carry. **`verify_facts.py` check 6 enforces this** — it compares every
  `.app__name` and `.app__blurb` on this page and both `hire/` pages against its source
  résumé, and reports the exact point of divergence on a mismatch. Run it after any edit to
  a card:

  ```powershell
  cd ..\ryan-resume-dev\resume_build ; python verify_facts.py
  ```

- **Do not tone-edit the ported blurbs.** [`docs/ryan-blog-tone.md`](../docs/ryan-blog-tone.md)
  §8 exempts résumé-derived content precisely so a third wording cannot appear. The tone rules
  bind the section kickers, ledes, case-study blurbs, and closing block only, and those pass
  the §9 checklist.
- **SetMaster 3 uses the `eng_only` framing**, not `eng_music`'s "RML SetMaster 3" (D-005).
  One source YAML for all eight cards.
- **The coral ration is enumerated in the header comment of `css/portfolio.css`.** Keep that
  comment true. It currently lists eight uses because the placeholder label is one of them,
  marked temporary; it returns to seven when the hero copy lands.
- **One CTA, the 30-minute intro call.** No intake-form link, no résumé download. The
  outbound `/rates_public/` link sits in a quiet coda band and is navigation, not a second
  funnel CTA.
- **`reveal.js` is copied, never rewritten** — byte-identical to `hire/assets/js/reveal.js`
  apart from its header comment, so reveal timing and scroll-spy match every other long-form
  page here.

## Adding a case study card

The `.cases` grid is built so each addition is one `<article class="case">`. A published study
gets a `.btn--ghost` link; an unpublished one gets the `.case__chip` "In preparation" device at
the same size, so adding the link later changes one element and not the layout. Case numbers
come from a CSS counter, so they renumber themselves.

**Both cards are live links as of 2026-08-04.** The SetMaster 3 study deployed that day (#104)
and its chip became a link, which is what the device was for. No `.case__chip` is in use on the
page right now; the rule stays in the stylesheet for the next unpublished study.

**The no-links rule is about the `hire/` résumés specifically, not about `noindex`.** Design
plan **D-003** and **D-010** settle it: a case study carries none of the résumé's problems, and
neither published study links back to `hire/`, so nothing here creates a path to those pages.
As of 2026-08-04 both linked case studies are **indexed** anyway, so this page links nothing
`noindex` at all. The rule that still binds: **never link `hire/`.**

**Use an absolute URL for a case-study link, not a relative one.** In this repo a case study
lives at `case_studies/<name>/`, but it deploys to its own root-level slug, so the two layouts
share no relative path.

## Deploying

This repo **serves nothing.** The page goes live only by copying `portfolio/` into
`wolfpackdata/ai-coaching-intake`, which owns `intake.wolfstrategyllc.com`. The folder here
mirrors the deploy path, so it is a single copy of `portfolio/` into that repo's root with no
path rewriting.

**This repo stays the source of truth. Never edit the deployed copy; re-copy on change.**

After shipping, update the canonical-URL table in [`CLAUDE.md`](../CLAUDE.md) and the Notion
**Web Property Map**.
