# Fable AIIM Position-Paper Re-review (R4)
## "Computable Clinical Intent: Recovering Executable Care Actions from Clinical Communication"

Reviewer: simulated top-tier AIIM Position Paper reviewer (Fable model), full re-read of the R4 index.html.

## 1. Recommendation: ACCEPT WITH MINOR REVISION

Every one of the six prior blockers has been substantively addressed; the text is internally tighter. No remaining issue changes the argument or requires a new review cycle. One genuine internal contradiction newly exposed (readiness ladder vs worked example on ACR 1) is the only item insisted on; two one-sentence precision edits and polish otherwise. The paper meets the AIIM Position-paper bar.

Mechanical checks: abstract 246 words; 7 keywords; 72 references, every citation first appears in strictly ascending order 1..72; Highlights 5 bullets (78/82/84/74/80 chars); no em-dashes; no unclosed <p>.

## 2. Resolution of prior items
- W1 (contradiction/revision definition): RESOLVED (exclusion relation covers hold/continue; communication-time precedence; STP/conditional-temporal-problem split).
- W2 (alignment rule vs box on invented attributes): RESOLVED (unsupported-attribute error -> unsafe).
- W3 (Schedule agreement vacuous; box scores asserted): RESOLVED (defined over reference pairs; box states emitted prediction and derives scores).
- W4 (orphan dependency unflagged; STP over-scoped): RESOLVED (box surfaces consistency flag; STP scoped to unconditional).
- W5 (conformal overreach): RESOLVED in substance, one wording fix (RW3).
- W9 (reference order; Highlights): RESOLVED (first-appearance 1..72; Highlights file present).

## 3. Strengths
Layer framework epistemically labeled; ACR consistently a recovery target + FHIR projection with semantic-parsing analogy; 5.3 defines (not just names) the set-level relations and locates novelty in reasoning over recovered/abstained sets (Asbru/PROforma/GLIF credited); evaluation framework is a real contribution (alignment, unsupported-attribute rule, consequence weighting, annotation precedence, worked scoring that derives its numbers); regulatory paragraph substantive; two falsifiable claims stated over measures both methods can produce.

## 4. Remaining weaknesses (none blocking; RW1 insisted-on)

**RW1. Readiness ladder contradicts the worked example on ACR 1 (5.1). Moderate — the one item to fix.**
Ladder: "adding 'two weeks' and a responsible actor makes it actionable; resolving a due date and workflow object makes it executable. A partially populated ACR sits below the actionable rung until its actor and timing are resolved." Example: ACR 1 has "actor: unresolved" yet "(derived) readiness: actionable" and "stays at the actionable rung, not executable, until an owner is confirmed." By the ladder, ACR 1 (timing resolved, actor unresolved) sits BELOW actionable; by the example it is AT actionable. Fix: redefine rungs as interpreted = typed action + target; actionable = plus a normalized temporal constraint or gating condition; executable = plus a resolved accountable owner and a due date bound to a workflow object; reword "until its actor and timing are resolved" to "until its owner and timing are resolved" (or "timing/gating condition").

**RW2. "hold" used in two senses (5.3 exclusion relation vs box "hold ... until"). Minor-moderate.** Add to 5.3: "A hold with a stated release event is a revision of the held action's temporal constraint; a hold with no release event is a contradiction under the exclusion relation." Change box "(CBC after the referral)" to "(CBC after the cardiology visit, an event that is not itself an ACR in the set)".

**RW3. Conformal wording (6). Minor.** "a distribution-free bound on the abstention threshold follows from conformal calibration" is imprecise. Fix: "a threshold with a distribution-free coverage guarantee follows from conformal calibration [.], and a distribution-free bound on the rate of accepted-but-erroneous records from conformal risk control [.], from which the selective risk follows at a given coverage."

**RW4. "Recognizing an action is close to solved" (7). Minor overreach** (gold spans supplied). Fix: "recognizing an action type from its span is close to solved."

## 5. Minor issues
- Box "Scores" row: call the invented actor an "unsupported-attribute error" to match the W2 prose.
- Box second-message row: add schedule agreement 0/1 (one reference ordered pair, visit before CBC, not reproduced) to exercise the new metric.
- 5.3 "A repeat count at one week and at two weeks are two serial orders" -> "A repeat CBC at one week and again at two weeks".
- 5.3 "Precedence runs by communication time, then speaker authority" -> add "for resolving which of two contradicting ACRs stands".
- ACR 2 origin: add "temporal inferred" (event-anchored-on-trigger is inferred).
- Table 3: action and target both map to ServiceRequest.code; note the action verb maps to Task.code / a modifier, or that action+target collapse into one coded element on write-back.
- 7 companion paragraph: "the five critical fields 88.4%" vs "all four closed fields"; say the five = action type plus the four closed fields.
- Highlights bullet 5: 18-35% is for the four closed fields, not full ACR; "recover the closed fields jointly only 18-35% of the time".
- 8 falsification sentence long; split after "coherent".
- 5.2 "dependency and status ... need profile-specific mapping" vs Table 3 "represented"; add "represented; profile mapping" qualifier.
- Figure 2 SVG legend 9px; check DOCX/PDF legibility.

## 7. Verdict on readiness
At the AIIM Position-paper bar and ready to submit once RW1 (the readiness-ladder contradiction) is fixed; that is the only insisted-on item. RW2-RW4 and the minors are one-sentence precision/polish that an editor would take as a minor revision. No prior blocker remains open.
