# Newsletter sources — 2026-07-25 (fetched UTC 2026-07-25T03:02:44Z)

Theme: Designed to bind — AI now generates antibodies (and cryo-EM confirms them), but the honest map shows the sure win is manufacturability/affinity maturation while de novo design is still early.

## Item 1 — AI designs antibodies from scratch, structurally validated (MAGE)
- VUMC news — https://news.vumc.org/2025/11/04/ai-can-speed-antibody-design-to-thwart-novel-viruses-study/ — FETCHED. MAGE (Monoclonal Antibody Generator), a protein language model (Georgiev lab, VUMC; first author Perry Wasdin), published in Cell (4 Nov 2025). Designs functional human antibodies recognizing viral surface proteins WITHOUT needing part of the antibody sequence as a template. Trained on antibodies vs a known H5N1 (bird flu) strain, it generated antibodies against a related but UNSEEN influenza strain. Cryo-EM revealed an RSV fusion protein bound to fragments of two MAGE-designed antibodies. Funded by ARPA-H (up to $30M) + NIH. Georgiev: "an important early milestone toward... designing novel biologics computationally." (Note: a SEPARATE later study, 16 Jan 2026, reported an RSV/hMPV cross-neutralizing antibody — not the MAGE paper.)

## Item 2 — The surer win: predicting whether an antibody can be MADE
- Drug Discovery News (2026) — https://www.drugdiscoverynews.com/antibody-design-with-ai-foundation-models-generative-approaches-and-the-biologics-pipeline-17359 — FETCHED. Antibody design "is not simply small-molecule design applied to bigger molecules" (vast sequence space, severe developability constraints, complex binding). Highest-confidence near-term value = DEVELOPABILITY prediction — it "front-loads failure": aggregation propensity, stability/expression, solubility/viscosity, immunogenicity risk. A 2026 study showed protein language models support developability in real pipelines via supervised prediction + "unsupervised screening using sequence perplexity." PLMs also do guided affinity maturation, humanization/liability removal.

## Item 3 — Reality check: de novo antibody design is still early
- Same Drug Discovery News (FETCHED). De novo design is "genuinely advancing but still early." The Germinal method generates antibody CDR loops against a chosen epitope with no starting binder — benchmark binding rates ~10.6% (heavy-chain CDR3) and ~1.8% (full heavy-chain CDR). Clinical antibodies are mostly "AI-assisted, not fully AI-designed"; affinity maturation is the "mature use." Best recipe: pair generative AI with experimental affinity maturation + high-throughput screening in an iterative loop.
- Context: anticipatory/pandemic-ready design — J Pharm Pharm Sci review — https://pmc.ncbi.nlm.nih.gov/articles/PMC13194078/ ; "Vaccinology in the AI era" — Sci Transl Med — https://www.science.org/doi/abs/10.1126/scitranslmed.adu3791
- Lab tie-in: generative modeling + structural validation — ProtiCelli /publication/sun-2026-proteome-wide/ ; propose->validate loop — REEF /project/reef-imaging-farm/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- Corrected a search overstatement: no "inflection point / solved" claim — the fetched source frames de novo as "advancing but still early." RSV/hMPV cross-protection attributed to the separate Jan-2026 study, not MAGE. No fabrication.
- Avoided repeating recent digests (Jul 18-24): open-science/OpenScience, NovoTags/genome-writing, protein dynamics, microscopy VLMs, enzyme design, segmentation FMs.
