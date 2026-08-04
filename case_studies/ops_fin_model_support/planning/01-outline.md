# Case study outline — "The Model Is Your Business Beacon"

**Working title, kept:** The Model Is Your Business Beacon
**Folder:** `case_studies/ops_fin_model_support/`
**Canonical public URL (planned):** `https://intake.wolfstrategyllc.com/ops-fin-model-case-study/`
**Robots:** public, indexed
**Source brief:** `planning/Why Startups Need Weekly Financial Models.srt` (Ry, 2026-08-04)
**Voice:** `docs/ryan-blog-tone.md`
**Frontend:** identical to `sm3-specific-pages/setmaster3-case-study/`, via the new shared
`case_studies/case-study-assets/`

---

## 1. Decisions taken before drafting

| # | Decision | Why |
|---|---|---|
| D-001 | **Practitioner thesis, Ry's own numbers.** No client is named, described, or implied. Every number traces to the transcript. | Ry confirmed 2026-08-04. The transcript carries argument, not an engagement. Inventing a client outcome is the single most damaging thing this page could do, and the tone guide §5 forbids it outright. |
| D-002 | **Shared asset folder** `case_studies/case-study-assets/`, referenced as `../case-study-assets/…`. | Ry confirmed. One duplicated font/CSS copy now, none on every case study after. The relative path resolves identically in this repo and on the deployed site, so paths are never rewritten. Same reasoning as `sm3-assets/`. |
| D-003 | **Public and indexed**, unlike the SM3 case study. | Different audience. SM3 is noindex because two differently-framed portfolio artifacts for one person read badly side by side. This page has no such twin: it is a client-facing argument, and being found is the point. |
| D-004 | **One CTA to the 30-minute call**, plus a navy-ghost link to the ROI calculator. | The book-first rule in `CLAUDE.md`. The calculator link is the same carve-out `rates/` has under spec R11: a consideration-stage tool, not a second funnel. |
| D-005 | **Working title kept.** "Beacon" is the one metaphor on the page. | Ry's call. Every section heading below is a plain Title Case statement, so the metaphor stays contained to the title and does not become a register. |
| D-006 | **CSS is generalized, not copied verbatim.** `case-study.css` drops SetMaster's magenta/cyan Out/In semantic and its `.trow` table, and replaces them with a neutral figure ground and a reusable `.dtable`. | Ry asked for standardized styling and animation. The SM3 palette exception existed so a product would look like itself; there is no product here, so carrying the exception forward would be borrowing a semantic as decoration. Every other rule, including the six-use coral ration, carries over unchanged. |
| D-007 | **"Correctness is not that important" is stated, then immediately bounded.** | The transcript says it flatly. Left unbounded on a public page it reads as permission to publish bad numbers to investors. Tone guide §4.4 requires the limit in the very next sentence. |
| D-008 | **"If you do not have a month-end close, you are not really a business" ships as an attributed opinion**, exactly as the transcript hedges it. | The transcript says "in my opinion, as an operator." Tone guide §5: attribute what you cannot stand behind as fact. |
| D-009 | **Six image placeholders, `M-01`–`M-06`,** sized at final aspect ratio. | Same device and same reasoning as SM3 `A-01`–`A-08`: dropping the real file in changes nothing about the layout. Never a gray box, never a "coming soon." |
| D-010 | **The feature-ROI comparison is built in HTML, not captured.** | It is a table, so it is a table. Sharp at every density, readable by a screen reader, and it cannot go stale against a spreadsheet edit the way a screenshot does. Directly inherited from SM3's `A-06` ruling. |

---

## 2. Thesis, in one sentence

A financial model is an operating tool that belongs in front of the product, and its value
comes from the exercise of building and maintaining it rather than from the accuracy of the
numbers inside it.

## 3. Reader

Founders, directors, and management at startups and small to medium businesses. Mostly
product-led and growth-led people. They are described in the third person for most of the
page and become "you" as it turns toward the ask, per tone guide §2.

## 4. Section spine

| § | id | Heading | Job | Assets |
|---|---|---|---|---|
| S1 | — | Hero | Title, standfirst, four stat tiles, opening figure | M-01 |
| S2 | `#misconception` | The Wrong Job for the Model | The misconception, the reversal, the cost of "not ready yet" | — |
| S3 | `#model` | What the Model Actually Is | Three statements, P&L primary, the headcount line, founder time as equity | M-02, sidebar |
| S4 | `#cadence` | The Weekly Look | 30 to 90 minutes, once a week. Month-end close as an h3 | M-03 |
| S5 | `#roi` | Finding the Highest-Return Hour | Time scarcity, per-feature ROI, the simulator | `.dtable`, M-04, sidebar |
| S6 | `#time` | Time Tracking Is the Other Half | What you should work on vs. what you did work on | M-05 |
| S7 | `#decisions` | Infeasibility Is Not an Opinion | 2,000 hours, eliminating the ten, quarters and years as an h3 | pull quote |
| S8 | `#room` | The Model in the Room | Meetings, boards, contractors, the VC framing, the honesty list | M-06, verdict, `.status` |
| S9 | `#start` | Where to Start | Smallest next step, one CTA | close block |

