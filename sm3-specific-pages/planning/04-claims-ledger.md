# Claims ledger

Every factual claim either page may make, with its source. **No number or factual
assertion appears in prose that is not in this table.**

This exists because of a lesson already paid for in this repo: the `hire/` pages
carried a corrected music-tenure fact that the source résumé YAML did not, the
two disagreed for a week, and `verify_facts.py` stayed green the whole time
because it read the YAML and not the pages. *That silence was the lesson.* These
pages have no automated fact check at all, so the ledger is the control.

**Sources:** `T` = Ry's 2026-07-31 transcript · `R` = the `wolfpackdata/setmaster3`
repo (path given) · `P` = the public `wolfpackdata/setmaster` repo · `Ry` = a direct
instruction from Ry, dated.

**`Ry` outranks `T`.** The transcript is Ry thinking out loud; a later instruction is
Ry deciding. Where the two disagree, the row records both and says which one ships,
so a fact that changed does not read as a fact that was never checked. Two rows carry
this so far: the *eight years* retirement (C-07) and the *cloud architect* line in S6.

---

## 1. Verified claims

Safe to write. Each traces to a checkable source.

### Product

| Claim | Source | Pages |
|---|---|---|
| Two jobs: structured set preparation, and Traktor®↔Spotify® catalog analysis | R `planning/00-overview.md` §1 | both |
| **Set preparation stands alone** — fully useful with no collection ever loaded; Traktor® is never a prerequisite | R `00-overview.md` §1 (stated as a binding rule) | both |
| Fully offline: local backend + browser UI on localhost. No cloud, no accounts, no telemetry, no external API calls | R `00-overview.md` §2 | both |
| `collection.nml` is opened **strictly read-only** and never written | R `00-overview.md` §2; sha256 integrity snapshots in `testdata/` | both |
| Single-user; no auth, no multi-tenancy | R `00-overview.md` §2 | case study |
| One row = one transition; out-track left, in-track right; read left to right | T; R `03-ui-design.md` §1.2 principle 4 | both |
| Manual RED / YELLOW / box cell formatting; no semantic flags | R `03-ui-design.md` §1.1 item 8 | landing |
| Customizable emoji palette (the *I like* validation list is user-editable) | T; R `02-features/advanced-settings-validation-lists.md` | both |
| Mix timer / Play Time / Mix Length stats | T; R `03-ui-design.md`, issue #72 vocabulary | both |
| Set export to CSV, XLSX, and Markdown | R `02-features/set-export.md` | landing |
| Compound filter and sort across the whole collection, beyond what Traktor® offers | T; R `02-features/track-playlist-matrix.md` | both |
| Comparison blank-cell notes **survive every re-run** (fail-safe snapshot-merge) | R `01-data-model.md` §6.3; verified in `build-notes/final-report.md` criterion 2 | both |
| Spotify® side is file-based via exportify.net CSVs — no Spotify API | R `00-overview.md` §2 | both |
| Windows and macOS launchers; double-click, no terminal | R `00-overview.md` §3 | landing (with C-03, **as narrowed**) |
| Release payload bundles its own CPython — no Python, no Node, no terminal needed | R `release/README.md` | landing |
| Dark theme only | R `03-ui-design.md` §1.1 item 3 | — |

### Build and engineering

