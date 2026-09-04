# index.html -> els-cas (cas-sc) mapping for the AIIM build

The HTML has been normalized to Elsevier conventions so the .tex is a mechanical conversion.
Target: single-column Position Paper, `\documentclass[a4paper]{cas-sc}`, numbered Vancouver refs.

## Decisions already applied to index.html
- **Headings**: consistent Title Case, numbered `N.` / `N.M`. At conversion, STRIP the leading `N.` / `N.M ` from each heading -> `\section{...}` / `\subsection{...}` (cas-sc auto-numbers). Section order is unchanged, so in-text "Section 2", "Sections 4-5", "Section 5.3", etc. remain correct against the auto-numbers.
- **Citations**: in-text now inline Elsevier numbered style `[n]` / `[n,m]` / `[n-p]`, placed BEFORE sentence punctuation (e.g. "fails [3],"). Each maps to `\cite{keyN}`. Reference list is Vancouver numbered, order of appearance.
- **Tone/format**: no em-dashes, no double-hyphens in prose, en-dashes for ranges in the reference list.

## Element -> LaTeX mapping
| HTML | els-cas LaTeX |
|---|---|
| `<h1>` title | `\title[mode=title]{...}` |
| authors + `<sup>` affil marks | `\author[1]{...}` + `\affiliation[n]{organization=,addressline=,city=,postcode=,country=}` |
| correspondence line | `\cormark[1]` + `\cortext[1]{Corresponding author}` + `\ead{...}` |
| ORCID | `\author[...]{...}[orcid=...]` |
| `<div class="abstract">` (unstructured) | `\begin{abstract}...\end{abstract}` |
| Keywords line | `\begin{keywords} kw \sep kw \sep ... \end{keywords}` |
| (Highlights file, separate) | `\begin{highlights}\item ...\end{highlights}` (3-5 items, <=85 chars) -- TODO author |
| `<h2>N. ...` / `<h3>N.M ...` | `\section{...}` / `\subsection{...}` (strip the number) |
| `<div class="defn">` (Definition 1) | framed box: `\begin{tcolorbox}` or a `description`/quote block; keep the ACR tuple as `\texttt{}` |
| `<div class="ex">` (worked example) | framed box (tcolorbox) or a small `\begin{table}`-style panel; the `.rec` spans -> `\texttt{}` |
| `<figure><svg>` + `<figcaption>` | `\begin{figure}\centering\includegraphics{figures/figN.pdf}\caption{...}\label{figN}\end{figure}` -- use the PNG/PDF from `figures/`, not the inline SVG |
| `<table class="cmp">` | `\begin{table}\caption{...}\begin{tabular*}{\tblwidth}{...}\toprule...\bottomrule\end{tabular*}\end{table}` |
| caption "Figure N." / "Table N." prefix | DROP the manual prefix; `\caption{}` auto-numbers |
| Data Availability / Funding / COI | back-matter sections (unnumbered) or Elsevier declaration blocks |
| CRediT paragraph | `\credit{...}` per author + `\printcredits` |
| `<div class="refs"><ol>` (55 `<li>`) | `cas-refs.bib` (BibTeX) + `\bibliographystyle{model1-num-names}` + `\bibliography{cas-refs}` |

## Build-time notes
- **Bib style**: cas-sc template ships defaulting to `cas-model2-names` (author-year). SWITCH to numbered: `\bibliographystyle{model1-num-names}` with `\usepackage[numbers]{natbib}`, to match AIIM's Vancouver `[n]` examples.
- **Figures**: convert the 3 inline SVGs to PDF (vector) for LaTeX; publication-ready PNG/SVG already exist under `figures/`.
- **Boxes**: `.defn` and `.ex` need a float/box environment (tcolorbox recommended) since cas-sc has no native callout.
- **Ref [54]** (ONC Cures Act, Federal Register) is grey literature: BibTeX `@misc`/`@techreport` with `howpublished`/`note` = "Fed Regist 2020;85:25642" + URL.
- Recommended converter: `html2tex` skill with the `elsarticle` template as a base, then graft into `cas-sc`; or hand-fill `cas-sc-template.tex` (frontmatter is small).
