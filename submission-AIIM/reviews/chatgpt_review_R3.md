:::writing{variant="document" id="41827" title="AIIM Third-Round Confirmation Review"}
# Third-round confirmation review

## (A) Updated recommendation: **Minor revision**

The manuscript is now very close to acceptance, and the substantive conceptual issues that originally justified major revision have been addressed. The authors have correctly narrowed the clinical-NLP contrast, qualified the layer model, acknowledged FHIR `RequestOrchestration`, added the RequestIntent subset qualification, improved the safety semantics, strengthened Table 5, moderated the empirical claims, and corrected the conformal-prediction wording. However, I cannot yet recommend Accept because **three of the explicit accept-list items are only partially resolved**: (i) recovery state and FHIR request lifecycle remain conceptually distinguished but still occupy one ACR `status` field; (ii) the supposedly reproducible alignment rule still lacks the actual cost function/weights and minimum threshold; and (iii) the worked scoring example still calls an unsupported unmatched prediction “therefore unsafe” without stating that it crossed the autonomous-execution threshold, contradicting the revised definition immediately above. These are narrow fixes and require no new experiments or conceptual restructuring.

---

# (B) Verification of the seven accept-list items and three additional notes

## 1. Remove residual “clinical NLP = concept indexing” from the abstract

**RESOLVED.**

The abstract now says:

> “separate from clinical language processing, which scores extraction targets independently”

rather than claiming that clinical NLP merely indexes concepts. 

This is consistent with Section 5.3, which explicitly recognizes extraction of concepts, events, temporality, action items, and medical decisions.

---

## 2. State that the four RequestIntent values are a subset of FHIR RequestIntent

**RESOLVED.**

Definition 1 now explicitly states:

> “a subset of FHIR RequestIntent: proposal, plan, order, or option”

and Table 3 repeats:

> “proposal, plan, order, option: a subset.”  

This removes the previous standards-precision problem.

---

## 3. Separate recovery/verification state from FHIR request status

**PARTIALLY RESOLVED.**

The manuscript now explicitly distinguishes the two semantics:

> “the ACR's status attribute keeps two state machines distinct: a recovery state (recovered, then confirmed on review) and, once confirmed, the FHIR request lifecycle (active, then completed or revoked)”

and Table 3 says the states are “mapped, not identical.”  

That is a substantial improvement, but it does **not literally separate them in the ACR schema**. There remains one tuple element, `status`, that apparently changes vocabulary from `recovered/confirmed` to `active/completed/revoked`.

This is awkward because these are orthogonal properties: a recovered ACR could be confirmed while the corresponding clinical request is still draft, active, on-hold, or revoked.

**Required final fix:** either use two fields, e.g. `recovery-state` and `workflow-status`, or explicitly define `status` as a structured pair:

`status = <recovery_state, workflow_status>`

The current phrase “one status attribute keeps two state machines distinct” does not actually specify how that distinction is represented.

---

## 4. Reconcile autonomous-execution safety throughout Section 7

**PARTIALLY RESOLVED.**

The main definition is now correct:

> “An output is operationally unsafe when a record crosses the autonomous-execution threshold... A record deliberately held below that threshold and routed to review is not unsafe for having abstained.” 

The alignment paragraph is also corrected:

> “an emitted actionable record with no span that expresses it is an unsupported recovery, unsafe only if it crosses the autonomous-execution threshold.” 

However, the worked scoring box still says:

> “P2 is unmatched, a false positive that is also unsupported and therefore unsafe”

without saying that P2 crossed the autonomous-execution threshold. 

That sentence contradicts the revised definition.

**Required final fix:** change it to, for example:

> “P2 is unmatched and unsupported; if emitted above the autonomous-execution threshold it is also operationally unsafe.”

Or explicitly state in the Prediction row that P2 was emitted above threshold.

---

## 5. Make Table 5 reproducible: alignment cost/threshold, dependency precision, licensed inference, branch-aware schedules

**PARTIALLY RESOLVED.**

Three of the four requested subitems are now satisfactorily addressed.

**Dependency precision — resolved.** Table 5 now specifies:

> “precision, recall, and F1 ... over relation, anchor, offset, and resolution state.” 

**Licensed inference — resolved.** Unsupported attributes are now defined as values:

> “neither grounded in the source nor licensed by a stated inference rule.” 

**Branch-aware schedule evaluation — resolved.** Schedule agreement is now:

> “evaluated per feasible branch of the conditions.” 