| Claim | Source | Pages |
|---|---|---|
| Spec package written first; open questions closed to zero before build | R `planning/`, `04-open-questions.md`, `CLAUDE.md` | case study |
| Ry and Claude worked on planning documents "for several days" before building | T | case study |
| SM2's matching/normalization heuristics ported **verbatim** by rule — restructuring allowed, behavior changes not | R `CLAUDE.md`, `00-overview.md` §2 | case study |
| Pipeline port is **golden-master byte-identical** to SM2 on real data | R `build-notes/final-report.md` (D-006, D-011) | both |
| First commit **2026-07-06** | R `git log --reverse` | case study |
| Build #1 complete **2026-07-07**, tagged `v3.0.0-build1` | R `CHANGELOG.md`, tags | case study |
| Fix rounds v3.0.1 (2026-07-08), v3.0.2 (2026-07-09), v3.0.3 (2026-07-30) | R `CHANGELOG.md`, tags | case study |
| **Build #1 plus four hardening rounds — 93 issues** (round sizes 26 / 12 / 36 / 19) | R `CHANGELOG.md` (C-02, revised by C-10) | both |
| First public release **2026-07-31**, `v3.0.3` | P releases | both |
| **25 days** from first commit to public release | derived: 2026-07-06 → 2026-07-31 | both |
| Current test totals: **236** backend pytest · **624** frontend vitest · **37** Playwright e2e = **897** | R `build-notes/v3.0.4-release-unblock-report.md` §2.2 final gate | both |
| Second public release **2026-08-05**, `v3.0.4` — Windows x64 zip **and** Apple silicon `.dmg` | P releases (verified live 2026-08-05) | both |
| Windows artifact `SetMaster3-3.0.4-windows-x64.zip`, **102 MB**; macOS artifact `SetMaster-3.0.4-macos-arm64.dmg`, **87 MB** | P release assets | landing |
| macOS build is **signed, notarized, and stapled**; passed a clean-install acceptance test on a quarantined download | R `build-notes/v3.0.4-fix-report.md` | both |
| Build #1 acceptance verified against Ry's **real** collection: 6,810 tracks × 149 playlists | R `build-notes/final-report.md` criterion 1 | case study |
| Signature digging workflow returned **111** rows in one pass | R same | case study |
| Ry tested the web app **in live DJ situations** during the fix rounds | T | case study |
| One issue → one branch → one PR; issues stay open until Ry verifies against real data | R `CLAUDE.md` | case study |
| Public repo is a **generated mirror** with no history — a history rewrite was considered and rejected as "one mistake away from a permanent, unrecoverable leak" | R `tools/public-mirror/README.md` | case study |
| Two independent defenses: a fail-closed allowlist, and a scanner that gates the **generated output** and deliberately does not share the allowlist's logic | R same | case study |
| Any scanner finding **aborts the build and deletes the output** — no warn-and-continue | R same | case study |
| The scanner has already caught a real leak (a `C:\Users\…` string in a UI placeholder) | R same | case study |
| A virtualenv is not a portable runtime, so the payload ships a relocatable python-build-standalone CPython; the smoke check fails the artifact if a `.venv` appears | R `release/README.md` | case study |
| Stack: FastAPI + Python pipeline · React 18 + Vite + TypeScript · pytest / vitest / Playwright | R `CLAUDE.md` | case study sidebar |
| **MIT licensed** | P `LICENSE` (SPDX: MIT; re-verified via the license API 2026-08-05, after the mirror was regenerated) | landing |
| ~~sha256 published with the release artifact~~ | **RETRACTED — see C-11. Never write this.** | neither |
| ~~Windows artifact: `SetMaster3-3.0.3-windows-x64.zip`, 72 MB~~ | superseded by the v3.0.4 row above | — |

### History

