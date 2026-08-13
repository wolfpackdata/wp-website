# Wolfpack AI Command — planning folder

Working documents for the case study on **Wolfpack AI Command** — the
integrated Notion + GitHub + Claude + Codex + Python operating system Ry built and runs
his project work through. The case study presents the system to three audiences at once,
with **hiring companies leading the framing** (Ry's ruling, 2026-08-13), and potential
system buyers and project clients reading along.

`planning/` never deploys (standard `case_studies/` convention), but **this repo is
public**, so everything in this folder is written to be world-readable.

## Exposure stance (Ry's ruling, 2026-08-13): capabilities, not internals

The system spans three private repositories. These briefs describe **what each layer does
and its shape** — capabilities, design principles, real counts, and the evolution story —
and deliberately omit:

- private repository names and file paths
- code specifics (module names, constants, schemas)
- internal document trees and skill slugs
- Notion workspace identifiers, database/template IDs, account names and emails
- issue/PR numbers internal to the private repos

Where a distinctive named detail would make the case study copy better (for example, the
AI's dedicated workspace account name), the brief says so generically and the decision to
name it on the page is left to Ry.

## Files

| File | What it is |
|---|---|
| `brief-github-ops-layer.md` | The layer that governs how code work happens: branching, review gates, labels, versioning, releases, and the skills that carry those rules into AI sessions. |
| `brief-notion-governance-layer.md` | The layer that governs the Notion workspace: databases, templates, interlinking, the AI's identity and provenance system, the status lifecycle, and the published rulebook every surface reads. |
| `brief-agent-scaffold-layer.md` | The Python agent layer: a deliberately small, teaching-grade scaffold where the primitives (tool boundaries, model routing, cost telemetry, secret hygiene) were worked out in real code. |
| `outline.md` | The case study outline: framing, part-by-part structure, themes, evidence rules, figure candidates, decisions ledger, and open questions for Ry. |

## Standing rulings for this case study (Ry, 2026-08-13)

1. **Audience:** bosses (hiring companies) lead; buyers and clients read along.
2. **Exposure:** capabilities, not internals (see above).
3. **Name:** **Wolfpack AI Command** — the official client-facing name (Ry,
   2026-08-13, renaming the earlier working title *Notion AI Command*). In the case
   study's copy the name is **rationed, not repeated** — see D-011 in `outline.md`.
4. **Evidence:** the <50% startup project-completion figure (attributed plainly to Ry's
   own client history), real artifact counts pulled from the repos and workspace at write
   time, and the 20-years-of-coding/GitHub/PM background. **No results section** — Ry did
   not grant the own-system exception.
5. **Genre:** not a how-to. The story of why the system is necessary and the approach —
   built by heavy use of the system on itself, refined continuously, over a foundation of
   20 years of practice.
6. **Audience breadth:** the piece speaks to SMBs, startups, and solopreneur developers
   alike — never startup-specific. The <50% figure keeps its startups-only attribution
   (the measured population); the pattern around it is drawn at every scale (D-012).
7. **PM stance:** the system **empowers project managers, it does not replace them** — a
   working PM should read the case study and want it; copy must never imply role
   elimination or a headcount saving (D-013).
8. **Content requirement:** the piece shows two-surface auditability — AI work easy to
   audit, trace, correct, and revert from *either* GitHub or Notion, because the two are
   interconnected — and carries the honest revert story: the gates stop most mistakes
   before they ship, and when volume makes a revert necessary, it is "a prompt away"
   (D-014).
9. **Icon placeholders:** wherever the page discusses the visual system (per-database
   icons, the color legend), it carries placeholder icon chips for visual interest —
   shipping neutral until Ry rules on whether the semantic icon colors may appear as
   figure content under the sheet's no-new-hues rule (D-015).
10. **Closing plug + CTA:** the piece ends on a brief product plug (integration takes
    hours, not days; the upgraded Notion system develops safely in parallel, isolated
    from the existing PM system) followed by the 30-minute intro-call CTA — one
    destination, book-first (D-016, resolving D-008). The nav CTA button stays as site
    chrome; the body carries no CTA before the close (D-017).
11. **Timeline:** dated from **November 2025**, when Ry started work on the system; the
    versioned repos (from July 2026) formalized the already-running practice (D-007).
12. **Named specifics:** the AI account's display name and Ry's verbatim icon-color
    rationales may appear on the page — a scoped exception to the exposure stance;
    everything else stays sanitized (D-010).
