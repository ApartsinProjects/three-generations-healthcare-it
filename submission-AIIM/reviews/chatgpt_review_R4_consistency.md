# AIIM Position Paper Review

## Verdict

**MINOR REVISION:** the core position is coherent and potentially acceptable, but the manuscript is not yet ready for Accept because several residual wording inconsistencies misstate the ACR, the contribution of this position paper, and the contrast with clinical NLP and existing workflow formalisms.

## Consistency findings

### 1. “Narrative Communication” in the title versus “clinical communication” throughout the body

**Quotes**

Title: “Computable Clinical Intent: Recovering Executable Care Actions from Narrative Communication.”

Abstract: “recovering patient-specific intended actions from unstructured clinical communication.”

Section 4, Table 2: “Typical source: clinical communication.”

Section 5.2: “Its inputs are the range of clinical communication.”

Figure 3: “Clinical communication” and “ACRs as the bridge between clinical communication and existing workflow infrastructure.”

Table 2 caption also uses “natural communication.”

**Assessment**

This is not a substantive scientific contradiction, but it is a visible terminology and scope mismatch. “Clinical communication” is the actual umbrella concept used by the paper. It covers discharge instructions, referral correspondence, portal messages, telephone calls, handoffs, and ambient transcripts. “Narrative communication” is narrower and less standard, and some listed inputs are communicative but not naturally described as narrative.

**Fix**

The cleanest fix is to use the same umbrella term in the title and abstract:

> **Computable Clinical Intent: Recovering Executable Care Actions from Unstructured Clinical Communication**

If the current title must be retained, define the relationship at first use:

> “We use narrative clinical communication to denote unstructured clinical communication in notes, messages, handoffs, conversations, and transcripts; below, clinical communication is used as shorthand.”

Then replace “natural communication” in the Table 2 caption with the chosen term.

### 2. The opening CBC example attributes semantics to the text that the worked example later says are absent

**Quotes**

Abstract: “When a clinician writes ‘repeat the complete blood count in two weeks,’ its action, timing, condition, and owner stay in narrative text, never computable.”

Introduction: “its action, timing, gating condition, and responsible owner exist only as narrative.”

Worked example: “condition: none” and “owner unresolved (candidate PCP).”

Later: “The discharge summary does not say who orders the repeat CBC, so its accountable owner is left unresolved.”

**Assessment**

The abstract and Introduction say the condition and owner are present in narrative text, but the worked example explicitly says there is no condition and that the owner is not stated. This is a direct internal inconsistency.

**Fix**

Replace the abstract sentence with a shorter statement such as:

> “When a clinician writes ‘repeat the complete blood count in two weeks,’ the intended action and timing remain embedded in narrative text, while execution-critical semantics such as accountable ownership may be unstated or implicit.”

Apply the same logic to the Introduction. This also saves words in an abstract that is already approximately 247 words.

### 3. The abstract defines every ACR as temporally normalized and executable, while the body explicitly permits non-executable ACRs

**Quotes**

Abstract: “We define the Actionable Clinical Record (ACR): one intended action, grounded in its source text, temporally normalized, and executable.”

Section 5 opening: “recovering it from communication as a structured, executable representation.”

Definition 1: “target, actor, temporal constraint, condition, and dependency are populated when communicated or inferred.”

Readiness ladder: “A partially populated ACR sits below the executable rung until its owner and timing are resolved.”

Worked example: ACR 1 has “owner unresolved” and “readiness: actionable,” followed by “the record stays at the actionable rung, not executable.”

Table 4: ACR output unit is “executable action.”

Section 5.3: “Recovering an executable ACR poses two families of open problems.”

**Assessment**

This is the most important title, abstract, and body mismatch. The body treats the ACR as a schema that can represent an action before it reaches executable readiness. The abstract, Section 5 opening, and Table 4 treat executability as an inherent property of every ACR instance.

There is also a naming tension: an “Actionable Clinical Record” can apparently exist below the actionable or executable threshold unless candidate states are distinguished explicitly.

**Fix**

State the distinction once and propagate it consistently:

> “The ACR is a source-grounded recovery representation for one intended action. Its target state is executable readiness, reached when the execution-critical attributes required for that action are resolved.”

Then make the local changes:

