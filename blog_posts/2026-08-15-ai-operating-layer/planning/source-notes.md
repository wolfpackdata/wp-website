# Source notes — An AI Operating Layer for Streamlining Project Delivery

Everything in this post came from one place: the case study at
`case_studies/wolfpack-ai-command/index.html`, as it stood at commit `3c5c292`
(2026-08-15, after Ry's tone pass in #189 and the shield hero embed in #191).

Ry's instruction for this post was explicit: **use verbatim copy from the case study
for most of the blog post so you don't reinvent the wheel** — the same for the
LinkedIn draft. So this is not a post *about* the case study written from notes. It is
the case study's own argument, cut down to a feed-length version, in its own words.

## Why that matters more than it sounds

The case study's copy is **Ry's**, not drafted-then-approved. The 2026-08-15 tone
iteration (#188/#189) was his own edit pass — the blunt bolded openers
(*"Chaos."*, *"Extremely boring."*), the TPS Report line, the direct reader address.
The standfirst and `h1` are supplied copy that
`case_studies/wolfpack-ai-command/planning/outline.md` D-019 says may not be reworded
without him.

**A lifted paragraph re-edited here silently forks his copy.** There is no validator
watching this pair the way `verify_facts.py` check 6 watches the résumé blurbs across
`hire/` and `portfolio/`, and no `verify_copy.py` the way the M&A case study has. If
the case study changes, this post has to be re-lifted by hand. Change the case study
first, then re-lift — never the other way around.

## Passage map

| Post section | Case study source | Treatment |
|---|---|---|
| Opening three paragraphs | §01 · The consensus | Verbatim, all three paragraphs |
| The two framing paragraphs after them | — | **Original copy, not lifted** (#203) — see below |
| "One Role, Two Completely Different Jobs" — the two lists | §02 · The split, the two `.card` lists | Verbatim bullet text, reflowed from two cards into two bolded paragraphs (Ricos has no card) |
| The pull quote | §02 `.pull` | Verbatim |
| "Extremely boring." paragraph | §02 prose | Verbatim |
| "There is one catch…" | §02 prose | Verbatim, minus the "calling an audible" sentence (cut for length) |
| "My question became…" | §02 closing line | Verbatim |
| "I Did Not Want Another Chatbot…" opener | §04 · The bet | Verbatim, minus the Notion-templates sentence (inside baseball for a feed reader) |
| The three governance questions | §04 `.numlist` | Verbatim, all three |
| "So I built the answers before I built the automation." | §04 prose | Verbatim ("code/documents" set as "code, documents") |
| "The rules are not a tuned system prompt…" | §04 `.callout--big` | Verbatim |
| "The whole thing — workspace governance…" | §04 closing prose | Verbatim. **This is the name's one use in the post** |
| "How Do You Know What the AI Did?" first two paragraphs | §06 · Supervision | Verbatim, minus the "when you develop using AI" sentence |
| "A silent state change…" | §06 F3 table, row 4 | Condensed from the table's last two cells |
| "A live status no one could have observed is theater." | §06 anti-theater | Verbatim rule text, condensed surround |
| "Merged is not accepted." | §05 code layer | Verbatim rule text, condensed surround |
| "forbidden from assigning work to itself" | §06 prose after F3 | Verbatim, minus the middle sentence |
| "What I Am Explicitly Not Claiming" — four bullets | §10 `.status` chips | Verbatim, all four |
| Closing CTA paragraph | §10 close `.close__lede`, second paragraph | Paraphrased down to one sentence |

## The one passage that is not lifted

Two short paragraphs sit between the verbatim opener and the first section heading, added
2026-08-15 on Ry's instruction (#203). They are **the only original prose in the body** and
they exist because the post needed to say two things the case study has no reason to say
about itself:

1. That this is an **abbreviated summary** of a longer case study.
2. That the system is **ready to integrate now** and starts adding value in **days, not
   months**.

The second is a claim, and it is the offer's estimate rather than a measured result — the
same footing as the case study's *"hours, not days"* line, which its `.tm` note explicitly
labels as the offer's estimate. It carries no number and must not gain one. The post's
*Not measured* bullet is untouched and does not conflict: it disclaims productivity
outcomes, which is a different claim from how fast the thing installs.

They sit **after** the three-paragraph opener rather than above it, so the hook lands before
the framing, and they deliberately **do not enumerate what the case study contains** — the
closing *The Full Version* section already does that, and saying it twice would make the
post read like it is apologising for being short.

## Deliberately left out

- **Every artifact count.** The case study's counts (8 skills, 54 rules, 10 sections,
  5 drift checks, 0 destructive tools, 1 AI identity) were measured 13 Aug 2026 and
  are stamped as such on that page. Repeating one here creates a second copy with no
  date attached to it, which is the exact failure mode this whole system exists to
  prevent. The post cites none.
- **The <50% completion figure.** Ry cut it from the case study in his 2026-08-15
  pass; it is not coming back into a derived post.
- **The three-layer tour (§05), confidentiality (§07), setup (§08), and the
  mistakes-to-rules table (§09).** These are the reason to click through. A post that
  summarizes all eleven sections is a worse case study, not a better post.
- **Icon chips, the shield's four hues, the F-figure placeholders.** Page furniture.

## Facts checked at write time

- Case study `h1`: *An AI Operating Layer for Streamlining Project Delivery* —
  the post's title, verbatim, per the repo rule set in #119.
- Canonical case study URL: `https://intake.wolfstrategyllc.com/wolfpack-ai-command/`
  (from the page's own `<link rel="canonical">`). **Live — fetched and confirmed
  2026-08-15**, h1 matching. The repo's root `CLAUDE.md` deployment table has not been
  updated to include it, so that table is stale rather than authoritative here.
- Intro-call URL: `https://calendar.app.google/zHNd1NA9wzb4VRLw5`, matching the case
  study's two CTAs and the current URL per #32.

## Redaction check

Nothing held back. The only source is a page that is itself written for publication
under D-002 ("capabilities, not internals") and already committed to this public
repo. No client is named anywhere in it, no repository names or file paths appear in
the lifted copy, and the two scoped exceptions Ry ruled in (D-010) — the AI account's
display name **Main**, and his verbatim icon-color rationales — are both already
public on that page. Only the first is carried into this post.
