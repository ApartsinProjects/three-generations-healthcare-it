# Peer Review: “Three Generations of Healthcare IT: From the Digital Record to the Computable Care Process”

## 1. Summary of the contribution

This Perspective proposes a conceptual reorganization of healthcare information technology around the *computational object* made available to machines rather than around successive technologies. It distinguishes three cumulative layers: (1) the clinical record, which becomes digitally available; (2) clinical state or facts, which become semantically interpretable and computable; and (3) a proposed layer of patient-specific clinical intent, in which intended actions expressed in ordinary clinical communication become operationally computable. The manuscript's main original construct is the **Actionable Clinical Record (ACR)**, defined in Section 5.1 as a source-grounded tuple containing an action and potentially its target, actor, temporal constraint, condition, dependency, status, provenance, and confidence. Sections 4–5 further distinguish prescribed, observed, and intended process and position the ACR as a bridge between narrative communication and existing workflow infrastructure such as FHIR Task, ServiceRequest, CarePlan, scheduling, referral, and results-management systems. Sections 6–8 add reliability principles, an “executable correctness” evaluation framework, and a research agenda, while Section 7 explicitly acknowledges that the article itself presents no new empirical validation and relies on a companion feasibility study for one follow-up extraction task. :contentReference[oaicite:0]{index=0}

## 2. Significance and novelty for health informatics

The manuscript addresses an important and recognizable informatics problem: clinically consequential intentions often remain embedded in narrative communication even when the underlying EHR can represent the eventual order, task, referral, or care plan. The move from extracting isolated concepts to recovering *action + arguments + temporal/conditional relations + provenance* is meaningful, particularly because reliable execution requires substantially more than recognizing that a test, drug, or referral was mentioned. The prescribed/observed/intended distinction in Section 4 is probably the manuscript's strongest conceptual simplification and could become useful vocabulary for separating guideline-based decision support, retrospective process reconstruction, and patient-specific commitments communicated during care.

However, the novelty claim currently operates at two different levels, and they should be separated. The narrow claim—**there is an underdeveloped informatics problem in recovering patient-specific intended actions from natural clinical communication and converting them into auditable workflow objects**—is persuasive and potentially important. The much larger claim—that this constitutes a **third generation of healthcare IT** following the digital record and computable clinical state—is not yet established. Healthcare systems have represented patient-specific intent for decades through orders, reminders, care plans, tasks, medication instructions, order sets, workflow engines, and decision-support artifacts. What is comparatively distinctive here is therefore not making clinical intent computable *per se*, but recovering incompletely structured intent from communication and binding it reliably to executable workflow.

The ACR itself could be reusable, but Section 5.1 needs to demonstrate more clearly why it is a new abstraction rather than a convenient intermediate schema for producing existing workflow resources. Its strongest differentiators appear to be source provenance, explicit uncertainty, communication grounding, and unresolved semantic constraints. Those properties deserve greater emphasis than the generic action fields, several of which already have obvious counterparts in established workflow representations.

## 3. Major strengths

First, the manuscript has a clear conceptual center. Sections 4 and 5 move beyond the vague assertion that “important information is hidden in notes” and identify a specific object that is lost: a patient-specific intended action together with the relations required to operationalize it. The examples involving “repeat complete blood count in two weeks,” conditional escalation, medication transitions, handoff commitments, and pending-result responsibility effectively demonstrate why conventional entity extraction is insufficient.

Second, the manuscript generally avoids presenting the proposed layer as a replacement for existing informatics infrastructure. Section 5.2 and Figure 3 appropriately position ACR recovery as a bridge from communication into FHIR resources, schedulers, referral systems, results managers, and work queues. This substantially strengthens the proposal because it makes the architecture potentially implementable rather than requiring creation of a parallel clinical information ecosystem.

Third, Sections 6 and 7 recognize that the scientifically relevant problem is not merely language-model accuracy. The emphasis on provenance, deterministic temporal normalization, abstention, calibration, unsupported-action rates, omissions, whole-record correctness, and loop closure is appropriate for clinically consequential automation. The phrase “executable correctness” is particularly useful because standard NLP component metrics can look strong while the resulting task remains unsafe to execute.

