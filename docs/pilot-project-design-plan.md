# Pilot project page — design plan and rulings ledger

**Page:** `pilot-project/` → `https://intake.wolfstrategyllc.com/pilot-project/` (`noindex, nofollow`).

## Why this ledger starts at P-001

`CLAUDE.md` has described this file as the page's "full design plan and 17-ruling ledger"
since the page shipped (#236, 2026-08-18). **No such file was ever checked in** — verified
against the repo history on 2026-09-06, `docs/` has never held it. The rulings it names are
real, but they survive only as comments in the code they govern:
`pilot-project/index.html`, `pilot-project/css/pilot.css`, and `social-cards/build_cards.py`,
which cites ids like *"plan A-5"* that have no document behind them.

So this file does **not** reconstruct those seventeen from the comments — a rebuilt ledger
would be a guess wearing the authority of a record. It starts its own series, `P-nnn`, at the
first ruling actually written down here; the older ids stay in the comments, cited as "the
A-series". **Flagged for Ry:** if the original plan exists outside the repo, it should land
here and the two series be reconciled in one pass.

---

## P-001 — the $500 kickoff model (Ry, 2026-09-06)

The pilot moves off a fixed price and onto a kickoff-plus-hourly shape. The page is rewritten
to it, and the rules the old shape needed are retired with it.

**The model, as it now publishes:**

- **$500 kickoff fee**, covering the client's **first 6 hours**. This is the headline figure —
  the `.rail__price` line and the `.k hero__kicker`, which can no longer read "fixed fee".
- **$85 / hour after that**, billed once at the end of the window.
- **30 calendar days**, everywhere. Never "two to three weeks".
- **Nothing else is billed until the 30 days are up.**
- **The client sets the ceiling** — cap the hours, name a deliverable, or both; past the 6
  covered hours there is no minimum. This is the page's **new spine**, replacing "one problem,
  scoped together".
- **10–20 hours a week is the recommendation**, not a commitment.
- **~$2,900** (10 hrs/wk for 30 days) is the **only total-shaped figure allowed anywhere on
  this page**, and it is explicitly an example. There is no total pilot price.
- **Day 31 is an open door** — roll into a project tier, keep going hourly as needed, or stop.
  **No post-pilot rate and no fence are named**; that is negotiated on the call.

**Retired, not weakened.** The no-hours rule — no hours, no weekly commitment, no effective
hourly rate — and its disarm sentence, *"a pilot buys a scoped outcome rather than reserved
time, so it sits off the rate curve above"*, are **dead**. Every comment defending them is
deleted rather than softened, here and on both rates pages. Ry's reason, recorded verbatim:

> "I realize this is a big change that offers a big discount, that is why I'm making it and
> putting it up top."

**Placement changed too.** The pilot now sits **above** the project tiers on both rates pages
as the first pricing a reader meets, reversing the placement reasoning the old band carried.
It went to the Q3 page first again this round, so it stays a **mirror-set** item under
`docs/public-rates-consistency-contract.md` — the $500, the 6 covered hours, the $85/hr, the
30 days, the 10–20 hrs/wk recommendation and the ~$2,900 example must match on both.

**What did not change, and is not up for reconsideration here:**

- `noindex, nofollow`, direct-link only. Ry sends the URL.
- **One per client, and the page still does not say so** — enforced on the call. Nothing
  plural: no "each project", no "your next pilot".
- **No measured outcome, percentage, multiple, or past client result.** The *"live dashboards
  that show what's working—and prove the ROI"* line stays — lifted verbatim from
  `/rates_public/`, method language, not a result.
- The three example shapes stay a **plain list, never a card grid**, three is the count, and
  at least one ("Operations automation") maps to **neither** of the two systems.
- Both product blurbs stay **written fresh** — not the résumé-YAML strings `verify_facts.py`
  check 6 guards; this page stays out of its `HTML_PAGES`.
- **No price in the card image** (the A-series ruling `build_cards.py` cites as A-5).
- Coral stays rationed to **five**, enumerated in `css/pilot.css`'s header with a
  `coral use N of 5` marker at each site. No use was added; type size still carries the price.

**The "Every pilot includes" section is reframed, not deleted.** With no fixed fee left to
justify, a fixed inventory read as a bundle priced against it. The list is now *how the
engagement runs* — scope agreed in writing, a ceiling the client sets, the two systems
installed in their own accounts, instrumented work, shared plans and decisions — under the
heading **"Inside the 30 days"**, and promises no fixed duration of build. The two systems
keep their own section: the page still needs an example mapping to neither of them, which only
means something if the reader knows what they are.

### Open item — the social card is now stale by one ruling

`pilot-project/img/og-pilot-project.png` bakes in the subtitle
**"Fixed fee · Two to three weeks · Two systems you keep"**. Two of those three are now false.
The card is **untouched by this ruling** — P-001 changed the offer, not the art, and the
`hire/` standing applies: `og:image:alt` describes the card's *pixels*, so it must not move
until the art does. A rebuild is one `social-cards/build_cards.py` run once Ry approves a new
subtitle. **Flagged for Ry — the last place on this property still advertising the old
model.**
