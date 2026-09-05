Yehudit Aperstein\
Intelligent Systems, Afeka Academic College of Engineering\
218 Bnei Efraim St., Tel-Aviv 6910717, Israel\
apersteiny@afeka.ac.il

5 September 2026

The Editor-in-Chief\
*Artificial Intelligence in Medicine*

Re: Submission of a Position Paper, "Computable Clinical Intent: Recovering Executable Care Actions from Unstructured Clinical Communication"

Dear Editor,

We are pleased to submit the enclosed manuscript for consideration as a **Position Paper** in *Artificial Intelligence in Medicine*. The article gathers, describes, and analyzes the scientific challenges of a specific problem for medical AI: recovering patient-specific intended actions from unstructured clinical communication, in a form a system can schedule, monitor, and close.

Our central argument is that health information technology is most durably understood not through the technologies it adopts but through the **unit of information it makes computable**. Read this way, the field has progressed from the computable *record* to the computable clinical *fact* (state), and we propose a third computational layer whose object is patient-specific clinical *intent*. We formalize the atomic object of that layer as the **Actionable Clinical Record (ACR)**, a source-grounded representation of one intended clinical action as the tuple (action, target, request-intent, actor, temporal constraint, condition, dependency, status, provenance, confidence), whose target state is executable readiness and which sits upstream of FHIR workflow resources rather than competing with them.

This fits the Position Paper genre because the contribution is conceptual and forward-looking: a layered model of the field, a reusable construct (the ACR), an analysis of the open inference sub-problems, an evaluation framework, and a set of falsifiable predictions, rather than a completed empirical study. The manuscript is deliberate about its boundaries. We do not claim that existing standards cannot represent care processes: FHIR workflow resources, computer-interpretable guidelines, and process mining already do so once a process has been structured, and we present them as complementary downstream infrastructure. The capability we localize is upstream and currently unmet: recovering incompletely expressed, patient-specific intent from natural communication and converting it into computable, executable records. We include an explicit ACR-to-FHIR element mapping to make that placement concrete.

We also distinguish the layer from adjacent clinical-NLP work. Established action-item, medical-order, and decision-extraction efforts recover useful content from notes and conversation, but typically into flat schemas evaluated by lexical overlap. The distinctive computation here is twofold: recovering each intended action with the actor, temporal, conditional, and dependency structure needed to execute it, and reasoning over the *set* of intents an encounter produces through individuation, scheduling, contradiction detection, and consistency checking. We propose evaluating this on **executable correctness** rather than text overlap.

We are explicit about evidence. This paper is a framework and a vocabulary; the feasibility results in Section 7 come from two separately reported companion studies and are presented as record-level feasibility, not as validation of the full framework. A FHIR-aligned benchmark study shows that current models recover an action's type reliably but recover its closed fields jointly far less often, and a hybrid neuro-symbolic follow-up study shows that separating learned interpretation from computed structure removes date error in a controlled setting. Clinical utility and safety are stated as prospective hypotheses, with human confirmation as the expected operating mode until task-specific calibration and prospective evidence justify more.

We believe the readership of *Artificial Intelligence in Medicine*, spanning medical-AI researchers, clinical informaticians, and standards developers, is the right audience to adopt, extend, evaluate, or refute these constructs, and that a shared target for "computable clinical intent" is timely as ambient documentation and clinical language models move from producing notes toward producing tasks and orders.

This manuscript is original, has not been published previously, and is not under consideration elsewhere. Both authors have read and approved the submission and agree to its content. No new data were generated for this article, and it involved no human-subjects data collected by the authors. The authors declare no competing interests and no external funding. Correspondence should be addressed to Yehudit Aperstein (apersteiny@afeka.ac.il).

Thank you for considering our submission. We would be glad to respond to any questions.

Sincerely,

Yehudit Aperstein (corresponding author), on behalf of\
Alexander Apartsin, Holon Institute of Technology (HIT)\
Yehudit Aperstein, Afeka Academic College of Engineering
