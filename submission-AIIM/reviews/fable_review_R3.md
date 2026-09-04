# Fable AIIM Position-Paper Re-review (R3)
## "Computable Clinical Intent: Recovering Executable Care Actions from Clinical Communication"

Reviewer: simulated top-tier AIIM Position Paper reviewer (Fable model), full re-read of the R3 index.html.

## 1. Recommendation: Minor revision (very close to Accept with minor revision)

The revision resolves the structural asymmetry that blocked R2. Set-level intent reasoning is now defined over ACR tuples, tied to a named constraint formalism, and grounded in Asbru/Shahar, PROforma/GLIF, and temporal-constraint-network literature; the degenerate Table 5 measures were redefined against the reference; the scoring box exercises a second message; the companion paragraph discloses synthetic data, two studies, R4/R5, and the anchor-selection boundary; the ACR schema is internally consistent on origin, derived readiness, and status crosswalk. What keeps it from a clean accept is a small number of newly exposed, text-level (not cosmetic) defects, listed as W1-W9, plus two journal requirements (first-appearance citation order; Highlights file). "I would expect to recommend acceptance once W1 to W5 and W9 are addressed."

Automated checks: abstract 246 words; all 70 references cited; zero em-dashes/double-hyphens; no apologetic register; citation numbering still NOT first-appearance (8 out-of-order steps); no Highlights file; the 5.1 paragraph at line 212 ("Framing the ACR as a target...") lacks a closing </p>.

## 2. Resolution of prior (R2) blockers
- W1 (set-level under-specified/ungrounded): RESOLVED in substance, one definitional flaw (see R3-W1).
- W2 (degenerate measures / no set-level demo): PARTIALLY RESOLVED (three measures fixed; "Schedule agreement" still vacuous; box scores asserted not derived).
- W3 (companion disclosure): RESOLVED, two residual gaps (synthetic size; 88.4%-of-what).
- W4 (schema inconsistency): RESOLVED (one residual: ACR 2 scalar confidence on an all-extracted record).
- W5 (CPOE residual): PARTIALLY RESOLVED (named, not sized).
- W6 (interface/calibration): RESOLVED (conformal claim imprecise, see R3-W5).

## 3. Strengths
S1 recovery-target framing airtight (5.1). S2 set-level paragraph says what is inherited vs new (5.3). S3 worked example is a genuine instance of the definition. S4 alignment/consequence/annotation make Section 7 a usable spec. S5 regulatory paragraph sharp. S6 companion evidence bounded. S7 taxonomy short, CPOE residual named.

## 4. Remaining weaknesses (path to accept = W1-W5 + W9)

**R3-W1. Contradiction definition does not cover its own example and over-flags serial orders (5.3).** "Two ACRs contradict when they share an action and target but carry incompatible temporal or status values; ... 'hold' against 'continue' the same drug is a contradiction ... resolved by recovery time, speaker authority, or clinician review." (a) hold/continue do NOT share an action (opposed actions, same target). (b) "CBC at one week" vs "at two weeks" are two serial orders unless the second supersedes; the rule needs cardinality/recurrence or communication-time ordering. (c) precedence should be COMMUNICATION time, not recovery time. Fix: define contradiction as same target with mutually-exclusive actions (a stated exclusion relation, e.g. hold/continue, cancel/perform) OR same action+target with temporal constraints that cannot both hold for a single-occurrence intent; define revision as later-communicated ACR replacing the earlier on same action+target (map to FHIR ServiceRequest.replaces, status revoked); state precedence (later communication time, then speaker authority, else review).

**R3-W2. Alignment rule contradicts the scoring box on invented attributes (7).** Rule: "Optional attributes are scored only where the reference populates them, so a system is neither rewarded for inventing an actor the source does not state nor penalized for leaving one unresolved." Box: "actor wrong (cardiology for an unstated owner)" contributes to unsafe. Under the rule the invented actor would NOT be scored. Fix: add a fourth outcome: where the reference leaves an attribute unresolved, a prediction that populates it is an unsupported-attribute error (counts toward unsafe); a prediction that also leaves it unresolved is correct.

**R3-W3. "Schedule agreement" still degenerate for the empty plan; second-message scoring asserted not derived (Table 5, box).** Empty prediction is satisfiable and vacuously consistent. Fix: define over reference pairs (fraction of reference ordered pairs whose relative order is reproduced; unrecovered pairs = disagreement; satisfiability a separate boolean). In the box, state what the system emitted for message 2, then derive the 0-of-1 scores. Align names: Table 5 "Contradiction detection" vs box "contradiction and revision detection".

