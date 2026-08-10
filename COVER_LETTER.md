Yehudit Aperstein
Intelligent Systems, Afeka Academic College of Engineering
218 Bnei Efraim St., Tel-Aviv 6910717, Israel
apersteiny@afeka.ac.il

9 August 2026

The Editors-in-Chief
*Journal of the American Medical Informatics Association (JAMIA)*

Re: Submission of a Perspective, "Three Generations of Healthcare IT: From the Digital Record to the Computable Care Process"

Dear Editors,

We are pleased to submit the enclosed manuscript for consideration as a **Perspective** in *JAMIA*. The article proposes a framework and a shared vocabulary for a research direction we believe is now emerging in biomedical informatics: making patient-specific clinical **intent** computable directly from ordinary clinical communication.

Our central argument is that healthcare IT is most durably understood not through the technologies it adopts but through the **unit of information it makes computable**. Read this way, the field has progressed from the computable *record* to the computable clinical *fact* (state), and we propose a third computational layer whose object is patient-specific clinical *intent*. We formalize the atomic object of that layer as the **Actionable Clinical Record (ACR)**, a source-grounded representation of an intended clinical action as the tuple ⟨action, target, actor, temporal constraint, condition, dependency, status, provenance, confidence⟩, carrying the semantics needed to interpret, execute, monitor, and audit it.

We think this fits *JAMIA*'s Perspective genre because the contribution is conceptual and forward-looking, a proposed framework, a reusable construct, an evaluation framework, and a set of falsifiable predictions, rather than a completed empirical study. The manuscript is deliberately careful about its boundaries. We do **not** claim that existing standards cannot represent care processes: FHIR workflow resources, computer-interpretable guidelines, and process mining already do so once a process has been structured, and we present them as complementary downstream infrastructure. The capability we localize is upstream and currently unmet: recovering incompletely expressed, patient-specific intent from natural communication and converting it into computable, executable records. We include an explicit ACR-to-FHIR field mapping to show that the ACR sits upstream of those resources rather than competing with them.

We are also careful to distinguish the ACR from adjacent clinical-NLP work. Established action-item, medical-order, and decision-extraction efforts recover useful content from notes and conversation, but typically into flat schemas evaluated by lexical overlap; the ACR instead requires the actor, temporal, conditional, and dependency structure needed to *execute* an intention, and we propose evaluating it for **executable correctness** rather than text overlap. That distinction, not the existence of the individual fields, is the contribution.

We are equally explicit about evidence. The manuscript is a framework and a vocabulary; a companion feasibility study is summarized as a controlled feasibility demonstration for one narrow task (follow-up-instruction extraction), not as validation of the framework itself, and clinical utility and safety are stated as prospective hypotheses with human confirmation as the expected operating mode. <span class="chg">For transparency, that companion study (Laufer M, Aperstein Y, Apartsin A. Reliable Extraction of Clinical Follow-Up Instructions: A Hybrid Neural-Symbolic Pipeline. arXiv:2605.26560), by overlapping authors and cited in the manuscript, is a preprint that is not under consideration for publication elsewhere.</span>

We believe *JAMIA*'s readership of informaticians, standards developers, and health-IT architects is the right audience to adopt, extend, evaluate, or falsify these constructs, and that a shared vocabulary for "computable clinical intent" would be timely as ambient documentation and clinical language models move from producing notes toward producing tasks and orders.

This manuscript is original, has not been published previously, and is not under consideration elsewhere. Both authors have read and approved the submission and agree to its content. The work involved no human-subjects data collected by the authors and no new data were generated for this article. The authors declare no competing interests and no external funding. Correspondence should be addressed to Yehudit Aperstein (apersteiny@afeka.ac.il).

Thank you for considering our submission. We would be glad to respond to any questions.

Sincerely,

Yehudit Aperstein (corresponding author), on behalf of
Alexander Apartsin, Holon Institute of Technology (HIT)
Yehudit Aperstein, Afeka Academic College of Engineering
