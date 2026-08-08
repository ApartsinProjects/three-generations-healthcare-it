# Revision Plan: Three Generations of Healthcare IT

> Reviewer guidance captured verbatim (lightly formatted). Goal: turn a good position
> paper into a **research object + architecture + vocabulary** that future researchers
> cite as "the Generation-3 problem defined by Apartsin and Aperstein" and that vendors
> use as an architecture vocabulary.

## Summary of the core move

The paper already has the nucleus of a potentially influential framework:
**document → fact → process**, organized around the **"unit of computability."** That
is stronger than organizing healthcare IT by fashionable technologies. The main issue is
that the present draft sometimes makes the historical/technological taxonomy more
vulnerable than necessary, while the genuinely novel idea — the transition from
communication to executable patient-specific intent — is not yet formalized strongly
enough.

## The most important conceptual change

Preserve the title:

> Three Generations of Healthcare IT: From the Digital Record to the Computable Care Process

But slightly change what "Generation 3" means.

FHIR already has CarePlan, ServiceRequest, Task, workflow models and PlanDefinition;
computer-interpretable guidelines (CIGs) have represented executable care processes for
decades. FHIR explicitly represents patient-specific intent through CarePlan and service
requests; PlanDefinition represents generic plans that can generate patient-specific
actions. Process-mining researchers have computed patient pathways from event logs for
years.

Therefore the strongest defensible claim is **not**:

> "Healthcare IT could not represent process before LLMs."

It **is**:

> "Healthcare IT could represent process when somebody or some system had already
> structured it. The missing capability was to recover patient-specific clinical intent
> and process commitments directly from ordinary clinical communication."

Conceptual progression becomes:

- **Gen 1** — Computational representation of clinical information artifacts: document → digital record
- **Gen 2** — Computational representation of clinical state: narrative/data → normalized facts
- **Gen 3** — Computational representation of clinical intent and process: communication → executable commitments/actions

This avoids conflict with FHIR, workflow engines, CDS, CIGs and process mining, and
positions all of them as **downstream infrastructure that Generation 3 can finally
populate automatically.** Much stronger industry story.

## Improvement plan

1. **Make "unit of computability" the central intellectual contribution**, not
   databases → NLP → LLMs. Put the principle everywhere: title/abstract, Figure 1,
   definitions, conclusion. Technologies change quickly; computational objects persist.
   Rename Table 2's "Enabling AI technology" to **"Enabling computational stack."**
   Gen 2 should **not** be described as the "NLP-based generation": structured lab
   results, CPOE, ICD coding, terminology systems, templates, interoperability and
   databases were at least as important as NLP. NLP is **one route** by which narrative
   facts entered the semantic layer. Makes the historical argument much harder to attack.

