# SetMaster 3 — case study outline

**This is an outline, not a draft.** Ry's instruction in the transcript:
*"You're going to plan out the case study as an outline from this transcript.
You're not going to write the whole case study yet. We're going to iterate on an
outline first."* Nothing below is finished prose, and the beats are written to be
argued with, cut, and reordered.

- **Page:** `intake.wolfstrategyllc.com/setmaster3-case-study/` · `noindex, nofollow`
- **Audience:** people who might hire Ry. One audience, not two.
- **Target length:** 2,200–2,800 words of body copy across 11 sections.
- **Sources:** the 2026-07-31 transcript (T), the `wolfpackdata/setmaster3` repo
  (R). Every beat below is tagged. Claims that need Ry's ruling are tagged with
  their `04-claims-ledger.md` id.

---

## 1. The thesis, and what this page is arguing

A case study aimed at hiring managers has to argue something. This one argues:

> **A working professional identified a real friction in his own craft, solved it
> three times in three years at increasing levels of sophistication, and the third
> time shipped it as a specified, tested, packaged, publicly-downloadable
> application in twenty-five days.**

*(Revised round 2: "eight years" was a drafting placeholder and is retired —
the first version is 2023, per C-07. **Three years is the better story anyway.**
Eight years reads as slow accretion; three reads as deliberate escalation, and it
sets up the twenty-five days rather than dwarfing it.)*

The DJ story is the *setting*. The argument is about how Ry works: he specifies
before he builds, he ports battle-tested logic rather than rewriting it, he
verifies against real data, and he ships with honest limitations stated out loud.

**The anti-pattern to avoid, stated once so it can't erode:** this must not read
as *"I used AI to build an app fast."* That story is now unremarkable and reads
as credulous. The interesting story is the **discipline around** the speed — the
spec package that existed before a line was written, the golden-master test that
made a verbatim port provable, the fail-closed scanner that gates the public
mirror, the release engineering, and the fact that the repo says *macOS is
untested* instead of claiming support. Speed is a consequence in this narrative,
never the subject.

---

## 2. The narrative spine

Seven movements. The section list in §3 hangs off this.

| # | Movement | The turn |
|---|---|---|
| I | A professional's problem | The tedium is not the DJing — it's the searching |
| II | The spreadsheet (v1) | The two-column transition row: the one idea everything else grew from |
| III | SetMaster 2 (v2) | Data engineering arrives; the catalog becomes queryable |
| IV | The lightbulb | Spotify® listening vs. Traktor® ownership — the gap becomes a shopping list |
| V | The rebuild (v3) | Spec first, then an agent build, then four rounds of hardening |
| VI | What it does now | Two jobs, one of which stands entirely alone |
| VII | What it gives back, and what's next | Hours; a teaching tool; Rekordbox® someday |

---

## 3. Section-by-section

### S1 · Hero

**Purpose:** state the thesis and the outcome in the space above the fold.

- Kicker: `CASE STUDY · 2026`
- Title: **decided (Ry, round 4)** — *"SetMaster 3: From a Spreadsheet on a Plane
  to a Robust Application."* Retired alternatives in §10.
- Standfirst, ~45 words: **Ry's framing (round 4)** — data engineering meets DJ
  engineering; he needed a road-worthy set preparation tool, so he built one three
  times in three years, and the third is a specified, tested, offline web
  application any DJ can download.
- Four stat tiles, all sourced:
  `25 days spec → public release` · `74 issues across 4 build rounds` ·
  `867 automated tests` · `byte-identical pipeline port`
- One hero image: the Track-Playlist Matrix at full scale. See
  `03-assets-and-capture-list.md` A-01.

**Do not** put a download button here. This page's job is the argument; the
landing page owns conversion.

---

### S2 · The problem (movement I)

**Purpose:** make a non-DJ hiring manager feel the friction in 150 words.

Beats:

- Ry is a professional DJ with **~7,000 tracks in Traktor®, drawn from a personal
  music library many times that size**, plus DJ partners' catalogs on the same
  machine (T; C-01). That is the only catalog figure the page uses — it is
  checkable against the public repo, which is what a technical reader will do.
