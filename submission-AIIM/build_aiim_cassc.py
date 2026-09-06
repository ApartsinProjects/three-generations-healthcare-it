"""Build the AIIM manuscript with Elsevier's official CAS single-column class
(cas-sc), reusing the venue-agnostic body.tex / bibliography.tex / compat
preamble produced by build_aiim_tex.py. Output: cassc_build/main.pdf.
"""
import re, subprocess, sys, shutil
from pathlib import Path

SUB = Path(r"E:\Projects\Submitted\three-generations-healthcare-it\submission-AIIM")
LB = SUB / "latex_build"
CB = SUB / "cassc_build"
SKILL = Path(r"C:\Users\apart\.claude\skills\html2tex")
PY = r"C:\Python314\python.exe"
PDFLATEX = r"C:\Users\apart\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"

TITLE = "Computable Clinical Intent: Recovering Executable Care Actions from Unstructured Clinical Communication"
ABSTRACT = r"""Much of what should happen next is decided in conversation and prose, not structured data. When a clinician writes ``repeat the complete blood count in two weeks,'' the intended action and its timing remain in narrative text, and the accountable owner goes unstated. Leaving intent in free text is implicated in failed test-result follow-up, unclosed referral loops, and avoidable diagnostic harm. We take the position that recovering patient-specific intended actions from unstructured clinical communication, in a form a system can schedule, monitor, and close, is a distinct and tractable problem for artificial intelligence in medicine. It goes beyond clinical language processing, which scores fields one at a time, and complements interoperability standards, which represent intent once structured. We organize health information technology into three layers by the unit each makes computable: the record, the clinical fact, and the intended action. We define the Actionable Clinical Record (ACR): a source-grounded representation of one intended action whose target state is executable readiness, upstream of FHIR workflow resources, not a new interchange format. Recovery has two sides: extracting each action, and reasoning over the resulting set through scheduling, contradiction detection, and consistency checking. Because temporal semantics must be computed and traceability kept source-grounded, not generated, we argue for a hybrid neuro-symbolic architecture with output invariants, and evaluation on executable correctness rather than text overlap. A worked example and two separately reported companion studies support record-level tractability. The ACR and its evaluation framework are offered for the community to build on, evaluate, or refute."""

# 1. assemble the cas-sc build dir from the shared bundle
CB.mkdir(exist_ok=True)
shutil.copy(LB/"html2tex_compat.tex", CB/"html2tex_compat.tex")
shutil.copy(LB/"bibliography.tex", CB/"bibliography.tex")
if (CB/"figures").exists(): shutil.rmtree(CB/"figures")
shutil.copytree(LB/"figures", CB/"figures")
# cas-sc renders \ead with a small email icon from thumbnails/
TH = SUB/"templates"/"els-cas-templates"/"els-cas-templates"/"thumbnails"
if (CB/"thumbnails").exists(): shutil.rmtree(CB/"thumbnails")
shutil.copytree(TH, CB/"thumbnails")

# body_clean.tex: drop the leaked pre-Introduction header block, and turn the
# two-column build's spanning floats (table*/figure*) into plain single-column
# floats with in-place placement so cas-sc (single column) keeps them near their
# text instead of drifting them to the end (Figure 3 was landing after the refs).
body = (LB/"body.tex").read_text(encoding="utf-8")
i = body.index("\\section{Introduction}")
body = body[i:]
body = (body.replace("\\begin{table*}", "\\begin{table}").replace("\\end{table*}", "\\end{table}")
            .replace("\\begin{figure*}", "\\begin{figure}").replace("\\end{figure*}", "\\end{figure}"))
body = re.sub(r'\\begin\{table\}\[[a-z!]*\]', r'\\begin{table}[htbp]', body)
# cas-sc + stfloats defers figure floats to the end regardless of [H]/[!ht], so
# place each figure INLINE (non-floating): centered image + caption as a small
# paragraph. Keeps every figure right where its text introduces it.
def inline_figure(m):
    img, cap = m.group("img").strip(), m.group("cap").strip()
    return ("\\begin{center}\n" + img + "\n\\end{center}\n\\noindent{\\small " + cap + "}\\par\\medskip\n")
body = re.sub(
    r'\\begin\{figure\}\[[^\]]*\]\s*\\centering\s*(?P<img>\\includegraphics[^\n]*)\s*\\caption\{(?P<cap>.*?)\}\s*\\end\{figure\}',
    inline_figure, body, flags=re.S)
(CB/"body_clean.tex").write_text(body, encoding="utf-8")

# 2. main.tex with cas-sc frontmatter
FRONT = r"""\documentclass[a4paper,fleqn]{cas-sc}
\usepackage{hyperref}
\usepackage{xurl}
\usepackage{newtxtext}% scalable text font (microtype expansion needs scalable fonts);
% newtxmath is NOT loaded: cas-sc already declares math fonts and adding it overflows
% the symbol-font limit ("Too many symbol fonts declared").
\input{html2tex_compat.tex}
\captionsetup{labelformat=empty,labelsep=none}% captions carry their own "Figure N." label

\begin{document}
\shorttitle{Computable Clinical Intent}
\shortauthors{Apartsin and Aperstein}
\title[mode=title]{%TITLE%}
\author[1]{Alexander Apartsin}
\affiliation[1]{organization={School of Computer Science, Faculty of Sciences, Holon Institute of Technology (HIT)}}
\author[2]{Yehudit Aperstein}
\affiliation[2]{organization={Intelligent Systems, Afeka Academic College of Engineering}}
\begin{abstract}
%ABSTRACT%
\end{abstract}
\begin{keywords}
clinical intent \sep actionable clinical record \sep clinical natural language processing \sep neuro-symbolic reasoning \sep temporal reasoning \sep FHIR \sep workflow automation
\end{keywords}
\maketitle

\input{body_clean.tex}

\FloatBarrier
\input{bibliography.tex}

\end{document}
""".replace("%TITLE%", TITLE).replace("%ABSTRACT%", ABSTRACT)
(CB/"main.tex").write_text(FRONT, encoding="utf-8")

# 3. compile (pdflatex twice for refs); print first error block if any
def compile_once(label):
    r = subprocess.run([PDFLATEX, "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                       cwd=str(CB), capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode
rc = compile_once("pass1")
compile_once("pass2")
log = (CB/"main.log").read_text(encoding="utf-8", errors="replace")
errs = re.findall(r'^! .*(?:\n.*){0,4}', log, re.M)
if (CB/"main.pdf").exists() and rc == 0 and not errs:
    import fitz
    print("OK: main.pdf pages =", fitz.open(str(CB/"main.pdf")).page_count)
else:
    print("COMPILE ISSUES (rc=%s):" % rc)
    for e in errs[:4]:
        print("----\n" + e.strip())
