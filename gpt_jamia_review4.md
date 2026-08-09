# ChatGPT (GPT-5, High effort) JAMIA review — cycle 4 (2026-08-09)

Consulted via GPTConsult on the current `index.html` manuscript (main text ~1970
words, 48 refs). File was uploaded and read by the model (grounded review; it
cross-checked HL7 FHIR R5, ACL Anthology, and PMC sources). Recommendation:
**Minor revision.**

---

## 1. Overall recommendation — Minor revision

The manuscript is close to publishable as a JAMIA Perspective. The major
conceptual boundary problem is largely resolved: the paper no longer claims FHIR
or workflow systems cannot represent clinical intent, but localizes the third-layer
capability to recovering patient-specific actionable intent from communication and
converting it into an operational representation.

Two issues must be fixed before acceptance, plus several citation corrections and a
sharper operational falsifier:
1. The manuscript still occasionally slips from the defensible claim
   ("communication-derived intent remains non-computable until recovered") to the
   broader claim that intended actions themselves were not computable under the
   first two layers, despite acknowledging CPOE, orders, scheduling, and FHIR.
2. The ACR `status` field is semantically underspecified and internally
   inconsistent with being mandatory.

## 2. Conceptual contribution

- Framework is useful; keep presenting it as an analytic decomposition, not a
  historical discovery (already done: Layers 1-2 retrospective, Layer 3 prospective).
- Strongest contribution is NOT that "intent" is a computable object (orders,
  requests, care plans, tasks already embody intent) but the **combination**:
  communication-derived recovery + source grounding + temporal/actor/dependency
  semantics + operational reliability requirements.
- **Principal remaining inconsistency = scope of "intent."** Section 3 says Layer 1
  included "order entry and results routing," yet Section 4 opens saying the first
  two layers made state computable "but not the intended actions that constitute
  care." Both cannot be literally true. Narrow the gap consistently in Table 1,
  Section 4, the ACR definition, and the conclusion: it is *patient-specific
  intended actions that remain embedded in natural communication*, not intent per se.
- **FHIR technical error:** Section 4 lists PlanDefinition among resources
  representing "patient-specific intent." In FHIR R5, PlanDefinition is a
  definition of actions independent of a specific patient. Replace with Task, or
  distinguish definitional PlanDefinition from instantiated patient-specific
  request resources.
- Section 5.2 mapping is too one-to-one. Task already spans intent/event and tracks
  ownership, requested performer, requested timing, basedOn, partOf, and
  provenance-linked history; ServiceRequest provides occurrence timing and requested
  performer. Frame "actor -> owner," "condition -> trigger," "dependency ->
  basedOn/partOf" as *illustrative mappings dependent on target resource*, not
  universal correspondences.
- Readiness-vs-lifecycle distinction is conceptually clear but implementation is
  incomplete: status is mandatory yet its only defined values are effectively
  "monitored, then closed." What is the status of a newly recovered, unconfirmed
  ACR? Define a small lifecycle (recovered/confirmed/active/completed/cancelled) or
  make lifecycle status optional until operationalization.
- prescribed/observed/intended: Table 2 still risks reading as three mutually
  exclusive source categories. State explicitly the taxonomy characterizes *what a
  process statement means*, not an exclusive source, storage format, or system class.

## 3. Scientific rigor and claims

- "nearly all of the intended action stays in narrative" (Sec 3) is not established
  by Rosenbloom et al. [21]. Replace "nearly all" with "a substantial portion" /
  "many intended actions."
- "the first two layers made clinical state computable but not the intended actions
  that constitute care" — most consequential residual overclaim; conflicts with the
  paper's own acknowledgement of CPOE and FHIR workflow objects.
- Detailed FHIR mapping relies on ref [16], a 2013 general FHIR paper — inadequate
  for current resource-level assertions (Task, ServiceRequest, PlanDefinition,
  basedOn, partOf, ownership, status, provenance). Cite the current HL7 FHIR spec
  directly. Note FHIR already has a dedicated **Provenance** resource and describes
  its use for middleware that extracts/transforms information into FHIR resources;
  so the "provenance is a property of recovery rather than a native field" sentence
  is defensible only if followed by "and can be represented through FHIR Provenance
  or an appropriate profile/extension."
- Section 6 citation-fit problems:
  - [43] automation-bias systematic review supports caution/oversight/reliance, NOT
    calibrated selective prediction or abstention as technical methods — cite
    selective-classification/calibration literature for those; keep Goddard for
    human factors.
  - [44] is speaker-role identification: supports the speaker component only, not
    the whole "source span, speaker, and encounter" invariant.
  - [45] is an indirect anchor for an "immutable trace" requirement — justify or
    replace with provenance/audit literature.
  - [35] Nori et al. primarily evaluates GPT-4 medical performance/calibration
    (reports strong capability); weak fit for "can produce unreliable or unsupported
    outputs." [34] supports the generic hallucination point; add a clinical
    factuality/safety reference for the medical application.
- Falsifier improved but not operational: "fails if standard representations and
  metrics suffice" makes "suffice" an unmeasured escape hatch. Strengthen to a
  testable disconfirmation (see Section 6 edit below).

## 4. Literature positioning (three additions strengthen the novelty boundary)

- **CLIP: A Dataset for Extracting Action Items for Physicians from Clinical Notes
  (Mullenbach et al., ACL 2021)** — most conspicuous omission; directly studies
  action-item extraction from clinical text, extremely close to the ACR object. Add
  to Section 5.3 and explicitly distinguish ACR recovery from prior action-item
  extraction.
