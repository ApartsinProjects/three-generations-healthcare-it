Below is the review I would submit to AIIM.

:::writing{variant="document" id="58314" title="Peer Review — Computable Clinical Intent"}
## Recommendation: **Major revision**

This is a thoughtful and potentially important position paper. Its strongest idea is not simply that clinical intent should be structured, because health IT standards and workflow systems have represented patient-specific requests and plans for decades. Rather, the manuscript identifies a more specific computational problem: **recovering patient-specific intended actions that remain latent in clinical communication, preserving their provenance and uncertainty, and then reasoning over the recovered set so that it can safely enter existing workflow infrastructure**. The proposed emphasis on set-level coherence and on evaluation of operationally consequential errors is valuable and well suited to *Artificial Intelligence in Medicine*.

However, several claims presently exceed what the conceptual analysis establishes. Most importantly, the manuscript sometimes defines clinical NLP too narrowly, understates the extent to which FHIR and computer-interpretable guideline systems already represent sets of intended actions, and overstates the completeness of the ACR-to-FHIR mapping. There are also substantive internal inconsistencies in the ACR schema, particularly the absence of FHIR request `intent`, the overloaded `actor` field, status semantics, provenance/origin semantics, and the meaning of “executable correctness.” The central set-level contribution remains a research proposal rather than something instantiated in either companion study. That is entirely permissible for a position paper, but the claims should reflect that status.

I therefore recommend **major revision rather than rejection**. The core position is defensible and interesting, but the paper needs conceptual tightening and several technical corrections before its novelty is sufficiently clear.

---

## 1. Core thesis: sound, but the novelty should be stated more narrowly

The paper's central organizing thesis is that health IT can be viewed through the unit made computable: record → clinical fact/state → patient-specific clinical intent. The proposed third unit is an intended action represented as an Actionable Clinical Record (ACR), with recovery followed by set-level reasoning. 

I find the **computable-intent problem sound**, but I am less convinced by the stronger historical claim that this constitutes a clean “third computational layer.” Patient-specific intent has long been explicitly computable whenever clinicians enter orders, care plans, tasks, prescriptions, or structured referrals. The manuscript itself correctly acknowledges this in Section 4: “Computerized order entry already makes computable the intent a clinician structures at entry.”  That acknowledgment significantly narrows what the proposed layer can mean.

The scientifically defensible novelty is therefore:

> **intent recovery from communication when the intent was not already structured**, followed by reconciliation of the resulting uncertain and partially specified patient-specific plan.

That is a strong research problem. It does not require the stronger historical proposition that “intent” has only now become a new unit of computability.

### Required fix

I would reframe Sections 2–4 so that the three layers are presented explicitly as a **conceptual decomposition of computational objects**, not as a strict historical sequence. Figure 1 and Table 1 can remain, but the paper should say that intent computation already exists in structured islands such as CPOE and CarePlan; the proposed frontier is **recovering the large residual of communicated-but-unstructured intent and reconciling it into operational workflow**.

Otherwise a skeptical reader can reasonably object that “Layer 3” existed before much of what the authors call Layer 2.

---

## 2. The distinction from clinical NLP is currently overstated

Several high-level sentences reduce clinical NLP to concept indexing. For example:

> “...separate from clinical language processing, which indexes concepts...”  

and:

> “Layer 2 recognizes ‘CBC’ and ‘cardiology’ as concepts; it does not bind them to repeat...”  

These are rhetorically effective but technically too strong. Clinical NLP includes event extraction, relation extraction, temporal relations, action-item extraction, recommendation extraction, semantic parsing, medical decision extraction, and order extraction. Indeed, Section 5.3 itself acknowledges this richer history and cites precisely those literatures. 

CLIP, for example, contains physician-annotated action-item spans and seven action classes, not merely “concept indexing.”  MEDIQA-OE also evaluates structured order properties and provenance, although much of its description/reason evaluation is overlap based. 

### Required fix

Replace the categorical distinction:

> clinical NLP = concepts  
> ACR = actions

with the more defensible one:

> existing clinical NLP tasks usually optimize **individual extraction targets**, whereas the proposed target requires a particular operational combination of action semantics, temporal resolution, responsibility, conditional/dependency structure, provenance, uncertainty, and plan-level coherence.

That is both more accurate and more novel.

Table 4 is useful, but its “no” entries should preferably mean **“not required by the task/schema”**, not “the paradigm cannot represent this.” This distinction matters scientifically.

---

## 3. The ACR is promising as a recovery target, but its FHIR alignment is currently incomplete

The Definition box is one of the paper's strongest devices. The ACR is explicitly framed not as a new interoperability standard but as a recovery target upstream of FHIR:

> “The ACR is not a new interchange format: it is a projection of FHIR workflow resources onto what must be recovered...” 

I support this framing. However, the subsequent statement

> “a completed ACR *is* a draft FHIR request”

is currently not technically justified.

### 3.1 Missing FHIR `Request.intent`

This is the most important schema omission.

FHIR `ServiceRequest.intent` is mandatory and is explicitly semantically important: it distinguishes proposal, plan, directive, order, etc.; HL7 describes it as a modifier because it changes how the other attributes are interpreted. `ServiceRequest.subject` is also mandatory. 

Yet Definition 1 contains:

`action, target, actor, temporal constraint, condition, dependency, status, provenance, confidence`

with **no request-intent/modality/authority field**. 

This is not merely a FHIR-compliance detail. Clinically,

- “consider repeating CT,”
- “recommend repeating CT,”
- “plan to repeat CT,” and
- “repeat CT”

do not have the same executable semantics.

The inconsistency becomes particularly visible in Section 7, where the companion benchmark apparently treats **FHIR request-intent as one of the critical closed fields**, despite request-intent being absent from the ACR itself. 

### Required fix

Add an explicit field such as `request_intent`, `commitment`, or `modality`, preferably aligned with FHIR RequestIntent, or explain rigorously how it is derived from other ACR attributes. I strongly favor making it explicit.

Also change “a completed ACR is therefore a draft FHIR request” to something like:

> “A sufficiently populated ACR contains most of the recovered semantics needed to construct a draft workflow request once patient context, request intent, resource type, and profile-specific mandatory fields are supplied.”

“Completed ACR” is also ambiguous because `completed` is itself an operational status.

---

## 4. `actor` collapses several clinically different roles

Definition 1 says that actor is the “accountable performer,” whereas Table 3 maps it to:

`requester / performer / Task.owner`. 

Those are not equivalent roles.

A clinician may request a CBC; a laboratory performs it; a PCP office may own the follow-up task. Section 5.3 itself correctly observes that “the ordering clinician, the performer, and the narrator can be three different people.” 

The current ACR nevertheless compresses them back into one `actor`.

The first worked example exposes the problem. The paper describes a draft `ServiceRequest` “whose owner is left unassigned.”  `ServiceRequest` does not have a `Task.owner`-style owner; requester and performer semantics are different. FHIR assigns `owner` to Task, not ServiceRequest. 

### Required fix

Replace the single actor with either:

`actor = <role, entity>`

allowing multiple actor-role pairs, or explicit fields such as:

- requester/authorizing party,
- responsible owner,
- intended performer,
- trigger observer when relevant.

At minimum, the ACR must distinguish **clinical responsibility for loop closure** from **physical performance of the requested service**.

This change would materially strengthen the manuscript because ambiguous responsibility is one of the clinical motivations of the entire paper.

---

## 5. Status and provenance/origin semantics need cleanup

### 5.1 ACR status is not simply FHIR `.status`

Table 3 states:

> “status → .status (draft, active, completed, revoked).”

But Section 5.1 defines an ACR lifecycle of:

> recovered → confirmed → active → completed/cancelled,

with recovered and confirmed mapped to FHIR draft. 

Thus ACR status is already **not identical to FHIR request status**.

Furthermore, FHIR Task and ServiceRequest have different lifecycle vocabularies. Task includes statuses such as requested, received, accepted, ready, in-progress, failed, and cancelled, whereas ServiceRequest uses draft, active, on-hold, revoked, completed, etc. 

### Required fix

Separate:

1. **recovery/verification state**: recovered, reviewed, confirmed;
2. **clinical request lifecycle state**: FHIR resource-specific status.

Do not place both in one field.

### 5.2 Extracted versus inferred is insufficient

The manuscript currently distinguishes values as “extracted verbatim or inferred.” Yet the central neuro-symbolic architecture computes dates deterministically.

For example, “two weeks” + discharge date → a concrete date is neither verbatim extraction nor ordinary inference. It is **derived/computed**.

I recommend at least:

- explicit/extracted,
- computed/derived,
- inferred,
- unresolved.

This would align the ACR much better with the architecture in Section 6 and would make provenance genuinely useful.

There is also a smaller inconsistency: Definition 1 says confidence is reported for inferred attributes, whereas Figure 2 says confidence is “always-carried metadata.”  Confidence should probably apply to all recovered semantic values, with deterministic computation inheriting uncertainty from its inputs.

---

## 6. Set-level reasoning is the manuscript's most interesting contribution, but the novelty needs sharper positioning

Section 5.3 is in my view the conceptual center of the paper. Individuation, conditioning, scheduling, revision, contradiction, cross-message reconciliation, and consistency checking are exactly where the problem becomes more than ordinary independent slot extraction. 

However, sentences such as

> “FHIR represents each ServiceRequest or Task independently...”

and

> “Neither ... interoperability standards ... provide this set-level reasoning”

need qualification.

FHIR R5 `RequestOrchestration` is specifically defined as a resource representing a **set of optional and related activities**, including conditions and explicit inter-action temporal relationships.  The manuscript itself invokes RequestOrchestration elsewhere.

Similarly, the paper correctly cites Asbru, PROforma, GLIF, temporal constraint networks, and other formalisms that already perform sophisticated plan-level reasoning over structured clinical plans. 

Therefore the novelty cannot be:

> nobody performs set-level clinical workflow reasoning.

The stronger and more accurate claim is:

> existing workflow formalisms reason over deliberately authored structured plans; the proposed scientific problem is to perform comparable reconciliation and consistency reasoning over a **recovered, uncertain, partially specified, provenance-linked plan derived from natural clinical communication**.

The manuscript reaches exactly this formulation at the end of Section 5.3. That sentence should become the organizing statement much earlier.

### Required fix

Revise Figure 3 to separate two operations inside the central box:

**communication → uncertain ACR graph → reconciliation/verification → FHIR/CIG/workflow infrastructure**

This would make the contribution visually unmistakable and prevent the appearance that FHIR lacks set representations.

---

## 7. “Executable correctness” is a good direction, but the current framework is not yet fully executable

I agree strongly with the motivation in Section 7. A model saying the correct words while assigning the wrong date or responsible party can be clinically dangerous, and conventional extraction scores can obscure this. The worked scoring box illustrates this very effectively. 

However, “executable correctness” presently remains largely a collection of structured accuracy metrics. The analogy in Section 5.1 with SQL execution is therefore somewhat stronger than warranted.

In executable semantic parsing, one can actually execute the predicted program and compare the resulting behavior/output. Here the proposed evaluation mostly measures:

- slot F1,
- exact match,
- date error,
- relation recovery,
- contradiction F1,
- schedule agreement.

These are valuable, but they do not yet define an execution semantics for the ACR.

### Required fix

Either rename the framework to something slightly less strong, such as **operational correctness**, or make “executable correctness” literal by defining a deterministic plan semantics.

For example, given a patient timeline and trigger assignments, an ACR set could execute to:

- enabled actions,
- disabled actions,
- due intervals,
- responsible parties,
- precedence relations,
- detected inconsistencies.

A predicted and reference plan could then be compared on these consequences.

That would make the SQL analogy persuasive rather than metaphorical.

---

## 8. Several Table 5 metrics need formal refinement

Table 5 is useful but not yet “fully specified” enough for independent implementation. 

### 8.1 Alignment is underspecified

The text says optimal bipartite matching “maximizes agreement on action and target,” with span overlap as a tiebreak.

This needs an explicit cost function and an unmatched threshold. Otherwise different implementations can produce different matchings, particularly when several repeated actions share targets.