| Claim | Source | Pages |
|---|---|---|
| Ry is a professional DJ; also performs with DJ partners whose catalogs are on his machine | T | both |
| **~7,000 tracks in Traktor®, drawn from a personal library many times that size** | R `build-notes/final-report.md`; framing per C-01 | both |
| **The first version of SetMaster was built in 2023 and used in professional settings immediately** — three years of professional use | Ry, 2026-07-31 (C-07) | both |
| First iteration was **Google Sheets**, chosen for built-in cross-device backup; later Excel | T | both |
| Motivation: Traktor®/Rekordbox® set prep was "super slow"; the tedium is searching, filtering, sorting, and checking against past sets so tracks don't repeat | T | both |
| Streaming made the problem worse, not better — bigger libraries still need organizing | T | case study |
| It became "a multi-tab beast of a workbook," built on planes between gigs | T | both |
| The workbook grew a **performance view** — zoomed, color-coded, for glancing at during long sets | T | case study |
| **The flight to LA** — prepping on a plane to a Los Angeles gig with Traktor® open and SetMaster alongside; found transitions good enough to insert into an already-prepared set; locked them in confidently enough to play them **that night**; mid-gig, switched to SetMaster to read the notes written that afternoon. **This was SetMaster 2** (Ry, 2026-07-31) | Ry, 2026-07-31 (anecdote) | case study S8; condensed on landing band 4 |
| SetMaster 3 has **no dedicated performance view**; the workbook grew one, and Perform Mode is specified and deferred | R `00-overview.md` §6, `03-ui-design.md` §5.4 | case study S8 caveat, landing band 9 |
| Ry's verdict, **verbatim and quoted as his**: *"beyond just a fancy spreadsheet with color coding — it really does improve the DJ craft"* | Ry, 2026-07-31 | case study S8 |
| SetMaster 2 = the workbook plus a **VBA and Python** backend | T; R `legacy/setmaster-2/` (13 VBA modules, 4-stage Python pipeline) | both |
| SM2 imported the Traktor® collection for multi-filtering on key, BPM, artist | T | both |
| Used during set prep, not live | T | case study |
| The lightbulb: a one-off flow joining SM2's Python output to exportify.net CSVs of his Spotify® playlists | T | case study |
| That flow "saved hours every month" | T | case study |
| **Building apps with Claude**, starting in **early 2025**, reframed it as a web app; work started **early July 2026** | Ry, 2026-07-31 (supersedes T, which said *cloud architect*) | case study |
| The prototype's Traktor® connection was **Windows-only** — the primary motivation for the rebuild | R `00-overview.md` §3 | case study |
| Rekordbox® collection import is **planned, no timeline** | T; R `00-overview.md` §6 lists it out of scope today | both |
| Perform Mode and the natural-language filter bar are **deferred** | R `00-overview.md` §6 | landing band 9 |
| A teaching tool for **intermediate** DJs — past beginner, already understand transitions and song composition | T | case study |
| SM2 workbook import has been **retired** now that every workbook is imported | R `CLAUDE.md`, issue #192 | neither (see `01-…` §7) |

---

## 2. Conflicts — all resolved

Nine were opened 2026-07-31 and closed the same day; **two more were opened and
closed on 2026-08-05**, when `v3.0.4` shipped and the pages were deployed. All
eleven are closed. Kept in full rather than deleted: each records *why* a claim
reads the way it does, which is what stops a future edit from quietly reopening
it.

| id | Subject | Outcome |
|---|---|---|
| C-01 | Catalog size | ~7,000 in Traktor®, library "many times that size" |
| C-02 | Build rounds | ~~Build #1 + three hardening rounds, 74 issues~~ → **revised by C-10** |
| C-03 | macOS | **NARROWED 2026-08-05, not lapsed** — Apple silicon, macOS 14+ |
| C-04 | Lexicon | Case study only, never the landing page |
| C-05 | Anthropic portfolio | Substance kept, company name dropped |
| C-06 | Orchestration detail | Yes — S6 sidebar, written to impress |
| C-07 | Years in use | **2023 → three years.** "Eight years" retired |
| C-08 | Origin-story dates | 2023 / ~2024 / 2026 — middle cell soft |
| C-09 | License | MIT |
| **C-10** | Build rounds after v3.0.4 | **Five rounds, 93 issues** (26/12/36/19); the 19 is soft |
| **C-11** | SHA-256 per release | **RETRACTED — no release publishes one. Never write it** |

**Nothing here blocks the prose any more.** Two soft cells remain and both
degrade safely: C-08's SM2 year, derived rather than stated, and C-10's
nineteen-issue v3.0.4 round, consistent with how 26/12/36 were counted rather
than stated by a source.

**Both 2026-08-05 rulings came from the same cause and are worth reading
together:** a release shipped, and three claims that had been true of `v3.0.3`
stopped being true of `v3.0.4` without anyone editing a word. Two were stale
(the round count, the test total) and one was false (the checksum). §4 already
said version-dependent values need a release checklist; C-10 and C-11 are what
it costs when the checklist is a paragraph in a planning document rather than a
step someone runs.

### C-01 — The catalog size figures — RESOLVED

**Was:** the transcript says a catalogue of **100,000 tracks**, of which Ry
maintains around **10,000**. The repo's real `collection.nml` is **6,810 tracks
across 149 playlists** (`build-notes/final-report.md`), later cited as 7,033 in
the same report — so even the repo figure needed picking.

**RESOLVED (Ry, 2026-07-31).** The pages use one precise sentence and no other
catalog number:

> **~7,000 tracks in Traktor®, drawn from a personal library many times that size.**

