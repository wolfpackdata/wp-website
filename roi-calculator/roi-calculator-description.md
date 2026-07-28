# AI Tool ROI Calculator — Build Plan

Source task: [Build AI Tool ROI Calculator for website](https://app.notion.com/p/376c70e5c7b480e39c6ce8f224dbf3db) (Notion, project: Wolfpack Website Updates June 2026)

## Goal

Build a standalone, single-page ROI calculator that lets a visitor estimate the dollar value of adopting an AI tool, based on their pay (salary or hourly), how much of their work AI touches, and how much faster/better that work gets. The page is hosted on GitHub Pages and linked from the main Wolfpack site (not embedded in the main site's codebase).

## Hosting & Stack

- **Hosting:** GitHub Pages (static site), separate repo from the main website. Linked to from wolfpack's main nav/CTA.
- **Stack:** Plain HTML/CSS/JS — no framework, no build step. Keeps it a true "just push and it's live" static page, simple to maintain, and fast-loading for a single-purpose tool.
  - `index.html` — page structure/content
  - `styles.css` — styling (match Wolfpack brand: pull colors, fonts, logo from the main site)
  - `calculator.js` — all input handling + calculation logic
  - Google Fonts (Roboto, weights 300/400/500/700) loaded via `<link>`/`preconnect` — the only external dependency; still no build step or bundler.
- No backend, no data storage — everything computes client-side in real time as the user types (no "Submit" button needed, though we may debounce input for smoothness).
- All dollar-amount input fields (annual salary, hourly rate, AI tool cost, cost of AI education) display a leading `$` and format the number with comma thousands separators as the user types (e.g. `80,000`, not `80000`).

## Inputs

| Input | Notes |
|---|---|
| Pay type | Toggle: **Annual salary** or **Hourly rate** |
| Annual salary ($/yr) | Shown only if Pay type = Salary |
| Hourly rate ($/hr) | Shown only if Pay type = Hourly |
| Hours worked per week | Default: 40 (only shown/used for Hourly) |
| Weeks worked per year | Default: 50 (only shown/used for Hourly) |
| % of work impacted by AI | Slider or number input, 0–100% |
| Productivity amplification | Toggle: **Time saved %** or **Multiplier (×)** |
| Time saved % | Shown if amplification = Time saved |
| Multiplier | Shown if amplification = Multiplier (e.g., 1.3×) |
| Quality of output multiplier | Slider, 5–25%. Extra value from AI-improved output quality (fewer errors, better results), added on top of time-saved value. Default: 15% (midpoint) |
| AI tool cost ($/month) | Number input. Default: $30/month |
| Hours per week learning/experimenting with AI | Number input. Time invested in learning/practicing AI tools, valued at the person's effective hourly rate as an added cost. Default: 0.5 hrs/week |
| Cost of AI education per month ($) | Number input. Courses, subscriptions, communities, etc. spent on AI education. Default: $350/month |
| Monthly improvement factor | Slider, 1–10%. Represents the person's skill/output improvement compounding month over month as they keep learning AI — see Calculation #3b. Default: 1% |

Currency-formatted inputs (salary, hourly rate, tool cost, education cost) accept up to 2 decimal places in addition to comma thousands separators (e.g. `1,250.50`).

## Calculations

**1. Annual labor cost**
- Salary: `AnnualCost = Salary`
- Hourly: `AnnualCost = HourlyRate × HoursPerWeek × WeeksPerYear`

**2. Normalize amplification input to a time-saved fraction**
- If user entered Time saved %: `TimeSavedFraction = %TimeSaved / 100`
- If user entered Multiplier `M`: `TimeSavedFraction = 1 − (1/M)` (e.g., M = 1.25 → 20% time saved)

**3. Annual value created (base)**
- `ImpactedFraction = %Impacted / 100`
- `QualityFraction = %QualityMultiplier / 100` (range 0.05–0.25)
- `BaseAnnualValue = AnnualCost × ImpactedFraction × (TimeSavedFraction + QualityFraction)`
  - Quality is additive with time saved: it captures value from AI-improved output (fewer errors, better results) that isn't just "faster," so it stacks on top of the time-saved contribution rather than replacing it.

**3b. Apply the monthly improvement factor**
- `MonthlyImprovementRate = MonthlyImprovementFactor% / 100` (range 0.01–0.10)
- The factor models the person getting better at using AI as the months go by: month 1 (January) is the baseline multiplier of 1.00, and each subsequent month adds one more increment of the rate — month 2 = `1 + rate`, month 3 = `1 + 2×rate`, ... month 12 = `1 + 11×rate`. E.g. at a 1% rate: Jan = 1.00, Feb = 1.01, Mar = 1.02, Apr = 1.03, etc.
- Averaging that linearly-growing multiplier across all 12 months collapses to a single growth factor:
  `GrowthFactor = 1 + 5.5 × MonthlyImprovementRate`
- `AnnualValue = BaseAnnualValue × GrowthFactor`

**4. Tool, education & learning-time cost**
- `EffectiveHourlyRate = AnnualCost / (HoursPerWeek × WeeksPerYear)` — uses the Hours-worked/Weeks-worked fields (default 40/50) as the basis even when Pay type = Salary, so learning time can be valued consistently.
- `AnnualLearningTimeCost = LearningHoursPerWeek × WeeksPerYear × EffectiveHourlyRate`
- `AnnualDirectAiCost = (ToolCostMonthly + EducationCostMonthly) × 12`
- `AnnualAiCost = AnnualDirectAiCost + AnnualLearningTimeCost`

**5. Net value & ROI**
- `NetAnnualValue = AnnualValue − AnnualAiCost`
- `ROI% = (NetAnnualValue / AnnualAiCost) × 100`
- Display with an explicit `+` sign when positive (e.g. "+219%"), and color-code the value green (positive) or red (negative). "N/A" and "∞" are shown uncolored.

**5b. Updated labor value**
- `UpdatedLaborValue = AnnualCost + NetAnnualValue` — reframes the net AI value as "what your labor is now effectively worth" once the tool's net contribution is folded in.
- Shown alongside a percentage: `LaborValuePct = (NetAnnualValue / AnnualCost) × 100`, displayed with a leading `+`/`-` sign and the same green/red color-coding as ROI. If `AnnualCost = 0`, show "N/A".

**6. Total hours saved per year**
- `HoursWorkedPerYear = HoursPerWeek × WeeksPerYear` (same hours-worked basis used for the effective hourly rate above, so it's consistent even for salaried pay).
- `HoursSavedPerYear = HoursWorkedPerYear × ImpactedFraction × TimeSavedFraction × GrowthFactor`
- Only the time-saved fraction counts here (not the quality multiplier, which reflects better output, not time back), scaled by the same monthly-improvement growth factor used for annual value.
- Display as a rounded whole number of hours (e.g., "253 hrs/yr"). A visitor can look at this and immediately understand "AI gives me back X hours a year" — no compounding-payback math to parse.

### Worked example (for testing)
- Salary: $80,000, Hours/wk: 40, Weeks/yr: 50, % impacted: 60%, Time saved: 20%, Quality multiplier: 15%, Tool cost: $30/mo, Learning hours: 0.5 hrs/wk, Education cost: $350/mo, Monthly improvement factor: 1%
- BaseAnnualValue = 80,000 × 0.60 × (0.20 + 0.15) = 80,000 × 0.60 × 0.35 = **$16,800/yr**
- GrowthFactor = 1 + 5.5 × 0.01 = **1.055**
- AnnualValue = 16,800 × 1.055 = **$17,724/yr**
- EffectiveHourlyRate = 80,000 / (40 × 50) = **$40/hr**
- AnnualLearningTimeCost = 0.5 × 50 × 40 = **$1,000/yr**
- AnnualDirectAiCost = (30 + 350) × 12 = **$4,560/yr**
- AnnualAiCost = 4,560 + 1,000 = **$5,560/yr**
- NetAnnualValue = 17,724 − 5,560 = **$12,164/yr**
- UpdatedLaborValue = 80,000 + 12,164 = **$92,164/yr** (**+15%**)
- ROI% = 12,164 / 5,560 × 100 = **~+219%**
- HoursWorkedPerYear = 40 × 50 = **2,000 hrs/yr**
- HoursSavedPerYear = 2,000 × 0.60 × 0.20 × 1.055 = **~253 hrs/yr**

## Output fields (displayed live, updates as inputs change)

- Annual labor cost
- Annual value created (time saved, quality, and monthly improvement factor)
- Annual AI cost (tool subscription + education cost + opportunity cost of learning time)
- Net annual value
- Updated labor value (annual labor cost + net value, with a color-coded % change)
- ROI % (headline stat, color-coded green/red)
- Total hours saved per year (headline stat)

## Edge cases & validation

- **AI tool cost = 0** (and all other AI costs 0, so `AnnualAiCost = 0`): ROI% is undefined (division by zero) — shows "∞" if annual value is positive, else "N/A". Hours saved is unaffected by AI cost, so it always renders as a plain number.
- **% impacted or time saved = 0**: Annual value = $0; net value negative; ROI% = −100%; hours saved = 0 hrs/yr. Should render cleanly, not as an error state.
- **Multiplier = 1** (no amplification): time saved fraction = 0, same as above.
- **Multiplier < 1**: would imply negative time saved (AI makes work slower) — either disallow (min value 1.0 in the input) or allow and show negative value honestly.
- **Quality of output multiplier**: constrain the slider/input to the 5–25% range (don't allow values outside it, since it's meant to represent a realistic quality-improvement band, not an open-ended input).
- **Monthly improvement factor**: constrain the slider/input to the 1–10% range.
- **Negative/blank numeric inputs**: clamp to 0 or show inline validation; don't let the calc silently produce `NaN`. This includes the currency-formatted inputs — strip the `$` and commas before parsing.
- Pay-type and amplification-type toggles should show/hide only the relevant fields (avoid asking for both salary and hourly, or both time-saved% and multiplier).

## Page layout

1. **Header** — short headline ("How much is AI actually worth to you?"), one-line explainer, Wolfpack logo/link back to main site.
2. **Input panel** (left column or top on mobile) — grouped form fields as above, sensible defaults pre-filled (salary $80,000, 40 hrs/wk, 50 wks/yr, 50% impacted, 25% time saved / 1.3× multiplier, 15% quality multiplier, $30/mo tool cost, 0.5 hrs/wk learning, $350/mo education cost, 1% monthly improvement) so the calculator shows a result immediately, before the user changes anything.
3. **Results panel** (right column or below on mobile, sticky on scroll) — the seven output fields, with ROI% and hours saved per year emphasized as the headline numbers.
4. **CTA footer** — link/button back to Wolfpack's main site or contact page ("Want help figuring out where AI fits in your workflow? Talk to us.").
5. Fully responsive: stacked single column on mobile, two-column on desktop.

## Style

- Match Wolfpack brand palette, type, and logo usage from the main site so the standalone page doesn't feel disconnected.
- Keep it lightweight and fast — this is a lead-gen/utility tool, not a marketing showcase; clarity over decoration.
- **Implemented palette:** dark navy background (`#000b29`), slightly-lighter navy surfaces for panels/inputs (`#0a1638` / `#10204a`), Wolfpack red/orange accent (`#f95954`) for the logo mark, active toggle state, and headline stat values, plus green/red (`#4ade80` / `#f87171`) for positive/negative value indicators.
- **Type:** Google-hosted Roboto (weights 300/400/500/700) — 300 for body copy, 700 for headings and headline stats.
- **Logo/header:** inline SVG Wolfpack wolf-paw mark next to the wordmark "Wolfpack Data & Strategy," linking to `https://www.wolfstrategyllc.com`; a lighter-weight "← Back to site" text link sits opposite it.

## Deployment

- New GitHub repo (or a `/roi-calculator` path in an existing GitHub Pages repo).
- Enable GitHub Pages on `main` (or `/docs`) branch.
- Add a link/button to this page from the main Wolfpack website's nav or relevant page (e.g., services or AI page).

## Open questions

- Exact GitHub repo name / URL path for the page (not yet created — files currently live locally only).
- ~~Final CTA destination~~ — **Decided** (superseded 2026-07-28, #34): the closing CTA points at the 30-minute intro-call calendar (`https://calendar.app.google/zHNd1NA9wzb4VRLw5`, book-first funnel — the original `contact-3` form link is retired); the header/back links still go to the live main site, `https://www.wolfstrategyllc.com`.
- Whether to add basic analytics (e.g., simple pageview tracking) to see if the calculator gets used.

## Next steps

1. ~~Scaffold `index.html` / `styles.css` / `calculator.js` with the form + results layout above.~~ **Done.**
2. ~~Implement calculation logic per the formulas above, wired to live input events.~~ **Done**, including the added "Updated labor value" stat (Calculation #5b) beyond the original spec.
3. ~~Handle edge cases (zero tool cost, zero impact/time-saved, invalid inputs).~~ **Done**, including color-coded positive/negative styling on ROI and updated labor value.
4. ~~Style to match Wolfpack brand.~~ **Done** — see implemented palette/type in the Style section above.
5. ~~Replace the break-even headline stat (months to pay back AI cost) with total hours saved per year — the break-even math was hard to parse; hours saved is a more intuitive number.~~ **Done.**
6. Create/point a GitHub repo with Pages enabled; verify live URL. **Still open.**
7. Add link from main Wolfpack site; update Notion task status to Done. **Still open.**
