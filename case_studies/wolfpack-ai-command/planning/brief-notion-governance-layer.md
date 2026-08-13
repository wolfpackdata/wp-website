# Brief — the Notion governance layer

> Capability-level summary per the exposure ruling in `README.md`. Private repo names,
> workspace identifiers, account details, and internal doc structure are deliberately
> omitted.

## Purpose

Ry runs the business out of a Notion team space — four core databases (Projects, Tasks,
Products, Clients) plus a document hub — and delegates a growing share of the work inside
it to AI. Left ungoverned, an AI writing into a business's system of record produces
pages that are **structurally wrong** (blank pages instead of template-derived ones,
missing icons, missing relations, invented priorities) and **epistemically opaque** — no
way to tell which pages and edits were the human's and which were the AI's, and no record
of what the AI actually did.

This layer is the answer: a workbench where the owner's Notion conventions are captured
into **permanent, reusable AI skills** and a **published rulebook**. The working method is
observational — Ry demonstrates a convention live in the workspace, the AI records it,
and the observation is folded into the skills and the SOP, with an explicit standing
instruction to *ask before assuming a convention*.

The distinctive architectural insight: an AI assistant's standing instructions can
themselves live *as a Notion page*. So one canonical rulebook page serves every surface —
Notion's built-in AI, the coding CLI, desktop/web/mobile chat — and every human, from a
single source of truth. The repo is the source; the page is the build artifact,
published one-way and never hand-edited; every other surface holds only a thin pointer.

## What it does (capabilities)

- **Five AI skills**: four creation skills (task, project, product, client) and one
  linking skill (connecting a task to its GitHub issue and PR). Every write skill opens
  with the same mandatory identity preflight (below).
- **A rulebook of roughly 44 numbered rules in ten lettered sections**, covering
  identity and attribution, databases and icons, template-first page creation,
  interlinking, required-versus-optional properties, the task status lifecycle, GitHub
  linking, comment protocol, a carve-out for Notion's own AI, and an optional
  engineering-manager-style review workflow.
- **A CI contract validator** — read-only, offline, dependency-free — that checks the
  deliberately-duplicated SOP surfaces against each other: version strings, rule-ID
  cross-references, terminology casing, retired-rule phrasing, and the registry of
  governed databases. Written after drift was actually found, not speculatively.
- **An opt-in review workflow**: on a task proposing feature work, the AI can leave one
  inline comment per item written as an engineering manager reviewing a backlog — sizing,
  risks, edge cases, a recommendation. Offered, never run unprompted; advisory only.

## Design principles

- **Templates, never blank pages.** Every database has a designated template carrying
  self-filtering embedded views (a project page shows its own tasks; a product page shows
  its own tasks and projects). A page created blank silently loses its whole information
  surface. Corollary: fetch the live schema first — never guess a property name.
- **Uniform icons; meaning lives in color.** Every entry carries its database's icon, so
  an open browser tab is identifiable by kind at a glance. Per-type distinction is pushed
  onto a governed tag-color palette with stated semantics, so the two signals never
  compete.
- **Nothing exists unlinked.** Every task must link both a project and a product,
  resolved by a ladder: stated → deduced → a clearly-prefixed placeholder created under
  standing permission, minimal by design, and always announced — the prefix *is* the
  human's review flag. Clients are never auto-created at all.
- **Defaults encode restraint.** Priority is never inferred ("especially not High" — a
  rule born from bulk-clearing a dozen tasks whose default priority had become
  meaningless). Pricing is never invented. Repository URLs are never guessed. A task body
  is never written unless asked for.
- **The workspace wins on schema.** Where the rulebook and the live workspace disagree
  about schema, the workspace is authoritative and the page gets fixed — precedence is
  defined even for the SOP itself.

## Theme material — AI supervision and transparency

The richest seam in the whole system. The through-line: **an AI operating inside a
human's system of record must leave a legible, durable, non-forgeable trail.**

- **The AI has its own workspace identity.** Originally the connector authenticated as
  Ry, so every AI-created page was stamped with the human's name — indistinguishable from
  his own work, and (because the platform exposes no per-property edit attribution)
  **permanently unrecoverable**: the workspace's then-existing tasks can never be sorted
  into who-wrote-what. The fix was a dedicated AI member account. From that day, every
  AI-created page, edit, and comment carries the AI's identity in the system's own
  audit fields.
