# Source notes — new client expectations post

Source: Ry's dictated transcript, 2026-08-25, committed beside this file as
`source-transcript.srt` (originally `blog_posts/Blog on Wolfpack New Client
Expectations 8-25-26.srt`). The transcript ends with Ry's own instructions: an outline in
the best digestion order, a draft keeping as much verbatim transcript copy as possible
(fillers removed, grammar deliberately not corrected), and a judge-it-as-a-client
feedback pass with no rewrite. Those three deliverables are `../planning/first-draft.md`,
the outline in `copywriter-brief.md`, and `draft-feedback.md`.

## Redaction decisions (this repo is public)

- **HBO and Time Warner** as early-career clients: cleared by Ry, 2026-08-25.
- Nothing else in the transcript names a current client, a private rate, or unannounced
  work. The client-facing offerings it describes (client-ID environments, subdomains,
  BQL, AI Command) are the subject of the post — publicizing them is the point.

## Transcription corrections applied in the draft

The speech-to-text introduced errors; these are corrections of the *transcription*, not
edits of Ry's wording:

| Transcript says | Draft says | Why |
|---|---|---|
| "HBCU" | HBO | Confirmed by Ry, 2026-08-25 |
| "pro-Cloud subscription" / "pro accounts" | Claude Pro subscription | Context: "highly subsidized processing rates," "skills and AI products that I send them" |
| "Macs" / "a Macs subscription" | Max (Claude Max) | Context: development-heavy firms, subscription tiers |
| "they probably already haven't" | "they probably already have it" | The sentence's own logic; flagged for Ry to confirm |
| "customer incoming" | "incoming customer email" | Sentence fragment repair |
| "own security. Processing environment" | "own secure processing environment" | Mid-sentence break artifact |
| "A O V" | AOV | Spelled-out acronym |
| "we're exposed to" | "I was exposed to" | Dictation slip in a first-person passage |
| "Wicks" (in Ry's chat framing, not the transcript) | Wix | — |

## Fact checks

### BigQuery running cost (Ry's in-transcript request)

The transcript says ~$100/month "because that is basically the lowest level of storage you
can buy," hedged to $50–$100, with an explicit instruction to fact-check without
understating. Checked 2026-08-25:

- There is **no ~$100 storage floor**. BigQuery has no minimum spend.
- On-demand queries: **$6.25/TiB scanned**, first **1 TiB/month free**.
- Active logical storage: **~$0.02/GB/month**, first **10 GB free**; long-term storage
  (untouched 90+ days) ~$0.01/GB/month.
- A typical SMB analytics footprint (tens to low hundreds of GB stored, a few TiB scanned
  monthly) lands in the **tens of dollars per month**.

So **$50–$100/month is a conservative ceiling, not an understatement** — the draft keeps
the range and adds "often less." The "lowest level of storage" rationale was dropped on
Ry's own instruction. Re-verify against Google's own calculator before publish (secondary
sources used here; Google's pricing page would not fetch):

- <https://costbench.com/software/data-warehousing/google-bigquery/>
- <https://cdcalculators.com/bigquery-pricing-calculator/>
- <https://www.modern-datatools.com/tools/google-bigquery/pricing>

### Other numbers carried by the draft

| Claim | Status |
|---|---|
| Google Workspace user ≈ $8/month | Matches Workspace Business Starter list pricing; stated "as of today" in the draft, which is the right hedge |
| Client-ID system "in place for 15 years" / "fully tested for the last year" | Ry's claims; the draft keeps both — see feedback item 1 on separating them |
| Weekly meetings, 30 minutes | Ry's claim |
| BQL setup "five to ten minute process" | Ry's claim; consistent with the pilot-project page's framing of the BQL install |

## Standing constraints that bind this post

- **No measured client outcomes, percentages, or multiples may be invented** — the ROI
  section describes *method* only, same rule as every page on the site.
- **Never link** `pilot-project/`, `hire/`, or `github/` pages from the post: noindex,
  direct-link only.
- The Wolfpack AI Command case study (`/wolfpack-ai-command/`) and the ROI calculator
  (`/roi-calculator/`) are public and linkable.
- AI Command copy must not imply PM headcount replacement (repo ruling D-013): the
  transcript's "bespoke project manager and a developer's best friend" framing is safe;
  keep it on that side of the line.