- **THYME / Clinical TempEval lineage** — more directly establishes mature work on
  clinical events, times, and temporal relations than the 2012 i2b2 challenge alone;
  central to the action-time binding argument.
- **MedDec** (medical-decision extraction from discharge summaries) — narrows what
  is genuinely new: decision/action span extraction remains an *extraction* task,
  whereas ACR requires linked operational semantics + execution-oriented evaluation.
- **Actor/responsibility is the least mature basis.** Speaker identity != execution
  responsibility ("Dr Smith said the CBC should be repeated" does not imply Dr Smith
  owns the follow-up). Make this distinction explicit; the unresolved ownership
  problem is itself a useful research gap supporting the ACR agenda.
- MEDIQA-OE is already appropriate for communication-to-workflow. One sentence
  acknowledging CLIP, MedDec, and the extraction-vs-execution distinction suffices
  within the word limit.

## 5. Presentation

- Abstract is appropriately restrained ("illustrates tractability for one narrow
  subproblem") — keep.
- Figure 1: change arrow label "each layer subsumes the one below" ->
  "each layer builds on the one below" ("subsumes" overclaims containment).
- Figure 2: exposes the status problem (status marked required while lifecycle
  status is only defined for an operationalized action). Fixing status semantics
  fixes the figure.
- Figure 3 (most important figure): keep, but frame "maps to existing
  infrastructure" as an adapter/profile-dependent translation, not a deterministic
  field mapping.
- Table 2: add a few words (not a column): rows are "semantic categories; sources
  are illustrative, not exclusive."
- **Concrete cross-reference error:** Data Availability says the
  "executable-correctness evaluation framework" is in Section 8; it is introduced in
  Section 7. Fix.

## 6. Specific section-level edits (quote -> replacement)

- **Sec 3:** "while much of the reasoning, and nearly all of the intended action,
  stays in narrative." -> "while much clinical reasoning and many intended actions
  remain expressed only in narrative."
- **Sec 4 opening:** "The first two layers made clinical state computable but not
  the intended actions that constitute care." -> "The first two layers made clinical
  state computable, but many patient-specific intended actions remain non-computable
  when they are expressed only in unstructured communication."
- **Sec 4 FHIR sentence:** "FHIR represents patient-specific intent through
  CarePlan, ServiceRequest, and PlanDefinition" -> "FHIR can represent
  patient-specific intent through resources such as CarePlan, ServiceRequest, and
  Task, while PlanDefinition represents reusable plan or protocol definitions that
  can be instantiated for a patient."
- **Sec 4 taxonomy sentence:** "intended ... expressed primarily in communication."
  -> "intended ... patient-specific actions that may be structured directly or
  expressed in communication; the proposed layer targets the latter when they have
  not already been operationalized."
- **Table 2 caption:** -> "The categories describe the semantic status of process
  information rather than exclusive source types. The proposed third layer targets
  recovery of patient-specific intended process that remains expressed in natural
  communication."
- **Sec 5 opening:** "clinical communication expresses intent" -> "clinical
  communication may express patient-specific intent."
- **Sec 5.1 status paragraph:** "the ACR's status attribute tracks the workflow
  lifecycle (monitored, then closed)" -> "Separately, the ACR's lifecycle status
  records the operational state of the recovered action - for example recovered,
  confirmed, active, completed, cancelled, or escalated - without changing its
  representational readiness."
- **Sec 5.2 FHIR mapping:** "action and target populate a Task or ServiceRequest ...
  actor the owner, dependency the basedOn/partOf links..." -> "ACR attributes can be
  translated into appropriate FHIR workflow elements according to the target
  resource and implementation profile - for example, timing into
  ServiceRequest.occurrence[x] or Task.requestedPeriod, responsible parties into
  performer/owner semantics, and workflow relationships into available request or
  task links."
- **Sec 5.2 after provenance sentence, add:** "Recovery provenance may itself be
  represented using FHIR Provenance or implementation-specific profiling, while
  model confidence generally remains metadata of the recovery system."
- **Sec 5.3, add after clinical-NLP sentence:** "Prior work has also directly
  extracted clinical recommendations, physician action items, medical decisions, and
  structured orders; the proposed distinction is therefore not action detection
  itself, but recovery of the linked semantics and reliability required for workflow
  execution." Cite CLIP, MedDec, the existing recommendation paper, and MEDIQA-OE.
- **Sec 8 falsifier:** "the proposal fails if standard representations and metrics
  suffice..." -> "The ACR is redundant if, across communication-derived task
  classes, direct mapping into existing workflow standards represents the required
  action, actor, temporal, conditional, dependency, provenance, and uncertainty
  semantics without ACR-specific distinctions, and existing extraction metrics
  discriminate operationally unsafe outputs as well as the proposed
  executable-correctness measures."
- **Figure 1:** "each layer subsumes the one below" -> "each layer builds on the one
  below."
- **Data Availability:** "the executable-correctness evaluation framework
  (Section 8)" -> "... (Section 7)."

## 7. Single most important change before acceptance

Make the manuscript completely consistent that the proposed third layer is about
**recovering intended actions that remain embedded in communication - not about
making clinical intent computable for the first time.** Residual sentences in
Section 3, the opening of Section 4, Table 1, and the third-layer unit definition
still permit the stronger interpretation. Adding a sentence like "structured orders
already make some intent computable; our proposed layer concerns the systematic
recovery of otherwise unstructured, communication-derived intent into
source-grounded executable objects" largely dissolves the FHIR objection and sharpens
the ACR's genuine contribution.
