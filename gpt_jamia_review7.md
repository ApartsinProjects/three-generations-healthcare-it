# ChatGPT (GPT-5, High effort) JAMIA review — cycle 7 punch list (2026-08-09)

Consulted via GPTConsult on current `index.html` (2000 words, 54 refs; bibtest 54/54).
Grounded review. **Verdict: Accept-after-these-edits** — two small must-fix items
(citation/consistency only), then "Accept, no further required revision."
ChatGPT confirmed no em-dashes in prose and all prior safeguards in place.

## A. MUST-FIX FOR ACCEPT (blockers) — both ~free on word count

1. **§4 final sentence contradicts §5.3.** "…but none recovers it from unstructured
   communication" conflicts with §5.3's acknowledgement of action-item/decision/order
   extraction.
   - Current: "Existing paradigms represent and operationalize intended process once
     it has been structured, but none recovers it from unstructured communication;
     that recovery, and its conversion into executable form, is the subject of the
     third layer."
   - → "Existing workflow paradigms represent and operationalize intended process once
     it has been structured, but they do not themselves specify recovery from
     unstructured communication; the third layer concerns that recovery and its
     conversion into executable form."

2. **Put the normative FHIR citation on the FHIR claims (citation-only).**
   - §4: "…PlanDefinition defines reusable protocols that are instantiated per
     patient;[17]" → change cite to **[28]** (HL7 FHIR R5 Workflow).
   - §8: "ACR-to-FHIR write-back into scheduling, results-management, and referral
     systems,[17,23]" → **[28]** (ref 23 is CIGs, not normative FHIR).

## B. SHOULD-FIX (recommended, word-neutral)

3. **§8 falsifier fairness.** "direct mapping into existing workflow standards
   represents the required action, actor, temporal, conditional, dependency,
   provenance, and uncertainty semantics without ACR-specific distinctions" → add
   "…existing workflow standards, **together with generic recovery metadata,**
   represents…" (confidence is recovery metadata, so the falsifier shouldn't require
   the standard itself to carry uncertainty).

4. **Definition 1 / §6 confidence optionality.**
   - "confidence records recovery-system uncertainty on inferred attributes." →
     "confidence, when inference is used, records calibrated per-attribute
     recovery-system uncertainty."
   - §5.1: "and confidence, a calibrated per-attribute uncertainty, routes uncertain
     records to review." → "and confidence routes uncertain inferred attributes to
     review."

5. **§3 over-strong adoption claim.** "HITECH and Meaningful Use moved adoption to
   near-universal within a decade" → "HITECH and Meaningful Use drove rapid nationwide
   EHR adoption."

6. **§5.2 citation conflation.** "Ambient documentation and recent shared tasks
   extract structured orders directly from clinical conversations,[29,30] showing
   these channels carry actionable content." → "Recent shared tasks extract structured
   orders directly from clinical conversations,[30] while ambient documentation shows
   that these conversations are already captured computationally.[29]"
   Also "Follow-up is the most-documented case" → "Follow-up is a well-documented case."

7. **§7 avoid implying autonomy.** "Because the third layer acts, it should be
   evaluated on executable correctness rather than text overlap." → "Because
   third-layer outputs can drive clinical action, they should be evaluated on
   executable correctness rather than text overlap."

8. **§6 evidence scope.** "General-purpose models interpret clinical language well[39]
   but can produce unreliable or unsupported outputs;[40]" → "Large language models
   show substantial clinical information-extraction and medical-reasoning
   capability[34,39] but can produce unreliable or unsupported outputs;[40]"

## C. OPTIONAL POLISH (take or leave)
- Figure 3: "extraction + symbolic reasoning" → "recovery + structured reasoning"
  (keeps the layer implementation-agnostic).
- §4: "provide the infrastructure to operationalize its outputs" → "provide
  infrastructure to operationalize the proposed layer's outputs" (pronoun clarity).
- Figure 1 "clinical state / fact" → "clinical state (fact)".

Word limit: none of the changes threaten ~2000 words (must-fix are shorter or
citation-only; should-fix are word-neutral). Bottom line: apply the 2 must-fix →
recommend Accept.