The action-detection score is also partly coupled to the alignment criterion because action agreement is used to generate the matching on which action accuracy is then calculated.

### 8.2 Dependency recovery reports recall but not precision

“Constraint and dependency recovery” uses recall only.

A system could recover every true dependency while inventing numerous false ones and still obtain perfect recall. Given the paper's emphasis on unsupported actions, unsupported constraints should be at least as important.

Use precision/recall/F1 or separately report an unsupported-relation rate.

### 8.3 Schedule agreement needs branch-aware semantics

For conditional workflows, a single global pairwise order is insufficient. The metric should specify whether ordering is measured:

- per condition branch,
- over transitive closure,
- only for explicitly constrained pairs,
- with ties/concurrency,
- with unresolved anchors.

### 8.4 “Unsupported attribute” conflicts with permitted inference

The text says:

> “an attribute the source does not state, populated anyway, is an unsupported-attribute error”

while Definition 1 explicitly allows attributes to be “explicitly inferred.” 

Those two rules conflict.

The criterion should instead be something like:

> unsupported = neither directly grounded nor licensed by an explicitly specified inference rule/context source.

Otherwise the paper's own inference of PCP responsibility from addressee information becomes an error.

---

## 9. “Operationally unsafe” conflicts with the readiness ladder

Section 5.1 distinguishes actionable from executable:

- actionable may contain sufficient timing or gating information,
- executable additionally resolves owner and due date. 

Section 7 then says an “actionable record” is operationally unsafe if it has an absent time or wrong actor. 

But by the manuscript's own definition, an actionable ACR may still have unresolved ownership and therefore deliberately not be executable.

### Required fix

Define unsafe emission relative to **what the downstream system is permitted to do**.

For example:

> An ACR is unsafe for autonomous execution if it crosses the execution threshold while a required executable attribute is missing or erroneous.

A deliberately unresolved ACR sent to human review should not be scored as unsafe merely because it abstained.

---

## 10. The companion evidence is useful but currently overinterpreted

The two companion studies strengthen a position paper because they show that some proposed subproblems are empirically tractable. However, neither evaluates the manuscript's most distinctive claim, namely set-level reasoning. The paper explicitly acknowledges this. 

Accordingly, the sentence

> “recognizing an action type from its span is close to solved”

is too strong.

An 85–91% result on gold spans does not constitute “close to solved” for a safety-relevant clinical task, and the very high action F1 in the second study comes from a controlled synthetic corpus.

A better conclusion is:

> “In these studies, action-type recognition is substantially easier than complete executable recovery.”

Likewise,

> “Executable correctness, not type accuracy, is the binding constraint”

should be bounded to the reported experiments rather than asserted generally across clinical intent recovery.

### A concrete citation problem

Reference [69] appears factually incorrect as currently written. The manuscript identifies:

> “Apartsin A, Aperstein Y. Clinical Intent Extraction: A FHIR-Aligned Representation and the CIRCA Benchmark. arXiv:2608.08806.” 

But arXiv:2608.08806 currently resolves to **“Three Generations of Healthcare IT: From the Digital Record to the Computable Care Process”**, by the same two authors, i.e. the precursor/closely related position paper, not the claimed CIRCA benchmark. 

This must be corrected before publication. If the CIRCA benchmark is not yet public, Section 7 should say so explicitly rather than attaching an incorrect identifier.

Reference [70]/arXiv:2605.26560 does appear to correspond to the hybrid follow-up extraction study. 

---

## 11. The conformal-prediction paragraph overstates what is guaranteed

Section 6 says:

> “conformal calibration supplies the abstention threshold, with a distribution-free coverage guarantee”

and then suggests conformal risk control bounds accepted-but-erroneous records and therefore provides selective risk at any chosen coverage. 

This conflates several different concepts:

- probability calibration,
- conformal coverage,
- selective classification,
- conformal risk control.

Standard conformal prediction provides finite-sample marginal coverage under exchangeability assumptions; it does not automatically turn an arbitrary LLM confidence into a calibrated probability, nor does it provide arbitrary conditional safety guarantees. Conformal risk-control results also depend on the specified loss and assumptions.

