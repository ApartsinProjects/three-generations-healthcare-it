# Revision Plan, Round 2: Scientific restraint, precision, visual discipline

> Reviewer guidance captured (lightly formatted). The core is now sound (defensible
> claim, reusable ACR object, boundaries against prior work, research agenda). This round
> is **not** about adding ideas. It is about **scientific restraint, terminological
> precision, and visual discipline.** Several passages still read like advocacy/manifesto,
> which helps a web essay but weakens a journal position paper.
>
> **Guiding principle: Make the ideas ambitious; make the prose conservative.**

## Highest-priority changes

### 1. Reduce rhetorical certainty in key places
- Keep the memorable "the third makes clinical intent operational by computers" **once**,
  not in heavy emphasis followed by categorical claims. Elsewhere prefer: *"We propose
  that an emerging third layer of healthcare IT makes patient-specific clinical intent
  increasingly computable from communication."*
- Replace "what finally makes ACR recovery tractable" -> *"what may make ACR recovery
  tractable at clinically useful scale."*
- Remove "finally," "at last," and similar; they sound promotional and assert unnecessary
  historical claims.

### 2. Don't present the three generations as historical fact when Gen 3 is a hypothesis
- State explicitly: **"Generations 1 and 2 are retrospective abstractions; Generation 3 is
  a prospective hypothesis."**
- In tables (at least Table 1), use **"Gen 3: Proposed emerging layer"** rather than
  "Gen 3: Care process."

