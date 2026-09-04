:::writing{variant="document" id="73142" title="AIIM Re-Review — Revised Position Paper"}
# Re-review of “Computable Clinical Intent: Recovering Executable Care Actions from Clinical Communication”

## (A) Updated recommendation: **Minor revision**

The revision is substantially improved and, in my view, has crossed the threshold from a manuscript requiring major conceptual repair to one requiring **targeted minor revision**.

The authors have addressed several of the most important problems in the previous version: the ACR now includes request-intent; actor semantics are role-tagged; the erroneous use of `ServiceRequest.owner` has been corrected; computed values are distinguished from inferred ones; dependency anchors are typed; autonomous execution rather than abstention defines operational unsafety; and the set-level hypothesis is now explicitly separated from the broader intent-recovery hypothesis. Most importantly, Section 5.3 now states the novelty much more defensibly: existing clinical guideline and temporal-plan formalisms already perform plan-level reasoning over curated inputs, whereas the proposed problem is to perform such reasoning over a **recovered, uncertain, partially unresolved set**. 

I would no longer recommend major revision. However, I would also not accept the paper as-is. Several residual issues remain, including one important unresolved issue from my previous review: **Table 5 is still not sufficiently specified to justify the manuscript's repeated claim that the evaluation framework is “fully specified.”** The recovery-status/FHIR-status conflation also remains. There are additionally two smaller inconsistencies introduced or exposed by the revisions: the manuscript gives only a subset of the FHIR RequestIntent code system while presenting it as the FHIR-aligned set, and the abstract still contains the old reductive characterization of clinical NLP that the body has correctly softened.

These are fixable without another conceptual redesign or new experiment.

---

# (B) Disposition of the previous major concerns

## 1. Historical/ontological claim that clinical intent is a new “third layer”

**PARTIALLY RESOLVED.**

The manuscript now clearly acknowledges that structured patient-specific intent already exists: “Computerized order entry already makes computable the intent a clinician structures at entry; the residual this layer targets is intent that is communicated but never ordered.” This is exactly the qualification that was needed. 

However, the stronger historical rhetoric remains in Sections 2 and 9:

> “In the field's documented history ... that unit has been the record and then the clinical fact; we argue the next is patient-specific intent.”

and:

> “Health IT has made the record and then the clinical fact computable; we take the position that patient-specific clinical intent is the next layer...”  

This is now defensible if read as a **conceptual frontier**, but it is still not literally a historical succession because CPOE, prescriptions, orders, CarePlans, and task systems have made selected patient-specific intentions computable for decades.

**Required minor fix:** explicitly state once in Section 2 that the three layers are a conceptual organization of computational objects, not a claim that no Layer-3 objects existed before Layer 2 matured. The current Section 4 qualification should be imported into the layer-model section itself.

---

## 2. Overstatement that clinical NLP merely “indexes concepts”

**PARTIALLY RESOLVED.**

The Introduction is substantially better:

> “...separate both from the clinical natural language processing that scores extraction targets independently...”

and Section 5.3 now accurately recognizes extraction of concepts, events, temporality, action items, medical decisions, and orders. Table 4 also explicitly states that “no” means “not required by that task or schema,” rather than “not representable.”  

But the **abstract was not updated consistently** and still states:

> “...separate from clinical language processing, which indexes concepts...”



The first worked example also retains:

> “Layer 2 recognizes ‘CBC’ and ‘cardiology’ as concepts...”



The latter can survive as an illustrative simplification, but the abstract cannot: it reproduces the exact overstatement the revision otherwise fixes.

**Required fix:** use the Introduction's more accurate distinction in the abstract.

---

## 3. Missing FHIR request-intent and overclaim that an ACR “is” a draft FHIR request

**PARTIALLY RESOLVED, with the substantive issue fixed.**