- **Three provenance questions, three deliberately separate answers.** Who *created* a
  page (system-managed authorship), who *completed* the work (a status split: an
  AI-complete state distinct from the human's own done state), and who *owns* it
  (assignment — which the AI is forbidden to set). The rulebook explicitly defends this
  redundancy against future "simplification," because collapsing the three loses
  information each one uniquely carries.
- **The never-self-assign rule is deliberate signal design.** The owner uses
  assignment-to-the-AI as *his own* marker for AI-completed work — and it only carries
  information *because* the AI never sets it. A human-only channel, preserved by
  prohibition.
- **A silent status flip is an incomplete transition.** Every status change the AI makes
  carries a timestamped comment: one sentence on entry ("working this now"), one on every
  exit — including the case where work stalls, which the SOP calls out as *the* case the
  human most needs explained: what remains, and why it stopped, naming the specific
  outstanding items. Mid-work comments only when they carry information; never a bare
  "done"; progress narration is treated as noise.
- **Anti-theater rules.** Completion is an objective test (every checkbox in the task
  body checked), not a feeling — and the AI may not unilaterally expand scope to clear
  the gate. Backfilling is forbidden: creating the task after the work and stamping it
  through the lifecycle in one pass "makes the status cosmetic… a live status no one
  could have observed is theater." Both rules exist because the AI actually did the thing
  once and the owner caught it.
- **Where identity fails, the other channel escalates.** Notion's built-in AI acts as
  the signed-in human, so the identity signal doesn't exist on that surface. The SOP's
  response: there, the status lifecycle and its comments are the *only* record an AI did
  the work — so they matter more, not less.
- **AI work is complete, not provisional.** The AI-complete status is terminal and equal
  in standing to the human's — a provenance marker, not "pending review." The SOP
  explicitly forbids re-doing AI-completed work or calling a project unfinished because
  its tasks were AI-completed. (An earlier draft framed it as "pending verification";
  the correction is recorded in one word: *wrong*.)

## Theme material — security and confidentiality

- **A mandatory identity preflight before writing.** Before its first write of a session
  — and again before anything destructive — the AI verifies which account the connector
  is bound to. Any identity other than its own is a **hard stop**: don't write, tell the
  human, and the fix is his, not something to work around. This rule was filed as a
  *fix*, not a docs change: the skills previously assumed the identity and **failed
  open**.
- **The re-auth hazard.** Re-authorizing the connector while the browser is signed in as
  the human silently rebinds the AI as the human — and looks like success. A genuine
  OAuth-session-bleed class of bug; the mitigation is a deliberate authorization flow
  plus verify-don't-trust.
- **Permission scope is the privacy boundary.** Anything the AI's account can't see is
  structurally invisible to it — enforced by workspace membership, not by prompt. The
  failure is quiet (missing from results, no error), so the standing rule runs both
  directions: grant access deliberately, and when something seems missing, suspect
  permissions before believing the data is gone.
- **An enumerated never-touch list**: system-managed attribution fields, the human's own
  completion status, assignment, and the published rulebook page (a build artifact) are
  all off-limits to AI writes; existing links are never silently overwritten.
- **Destructive changes require a named snapshot first** — duplicate the database,
  timestamp-rename the copy, trash it only after the human confirms — plus a baseline
  export kept as a last-resort reference.
- **CI holds no credentials by design.** The automated validator is read-only and
  offline; live-workspace drift checking is deliberately a manual, read-only runbook
  rather than a credentialed pipeline.
- **The system knows what it can state versus enforce.** Per-user AI instructions can't
  be pushed workspace-wide, and the SOP says so — concluding that the real enforcement
  surfaces are templates, property descriptions, and violation views, which bind every
  assistant and every human equally.

## Theme material — intuitive setup with flexibility

- The rulebook is written to be read two ways — by people, and loaded by an AI as
  standing instructions — and each surface gets a thin pointer, not a copy, with an
  explicit warning against copying the SOP into independent memories that drift.
- Templates make the correct shape the default shape; the skills make the conventions
  self-applying; the color legend records the owner's own stated rationale for every
  choice, so the system's aesthetics are documented taste rather than arbitrary rules.
- Rules are relaxed as experience warrants — a backup rule narrowed to destructive
  changes only; a creation gate relaxed into standing placeholder permission *paired
  with* a compensating transparency requirement — so the ceremony tracks reality.

## Real numbers (measured 2026-08-13; re-verify at write time)

- **5** AI skills; **14** SOP documents; **~44** numbered rules in **10** sections.
- **25** commits over **13 days** of initial build (2026-07-09 → 2026-07-21); **2**
  tagged releases; the rulebook page itself versioned and still receiving updates weeks
  later.
- Workspace scale at capture: **27** projects, **~117** tasks, **21** products, **6**
  governed data sources.
- The CI validator runs **5** check classes; a second-vendor AI review produced the
  findings that motivated it.

## Evolution highlights

- **A linking convention changed three times in twelve days** — plain URL → the
  platform's official integration (ruled out by a platform-side bug) → back to plain
  URLs, reframed as the deliberate standard → cardinality narrowed to exactly one link
  per property, with pre-existing multi-link tasks grandfathered and the retired phrasing
  written into the validator so it can't creep back.
- **A sub-task experiment was built, shown, rejected, and reverted the same day** — and
  the rejection became a standing prohibition with the cleanup gotchas recorded.
- **A negative-only rule generalized wrongly** ("never write a body just to create a
  comment anchor" got over-read as "never write task bodies") — caught when the AI
  described an explicitly-requested body as forbidden. The fix states the default
  positively: the only body the AI must never write is one the human didn't ask for.
- **The self-audit turn:** a second AI vendor's review found the SOP drifting against
  its own duplicated surfaces — a skill carrying a superseded rule, mirrors stale against
  the live workspace. The response was the contract validator, whose stated philosophy
  doubles as the system's: *duplication drifts; a check that cries wolf gets deleted.*
- **Honesty corrections:** an unvalidated surface (a third AI vendor's chat product) was
  advertised as supported, then re-marked planned/experimental across every mention; an
  ambiguous icon on one product was surfaced to the human rather than silently
  "corrected."
- Nearly every rule carries the date it was captured and the incident that produced it —
  the SOP is legible as a changelog at the level of an individual sentence.