* Abstract: replace “temporally normalized, and executable” with “designed to carry normalized timing and the semantics required for executable use.”
* Section 5 opening: replace “a structured, executable representation” with “a structured representation intended for executable use.”
* Table 4 output unit: replace “executable action” with “intended action with executable semantics.”
* Section 5.3: replace “Recovering an executable ACR” with “Recovering an ACR to executable readiness.”
* Consider calling below-threshold objects “ACR candidates” if the authors want “Actionable Clinical Record” to denote only actionable or executable instances.

The title can still say “Recovering Executable Care Actions” if executability is explicitly defined as the target state rather than a guaranteed property of every recovered record.

### 4. Provenance is required by the architecture, but its schema-level meaning is less specific than the later invariant

**Quotes**

Definition 1: “action, request-intent, status, and provenance are required.”

Table 3: provenance maps to the “Provenance resource,” with “span needs extension.”

Section 6 invariant: “every acted-upon record traces to a source span, speaker, and encounter.”

Worked example provenance: “span ‘Repeat CBC in two weeks,’ discharge summary.”

**Assessment**

The later reliability contract requires span, speaker, and encounter traceability, but Definition 1 does not explicitly define those as components of provenance. The worked ACR also does not encode all three explicitly.

**Fix**

Define provenance structurally in Section 5.1, for example:

> “provenance identifies the source document or communication, encounter, source span, and speaker or author when available.”

If all three are mandatory only for records that may cross the execution threshold, say so explicitly. The invariant then becomes a readiness or execution requirement rather than an unstated schema requirement.

### 5. “Clinical fact” in the abstract and “clinical state” in the body need one explicit naming rule

**Quotes**

Abstract: “the record, the clinical fact, and the intended action.”

Figure 1: “Layer 2 · clinical state (fact).”

Table 1: “Layer 2: Clinical state,” with unit “Discrete clinical fact.”

Section 3: “The second layer turned the record into computable clinical state.”

Conclusion: “Health IT has made the record and then the clinical fact computable.”

**Assessment**

This is mostly reconcilable because the abstract says it is naming the unit made computable, while the body often names the layer. However, the paper alternates between the two without stating that distinction explicitly.

**Fix**

Add one sentence in Section 2:

> “We call the second layer clinical state; its atomic unit of computability is the discrete clinical fact.”

Alternatively, rename Layer 2 “Clinical fact” everywhere. The first option preserves the present conceptual vocabulary while making it fully consistent with the abstract.

### 6. Computerized order entry occupies three different conceptual positions in the layer model

**Quotes**

Section 2: “order entry and care plans already make selected patient-specific intent computable.”

Section 3, Layer 1: “operations such as order entry and results routing.”

Section 3, Layer 2 enabling stack: “structured data entry, controlled terminologies, computerized order entry, data warehouses, and interoperability standards.”

Section 4: “Computerized order entry already makes computable the intent a clinician structures at entry.”

**Assessment**

CPOE appears as a Layer 1 operation, a Layer 2 enabling technology, and an existing mechanism that already computes selected Layer 3 intent. That makes the three-layer boundary look unstable unless CPOE is explicitly described as cross-layer infrastructure.

**Fix**

Use one qualification such as:

> “CPOE is cross-layer infrastructure: its transactional storage belongs to the record layer, while the structured request it captures already makes selected patient-specific intent computable. The proposed third layer addresses intent that never enters CPOE or another structured workflow resource.”

Then remove CPOE from whichever Layer 1 or Layer 2 list is not needed.

### 7. The abstract and Introduction overstate the contrast with clinical NLP, while Section 5.3 is appropriately nuanced

**Quotes**

Abstract: “It differs from clinical language processing, which scores fields one at a time.”

Introduction: “separate both from the clinical natural language processing that scores extraction targets independently.”

Section 5.3: “Clinical NLP extracts concepts, events, and temporality … and, closest to this layer, physician action items and medical decisions from notes.”

Worked example: “Layer 2 recognizes ‘CBC’ and ‘cardiology’ as concepts; it does not bind them to repeat, to a discharge-anchored due window, to a responsible owner, or to the condition that gates the referral.”

Table 4 caption already gives the correct qualification: “A ‘no’ marks a field not required by that task or schema, not one the paradigm cannot represent.”

**Assessment**

The Section 5.3 wording is defensible. The abstract and Introduction generalize a property of selected extraction task formulations to “clinical language processing” as a field. The worked example is more problematic because it reduces Layer 2 to concept indexing, directly contradicting Section 5.3’s acknowledgment of event, temporal, action-item, and decision extraction.