The major problem is corrected. `request-intent` is now a required ACR field; the manuscript explains why “consider,” “recommend,” and “order” differ operationally; Table 3 maps the field to `ServiceRequest.intent`; and the earlier statement that a completed ACR simply “is” a FHIR request has appropriately become:

> “a sufficiently populated ACR carries most of the semantics needed to construct a draft FHIR request, once patient context and profile-specific mandatory fields are supplied.”

 

There is, however, a new standards-precision issue. The paper states that FHIR RequestIntent comprises:

> “proposal, plan, order, or option”

whereas FHIR R5's required RequestIntent value set also includes `directive`, `original-order`, `reflex-order`, `filler-order`, and `instance-order`. 

This is easily fixed by either listing the complete FHIR value set or saying explicitly that the ACR initially uses a **restricted subset** of RequestIntent.

---

## 4. `actor` conflated requester, accountable owner, and performer; incorrect `ServiceRequest.owner`

**RESOLVED.**

The revised definition now makes actor “a role-tagged set” separating requester, accountable owner, and performer, and Table 3 correctly distinguishes `ServiceRequest.requester`/`performer` from `Task.owner`.  

The worked example also correctly maps the CBC to a `ServiceRequest` plus a companion follow-up `Task`, explicitly stating:

> “a ServiceRequest carries requester and performer, not an owner.”



One sentence should nevertheless be cleaned up. The subsequent paragraph says:

> “The discharge summary does not say who orders the repeat CBC, so its actor is left unresolved...”

This reverts to singular “actor” language even though only the **owner/accountability role** is unresolved while performer and requester have separately been populated. 

That is a wording inconsistency, not a remaining schema defect.

---

## 5. Recovery status versus FHIR lifecycle status; extracted/inferred provenance

**PARTIALLY RESOLVED.**

The provenance/origin problem is resolved. Values are now explicitly classified as:

- extracted,
- deterministically computed,
- inferred.

The worked example correctly identifies the temporal value as computed.  

However, the **status problem remains essentially unchanged**. Section 5.1 still says:

> “the ACR's status attribute records the operational lifecycle of the recovered action, from recovered and confirmed to active and then completed or cancelled”

and then maps `recovered` and `confirmed` onto FHIR `draft`. Table 3 meanwhile presents ACR `status` simply as FHIR `.status`. 

These are two distinct state machines:

1. recovery/verification state: recovered, reviewed/confirmed;
2. workflow/request lifecycle state: draft, active, on-hold, completed, revoked, etc.

My previous recommendation was to separate them. That has not been done.

**Required fix:** introduce a separate `recovery-state`/`verification-state`, or state that `status` is an ACR-internal state and is mapped rather than identical to FHIR status. The current Table 3 presentation is internally inconsistent with Section 5.1.

---

## 6. Novelty of set-level reasoning versus FHIR/CIG/temporal-plan formalisms

**PARTIALLY RESOLVED, and substantially improved.**

The crucial conceptual correction has been made. Section 5.3 explicitly acknowledges that Asbru, PROforma, GLIF and related formalisms already perform temporal and task-network reasoning over structured inputs, then states:

> “What is new is performing it over a recovered, uncertain, and partially unresolved set...”

This is the right novelty claim. 

However, Section 5.2 still contains an unnecessarily categorical formulation:

> “FHIR represents each ServiceRequest or Task independently...”

followed later by:

> “Neither ... interoperability standards, which represent resources independently, provide this set-level reasoning...”

 

This sits awkwardly beside the paper's own Table 3 use of `RequestOrchestration`, which explicitly exists to coordinate related requests.

The defensible distinction is no longer that FHIR lacks grouped requests or that CIG systems lack set reasoning. It is that **FHIR represents the result but does not recover/reconcile it from noisy communication**, while CIG reasoning generally assumes deliberately authored structured plans.

**Required fix:** make Section 5.2 use the same careful formulation as the final sentence of Section 5.3.

---

## 7. “Executable correctness” was not literally executable

**PARTIALLY RESOLVED.**