Rationale: it is checkable against the public repo, which is exactly what a
technical reader will do. The 100,000 figure describes the whole music library
across drives and formats and is not asserted, because the page has no room to
explain the difference and an unexplained 100,000 next to a countable 7,000 reads
as inflation. "Many times that size" carries the scale honestly.

### C-02 — How many build rounds — RESOLVED

**Was:** the transcript says *"four rounds of fine-tuning and one big round of bug
fixes after the initial build."* The repo has build #1 plus **three** numbered fix
rounds (v3.0.1 / v3.0.2 / v3.0.3), totalling 74 issues. (`v3.0.3-round1-plan.md`
and `v3.0.4-round2-plan.md` suggest Ry numbers rounds within the current cycle
separately from versions, which likely explains the count.)

**RESOLVED (Ry, 2026-07-31)** — use the repo's numbers, which are checkable
against the changelog:

> **Build #1 plus three hardening rounds — 74 issues.**

Round sizes 26 / 12 / 36, dated 2026-07-08 / 07-09 / 07-30.

### C-03 — macOS support — **NARROWED 2026-08-05, not lapsed** ⛔ still a hard rule

**What changed.** `v3.0.4` shipped on 2026-08-05 with
`SetMaster-3.0.4-macos-arm64.dmg`: a signed, notarized, stapled `.app` in a
drag-to-Applications disk image, built and acceptance-tested on a real Mac
against a quarantined download. The condition C-03 was waiting on is met, and
both pages now carry a working macOS download.

**The rule did not disappear. It narrowed, and the narrow version is still hard:**
- ✅ *"Apple silicon, macOS 14 (Sonoma) or later."* Every visible macOS claim
  carries that qualifier.
- ✅ Naming what is still unverified: the end-to-end suite and the golden-master
  pipeline tests **have never run on macOS**. The artifact passed its own
  clean-install acceptance test instead, which is a different and smaller claim.
- ❌ **"Intel Macs"** — not supported, and the page says so rather than leaving
  it to be discovered on first launch.
- ❌ **"macOS 13 or earlier"** — the bundled NumPy is `macosx_14_0_arm64`, the
  app claims 14.0, and the builder refuses to produce an image claiming less.
- ❌ Plain **"macOS support"**, **"cross-platform"**, or `operatingSystem:
  ["Windows","macOS"]` with no version floor.

**Why this row stays instead of being deleted.** The failure it guards against
never was "claiming macOS" in the abstract; it was *rounding a qualified platform
claim up to an unqualified one*. That failure is still available, and it is now
easier to make, because the qualifier is a detail rather than a whole missing
platform. A later edit that quietly drops "Apple silicon, macOS 14 or later"
re-opens C-03 exactly as it stood.

**Superseded phrasing, recorded so it is not restored:** *"The Mac build is
written and waiting on a Mac to build and verify it."* True until 2026-08-05,
false after it. It appeared on the landing page, the case study, and the blog
post; all three were corrected.

### C-10 — Build rounds after v3.0.4 — RESOLVED (Ry, 2026-08-05)

**Was:** C-02 fixed the figure at **build #1 plus three hardening rounds, 74
issues** (round sizes 26 / 12 / 36). `v3.0.4` is a fourth hardening round, so the
landing page's *"Four rounds, 74 issues"* and the case study's *"Four Rounds,
Seventy-Four Issues"* both went stale the day the release shipped. The case
study's **body** already described the fifth round; only the headline figures
lagged, which is the more dangerous shape of staleness because the page
contradicts itself rather than simply being old.

**RESOLVED — five rounds, 93 issues.**

> **Build #1 plus four hardening rounds — 93 issues** (round sizes 26 / 12 / 36 / 19).

**The 19 is the softest number on either page, and it is recorded as such.** It
is a count of unique `#NNN` references in the `CHANGELOG.md` 3.0.4 section, which
is the same accounting that produced 26 / 12 / 36, so it is consistent rather
than sourced. It is deliberately *not* the private repo's closed-issue count for
the period (15) or its lifetime closed count (99); those use different
accounting, and mixing them is how a page ends up with a number no source
supports. If a future release makes this figure awkward again, drop the issue
count rather than re-deriving it: the round count and the test total are both
checkable, and the issue count buys little next to them.