- Preparing a set in Traktor® or Rekordbox® alone was *"super slow"* (T).
- The tedium, named precisely — this is the sentence the whole page turns on:
  searching, filtering, and sorting a huge catalog, **and** cross-checking against
  recent and past sets so the same track doesn't get replayed too often. Ry:
  *"always being fresh… an important part of being a pro DJ."*
- Second friction: reconciling Spotify® playlists maintained on the go against
  what he actually owns in Traktor® (T).
- The modern twist, and the reason this problem got *worse* rather than better:
  streaming means you no longer need to own a track, but *"it is still about
  organizing those"* — a bigger library is more friction, not less (T).
- Closing beat: he's a data engineer. He kept seeing the automation.

**Tone check:** no "as a DJ, I've always been passionate about…". Open on the
friction, in the second sentence.

---

### S3 · The spreadsheet (movement II)

**Purpose:** establish that the core product insight is old, specific, and was
validated by years of professional use before any code existed.

Beats:

- First iteration: **2023**, in **Google Sheets**, chosen specifically for built-in
  cross-device backup; later Excel (T; C-07).
- **It was used in professional settings immediately** (Ry, 2026-07-31). Worth its
  own sentence: this was never a hobby project that later got serious. The first
  version went straight into paid work, which is why the domain logic in it
  survived two rewrites intact.
- **The one idea.** Traktor® and Rekordbox® read top-to-bottom, one track per row;
  comments there are hard to read and eat real estate. Ry wanted **one row = one
  transition**: the track you're coming *from* on the left, the track you're going
  *into* on the right (T).
- Why that matters, in his words: *"what you really need to focus on is the
  transition"* — the cue points, the volume cues, the tempo changes. *"The set
  list can just be a list of tracks… done and done."*
- **This is the single most important paragraph in the case study.** It is a
  product decision made from domain expertise, and everything in SetMaster 2 and 3
  is downstream of it. Give it room — a diagram, not just prose. See A-06.
- Why a spreadsheet and not an app: copy-paste, moving things around, whitespace
  between chunks, a freeform palette. Tracks move earlier and later as a set
  develops; you add and replace; you keep detailed notes so you remember where you
  left off, what you liked, and your cue points (T).
- Validation beat: he just used it. DJing constantly, building sets on planes.
  It became *"a multi-tab beast of a workbook"* (T).
- It grew a **performance view** — zoomed, more real estate, color-coded — for
  glancing at during long sets with rehearsed, complicated transitions (T).
  *Worth noting:* Perform Mode is explicitly deferred in SM3 (R,
  `00-overview.md` §6), so the v1 spreadsheet did something v3 currently does not.
  **Say so.** It's a small honesty that costs nothing and buys the whole page
  credibility.

---

### S4 · SetMaster 2 (movement III)

**Purpose:** the moment the tool stops being a spreadsheet and becomes software.

Beats:

- SM2 = the Excel workbook extended with a **VBA and Python backend** (T; R
  confirms — 13 VBA modules and a four-stage Python pipeline in
  `legacy/setmaster-2/`).
- It imported the Traktor® collection so the catalog could be filtered like data:
  multi-filters against key and BPM, fast switching, artist search (T).
- Used during set prep, never live (T) — a good detail, because it shows a clear
  sense of where a tool belongs.
- The payoff: minutes off the tedious part, repeatedly, every session.
- Positioning beat to plant here and pay off in S7: the catalog work is the
  *optional* half. The transition editor stood alone from day one.

---

### S5 · The lightbulb (movement IV)

**Purpose:** the story's turn. Short section, high energy.

Beats:

- A one-off workbook flow: take SM2's Python output, import exportify.net CSVs of
  his Spotify® playlists, and compare (T).
- Ry: *"that's really when the lightbulb got bright in my head."*
- What it produced: a fast path from *what I've been listening to and actually
  want* → *which of those I don't own* → buy them → they're in the next set (T).
