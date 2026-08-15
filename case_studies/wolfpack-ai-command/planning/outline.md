# Wolfpack AI Command — case study outline

Official name: **Wolfpack AI Command** (Ry's ruling, 2026-08-13, renaming the earlier
working title *Notion AI Command*). In copy the name is **rationed, not used
throughout** — see D-011. Genre: **not a how-to.** The story of why the system had to exist and the approach
Ry took to building it — by running the system on itself, refining continuously, over a
foundation of 20 years of coding, GitHub, and project management.

**Audiences, in order:** hiring companies lead the framing; potential buyers of the
system and potential project clients read along. Like the portfolio hero, the copy should
mostly address *the work itself* — a well-governed AI operating system reads as
capability evidence to a boss, as a product to a buyer, and as process assurance to a
client without being re-aimed at any one of them. Where a sentence must pick a reader, it
picks the company leader deciding who runs their projects.

**Org breadth (D-012):** the piece speaks to SMBs, startups, and solopreneur developers
alike — never startup-specific. "Company leader" spans an SMB director, a founder, and
the solo developer who is their own PM; pain points and examples draw from all three
scales. **PM stance (D-013):** the system **empowers project managers, it does not
replace them** — a working PM should read this piece and want it. Copy must never imply
the role's elimination or a headcount saving.

**The three carried themes** (every part should advance at least one):

1. **Business and customer data security & confidentiality**
2. **AI supervision and transparency**
3. **User-friendly, intuitive setup with flexibility throughout**

---

## The argument (spine of the piece)

Everyone agrees the Project Manager role makes or breaks work at every scale — and
everyone agrees it is a deadline-laden job that is brutally hard to do well and highly
prone to burnout. The reason is a structural split: **most of the job is tedium**
(status-chasing, ticket hygiene, cross-linking, version bookkeeping, writing down what
happened), while **the part that requires talent** — relationships, scheduling
clairvoyance, confident vertical communication, wide technical knowledge — is the part
that actually pushes projects from okay to excellent and through to completion. Because
excellence demands both halves, organizations at every scale under-resource the role:
startups omit it outright, SMBs hand it to someone as a side-duty, and the solo developer
carries it alone in the hours after the real work. The chaos that follows is measurable —
in Ry's own client history with startups, project completion rates run **below 50%** (the
figure keeps that specific attribution; the pattern it illustrates does not).

Wolfpack AI Command rips out the tangled cords of tedium. AI operators do the
record-keeping half — inside written, versioned guardrails, under an identity system that
makes every AI action attributable, inspectable, and reversible — so the human half of
the role gets its hours back for the part that needed a human all along. **This empowers
the role rather than replacing it:** where a dedicated PM exists, the system is theirs to
command, and the week it returns goes to the talent half that pushes projects to
excellent; where none exists, the role finally becomes feasible for a CTO, a
delivery-minded manager, or the solo developer to carry — and easy to share transparently
among silo leaders. The system was not designed on a whiteboard: it was
built by using it on itself, every rule earned from a real mistake, dated, and recorded.

---

## Part-by-part outline

### Part 1 — Hero
- Title: **not the product name** (D-011) — **resolved by D-019 (Ry, verbatim):**
  *An AI Operating Layer for Streamlining Project Delivery*. Ry's pick is descriptive
  rather than editorial, superseding the four editorial candidates drafted under this
  part. The name **Wolfpack AI Command** appears in the standfirst — its first rationed
  use, unchanged.