### Required fix

State precisely what quantity is calibrated or controlled. For example:

> “A held-out calibration set can be used to select an abstention policy with finite-sample guarantees on a pre-specified loss under exchangeability assumptions.”

Avoid implying that “conformal calibration” solves general uncertainty calibration.

---

## 12. Regulatory wording should be updated and softened

The manuscript states:

> “Software a clinician cannot independently review, or that drives time-critical action, falls under device oversight in the United States...”

This is too categorical.

FDA's current Clinical Decision Support Software guidance was issued in **January 2026**, not 2022 as reference [67] states.  FDA does indicate that time-critical decision support generally cannot satisfy the Non-Device CDS criteria, but software classification still depends on intended use and the statutory criteria; FDA's language is more nuanced than “falls under device oversight.” 

### Required fix

Update reference [67] to the 2026 final guidance and use wording such as:

> “may constitute device software and, in particular, time-critical recommendation functions generally do not qualify for the Non-Device CDS exclusion.”

The EU AI Act sentence should likewise specify that high-risk classification under the product-safety route depends on the medical-device/safety-component status **and** the requirement for third-party conformity assessment, rather than implying that every medical-device AI system automatically falls into the same category.

---

## 13. Table 2 is conceptually useful, but “prescribed” is a poor label

The prescribed / observed / intended distinction is one of the clearest conceptual devices in the manuscript. 

However, “prescribed” is potentially misleading in medicine. A prescription is usually patient-specific and therefore itself an instance of intended care, whereas the paper uses “prescribed” to mean:

> “what should generally happen” according to a guideline or protocol.

I suggest **normative**, **protocol-defined**, or **recommended-by-guideline** instead.

The resulting distinction would be much cleaner:

- normative/protocol: what should generally happen;
- intended: what someone means to happen for this patient;
- observed: what actually happened.

---

## 14. Dependencies need a typed target

The second worked example is particularly revealing. It says a CBC becomes dependent on a cardiology visit “that is not itself an ACR in the set.” 

This means `dependency` cannot simply be a relation between two ACRs. It can point to:

- another ACR,
- a clinical event,
- a scheduled encounter,
- a result,
- a patient-observed trigger,
- an unresolved future event.

The ACR definition currently does not specify this.

### Required fix

Define a typed constraint/dependency object, e.g.:

`dependency = <relation, anchor_type, anchor_reference, offset, resolution_state>`

This would also greatly improve the temporal reasoning section.

---

## Strengths

Despite the concerns above, the manuscript has substantial strengths.

**First, the clinical problem is important and well motivated.** The transition from communicated recommendation to tracked responsibility is a genuine failure point in care, and the manuscript wisely avoids claiming that information-system failure is the only cause of missed follow-up. 

**Second, the paper has found a useful level of abstraction.** Treating the ACR as a recovery target rather than proposing another interoperability standard is the right decision. It allows AI/NLP methods to be compared without competing with FHIR.

**Third, provenance and unresolved uncertainty are correctly treated as first-class properties.** The worked discharge example is particularly good because it refuses to invent the owner of the CBC follow-up.  This is a much stronger safety argument than simply demanding better extraction accuracy.

**Fourth, the separation between per-action recovery and set-level reasoning is genuinely useful.** The paper becomes most original when it asks whether several individually plausible outputs form a mutually coherent patient-specific plan.

**Fifth, the executable/operational evaluation perspective is compelling.** The second worked example makes clear why a high-overlap extraction can still be clinically wrong. The emphasis on omission, invention, timing, responsibility, revisions, and contradictions is appropriate for AIIM.

**Sixth, the paper is unusually falsifiable for a position article.** The authors explicitly state conditions under which their proposed framework would be unnecessary. That is commendable.

However, one of those falsifiability statements should be revised. The manuscript says the “layer is redundant” if set-level reasoning does not improve over independent extraction plus mapping.  That does not logically follow: even if set-level reasoning adds no benefit, recovery of patient-specific structured intent could remain a distinct task. The paper should separate at least two hypotheses:

1. richer intent recovery is distinct from conventional item extraction;
2. explicit set-level reasoning improves coherence beyond independent recovery.

