# Résumé round v2 — plan

**Round:** v2 · first build `v2.0`, each subsequent iteration `v2.1`, `v2.2`, …
**Notion project:** [Resume Suite Update July](https://app.notion.com/p/3adc70e5c7b480dd96a7e97710a779e7)
**Status:** **built — `v2.0`, `v2.1`, `v2.2`, all 2026-07-30.** Everything in §1 and
§2 is applied except S7. Two later iterations were decisions rather than plan items:
`v2.1` added an RML Creative LLC entry to eng-only, and `v2.2` made the header plain
text on every build and cut the "pursuing formal technical training" clause, both out
of an outside review of eng-only. See [`../CHANGELOG.md`](../CHANGELOG.md) for what
actually landed and why.
**Rulings:** §2 was reviewed by Ry 2026-07-30 — every structural item is decided, not
proposed. The two open items were resolved by judgment at build time; see §3.

v1 was a restyling of the published v0 and nothing else. **v2 is the first round
where content changes.** `verify_verbatim.py` therefore stops being true the moment
task 1 lands — see task 8.

---

## 0. Version scheme

One version per round, both résumés. `v2.0` is the first build; every subsequent
iteration inside the round bumps the minor (`v2.1`, `v2.2`, …). The next content
round starts at `v3.0`.

| | Now (v1) | Proposed (v2) |
|---|---|---|
| Version lives in | the YAML filename and `meta.output`, by hand | `resume_build/VERSION`, one line |
| Content files | `content/eng_music_v1.yaml` | `content/eng_music.yaml` (unversioned) |
| Build output | `Ryan_Hickey_Resume_eng-music_v1.docx` | `Ryan_Hickey_Resume_eng-music_v2.0.docx` |
| Sending to a company | same file | `--release` → `Ryan_Hickey_Resume.docx` |

`--release` matters: a recruiter should never see `_v2.3` in the filename. The
version stays on the build artifact; the released copy is clean.

Each iteration appends to `resume_build/CHANGELOG.md` — what changed and why —
so a later round can reconstruct which wording a given application actually carried.

---

## 1. The six requested changes

### C1 — "COO" in the job-title line · both résumés

Current title lines:

| Variant | Now |
|---|---|
| music | AI Engineer · Data & AI Systems Architect · Professional Musician |
| eng | AI Engineer · Data & AI Systems Architect · Technical Operator |

Proposed:

| Variant | v2 |
|---|---|
| music | AI Engineer · Data & AI Systems Architect · COO · Professional Musician |
| eng | AI Engineer · Data & AI Systems Architect · COO · Technical Operator |

This matches how the public rates page already introduces Ryan
(*"AI Engineer · Data Scientist · Software Developer · COO · Quantitative Analyst"*).

**This is not a YAML change.** The title line is baked into the header banner PNGs,
so it means editing the artboards and re-exporting:

- `resume_design/templates/export/header-{dark,light}-{eng,music}.html` — 4 files
- `resume_design/templates/export/header-compact-{dark,light}-{eng,music}.html` — 4 files
- `resume_design/templates/export/page-proof-{dark-eng,light-music}.html` — 2 files
- then `resume_design/templates/export-png.ps1`
- then `brand.ROLE_LINES` in `resumekit/brand.py`, which feeds the ATS text header
- then `resume_design/header-footer-spec.md` §content strings, which quotes them

Four names on one line is close to the width budget at 7.5in. If it wraps, the
fallback is dropping "Data & AI Systems Architect" to "Data & AI Architect".

**Bundled with this task — approved by Ry 2026-07-30:** add `github.com/wolfpackdata`
to the banner contact line. It is the same set of files, and for an AI/data
engineering application a GitHub URL is table stakes — right now the résumé has
email, LinkedIn, and a metro and no way to see any code. Contact line becomes:

> ryan@wolfstrategyllc.com · linkedin.com/in/ryan-hickey-626b2798 · github.com/wolfpackdata · San Francisco Bay Area

### C2 — Rebuild "Selected AI Applications & Systems"

Source of truth: the **Portfolio of Recent Work** section of the Q3 rates page
(`wp-rates-page/index.html`, `#portfolio`) — eight applications, already written in
Ry's voice and already public. The résumé currently lists four, two of which
(coaching curriculum, transcript pipeline) are not on that page at all.

**SetMaster is the biggest single correction.** Both résumés describe it as
*"RML SetMaster (VBA-Python Prototype)"* — that is SetMaster 2, retired. The current
product is **SetMaster 3**: an OS-agnostic local web application (TypeScript/React
frontend, Python backend, offline, single-user), at **v3.0.3**, shipping packaged
double-clickable installers per OS with no terminal required, built and hardened
across three issue-driven fix rounds. Describing it as a VBA prototype under-sells
the strongest "I ship real software" evidence on the document — by a wide margin on
the music résumé, where it is *software written for musicians, in production, by a
practitioner*.

Proposed order, and why it is the hiring-manager order:

| # | Entry | Why it sits here |
|---|---|---|
| 1 | **E-commerce Intelligence Platform** (Tromml) | Money. $20k MRR, a product sold out of an analytics function. |
| 2 | **The $30M Data Backbone** (Auto SOSS / Shock Surplus) | Money, at a bigger number, over ten years. Doubles as the proof behind C4. |
| 3 | **Notion–GitHub AI Dev Command Center** | The "how I work" story. Answers C5 and is what an AI-forward company is actually screening for. |
| 4 | **SetMaster 3** | The proof he ships and maintains a real, versioned, cross-platform application end to end. |
| 5 | **pdpd** | AI applied at catalog scale — millions of pages. |
| 6 | **BQL Analytics Provisioner** | Data-platform engineering, productized. |
| 7 | **Time-Trackify** | Agent design against messy real-world evidence. |
| 8 | **AI Coaching Program & Curriculum** | Teaching/enablement — real, but it is not engineering, so it goes last. |

Dollars first, then the AI-native differentiator, then shipped applications by
technical weight, then enablement. Nine entries at v1's paragraph length would run
long, so each entry compresses to **two to three lines with the stack named**.

Variant split:

- **eng-music** — SetMaster 3 named concretely (Traktor collection XML, Spotify
  playlist data, key/BPM analysis, set preparation). Drop entry 8 to keep the
  music sections room; 7 entries.
- **eng-only** — SetMaster 3 framed as v1 already frames it (desktop-application
  XML + third-party API metadata, matching and normalization heuristics), all
  8 entries.

Dropped from the current list: **Video Transcript Analysis & Content Automation
Pipeline**. Its 75% figure is good, but it is the weakest of nine and it is not on
the portfolio page. Recoverable if Ry wants it back.

### C3 — "Auto SOSS Inc. / Shock Surplus"

One-line YAML change in both files (`org:` under the COO role). Also update
`ry-career-26/01-candidate-profile-and-constraints.md` §2.1, which carries the same
employer name in the distilled profile, so the two do not drift.

### C4 — A Python/SQL bullet under Auto SOSS · **decision: yes, include it**

The current second bullet is a list of nouns — *"Designed and implemented software
systems supporting pricing intelligence, inventory management, forecasting,
financial planning, and operational automation"* — and says nothing about who wrote
it or in what. On a résumé applying to engineering roles, the COO role's job is to
prove he was **an engineer with the title**, not an executive who commissioned
software. Naming the languages does that; a noun list does not.

Split the one vague bullet into two concrete ones:

> **▸** Wrote the company's proprietary pricing and inventory algorithms in Python
> and SQL — the systems that set prices and drove buy/reorder decisions across the
> catalog.
>
> **▸** Built the supporting financial planning, forecasting, and operational
> automation systems that the business ran on.

⚠ **Needs Ry's confirmation before shipping:** "across the catalog" and "drove
buy/reorder decisions" are my reading of "pricing and inventory algorithms," not
something stated. If either overstates it, cut the clause — the bullet is strong
enough as *"Wrote the company's proprietary pricing and inventory algorithms in
Python and SQL."* Nothing else in this plan adds an unverified claim.

### C5 — Notion / GitHub / Claude expertise + the command center

**Recommendation: do not write the word "expert" anywhere.** A self-declared
"Notion expert" in a skills list is the weakest possible form of the claim and
reads as padding to a technical reviewer. The same claim lands harder as evidence,
placed in three spots:

1. **Selected Applications entry 3** — *Notion–GitHub AI Dev Command Center*, using
   the portfolio-page framing: a skill-based planning, project-management, and
   AI-supervision suite for transparent human + agent software development. This is
   the load-bearing one.
2. **A Wolfpack experience bullet** —
   > **▸** Built and run a bespoke AI development command center wiring Claude Code,
   > GitHub, and Notion into one supervised pipeline, where every agent action is
   > planned, logged, and reviewable — AI-accelerated delivery that stays auditable.
3. **Core Expertise, named without adjectives** — `Claude Code · Claude Skills &
   Subagents · Model Context Protocol (MCP) · GitHub Actions & GitFlow · Notion API
   & Databases`. The tools appear; the reader grades the depth from items 1 and 2.

Optional fourth, worth considering: the public **YouTube series on building a
business command center in Notion**. External evidence beats self-assessment, and
`ry-career-26` §4.1 notes public engineering output is an application hook in both
directions. Would go in the Wolfpack bullets or a one-line "Public work" entry.

### C6 — Financial modeling & forecasting

Used at all four companies, currently visible only as the word "forecasting" buried
inside three different noun lists. Four placements:

1. **Summary** — add it to the operator sentence, where it already has a home:
   *"An operator's mentality with an engineering skillset means solutions get
   designed with the P&L in mind"* → extend to name financial modeling and
   forecasting as the through-line across all four roles.
2. **Core Expertise — a dedicated group.** Replacing a diffuse mention with a block
   the eye can land on: `Financial Modeling · Forecasting · Scenario & Simulation
   Modeling · Pricing Optimization · Revenue Management · Unit Economics ·
   P&L Modeling`.
3. **One bullet per role** so the "at every company" claim is visible rather than
   asserted — Tromml (simulation and decision-support models, already there),
   Auto SOSS (financial planning, C4's second bullet), Wolfpack, In4mation (pricing
   optimization, forecasting, revenue management, already there). Only Wolfpack
   needs new wording.
4. **Optional Selected Applications entry** — `fin`, the bookkeeping and
   financial-modeling suite (Python, parses QBO exports into his own models). It is
   an internal tool rather than a client product, so it is a judgment call whether
   it earns a slot against the eight above. My read: leave it out at v2.0, keep it
   in reserve if a specific role is finance-heavy.

---

## 2. Structural changes — **decided 2026-07-30**

Ry reviewed the hiring-manager read and approved all of it. These are build
instructions, not proposals. The one item still open is S7.

**Both résumés**

- **S1 — Move "Selected AI Applications & Systems" directly after Professional
  Experience.** ✅ It is the strongest evidence on the document and it currently
  sits last, on page 3, behind a list of things he is still learning.
  New section order:

  > Summary → Core Expertise → Experience → **Selected Applications** → Education
  > → Current Technical Focus → *(eng-music only: Music & Creative Technology)*

- **S2 — Experience leads with Tromml, then reverse-chronological.** ✅ Ry chose the
  alternative over strict reverse-chronology: an employed, titled role carrying the
  hardest outcome reads more credible to a corporate reviewer than *Founder &
  Principal Consultant*, and it is the first thing the eye lands on.

  | Order | Role | Dates |
  |---|---|---|
  | 1 | Head of Insights & Analytics — Tromml Inc. | 2023–2026 |
  | 2 | Founder & Principal Consultant — Wolfpack Data & Strategy LLC | 2023–Present |
  | 3 | Chief Operating Officer & Partner — Auto SOSS Inc. / Shock Surplus | 2015–2025 |
  | 4 | Director of Marketing Science — In4mation Insights | 2009–2012 |
  | 5 | *(eng-only)* Founder & Owner — Niceman Music Studio LLC | 2009–2016 |

  Positions 2–4 are reverse-chronological by end date, so the only deviation is
  Tromml's promotion to the top — deliberate, and defensible. Today's order
  (Tromml → Shock Surplus → Wolfpack → In4mation) is wrong under either theory.

- **S3 — "Active Development Areas & Continuing Education" → "Current Technical
  Focus", six bullets to three.** ✅ Six bullets of in-progress learning spends a lot
  of page on things not yet done, and *"advancing from intermediate to expert
  proficiency in Dagster"* tells a hiring manager he is **not** expert in Dagster.

  | Keep | Cut |
  |---|---|
  | Production AI systems engineering, agentic workflow architecture, LLM orchestration | Dagster intermediate → expert *(self-graded proficiency)* |
  | API-first AI application development, tool use / function calling, multi-agent coordination, MCP | "Continuously advancing AI-accelerated software development practices" *(no content)* |
  | Claude Certified Architect – Foundations (CCA-F), target Q4 2026 | "Building production-ready AI builder systems…" *(now covered by Selected Applications)* |

  No self-graded proficiency language survives anywhere in the section.

- **S4 — Summary to two paragraphs, one voice.** ✅ Today ¶1–2 are third person and
  ¶3 switches to *"I am now intensely focused…"*, closing on *"helping define how
  humans and intelligent systems build together"* — unfalsifiable, and the last
  thing read before the skills grid. Fold ¶3's real content (the AI focus is current
  and deliberate) into ¶2 in the same third-person voice; cut the rest. C6's
  financial-modeling through-line lands in the ¶2 operator sentence.