- The outcome claim: **hours saved every month** (T).
- **The Lexicon beat.** Ry insisted on it: Lexicon has a comparison tool, it's
  *"really powerful,"* it didn't handle the bulk list filtering he wanted, and
  SetMaster *"isn't supposed to compete with it… it's just another functional
  application of filtering metadata."* Keep this generous and keep it in — see
  C-04 and §9.

---

### S6 · The rebuild (movement V) — the section hiring managers read closest

**Purpose:** show the engineering practice. This is where the page earns its keep,
and it is the section most at risk of turning into an AI-hype paragraph.

Beats, in order:

1. **Why rebuild at all.** Building apps with Claude, starting in early 2025,
   reframed it as a web app (Ry, round 4 — supersedes the transcript's *cloud
   architect*). The blocking defect was structural: the prototype's Traktor®
   connection was **Windows-only**, and *"the OS split must not survive"* (R,
   `00-overview.md` §3).
2. **Spec before code.** Ry gave Claude the prototype and all the VBA and they
   worked on planning documents *"for several days"* (T). The result (R): a
   complete spec package — overview, data model, UI spec, ten feature specs, an
   open-questions log closed to zero, and a pre-handoff review. The repo's own
   `CLAUDE.md` says it plainly: *"The spec is complete and decided; if you are the
   build agent, your job is to implement it, not re-litigate it."*
   **This is the best single artifact on the page for a hiring manager.**
3. **Port, don't rewrite.** SM2's matching and normalization heuristics — track
   name cleaning, playlist-name and filename normalization, key mapping — are
   *"years of accumulated fixes"* and were ported **verbatim**, by rule.
   Restructuring stages was allowed; changing matching behavior was not (R).
4. **How that was made provable: golden-master tests.** The ported pipeline is
   byte-identical to SM2's engine on real data — pandas pinned, CSV round-trips
   preserved between stages specifically to preserve output bytes (R,
   `build-notes/final-report.md` D-006/D-011). This is the technical beat with the
   highest signal-to-length ratio on the entire page. **Do not cut it.**
5. **Hard constraints as design.** `collection.nml` is opened **strictly
   read-only** and never written — restated in UI copy, checked by sha256
   integrity snapshots. Fully offline: local backend, browser UI on localhost, no
   cloud, no telemetry, no external API calls. Single user, no auth (R).
6. **The build, and the rounds.** Build #1 tagged `v3.0.0-build1` (R). Then
   **three hardening rounds — 74 issues** (26 / 12 / 36) against a real backlog —
   one issue, one branch, one PR, and the issue left **open** until Ry verifies it
   against his own data (R; C-02). That last rule is worth a clause: merging does
   not close anything here, because the person who has to live with the tool is
   the one who decides it works.
7. **Verified against real work, not fixtures.** Ry was out DJing and testing the
   web app in live situations while the rounds ran (T). The acceptance criteria
   were demonstrated end-to-end against his actual collection and his actual
   workbook (R). Concrete: real `collection.nml` → 6,810 tracks × 149 playlists;
   the signature digging workflow returned 111 rows in one pass; a blank-cell note
   survived a re-import and re-run.
8. **Packaged for people without a terminal.** Self-contained per-OS release
   payload with a bundled CPython and locked dependencies; a double-click
   launcher; no Python, no Node, no terminal (R). Then the detail that sells it:
   a virtualenv is *not* a portable runtime, so the payload ships a relocatable
   python-build-standalone CPython — and the smoke check **fails the artifact** if
   a developer `.venv` ever appears in it.
9. **Publishing safely.** The private repo contains Ry's entire real Traktor®
   library. The public repo is a **generated mirror** with no history at all —
   because a history-rewrite is *"one mistake away from a permanent,
   unrecoverable leak"* and a tree with no history has no leak surface. Two
   independent defenses: an allowlist that fails closed, and a separate scanner
   that gates the **generated output** rather than the source, deliberately not
   sharing the allowlist's logic. Any finding aborts the build and deletes the
   tree — no warn-and-continue. It has already caught a real leak (R).
   **This beat is the strongest engineering-judgment story in the repo** and
   almost nobody writing a portfolio case study would think to include it.