Nav carries five: The Wrong Job · What It Is · The Weekly Look · Highest-Return Hour · In the Room.

## 5. Beats, section by section

### S1 — Hero
- Kicker `CASE STUDY · 2026`.
- Standfirst: the reversal in miniature. Most founders treat the model as an accounting
  artifact and a fundraising artifact. It is neither. It is the document that decides what
  gets worked on this week.
- **Four stat tiles.** Build facts and cost facts, never impact metrics, because there is no
  instrumented outcome to report:
  - `2 to 3 days` — To build a straw model from nothing
  - `30 to 90 minutes` — The entire weekly maintenance cost
  - `1 day` — Month-end close to update the model
  - `2,000 hours` — Workable hours in a year, and you have to pick
- `M-01` wide, 16:9: the three-statement package in one workbook.

### S2 — The Wrong Job for the Model
- Open cold on the observation: better than nine in ten of the founders, directors, and
  managers Ry talks to hold the same misconception.
- Name it generously, never making the reader feel stupid for holding it: the model is for
  the accountant and for the raise, and it has to be right before it is worth the time.
- **Reversal.** The model is not an accounting document. It is an operating document.
- Correctness claim, then its limit in the next sentence (D-007).
- The exercise is what produces the value: it fleshes out the details of the business and
  surfaces the golden paths, the places where profit is high relative to the work and
  expense that generate it.
- Without the math written down it is all assumptions, and most assumptions are wrong.
- The objection Ry actually gets: "not ready for one," unsure which assumptions to use,
  wanting to develop the product further first.
- What he observes instead: stress and decision paralysis, from people with no model to
  look at.
- The split. Founders who reach viability and founders who do not. Define the terms
  explicitly: funding or self-sufficiency, not an exit.

### S3 — What the Model Actually Is
- Three-statement package: profit and loss, balance sheet, cash flow.
- Mostly P&L. The balance sheet and the cash flow fall out of it. The P&L is the document
  you look at most.
- The pre-revenue case, which is the part most founders have never been shown. There is a
  headcount line. If you are not paying yourself, the time you put in is creating
  shareholder equity, and a monthly close makes that visible.
- Investors read that as awareness. Immediate caveat: it does not substitute for traction.
- `M-02`, 16:9: the P&L with the headcount line and founder time converting to equity.
- **Sidebar: The Straw Model.** What it is, why two to three days is the right budget, and
  why a model that is deliberately wrong in places still works. It is a frame for
  argument, not a forecast.

### S4 — The Weekly Look
- Not daily, and not made accurate. That is the accountant's job, and the investor's, later,
  once the business is profitable.
- Once a week, 30 to 90 minutes. Purposes, plainly: keep it loaded in your mind, catch the
  ideas that have not made it onto the model's task list, check off wins, update timelines.
- `M-03`, 4:3: the model's own task list in the weekly review.
- **h3 — Month-End Close.** One day per month. Take the straw model to your accountant, ask
  for feedback, ask for a month-end close. The opinion, attributed (D-008).

### S5 — Finding the Highest-Return Hour
- Time is the scarcest thing in a startup, and in a one-person startup it is the only thing.
- You cannot compute the return on your own hours in your head. You will estimate, and you
  will be wrong.
- The model estimates it per project, per product, per sub-product.
- **`.dtable`, built in HTML (D-010).** Three features, annual return, and the ordering that
  falls out: one at roughly $100,000 a year and two at roughly $10,000 a year, so the first
  one goes first. Illustrative figures, labeled as such in the caption.
- **Sidebar: The Simulator.** Ad spend to followers to conversion to path value, built into
  the model rather than done on a napkin or in a loose spreadsheet. Caveat: a simulator
  built on invented conversion rates returns invented answers, so the input that matters is
  the one number you have measured.
- `M-04`, 16:9: the simulator block.

### S6 — Time Tracking Is the Other Half
- The model says what should be highest return. Time tracking says what actually got worked
  on. Neither half is useful alone.
- The end-of-week check, stated rather than asked, because the tone guide bans rhetorical
  questions: look at whether the highest-return work got the most hours, and name what
  blocked it when it did not.
- Ry's own position, in his own voice: minute-by-minute self-tracking is too distracting to
  be worth it. An end-of-day estimate, or an application that tracks projects on its own,
  beats interrupting the work to think about the work.
- Honest note: he is rebuilding his own time tracking system right now.
- The employee-facing use: show the team the return, be transparent about why one project
  runs to completion before the others start, and tie the reward to it.
- `M-05`, 16:9: one week of tracked time lined up against model line items.
- Fragment triple lands here, once on the page.

### S7 — Infeasibility Is Not an Opinion
- The model shows infeasibility with math, and math is hard to argue with.
- Translation for qualitative readers: call it an extremely expensive path.
- Immediate caveat: this does not remove free will and it does not make the decision. It
  removes the argument about whether the decision is affordable.
- 2,000 workable hours in a year. You have to pick.
- Ten ideas, two viable. Eliminate the ten now. Diluted attention finishes neither.
- **Pull quote:** the one on the page. Something close to: *Ten ideas will not get finished.
  Two might, and only if the other eight are gone.*