Fourth, the authors are appropriately explicit in Sections 2 and 7 about epistemic status. The first two layers are described as retrospective abstractions, whereas the third is called a prospective hypothesis, and the companion extraction study is presented as evidence of feasibility for one task rather than validation of the overall conceptual framework. That restraint is important for a Perspective.

## 4. Major weaknesses and concerns

### 4.1 The “three generations” thesis is substantially stronger than the evidence supporting it

Section 2 proposes five markers for a computational layer—unit, external driver, enabling technology, class of computation, and residual limitation—but these criteria are asserted rather than derived or validated against competing periodizations of health informatics. Sections 2–3 then compress a heterogeneous history into “record” followed by “clinical state.” In practice, these capabilities developed concurrently and recursively: computerized orders already encoded intended actions; structured clinical facts existed before modern EHR adoption; messaging, CDS, terminologies, workflow systems, and interoperability did not arise as cleanly successive generations. Thus Table 1 is a useful heuristic but is not yet convincing as a historical or theoretical taxonomy.

The paper would be stronger if it explicitly downgraded “three generations” from a historical claim to an **analytical model of three computational layers**. The authors already state that layers accumulate rather than replace one another; following that logic consistently would avoid inviting easily avoidable historical objections.

### 4.2 “Clinical intent is not computable” is too broad; “intent recovery from communication” is the defensible claim

Section 4 correctly acknowledges that FHIR can represent patient-specific intent through CarePlan, ServiceRequest, and related resources. That acknowledgment creates tension with the broader formulation that the first two layers do not make intended actions computable. An entered laboratory order is already a computable patient-specific intention. A Task can be assigned and monitored. A medication order may contain timing and conditions. A care plan may specify goals and actions.

The true gap appears to be that **clinical intent originating in unstructured communication is not reliably transformed into these representations**. This narrower formulation is both more defensible and more interesting. I recommend revising the title-level claim, Table 1, Sections 1, 4, 5, and 9 so that the third layer is consistently defined as *communication-grounded recovery and operationalization of clinical intent*, not simply “computable clinical intent.”

### 4.3 The ACR schema is promising but not yet conceptually rigorous enough

Definition 1 in Section 5.1 is central to the manuscript, but several schema decisions require clarification. Most importantly, `status` is said to correspond to the maturity ladder “mentioned → interpreted → actionable → executable → monitored → closed.” This mixes at least two fundamentally different dimensions. “Mentioned,” “interpreted,” “actionable,” and “executable” describe representational completeness or system capability; “monitored” and “closed” describe the lifecycle state of an instantiated workflow action. An executable referral can subsequently be pending, scheduled, completed, cancelled, superseded, or overdue; those are not later stages of representational maturity.

The model should therefore separate, for example, **representation maturity/completeness** from **workflow lifecycle state**. Similarly, the tuple presents a single `confidence`, whereas Section 6 calls for confidence at the attribute level; provenance may also need attribute-level granularity because the action, time, condition, and actor can originate from different clauses or messages. The manuscript should additionally define how negation, cancellation, revision, conflicting instructions, multiple actors, alternative actions, recurring schedules, and cross-message dependencies are represented. These are not peripheral extensions: they determine whether ACR can actually serve as a reusable informatics object.

### 4.4 The framework's evidence base is too thin for some of its claims

Section 7 appropriately states that the companion study demonstrates feasibility only for follow-up-instruction extraction. Nevertheless, portions of Sections 5–6 generalize to handovers, medication transitions, portal messages, telephone calls, referrals, self-management, multimodal communications, and cross-message workflows without direct evidence that the same representation or technical architecture generalizes across these domains. Citation [24] alone cannot carry the broad claim in Section 5.2 that these communication channels “routinely carry” a common class of actionable process objects.

For a Perspective, new experiments are not mandatory, but a conceptual framework this broad needs stronger synthesis of prior work. The manuscript should show, preferably through a compact mapping, several distinct communication-derived task classes and demonstrate that the proposed ACR attributes actually cover them. Otherwise the ACR risks being generalized from the authors' follow-up use case rather than independently motivated.