### 3. Reconcile "generation" vs "layer"
- Keep "generation" (it's central) but add: *"We use generation to denote the historical
  emergence of a new computational layer; the resulting layers coexist and accumulate
  rather than replace one another."* Resolves the obvious reviewer objection up front.

### 4. Make the ACR definition visibly formal
- Give it a **numbered/boxed definition**:
  > **Definition 1 — Actionable Clinical Record (ACR).** An ACR is a source-grounded
  > representation of a patient-specific intended clinical action together with the
  > semantic attributes required to interpret, execute, monitor, or audit that action.
- Put the schema immediately below. Makes ACR a scientific construct, not a branded term.

### 5. Make intent / action / process terminology perfectly consistent
The paper alternates among clinical intent, intended action, care process, executable
action, clinical commitment, process step, actionable record. Adopt one hierarchy:

> clinical communication -> clinical intent -> intended action(s) -> ACR(s) -> care process/workflow

Reserve: **intent** = semantic content expressed by a communicator; **action** = atomic
operational unit; **ACR** = computable representation of that action; **process** =
collection/sequence/network of ACRs and other workflow events.

## Tone and language

- "best read not through the technologies that happen to be fashionable" -> *"Healthcare
  information technology can be analyzed more durably through the computational objects it
  supports than through individual technologies, which evolve rapidly."*
- "A generation is not any trend" -> *"We distinguish a generation from an incremental
  technological trend by requiring five structural markers."*
- "a purported generation that fails these markers is a feature, not a generation" ->
  *"A proposed generation that does not satisfy these markers is better interpreted as an
  incremental capability within an existing layer."*
- "reliability stated as a formal system property rather than a slogan" -> *"reliability
  formulated as an explicit system property."*
- Conclusion: "so that others can build on the framework rather than merely agree with it"
  -> *"thereby providing constructs that can be operationalized, evaluated, extended, or
  falsified in subsequent work."*

### Personification (make literal)
- "The residue ... seeds the next generation." -> *"The residual limitation of each layer
  motivates the computational object addressed by the subsequent layer."*
- "The symbolic layer supplies guarantees." -> *"Explicit symbolic components can make
  selected transformations independently verifiable."* ("Guarantee" is risky; most real
  systems won't offer mathematical guarantees.)
- "Guidelines address the first, process mining the second." -> literalize similarly.

## Structure

Sequence is good (thesis -> criteria -> Gen1 -> Gen2 -> gap -> Gen3 -> comparison ->
empirical -> requirements -> agenda -> conclusion); keep it. But **Section 6 is too large
and lopsided.** Restructure:

```
6. Generation Three: Computable Clinical Intent
   6.1 Actionable Clinical Record
   6.2 From communication to workflow
   6.3 Representative use cases
   6.4 Boundaries with related paradigms
7. Reliability and System Architecture
   7.1 Why generation alone is insufficient
   7.2 Neural-symbolic decomposition
   7.3 Provenance, calibration, and oversight
```
Put convergent industry evidence at the end of Section 6 or in a short dedicated section.
Rename the blog-style FAQ heading "Will end-to-end LLMs make the symbolic layer obsolete?"
-> **"Architectural implications of increasingly capable foundation models"** (or "Role of
explicit reasoning in future model architectures").

## Abstract

Intellectually better but **too dense** (occupies a very large block, heavy bolding, long
parenthetical lists, introduces nearly every contribution). Reduce to five moves:
**problem -> proposed model -> precise novelty -> empirical grounding -> implications.**
Target ~200-250 words unless the journal allows more. Move the FHIR resource list out:
instead of "FHIR CarePlan, ServiceRequest, Task, and PlanDefinition..." say *"Existing
workflow standards and guideline representations can encode care processes once they have
been explicitly structured."*

## Introduction

The prescribed/observed/intended distinction is one of the strongest contributions; give
it **greater prominence** via a small table, rather than burying it in the "What the claim
is, and is not" paragraph:

| Process type | Meaning | Typical source | Existing paradigm |
|---|---|---|---|
| Prescribed | What should generally happen | guideline/protocol | CIG/CDS |
| Observed | What actually happened | event log/EHR | process mining |
| Intended | What is supposed to happen for this patient | communication | proposed Gen 3 |

Remove the heading "What the claim is, and is not" (sounds defensive) -> **"Scope and
relation to existing process representations."**

## Tables

Rendering needs attention (cramped, bad hyphenation: "computabil-ity", "reimburse-ment",
"responsi-bility", "temporal con-straint"). Tables are among the most-reproduced elements.
- Use **full-width single-column** tables rather than squeezing into the two-column grid.
- Fewer words per cell; **prevent hyphenation inside tables**.
- **Left-align text-heavy cells**; center only short category labels.
- Lighter rules/background; fewer horizontal lines.
- Table 1 "driving force" row is heterogeneous (Gen1/2 = regulatory/economic; Gen3 =
  tech + safety). Split into **External driver** and **Enabling technical capability**.

## Figures

- Figure 1 is attractive but looks like an executive-deck graphic (large rounded cards,
  blue gradient, timeline dots). Make more restrained: reduce rounded-card styling; one
  neutral hierarchy (not progressively stronger blue); larger box text; arrows if
  progression intended. **A stacked (cumulative) representation may be conceptually
  superior** (Process/intent on top of Facts/state on top of Records/documents), since the
  paper says each layer subsumes the previous; the timeline can imply replacement.
- Caption: "The bottom row is the paper's shorthand..." -> *"The bottom row summarizes the
  canonical question addressed by each computational layer."*

## Typography and PDF layout

Page 1 is visually overloaded. Make more journal-like:
- Affiliations in **regular roman, not decorative italics; remove blue**.
- Remove "Position paper . draft" from the visual center; if kept, "Position paper" beneath
  the title in regular black.
- **Substantially reduce bolding in the abstract.**
- Avoid italic + bold + blue as simultaneous semantic channels.
- More whitespace between abstract, keywords, body.
- Blue headings are OK for a preprint; black headings look more journal-neutral.

### Bold and italic (the most obvious stylistic issue)
Too much bold inside prose. Rule:
- **Bold only:** headings; defined terms at first introduction; perhaps one central
  sentence/construct per major section. **Do not bold complete argumentative clauses.**
- **Italics only:** symbols/variables; defined distinctions on first introduction; journal
  names in references.

## Section headings (make less conversational)
- "What the third generation is not" -> **"Relationship to existing clinical informatics paradigms"**
- "Will end-to-end LLMs make the symbolic layer obsolete?" -> **"Architectural implications of end-to-end foundation models"**
- "Why fluent generation is not enough" -> **"Reliability requirements beyond semantic interpretation"**
- "The Gap: The Care Process Lives in Communication" -> **"The unresolved computational gap: patient-specific intent in clinical communication"**

## Generation 2 wording
- "it is a mistake to reduce it to one technique" -> *"Its enabling stack was broad and
  cannot be reduced to a single technique."*
- Ensure **all summary tables agree**: never "Gen 2 = Clinical NLP"; use *"structured
  clinical data + terminologies + interoperability + clinical NLP."*

## Generation 1 nuance
- "The first generation replaced the paper chart with an electronic one" is historically
  compressed; "clinical document" as the unit sits awkwardly with CPOE/pharmacy/lab/
  transactional data already structured. Define Gen 1 as **"digitization of the clinical
  record and its transactions"** rather than purely the document; then Gen 2 = making
  clinical meaning/state semantically computable across systems.

## Empirical section

The 0.997 / 0.986 / 0.00 / ~0.53 cards make it look like selling a model result. Convert
to a small conventional table:

| Evaluation condition | Hybrid pipeline | Generative baseline |
|---|---|---|
| Seen action types, Pair F1 | 0.997 | ~0.53 |
| Unseen action types, Pair F1 | 0.986 | ... |
| Temporal error | 0 days | ... |

Add explicitly: *"These results are not evidence for the three-generation model itself;
they establish only the technical feasibility of one minimal ACR extraction task."*

## Research agenda

Organize into **four research domains** so others can cite "the four-part Computable Care
Process agenda":
1. **Representation.** ACR ontology, temporal/conditional semantics, provenance, revisions/cancellation.
2. **Inference and reliability.** extraction, relation construction, temporal reasoning, uncertainty, abstention, contradiction handling.
3. **Evaluation.** authentic-data benchmarks, executable correctness, cross-institution/language generalization, clinical utility.
4. **Integration and impact.** FHIR mapping, workflow integration, human factors, regulatory classification, loop-closure and patient outcomes.

## References
- Two weak-looking entries: the ACR follow-up collaborative ([4]) and the Duke/CMS
  referral-loop entry ([5]). Key motivating statistics should rest on peer-reviewed primary
  sources or systematic reviews. Prefer those.
- As a forward-looking paper, add 2024-2026 references around: ambient AI; autonomous/
  agentic workflow; FHIR workflow operationalization; closed-loop referrals/results; LLM
  clinical information extraction; temporal reasoning with LLMs; human-in-the-loop clinical
  AI. Purpose: show the claimed convergence is visible across independent lines of work
  (not length for its own sake).

## Specific sentence-level edits (apply directly)
- "Technologies turn over quickly; the computational object persists." -> *"Individual
  technologies evolve rapidly, whereas the computational objects they enable are more
  persistent."*
- "The residue left by the first two generations is the same one clinicians experience
  daily." -> *"A persistent limitation of the first two layers is visible in routine
  clinical communication."*
- "These are not competitors to the third generation but its downstream infrastructure."
  -> *"These paradigms are complementary to the proposed third layer and, in many cases,
  provide the downstream infrastructure required to operationalize its outputs."*
- "LLM-era semantics are what finally make it tractable at scale." -> *"Recent advances in
  language models substantially improve the feasibility of recovering these relations from
  heterogeneous clinical language at scale."*
- "The symbolic layer supplies guarantees, not missing knowledge." -> *"Explicit symbolic
  components can provide deterministic or independently verifiable transformations where
  the relevant semantics are formally specified."*
- "Reliability, not scale, is the binding constraint." -> **keep**, but use once (end of
  the architectural section), not repeated variants throughout.

## What NOT to change (keep)
- The title.
- "Actionable Clinical Record" (reusable atomic construct).
- The prescribed / observed / intended distinction.
- Communication -> ACR -> workflow as the central architecture.
- "What was documented? -> What is true? -> What should happen?" shorthand, but present it
  **once**, in a figure/table, not repeatedly in bold prose.
- The prospective predictions (falsifiability is a scientific strength).

## Overall
Close to submission-quality for a position/perspective venue. Remaining work is chiefly
making the presentation quieter and more rigorous. Define claims precisely, support each
once, and let the ACR formalization, comparisons, architecture, feasibility result, and
testable predictions carry the argument.
