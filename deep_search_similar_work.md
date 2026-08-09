# Deep literature search — similar papers & novelty check (2026-08-09)

Broad web search around the paper's thesis (computable clinical intent, the ACR,
communication-to-workflow recovery, generational/unit-of-computability framing).
Verdict: **the ACR 9-tuple and the three-layer / "unit of computability" framing are
defensibly novel.** Exact-phrase searches for "Actionable Clinical Record,"
"computable clinical intent," "computable care process," and "three generations of
healthcare IT" / "unit of computability" returned nothing. The problem space is
occupied, but every precedent is either flat order/action extraction or
population-level computable guidelines; none unifies patient-specific intent into an
owned, scheduled, conditional, dependency-linked, executable record evaluated for
executable correctness.

## Closest precedents / novelty threats (most threatening first)

1. **MEDIQA-OE 2025 — Medical Order Extraction from Doctor-Patient Consultations**
   (Ben Abacha et al.; Clinical NLP @ ACL 2025; arXiv:2510.26974). **Sharpest
   threat** — it does "recover intended orders from conversation into a structured
   schema with provenance." But the schema is a flat 4-tuple
   `(order_type, description, reason, provenance)` scored by ROUGE/text overlap: no
   actor, dependency, conditional logic, status, or executable representation. It
   stops exactly where the ACR begins. **Already cited** in the manuscript ([27]).
2. **CLIP** (Mullenbach et al., ACL 2021) — "actionable follow-up items," 7 action
   types over MIMIC-III, but sentence-level span classification, not a structured
   executable record. **Already cited** ([50], §5.3).
3. **MedDec** (Elgaar et al., Findings-ACL 2024) — 10 decision types (DICTUM
   taxonomy) from notes; decisions are typed labels, not scheduled/owned actions.
   **Already cited** ([51], §5.3).
4. **MedFollow / companion pipeline** (arXiv:2605.26560) — the authors' own companion
   method; not a threat. **Already cited** ([49] companion study).

## Positioning citations we could add (optional)

- **HIS taxonomy**: "A Taxonomy for Health Information Systems," JMIR 2024;26:e47682
  — closest existing HIS taxonomy to anchor "unit of computability" against.
- **Responsibility / loop-closure (justifies the ACR `actor` field)**: "Assigning
  responsibility to close the loop on radiology test results," Diagnosis 2017;
  doi:10.1515/dx-2017-0019. (Wright 2020 loop-closure already cited [7].)
- **Neuro-symbolic + beyond-overlap evaluation**: "Neuro-symbolic AI for auditable
  cognitive information extraction from medical reports," Commun Med 2025;
  doi:10.1038/s43856-025-01194-x — closest peer-reviewed neuro-symbolic
  clinical-extraction precedent for the hybrid pipeline + executable-correctness
  argument. (Currently the paper cites Garcez & Lamb [40] for neuro-symbolic AI
  generally.)

## Recommended inoculating sentence (defends novelty vs the #1 threat)

Add to §5.3, distinguishing the ACR from flat order-extraction:
> "Unlike order-extraction schemas such as MEDIQA-OE's flat
> `(type, description, reason, provenance)` tuple or CLIP's action-item spans, the
> ACR encodes the actor, temporal constraint, condition, and dependency structure
> required to execute an intention, and is evaluated for executable correctness
> rather than lexical overlap."

(The paper already draws this distinction in general terms; naming MEDIQA-OE/CLIP's
schema explicitly is the strongest single hardening against a "this already exists"
reviewer. Trade-off: the manuscript is locked at exactly 2000 words, so adding it
requires a compensating trim.)

## Could not verify
- Full author lists for MEDIQA-OE overview and a couple of NLP items were from
  snippets; the three added refs (CLIP, Clinical TempEval, MedDec) were separately
  verified against ACL Anthology in the prior citation-check pass.
