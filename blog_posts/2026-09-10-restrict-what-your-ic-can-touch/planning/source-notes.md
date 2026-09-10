# Source notes — How to Restrict What Your IC Can Touch

Ry's prompt, 2026-09-10, cleaned. This post was **written by Claude in the same session**,
at Ry's direction, rather than briefed to a copywriter — see `workflow.md` for how that
departs from the standard Phase 1.

## The ask

- Subject: *How to Restrict What Your IC Can Touch.* IC = **independent contractor**, and
  the post treats an AI coding agent as one too (Ry, answer 1).
- Reader: a founder or CEO of a technical company who is **not** an engineer. The
  engineering mechanism is named at a high level, one level below each plain-language point.
- First person, as the contractor who insists on being locked out (answer 2).
- Under 1,500 words (answer 5). American spelling throughout — Ry's explicit instruction.
- Must mention: GitHub branch rulesets; sandbox repositories; client-owned data accounts
  with IC access granted; GitHub PATs; development (non-production) databases; robust SOPs
  for AI to obey guardrails. Claude was asked to research and add or prune against Ry's
  actual practice.
- Hero image generated programmatically, committed generator (answer 6).
- Links: the 30-minute intro call as the only CTA; the "New Clients" post; the GitHub SOP
  overview post *once it is live* (not live at push time, so not linked yet). No link to
  `/pilot-project/`, `/hire/`, or `/github/`. Tags from the existing Wix list (answer 7).

## What the research found in Ry's own practice (used as-is)

Sources: `wolfpackdata/wp-github-sop` (`docs/sop/09-roles-and-permissions.md`,
`docs/sop/10-ai-review.md`), `wp-codex-init` (`docs/07-reviewer-github-access.md`),
`wp-codex-sop` (`codex-home/AGENTS.md`, `hooks/`), `wp-bql` (`README.md`,
`docs/spec/04-client-onboarding.md`), `wp-notion-team` (`docs/notion-sop/`), and this repo's
`pilot-project/index.html` and the two previous posts. All private except this repo, so
the post names no file paths and links none of them.

- Two org-level rulesets (`sop-main`, `sop-develop`) covering every repo in the org.
  `sop-main`: one approving review, code-owner review required, merge commit only, a
  required "needs-ai-review must be clear" check, no deletion, no force-push. `sop-develop`:
  PR required, zero approvals, squash only. Bypass: org admin, pull-request mode only,
  recorded.
- CODEOWNERS is one line naming the Admin, in every repo, never inherited.
- The AI Reviewer (Codex, `main-wolfpack`) sits on team `ai-reviewers` with **triage** — the
  least role that can post a review. May never push, merge, change settings, hold admin,
  sit on a bypass list, appear in CODEOWNERS, or close an issue. Prefixes everything with
  `[codex]`. Its only writable location is its run folder; a write elsewhere fails rather
  than prompting.
- The AI Implementer has no identity of its own; it carries the human's permissions.
- Reviewer PAT: fine-grained, four permissions (Contents read; PRs read/write; Issues
  read/write; Metadata read), expiring, stored in the user profile outside every repo.
  The audit PAT is the one with a 30-day expiry-warning issue. Two documented exposures,
  both rotated first (#19 and #39 in `wp-codex-init`; the post names neither).
- Secrets rule: none in issues, PRs, commits, logs, Notion, or AI prompts; `.env`
  git-ignored from bootstrap; rotate first, paperwork second; a leak is `critical`.
- Client data: provisioned inside the client's own Google Cloud project; consultant is a
  guest via `roles/iam.serviceAccountTokenCreator` on one service account; no key files
  ever; revocation is deleting one binding, in under a minute, alone. Roles refused by
  name: `bigquery.admin`, `resourcemanager.projectIamAdmin`, `storage.admin`, domain-wide
  delegation.
- `bql apply` is a dry run by default; `--offline` swaps in an in-memory stand-in.
- Five numbered hard stops in `AGENTS.md` / `CLAUDE.md`: local machine only; never write
  outside the working directory; never commit or merge to `main`; never write to Notion as
  anyone but Main; never bump a version without the Admin, and never close an issue.
  "Reaffirming the request does not unlock these."
- Hooks: branch guard, Notion identity gate, GitHub identity gate, session preflight.
  Described in the SOP as forcing functions, not security boundaries.
- Client-side guidance already published in the "New Clients" post: create an account for
  the AI as for a new employee; read-only where appropriate; restrict to what it needs.

## Not in Ry's practice — kept as general advice by Ry's call (answer 3, option A)

- A contractor sandbox / template repository convention. What exists is a rollout canary
  repo and a bootstrap skill that stamps every new repo with its rulebooks.
- Dev vs prod databases. BQL layers are by stage (`_raw`, `_staging`, `_intermediate`,
  `_marts`), not by environment; there is a per-process test instance and a dry-run default.

The post frames both as "what to ask for" and says only that "in my own tools" writes are
dry runs by default, which is true.

## Accuracy notes on the copy

- "A reminder opens thirty days before expiry" is scoped to "the tokens my automation
  depends on" because it is the audit token that carries the warning issue, not the
  reviewer PAT.
- "Both times it was rotated before anything else" follows the SOP's "rotation first,
  paperwork second" and invents no timing.
- No file paths, issue numbers, ruleset ids, or account names appear in the post.