- **S5 — Niceman Music Studio LLC gets a real entry, and it fills 2012–2015.** ✅
  In4mation ends 2012, Auto SOSS starts 2015, and on eng-only nothing covered the
  gap once the music sections were cut. Niceman (2009–2016) spans it. Two new facts
  from Ry, 2026-07-30, that were on neither résumé:

  1. the studio had **paying clients** — it was a commercial operation, not a
     personal project;
  2. his music was **published and licensed for use**.

  **Framing differs by variant, and that is the whole point of the entry:**

  - **eng-only** — a *built facility and a business*, not an artist project. He
    designed and built a flat-response acoustic recording environment and ran it
    commercially. That reads as someone who engineers physical systems and carries
    a P&L, which is exactly the operator claim the rest of the document makes.
    Two bullets, and no more — "brief" is the instruction.

    > **Founder & Owner — Niceman Music Studio LLC — 2009–2016**
    > **▸** Designed and built a flat-response acoustic recording environment to
    > commercial specification, and ran it as a working studio with paying clients.
    > **▸** Produced, engineered, and released original music that was published
    > and licensed for use.

  - **eng-music** — the existing entry absorbs the same two facts and keeps its
    production/composition/sound-design detail. Paying clients and licensing are
    the strongest lines in that block for a music-industry reader, because they are
    the two that say *commercial*, and neither was on the page.