- **h3 — Quarters and Years, Not Weeks.** Granular work that feels urgent, spread across
  bigger periods. Nobody in 2028 asks what was finished in August 2026. They ask what was
  finished in 2026. Flag it as close to fact rather than as philosophy, exactly as the
  transcript does. The model shows the actual difference between an end-of-August date and
  an end-of-year date.

### S8 — The Model in the Room
- The maintained model is a source of truth for every conversation with a development
  partner, an investor, a mentor, or family working on the project.
- Meetings get shorter. Everyone huddles around the same document: what has had time put
  into it, what assumptions have been made, what has been ruled out.
- Board members who are not in operations daily bring ideas that were already ruled out.
  Show why, rather than having the discussion again. It runs both directions: less
  profitable than they think, and more profitable than they think.
- Do not put it on the founder to produce that evidence on the spot. Maintaining the model
  along the way is what makes the evidence available on the fly.
- The contractor decision, as a worked example: model the return on what the contractor
  would build, model how long, write it into the model rather than treating it as a one-off,
  and see what it sits behind. By the end of getting it in, the initiative is ruled out,
  refined, or reordered.
- **h3 — You Are Your Own Venture Capitalist.** Even with no raise planned. You are not going
  to reinvent how an application gets funded, so run the VC's practice: keep the
  three-statement model maintained continuously.
- **Verdict blockquote**, attributed to Ry, from the transcript's own framing.
- **h3 — What the Model Does Not Do**, with `.status` chips, mirroring SM3's "What Is Not
  Finished":
  - `Not accounting` — it does not replace books, an accountant, or a close process it feeds.
  - `Not accurate` — a straw model is wrong in places by design, and wrong numbers presented
    as certain do real damage.
  - `Not automatic` — 30 to 90 minutes a week is a real cost, and a model nobody opens is
    worse than no model, because it is trusted and stale.

### S9 — Where to Start
- Smallest next step, per tone guide §7.4: block two to three days and build the straw
  model. Not a forecast, not a raise deck. One P&L with your real cost lines and your
  honest guesses.
- Then the weekly hour.
- One CTA, plainly labeled: **Contact Wolfpack**, to the 30-minute call.
- Ghost link: the ROI calculator, framed as a consideration-stage tool.

## 6. Tone compliance targets

Checked against `docs/ryan-blog-tone.md` §9 before ship.

- Zero em dashes and en dashes in visible copy
- Zero exclamation points
- Zero rhetorical questions, including in every heading
- Contractions expanded throughout
- Quotation marks only around language held at arm's length: "not ready for one",
  "correct", "big-boy business"
- At least one reversal (S2 carries the load-bearing one, S3 and S6 carry smaller ones);
  exactly one fragment triple (S6)
- Every number specific and hedged: "2 to 3 days", "30 to 90 minutes", "better than nine in
  ten", "roughly $100,000 a year"
- Every strong claim followed immediately by its limit (S2 correctness, S3 investors, S5
  simulator, S7 free will)
- No client named, no testimonial invented
- No word from the reject list
- Opens cold on the misconception, no throat-clearing
- Closes on the straw model, then exactly one plainly-labeled CTA
- **Length: 2,422 prose words as built, against a 1,900 to 2,200 target.** The overrun is
  recorded rather than hidden. The transcript carries more distinct arguments than the
  target assumed, and the three that pushed it over (time tracking, quarters versus weeks,
  and the contractor worked example) each earn their place. It sits just under the SetMaster
  case study, which is the closest comparable page in this repo. If Ry wants it shorter, the
  first cut is S6's employee-facing paragraph and the second is S8's worked example.

**Lint results, run 2026-08-04 against the built page** (visible copy only, head/comments/
script stripped): 0 em or en dashes, 0 exclamation points, 0 question marks, 0 contractions,
0 reject-list words, 2 double quotes (the single arm's-length use of "correct"). Every h2 and
h3 is a Title Case statement.

## 7. Asset capture list

| ID | Ratio | What to capture | Section |
|---|---|---|---|
| M-01 | 16:9 | The three-statement package in one workbook. P&L, balance sheet, and cash flow visible as tabs or panes. | Hero |
| M-02 | 16:9 | The P&L with the headcount line visible, and founder time converting to shareholder equity. | S3 |
| M-03 | 4:3 | The model's own task list in the weekly review, in Notion. | S4 |
| M-04 | 16:9 | The simulator block: ad spend, followers, conversion rate, resulting path value. | S5 |
| M-05 | 16:9 | One week of tracked time lined up against model line items. | S6 |
| M-06 | 4:3 | The model open in a working session, as it appears when a group is reading it together. | S8 |

**Redaction rule for every capture.** These are Wolfpack's own model and Wolfpack's own
numbers, so no client data can appear in any of them. Before a file replaces a placeholder,
check the visible cells for client names, real contract values, and file paths that carry a
machine or client name. This is the same class of thing the SM3 publish scanner caught in an
interface placeholder, and it survives review because nobody is looking at the corner of a
screenshot.
