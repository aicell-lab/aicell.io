# Newsletter sources — 2026-07-13 (fetched UTC 2026-07-13T03:03:03Z)

Theme: Wiring diagrams for the cell — the structural interactome goes public at scale, interpretable foundation models map the regulatory wiring, and honest tests ask whether the diagrams are real.

## Item 1 — The interactome goes public at scale (AlphaFold Database complexes)
- EMBL-EBI — https://www.embl.org/news/science-technology/first-complexes-alphafold-database/ — FETCHED. EMBL-EBI + Google DeepMind + NVIDIA + Seoul National University (Steinegger Lab). 30M complexes calculated; 1.7M high-confidence homodimer predictions added + 18M lower-confidence homodimers (bulk download); heterodimer update (19 May 2026): ~80,000 high-confidence + 8.1M lower-confidence heterodimers. Recreating would take ~17M GPU-hours. AFDB: 3.4M+ users, 190 countries. "First step toward a full description of the human interactome" (>20k proteins, complexity from PPIs). Quotes: Jo McEntyre (EMBL-EBI), Anthony Costa (NVIDIA), Martin Steinegger (SNU), Anna Koivuniemi (DeepMind). Main article 16 Mar 2026.
- Lab tie-in: ProtiCelli recovers protein-protein interaction landscapes /publication/sun-2026-proteome-wide/

## Item 2 — Interpretable foundation models map the regulatory wiring
- CellVQ — Nature Communications 2026 — https://www.nature.com/articles/s41467-026-70071-5 — (fetch blocked: Nature auth; grounded via search) interpretable single-cell foundation model; outperforms scGPT & scFoundation on clustering, annotation, property/gene/drug-perturbation and drug-response prediction; CellVQ + CellVQ-Graph used for cell-state discovery, gene discovery, gene regulatory network (GRN) analysis, multimodal analysis — emphasis on INTERPRETABILITY.
- CellxPert (Novartis) — https://arxiv.org/abs/2605.00930 — multimodal single-cell FM; hierarchical molecular/cellular/multicellular layers; critiques token-shuffling perturbation methods that push models out-of-distribution; aims for biologically grounded in-silico perturbation.

## Item 3 — The honest test: are the wiring diagrams real?
- "Attention captures co-expression rather than unique regulatory signal" — https://arxiv.org/abs/2602.17532 — systematic eval of single-cell FM interpretability.
- Perturbation prediction still contested vs simple baselines (Nat. Methods 2025, "does not yet outperform simple linear baselines"); benchmarks like PertEval-scFM exist because it's unsolved.
- Largest perturbation atlases (fuel): Tahoe-100M (100M cells, 50 lines, 1,100 drugs; Arc Virtual Cell Atlas); genome-wide Fix-Cryopreserve Perturb-seq ~8M cells all protein-coding genes.
- Lab tie-in: interpretability + validation over scale = REEF closed loop /project/reef-imaging-farm/ ; Human Cell Simulator /project/human-cell-simulator/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- CellVQ primary paywalled to direct fetch (Nature auth); grounded via search excerpts + arXiv for CellxPert. No fabrication.
- Avoided repeating recent digests (Jul 5–12): AI drug discovery economics, Claude Science/connectors, RNA/CRISPR design, AI co-scientists, whole-cell sim, genome FMs, HEX, open-weight models.