This revision is conceptually important. Section 5.1 now defines what “running” an ACR set means:

> “resolving the plan it implies against a patient timeline, its enabled and disabled actions, due intervals, owners, ordering, and any detected inconsistency.”



That makes the semantic-parsing analogy considerably more credible.

Nevertheless, the evaluation framework does not yet fully operationalize that execution semantics. Table 5 still evaluates slot correctness, relation recovery, contradiction F1, and pairwise schedule agreement; it does not define an explicit metric comparing the **resulting enabled/disabled action set**, branch-dependent execution consequences, resulting due intervals, or executed ownership assignments against a reference plan. 

Thus the paper now defines the idea of execution, but not a complete executable semantics in the SQL-like sense implied by:

> “recovery measurable by what the structure implies when run.”

I would retain the term “executable correctness,” but either add one explicit **plan-consequence agreement** measure or soften the claim that this has been fully specified.

---

## 8. Formal specification of Table 5

**NOT RESOLVED.**

This is the main remaining technical weakness.

The same four issues raised in my previous review remain visible.

### 8.1 Alignment objective remains underspecified

The manuscript says bipartite matching “maximizes agreement on action and target, with source-span overlap as the tiebreak,” but does not define the scoring weights, lexical/semantic equivalence rules, threshold for allowing a match, or behavior when repeated same-action/same-target intentions occur. 

This is not sufficient for two independent benchmark implementations to guarantee the same alignment.

### 8.2 Dependency recovery is recall-only

Table 5 still defines:

> “Constraint and dependency recovery — recall of the reference's timing, ordering, and dependency constraints.”



A system could invent ten false dependencies while recovering all true ones and receive perfect recall.

At minimum, use precision/recall/F1, or add an unsupported-constraint rate.

### 8.3 Schedule agreement remains insufficiently branch-aware

The metric remains pairwise relative-order agreement. 

But the manuscript's own worked example contains conditional branching: the cardiology visit occurs only if palpitations recur. A meaningful executable schedule therefore depends on a branch or trigger valuation.

The metric should specify schedule comparison **per feasible branch/scenario**, including unresolved anchors and concurrency.

### 8.4 “Unsupported attribute” still conflicts with legitimate inference

The manuscript says:

> “an attribute the source does not state, populated anyway, is an unsupported-attribute error”

yet the ACR explicitly permits inferred owner values, and the worked example infers the PCP owner from the addressee.  

The correct rule is not “not literally stated = unsupported.” It should be:

> an attribute is unsupported if it is neither directly grounded nor licensed by a documented derivation/inference rule and supporting context.

This matters because the paper now explicitly distinguishes extracted, computed, and inferred origin types.

These changes are local but necessary if the manuscript retains the claim in the Conclusion and Data Availability section that the framework is “fully specified.” 

---

# Citation issue 1: incorrect CIRCA arXiv identifier

**RESOLVED as to the original error.**

The incorrect arXiv identifier has been removed. Reference [69] now identifies the CIRCA work as a 2026 manuscript and provides the Zenodo dataset DOI rather than falsely assigning another paper's arXiv number. 

One residual issue remains: Section 7 reports numerous quantitative results from [69], but the cited item is now merely “Manuscript; 2026.” If that manuscript is not publicly accessible at submission, the reader cannot independently verify the reported 88.4%, 85–91%, and 18–35% results from the citation alone. The Zenodo dataset citation establishes the dataset, but not necessarily the experimental claims.

This is not the previous factual citation error, but the editor should require a stable manuscript/preprint reference if the quantitative companion-study claims remain central.

---

# Citation issue 2: outdated FDA CDS guidance and categorical regulatory claim

**RESOLVED.**

Reference [67] now correctly cites the **January 2026** revision of FDA's Clinical Decision Support Software guidance, and the text has been softened from a categorical device-classification statement to:

> “Software a clinician cannot independently review may constitute device software; in particular, time-critical recommendation functions generally do not qualify for the Non-Device CDS exclusion...”

 

FDA's official page confirms that the final CDS guidance is dated January 2026. 

This adequately addresses my previous concern.

---

# (C) Remaining or newly introduced weaknesses

## C1. The abstract still contains language that the body has explicitly corrected

This is the most obvious editorial inconsistency introduced by an incomplete revision.

The abstract says:

> “clinical language processing, which indexes concepts”

whereas Section 5.3 correctly says clinical NLP extracts “concepts, events, and temporality” and includes physician action-item and medical-decision extraction.  

This should be corrected before publication because readers and editors will judge the novelty claim primarily from the abstract.

---

## C2. The RequestIntent enumeration is presented as FHIR-complete when it is not

Definition 1 and Table 3 say RequestIntent is:

> “proposal, plan, order, or option.”

 

FHIR R5 also includes `directive`, `original-order`, `reflex-order`, `filler-order`, and `instance-order`. 

The paper has two reasonable choices:

- use the complete FHIR RequestIntent value set; or
- define an ACR-specific reduced vocabulary and map it explicitly to FHIR RequestIntent.

What it should not do is call the four-value list simply “aligned to FHIR RequestIntent” without noting that it is a subset.

---

## C3. `status` remains semantically overloaded

As noted above, this is the main schema issue still left from the first review. A record being “recovered” is not the same type of state as a clinical request being “active.” 

The new request-intent and actor distinctions make this inconsistency more conspicuous because the rest of the schema is now much more carefully role-separated.

---

## C4. The actor revision is correct, but the worked-example prose partially slips back to the old model

The structured ACR says:

> “performer=lab, owner unresolved”

while the mapping identifies the discharging team as requester. Immediately afterward, however, the explanation says:

> “its actor is left unresolved.”



It should say “its accountable owner is unresolved.”

Also, if the discharging team is asserted as `requester`, the manuscript should be clear that this means the **source/authorizing requester of the recovered plan**, not necessarily the person who will later enter the laboratory order. The current wording “does not say who orders” could otherwise be read as contradicting the assigned requester.

---

## C5. The typed dependency revision is good, but Table 5 does not exploit it

The definition now usefully specifies that a dependency can point to:

- another ACR,
- clinical event,
- encounter,
- result,
- future trigger,

with offset and resolution state. 

This resolves an important representational weakness.

However, Table 5 continues to score all dependency recovery under a single undifferentiated recall measure. 

Since the dependency schema is now richer, evaluation should at least specify correctness of:

`relation + anchor type/reference + offset + resolution state`.

Otherwise the framework cannot distinguish “correct dependency type, wrong event anchor” from a correct executable constraint.

---

## C6. The autonomous-execution safety definition is now conceptually correct, but one earlier sentence still uses the old unsafe-output rule

Section 7 now correctly says:

> “A record deliberately held below that threshold and routed to review is not unsafe for having abstained.”



That resolves my previous concern.

But the preceding alignment paragraph still says an unmatched prediction with no supporting span is:

> “additionally counted as an unsafe output”

without conditioning this on crossing the autonomous-execution threshold. 

Those definitions should be harmonized. An unsupported hallucinated candidate held below threshold may be a false positive/recovery error, but under the paper's new definition it is not yet **operationally unsafe**.

---

## C7. The conformal-prediction wording from the prior review remains unrevised

Although this was outside the user's numbered 1–8 list, it remains a technical issue from the previous report.

Section 6 still states:

> “conformal calibration supplies the abstention threshold, with a distribution-free coverage guarantee”

and that conformal risk control “gives the selective risk at any chosen coverage.” 

This is still too compressed. Conformal guarantees require assumptions such as exchangeability and apply to a specified prediction set or loss/risk-control construction; conformal prediction is not a generic mechanism that transforms arbitrary LLM confidence into calibrated uncertainty.

A short qualification would suffice:

> “A held-out calibration set can support an abstention/risk-control rule with finite-sample guarantees on a pre-specified loss under exchangeability assumptions.”

I would regard this as a minor technical correction, not a publication-blocking conceptual issue.

---

## C8. The companion-study interpretation remains slightly too strong

The manuscript still concludes:

> “recognizing an action type from its span is close to solved”

and:

> “Executable correctness, not type accuracy, is the binding constraint.”



I remain unconvinced by “close to solved” based on 85–91% action accuracy in one harmonized benchmark and near-perfect action recognition in a controlled synthetic study.

The safer and empirically supported statement is:

> “action-type recognition was substantially easier than complete executable recovery in both companion studies.”

Likewise “the binding constraint” should be “the dominant constraint in these experiments.”

This wording change would strengthen rather than weaken the position.

---

## C9. The falsifiability section is now logically sound

This was a significant improvement and I find no remaining problem with it.

The revised paper now distinguishes:

1. whether intent recovery itself is a distinct task; and
2. whether explicit set-level reasoning adds value.

It correctly states:

> “Failure of the second claim leaves the recovery task standing; only failure of the first would retire the layer.”



This resolves the logical error in the previous version.

---

## C10. “Normative / intended / observed” is a clear improvement

Replacing “prescribed” with “normative” removes the medical ambiguity between a guideline recommendation and a patient-specific prescription. The revised Table 2 now cleanly distinguishes normative protocol, patient-specific intended process, and observed process. 

I consider this resolved.

---

# (D) Does the manuscript now meet the AIIM Position Paper bar?

**Yes, subject to minor revision.**

The revised manuscript now has the elements I would expect from a publishable AIIM Position Paper:

- an important clinical information-processing problem;
- a clearly articulated position;
- engagement with clinical NLP, interoperability, clinical workflow, temporal reasoning, and safety literature;
- a concrete representation that can be implemented and challenged;
- a defensible differentiation from FHIR: **FHIR can represent structured intent; the proposed AI problem is recovering and reconciling intent before it reaches FHIR**;
- a defensible differentiation from CLIP, MedDec, and MEDIQA-OE: not that those tasks are “mere concept extraction,” but that they do not require the full operational bundle of normalized time, accountable responsibility, conditional/dependency semantics, uncertainty/provenance, and recovered-plan coherence;
- an explicit acknowledgement that set-level workflow reasoning itself is not new in CIG systems;
- a testable research agenda;
- clear falsifiability conditions;
- an appropriate acknowledgement that real-world validation and the set-level benchmark remain future work.

The paper also correctly states that its strongest distinctive set-level claim has **not yet been demonstrated by the companion studies**:

> “the set-level measures remain to be instantiated on recovered plans...”



That is acceptable for a Position Paper and should not trigger a demand for new experiments.

My remaining objections no longer challenge the central thesis. They concern internal consistency and the precision required to make the schema/evaluation framework genuinely reproducible. In particular, I would require before acceptance:

1. remove the residual “clinical NLP = concept indexing” sentence from the abstract;
2. clarify that the four RequestIntent values are a subset or use the full FHIR set;
3. separate recovery/verification state from FHIR request status;
4. reconcile the autonomous-safety definition throughout Section 7;
5. make Table 5 reproducible by specifying alignment, dependency precision, licensed inference, and conditional/branch-aware schedule evaluation;
6. moderate “close to solved” and the absolute “binding constraint” language;
7. qualify the conformal-guarantee sentence.

With those changes, I would support acceptance as an AIIM Position Paper. The core argument is now substantially sharper than in the previous version: the manuscript no longer needs to claim that FHIR cannot represent intent or that clinical NLP cannot extract actions. Its publishable proposition is that **recovering uncertain, source-grounded patient-specific intent from clinical communication and converting the recovered set into a coherent, operationally testable plan is a distinct AI problem that existing extraction tasks and workflow representations each address only partially.**
:::