**R3-W4. The second-message example creates the orphan-dependency hazard the framework claims to catch, and the box does not notice it (5.3, box).** "hold the CBC until after the cardiology visit" makes the CBC depend on a visit that only happens if palpitations recur, so in one branch the CBC is never due: an orphan/branch-unsatisfiable dependency. (a) The box should show the REFERENCE plan triggering a consistency flag ("CBC gated on a visit that may not exist"), which strengthens the set-level demo. (b) Conditional ACRs make this a conditional/disjunctive temporal problem, not a plain STP; "scheduling treats event-anchored temporal constraints as a simple temporal problem whose consistency is decidable [69]" is correct only for UNCONDITIONAL constraints. Fix: say unconditional constraints form an STP (consistency in polynomial time), conditional actions require per-branch consistency (a conditional temporal problem); cite Tsamardinos, Vidal, Pollack (2003) or scope to the unconditional subset.

**R3-W5. Conformal claim stronger than the citation supports (6).** "a distribution-free guarantee on the selective-risk curve follows from conformal prediction [70]." Split conformal guarantees marginal COVERAGE, not selective RISK. Fix: cite conformal risk control (Angelopoulos, Bates, Fisch, Lei, Schuster) alongside [70], or rephrase to "a distribution-free bound on the abstention threshold via conformal calibration."

**R3-W6. Residual companion disclosure (7).** (a) synthetic corpus size not given; (b) which five corpora / synthetic share not stated; (c) 88.4% of which field over how many items, and the stratum share; (d) delete the dangling "the framework's value rests on its constructs" after "This is direct evidence..."; also state which Table 5 measures each study instantiates (Study 1 ~ whole-record exact match on closed fields; Study 2 ~ temporal-normalization error + per-pair linking F1).

**R3-W7. Falsification test tilted (8).** A per-item extractor emits no contradiction pairs, so it scores 0 on contradiction detection by definition. Fix: restrict falsification measures to individuation, constraint recall, and schedule agreement, or specify the baseline as extraction plus off-the-shelf plan checking. Also fix name "schedule feasibility" -> "schedule agreement".

**R3-W8. Worked-example actor asymmetry + one wrong origin flag (5.1).** ACR 2 "actor: PCP ... origin: extracted" but the PCP is inferred from the addressee, not extracted verbatim -> origin should be inferred; add one sentence on why one actor resolves and the other does not (or make both unresolved-with-candidate).

**R3-W9. Journal requirements.** (a) First-appearance citation order (Vancouver): 8 out-of-order steps. (b) No Highlights file (3-5 bullets, <=85 chars). Both mechanical.

## 5. Minor issues (selected)
- 5.1 line 212 paragraph missing closing </p> (check build).
- Figure 2 legend "outlined = optional" conflicts with confidence being always-carried metadata; use three classes (required / optional content / always-carried metadata); origin flag not drawn.
- ACR 2 scalar confidence 0.95 on all-extracted record vs Def 1 "reported for inferred attributes"; make per-attribute or allow record-level confidence.
- ACR 2 "temporal: on-condition" not among the four forms (absolute/relative/event-anchored/recurring); call it event-anchored on the trigger.
- Confidence write-back: Table 3 "recovery extension" vs 5.2 "metadata of the recovery system"; state once whether written to FHIR.
- Table 3: add ServiceRequest.replaces to dependency row (revision now defined); status row list "revoked".
- Table 4 "Set-level coherence: yes" for ACR -> "specified (5.3)" (coherence is a framework property, not a per-action schema field).
- Table 5 individuation: report split/merge RATES per reference intent (unnormalized count not comparable). Delete "so that omission is penalized rather than rewarded" (reads as reviewer reply).
- 5.3 "consistency is decidable [69]" -> STP consistency is polynomial.
- Section 4: quantify CPOE residual with the [3] range so "often fails" has a number.
- Section 6: add that verbalized/token-level confidences are poorly calibrated for LLMs (motivates conformal).
- Section 7 provenance "above threshold": threshold still unstated.
- Section 8: say which of the two studies "moving from synthetic corpora..." refers to.
- [29],[39] arXiv without "preprint" label; harmonize with [51],[64].
- Section 1 apposition "its distinct and unmet object" dangles; rewrite.
- Trim rhetorical tails ("the framework's value rests on its constructs").

## 8. Verdict
At the AIIM bar in substance. Blocking only: contradiction definition that misses its own example (W1), scoring rule vs box contradiction (W2), one still-vacuous measure + asserted box scores (W3), orphan-dependency in the second-message example + STP over-scope (W4), over-strong conformal claim (W5), and the two mechanical journal items (W9). All fixable in one editing pass, no new experiments. Acceptance expected once W1-W5 and W9 are addressed.