This is likely to draw reviewer resistance because the novelty claim does not require a strawman version of clinical NLP.

**Fix**

Abstract:

> “It extends common clinical NLP extraction formulations that evaluate items or fields independently, and complements interoperability standards that represent intent once structured.”

Introduction:

> “distinct from common per-item clinical NLP extraction formulations and complementary to interoperability standards that represent structured intent.”

Worked example:

> “Layer 2 methods can identify the concepts, events, temporal expressions, and some relations in this instruction. The proposed intent layer additionally requires them to be assembled into one source-grounded operational action with normalized timing, accountable responsibility, conditional and dependency semantics, and set-level coherence.”

Also revise Section 5.3’s “Neither the extraction literature” to “The compared extraction tasks” or “Common extraction task formulations.”

### 8. The interoperability and guideline contrast is inconsistent about whether existing formalisms reason over constraints

**Quotes**

Section 5.2: “the decision-support layers that could check such properties act on structured, already-consistent inputs.”

Section 5.3: “This is the reasoning that clinical guideline and care-plan formalisms already perform over curated inputs.”

**Assessment**

These sentences conflict. If guideline and care-plan formalisms already perform temporal and constraint reasoning, their inputs cannot simply be characterized as “already-consistent.” The defensible novelty is recovery and reasoning over uncertain, partially unresolved structures, not the existence of temporal or consistency reasoning itself.

**Fix**

Replace “structured, already-consistent inputs” with:

> “structured, authored or curated inputs whose workflow semantics have already been made explicit.”

Then retain the later statement that the proposed challenge is applying related reasoning to recovered, uncertain, and partially unresolved intent.

### 9. “Temporal semantics and traceability must be computed, not generated” conflates two different requirements

**Quotes**

Abstract: “Because temporal semantics and traceability must be computed, not generated, we argue for a hybrid neuro-symbolic architecture.”

Section 6: “the deterministic component computes the due date.”

Section 6 invariant: “deterministic semantics are computed, not generated,” while separately “every acted-upon record traces to a source span, speaker, and encounter” and “an immutable trace links communication to action.”

**Assessment**

The body supports “computed, not generated” for deterministic temporal or constraint semantics. It supports source grounding and preservation for traceability. Traceability is not naturally described as something that is “computed.”

**Fix**

Abstract:

> “Because temporal semantics must be computed and traceability must remain source-grounded rather than generated, we argue for a hybrid neuro-symbolic architecture with output invariants.”

Section 6 can be sharpened to:

> “deterministic temporal and constraint semantics are computed, not generated; traceability remains linked to source evidence.”

### 10. One sentence incorrectly says this position paper contributes a parser

**Quote**

Section 5.1: “The contribution is the parser and the metric, not the target language.”

**Assessment**

This directly conflicts with the abstract, the position-paper framing, and the Data Availability statement. The manuscript introduces no parser and no new model. It explicitly presents the ACR and evaluation framework as the contribution.

**Fix**

Replace with:

> “The contribution here is the recovery target and executable-correctness evaluation framework, not a new interchange format or a new parser.”

This correction is required before acceptance.

### 11. The paper alternates between “evaluation framework” and a “shared benchmark,” and overstates how fully operationalized the framework is

**Quotes**

Abstract: “The ACR and its evaluation framework are offered for the community to build on, evaluate, or refute.”

Section 8: “computable clinical intent supplies a well-posed target and a shared, executable-correctness benchmark.”

Conclusion: “the ACR and its evaluation framework, specified fully enough to implement, test, extend, or refute.”

Data Availability: “The ACR schema … and the evaluation framework … are fully specified in the text.”

Section 7: “An output is operationally unsafe when a record crosses the autonomous-execution threshold…”

The same paragraph says consequence class is “assigned from the action type by a stated safety taxonomy,” but the manuscript does not actually state that taxonomy or its weights.

Section 5.3 also defines contradiction relative to “a stated exclusion relation on action types,” but no complete exclusion relation is supplied.

**Assessment**

The abstract is accurate: this paper specifies an evaluation framework. It does not introduce a new benchmark dataset. The CIRCA benchmark is a separate companion work.

The framework is detailed, especially its matching rule and set-level measures, but “fully specified” is too strong while the autonomous-execution threshold, consequence taxonomy, weighting scheme, action exclusion relation, and some benchmark-specific thresholds remain task-defined.

**Fix**

