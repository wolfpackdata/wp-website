# Changelog — résumé builds

Newest first. One version per round, both résumés
([Keep a Changelog](https://keepachangelog.com), [SemVer](https://semver.org)).
The round plan for each major lives in `docs/`.

## [2.4] — 2026-07-31

The music facts, corrected. The `hire/` landing pages fixed these across their
feedback rounds 2 and 3 and the YAML was left behind, so the `.docx` and `.pdf`
the pages offered for download contradicted the page offering them
([#77](https://github.com/wolfpackdata/wp-website/issues/77), refs
[#76](https://github.com/wolfpackdata/wp-website/issues/76)). Nothing failed
while that was true — `verify_facts.py` reads the YAML, not the pages — which is
the whole reason it needed a task instead of a red build.

### Changed

- **"A 36-year music career" is retired** (D-009). It collapsed four different
  spans into one number, and the one it picked was the study span. Summary ¶1 on
  eng-music now reads *36 years at the piano and 23 years paid to perform …
  professional DJ work since 2009*, verbatim from the landing page.
- **"20+ years of DJ performance" → "professional DJ since 2009"** in the Music
  section's `closing:` strip — the old figure was four years early — and the
  strip gains *23 years paid to perform, since 2003*.
- `FIGURES` re-annotated so the retired readings can't come back quietly:
  `"36 years"` is now *a practice span, never a career span* and `"20+ years"` no
  longer claims DJ performance.

### Added

- **The training, on both résumés** (D-010): ten years of classical piano study
  with a university professor, and sound engineering and composition learned
  through mentors, online programs, and practice. Neither YAML had said any of
  it, which left the résumé the last artifact reading as though the music were
  self-taught. eng-only's Education panel carries the spans too, because it is
  the only place music appears on that page; eng-music's leaves them to the
  Music section a page above.
- `FIGURES` rows for `23 years`, `10 years`, and `2003`.
- **Two `SHARED` rows guarding the training sentences.** They are Ry's wording,
  used verbatim on both résumés and both landing pages. Check 3 now fails if one
  side is edited alone — the same class of silent drift this round existed to
  clean up.

### Measured

Not re-measured in Word. Net change is roughly a paragraph added to each
Education section.

## [2.3] — 2026-07-31

Content-only round: Ry's correction to how the AI Dev Command Center is
described. Same edit landed on the two `hire/` landing pages in the same commit,
so the résumés and the public pages keep saying the same thing about it.

### Changed

- The **Notion–GitHub AI Dev Command Center** portfolio entry and the matching
  Wolfpack bullet now name the system's **Python engine** and list **OpenAI
  Codex** and **BigQuery** alongside Claude Code, GitHub, and Notion. The
  pipeline was understated before — it read as three SaaS tools wired together
  rather than a system with something running it.
- *"human + agent software development at speed"* → **"at blistering speed"**.

No design, build, or fact-table changes.

## [2.2] — 2026-07-30

Triggered by an outside review of the eng-only résumé, which called the image
banner an ATS defect. Checked rather than assumed, and it was right.

### Changed

- **The header is plain text on every build. The image banner is gone.**

  Extracting `word/document.xml` from the v2.1 build showed the first parseable
  string in the document was `Professional Summary`. Name, email, LinkedIn,
  GitHub, location — all pixels, none of it in the text stream. An ATS reading
  it files a résumé with no candidate name and no way to make contact. That had
  been true since v1.

  A text header already existed behind `--header text`, documented for online
  applications. Ry's call: make it the only header. The old split depended on
  choosing the right export every time and the cost of choosing wrong was
  total.

  Removed with it: `--header`, `--theme`, `--compact`, `brand.banner_path()`,
  the `WP Banner` style, and `meta.theme` / `meta.header` in the content files.
  The `resume_design` artboards and PNGs stay — they are the design record of
  the header, and `verify_facts.py` check 4 still holds them to the shipped
  strings.

  Cost: the navy field, the wolf mark, and the RML mark are off the résumé.
  `header-footer-spec.md` §9 keeps the one option that puts a mark back without
  reopening the problem.

- Summary drops **"and pursuing formal technical training"** on both résumés. It
  was the weakest clause on the page — a candidate with 17 years of leadership
  saying he is in training invites a question the rest of the document answers.
  The CCA-F line under Current Technical Focus stays; that placement reads as
  direction rather than as a gap.

- `METRICS.banner_space_after_pt` → `header_space_after_pt`.

### Added

- `verify_facts.py` **check 5**: the built `.docx` must yield the name and every
  contact detail as extractable text, and must open with the name. The only
  check that reads the artifact rather than the YAML, because this failure was
  invisible in the YAML — which is how it shipped three times. Verified against
  the v2.1 build: 7 errors, including *"does not open with the name — it opens
  'Professional Summary AI engineer, data s'"*.

### Measured

3 pages on both, ~2.64 (eng-music) and ~2.65 (eng-only) of ink, down from ~2.7 —
the text header is shorter than the 1.333in banner. File size ~130KB → ~41KB.

## [2.1] — 2026-07-30

### Added

- **eng-only: RML Creative LLC (2023–Present) as a brief Professional Experience
  entry**, sitting with Niceman at the foot of the work history.

  Ry asked whether a dedicated `PROFESSIONAL MUSICIAN EXPERIENCE` section at the
  end would help him stand out. Recommendation was no, and this is the
  alternative. The three things he wanted from it — the two-track reality, the
  multiple LLCs, and a reader googling RML and finding a real universe — were
  already two-thirds delivered by the Niceman entry and the piano line under
  Education. The genuinely missing piece was that **"RML Creative LLC" appeared
  nowhere on eng-only**, so the search hook did not exist.

  A section would have cost ~12 lines and changed how the document reads: a
  heading makes music a *category* of the candidacy, which invites the
  divided-attention question at exactly the companies eng-only targets. A
  work-history entry makes it a business he runs, which reads as range and
  ownership. Same facts, four lines, better framing.

- `verify_facts.py`: `RML Creative LLC` added to `SHARED`, so a reader searching
  it from either résumé lands on the same entity. Dropping it from one now fails
  the build.

### Measured

3 pages / ~2.7 of ink on both (eng-only up from ~2.6). Still inside tolerance.

## [2.0] — 2026-07-30

First round where content changes. Plan and rulings:
[`docs/v2-plan.md`](docs/v2-plan.md).

### Added

- `COO` in the banner title line on both résumés, matching how the public rates
  page introduces Ryan (C1).
- `github.com/wolfpackdata` in the banner contact line and the ATS text header —
  for an engineering application a GitHub URL is table stakes, and the résumé
  previously offered no way to see any code (C1).
- **Niceman Music Studio LLC (2009–2016) as a real entry**, filling the
  2012–2015 gap on eng-only (S5). Two facts new to both résumés, from Ry: the
  studio had **paying clients**, and his music was **published and licensed for
  use**. Framed as a built facility and a commercial business on eng-only; kept
  in the music section on eng-music.
- A Python/SQL bullet under Auto SOSS naming the proprietary pricing and
  inventory algorithms (C4). Ships the fuller wording — the systems behind
  catalog pricing and inventory decisions — because v0 already claimed "pricing
  intelligence" and "inventory management" on the same role; the languages are
  the only genuinely new claim.
- A `Quantitative Modeling & Forecasting` skill group, the financial-modeling
  through-line in the summary, and a financial-models clause in the Wolfpack
  bullets (C6).
- A Wolfpack bullet and a portfolio entry for the **Notion–GitHub AI Dev Command
  Center** (C5). Deliberately no self-declared "expert" anywhere — the claim is
  made with evidence instead.
- eng-music: an `Audio Data & Catalog Engineering` skill group — collection and
  metadata pipelines, name normalization, fuzzy matching, key/BPM analysis (S12).
- `closing:` on the `experience` section type, so the merged music section can
  end on one credentials line instead of needing a second heading for three
  facts.
- Version scaffolding: `VERSION`, versioned build filenames, `--release` for a
  clean `Ryan_Hickey_Resume.docx`, and the version in the docx properties.

### Changed

- **Selected AI Applications & Systems rebuilt** from the Q3 rates page portfolio
  and reordered for a hiring manager: money first, then the AI-native
  differentiator, then shipped applications by technical weight, then enablement
  (C2). Seven entries on eng-music, eight on eng-only.
- **SetMaster is now SetMaster 3**, not the retired VBA prototype — offline
  cross-platform application, TypeScript/React over a Python engine, packaged
  installers, v3.0.3 after three fix rounds (C2).
- `Shock Surplus` → **`Auto SOSS Inc. / Shock Surplus`** (C3).
- Selected Applications moved from last to directly after Experience (S1).
- Experience leads with Tromml, then reverse-chronological: Wolfpack, Auto SOSS,
  In4mation, (eng-only) Niceman (S2).
- `Active Development Areas & Continuing Education` → **`Current Technical
  Focus`**, six bullets to three, with all self-graded proficiency language cut
  (S3).
- Summary is two paragraphs in one voice; the first-person third paragraph and
  its unfalsifiable close are gone (S4).
- `14+ years leading` → **`17 years`** — In4mation starts 2009 (S6).
- eng-music: the two music sections merged into one, `Music & Creative
  Technology`, closing on a single credentials line (S9).
- eng-music: RML Creative and Niceman have role titles instead of rendering as
  bare org names (S10). Niceman's title is identical on both résumés.
- eng-music: the plugin/hardware vendor list trimmed from eleven to nine (S11).
- Banner contact line 6.5pt → **6pt**, to pay for the fourth run-in item. 6pt was
  already the compact banner's contact size, so no new value entered the system.
- Content files dropped their `_v1` suffix; `meta.output` became
  `meta.output_dir` + `meta.slug`.

### Removed

- `verify_verbatim.py` — its contract was "eng-music says exactly what v0 said",
  which this round deliberately breaks. Replaced by `verify_facts.py`.
- `Video Transcript Analysis & Content Automation Pipeline` from Selected
  Applications — the weakest of nine, and not on the portfolio page. Recoverable.

### Not shipped

- **S7 — figures in the Wolfpack bullets.** Six bullets, no numbers, next to
  $20k MRR and $300K→$30M. Nothing was invented to fill the gap; a client or
  engagement count from Ry lands in v2.1.

## [1.0] — 2026-07-29

Restyling of the published v0 to the `resume_design` system, content untouched.
eng-only derived from it with music reduced and engineering deepened. Verified
word-for-word against v0 by the now-retired `verify_verbatim.py`.
