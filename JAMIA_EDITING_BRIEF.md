# Editing Brief — JAMIA Submission

> Editing brief for the final revision on the `jamia` branch. Transform the current
> manuscript into a publication-ready JAMIA article that introduces a durable
> conceptual framework for biomedical informatics. The paper should be remembered not for
> a particular AI method, but for defining a **new computational layer of healthcare IT**
> and a **reusable scientific vocabulary.** It should read as a mature scientific
> perspective written for researchers, informaticians, standards experts, and healthcare
> IT architects.

## Target article type: Research and Applications (decided 2026-08-08)

Although the original brief said "Perspective," we target JAMIA **Research and
Applications**, because its definition explicitly covers "the formulation… of a new model"
(an exact fit for the generational framework + ACR construct), whereas *Perspectives* is
defined narrowly as "views of an organization or opinion leaders" (borderline type-fit) and
caps at 2000 words. Hard constraints from the official OUP JAMIA General Instructions
(https://academic.oup.com/jamia/pages/General_Instructions):

- **Main text ≤ 4000 words** (excludes abstract, acknowledgments, references, supplements).
- **Structured abstract ≤ 250 words** (JAMIA requires *structured*, not the ~200–250 word
  unstructured abstract in the section below — follow the structured format).
- **≤ 4 tables, ≤ 6 figures**; alt text required for every figure.
- **References: unlimited, Vancouver numbered** (superscript, in order of appearance).
- **Double-spaced Word document**; mandatory **Data Availability Statement**; **CRediT**
  author-contribution taxonomy. ORCID likely required at submission (verify in the portal).
- Reviewers expect evaluation substance: frame the follow-up-extraction study as a
  **formative feasibility** demonstration and elevate the **proposed evaluation framework**
  to a first-class contribution; do not oversell the numbers.

(The 200–250 word / abstract-structure guidance below is superseded by the structured
≤250-word requirement above; all other brief guidance still applies.)

## Overall positioning

The paper is **not**:
- a paper about LLMs,
- a paper about NLP,
- a paper about follow-up extraction,
- a product proposal.

It is a paper **proposing a new conceptual framework for healthcare informatics.**
Everything else serves as supporting evidence.

Central thesis (keep): healthcare IT has evolved by making progressively richer
computational objects available to software:
- **Generation 1:** clinical records
- **Generation 2:** computable clinical state
- **Generation 3:** computable clinical intent and care process

## Scientific tone

Rewrite to sound like a high-impact Perspective rather than a manifesto:
- reduce promotional language;
- replace certainty with precise scientific language;
- avoid rhetorical questions;
- avoid dramatic expressions ("finally", "revolution", "game changing", "fashionable", "obviously", etc.);
- avoid absolute statements unless demonstrably true;
- use cautious wording: *we propose, we argue, we hypothesize, suggests, may enable, provides a useful abstraction.*

**The ideas should be ambitious. The language should be conservative.**

## Position the contribution correctly

Do **not** claim previous healthcare IT could not represent workflows. State clearly:
healthcare already possesses mature representations for structured workflows (FHIR,
CarePlan, Task, ServiceRequest, PlanDefinition, computer-interpretable guidelines, process
mining). The **missing capability** is recovering patient-specific clinical intent directly
from ordinary clinical communication and converting it into computable actionable records.
This distinction must remain explicit throughout.

## Strengthen the ACR

Present the **Actionable Clinical Record (ACR)** as a formal scientific construct with a
**numbered definition.** Clearly distinguish: communication / intent / action / Actionable
Clinical Record / workflow / care process. Present ACR as the **atomic computational object
of Generation 3**, not merely an example.

## Clarify terminology (use consistently, never interchangeably)

```
Clinical communication
  ↓
Clinical intent
  ↓
Intended clinical actions
  ↓
Actionable Clinical Records
  ↓
Clinical workflow
  ↓
Care process
```

## Strengthen scientific precision

- Generation 1 and Generation 2 are **retrospective abstractions.**
- Generation 3 is a **proposed emerging computational layer.**
- Explicitly state that generations **accumulate rather than replace** previous capabilities.

## Improve historical framing

Generation 2 should never be described simply as "the NLP generation." Describe it
consistently as **structured clinical information**, enabled by: structured data,
terminologies, interoperability, clinical NLP, semantic computing. NLP is **one** enabling
technology, not the defining characteristic.

## Strengthen the research framework

Provide reusable concepts future papers can cite, as **formal constructs** (not narrative
ideas): Actionable Clinical Record; intended process; computable care process; Generation
3; maturity ladder; evaluation framework.

## Figures

Revise to resemble **journal figures**, not presentation slides: reduce decorative styling;
neutral colors; reduce gradients; increase readability. Illustrate **cumulative
computational layers** rather than a historical timeline where possible.

## Tables

Improve all tables: avoid dense text; avoid hyphenated words; increase whitespace. Split
**"Driving force"** into **External driver** and **Enabling technology.** Tables should
communicate concepts quickly.

## Abstract

Rewrite to ~**200–250 words**, structured: Problem → Framework → Novel contribution →
Supporting evidence → Implications. Avoid long enumerations; do not overload with
implementation details.

## Section organization (one clear purpose per section)

1. Introduction
2. Generational Framework
3. Generation 1
4. Generation 2
5. The Remaining Computational Gap
6. Generation 3
   - Actionable Clinical Record
   - Communication to Workflow
   - Representative Use Cases
   - Relation to Existing Paradigms
7. Reliability and Architecture
   - Hybrid AI
   - Provenance
   - Calibration
   - Human oversight
8. Evaluation Framework
9. Research Agenda
10. Conclusions

## Evidence

Use follow-up extraction **solely as a feasibility demonstration**, not proof of the
theory. Explicitly state that the experiment validates **one minimal Generation-3 task**
rather than the conceptual framework itself.

## References

Strengthen references supporting: ambient clinical AI; healthcare workflows; clinical
communication; temporal reasoning; FHIR workflow; clinical AI reliability; human-AI
collaboration. Prefer **systematic reviews, major informatics papers, and standards
documentation** over white papers.

## Typography and formatting

Reduce bold substantially: bold only for section headings and the first definition of
important terms. Minimize italics. Increase whitespace. Ensure tables and figures fit
comfortably within journal columns. The paper should visually resemble a **JAMIA
Perspective**, not a polished website.

## Final quality criterion

A reader should finish believing that:
- the three-generation framework is a useful abstraction;
- the Actionable Clinical Record is a reusable scientific construct;
- "computable clinical intent" is a meaningful new research area;
- future work can extend, evaluate, or falsify the framework.

The paper should **establish terminology that future biomedical informatics papers
naturally adopt**, rather than simply presenting a successful AI application.