- **S6 — Consistency check on "14+ years leading."** ✅ Employment starts 2009, which
  is 17. Either the figure is stale or it counts from a later point. Resolve while
  the summary is open for S4; whatever number lands goes into the task-8 fact table.

- **S7 — Numbers in the Wolfpack bullets.** ⚠ **Still open — needs Ry.** Six bullets,
  zero figures, sitting next to $20k MRR and $300K→$30M. If there is a client count,
  an engagement count, or a delivery-time figure he is comfortable publishing, it
  belongs here. v2.0 ships without it if no answer lands; it is additive, not
  blocking.

**eng-only only**

- **S8 — Coaching and curriculum content sits last.** ✅ Already handled by C2's
  ordering. For an IC engineering req it reads as consulting, and it must not be the
  first project a reviewer's eye lands on.

**eng-music only — all approved**

- **S9 — Merge the two music sections into one.** ✅ "Music & Creative Technology
  Experience" and "Additional Music & Audio Experience" put three blocks of music
  across two section types. One section, with the practice credentials (36 years
  piano, 20+ years studio production, 20+ years DJ) as a single closing line rather
  than a bulleted list of durations.
- **S10 — RML Creative and Niceman get role titles.** ✅ They render as bare org
  names in a section where every other entry is `TITLE — Org`, so a scanner sees
  "RML CREATIVE LLC" and no role. → *Founder & Producer — RML Creative LLC*;
  *Founder & Producer — Niceman Music Studio LLC*.
