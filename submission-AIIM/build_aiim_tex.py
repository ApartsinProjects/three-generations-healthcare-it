import re, subprocess, sys, shutil
from pathlib import Path

ROOT = Path(r"E:\Projects\Submitted\three-generations-healthcare-it")
SUB = ROOT / "submission-AIIM"
SRC = SUB / "latex_src"
BUILD = SUB / "latex_build"
FIGS = SRC / "figures"
SKILL = Path(r"C:\Users\apart\.claude\skills\html2tex")
PY = r"C:\Python314\python.exe"
PDFLATEX = r"C:\Users\apart\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"

TITLE = "Computable Clinical Intent: Recovering Executable Care Actions from Unstructured Clinical Communication"

# LaTeX-form abstract (quotes as ``...''), kept in sync with index.html (<=250 words)
ABSTRACT = r"""Much of what should happen next is decided in conversation and prose, not structured data. When a clinician writes ``repeat the complete blood count in two weeks,'' the intended action and its timing remain in narrative text, and the accountable owner goes unstated. Leaving intent in free text is implicated in failed test-result follow-up, unclosed referral loops, and avoidable diagnostic harm. We take the position that recovering patient-specific intended actions from unstructured clinical communication, in a form a system can schedule, monitor, and close, is a distinct and tractable problem for artificial intelligence in medicine. It goes beyond clinical language processing, which scores fields one at a time, and complements interoperability standards, which represent intent once structured. We organize health information technology into three layers by the unit each makes computable: the record, the clinical fact, and the intended action. We define the Actionable Clinical Record (ACR): a source-grounded representation of one intended action whose target state is executable readiness, upstream of FHIR workflow resources, not a new interchange format. Recovery has two sides: extracting each action, and reasoning over the resulting set through scheduling, contradiction detection, and consistency checking. Because temporal semantics must be computed and traceability kept source-grounded, not generated, we argue for a hybrid neuro-symbolic architecture with output invariants, and evaluation on executable correctness rather than text overlap. A worked example and two separately reported companion studies support record-level tractability. The ACR and its evaluation framework are offered for the community to build on, evaluate, or refute."""

FRONTMATTER = r"""\author[hit]{Alexander Apartsin}
\author[afeka]{Yehudit Aperstein}
\affiliation[hit]{organization={School of Computer Science, Faculty of Sciences, Holon Institute of Technology (HIT)}}
\affiliation[afeka]{organization={Intelligent Systems, Afeka Academic College of Engineering}}

\begin{abstract}
%ABS%
\end{abstract}

\begin{keyword}
clinical intent \sep actionable clinical record \sep clinical natural language processing \sep neuro-symbolic reasoning \sep temporal reasoning \sep FHIR \sep workflow automation
\end{keyword}

\end{frontmatter}

\section{Introduction}""".replace("%ABS%", ABSTRACT)

# ---- A. Build paper_build.html from index.html ----
html = (ROOT / "index.html").read_text(encoding="utf-8")
FIGS.mkdir(parents=True, exist_ok=True)
figs = re.findall(r'<figure>(.*?)</figure>', html, re.S)
out = html
for i, fig in enumerate(figs, 1):
    m = re.search(r'(<svg\b.*?</svg>)', fig, re.S)
    svg = m.group(1)
    (FIGS / f"Figure_{i}.svg").write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + svg, encoding="utf-8")
    out = out.replace(svg, f'<img src="figures/Figure_{i}.svg" alt="Figure {i}">', 1)
out = out.replace('<div class="refs">\n<h2>References</h2>\n<ol>',
                  '<div class="refs">\n<h2>References</h2>\n<ol class="refs">', 1)
(SRC / "paper_build.html").write_text(out, encoding="utf-8")
print("A. paper_build.html written; figures:", len(figs))

# ---- B. convert + pack ----
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(" ".join(str(c) for c in cmd[-3:]), "->", r.returncode)
    if r.returncode != 0:
        print(r.stdout[-2000:]); print(r.stderr[-2000:]); sys.exit(1)
    return r.stdout

# clean stale generated files so convert/pack never accumulate into a dirty dir
for f in ["main.tex", "body.tex", "bibliography.tex", "html2tex_compat.tex", "meta.json",
          "main.aux", "main.log", "main.out"]:
    (BUILD/f).unlink(missing_ok=True)
run([PY, str(SKILL/"scripts"/"convert_to_tex.py"), "--input", str(SRC/"paper_build.html"),
     "--out-dir", str(BUILD), "--columns", "2", "--citations", "numeric"])
run([PY, str(SKILL/"scripts"/"pack_tmlr_bundle.py"), "--in-dir", str(BUILD),
     "--template", "elsarticle", "--title", TITLE])

# ---- C. patch main.tex ----
mt = (BUILD/"main.tex").read_text(encoding="utf-8")
# the packer emits a trailing duplicate of the body/bibliography after the first
# \end{document}; the compiler ignores it, but keep the .tex clean by truncating
# at the first \end{document} (the first document is the complete paper + bib).
_ed = "\\end{document}"
if mt.count(_ed) > 1:
    mt = mt[:mt.index(_ed) + len(_ed)] + "\n"