Replace “shared, executable-correctness benchmark” with “shared executable-correctness evaluation framework.”

Replace “fully specified” and “specified fully enough to implement” with:

> “specified as an implementable evaluation framework, with deployment-specific parameters such as execution thresholds, safety taxonomy, exclusion relations, and benchmark thresholds to be prespecified for each task.”

Alternatively, add those missing specifications to the paper.

### 12. The companion studies need more explicit separation from the present article

**Quotes**

Introduction: “an executable-correctness evaluation framework with two companion studies.”

Abstract: “A worked example and two separately reported companion studies show tractability.”

Section 7: “Two companion studies give the framework empirical grounding.”

The Section 7 paragraph then reports detailed numerical results without naming CIRCA or MedFollow and says: “separating learned interpretation from computed structure closes the date-computation gap once the anchor is fixed.”

Data Availability later clarifies: “No new data were generated for this article. The feasibility results in Section 7 come from two companion studies [69,70].”

**Assessment**

The abstract and Data Availability correctly say the studies are separate. The Introduction’s “with two companion studies” can be read as if Section 7 contains studies performed in this paper, and the dense results paragraph reads like a Results section unless the external attribution is made explicit at the start.

The “closes the date-computation gap” sentence is also stronger than the evidence described in the manuscript because the second companion study uses a controlled synthetic corpus and fixed anchors.

**Fix**

Introduction:

> “an executable-correctness evaluation framework, with feasibility evidence drawn from two separately reported companion studies.”

Section 7:

> “Two separately reported companion studies provide record-level feasibility evidence. The CIRCA benchmark study [69] reports … The MedFollow hybrid follow-up study [70] reports … These are external companion results, not empirical results of this position paper.”

Replace:

> “closes the date-computation gap once the anchor is fixed”

with:

> “eliminated date error in that controlled setting once the temporal anchor was fixed.”

Also replace “show tractability” in the abstract with “support record-level tractability” if maximum precision is desired, because neither companion study evaluates the proposed set-level reasoning.

### 13. The FHIR positioning drifts from “upstream recovery target” toward “candidate FHIR extension”

**Quotes**

Abstract: “a recovery target upstream of FHIR workflow resources, not a new interchange format.”

Definition 1: “The ACR is not a new interchange format but a projection of FHIR workflow resources onto what must be recovered.”

Section 8: “For standards, the ACR gives a concrete object to profile: a candidate FHIR extension or implementation-guide direction for representing recovered, source-linked intent upstream of workflow resources.”

**Assessment**

An implementation guide around existing FHIR workflow resources is compatible with the paper’s position. Calling the ACR itself a “candidate FHIR extension” risks implying that it is a new FHIR data object, which the abstract and Definition 1 explicitly deny.

**Fix**

Use:

> “For standards, the ACR identifies recovery metadata and workflow semantics that could inform implementation guidance or extensions around existing FHIR workflow resources, without introducing a competing interchange format.”

### 14. The concluding claim of full implementation readiness is stronger than the paper’s stated prospective status

**Quotes**

Section 2: “the third is a prospective hypothesis.”

Conclusion: “We offer the ACR and its evaluation framework, specified fully enough to implement, test, extend, or refute.”

Section 8 acknowledges that “the set-level measures remain to be instantiated on recovered plans” and that moving to real-world notes is “the central empirical risk.”

**Assessment**

“Implement” is plausible for the core schema and basic metrics, but the wording can be read as claiming that the entire third-layer system and safety evaluation are operationally specified. That is stronger than the paper’s own prospective framing and its acknowledgment that the set-level benchmark is future work.

**Fix**

Use:

> “We offer the ACR and an executable-correctness evaluation framework specified sufficiently to instantiate, test, extend, and refute, while leaving task-specific safety thresholds and set-level benchmark construction to future work.”

## Acceptance findings

### 1. Correct the paper’s contribution identity before acceptance

The sentence “The contribution is the parser and the metric” is incompatible with a position paper that contains no new parser, and “shared … benchmark” incorrectly absorbs the separate CIRCA benchmark into this article. These are not stylistic details. They affect what the paper claims as its contribution. Both should be corrected.

### 2. Reconcile ACR schema membership with executable readiness

The paper currently uses “ACR” both for partially resolved recovery objects and for “executable actions.” The readiness ladder is a useful solution, but the definition must make clear whether below-threshold objects are ACRs, ACR candidates, or simply incomplete ACR instances. This matters for annotation, scoring, safety thresholds, and the title’s promise of “Executable Care Actions.”