10. **Honest limitations, shipped.** The v3.0.3 changelog leads with a platform
    verification note stating Windows is verified end to end and **macOS is
    untested**, with a named checklist that would earn the claim (R). Ending the
    engineering section on a stated limitation is the most persuasive move
    available here.

**Where "built with Claude" belongs.** Woven through beats 2, 6, and 9 as *how the
work was executed*, never as its own section and never as the headline. The
orchestration detail ships as a **sidebar** (C-06, resolved yes) — spec in §S11,
which is written to be the most impressive 120 words on the page.

---

### S7 · What it does now (movement VI)

**Purpose:** the product, briefly. The landing page carries the full feature
story; this section only needs to make the outcomes legible.

Beats:

- **Two jobs.** (1) Set preparation — a structured editor for writing a set as
  transition rows: track order, hot cues, EQ and level moves, timing, mix notes.
  (2) Catalog analysis — read Traktor® read-only, cross-reference against Spotify®
  playlists exported via Exportify, find *owned but not organized* and *on Spotify
  but not owned*, and run compound filters Traktor® itself cannot.
- **The positioning sentence, quoted from the repo because it is load-bearing:**
  job 1 does not depend on job 2. SetMaster 3 is fully useful with **no collection
  ever loaded**. *"Never present Traktor as a prerequisite."*
- Named features that carry Ry's voice (T): your own customizable emoji palette,
  your own workflow, *"the best mix timer so you know how long sections are and
  how long your whole mix is,"* and the framing that matters most —
  **it becomes your source of truth**, so you stop fighting Traktor® or Rekordbox®
  filtering.
- Two or three screenshots, not eight. See A-02/A-03/A-04.

---

### S8 · What it gives back (movement VII, first half)

**Purpose:** the payoff, in the user's terms — and the section that carries **the
flight to LA**, the page's only scene.

**Structure: scene → thesis → verdict.** This is a deliberate escalation and the
order matters. The anecdote earns the thesis; the thesis is Ry's abstraction of
it; the verdict is him saying what it meant. Reversing any two flattens it.