**Alignment cost/threshold — still not fully resolved.** The manuscript now says:

> “optimal bipartite matching under a fixed cost (agreement on the action and the coded target, source-span overlap as tiebreak) with a minimum-agreement threshold”

but it still does not specify the actual cost formula, weights, or threshold value. 

Calling a cost “fixed” does not make it reproducible unless the fixed rule is given.

For example, the paper could define:

- action match = 2 points,
- target match = 1 point,
- span overlap only breaks exact score ties,
- candidate pair admissible only if action matches or score ≥ specified threshold.

Any explicit deterministic rule is acceptable. As written, two implementations could choose different weights and thresholds and produce different alignments.

---

## 6. Moderate “close to solved” and absolute “binding constraint” language

**RESOLVED.**

The revised text now states:

> “recognizing an action type from its span was substantially easier than recovering an executable one”

and:

> “In these studies, executable correctness, not type accuracy, was the dominant constraint.”



This is appropriately bounded to the actual companion-study evidence and no longer overclaims general task saturation.

---

## 7. Qualify the conformal-guarantee sentence

**RESOLVED.**

Section 6 now says:

> “a held-out calibration set supports an abstention rule with finite-sample guarantees on a pre-specified loss under exchangeability”

before distinguishing conformal coverage from conformal risk control. 

This is considerably more precise and addresses my prior statistical objection.

---

# Additional note 1. Narrow the categorical FHIR wording in Sections 5.2/5.3

**RESOLVED.**

Section 5.2 now explicitly acknowledges:

> “FHIR can group related requests (through RequestOrchestration)”

and draws the correct distinction: FHIR holds structured results rather than providing the recovery procedure from communication. 

Section 5.3 similarly says interoperability standards:

> “hold structured results rather than recover them”

rather than claiming they merely represent independent resources. 

This is the appropriate novelty boundary.

---

# Additional note 2. Import the CPOE/order-entry qualification into Section 2

**RESOLVED.**

Section 2 now explicitly states:

> “The layers organize computational objects rather than assert a strict succession: order entry and care plans already make selected patient-specific intent computable, and the frontier is the large residual that remains in communication.” 

This substantially improves the defensibility of the “third layer” framing.

---

# Additional note 3. Correct worked-example wording from “actor unresolved” to “accountable owner unresolved”

**RESOLVED.**

The worked example now says:

> “its accountable owner is left unresolved”

and correctly distinguishes ownership from requester/performance roles. 

---

# (C) Remaining or newly introduced problems

There are three items I would correct before acceptance.

### C1. The worked scoring example still violates the revised safety definition

As noted above:

> “P2 is unmatched, a false positive that is also unsupported and therefore unsafe”

is no longer correct under the paper's own definition unless P2 crossed the autonomous-execution threshold. 

This is a direct internal inconsistency and should be fixed.

### C2. The alignment rule is still not actually reproducible

The newly added phrase:

> “under a fixed cost ... with a minimum-agreement threshold”

sounds formal but leaves both the cost and threshold unspecified. 

This is particularly noticeable because the Conclusion says the framework is:

> “specified fully enough to implement, test, extend, or refute”

and Data Availability says it is:

> “fully specified in the text.” 

Those claims are slightly too strong until the matching rule is explicit.

### C3. The status fix remains representationally ambiguous

The revision says one `status` attribute “keeps two state machines distinct,” but the ACR tuple still exposes only a single `status` component.  

This is not merely stylistic because recovery confirmation and operational request state can coexist rather than occur sequentially as one vocabulary.

A two-component status representation would remove the ambiguity cleanly.

### Very minor wording issue

The worked scoring reference still says:

> “repeat CBC ... (actor unresolved)”

although the revised schema now specifically means **owner unresolved**, not all actor roles. 

This is a trivial copyedit but should be made consistent with the earlier worked example.

I found no new major conceptual, factual, or logical problem elsewhere in the revised manuscript.

---

# (D) Is this now ready to submit to AIIM?

**No — not quite as the final acceptance-ready version.**

It is at the **very narrow minor-revision stage**. I would require only three substantive text/schema clarifications before recommending acceptance:

1. make recovery state and workflow status structurally distinct;
2. give the actual deterministic alignment cost/threshold rather than merely saying one exists;
3. fix the worked scoring sentence so “unsupported” does not automatically mean “operationally unsafe.”

After those changes, I would recommend **Accept / Accept with trivial copyedits**. No further experiments, literature expansion, or conceptual restructuring are needed.
:::