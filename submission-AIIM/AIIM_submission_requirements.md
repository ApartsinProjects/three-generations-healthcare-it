# AIIM (Artificial Intelligence in Medicine, Elsevier) - Submission Requirements
Source: journal Guide for Authors (captured to AIIM_guide_for_authors.txt). Journal: ISSN 0933-3657; Impact Factor 7.8, CiteScore 15.0; hybrid (free-to-publish subscription route; OA optional).

## Article type: Position paper  (our target)
"Papers that gather, describe, and analyze the scientific challenges of a specific field, founding them on the related literature." Unsolicited submissions accepted. (Editorials and guest editorials are invited-only.)

## Hard formatting rules
- **Abstract**: concise, factual, **<= 250 words**, must stand alone, **avoid references** (if essential, cite author + year), avoid uncommon abbreviations. **Unstructured** (single paragraph).
- **Keywords**: **1 to 7**, English; avoid multi-word keywords using "and"/"of"; abbreviations only if firmly established.
- **Highlights** (encouraged, separate editable file with "highlights" in filename): **3 to 5 bullets, each <= 85 characters incl. spaces**; capture novel results/methods.
- **References**: Vancouver **numbered** style `[1]` in order of appearance; journal names abbreviated (LTWA); **DOIs encouraged**; references cited in the abstract must be given in full. Example:
  `[1] Van der Geer J, Hanraads JAJ, Lupton RA. The art of writing a scientific article. J Sci Commun 2020;163:51-9. https://doi.org/10.1016/j.sc.2020.00372.`
- **CRediT author statement**: required.
- **Declaration of generative AI use**: required section IF generative AI was used in the writing process (author decision to disclose).
- **Appendices**: label A, B, ...; equations Eq. (A.1); tables/figures Table A.1 / Fig. A.1.
- **File format**: LaTeX (Elsevier elsarticle / els-cas class) OR Word accepted for submission.
- **Word count**: no fixed limit stated for position papers.

## Status of our manuscript vs these rules
- Abstract: unstructured, single paragraph (see word count printed at build). OK if <= 250.
- Keywords: 7, mostly single/compound terms. OK (a couple are multi-word; acceptable but could trim).
- References: already numbered Vancouver with abbreviated journals + DOIs. MATCHES.
- CRediT: present. Funding/COI: present.
- TODO before submission: (1) add Highlights file (3-5 bullets <=85 chars); (2) decide genAI-use declaration; (3) resolve the 2 pending FHIR-adoption citations [NR1],[NR2]; (4) build LaTeX (els-cas) + Word from index.html.

## Official AIIM template & tool links (verified from the journal's own Guide for Authors)
- **LaTeX template AIIM links to**: `els-cas-templates.zip` via https://assets.ctfassets.net/o78em1y1w4i4/5uFmLZJTPDMAUjFnHRpjj8/6f19a979146eb93263763d87a894ab0d/els-cas-templates.zip  -> **byte-identical (md5 7753a16940bccbde50b20cc69899e8c1) to the CTAN copy in templates/**. So the Elsevier **CAS** template IS the official AIIM template. Guide wording: "We encourage you use our LaTeX template when preparing a LaTeX submission."
- **LaTeX submission instructions**: https://www.elsevier.com/latex
- **Highlights tool/examples**: https://www.elsevier.com/researcher/author/tools-and-resources/highlights  (3-5 bullets, <=85 chars each, separate editable file with "highlights" in the filename)
- **Word**: NO journal-specific Word template for AIIM. Word `.doc/.docx` is accepted for submission; the only Elsevier `.docx` templates on the page are for *other* article types (Data in Brief, MethodsX), not AIIM research/position papers.
- **References**: no proprietary reference-manager template needed; follow the Vancouver numbered examples in the guide (which the manuscript already matches).

## Templates downloaded (templates/)
- `els-cas-templates/` - **the official AIIM template** (Elsevier "CAS" class): `cas-sc` (single-column) and `cas-dc` (double-column) `.tex` + `.cls` + sample PDFs + `cas-model2-names.bst` (numbered). Use **cas-sc** (single-column) for a Position Paper.
- `elsarticle/` - classic Elsevier class (fallback), + template-num/harv/num-names `.tex`.
