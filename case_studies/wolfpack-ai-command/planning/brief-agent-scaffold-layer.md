# Brief — the Python agent scaffold layer

> Capability-level summary per the exposure ruling in `README.md`. The repo name, module
> names, and code specifics are deliberately omitted.

## Positioning note — read this first

This layer must be presented honestly: it is a **deliberately small, teaching-grade
scaffold, frozen by design** — not a production automation engine. Its own documentation
says so twice ("a starter scaffold, not a finished product… built to teach you the moving
pieces while giving you real working code to build on"). Roughly 600 lines, built in a
day, corrected from real use within hours, wired into the governance system two weeks
later, and then left alone — because the *ideas* worked out in its code graduated upward
into workspace-wide policy and skills. The case study should claim exactly that: this is
where the primitives were proven in code, and the living system moved to the governance
layers. A version of the story that casts it as the live automation engine would be
making a claim the artifact cannot support.

## Purpose

Notion ships its own AI. This layer exists to answer *why build your own agent instead*:
because you then own the model routing, the cost visibility, the tool boundary, and the
ability to replicate the setup per client — none of which a vendor-hosted assistant
gives you. It is a working Claude-powered agent that creates and manages projects and
tasks in a Notion workspace and reasons about team workload, written so that a competent
non-specialist can read every moving piece: API keys, tool use, token tracking, model
routing.

## What it does (capabilities)

- **A conversational agent loop** — the human types, the model reasons, and when it needs
  to act it requests one of a fixed set of named tools; the code executes the tool and
  hands the result back. The agent's own documentation demystifies it: *"This is the
  entire mechanism behind 'agents' — there's no magic beyond this request/execute/respond
  loop."* The model never touches Notion directly; every action passes through a
  code-owned boundary.
- **Five tools, all constructive or read-only:** create a project; create a task; list
  team members (so work can be assigned to a name instead of a copied ID); read a
  database's schema before acting; and query tasks with arbitrary filters — the read
  path behind every workload question ("who's overloaded," "what's due this week").
- **Zero destructive tools — by design, stated three times.** There is no delete and no
  update. The documented condition for ever adding one: a confirmation step **in code,
  not just in the prompt**.
- **Two-model cost routing.** Routine create/read turns run on a fast, inexpensive
  model; messages showing reasoning signals (workload, priorities, dependencies,
  trade-offs, bottlenecks) escalate to a stronger one. The routing is deliberately a
  simple heuristic, with the rationale recorded: using an LLM to decide which LLM to use
  would spend tokens to save tokens. The top-priced tier is deliberately ruled out — this
  job doesn't need frontier reasoning, and the cost difference is real.
- **Per-turn cost telemetry.** The chosen model is printed *before* every call, and
  cumulative token usage after every turn — with the standing instruction to sanity-check
  the in-session numbers against the vendor's billing dashboard, which is named as the
  ground truth. "Don't fly blind on usage-based billing."

## Theme material — AI supervision and transparency

- **Prompts express intent; code enforces it.** The scaffold's three gates sit at three
  deliberate strengths, and the documentation knows they differ: structural (no
  destructive tool exists — the model *cannot* destroy data), prompt-level (summarize
  before creating more than two items and give the human a chance to object — labeled as
  the weakest kind), and rate-limiting (a hard cap on response size, called out as the
  guard against accidental overspend).
- **Anti-hallucination guards live where the model actually reads them.** A task with no
  due date gets a sensible default with the schema text saying *do not guess one
  yourself*; priority stays unset with the schema text saying *do not default to
  Medium*. Two opposite defaults, each chosen deliberately — a blank due date is useless,
  a guessed priority is worse than none.
- **The durable audit trail is the system of record itself.** Every create returns the
  new page's URL — a clickable artifact a human can go verify — and the platform's own
  authorship fields and page history record the change permanently.
- **Attribution runs to the model level.** The layer's own git history co-credits the
  specific AI models that worked on it by name and version — and even a small
  documentation change went through branch → PR → merge under the GitHub operations
  layer's rules. The governance applied to itself.

## Theme material — security and confidentiality

- **Secrets never touch the code.** All credentials live in an environment file that is
  ignored by version control, read through a single documented chokepoint, with a
  placeholder example file shipped instead. The stated reason is a *business* property,
  not just hygiene: this is what lets you hand the project to a client, or publish it,
  without leaking credentials.
- **Least privilege at the platform boundary.** The setup guide prescribes granting the
  integration only the capabilities it needs and declining user-PII access it doesn't.
  It names the platform's sharing model as the main safety boundary — the agent can see
  nothing until a human explicitly shares specific databases with it — and treats that
  boundary as a feature to lean on, enforced server-side rather than by this code.
- **Blast-radius narrowing beneath the token's scope.** The integration token could
  update pages; the code exposes no tool that does. If the model misbehaves, the
  credential can create and read, not destroy or overwrite — defense in depth in the
  correct direction.
- **What leaves the machine is enumerated**: conversation and tool results to the model
  vendor (meaning queried workspace content enters model context — stated, not hidden),
  page operations to the platform, nothing else; three dependencies, no telemetry, no
  third parties.
- **Sandbox-first sequencing.** Before touching anything real: point the agent at a
  throwaway workspace with test databases, watch it behave, *and only then* aim it at
  anything resembling client data. Client-data protection expressed as ordering, which
  is a stronger control than a policy sentence.
- **Known gaps are disclosed in place** — no retry/backoff for platform rate limits, no
  cap on the tool loop, per-client isolation only as strong as separate config files —
  each recorded as a stated limitation with the recommended fix.

## Theme material — intuitive setup with flexibility

- **Setup is six numbered steps, each with its reason attached** — including the one
  disambiguation most guides omit (an API key is not a chat subscription; it bills by
  usage) and a step that names the single most common first bug (property names must
  match your real schema) *before* it happens.
- **Error messages teach.** The one hard failure in the scaffold tells you the fix and
  where to read more, instead of printing a stack trace.
- **Replication is configuration, not code.** The closing thesis of the setup docs: once
  the pattern works for one client, **a new client is a new config file and new database
  IDs, not new code**.
- **The next decisions ship alongside the current ones** — where to refine the routing
  signals, how to add a delete tool safely, which optimization to wire next (prompt
  caching, deliberately deferred until the basic loop is proven) — so the scaffold
  teaches judgment, not just mechanics.

## Real numbers (measured 2026-08-13; re-verify at write time)

- **~600** lines total, roughly two-fifths of it documentation; **5** tools exposed to
  the model; **0** destructive tools; **2** models routed between; **3** runtime
  dependencies; **4** environment variables.
- **3** commits across **14 days** (2026-07-02 → 2026-07-16), then deliberately frozen.
- Docs-first from day zero: the first commit already carried ~200 lines of setup and
  strategy documentation against ~370 of code.

## Evolution highlights

- **Hours-later correction from real use.** The only behavioral change the scaffold ever
  received came ten hours after the initial build, and it is precisely the shape of a
  lesson learned by using the thing: default the due date, never default the priority —
  pushed into the tool schema text the model actually reads. Twelve days later the same
  judgment reappears one layer up as workspace-wide policy ("never infer priority").
  The clearest single trace of an idea being proven in code and then graduating into
  governance.
- **Day 14: subordination.** The final change added the standard governance pointer
  file — repo pin, links to both SOP layers, "nothing here overrides them" — turning a
  standalone project into a governed node of the system. Even that docs-only change went
  through a reviewed PR.
- **A disclosed-by-design divergence.** The scaffold's property names predate the
  workspace SOP and were never updated to it; its own docs warn in two places that
  property names must match your real schema, and its governance file says the live
  workspace is authoritative. Honest — but it means the scaffold as committed would need
  its property strings edited before running against the current workspace. The case
  study must not imply otherwise.