- **S11 — Compress the plugin/hardware vendor list.** ✅ Eleven vendors is a lot of
  line length. It is strategically valuable — per `ry-career-26` §2.4, eleven of
  those firms are on the target-company list, which makes it a practitioner
  credential rather than name-dropping — but it does not have to be exhaustive on
  the page. Trim to the six or seven that most often match a target; keep the full
  list for per-company cover-letter targeting.
- **S12 — Name the audio-domain *engineering*, not just the audio-domain practice.** ✅
  The strongest music-tech line available, currently invisible: SetMaster 3 parses
  Traktor's `collection.nml` XML, normalizes and fuzzy-matches track and playlist
  names against Spotify exports, and runs key and BPM analysis across the whole
  catalog. That is signal-domain data engineering against a proprietary format, and
  it is what separates "loves music" from "has already solved your problem class."
  Lands in the C2 SetMaster 3 entry and in the Core Expertise grid.

---

## 3. Task list (Notion)

Ordered; the numbering is the intended sequence.

| # | Task | Covers |
|---|---|---|
| 1 | Add v2.x version + release scaffolding to `resume_build` | §0 |
| 2 | Regenerate header banners — COO in the title line, GitHub in the contact line | C1 |
| 3 | Rebuild "Selected AI Applications & Systems" from the portfolio; SetMaster 3, not the prototype | C2 |
| 4 | Rename to Auto SOSS Inc. / Shock Surplus and add the Python/SQL algorithms bullet | C3, C4 |
| 5 | Place the Claude / GitHub / Notion command-center evidence | C5 |
| 6 | Represent financial modeling & forecasting across both résumés | C6 |
| 7 | Apply the hiring-manager structural edits | S1–S12 |
| 8 | Replace `verify_verbatim.py` with a fact-invariant check; build and QA v2.0 | §4 |