**Beat 1 — the anecdote (~130 words, the page's one first-person scene).**
Ry, 2026-07-31, recounted here because it is the single best piece of evidence on
the page and none of it is invented:

- On a plane to **Los Angeles**, to play a gig **that night**.
- Traktor® open, alt-tabbing to SetMaster, digging for transitions — the set for
  that night was **already prepared**.
- He finds ideas good enough to consider inserting into a finished set.
- **SetMaster let him lock the transitions in to the point of confidence** — cue
  points, the moves, the notes — well enough to commit them to a paying gig the
  same day.
- **That night, mid-gig, he alt-tabbed back to SetMaster and read his own notes
  from the plane ride that afternoon.**
- The realization, in his words: this is *"beyond just a fancy spreadsheet with
  color coding — it really does improve the DJ craft."*

**Why this is the most valuable 130 words available:**

1. **It closes the loop the entire product is built around** — prep and
   performance are the *same artifact*, hours apart, and the handoff between them
   is the notes. Every feature claim in S7 is abstract until this scene makes them
   concrete.
2. **It is the highest-stakes possible test of the notes feature.** "Detailed notes
   so you remember where you left off" sounds like a convenience until the
   remembering happens live, in front of an audience, on the same day.
3. **It demonstrates confidence, not just capability.** Changing a prepared set on
   the day of a paid gig is a real professional risk. The story is that the tool
   absorbed enough of that risk to make the change worth making — which is a far
   stronger claim than "it saved time."
4. **The closing line is the thesis of the whole page in Ry's own voice**, and it
   pre-empts the exact objection a skeptical reader is forming: *isn't this just a
   spreadsheet?*

**Beat 2 — the thesis**, as a pull quote, presented as the conclusion the scene
supports rather than a claim standing alone:

> *"Connect your brain's idea with the tracks you have that fit that idea,
> faster."*

**Beat 3 — the quantified payoff.** Hours out of catalog filtering and
Spotify®-vs-Traktor® comparison; hours back into DJing and into music discovery
(T). Kept brief — the scene already did the persuading.

**Beat 4 — the verdict.** Ry's *"beyond just a fancy spreadsheet with color
coding"* line lands here as the section's last sentence, in quotes and attributed.
**Not** as a second pull quote — two pulled quotes in a 300-word section is
shouting.

**Writing notes.** Present tense for the scene, past for the frame. Name Los
Angeles; a real city is worth three adjectives. **Do not embellish** — no set
names, no crowd reaction, no track titles, none of which Ry gave. The restraint is
what keeps it credible next to a page that otherwise refuses to editorialize.

**RESOLVED (Ry, 2026-07-31): this was SetMaster 2.**

That is the better answer, and it changed the section's job. The anecdote now
argues **for** Perform Mode instead of around it:

- The workbook grew a zoomed performance view; **SetMaster 3 has not rebuilt it**
  (deferred, `00-overview.md` §6).
- So the closing beat is the tone guide's §4.4 immediate caveat, stated plainly:
  the current version does not have that view, the set editor is there to switch
  to and it works, and Perform Mode is specified and waiting rather than built.
- **The flight is the reason it is on the list instead of off it.** That converts
  a deferred feature from an omission into a considered decision with evidence
  behind it, which is a better outcome than the SM3 reading would have produced.

Knock-on: **S3 absorbs the performance-view beat** rather than carrying it as a
standalone aside, so the flight pays it off directly two sections later.

---

### S9 · Teaching, and what's next (movement VII, second half)

**Purpose:** show the roadmap thinking. Keep it to ~120 words.

Beats:

- **Teaching.** Always in the back of Ry's mind: a great tool for teaching DJs —
  *not beginners*, intermediate, once they understand transitions and song
  composition. A set page is a legible artifact for learning to cue a track and
  to line up key, BPM, and cue points; a student can study a complex transition
  or a group of them (T). Ties directly to Ry's AI-coaching practice without
  needing to say so.
- **Rekordbox® collection import is planned**, no timeline, definitely a future
  version (T). Note the discipline: it is currently listed *out of scope* in the
  repo's non-goals (R), which is what "planned, no timeline" honestly looks like.
- **A portfolio piece, and actively developed** (T; C-05). The phrasing is settled:
  *"built as a portfolio piece for AI-engineering work, and actively developed."*
  **The company name is not used** — naming one employer narrows the page to that
  employer and dates it the moment Ry lands anywhere else.

---

### S10 · Closing

- One paragraph, no summary-of-a-summary.
- Three links: **try it** → the landing page; **the code** → the public repo;
  **work with Ry** → the intro call.
- The unaffiliated-software line and the ® attributions (D-006).

---

### S11 · Sidebars (running alongside, not in the main column)

Each drops without affecting the spine:

| Sidebar | Where | Contains |
|---|---|---|
| *The transition row* | S3 | A diagram of the two-column layout — the product's core idea in one picture |
| *Golden-master testing* | S6 | ~60 words on why byte-identical output is the right bar for a port |
| **How the build was run** | S6 | The orchestration and cost policy — **shipping (C-06)**. Spec below |
| *Stack* | S6 | FastAPI + ported Python pipeline · React 18 + Vite + TypeScript · SQLite · pytest / vitest / Playwright |

#### S11a · "How the build was run" — the orchestration sidebar

Ry's instruction (2026-07-31): ship it, **and be impressive about it.** So this is
the one place on the page where the register shifts from understatement to
specificity — not by adding adjectives, but by putting the actual numbers where a
reader expects vagueness.

**The discipline that makes it land: no adjectives, only facts a reader can't
dismiss.** "Sophisticated multi-agent orchestration" is a claim anyone can make.
*"Enforced two ways — an environment variable and a per-call model pin — zero
deviations across the build"* is a claim almost nobody can make, and it does the
persuading by itself. **If a sentence in this box would survive being written by
someone who hadn't done the work, cut it.**

Beats, ~120–150 words, in this order:

1. **The build was cost-tiered on purpose.** One orchestrator on the frontier
   model; **every** sub-agent on Opus; no frontier sub-agents spawned. Written
   down as policy *before* the build, not rationalized after.
2. **The policy was enforced, not hoped for** — an environment variable **and** a
   per-call model pin, belt and braces. **Zero deviations** across the entire
   build.
3. **The output.** A complete spec package in, and in **about a day**, an
   application that passed all four acceptance criteria end to end against real
   data. *(First commit 2026-07-06; final report 2026-07-07.)*
4. **It was audited as it went** — **31 logged decisions**, each with its
   rationale, and verification driven by a Playwright suite against the **real
   built app**, re-run independently by the orchestrator rather than taken on the
   builder's word.
5. **The closing line does the work the rest of the page has been doing:** the
   speed is not the point — the *reproducibility* is. Anyone can get an app out of
   a model once. The interesting question is whether you can say why it came out
   the way it did, and this build can, thirty-one times over.

**Guardrails.** No token or dollar figures (not published anywhere, and they date
instantly). No model marketing language. **No implication that SetMaster 3 contains
AI** — it explicitly does not, and this box sits closest to that misreading, so it
is the one place the distinction has to be airtight.

**Visual treatment.** A `--surface-2` panel with a mono `HOW THE BUILD WAS RUN`
label, the three numbers (`1 day` · `31 decisions` · `0 deviations`) set as a small
stat row, and the prose beneath. It should look like the instrument-panel readouts
elsewhere on the page, not like a callout box.

---

## 4. Section budget

| Section | Words | Media |
|---|---|---|
| S1 Hero | 60 | 1 screenshot + 4 stat tiles |
| S2 The problem | 180 | — |
| S3 The spreadsheet | 350 | 1 diagram + 1 legacy screenshot |
| S4 SetMaster 2 | 220 | 1 legacy screenshot |
| S5 The lightbulb | 200 | 1 comparison screenshot |
| S6 The rebuild | 750 | 1–2 screenshots + up to 2 sidebars |
| S7 What it does now | 320 | 2–3 screenshots |
| S8 What it gives back | 330 | the LA scene + pull quote |
| S9 Teaching / next | 160 | — |
| S10 Closing | 80 | — |
| **Total** | **~2,650** | **8–10 visuals** |

S8 grew from 180 in round 1 — it now carries the flight-to-LA anecdote, which is
worth every word it takes. It is the only section on the page allowed a scene.

---

## 5. Evidence inventory — what exists to cite

Everything here is already in a repo; none of it needs to be created.

| Evidence | Where | Used in |
|---|---|---|
| Complete spec package, open questions closed to zero | `setmaster3/planning/` | S6 |
| Build #1 final report with acceptance evidence and a 31-entry decision log | `build-notes/final-report.md` | S6, S7 |
| Per-round fix reports v3.0.1 – v3.0.3 | `build-notes/v3.0.*-fix-report.md` | S6 |
| Changelog with the macOS honesty note | `CHANGELOG.md` | S6 |
| Public mirror rationale and the two defenses | `tools/public-mirror/README.md` | S6 |
| Release engineering rationale | `release/README.md` | S6 |
| macOS verification checklist | `build-notes/macos-release-verification.md` | S6 |
| SM2 VBA + Python archive | `legacy/setmaster-2/` | S3, S4 |
| SM2 prototype screenshots | `docs/sources/screenshots/` | S3, S4 |
| Public release with artifact + sha256 | `wolfpackdata/setmaster` releases | S6, S10 |

---

## 6. Rules for whoever writes the prose

1. **Every number traces to `04-claims-ledger.md`.** No figure appears in prose
   that isn't in that table with a source. This is the lesson `hire/`'s v2.4
   correction taught at cost: an unguarded second copy of a fact will drift, and
   nothing will notice.
2. **Quote Ry directly where his phrasing is better than a rewrite** — *"the
   lightbulb got bright,"* *"always being fresh,"* *"multi-tab beast of a
   workbook,"* *"your new source of truth."* Mark quotes as quotes.
3. **® on every visible Traktor / Native Instruments / Spotify.** "Exportify"
   plain. Ry's own name for the app in conversation is sometimes "RML SetMaster";
   the page says **SetMaster 3** throughout.
4. **No superlatives the repo can't support.** "Unparalleled" is in the transcript
   (T) and does not survive into the page.
5. **Limitations stay in.** Perform Mode deferred, macOS unverified, Rekordbox® not
   yet, the collection is one user's. Each one costs a sentence and buys the
   page's credibility.
6. **Past tense for the history, present for the product.**

---

## 7. What this outline deliberately omits

Named so Ry can overrule rather than discover the gap later:

- **A "results/metrics" band.** There is no user base, no revenue, no adoption
  curve. Inventing an impact section would be the single most damaging thing the
  page could do. The stat tiles in S1 are build facts, and they are honest.
- **A tech-stack hero section.** Logo walls of FastAPI/React/etc. are exactly the
  corny the `hire/` plan banned. The stack goes in a sidebar.
- **Screenshots of Traktor® or Rekordbox®** to illustrate the problem. Tempting,
  and forbidden by D-006 — those are NI assets. The problem section is prose, and
  the SM2 workbook screenshots are Ry's own.
- **A timeline graphic of the three years.** Considered; the `hire/` pages already
  own the timeline device, and here it would compete with the narrative rather
  than serve it.
- **The SM2 workbook import story.** It shipped, it was used, and it has since
  been retired now that every workbook is imported (R). Interesting to an
  engineer, a dead end in a narrative.

- **A "my journey" narrative device.** No *"I've always loved music…"* opening, no
  chapter framing, no reflective interludes between sections, no second-person
  address to the reader. The page is an argument with evidence attached, and the
  history earns its place only because it *is* the evidence.

  **The one exception, deliberate and bounded: the flight-to-LA scene in S8.** It
  is permitted because it is dated, specific, supplied by Ry, and load-bearing —
  it demonstrates the prep→performance loop that nothing else on the page can. It
  is **one scene, in one section, ~130 words.** A second scene anywhere makes both
  of them look like technique.

---

## 8. Open questions on the outline itself

C-01 through C-09 are all closed (`04-claims-ledger.md` §2), so items 3 and 4 from
round 1 are gone — Lexicon stays in the case study only, and the orchestration
detail ships as the §S11a sidebar.

Still open:

1. **Is the argument in §1 the right argument?** Everything else follows from it,
   and it changed shape in round 2 when "eight years" became three.
2. **Is S6 too long at 750 words?** It is 30% of the page. My read: it is the
   section the audience actually reads, and it should be the longest.
3. ~~**Which title?**~~ — **CLOSED, round 4.** Option 1 with *robust* for
   *shipped*. See §10.
4. ~~**The SM2 year** (C-08)~~ — **CLOSED, round 4: "leave it" (Ry).** The prose
   stays dateless on SetMaster 2 and the derived ~2024 figure never ships.
5. ~~An anecdote from three years of use~~ — **CLOSED, round 3.** Ry supplied the
   flight-to-LA story and confirmed it was **SetMaster 2**. It anchors S8.

**The outline is now written out in full.** Draft 1 of the prose lives in
[`05-case-study-copy.md`](05-case-study-copy.md), in the
[`docs/ryan-blog-tone.md`](../../docs/ryan-blog-tone.md) voice. Its own open items
(title, the hours-per-month figure, the Rekordbox® ® question) are listed at the
end of that file. **This outline is now the structure of record; the copy deck is
the text of record.** When they disagree, fix both.

---

## 9. The Lexicon rule

Ry named a real commercial product generously and unprompted. The rule that
follows:

- **Case study: keep it.** Naming a competitor, crediting what it does well, and
  declining to claim you beat it is a credibility move, and it is *true* here —
  Lexicon's comparison tool is powerful; it didn't do the bulk list filtering Ry
  wanted.
- **Landing page: leave it out.** A hype page that names a competitor invites the
  comparison it just declined to make.
- **Never** frame it as "unlike Lexicon…" or put it in a feature table. The
  sentence is *"this isn't supposed to compete with it."*

---

## 10. Title options

**Closed in round 4.** Ry took option 1 with one word changed: *shipped* became
**robust**. The live title is *"SetMaster 3: From a Spreadsheet on a Plane to a
Robust Application."* The table below is the record of what was considered.

| # | Title | Reads as |
|---|---|---|
| 1 | *SetMaster 3: from a spreadsheet on a plane to a shipped application* | Narrative. Uses the best concrete image in the transcript. **Chosen, with *shipped* → *robust*.** |
| 2 | *Three years, three rewrites, one idea: building SetMaster 3* | Structural. **Replaces round 1's "Eight years…"**, retired by C-07 — and it is stronger at three, because the number now reads as pace rather than tenure |
| 3 | *Specifying before building: how SetMaster 3 got made* | Engineering-first; the truest to S6 and the least inviting |
| 4 | *The tedious part* | Ry's own framing, minimal. Strong if the standfirst carries the weight |

---

## 11. Iteration log

**Round 1** — outline drafted from the transcript and repo, 2026-07-31.

**Round 2** — 2026-07-31, Ry's rulings on all nine claim conflicts:

- **C-07 landed the biggest change.** The first SetMaster is **2023**, used
  professionally from the start — so *eight years* became **three**, and the §1
  argument, the S1 standfirst, the S3 opening, and title option 2 all changed with
  it. The figure was never sourced; it was mine, and it is retired everywhere.
- **C-01** — one catalog number only: ~7,000 in Traktor®, library many times that.
- **C-02** — build #1 plus three hardening rounds, 74 issues.
- **C-04** — Lexicon stays in S5; never on the landing page.
- **C-05** — portfolio framing kept, company name dropped.
- **C-06** — the orchestration sidebar ships, and §S11a was rewritten from a
  one-line table entry into a full content spec at Ry's request to make it
  impressive.
- **C-08** — origin dates 2023 / ~2024 / 2026; the middle one is derived and soft.

**Round 3** — 2026-07-31, Ry supplied the **flight-to-LA anecdote**.

S8 was restructured around it into **scene → thesis → verdict** and grew from 180
to 330 words. It is the page's only first-person scene and the only place a
narrative moment is permitted; §7's ban on "my journey" narrative devices stands
everywhere else, and this is not one — it is evidence, dated, specific, and
unembellished.

What it buys, briefly: it closes the prep→performance loop the product is built
around, it tests the notes feature at the highest possible stakes (live, same
day), it demonstrates *confidence* rather than mere capability, and its closing
line — *"beyond just a fancy spreadsheet with color coding"* — pre-empts the exact
objection a skeptical reader is already forming.

**Still awaiting Ry:** the five items in §8 — now including **which version of
SetMaster the LA story used**, which is a one-clause difference but a meaningful
one. None of them blocks the prose.

**Round 4** — 2026-07-31, after the page was built. Ry's followup list on the
Notion task, worked against both the copy deck and the live page.

- **The standfirst is now Ry's own framing** and opens on *data engineering meets
  DJ engineering* rather than on the job title. The change is recorded in
  `05-case-study-copy.md`.
- **The title takes *robust* for *shipped*.** §10 closed.
- **Two claims closed by ruling rather than by evidence:** the SetMaster 2 year
  stays out (*"leave it"*), and the hours-per-month estimate keeps its hedge.
- ***Cloud architect* is retired from the S6 opening** in favor of *"I began
  building apps with Claude."* This is the second time a transcript fact has been
  superseded by a direct instruction from Ry (the first was C-07's *eight years*),
  and the ledger now carries a source class for it.
- **The favicon** was added here and to `roi-calculator/`, the two pages in the
  repo that lacked one.

**Still open after round 4:** whether S6 is too long at 750 words (§8 item 2),
and the four outstanding screenshots, which are Ry's to capture.