### 3. Narrow the clinical NLP contrast

The manuscript has enough novelty without claiming that clinical language processing as a field “scores fields one at a time” or that Layer 2 merely recognizes concepts. Section 5.3 already contains the more defensible positioning: prior work can extract concepts, events, temporality, action items, decisions, and orders, while this proposal requires a source-grounded operational record plus set-level coherence and execution-oriented evaluation. That should be the framing everywhere.

### 4. Do not claim the evaluation framework is fully specified unless the remaining parameters are supplied

The matching rule is now unusually concrete and is a strength. However, the autonomous-execution threshold, consequence taxonomy and weights, action exclusion relation, and some benchmark thresholds are not specified. Either provide them or explicitly classify them as task-specific parameters that must be prespecified. The current “fully specified” wording is too strong.

### 5. Attribute and scope the companion evidence more carefully

Section 7 should visibly separate “results reported in [69] and [70]” from the contributions of the present paper. CIRCA uses harmonized corpora and MedFollow uses a controlled synthetic corpus. Neither tests the proposed set-level reasoning. Therefore the strongest defensible conclusion is that they support record-level feasibility and the learned-versus-computed design principle in a controlled temporal setting. They do not yet validate the complete third-layer architecture.

### 6. Clarify the historical layer model as an authorial synthesis and explain cross-layer technologies

“In the field’s documented history … that unit has been the record and then the clinical fact” reads as if the three-stage abstraction were itself established historical consensus. It is better written as the authors’ synthesis of the cited history.

Suggested wording:

> “We synthesize the documented history [8,9] as a progression in the dominant unit made computable, from the record to the clinical fact, and propose patient-specific intended action as the next target.”

The CPOE issue should be resolved at the same time by explicitly calling it cross-layer infrastructure.

### 7. Several interoperability claims need either tighter wording or more direct grounding

Three claims are broader than the citations, as presented in this manuscript, obviously establish:

* “patient- and population-level FHIR query is broadly available.”
* “unstructured communication … remains the dominant carrier of what a clinician means to happen next [22].”
* an unresolved timing constraint is something “a concrete FHIR timing cannot express.”

The first is a current deployment claim, the second is a dominance claim about clinical intent, and the third is a categorical representational claim. The cited material may support parts of these assertions, but the wording should be narrowed unless a direct source is added.

Examples:

> “FHIR-based query capabilities are increasingly deployed…”

> “unstructured communication remains an important carrier of intended next actions…”

> “an unresolved constraint does not map cleanly to a resolved FHIR occurrence time without additional representation or profile-specific handling.”

### 8. The “executable semantic parsing” analogy needs a citation if retained

Section 5.1 says: “The parallel is executable semantic parsing, where a fixed target makes recovery measurable by what the structure implies when run rather than by surface overlap.”

That is a useful positioning analogy, but it introduces a distinct research literature without a citation. Add one or more canonical executable semantic parsing references, or remove the literature-level analogy and state it as a conceptual comparison.

### 9. Soften the regulatory sentence that equates architectural invariants with legal obligations

Section 6 says: “The invariants above … are the technical form of those obligations.”

That is stronger than needed. Traceability, abstention, human review, and logging can be presented as technical design responses aligned with regulatory obligations, not as an exhaustive technical instantiation of the law.

Suggested wording:

> “These invariants provide technical design mechanisms aligned with requirements for traceability, logging, human oversight, and transparency.”

### 10. The present abstract is already at the word limit margin

The abstract is approximately 247 words. Any consistency corrections must be net-neutral or shorter. The fixes proposed above can reduce rather than increase length, especially by replacing the CBC sentence and narrowing the NLP contrast.

## Any title recommendation

**Preferred title:**

> **Computable Clinical Intent: Recovering Executable Care Actions from Unstructured Clinical Communication**

This is the cleanest title because it matches the abstract’s own terminology and the full range of sources shown in Figure 3, including prose, messages, handoffs, conversations, calls, and transcripts.

If “Narrative Communication” is retained for stylistic reasons, it is acceptable, but the manuscript should define it once as the umbrella term and then use one consistent shorthand. The current combination of “Narrative Communication,” “unstructured clinical communication,” “clinical communication,” “natural communication,” and “ordinary communication” is unnecessary terminology drift.