2. **Define a formal artifact researchers can adopt: the Actionable Clinical Record (ACR).**
   Currently the actionable record (Action + Time + Condition + Actor + Context +
   Dependency + Status) appears almost as an example. Promote it into a **formal
   definition**:
   `ACR = <action, target, actor, temporal constraint, condition, dependency, status, provenance, confidence>`.
   Distinguish required from optional fields. Define each field semantically. Define
   **provenance** as source communication + source span + speaker + encounter. Define
   **temporal constraints**, not merely "time" ("after finishing antibiotics," "if pain
   persists," "within six months," "before next visit" cannot all be a date). Once a
   named formal object exists, others can say "We extract ACRs," "We extend the ACR
   schema," "Our benchmark evaluates ACR recovery." This makes the paper citable
   infrastructure, not just an essay.

3. **Introduce the missing transformation explicitly: Communication → ACR → Workflow.**
   Make this the canonical diagram. Inputs: discharge instructions, patient-clinician
   conversation, EMS handover, nurse handoff, referral correspondence, portal messages,
   telephone calls, ambient encounter transcripts. AI converts these into ACRs. The ACR
   layer maps into FHIR Task/ServiceRequest/CarePlan, scheduling, alerts, work queues,
   referral systems, results-management systems. FHIR provides the downstream machinery;
   ServiceRequest models proposals/orders progressing through fulfillment; CDS Hooks
   inserts decision support into workflow. Gen-3 AI is the **semantic-to-operational
   bridge, not a replacement EHR.**

4. **Distinguish three fundamentally different kinds of process information:**
   - **Prescribed process** ("patients with X should undergo Y") — guidelines / CIGs.
   - **Observed process** ("the patient actually underwent A → B → C") — records / process mining.
   - **Intended process** ("for this patient, do X in two weeks, unless Y") — communicated during care.
   Gen 3 primarily captures the **third**. This three-way distinction may become more
   influential than the generational terminology itself; it precisely identifies the
   missing object.

5. **Broaden motivating examples beyond follow-up** while keeping follow-up as the
   empirical proof. One compact table with ~eight communication-derived process objects:
   follow-up ("repeat CBC in two weeks"); conditional escalation ("return immediately if
   fever develops"); medication transition ("reduce dose after seven days"); handoff
   commitment ("cardiology to review echo tomorrow"); referral; pending-result
   responsibility; self-management action; patient-declared intended action ("I will stop
   taking it until I speak with my doctor"). Recent work on patient messages,
   incidental-radiology follow-up and ambient communication shows these channels contain
   clinically consequential actionable information.

6. **Turn "Generation 3" into an explicit capability ladder.** Define levels inside
   Gen 3: extraction → relation construction → executable interpretation → workflow
   integration → closed-loop execution. Recognizing "CBC" is Gen 2. Extracting "repeat
   CBC" is partial Gen 3. Linking test to "two weeks" and responsible party creates an
   ACR. Mapping to a due date and FHIR object makes it executable. Detecting
   completion/escalation closes the loop. A maturity model future systems classify against.

7. **Radically strengthen the evaluation framework.** The 0.997 Pair F1 result is
   impressive but rhetorically dangerous (controlled synthetic 2,000-note benchmark). A
   skeptic can dismiss the framework as built around an artificially easy feasibility
   experiment. Keep the result, but stop making the numerical score carry the Gen-3
   thesis. Define a **general benchmark suite**: action detection; argument extraction;
   action–time/condition/actor linking; temporal normalization error; executable-record
   exact match; unsupported-action rate; omitted-action rate; calibration/selective-risk
   curves; source-provenance accuracy; and eventually loop-closure outcome. P2 already
   points here; turn it into a formal evaluation proposal.

8. **Make reliability a formal system property, not a general safety principle.**
   "Reliability, not fluency, is the binding constraint" is one of the strongest phrases.
   Expand into an architecture principle: no executable item without provenance;
   deterministic computation where deterministic semantics exist; uncertainty attached to
   every inferred field; abstention/selective prediction; human review according to risk;
   immutable trace between communication and action; explicit distinction between
   extracted content and inferred content. This is where the neuro-symbolic argument
   becomes compelling: not that symbolic AI is intrinsically superior, but that certain
   workflow semantics are externally verifiable and therefore should not remain latent
   inside generative inference.

9. **Add an explicit industry architecture and value model.** Diagram:
   Communication sources → multimodal capture/ASR → semantic interpretation → ACR layer →
   validation/reasoning → FHIR/workflow adapters → EHR/scheduler/referral/results systems
   → completion events → loop monitor. Connect value to four outcomes: fewer dropped
   commitments, lower coordination workload, shorter delays, better auditability. Ambient
   AI is already shifting from pure documentation toward workflow integration, supporting
   the convergence argument. Makes the paper relevant to EHR vendors, ambient-scribe
   companies, payer/provider systems and workflow startups, not just NLP researchers.

10. **End with a much larger research program than the present four predictions.** Keep
    the falsifiable predictions, but introduce a named agenda: **The Computable Care
    Process Research Agenda.** Define research questions: the ACR ontology; extraction
    from multilingual/multimodal communication; temporal and causal reasoning;
    cross-message reconciliation; contradictions; patient vs clinician intent;
    changing/revoked plans; provenance; calibrated abstention; integration standards;
    authentic-data benchmarks; human factors; regulatory categorization; and ultimately
    whether automatic loop closure improves clinical outcomes. A menu of publishable
    problems originating from this paper.

## The centerpiece diagram (signature figure)

Turn the existing "one note, three generations" example into the signature figure:

```
Communication
  "Repeat CBC in two weeks; refer to cardiology if chest pain persists."
        ↓
Gen 1 — Record            stored narrative
        ↓
Gen 2 — Clinical state    CBC → LOINC ; chest pain → SNOMED CT
        ↓
Gen 3 — Clinical intent
  ACR1: repeat CBC | due +14d | owner=? | pending | provenance=…
  ACR2: cardiology referral | trigger=persistent chest pain | owner=… | conditional | provenance=…
        ↓
Operationalization
  FHIR ServiceRequest / Task / CarePlan → scheduler → completion monitoring
```

Understandable in ~20 seconds.

## Second figure: "The Missing Middle Between Communication and Workflow"

- **Left:** patient-clinician conversation, discharge communication, handoff, EMS radio,
  portal message, referral, telephone.
- **Right:** existing structured infrastructure — FHIR, Task, CarePlan, ServiceRequest,
  scheduler, CDS, referral system, result manager.
- **Between them:** the **Actionable Clinical Record layer.**

Visual point: healthcare already has infrastructure for executing **known** instructions.
The new opportunity is making instructions **known to the machine** when they originate as
natural communication.

## Revised historical taxonomy (replace databases → NLP → LLM table)

| | Gen 1 | Gen 2 | Gen 3 |
|---|---|---|---|
| **Object** | Record | Clinical state/fact | Clinical intent/process |
| **Question** | What was documented? | What is true about the patient? | What is supposed to happen? |
| **Representation** | Documents/events | Concepts/observations | Actions, constraints, dependencies |
| **Primary computation** | Store/retrieve/exchange | Query/reason/predict | Schedule/coordinate/monitor/close |
| **Enabling stack** | EHR + DB + messaging | Terminologies + structured systems + NLP + interoperability | LLM/ML + relation/temporal reasoning + workflow semantics |
| **Canonical output** | Document | Fact | Actionable Clinical Record |
| **Failure residue** | Meaning trapped in narrative | Intent trapped in communication | Safe reliable execution |

The **Question** row is the shorthand for the whole paper:

> What was documented? → What is true? → What should happen?

## Terminology changes

- Stop calling Gen 2 "the NLP generation." Use **semantic/structured clinical information
  generation** or **computable clinical facts.**
- Be careful with "digitizing the care process" — parts are already digitized. Prefer:
  **"making patient-specific care intent computable from clinical communication."** Retain
  "computable care process" as the broader destination.
- Distinguish **actionable** from **executable**: an extracted instruction can be
  actionable but still lack sufficient information for automatic execution. Natural
  progression / Gen-3 maturity scale:
  **mentioned → interpreted → actionable → executable → monitored → closed.**

## Abstract additions

Protect the novelty claim from prior workflow work:

> Existing healthcare standards and workflow systems can represent orders, tasks, care
> plans, and executable guidelines once these have been explicitly encoded. The
> unresolved gap is upstream: much patient-specific clinical intent is expressed only in
> natural communication and therefore never enters this computable process layer.

Then introduce the ACR:

> We define the Actionable Clinical Record as the atomic object of this layer: a
> source-grounded representation of an intended clinical action together with its
> temporal, conditional, responsibility, dependency, status, and confidence semantics.

## What makes it genuinely influential

Turn the paper from a narrative taxonomy into a **research object + architecture +
vocabulary.** After revisions a researcher should be able to: adopt the ACR schema;
classify their task using the generation/maturity model; evaluate against the proposed
metrics; implement ACR → FHIR mappings; and describe their system as solving one portion
of the Computable Care Process agenda. That is the difference between a position paper
people agree with and a framework that establishes a field.

## Two anchor sentences to build the revision around

> The first generation made clinical information available to computers; the second made
> clinical state interpretable by computers; the third makes clinical intent operational
> by computers.

> The defining problem of the third generation is not generating clinical text, but
> transforming what people communicate about future care into source-grounded,
> verifiable, executable and monitorable clinical commitments.
