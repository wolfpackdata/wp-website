# Draft feedback — read as a potential client hiring Wolfpack

Judged against `first-draft.md` by Claude, 2026-08-25, at Ry's instruction in the source
transcript: where the draft needs more support, what to consider cutting, and where the
wording could change. **This is advice for Ry and the copywriter; the draft was
deliberately not rewritten to it.**

The one overall reaction first: as a prospect, this post makes me *trust* Wolfpack before
it makes me *want* it. The safety mentality, the draft-only email SOP, the "hesitant to
take the project" honesty, and the wheelhouse section are the strongest trust-builders I
have read on a consultant's site. What the post underuses is proof: several claims have
published evidence one link away and don't use it.

## Where to add support

1. **The "15 years" and "last year" claims collide.** "In place for 15 years" and "fully
   tested system for the last year" sit two sentences apart, and as a client I stumbled:
   which is it? The fix is one sentence of separation: the client-ID isolation *practice*
   is 15 years old; the AI-gated *implementation* of it has been running in production for
   the past year. Said that way it becomes a strength (an old discipline extended to a new
   tool) instead of a contradiction.
2. **Link the published evidence.** The Wolfpack AI Command paragraph has a public case
   study (`/wolfpack-ai-command/`) and says none of it. The adversarial-agents claim is
   demonstrated in that same case study. The ROI section could link the public ROI
   calculator (`/roi-calculator/`). Each link turns an assertion into something I can go
   verify, which is exactly the mode the rest of the post is in. (Constraint from the
   repo: do **not** link the pilot-project, hire, or github pages — they are noindex and
   direct-link only.)
3. **The chatbot SOP needs one concrete beat.** "Draft responses that a human must
   ultimately send" is the strongest guardrail in the post; give the non-technical reader
   the picture in one sentence — the reply sits drafted in your own outbox, and nothing
   leaves until a person presses send.
4. **Say what happens when the engagement ends.** "They own all the data on their side" is
   good; a prospect's next question is exit. One sentence: the BigQuery project, the
   repos, and the workspace accounts are theirs, and Wolfpack's access is revocable by
   them at any time. (Verify with Ry that this is precisely true before writing it — it
   matches how the BQL install is described elsewhere on the site.)
5. **Total the running costs.** The $8 workspace user, the $50–$100 BigQuery range, and
   the Claude Pro subscription are scattered across two sections. As a client I want the
   one number: roughly $80–$130 a month in third-party costs, all in accounts I own. That
   single line answers "what is my overhead beyond Wolfpack's fee" and no competitor page
   answers it.
6. **Is my data training a model?** The post talks permissions and isolation but never
   answers the question every 2026 client asks first. If the true answer is favorable
   (e.g. commercial API/subscription terms, no training on client data), one supported
   sentence belongs in the safety section. Question for Ry — do not invent the claim.

## What to consider cutting

1. **The Codex / Max paragraph.** As a prospect I don't know what Codex is, and whether
   Wolfpack needs a second subscription is internal tooling logic, not my problem. Keep
   the valuable part in one sentence: an independent AI reviewer, on a different vendor's
   model, checks the code before it ships. Cut the subscription accounting.
2. **The AOV walkthrough.** The conversion example is persuasive; by the time it has been
   stated as basis points, then as AOV multiplication, then as "0.1 of a percent equals X
   dollars," it has been said three times. One pass through the arithmetic is enough.
3. **The HBO / Time Warner mention.** It is a credibility flex sitting inside the
   weaknesses section, and it blunts the honesty that makes that section work. Either move
   it up into the wheelhouse paragraph as plain history or cut it. (Ry has cleared the
   names themselves for publication.)
4. **"Or whatever"** in the Notion/Trello/Salesforce sentence — fine in speech, reads
   throwaway in print, and the list is doing serious work right there.

## Wording

1. **Keep verbatim:** "anonymous check bots, not finger-pointing blame machines"; "you can
   sleep easy that they're not reading them"; "Otherwise, it's not a win-win." These are
   the post's voice.
2. **"Gated community" → "gated environment."** A community is a thing you share; the
   whole point of the sentence is that nothing is shared.
3. **"Restrict them just as you would a new employee"** — the transcript says "low-level
   employee" here; the draft already uses "new employee" to match the analogy established
   in the opening section. Recommend keeping "new employee" in both places.
4. **"Safeguard your AI's interference with things that you have not given it permission
   to interfere with"** — the double "interfere" reads as a loop. Something like
   "…platform's own ironclad permission structure, instead of on instructions you hope the
   AI follows" keeps the argument and loses the knot. Writer's call.
5. **"The client" vs "you."** The draft drifts between third person ("the client is
   given") and second ("you can sleep easy"). Second person is stronger for this post —
   it is literally addressed to the person deciding to hire. Suggest normalizing to "you"
   throughout except where Ry is describing his own system.
6. **Structure suggestion:** the post lists roughly ten distinct things a client gets. A
   short plain-list summary near the top (five to seven bullets, no detail) would let a
   skimming reader see the inventory before the depth. The current structure rewards only
   the reader who finishes.
7. **The close:** "Otherwise, it's not a win-win" is the best closing sentiment in the
   piece. Consider ending the body on the ROI section's honesty and letting the CTA
   follow it directly, with the wheelhouse section moved ahead of ROI. Ordering is the
   copywriter's call; flagging it because the current order buries the strongest exit
   line mid-post.