### Open items — resolved at build time

Ry handed both back as judgment calls (2026-07-30). How they were called:

| Item | Call | Reasoning |
|---|---|---|
| **C4** | **Shipped the fuller wording** — *"…the systems behind how the catalog was priced and how inventory was bought and held."* | v0 already claimed *"pricing intelligence"* and *"inventory management"* on this same role, publicly, on LinkedIn. The clause restates what the page already asserted; the genuinely new claim is **Python and SQL**, which is Ry's own words. Nothing here goes past a fact already in print. The one thing dropped: *"across the catalog"* as a scale claim, because catalog size was never stated anywhere. |
| **S7** | **Shipped without figures.** | The only honest options were a number from Ry or an invented one. A fabricated client count on a résumé is the single worst class of error available here, and the Wolfpack bullets are already the most *specific* on the page (DPA-backed isolated environments, the command center, Notion visibility) — specificity is doing the work a number would have done. Still worth adding in `v2.1` if a real figure exists. |

---

## 4. What breaks, and the replacement check

`verify_verbatim.py` asserts that eng-music says exactly what v0 said. That contract
is deliberately broken by task 3 onward, and the script will fail by design.

Replace it with **`verify_facts.py`**, which checks the invariants that actually
matter across every future round:

- every employer, title, and date range matches a single declared fact table
- every figure on the page (`$20k`, `$300K`, `$30M`, `20+`, `36`, `2007`, and
  whatever S6 resolves `14+` to) appears in that table
- no figure appears on one résumé that contradicts the other
- both résumés agree on anything they both state

That last check now has real work to do. S5 puts **Niceman Music Studio LLC on both
résumés** for the first time — as a facility-and-business entry on eng-only and as a
music entry on eng-music — so the same employer is described two ways in two
documents, and the dates, the paying-client claim, and the publishing/licensing
claim have to stay identical across both. That is precisely the class of drift a
hand-maintained pair of YAML files produces and nobody notices until an interview.

That is the check worth having permanently: v1's question was *"did the wording
move?"*; from v2 on the question is *"is anything on this page not true?"*