# title (function repl to avoid backslash-escape parsing)
mt = re.sub(r'\\title\{[^}]*\}', lambda m: '\\title{' + TITLE + '}', mt, count=1)
# frontmatter graft + strip leaked header: replace from \author{Anonymous Authors} up to first \section{Introduction}
mt = re.sub(r'\\author\{Anonymous Authors\}.*?\\section\{Introduction\}', lambda m: FRONTMATTER, mt, count=1, flags=re.S)
# xurl after hyperref
if "\\usepackage{xurl}" not in mt:
    mt = mt.replace("\\usepackage{hyperref}", "\\usepackage{hyperref}\n\\usepackage{xurl} % break long URLs", 1)
# Table 3 -> full width
def widen_table3(text):
    idx = text.find("Table 3.}")
    if idx < 0: return text
    start = text.rfind("\\begin{table}[ht]", 0, idx)
    end = text.find("\\end{table}", idx) + len("\\end{table}")
    block = text[start:end]
    nb = (block.replace("\\begin{table}[ht]", "\\begin{table*}[t]", 1)
               .replace("\\begin{tabularx}{\\linewidth}", "\\begin{tabularx}{\\textwidth}", 1)
               .replace("\\end{table}", "\\end{table*}", 1))
    return text[:start] + nb + text[end:]
mt = widen_table3(mt)
# wrap bare bib URLs in \url{}
def wrap_bib_urls(text):
    b = "\\begin{thebibliography}"; e = "\\end{thebibliography}"
    i = text.find(b); j = text.find(e) + len(e)
    if i < 0: return text
    bib = text[i:j]
    def w(mm):
        tok = mm.group(0); url = tok.rstrip('.'); trail = tok[len(url):]
        return tok if url.startswith("\\url{") else "\\url{" + url + "}" + trail
    return text[:i] + re.sub(r'https?://\S+', w, bib) + text[j:]
mt = wrap_bib_urls(mt)

# back-matter: unnumber the trailing declaration sections (Elsevier convention)
for h in ["Data Availability", "Author Contributions (CRediT)", "Funding", "Conflicts of Interest"]:
    mt = mt.replace("\\section{" + h + "}", "\\section*{" + h + "}", 1)
# drop the duplicate "References" section header (thebibliography prints its own)
mt = re.sub(r'\\section\{References\}(\\label\{[^}]*\})?\s*', '', mt, count=1)
# unnumber the two worked-example headings (avoids the ugly 7.0.1 artifact)
mt = mt.replace("\\subsubsection{Worked example:", "\\subsubsection*{Worked example:", 1)
mt = mt.replace("\\subsubsection{Worked scoring:", "\\subsubsection*{Worked scoring:", 1)

# widen the two horizontal schematic figures to full page width for legibility
def widen_figure(text, figfile):
    i = text.find(figfile)
    if i < 0: return text
    start = text.rfind("\\begin{figure}", 0, i)
    end = text.find("\\end{figure}", i) + len("\\end{figure}")
    block = text[start:end]
    nb = (block.replace("\\begin{figure}[tbp]", "\\begin{figure*}[t]", 1)
               .replace("width=\\linewidth", "width=\\textwidth", 1)
               .replace("\\end{figure}", "\\end{figure*}", 1))
    return text[:start] + nb + text[end:]
mt = widen_figure(mt, "Figure_2.pdf")
mt = widen_figure(mt, "Figure_3.pdf")

# widen the one remaining single-column data table (Table 4, 5 columns) to full
# width so it matches Tables 1-3/5 and stops spilling into the margin
def widen_table_caption(text, capmarker):
    i = text.find(capmarker)
    if i < 0: return text
    start = max(text.rfind("\\begin{table}[ht]", 0, i), text.rfind("\\begin{table}[tbp]", 0, i))
    if start < 0: return text
    end = text.find("\\end{table}", i) + len("\\end{table}")
    block = text[start:end]
    nb = (re.sub(r'\\begin\{table\}\[(ht|tbp)\]', r'\\begin{table*}[t]', block, count=1)
              .replace("\\begin{tabularx}{\\linewidth}", "\\begin{tabularx}{\\textwidth}", 1)
              .replace("\\end{table}", "\\end{table*}", 1))
    return text[:start] + nb + text[end:]
mt = widen_table_caption(mt, "Table 4.}")

(BUILD/"main.tex").write_text(mt, encoding="utf-8")
print("C. main.tex patched; title set:", TITLE[:40], "... xurl:", "\\usepackage{xurl}" in mt,
      "table*:", "\\begin{table*}[t]" in mt)

# ---- D. compile ----
run([PY, str(SKILL/"scripts"/"compile_local.py"), "--in-dir", str(BUILD),
     "--auto-patch", "--pdflatex", PDFLATEX])
# enforce a single document (defensive: drop any trailing duplicate the toolchain
# may leave after the first \end{document}), recompile if we had to cut.
mt = (BUILD/"main.tex").read_text(encoding="utf-8")
if mt.count(_ed) > 1:
    mt = mt[:mt.index(_ed) + len(_ed)] + "\n"
    (BUILD/"main.tex").write_text(mt, encoding="utf-8")
    run([PY, str(SKILL/"scripts"/"compile_local.py"), "--in-dir", str(BUILD),
         "--auto-patch", "--pdflatex", PDFLATEX])
mt = (BUILD/"main.tex").read_text(encoding="utf-8")
assert mt.count(_ed) == 1 and mt.count("\\begin{thebibliography}") == 1, "duplicate document survived"
print("D. compiled OK; single document:", mt.count("\\bibitem{ref"), "bibitems")
