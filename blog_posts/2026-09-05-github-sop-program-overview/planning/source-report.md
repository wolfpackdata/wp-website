# The Wolfpack GitHub SOP — Program Overview

**What it is:** a standard operating procedure that governs every git and GitHub action across
Wolfpack's 36 repositories — written for a team in which most of the commits are made by AI
agents, and designed so that a person can still tell, months later, exactly what happened and
who decided it.

**Status:** current release **v1.4.0** (2026-09-04). This overview was written during the
**v1.5.0** round, which is structural cleanup rather than new rules. Source of truth:
[`wolfpackdata/wp-github-sop`](https://github.com/wolfpackdata/wp-github-sop).

**Who this is for:** technical partners and clients who want to understand how AI-assisted
delivery is controlled here before trusting it with their codebase.

---

## Part I — The SOP

### The problem it solves

An AI agent can open, implement, review, and merge a pull request in the time it takes a person
to read the diff. That speed is only useful if three things stay true: work is **attributable**
to a named actor, changes are **reversible**, and the rules an agent follows are the same rules
on every machine and in every session. Ordinary process documents fail all three the moment an
agent is faster than the person reading them, because a document nobody re-reads is a
suggestion.

So this SOP is not only written down. It is **loaded into the agent, guarded in the session,
checked on the forge, and enforced by branch rulesets** — four layers, each catching what the
one before it cannot.

### The flow, in one line

**Issue → branch → pull request → (AI review, where the change is risky) → squash-merge into
`develop` → label the issue → release `develop` → `main`, tagged `vX.Y.Z`.**

Nothing is committed directly to `main` or `develop`. Issues are never auto-closed by a merge —
the person who reported an issue verifies it and closes it, which keeps "fixed" and "verified"
as two separate facts.

### The ten rules

| # | Topic | Why it exists |
|---|---|---|
| 01 | [Branch model](sop/01-branch-model.md) | `main` is always releasable, `develop` integrates. One issue → one branch → one PR, so history reads as a sequence of decisions rather than a stream of edits. |
| 02 | [Commits & PRs](sop/02-commits-and-prs.md) | Conventional Commits with an area scope, squash-merge, and one inexpensive CI gate wherever a repo has something to run — a reproducible check, not a claim in a PR body. |
| 03 | [Issues & labels](sop/03-issues-and-labels.md) | Issues stay open until verified. `fixed-on-develop` splits the backlog from the verification queue so both queries are exact and neither silently grows. |
| 04 | [Versioning & changelog](sop/04-versioning-and-changelog.md) | SemVer. A round of work triggers a bump; the highest-impact change in it sizes the bump; only the Admin confirms it. Every release carries a changelog entry and a round report. |
| 05 | [Development timeline](sop/05-development-timeline.md) | An optional append-only project log — management history, deliberately separate from documentation. |
| 06 | [Resolving the repo](sop/06-repo-resolution.md) | The target repository is read from git, never inferred from a folder name. This single rule prevents the most common cross-repo mistake an agent makes. |
| 07 | [SOP cross-links](sop/07-sop-cross-links.md) | Every repo embeds links back to both SOPs, so a session started anywhere can reach the rules. |
| 08 | [Code-review retention](sop/08-code-review-retention.md) | Review evidence is retained in three layers with different lifetimes: the application repo gets a sanitized summary, a private archive keeps the full pack, quarantine expires. |
| 09 | [Roles & permissions](sop/09-roles-and-permissions.md) | Rules name **roles**, not people, so they survive staffing changes and apply identically to humans and agents. |
| 10 | [AI review](sop/10-ai-review.md) | When an independent AI review is required rather than advisory, the P0–P3 severity rubric, what "passed" means, and the file-based handoff between the two AI halves. |

### Who may do what

| Role | Held by | Distinguishing power |
|---|---|---|
| **Admin** | The org owner (one person) | The only role that approves and merges into `main`, confirms every version bump, and may close any issue. |
| **Maintainer** | A trusted human | Merges into `develop`, sets round boundaries, writes round reports, proposes bumps. |
| **Contributor** | Anyone else with access | Files issues, opens PRs, verifies and closes what they reported. |
| **AI Reviewer** | Codex, as its own GitHub account `main-wolfpack` (triage permission, every comment prefixed `[codex]`) | Performs the pre-merge review for risky changes and submits it as a verdict. Its approval never satisfies the `main` gate. |
| **AI Implementer** | Claude Code, running under a human's own GitHub identity | Opens PRs and self-merges them into `develop` for the Maintainer. Never merges to `main`, never closes an issue, never bumps a version unconfirmed. |

Two more roles appear throughout: the **Requester** (who asked for the work) and the **Reporter**
(who filed the issue, and therefore verifies it).

The critical structural choice is that **the reviewer and the implementer are different
accounts, on different models, in different repositories.** The same session can never both
write the code and sign it off.

### Where a review is required

An independent AI review is mandatory before merge when a change touches any of six risk tiers:
**authentication, data migration, security, release tooling, CI / rulesets / repository
configuration, and the SOP or skills that other agents obey.** Everything else self-merges after
its local and CI gates. Every release pull request into `main` takes the review regardless of
what it contains.

### The skills — the SOP as agent behavior

Skills are the operational rendering of the rules: they load automatically when a session
touches the relevant work, so an agent follows the SOP without anyone pasting it in. They are
**linked, never copied**, into each machine's agent directory — a copy rots, a link keeps every
machine in lockstep through `git pull`.

| Skill | What it does | Why it exists |
|---|---|---|
| `github-gitflow` | Branch, commit, PR, review, merge, label, version, release | The operational reference for all git work, so no session invents its own procedure. |
| `create-github-issue` | Files one well-formed, correctly-labeled, reviewable issue | An issue a reviewer can check a PR against and a reporter can close against — and it stops after filing, so "file this" never silently becomes "and implement it". |
| `new-repo-bootstrap` | Installs `CLAUDE.md`, `AGENTS.md` and `CODEOWNERS` from verbatim templates | A new repository is never born blank or half-governed; the files are copied, never reconstructed from memory. |
| `codex-review-response` | The implementer's half of the review loop: verify each finding, record a disposition, answer on the pull request | Keeps the model being critiqued from quietly dismissing findings, and keeps the two halves of the review in separate repositories. |
| `wp-independent-review` *(sibling repo)* | The reviewer's half: run the review, submit the verdict | Deliberately not co-located with the response skill, so one session cannot hold both. |

### The hooks — guardrails inside the session

Hooks catch the class of mistake that is **invisible until after it lands**. They are
model-neutral scripts with thin per-model adapters, so Claude and Codex are bound by the same
guardrail rather than by two copies that drift. They are forcing functions, not security
boundaries — the honest claim is that they turn "remember to check" into "the call does not go
through until you have".

| Hook | Refuses | The failure it is built for |
|---|---|---|
| **Branch guard** | `git commit` / `git push` targeting `main` or `develop` | The forge rejects the *push* — by which time the commits already exist on the wrong branch and have to be moved. |
| **Notion identity gate** | A Notion write until the session has proved it is acting as the AI's own account | Authorship metadata is system-managed and **cannot be corrected afterwards**. |
| **GitHub identity gate** | A state-changing `gh` call or `git push` under the wrong credential, in **both** directions | A write under the reviewer's identity destroys the review loop's whole premise: two distinct authors. |
| **Session preflight** | Nothing — it never refuses | Publishes the session id and states what the session still owes, so the gates above are opened deliberately rather than by accident. |

The identity gates **fail closed**: if they cannot tell who is acting, they refuse. The suite
ships with 67 fixture tests, four of which run live against the real accounts, because a
guardrail tested facing only one direction is half a guardrail.

### The automation on GitHub

| Mechanism | What it does | Why |
|---|---|---|
| **`sop-main` / `sop-develop` rulesets** (organization-level) | Pull requests required; `main` needs one Code Owner approval, merge-commit only, no force-push; `develop` is squash-only | The forge, not agent memory, is what actually blocks a bad merge. Organization-level means one place to change and 36 repositories affected. |
| **AI-review gate** (reusable workflow) | Blocks a merge while `needs-ai-review` is set, and turns that label into a review request automatically | Requesting the review used to depend on a second manual flag whose omission failed in the quietest possible way: the gate still blocked, the PR still looked correct, and the review was simply never assigned. |
| **`fixed-on-develop` labeler** | Labels every issue a merged pull request references | The verification-queue invariant is enforced by a workflow instead of by an agent remembering. |
| **Weekly fleet audit** | Audits every repository for baseline drift and keeps exactly one issue — opened on drift, rewritten in place, closed by the first clean run | **A clean fleet is silent.** A weekly "all clear" is right 51 weeks a year and trains its reader to close the 52nd unread. |
| **Script self-tests (CI)** | Runs the scripts' self-tests on every pull request | Added after a defect proved that a self-test nothing invokes is a self-test that does not exist. |
| **Label set** | `fixed-on-develop`, `critical`, `codex-review`, `needs-ai-review`, `sop-fanout`, plus `bug` / `enhancement` / `documentation` | Each label is a queue with a named owner, not decoration. |
| **Issue and PR templates** | Served organization-wide from the `.github` repository | Acceptance criteria and a verification plan on every issue, so "done" is testable by someone other than the author. |

### The scripts

Nine executable pieces keep the fleet in the state the documents describe: label bootstrap,
organization-ruleset bootstrap, per-repository retrofit and fleet-wide retrofit, the read-only
fleet audit and the separate drift judgement (measurement and judgement are deliberately two
files, so the judgement can be tested against fixtures with no network and no credential), a
workflow-parity check, an internal documentation link checker, and the AI-review queue consumer.

### The written record

Rules live in `docs/sop/`. Everything else is history, kept separately and labelled as such:
**runbooks** for procedures (new-repo bootstrap, fix round, release, AI review, organization
migration, machine setup), **round reports** per version, **review evidence packs** per run, and
a root changelog. The separation is itself a rule — records never live where rules live, so a
reader can never mistake what happened once for what to do next.

---

## Part II — The last two weeks

Between 2026-08-22 and 2026-09-05 the SOP went from a written document to an enforced system.

| Release | Date | What it did |
|---|---|---|
| **v1.1.0** | 08-29 | Rewrote a one-person procedure into a small-team one: roles, the Admin-only `main` gate, the AI-review stage, reviewable issue and pull-request templates — then retrofitted that baseline across every repository by script. |
| **v1.2.0** | 08-31 | Closed the entire open backlog in one round (12 issues), most of them findings from an independent AI review of this repository itself, and made the round's own enforcement real: the review gate became a required check and the verification-queue invariant became a workflow. |
| **v1.2.1** | 09-01 | Closed the release-review findings and recorded the review. |
| **v1.3.0** | 09-03 | Made the AI Reviewer a real account with its own permissions and verdicts, and added the byte-identical fan-out rule so a 35-repository sweep inherits one review instead of queueing 35. |
| **v1.4.0** | 09-04 | Centralized the automation — one copy of each workflow, reached by 32 repositories through a pinned stub — plus organization-level rulesets, the weekly silent audit, the review loop's single trigger, and the session hooks. |

**By the numbers:** 82 pull requests merged, 55 issues closed, 10 open and triaged, four
releases, 36 repositories brought to one baseline, and every merge into `develop` since the
mid-round enforcement fix recording a clean ruleset result.

### How the work was divided

The division is the point, so it is worth stating plainly.

- **The Applied AI Engineer** set every boundary that mattered: what each round contained, when
  a version was confirmed, which of several proposed automation triggers was actually
  implemented (one), which findings were rulings rather than fixes, and every stop where the run
  paused for a decision — roughly a dozen named decision stops across the two weeks, each
  answered and recorded.
- **Claude Code**, as AI Implementer, did the drafting and the mechanical work: the documents,
  scripts, workflows, retrofits, reports and the responses to review findings — always under a
  human GitHub identity, never merging to `main`, never confirming its own version bump.
- **Codex**, as AI Reviewer, reviewed independently under its own account. In one round it
  raised 24 findings (14 of them P1) of which 23 were fixed; in the next, 29 findings, 24
  confirmed fixed by a returned verdict.

No agent graded its own homework at any point in the two weeks.

### What actually improved

- **Enforcement replaced etiquette.** Rules that used to live in a document an agent might read
  are now branch rulesets, required checks and session hooks. The difference is measurable: the
  ruleset result is recorded per merge.
- **One copy of everything.** Workflow logic lives in a single file that 32 repositories reach
  through an eleven-line stub pinned to a tag. Changing the fleet is one edit and a tag move,
  not a 32-repository sweep with 32 reviews.
- **Silence when healthy.** The weekly audit says nothing while the fleet is clean, which is
  what makes it worth reading when it speaks.
- **Two AI accounts, not one.** Implementation and review are separated by account, model,
  repository and skill — the property that makes an AI-reviewed merge mean anything at all.

### What went wrong, and is on the record

Three items are worth naming, because a process document that records only successes is not
evidence of anything.

1. **The merge gate had not been enforcing.** Mid-round it emerged that the required check could
   be satisfied in a way that let merges through; seven merges record a bypass. The fix landed
   inside the same round and every merge after it records a clean pass. The round report leads
   with this rather than with a feature list.
2. **A release merged to `main` before its mandatory review existed.** It was raised as an
   issue, ruled on by the Admin, and recorded — not quietly corrected.
3. **A labeling workflow marked one issue as fixed that had only been referenced.** The
   convention gap is filed as an open issue rather than patched invisibly.

Each is a filed issue with a decision attached. That is the intended behavior of the system, not
an exception to it.

### What is next

**v1.5.0** is deliberately narrow: structural cleanup of the documents themselves — no new
rules, no new code, no skill changes. The remaining enforcement work, including the three gaps
above, is scheduled behind it as a separate round with its own boundary.

---

## Why this matters

For a partner evaluating AI-assisted delivery, the useful questions are not about model choice.
They are: *can you tell who did what, can you undo it, and does the process hold when nobody is
watching?* This SOP answers those with an attributable actor on every change, a reversible path
for every merge, an independent reviewer that is never the author, and enforcement that lives on
the forge rather than in anyone's memory — including a record of the times it failed and what
was done about it.