### 4.5 Engagement with adjacent informatics work is incomplete

Section 5.3 mainly contrasts the proposal with traditional clinical NLP and computer-interpretable guidelines. That is too narrow for the novelty claim. The manuscript needs deeper engagement with work on clinical task extraction, order and recommendation extraction, care coordination, workflow management, referral closure, results-management systems, temporal information extraction, clinical plans and goals, patient instructions, conversational/ambient documentation, and representations of intent within interoperability standards.

The key scholarly question is not whether MedLEE or cTAKES extracted facts rather than ACRs. It is whether prior systems have already modeled combinations of action, actor, timing, conditions, status, provenance, and workflow execution, and exactly what ACR adds. Section 5.3 should become a much more rigorous “boundary of the contribution” section.

### 4.6 The evaluation framework is sensible but currently a metric inventory rather than a framework

Section 7 lists useful measures, but important evaluation semantics remain unspecified. For example, what constitutes whole-record exact match when several semantically equivalent temporal representations exist? How are omitted actions distinguished from intentionally abstained actions? How should false positive actions be weighted relative to incorrect arguments? How is temporal-normalization error measured for intervals, recurrence, conditional times, or event-relative expressions? What is the unit for calibration when confidence is attribute-specific?

A more mature framework would organize evaluation hierarchically: **detection → semantic reconstruction → executable resolution → safety/reliability → workflow outcome**, and define which failures prevent advancement to the next level. That would materially strengthen the manuscript's claim that “executable correctness” is a reusable contribution.

### 4.7 Clinical validity and human factors are underdeveloped

The manuscript primarily treats the problem as one of faithful extraction of clinician intent, but communicated intent is not necessarily correct, current, authorized, or appropriate to execute. Communications may contain tentative plans, alternatives, teaching statements, patient preferences, copied text, hypothetical recommendations, or instructions subsequently superseded elsewhere. Extracting a statement correctly does not establish that the system should operationalize it.

Section 6 should therefore distinguish at least three concepts: **semantic fidelity to the communication, authority/current validity of the instruction, and safety of execution**. This distinction is necessary if the manuscript is to move from information extraction to “schedule, coordinate, monitor, close,” as claimed in Table 1.

## 5. Minor issues

The prose is generally clear, but the terminology alternates among “clinical fact,” “clinical state,” “clinical intent,” “intended process,” “intended action,” “workflow,” and “care process.” Section 5 provides definitions, but earlier sections should adhere more strictly to them. In particular, “clinical state/fact” in Figure 1 suggests equivalence between a discrete fact and the broader latent state of a patient, which is conceptually questionable.

Figure 1 is visually clear but presents the proposed taxonomy more definitively than the evidence warrants; labeling it explicitly as a conceptual model would help. Figure 2 adds little beyond the tuple in Definition 1 unless the schema is expanded to show cardinalities or relationships. Figure 3 is the most informative figure because it clarifies the integration proposition.

Table 2 is useful but somewhat categorical. Patient-specific prescribed care can exist in structured systems, and observed information can also originate in communication. The table should distinguish *semantics* from *typical source* more carefully rather than implying a one-to-one correspondence.

Some statements in Sections 5.3 and 6 overgeneralize clinical NLP as producing concepts or facts. Relation extraction, temporal relation extraction, assertion modeling, event extraction, and clinical information extraction have long addressed richer structures, including several components that the ACR requires. The contrast should therefore be “component semantic extraction versus an operational workflow contract,” not “NLP produces facts whereas the third layer produces actions.”

The abstract is well aligned with the body and is approximately 147 words, but the sentence asserting that existing standards “do not provide” recovery of intended process should be narrowed in the same way as the corresponding argument in Section 4.

Finally, the manuscript is already very compact. Any additional prior-work positioning should largely replace broad historical exposition rather than simply expand the text.

## 6. Concrete, actionable suggestions for improvement

1. **Reframe the central claim.** Change the strongest formulation from “the third generation makes clinical intent computable” to something closer to “a proposed computational layer recovers patient-specific clinical intent from communication and operationalizes it within existing workflow infrastructure.” This preserves the genuinely novel proposition while avoiding conflict with decades of computable orders, tasks, and care plans.

