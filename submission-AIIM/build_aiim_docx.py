"""Build the AIIM Word (.docx) manuscript from index.html via the html2doc skill.

Depends on the LaTeX build having run first (build_aiim_tex.py), which regenerates
submission-AIIM/latex_src/paper_build.html and latex_build/figures/Figure_N.pdf
(Chromium-rendered from the current inline SVGs). This script rasterizes those
figure PDFs to high-res PNG (Word-safe; SVG-in-DOCX is unreliable across Word/
Elsevier), rewrites the build HTML to reference the PNGs, and runs the three
html2doc stages into submission-AIIM/Computable-Clinical-Intent_AIIM.docx.
"""
import subprocess, sys, os
from pathlib import Path
import fitz

SUB = Path(r"E:\Projects\Submitted\three-generations-healthcare-it\submission-AIIM")
SRC = SUB / "latex_src"
FIGS = SRC / "figures"
FPDF = SUB / "latex_build" / "figures"
SKILL = Path(r"C:\Users\apart\.claude\skills\html2doc")
PY = r"C:\Python314\python.exe"
NODE_MODULES = str(SKILL / "node_modules")
OUT = SUB / "Computable-Clinical-Intent_AIIM.docx"

# 1. rasterize the current figure PDFs to high-res PNG
for n in (1, 2, 3):
    pix = fitz.open(str(FPDF / f"Figure_{n}.pdf"))[0].get_pixmap(matrix=fitz.Matrix(3, 3), alpha=False)
    pix.save(str(FIGS / f"Figure_{n}.png"))
    print(f"Figure_{n}.png: {pix.width}x{pix.height}")

# 2. docx-input HTML referencing PNGs (Word-safe) instead of the inline-extracted SVGs
html = (SRC / "paper_build.html").read_text(encoding="utf-8")
for n in (1, 2, 3):
    html = html.replace(f"figures/Figure_{n}.svg", f"figures/Figure_{n}.png")
(SRC / "docx_build.html").write_text(html, encoding="utf-8")

def run(cmd, env=None):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    print(" ".join(str(c) for c in cmd[:2]), "->", r.returncode)
    tail = "\n".join((r.stdout or "").splitlines()[-4:])
    if tail: print(tail)
    if r.returncode != 0:
        print(r.stderr[-1500:]); sys.exit(1)
    return r.stdout

env = dict(os.environ, NODE_PATH=NODE_MODULES)
# stage 1: KaTeX -> MathML (no math here, but keeps the pipeline uniform)
run(["node", str(SKILL/"scripts"/"katex_to_mathml.js"), "--input", str(SRC/"docx_build.html"),
     "--output", str(SRC/"_mathml.html")], env=env)
# stage 2: MathML -> DOCX (figures embed as PNG; verify the "Figures: N/M" canary)
out = run([PY, str(SKILL/"scripts"/"convert_to_docx.py"), "--input", str(SRC/"_mathml.html"),
           "--output", str(SUB/"_docx_converted.docx"), "--profile", "camera-ready-generic"])
assert "3 embedded / 3 referenced" in out, "figure embedding regressed"
# stage 3: academic styling
run([PY, str(SKILL/"scripts"/"apply_academic_style.py"), "--input", str(SUB/"_docx_converted.docx"),
     "--output", str(OUT), "--profile", "camera-ready-generic"])

# verify media are all PNG
import zipfile
media = [n for n in zipfile.ZipFile(str(OUT)).namelist() if n.startswith("word/media/")]
assert media and all(m.lower().endswith(".png") for m in media), ("non-PNG media", media)
print("OK:", OUT.name, "| media:", [m.split('/')[-1] for m in media])
# clean intermediates
for f in ["_docx_converted.docx"]:
    (SUB/f).unlink(missing_ok=True)
(SRC/"_mathml.html").unlink(missing_ok=True)
