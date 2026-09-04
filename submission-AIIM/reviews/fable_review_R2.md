# Fable AIIM Position-Paper Re-review (R2)
## "Computable Clinical Intent: Recovering Executable Care Actions from Clinical Communication"

Reviewer: simulated top-tier AIIM Position Paper reviewer (Fable model), full re-read of the revised index.html.

## 1. Recommendation: Minor revision

The revised manuscript is now a coherent AI-in-medicine position paper rather than a health-IT taxonomy: the ACR is convincingly re-cast as a FHIR-aligned recovery target, the semantic-parsing analogy makes the problem well-posed, the differentiation tables (3 and 4) are specific, and the evaluation framework is concrete at the per-record level with a useful worked scoring example. What remains is a single structural asymmetry that the authors must close in text: the paper's claim to novelty rests on *set-level* intent reasoning, yet that half is the least specified (no characterization of what a contradiction or a satisfiable schedule is over ACR tuples), two of its four measures are degenerate as written (a system that recovers nothing scores perfectly), it is never exercised in a worked example, it has no companion-study evidence at all, and it does not engage with AIIM's own temporal-planning and guideline-execution literature (Asbru, Shahar, temporal constraint satisfaction), which is where an AIIM reader will immediately look for prior art. Add to this a few disclosure and consistency problems around the companion studies (synthetic corpus disclosed only in Section 8; "a companion study" singular in abstract/intro/Data Availability versus two in Section 7; R4 versus R5). None of this requires new experiments; all of it is fixable by writing, but it is not optional.

Automated checks run by the reviewer: abstract 249 words (limit 250); zero em-dashes or double hyphens; no "honestly/frankly" register; all 64 references cited; citation numbering is NOT in order of first appearance.

## 3. Strengths
- S1 (5.1, Def 1, Table 3): "recovery target, not representation" framing explicit and well argued; "recovery accuracy is undefined against FHIR in general, but it is exactly defined against this schema"; SQL/semantic-parsing analogy. Table 3 per-attribute FHIR R5 mapping concrete and mostly correct.
- S2 (5.1 after Table 3): the four recovery-side annotations are exactly the right delta from FHIR, stated as annotations not a rival model.
- S3 (5.3, Table 4): capability-by-capability differentiation from CLIP/MedDec/MEDIQA-OE.
- S4 (7, alignment + worked scoring box): per-record framework is usable; the paper's most AIIM-relevant contribution.
- S5 (5.1 worked example): best articulation of why abstention is a structural requirement.
- S6 (6, regulatory; 8): invariants tied to FDA CDS + EU AI Act; two genuinely falsifiable claims.
- S7 (2-3): layer framework short, epistemic status stated plainly, no longer dominates.

## 4. Remaining major weaknesses (path to acceptance = W1-W4 + reference renumber)

**W1. Set-level reasoning carries the novelty but is under-specified, unevidenced, and disconnected from AIIM's temporal-planning literature (5.2-5.3, 7).**
- The paper concedes decision-support layers already do such reasoning "on structured, already-consistent inputs"; what is new is applying it to noisy recovered sets, but the manuscript never engages Asbru / Shahar-Miksch temporal plan representation and execution monitoring, knowledge-based temporal abstraction, PROforma/GLIF task networks, or temporal constraint satisfaction (STP/Allen) that underlies "satisfiable schedule".
- Nothing says what "cannot jointly hold" means over ACR tuples ("CBC in one week" + "CBC in two weeks": contradiction or two orders? "hold warfarin" vs "continue warfarin": later-wins, speaker authority, or review?).
- Neither companion study reports any set-level measure (Study 1 gives models the gold span, removing individuation; Study 2 is per-pair), so "direct evidence that executable correctness is the binding constraint" is evidence for the per-record half only.
- Fix: (a) a paragraph in 5.3 defining set-level relations over ACR tuples (contradiction, revision/revocation, dependency, temporal-constraint form) and naming the constraint language (a simple temporal problem with event-anchored variables suffices); (b) 4-6 references to Asbru/Shahar/Miksch, PROforma, temporal CSP, stating precisely what is new (plan-consistency reasoning over recovered, uncertain, partially unresolved sets that tolerates abstained attributes); (c) state in 7 that companion evidence grounds per-record measures only and set-level remains to be instantiated.