### C-11 — SHA-256 published with each release — **RETRACTED (Ry, 2026-08-05)**

**Was:** the ledger carried *"sha256 published with the release artifact"*
(sourced to the v3.0.3 release body), and **six** places in shipped copy said so:
four on the landing page (both download cards, the "downloading for another
machine" note, the *Open source* card), one in the case study's closing block,
and one in the blog post.

**Fact, checked against the live release before deploying.** `v3.0.4` publishes
**no checksum at all** — not in the release body, and not as a checksums asset.
The release carries exactly two files, the Windows zip and the macOS `.dmg`.
`v3.0.3`'s body mentioned a hash once, which is how the claim got into the
ledger and then into copy, and it was never re-checked against the next release.

**RESOLVED — every instance removed. Never write it again until a release
actually publishes hashes.** Replacement phrasing, which is true and needs no
maintenance: *"every release and every artifact listed publicly on GitHub."*

**This is the ledger's own failure mode, caught by its own procedure.** §4 says
version-dependent values go stale on every release and that updating them belongs
in the `setmaster3` release checklist. A hash is exactly that kind of value, and
it is worse than a stale number: a wrong test count is embarrassing, an
advertised checksum that does not exist invites a technical reader to go looking
and find nothing. **If hashes are added to a future release, this row is the
thing to edit first, then the six places.**

⚠️ **Do not confuse this with the two SHA-256 claims that remain true.** The case
study says `collection.nml` integrity is checked with SHA-256 snapshots in
`testdata/`, and that the acceptance harness hashes against the known collection
file. Those are about **test fixtures**, are sourced, and stay.

### C-04 — Naming Lexicon — RESOLVED

**Fact.** Ry named it generously and unprompted (T): powerful comparison tool,
didn't do the bulk list filtering he wanted, *"this isn't supposed to compete with
it."*

**RESOLVED (Ry, 2026-07-31)** — **case study yes, landing page no.**

Keep it in S5 as written. Naming a competitor on a hype page invites the exact
comparison the sentence declines to make; in a case study the same sentence reads
as credibility. **Never phrase as "unlike Lexicon,"** and never in a feature table.

### C-05 — "Part of my Anthropic portfolio" — RESOLVED

**Fact.** Ry: *"this is always meant to be part of my Anthropic Portfolio"* (T).

**RESOLVED (Ry, 2026-07-31)** — **keep the substance, drop the company name.**

> **Built as a portfolio piece for AI-engineering work, and actively developed.**

Naming one company narrows the page's audience to that employer and dates the page
the moment Ry lands anywhere else — the same staleness class the `hire/` pages
already carry a warning for. **Omitted entirely from the landing page**, where it
is a non sequitur to a DJ.

### C-06 — Publishing the agent-orchestration detail — RESOLVED

**Fact.** The build ran under an explicit cost policy — a Fable orchestrator with
Opus sub-agents, no Fable sub-agents, enforced by env var **and** per-call pin,
zero deviations (R `build-notes/final-report.md` D-022, `prompts/fable-workflow-prompt.md` §0).

**RESOLVED (Ry, 2026-07-31)** — **yes, sidebar in S6, and make it impressive.**

Sidebar, not main column, because the case study's argument is that the discipline
mattered more than the speed — orchestration mechanics in the main column would
invert that. But within the sidebar it should be specific and confident rather
than hedged. Full content spec: `01-case-study-outline.md` §S11.

The facts it is allowed to use, all repo-sourced:

| Fact | Source |
|---|---|
| Cost-tiered execution: orchestrator on Fable, **every** sub-agent on Opus, no Fable sub-agents | `prompts/fable-workflow-prompt.md` §0 |
| Enforced **two ways** — env var *and* a per-call model pin | `final-report.md` D-022 |
| **Zero deviations** across the whole build | `final-report.md` D-022 |
| Build #1 spec-complete → all four acceptance criteria passing in **~1 day** (first commit 2026-07-06, final report 2026-07-07) | git log + `final-report.md` |
| **31 logged build decisions** (D-001–D-031), each with rationale | `build-notes/decisions.md` |
| Verification driven by a Playwright suite against the **real built app**, re-run independently by the orchestrator | `final-report.md` |

### C-07 — Years in professional use — RESOLVED

**Gap.** No start date for the original spreadsheet appears anywhere. The
transcript says the prototype was used "for a year" before SM2, and that the web
app was conceived in early 2025 — but never when the sheet began. The archived SM2
git history was checked and starts **2026-06-16**, which is the prototype's public
*publication*, not its creation. No source in either repo carries the date.

**RESOLVED (Ry, 2026-07-31): the first version of SetMaster was built in 2023 and
used in professional settings immediately.**

> **Three years of professional use, since 2023.**

⚠️ **This retires the "eight years" figure**, which was a drafting placeholder
derived from Ry's framing and was never sourced. Every page and doc using it has
been corrected. Consequences, because this is a bigger edit than a number swap:

- The case study's **central argument** was *"solved it three times over eight
  years"* → now **"three times in three years"** (`01-…` §1).
- Title option 2, *"Eight years, three rewrites, one idea,"* is retired and
  replaced (`01-…` §10).
- The S1 standfirst and the landing hero stat both change.
- **The story gets better, not worse.** Eight years read as slow accretion; three
  years reads as rapid, deliberate escalation — and *"used in professional
  settings immediately"* is a genuinely strong fact on its own, because it means
  the tool was never a toy that later got serious. Both pages should say it.

### C-08 — Origin-story dates — RESOLVED

**RESOLVED** by C-07, for the three-panel timeline in landing band 4.6:

| Panel | Year | Basis |
|---|---|---|
| The spreadsheet | **2023** | Ry, 2026-07-31 — stated |
| SetMaster 2 | **~2024** | **Derived**, not stated: the transcript says the prototype ran *"for like a year"* before becoming SM2. Renders as "2024" only if Ry confirms; otherwise the panel drops its year and leads with the name. |
| SetMaster 3 | **2026** | git log, first commit 2026-07-06 |

The middle column is the only soft cell. Coherence check against the transcript:
sheet 2023 → SM2 ~2024 → *"becoming a Cloud Architect… early 2025"* reframes it as
a web app → build starts early July 2026. That sequence holds.

### C-09 — RESOLVED

The public repo is **MIT** (`SPDX: MIT`, verified via the GitHub license API,
2026-07-31). The "Open source" card in landing band 4.7 may say so.

---

## 3. Claims that must never appear

Not conflicts — prohibitions. Each is a thing a marketing page naturally reaches
for and none of them is true here.

| ❌ Never say | Why |
|---|---|
| Any detail of the LA gig Ry didn't give — the venue, the date, the crowd, a track title, a set name | The anecdote's whole value is that it is unembellished and checkable-sounding. One invented detail and it reads as marketing fiction, taking the rest of the page with it. |
| Any user count, download count, or "trusted by N DJs" | There are none. First public release was 2026-07-31. |
| **"Eight years"** — of use, of development, of anything | Retired by C-07. The figure is **three years, since 2023**, and the old number is unsourced. |
| Testimonials or quotes from other DJs | None exist. |
| That it is affiliated with, endorsed by, or partnered with Native Instruments, Spotify, or Lexicon | It is not. D-006. |
| That it supports Rekordbox® | Planned, not built. |
| That it has Perform Mode or a natural-language filter bar | Deferred, not built. |
| That it works with Serato, Engine DJ, or anything but Traktor® | Only Traktor®. |
| "Enterprise-grade", "AI-powered", "revolutionary", "unparalleled" | The last one is Ry's own word (T) and still doesn't ship. |
| Any performance figure not in `build-notes/` | The real ones are good; invented ones are checkable. |
| That the app uses AI or an LLM | It explicitly does not — every LLM integration is deferred (R `00-overview.md` §6). **This is the single easiest mistake to make**, given the case study talks about being *built with* Claude. Built with ≠ contains. |

---

## 4. Maintenance

- **Version-dependent values** — version, release date, artifact size, download
  URL, test totals — are declared **once** per page and read from that single
  declaration (`02-…` §6.4). They are not typed into prose.
- **Every SetMaster 3 release makes this page stale.** Updating it belongs in the
  `setmaster3` repo's release checklist, not only here.
- **When a conflict above is resolved, edit this file first**, then the page. The
  ledger is the source; the page is the copy.