Failure of hypothesis 2 does not falsify hypothesis 1.

---

## Tone, readability, and clarity

The manuscript is generally well written and unusually readable for a conceptual health-informatics paper. The two worked examples are effective, and the figures make the architecture easy to understand.

The principal stylistic weakness is **overstatement through categorical contrast**. Phrases such as:

> “clinical language processing, which indexes concepts”

> “Layer 2 recognizes ‘CBC’ and ‘cardiology’ as concepts”

> “Neither ... interoperability standards ... provide this set-level reasoning”

make the argument sound stronger but invite technically justified objections.

The paper would actually become more persuasive by narrowing these claims.

Figure 1 is clear, but it currently visually reinforces an overly clean historical progression. Figure 2 is useful but should be revised when the schema is corrected. Figure 3 is also clear, but it should explicitly show that FHIR/RequestOrchestration and CIG systems can already carry plan-level relations; what the proposed layer contributes is recovery, uncertainty handling, and reconciliation.

Tables 1, 2 and 4 are readable. Table 3 needs substantive correction. Table 5 is promising but needs enough formal detail to be reproducibly implemented.

---

## Fit to *Artificial Intelligence in Medicine* and to the Position Paper article type

The manuscript is a **good substantive fit for AIIM**. It is directly about an AI problem created by the interface between unstructured clinical communication, reasoning, safety, and operational health-information systems. The neuro-symbolic discussion, temporal reasoning, selective prediction, workflow integration, and evaluation issues all sit naturally within the journal's scope.

It also fits the stated **Position Paper** format. The paper gathers and organizes several relevant literatures, identifies a scientific gap, proposes a formal target, articulates challenges, and gives a research agenda. It does not need to perform new experiments to justify publication in this article category.

I therefore would **not require a new set-level experimental benchmark as a condition of revision**. Instead, if no such evidence exists yet, the manuscript should consistently describe set-level reasoning and its metrics as the central proposed research agenda rather than as an empirically validated distinctive capability.

The two companion studies can remain as feasibility evidence for narrower components, provided their citations and claims are corrected.

---

## Essential revisions before acceptance

The following changes would, in my view, move the paper substantially closer to acceptance:

1. Reframe the “third layer” as a proposed computational lens/frontier centered on **communicated-but-unstructured patient-specific intent**, not as if structured intent did not previously exist.
2. Stop defining clinical NLP as concept indexing; distinguish ACR recovery through its **operational target and set-level requirements**.
3. Correct the ACR schema by addressing mandatory **request intent/modality**, patient context, and the distinction between requester, responsible owner, and performer.
4. Separate recovery status from FHIR workflow status.
5. Expand provenance/origin beyond extracted vs inferred to include deterministically computed/derived values.
6. Position set-level novelty against **RequestOrchestration, CarePlan and CIG reasoning**, emphasizing uncertain recovered plans rather than claiming existing systems lack set structure.
7. Formalize the evaluation sufficiently for independent implementation: matching function, unsupported relations, dependency precision, branching schedules, unresolved constraints, and the exact definition of unsafe execution.
8. Either operationalize “executable correctness” with an execution semantics or soften the name/SQL analogy.
9. Moderate the empirical claims from the two companion studies, especially “action type ... close to solved.”
10. Correct reference [69], update the FDA reference and regulatory language, and review the FHIR element mappings carefully.
11. Revise the falsification criterion so that failure of set-level reasoning does not logically imply that the entire intent-recovery layer is redundant.

### Overall judgment

The paper contains a publishable position, but the publishable position is **more precise than the current headline claim**. The strongest formulation is:

**Clinical communication contains patient-specific intended actions that existing workflow standards can represent once structured, but that existing extraction tasks do not generally recover with the provenance, responsibility, temporal/conditional semantics, uncertainty handling, and cross-action reconciliation required for safe operational use. ACR provides a candidate recovery representation, and set-level reasoning plus operationally consequential evaluation define the research frontier.**

Framed this way, the paper is differentiated from both FHIR and conventional clinical NLP without needing to diminish either literature, and the contribution becomes substantially harder to dismiss.
:::