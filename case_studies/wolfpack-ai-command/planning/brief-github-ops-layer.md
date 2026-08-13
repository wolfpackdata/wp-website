# Brief — the GitHub operations layer

> Capability-level summary per the exposure ruling in `README.md`. Private repo names,
> file paths, and internal doc structure are deliberately omitted.

## Purpose

The rules that govern how code work happens across Ry's repositories originally lived as
always-on AI instructions — unversioned, un-reviewable, and loaded into every session
whether relevant or not. This layer extracts them into a **standalone, versioned standard
operating procedure**: documentation that is read and refined in one place, follows its
own rules (the SOP repo is governed by the SOP), and is compiled into **on-demand AI
skills** that load only when a session actually touches git or GitHub.

The founding bug is instructive and the SOP records it plainly: an AI session working in
one repository with a subfolder selected inferred the repository name from the folder
name — the most salient string in context — and filed an issue against a repository that
does not exist. The first rule of the whole layer came out of that failure: **resolve the
repository from git; never guess.** Everything else accreted around that fix.

## What it does (capabilities)

**Three AI skills** render the SOP operational:

1. **End-to-end git/GitHub operations** — branch naming, commits, pull requests, merges,
   labeling, versioning, and releases, with a preflight that resolves the target
   repository from git before any operation. Ends with an explicit "never do" list.
2. **Issue filing that stops** — files exactly one well-formed, correctly-labeled issue
   and then stops. "New issue" is encoded as *create and stop*: no branch, no code, no PR
   unless explicitly told to proceed. Filing an issue must never quietly become
   implementing it.
3. **New-repository bootstrap** — stamps a new repo with the standard operating files
   from a canonical template, copied verbatim rather than retyped from memory, validating
   embedded links before committing and refusing to invent a project description.

**Runbooks** cover the human-facing procedures: bootstrapping a repository (branch
protection, merge settings, label taxonomy), running a multi-issue fix round end to end,
promoting a release, and setting up a new machine so a second workstation reproduces the
same environment from pointers rather than copies.

## Design principles

- **A defined precedence chain.** A repository's own instructions beat the SOP; the SOP
  beats global AI instructions. Stated everywhere, so no session has to guess which rule
  wins.
- **Two branching profiles, right-sized ceremony.** A full release-train profile
  (permanent integration and release branches, one issue → one branch → one PR) and a
  documented lighter profile — plus two *audited* carve-outs (trivial edits, emergency
  hotfixes) so the process doesn't accrete silent workarounds.