**W2. Two set-level measures in Table 5 are degenerate; no set-level score is demonstrated (7, Table 5, worked box).**
- "Schedule feasibility" and "whole-plan consistency" are maximized by a system that emits no constraints/dependencies (property of the prediction alone, not agreement with reference -> rewards under-recovery). "Intent individuation" duplicates action-detection F1. The worked box scores only per-record measures.
- Fix: define feasibility/consistency against the reference (fraction of reference constraints/dependencies recovered such that predicted plan is satisfiable AND agrees with reference's satisfiable set; or report jointly with dependency/constraint recall). Redefine individuation as split/merge error counts. Extend the worked scoring box with a second message ("Actually, hold the CBC until after the cardiology visit") showing contradiction-detection and dependency scoring.

**W3. Companion-study disclosure and consistency (7 last para, 8, Abstract, Intro, Data Availability).**
- (i) Synthetic nature of Study-2 corpus (and CIRCA's synthetic share) must be disclosed where numbers are reported, not in Section 8. (ii) 0.99/zero-day on synthetic data with unambiguous anchors: the hybrid computes dates given the right anchor; it does not solve anchor selection, so "separating learned interpretation from computed structure closes the gap" over-generalizes. (iii) Abstract/Intro/Data Availability say ONE study; Section 7 uses two. (iv) Table 3 targets FHIR R5 (RequestOrchestration) but CIRCA uses R4 (RequestGroup, not RequestOrchestration), so conditional/dependency rows are not what the benchmark realizes. (v) "audited agreement 88.4%" does not say agreement on what, over how many items.
- Fix: state "synthetic" + corpus size in 7; add that Study 2 fixes the anchor regime and anchor selection under ambiguity is untested; qualify "closes the gap" -> "closes the date-computation gap"; make abstract/intro/Data Availability say two studies and cite [64]; note R4/R5 and what changes; say what 88.4% measures.

**W4. ACR schema inconsistency between Definition 1 / Figure 2 and the worked example (5.1).**
- Def 1 fixes a nine-attribute tuple with confidence as a calibrated map. Worked example shows `readiness: actionable` (not in tuple) and `confidence: extracted` for ACR 2 (that is the extracted/inferred flag, not a number). The extracted-vs-inferred flag is one of the "four things" but absent from tuple and Figure 2. Status values differ (5.1: recovered/confirmed/active/completed/cancelled; Table 3: FHIR draft/active/completed/revoked; recovered/confirmed have no FHIR value).
- Fix: add an `origin` attribute (extracted | inferred, per attribute) to tuple + Figure 2; make readiness explicitly a derived property; give ACR 2 a numeric confidence; add a status-value crosswalk.

**W5. CPOE already makes structurally entered intent computable; name and size the residual (3-4).**
- Section 3 lists CPOE as layer-2 tech; Section 4 concedes intent is computable once structured. Layer 3 = machine recovery of intent that is communicated but never ordered (discharge recommendations, conditional advice, patient instructions, handoffs). State this and size it (studies of discharge-recommended tests / pending results that never become orders; figures exist in cited [3,8]).

**W6. Section 6 thin on the learned/symbolic interface and how per-attribute calibration is obtained.**
- Name the contract: what the learned component emits (normalized relative expression + anchor label?), the anchor-ambiguity failure (deterministic arithmetic inherits a wrong anchor with full confidence -> confidently wrong), and how per-attribute confidence is produced (verbalized, token-likelihood, or conformal/split-conformal selective prediction; conformal is the natural fit for a guaranteed selective-risk curve and is absent). Add one paragraph + cite conformal prediction alongside [57,58].

## 5. Minor issues (selected)
- Abstract asserts causation ("has a measurable cost in failed test-result follow-up...") that Section 1 hedges as multi-factorial; rephrase to "is implicated in".
- Reference numbering not first-appearance order; renumber before submission.
- Section 1: "read against the field's documented history [1,2]" - say the five markers are the authors' construct.
- Table 1 layer-3 "Class of computation": "Schedule, coordinate, monitor, close" already done by schedulers on structured intent; consider "recover, reconcile, schedule, close".
- Figure 1 caption: "right-hand label" but labels are inside each box; fix wording.
- Figure 2 caption: confidence drawn optional but Def 1 says always carried; align.
- Table 3 target row: `subject` is the patient, not the target; drop or explain.
- Table 3 / worked example condition: `asNeeded[x]` is PRN execution of an active order, not a conditional order that comes into existence on a trigger; map "refer if palpitations recur" to a RequestOrchestration action condition or a proposal-intent request with a trigger; say which.
- Table 4: ACR column scores a specification vs implemented datasets; state in caption. Consider a row/footnote on i2b2-2012/THYME (the "temporal normalization exists" objection).
- Section 7 alignment: define a match when action agrees but target does not (matched with target error, or unmatched?).
- Section 7 unsupported-action rate: "no supporting span" is gameable; require the span *expresses* the action.
- Section 7: "consequence class" - who assigns, what taxonomy? "temporal anchor chosen by a stated precedence" - give the precedence (explicit anchor > discharge > document time). Provenance "above threshold" - give it.
- Section 6 EU AI Act: "places clinical decision software in its high-risk category" imprecise; the Act classifies AI that is a safety component of / is a medical device under MDR/IVDR third-party conformity assessment as high-risk. Rephrase.
- Section 5.2 first paragraph repeats Table 3 mapping almost verbatim; compress.
- Definition 1 "confidence is a per-attribute map" vs 5.2 "confidence generally remains metadata" vs Table 3 "recovery extension": decide whether confidence is written to FHIR and say once.
- [23] accessed 9 Aug 2026 vs others 4 Sep 2026; harmonize. [51],[64] are author preprints; say "preprint" in text.
- Keyword "care-process automation" -> "workflow automation".
- Highlights file required (separate file) - TODO.
- "exactly the failures that would reach a patient" slightly rhetorical -> "the failures that matter clinically".

## 8. Verdict on readiness
Close to the AIIM Position-paper bar. Problem framing, ACR-as-target argument, FHIR/NLP differentiation, per-record evaluation design, and honest qualitative use of the two companion studies are all at the journal's level, and the writing is confident without over-hedging. What still blocks acceptance: the declared novelty (set-level intent reasoning) is the least specified part (no definition of relations, two degenerate measures, no worked demonstration, no companion evidence, no engagement with AIIM temporal-planning literature), plus the companion-study disclosure/consistency items and ACR schema inconsistencies. All text-level. "I would expect to recommend acceptance once W1-W4 are addressed and the reference numbering is corrected."