2. **Treat the three generations primarily as computational layers rather than a literal historical sequence.** In Sections 1–3, explicitly state that the model is a functional abstraction and that capabilities overlap historically. Consider retaining “generations” as an interpretive metaphor rather than a strong historiographic assertion.

3. **Strengthen Section 5.3 substantially.** Add a compact comparison of ACR with FHIR Task/ServiceRequest/CarePlan, guideline representations, conventional clinical NLP/event extraction, temporal extraction, and process mining. For each, identify what is represented, where the representation originates, whether provenance to communication is retained, and whether unresolved uncertainty can be carried forward.

4. **Repair the ACR ontology.** Separate representation maturity from workflow lifecycle status; make confidence explicitly attribute-level; specify provenance granularity; define cardinalities; and describe cancellation, revision, competing instructions, conditional alternatives, recurring actions, cross-message dependencies, and actor ambiguity. A small formal example containing two related ACRs would be more valuable than Figure 2 in its current form.

5. **Demonstrate domain coverage conceptually.** Take 4–6 heterogeneous examples—for example follow-up testing, referral, medication taper, conditional emergency escalation, pending-result ownership, and patient self-management—and instantiate the complete ACR representation for each. This would provide much stronger support that the proposed schema generalizes beyond the companion follow-up study.

6. **Reorganize Section 7 into an evaluation hierarchy.** Separate semantic correctness, executability, reliability/safety, and clinical/workflow outcome. Define at least conceptually how whole-record correctness, temporal correctness, abstention, unsupported actions, omissions, provenance, and calibration interact.

7. **Add a clinical-validity layer to Section 6.** Explicitly distinguish “the system correctly recovered what was communicated” from “the communicated instruction remains authoritative and safe to execute.” Revision, contradiction, authorship/authority, and reconciliation with existing structured orders should be first-class reliability concerns.

8. **Moderate claims about language models and hybrid architecture.** The neural-symbolic architecture is a plausible design pattern supported by the companion study, but it should be framed as one candidate implementation of the computational layer rather than an architectural consequence of the framework itself. A future system could satisfy the ACR contract using other technical approaches.

9. **Sharpen falsifiability.** The proposed trends in Section 8—such as increasing machine-actionable FHIR usage or ambient systems generating tasks—would not necessarily validate this particular three-layer theory. More direct tests would ask whether the ACR representation transfers across clinical task classes, improves interoperability between communication understanding and workflow systems, and enables safer/more complete loop closure than task-specific representations.

10. **Use the title carefully.** If the broad framing is retained, “Three Computational Layers of Healthcare IT: From the Digital Record to Computable Care Intent” would more accurately reflect what the paper actually establishes. The current “Three Generations” formulation raises a historical burden of proof that the manuscript does not presently meet.

## 7. Recommendation: Major revision

**Recommendation: Major revision.**

The manuscript contains the basis of a potentially useful JAMIA Perspective. In particular, the distinction between prescribed, observed, and intended process; the focus on communication-derived patient-specific action; the ACR's provenance-oriented representation; and the shift from NLP accuracy toward executable correctness are worthwhile contributions. I can see the ACR becoming a reusable construct if its semantics are clarified and its relationship to established workflow representations is made explicit.

However, the current manuscript overstates its highest-level theoretical claim. Patient-specific clinical intent is already computable in many forms; what remains incompletely solved is its reliable *recovery from ordinary communication and transformation into operational workflow*. In addition, the ACR currently conflates representation maturity with workflow state, its generality is supported primarily by examples rather than a broader evidence synthesis, and the prior-work comparison does not yet establish the boundary between the proposed construct and existing clinical workflow, task, plan, and information-extraction representations.

These are substantial but addressable problems. I would not recommend rejection because the core problem and proposed abstraction are relevant to JAMIA and the paper is unusually clear about being a prospective conceptual framework rather than an empirical validation study. A major revision that narrows the generation-level claim, formalizes the ACR more rigorously, strengthens engagement with adjacent informatics work, and differentiates semantic recovery from authoritative/safe execution could produce a strong and genuinely reusable Perspective.