- **Merge method is semantic, not stylistic.** Squash-merges into the integration branch
  keep one line per change; release merges use a true merge commit, with the ancestry
  reasoning written out (a squashed release makes version tags unreachable from the
  release branch's history).
- **Merged is not accepted.** Every issue whose fix lands on the integration branch is
  labeled into a visible **human verification queue**. Two queries become exact: the true
  backlog, and the list of things awaiting the owner's verification against real data.
  Auto-closing keywords are banned everywhere so that closing an issue is always a human
  decision.
- **Versioning separates cadence from magnitude.** A round of work *triggers* a version
  bump; the highest-impact change in the round *sizes* it. No bump ever happens without
  the owner's explicit confirmation, and the changelog updates in the same PR as the
  version strings so the two can never drift.
- **Pointers, not copies.** Skills are linked into the machine from the repo rather than
  copied; cross-references link to the canonical document rather than restating it;
  syncing a second machine is `git pull`, not file copying. The most-repeated meta-rule
  in the layer.

## Theme material — AI supervision and transparency

This layer's strongest seam. Nearly every rule is a mechanism for keeping a human
meaningfully in charge of AI-executed work:

- **The review split by destination is the supervision model.** Into the integration
  branch: the AI self-merges with no pre-merge review — an explicit, named small-team
  speed tradeoff — compensated by a mandatory local-verification gate (test output pasted
  into the PR, not a checkbox), post-merge human review, and the verification-queue
  label. Into the release branch: **external review before merge, never self-merged.**
  Branch protection encodes the split numerically.
- **Risk-tiered override.** Authentication, data-migration, security, and release
  changes require human review before merge regardless of profile.
- **Human-gated decisions are enumerated, not implied:** the round boundary, every
  version bump, closing any issue, the release sign-off, and the post-release close-out
  are all decisions the AI must bring to the owner. Never automatic.
- **Cross-model review.** A second AI vendor's model was used to review the SOP and the
  live skills; its raw findings, the reconciliation of each finding, and the
  executed-versus-deferred split are all committed. The system's own orchestration
  protocol generalizes the principle: verify with a *different* agent than the one that
  did the work — implementers don't sign off on themselves.
- **Waivers are recorded, not hidden.** The one release that shipped with its external
  review gate waived says so in the changelog — by whom, why, and with the gate
  re-affirmed for next time.
- **Evidence, not assertion.** "Done" means demonstrated with pasted output. The
  machine-verification procedure states the philosophy outright: a setup that reports
  green while something is broken is worse than one that fails loudly.

## Theme material — security and confidentiality

- **Three-layer review retention.** Application repos carry only sanitized release-level
  summaries; the full evidence pack lives in a private archive indefinitely;
  temporary quarantine material ages out on a schedule. Security-sensitive detail stays
  private until fixed.
- **An explicit never-commit list**, including copied production or test data and
  secret-bearing logs. The commit SHA is the canonical source snapshot, so no source
  copies need retaining.
- **3-2-1 backups with tested restoration** — folder synchronization alone is recorded as
  insufficient.
- **Portable configuration carries no secrets.** Machine setup ships pointers and
  settings that are portable precisely because credentials, tokens, and
  machine-bound state are never copied between machines.
- **The silent-misattribution threat is named and countered.** Re-authorizing the
  workspace connector while the browser is signed in as the human silently rebinds the
  AI's writes to the human's identity — and reports success. The countermeasures:
  a deliberate no-browser authorization flow, and a mandatory identity check before any
  write (detailed in the Notion governance brief).
- **Two hard stops in the AI's standing configuration:** never execute commands on any
  machine other than the one the session runs on (phrased machine-neutrally so it cannot
  evaporate by rewording), and never write outside the working repository by default —
  "tool capability is not authorization."
- **Known gaps are recorded as open items**, not papered over: a dedicated secrets rule,
  code ownership, and dependency scanning are logged as deferred work.

## Theme material — intuitive setup with flexibility

- A new repository is bootstrapped in ten copy-paste steps ending in an eight-item
  checklist; labels are applied by an idempotent script; PR and issue templates pre-fill
  the conventions so the correct shape is the default shape.
- A new machine is set up from a preflight checklist plus three paste-in prompts, the
  last of which is a verification pass with an explicit instruction not to fix silently:
  the owner wants to see the failure before it's papered over.
- Two branching profiles plus documented carve-outs mean the ceremony scales to the work
  instead of the work bending to the ceremony.

## Real numbers (measured 2026-08-13; re-verify at write time)

- **3** AI skills; **8** numbered SOP topic documents; **3** runbooks plus a multi-file
  machine-setup procedure; **23** documents in the SOP tree overall.
- **16** commits over **24 days** (first commit 2026-07-10), one tagged **v1.0.0**
  release (2026-07-30), every commit following the layer's own commit convention.
- External cross-model review: **7 findings, 7 corrections applied the same day**, plus
  8 deferred hardening items still tracked as open.

## Evolution highlights (mistakes that became rules)

| What happened | What it became |
|---|---|
| AI inferred a repo name from a folder name and filed an issue against a nonexistent repo | The founding rule: resolve from git, never guess — now a preflight in two skills |
| The first skills were written outside version control and were lost — unrecoverable on any machine, and already stale against the docs | Skills version with the SOP they render; machines link to the repo rather than holding copies |
| A second machine's copied skills silently fell weeks behind — running an outdated rule with no symptom | Junction-links only; a machine-setup verification pass that treats drift as a reportable failure |
| Release squash-merge made version tags unreachable from the release branch | Release merges use true merge commits, with the ancestry reasoning documented |
| One flat "patch bump per round" rule conflated how often to version with how much changed | Round triggers the bump; highest-impact change sizes it |
| A stale machine-specific "fact" (a clock offset) nearly skewed every timestamp | Machine-local facts are measured per box and can no longer be inherited from another machine's file |

The SOP also self-corrects against its own dogfooding: when the repo caught itself
legitimately violating its own ceremony, the violation became a documented lighter
profile instead of a hidden exception. Planning documents keep their reasoning trail —
superseded decisions are struck through with dated explanations, not deleted.