- Standfirst — **resolved by D-019 (Ry, verbatim):** the overlap/synchronization
  framing (hundreds of small facts, dependencies, decisions, and handoffs kept
  synchronized; developers stay on the product, PMs on orchestration; "Command and
  deliver projects faster, with more control and transparency than you thought
  possible.").
- No results claim, no client named. Stat tiles carry artifact/method facts only
  (see candidates below).

### Part 2 — The role everyone agrees on
- Open on the consensus: from small project to company initiative, PM quality decides
  outcomes — and the job burns people out. Write to the reader who has watched both
  happen (the company leader) — in a way the PM who has lived it recognizes as true.
  The burnout diagnosis is sympathy for the role, never an indictment of the people
  in it (D-013).
- Establish the stakes without a villain: this is a structural problem, not a talent
  shortage.

### Part 3 — Two jobs in one title
- The split, made concrete. Tedium: chasing statuses, keeping tickets honest, linking
  work to plans, writing the record, versioning, release notes, remembering what was
  decided. Talent: relationships, scheduling clairvoyance, confident vertical
  communication, wide technical knowledge.
- Key line to earn: the tedium is *most* of the job, but none of the reason you hire
  a great PM — and none of the reason anyone becomes one. The split must read as *the
  PM's own complaint, finally taken seriously*, not as an outsider's case against the
  role (D-013).
- **Figure candidate F1** (the split, two columns).

### Part 4 — What organizations do about it, and what it costs
- The under-resourcing pattern, drawn at every scale (D-012): startups omit the role
  outright; SMBs hand it to someone as a side-duty done at 10% attention; the
  solopreneur developer is their own PM in the hours after the real work.
- The consequence: project chaos — duplicated work, silent stalls, decisions lost in
  chat threads, "done" that means five different things.
- **The <50% completion figure lands here**, attributed plainly and only to Ry's own
  client history with startups — the attribution stays that narrow because that is the
  measured population. No external citation implied; phrasing must make the provenance
  self-evident (site rule: fact provenance). The surrounding copy draws the pattern at
  every scale, so the figure reads as the sharpest end of a general problem, not as
  the section being startup-only.

### Part 5 — The idea: a command center, not an assistant
- The design bet: don't bolt an AI chat onto the chaos — build an operating system where
  the system of record (Notion), the system of work (GitHub), and AI operators (Claude
  as the working agent; a second vendor's model as independent reviewer; Python where
  code is the right tool) are bound by **written, versioned rules the AI itself is
  governed by**.
- Name the inversion: most AI adoption asks "what can the AI do?" This system asks
  "what is the AI *allowed* to do, who can tell what it did, and how would we know if
  it went wrong?" — the questions a company leader actually has.
- Introduce "Wolfpack AI Command" as the name for the whole: workspace governance + code
  governance + agents + skills, one source of truth with thin pointers on every surface.
  This is the name's formal christening moment — the second of its ~three rationed uses
  (D-011); after this, running copy returns to common nouns.

### Part 6 — The system in three layers
Capability tour, one subsection per layer, drawn from the three briefs. Depth budget:
enough to be credible, never tutorial.
- **The workspace layer**: four databases; template-first creation (the correct shape is
  the default shape); uniform icons with meaning pushed to a governed color system;
  nothing exists unlinked; ~44 numbered rules published as one canonical rulebook that
  humans and every AI surface read; a drift validator that checks the rulebook's
  duplicated surfaces against each other.
  - **Icon placeholders where the visual system is discussed** (D-015): wherever the
    copy talks about the icon/color system — one icon per database, meaning carried by
    a governed color legend — the page carries **placeholder icon chips** for visual
    interest (precedent: the ai-coaching reviews section's dashed placeholder cards,
    with an HTML comment naming what fills them). ⚠️ Open sub-question for Ry: the
    case-study sheet introduces **no hues beyond the navy system and the neutral
    figure ground**, and the database icon colors are four hues — so the placeholders
    ship neutral (navy/ground) unless Ry rules the semantic colors in as *figure
    content* rather than page accent.
- **The code layer**: repository resolution before any action ("resolve, never guess");
  two-profile branching with audited carve-outs; a verification queue that separates
  *merged* from *accepted*; versioning where a round triggers the bump and the owner
  confirms every one; releases with the review gate on the outside.
- **The agent layer**: eight AI skills that carry the rules into every session, and the
  deliberately small Python scaffold where the primitives were proven — five tools, none
  destructive, two-model cost routing, per-turn cost telemetry. **Positioning per
  D-005: the scaffold is the teaching/proving layer, deliberately frozen once its ideas
  graduated into governance — never described as a production engine.**
- **Figure candidate F2** (three-layer architecture).

### Part 7 — Theme: supervision and transparency ("How do you know what it did?")
The strongest material in the system; give it the longest theme treatment.
- The AI has **its own identity** in the system of record — every page, edit, and
  comment it makes carries its own name in the platform's audit fields. Include the
  origin scar: before the split, AI and human work were permanently indistinguishable,
  and that history can never be sorted out. The rule exists because the gap is real.
- **Three provenance questions, three separate answers**: who created it, who completed
  it, who owns it — and the AI is forbidden to write the human-only channels, which is
  precisely what keeps them meaningful.
- **A silent status flip is an incomplete transition**: every AI status change carries a
  timestamped comment; the stalled case is called out as the one the human most needs
  explained.
- **Anti-theater rules**: completion is an objective checkbox test, not a feeling;
  backfilled statuses are forbidden ("a live status no one could have observed is
  theater").
- **Merged is not accepted**: AI work flows fast into integration but sits in a visible
  human verification queue; nothing closes without the human.
- **Auditable from either surface, because the surfaces are interconnected** (D-014): a
  task in the workspace links its issue and PR; the code side carries the same trail
  back. Start from the project record or start from the diff — either way you arrive at
  who did what, when, and why. Auditing AI work never requires knowing which system to
  ask first, and a company leader can audit a *project* in the workspace with the same
  ease a developer audits *code* in the repo.
- **Reverting is a prompt away** (D-014 — key line to earn): the gates (review, the
  verification queue, automated checks) are built to stop the system's own mistakes
  before they ship — but at a real volume of code and updates, the occasional revert is
  inevitable, and the system treats it as routine rather than exceptional. Because every
  AI change is small, attributed, linked across both surfaces, and versioned, tracing,
  correcting, or reverting one is a single instruction to the operator, not an
  archaeology project. Phrase as design/method ("built so that"), never as a measured
  error rate (evidence rules).
- **Cross-model review**: a different vendor's model audits the rules and the skills;
  implementers don't sign off on themselves. Findings, reconciliations, and even waived
  gates are recorded.
- **Figure candidates F3** (provenance table) **and F4** (an illustrative work-session
  trail — status flip → timestamped comments → PR → verification queue; labeled
  illustrative inside the figure).

### Part 8 — Theme: security and confidentiality ("Whose data is it?")
- **Permission scope is the privacy boundary**: the AI sees only what is explicitly
  shared with its account — enforced by the platform, not by a promise in a prompt.
- **Secrets never touch code**: environment-file configuration through a single
  chokepoint, framed as the property that makes the system *deliverable* — handable to
  a client without leaking a credential.
- **Structurally bounded blast radius**: no destructive tools exist in the agent layer;
  the documented bar for adding one is a confirmation step in code, not in the prompt.
- **Identity verification before writing**, and the hard stop on any mismatch — plus the
  silent re-auth hazard it defends against.
- **Destructive changes require named snapshots**; automated checks run credential-free
  and offline by design; what leaves the machine is enumerated, including the honest
  item (workspace content queried by the agent enters model context — stated, not
  hidden).
- **Sandbox-first sequencing** for anything near client data.

### Part 9 — Theme: intuitive setup, flexibility throughout ("Could your team run this?")
- Templates make the correct shape the default; skills make the conventions
  self-applying; the rulebook is written to be read by people and loaded by AIs.
- **Thin pointers, one source of truth** — the explicit anti-drift architecture across
  every surface (coding sessions, desktop, web, mobile, the workspace's own AI).
- **Replication is configuration, not code**: a new client is a new config file and new
  database IDs.
- **Ceremony scales to the work**: two branching profiles, audited carve-outs, rules
  relaxed on evidence (with the compensating transparency requirement when a gate
  loosens).
- Setup guides with the reason attached to every step; error messages that teach.

### Part 10 — How it was built: the system built itself
The approach story; the narrative lives here (timeline per D-007: the practice started
**November 2025**; the versioned repos, from July 2026, formalized it — dated from the
practice, on the 20-year foundation).
- The method: Ry demonstrates a convention live; the AI records it; the observation
  becomes a rule; the rule becomes a skill; a validator guards the copies. Ask before
  assuming.
- **Mistakes became rules, and the dates survive**: the folder-name guess that founded
  the code layer's first rule; the lost skills that mandated pointers-not-copies; the
  silently-stale second machine; the backfilled status the owner caught; the
  priority-default purge; the "AI done means pending review" misread corrected in one
  recorded word — *wrong*.
- **The system audits itself**: a second vendor's review caught the SOP drifting against
  its own copies; the response was an automated contract check with a stated philosophy
  ("a check that cries wolf gets deleted").
- The 20-year foundation frames *why the rules are the right rules*: they encode two
  decades of what actually goes wrong in real projects, not a vendor's best-practice
  list.
- **Figure candidate F5** (dated mistake→rule timeline).

### Part 11 — What this changes for the org, and close
- The role, re-divided — in two postures (D-013). Where a dedicated PM exists, the
  system is **their command center**: the record-keeping half runs under their
  supervision, and the week it returns goes to relationships, foresight, and the
  vertical communication that makes projects excellent. Where none exists, the role
  becomes feasible for a CTO, a delivery-minded manager, or a solo developer to
  carry — and because every action is attributed and narrated, it can be **shared
  transparently across silo leaders** instead of living in one exhausted person's head.
- What the reader should take away, by audience: a boss reads *this person builds
  systems that make teams legible*; a buyer reads *this exists and is transferable*; a
  client reads *this is how my project would be run*; a working PM reads *this takes
  the half of my job I never wanted and hands me back the half I'm best at*.
- **Close with a brief product plug, then the CTA (D-016, resolving D-008).** A short
  block in the territory of: *"Want the Wolfpack AI Command system for your
  organization? Integration takes hours, not days — mostly installing dependencies,
  AI configuration, and prompting Claude. The upgraded Notion system can be developed
  safely in parallel, in isolation from your existing Notion (or other) PM system."*
  Then the standard book-first CTA: the 30-minute intro call, one destination.
  - The plug is the name's **third rationed use** (D-011).
  - It stays **brief** — a short paragraph, not a section of chrome.
  - The isolation sentence deliberately echoes theme 1 (safety) and theme 3 (setup
    ease); "(or other)" keeps the door open for orgs not on Notion (D-012 breadth).
  - "Hours, not days" is **the offer's claim, voiced as the offer** — never dressed as
    a measured result (evidence rules).

---

## Evidence rules (Ry's ruling, 2026-08-13)

- **Allowed:** the <50% startup completion figure, attributed plainly to Ry's own client
  history; **real artifact counts** pulled from the repos and workspace at write time;
  the 20-years background claim.
- **Not allowed:** a results section (not granted); invented outcomes; client names or
  invented testimonials; implied external sources for the completion figure.
- Counts must be re-measured at write time, not copied from these planning docs.

### Stat-tile candidates (artifact/method facts only, per the folder rule)
- **8** AI skills carrying the rules into every session
- **~44** numbered rules in the published workspace rulebook
- **2** SOP layers, each versioned and released like software
- **5** automated drift checks guarding the rulebook's copies
- **0** destructive tools exposed to the agent (by design)
- **1** dedicated AI identity — every AI action attributable
- (Alternates: SOP doc counts, review findings → corrections, commit spans)

---

## Figures (all built to the shared case-study sheet; illustrative labels in-figure)

| # | Figure | Notes |
|---|---|---|
| F1 | The split: tedium vs talent | Two-column; the piece's thesis in one image |
| F2 | Three-layer architecture | Rules → skills → sessions; Notion ↔ GitHub ↔ AI operators; thin pointers to one source of truth |
| F3 | Provenance table | Who created / who completed / who owns — and which channels the AI may not write |
| F4 | A supervised work session | Illustrative timeline: status flip → timestamped comments → PR → verification queue; optionally end on a caught-and-reverted step to show D-014's "a prompt away" visually |
| F5 | Mistakes → rules | Dated; the built-with-itself story in one image |
| F6 | Database icon chips | Not a full figure — inline placeholder chips beside the workspace-layer copy (D-015); ships as placeholders, colors pending the no-new-hues sub-question |

Likely cuts if the piece runs long: F4 or F5 (keep at least one of the two). F6 is not
cuttable the same way — it is a copy-adjacent visual, not a standalone figure.

---

## Site conventions checklist (from `case_studies/` + repo CLAUDE.md)

- Shared stylesheet only (`case-study-assets/css/case-study.css`); anything new goes
  into the shared sheet; `reveal.js` byte-identical; coral ration is the sheet's six
  uses, count never moves silently.
- Public and indexed (pending D-009); **never links the hire pages**; Open Graph block
  in `<head>` + registration in the social-card guard when built.
- Folder name is not the URL: deploys by copying to the intake repo root under a slug
  (working slug: `wolfpack-ai-command`); `planning/` never deploys.
- No client named; illustrative figures labeled inside the figure; check any real
  screenshot's pixels at 5–6x before committing (workspace screenshots would carry
  client/project names — treat like the financial-model hero's blur).
- Copy judged by Ry against the existing case studies' voice; no rulebook.
- Verify at phone width via the 390px iframe method.
- Word-count target: **~3,000–4,500 words** proposed (between the financial-model piece
  and the M&A report) — Ry to confirm.

---

## Decisions ledger

| # | Decision | Who / status |
|---|---|---|
| D-001 | Bosses (hiring companies) lead the framing; buyers and clients read along | Ry, 2026-08-13 |
| D-002 | Exposure: capabilities, not internals — no private repo names, code specifics, or internal doc structure in committed/published text | Ry, 2026-08-13 |
| D-003 | Name: *Notion AI Command*, used consistently — **superseded by D-011** (renamed, and "used consistently" reversed in favor of rationing) | Ry, 2026-08-13; superseded 2026-08-13 |
| D-004 | Evidence: <50% figure (own client history), real artifact counts, 20-year background; **no results section** | Ry, 2026-08-13 |
| D-005 | The Python scaffold is presented as the proving/teaching layer, deliberately frozen — never as a production engine (the artifact cannot support that claim) | Claude, 2026-08-13 — **confirmed by Ry, 2026-08-13** |
| D-006 | "Codex" appears in the story as the **independent cross-model reviewer** (the role it actually plays), not as a runtime operator | Claude, 2026-08-13 — **confirmed by Ry, 2026-08-13** |
| D-007 | **Timeline — resolved: count from the practice.** Ry started work on the system in **November 2025**; the piece dates it from then and says explicitly that the repos (whose measurable history begins early July 2026) formalized an already-running practice — "in practice since November 2025, formalized into versioned, released rules from July 2026" territory | Ry, 2026-08-13 |
| D-008 | **Destination — resolved by D-016:** standard book-first close, one destination, the 30-minute intro call, preceded by a brief product plug. The general citation-link policy for case studies (see the M&A study's open ruling) remains open but is unlikely to bite here — this piece cites its own artifacts, not external sources | Ry, 2026-08-13 |
| D-009 | **Indexing — assumed in force.** Public + indexed per `case_studies/` convention; stated as the build assumption 2026-08-13 and not objected to. Confirm with Ry before deploy | Assumed; confirm pre-deploy |
| D-010 | **Named specifics — resolved: name both.** The AI account's display name and Ry's verbatim icon-color rationales may appear on the page — a scoped exception to D-002; everything else stays sanitized | Ry, 2026-08-13 |
| D-011 | Official client-facing name: **Wolfpack AI Command** (supersedes D-003). In the case study the name is **rationed, not repeated**, to keep the piece editorial rather than salesy: **(a)** ~three uses total — the hero standfirst/subtitle, the Part 5 introduction, optionally the close — with running copy using common nouns (*the system*, *the command center*, *the operating layer*) and generic descriptors (*the command system*, *the governance layer*) everywhere else; **(b)** the piece carries an **editorial, argument-led title** (like the other two case studies), with the product name in the standfirst/subtitle, exact title Ry's pick (resolved by D-019); **(c)** the full branded name lives natively where names belong — the `<title>` tag, the Open Graph card, and off-page product/sales surfaces. Folder renamed `notion-ai-command` → `wolfpack-ai-command`; working slug likewise | Ry, 2026-08-13 |
| D-012 | **Audience breadth:** the piece speaks to SMBs, startups, and solopreneur developers alike — never startup-specific. The <50% figure keeps its startups-only attribution (that is the measured population), but the under-resourcing pattern around it is drawn at every scale | Ry, 2026-08-13 |
| D-013 | **PM stance:** the system **empowers project managers, it does not replace them** — a working PM should read the piece and want it. Where a PM exists, they command the system and reclaim the talent half of the role; where none exists, the role becomes carryable. Copy must never imply role elimination or a headcount saving, and the burnout/tedium diagnosis always reads as sympathy for the role, not a case against it | Ry, 2026-08-13 |
| D-014 | **Content requirement — two-surface auditability and easy reverts.** The piece must show that AI work is easy to audit from *either* GitHub or Notion — the two are interconnected, so tracing, correcting, or reverting starts from whichever surface the reader lives in (a leader auditing a project, a developer auditing code). And it must carry the revert story honestly: the gates are built to stop the system's own mistakes before they ship, but at high volume of code and updates the occasional revert is inevitable — and the system makes a revert **"a prompt away."** Phrased as design/method, never as a measured error rate | Ry, 2026-08-13 |
| D-015 | **Icon placeholders for visual interest.** Wherever the page discusses the system's visual aspects (per-database icons, the governed color legend), it carries placeholder icon chips (precedent: ai-coaching's dashed placeholder cards + explanatory HTML comment). **Open sub-question:** the shared case-study sheet allows no hues beyond the navy system and the neutral figure ground, and the icon system's meaning *is* four hues (blue/orange/green/brown) — placeholders ship neutral unless Ry rules the semantic colors in as figure content | Ry, 2026-08-13; color sub-question needs Ry |
| D-016 | **Closing product plug.** The case study ends on a brief product plug — territory: *"Want the Wolfpack AI Command system for your organization? Integration takes hours, not days — mostly installing dependencies, AI configuration, and prompting Claude. The upgraded Notion system can be developed safely in parallel, in isolation from your existing Notion (or other) PM system."* — followed by the 30-minute intro-call CTA (one destination, book-first). The plug consumes the name's third rationed use (D-011); "hours, not days" is voiced as the offer, not a measured result; and the plug is a deliberate choice for this buyers-audience piece, not a precedent the other case studies inherit | Ry, 2026-08-13 |
| D-017 | **Nav CTA stays; "no CTA until the very end" governs the body.** The standard nav CTA button remains (site chrome, consistent with the sibling case studies); the body carries no CTA, calendar link, or funnel ask before the closing plug (D-016). Two calendar links on the page total, like the siblings | Ry, 2026-08-13 |
| D-018 | **Notion representation:** the case study gets an entry in the **Wolfpack Content DB** (the pattern the two existing case-study pages set), plus a project and numbered publishing tasks in the standard Projects/Tasks databases, PM-tracked with live statuses. No new Product page for Wolfpack AI Command (not ruled in) | Ry, 2026-08-13 |
| D-020 | **Tone iteration (2026-08-15).** Ry pointed at the `rml-dj-beginner` gear-guide article as the reference for how he actually sounds, and made a manual edit pass on this page (blunt bolded openers — *"Chaos."*, *"Extremely boring."* — TPS Report, calling an audible, direct reader address). Claude captured the direction as non-binding tone notes in `case_studies/README.md` §Voice and rewrote the page's remaining copy toward it, cutting ~9% of visible words (running copy >10%; the tables, tiles, and figure placeholders are fixed). **Consequence of Ry's pass:** he cut the <50% completion figure from §03, so the "honest limit of that number" aside and the .tm sentence attributing the figure were removed with it — they referenced a number no longer on the page. Flag for Ry: confirm the aside's removal; restoring the figure would mean restoring both | Ry (direction + edit pass); Claude (application), 2026-08-15 |
| D-019 | **Title and standfirst — resolved with Ry's verbatim copy**, closing the open title pick in D-011(b) and superseding the four editorial candidates (preserved in git history, PR #177's version). h1: *An AI Operating Layer for Streamlining Project Delivery*; standfirst: Ry's supplied paragraph — overlapping teams/projects, hundreds of small facts kept synchronized, developers on the product and PMs on orchestration, closing on *"Command and deliver projects faster, with more control and transparency than you thought possible."* Applied together with Ry's ROI iteration of the page copy (issue #178), which rewrote the closing section as *"What does this buy me?"*, added developer-context and conflict-handling material to the code layer, and reframed the honesty note as mechanism-not-percentage. `<title>`, og:title and og:image:alt reconciled in the same edit; the standfirst keeps the name's first rationed use, so the body count stays three. Neither the h1 nor the standfirst may be reworded without Ry — they are supplied copy, not drafted copy. **Standfirst since revised by Ry himself** in the 2026-08-15 edit pass (D-020): opens *"Project management can be brutal."*, bolds *product*/*delivery*, closes *"Command and complete AI-accelerated projects faster, tighter, with more control than you thought possible."* The page is the ruling copy; the h1 is unchanged | Ry, 2026-08-13; standfirst revised 2026-08-15 |

## System findings surfaced during research (not case-study content — for Ry)

1. **The live workspace rulebook page has drifted ahead of its repo mirror.** The page
   was edited weeks after the repo's last commit; at least two rules differ from the
   mirror, and one rule ID is referenced on the page but defined nowhere — exactly the
   dangling-reference class the contract validator exists to catch (it only runs against
   the repo's own copies). Either newer repo work exists that the local clone hasn't
   pulled, or the page was hand-edited against the one-way-publish rule. Worth
   resolving before the case study cites the rulebook's numbers.
2. **The Python scaffold's schema predates the workspace SOP** and would need its
   property strings updated before running against the current workspace — disclosed in
   its own docs, but relevant if a demo or screenshot is ever wanted.
3. **The case study ships "54 numbered rules", and that number is the repo-mirror
   count, measured 2026-08-13.** The stat tile, the §05 body and the readout all carry
   54 (up from the "~44" in these planning docs, which was a stale estimate). Reconciling
   it against the live rulebook page — which finding 1 above says has drifted ahead of the
   mirror — is a **pre-deploy gate**, not a copy-editing task: if the live page holds a
   different count, the page is wrong the day it publishes. The page's `.tm` note already
   states that every count was taken from the system's own repositories, so no `.tm`
   change is needed either way; only the number itself would move.
4. Both findings are, honestly, *good case-study material* — the drift validator
   catching its own scope boundary is the "duplication drifts" thesis proving itself —
   but they're logged here as operational items first.
