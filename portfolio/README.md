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

**Built and deployed.** Live at `https://intake.wolfstrategyllc.com/portfolio/` since
2026-08-05 ([#126](https://github.com/wolfpackdata/wp-website/issues/126)). This repo stays
the source of truth; it reaches the public only by re-copying into
`wolfpackdata/ai-coaching-intake`. See *Deploying* below.

- [x] `fonts/` — 14 woff2 (Roboto + Montserrat), copied from `hire/assets/fonts/`
- [x] `img/` — 8 app screenshots + the wolf mark
- [x] `css/portfolio.css`, `css/fonts.css`
- [x] `js/reveal.js`
- [x] `index.html`
- [x] Hero copy — **written by Ry 2026-08-04**; placeholder and its CSS removed
- [x] Deployed to `ai-coaching-intake` — 2026-08-05, `ai-coaching-intake#51`

Verified: zero external requests, zero horizontal overflow at 320/360/390/414/768/1024/
1440px, complete render with JavaScript disabled, single H1 with clean heading order,
`verify_facts.py` check 6 passing.

## Four things to know

**1. The hero copy is Ry's, written 2026-08-04.** It shipped as a marked placeholder first,
because the hero had to address a prospective client and a hiring company in the same breath
and that is a positioning judgment rather than a copy task (design plan D-004). His answer is
worth noting: **"Systems, apps, and projects"** over *"Selected examples of recent
applications, data systems, and AI workflows built and evolving, with some case studies
below."* It solves the two-audience problem by addressing **neither audience directly** — it
just names the work, which reads the same to a client and to an employer. Do not re-point it at
one of them.

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

- **Do not tone-edit the ported blurbs.** They are résumé-derived, and rewording them here
  creates a third wording that `verify_facts.py` check 6 then fails on. Everything else on the
  page — the section kickers, ledes, and case-study blurbs — is Ry's to judge; the voice guide
  that used to govern them was removed 2026-08-06 (#150).
- **SetMaster 3 uses the `eng_only` framing**, not `eng_music`'s "RML SetMaster 3" (D-005).
  One source YAML for all eight cards.
- **The coral ration is enumerated in the header comment of `css/portfolio.css`.** Keep that
  comment true. **Six uses**, and the count has only ever gone down: a temporary eighth carried
  the hero placeholder's label and left with it, and the closing CTA left with its block
  (D-013).
- **One accented CTA — the 30-minute intro call — plus exactly one subordinate destination,
  the SetMaster 3 product page.** Still no intake-form link, no résumé download, no rates link:
  a `/rates_public/` coda band briefly existed and **Ry cut it** on 2026-08-04 (**D-011**).
  The subordinate link was ruled in on 2026-08-17 (**D-015**, #218) and sits in the SetMaster
  tile, navy-ghost and one size down — the site brief's §6 subordination rule, which is what
  keeps the intro call the only accented ask on the page. **Case-study links do not count
  against this**: D-014 settled that they are navigation within the work. Do not add a third
  destination without a ruling of its own.
- **The page ends on the case studies, and that is deliberate.** The closing "Start with a
  call" section was cut on 2026-08-04 (**D-013**), the day after its copy was rewritten — the
  rewrite was fine, the block was not wanted. The intro call still reaches the reader twice,
  through the nav CTA and the hero CTA, so nothing about the one-destination rule changed. Do
  not re-add a closing section, and do not "restore" the `#contact` nav item: there is no
  `#contact` section for it to point at.
- **Every case card carries a real image, and none of them is a re-encode.** The financial
  model card showed a `Figures in preparation` panel until its case study had a figure; it now
  carries that page's beacon hero (#113), built at card width by
  `case_studies/ops_fin_model_support/planning/hero/build_hero.py` rather than re-encoded from
  the page-sized file. The AI Command card (#192) is built the same way, by that case study's
  own `build_hero.py`, which grew the identical output-width argument for the purpose —
  **one composition, several sizes, no generational loss.** Rebuild a card image rather than
  scaling the delivered one. The `.case__shot--empty` device stays in the stylesheet for the
  next unpublished study. **All four card images are their case study's own hero**, and
  Consolidation stopped being the exception on 2026-08-17 (#226): it carried the transaction map
  while that page shipped no hero, and now carries the hero art Ry supplied. Its
  `planning/hero/build_hero.py` writes this file and `hire/assets/img/`'s copy in one run — the
  two are byte-identical by construction, so **don't replace either with a copy of the other**,
  and nothing is upscaled (the generator refuses).
- **`reveal.js` is copied, never rewritten** — byte-identical to `hire/assets/js/reveal.js`
  apart from its header comment, so reveal timing and scroll-spy match every other long-form
  page here.

## Adding a case study card

The `.cases` grid is built so each addition is one `<article class="case">`. A published study
gets a `.btn--ghost` link; an unpublished one gets the `.case__chip` "In preparation" device at
the same size, so adding the link later changes one element and not the layout. Case numbers
come from a CSS counter, so they renumber themselves.

**All four cards are live links as of 2026-08-17.** The SetMaster 3 study deployed on
2026-08-04 (#104) and its chip became a link, which is what the device was for; the AI Command
study was added already linked on 2026-08-15 (#192); Consolidation Under Pressure was added on
2026-08-17 (**D-016**, #222). No `.case__chip` is in use on the page right now; the rule stays
in the stylesheet for the next unpublished study.

**New cards are appended, and the section head states no count.** Both matter. The old lede
said *"All three are published and all three are a click away"*, which went stale the moment a
fourth shipped — D-014 flagged that failure mode when it changed the number from two to three,
and #222 is the addition that proved it. **The hire pages' card order is Ry's and is specific to
those pages; it is not a site-wide order to mirror here.**

**Two tiles in the applications gallery carry the same link as a case card** (#218): `SetMaster
3` and `Notion–GitHub AI Dev Command Center`, the two whose system has a published write-up. That
is the whole selection rule — a button on every tile would say nothing. Put them **after
`.app__blurb`**, never between the name and the blurb: `verify_facts.py` check 6 matches those
two as adjacent siblings, so anything wedged between them unguards a résumé string *without
failing the check*.

**The no-links rule is about the `hire/` résumés specifically, not about `noindex`.** Design
plan **D-003** and **D-010** settle it: a case study carries none of the résumé's problems, and
neither published study links back to `hire/`, so nothing here creates a path to those pages.
As of 2026-08-15 all three linked case studies are **indexed** anyway, so this page links
nothing `noindex` at all. The rule that still binds: **never link `hire/`.**

**Use an absolute URL for a case-study link, not a relative one.** In this repo a case study
lives at `case_studies/<name>/`, but it deploys to its own root-level slug, so the two layouts
share no relative path.

## Deploying

This repo **serves nothing.** The page goes live only by copying `portfolio/` into
`wolfpackdata/ai-coaching-intake`, which owns `intake.wolfstrategyllc.com`. The folder here
mirrors the deploy path, so it is a single copy of `portfolio/` into that repo's root with no
path rewriting.

**This file is the one exception — `README.md` does not deploy.** It is internal build
documentation, and unlike `hire/` (which is `noindex` and does carry its README into the
intake repo) this page is **public and indexed**. Copy from `git ls-files portfolio` minus
this file. If the `hire/README.md` already sitting in the intake repo ever bothers you, it
can come out the same way — flagged, not actioned.

**This repo stays the source of truth. Never edit the deployed copy; re-copy on change.**

After shipping, update the canonical-URL table in [`CLAUDE.md`](../CLAUDE.md) and the Notion
**Web Property Map**.
