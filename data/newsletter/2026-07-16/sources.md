# Newsletter sources — 2026-07-16 (fetched UTC 2026-07-16T03:03:36Z)

Theme: Turning back the cellular clock — an AI that predicts how cells age (with validated drivers), reprogramming that reverses senescence, and why aging is the ultimate dynamic virtual-cell problem.

## Item 1 — MaxToki: a temporal AI model of cellular aging (validated drivers)
- Gladstone — https://gladstone.org/news/new-ai-model-predicts-how-cells-age — FETCHED. MaxToki (Christina Theodoris's lab, Gladstone + NVIDIA); builds on Geneformer. Trained on ~170M cells from healthy humans birth->90+; ~1 trillion genetic tokens; ~billion-parameter (NVIDIA BioNeMo + CUDA-X). Follows tissues THROUGH aging (not snapshots); predicts genes that accelerate/slow aging + age-disease genes. Trained only on healthy data yet detected accelerated aging: pulmonary fibrosis +15 yr, heavy smokers +5 yr, Alzheimer's microglia ~+3 yr (absent in "Alzheimer's-resilience" patients). Heart: flagged candidate aging genes, 5 tested -> aging hallmarks; top-2 pro-aging genes caused heart dysfunction in young mice within a month. Open model+code. bioRxiv "Temporal AI model predicts drivers of cell state trajectories across human aging." Quotes: Gómez Ortega (first author), Theodoris ("targets we would not have tested otherwise"); NVIDIA's Anthony Costa ("over 400x faster").
- Lab tie-in: virtual cell / Human Cell Simulator /project/human-cell-simulator/ (temporal cell-state modeling) ; ProtiCelli /publication/sun-2026-proteome-wide/

## Item 2 — Reversing the clock: reprogramming reverses senescence (AI still emerging)
- Tang et al., Stem Cells Transl Med 2026;15(1):szaf069 (Open Access) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12798543/ — FETCHED (review). Yamanaka-factor (OSKM) reprogramming reverses senescence but risks tumorigenicity; chemical/small-molecule cocktails reset the epigenetic clock WITHOUT genetic manipulation (a chemical-free TCP/RepSox system reduced SA-β-gal in aged fibroblasts, up OCT4/Nanog, down p21/p53/IL6). ~42 representative compounds (Table 1). IMPORTANT: AI appears only in "future directions" (deep learning for small-molecule-target interaction prediction) — NOT a demonstrated "safe-zone" method; safety handled via nanocarriers/targeting/safer combinations. (Correction: blog claims that "AI defines safe zones for reprogramming" are NOT supported by the peer-reviewed source.)
- Industry context (reported, not peer-reviewed here): Altos Labs advancing partial (Yamanaka) reprogramming toward human trials.

## Item 3 — Strategy radar: aging is the dynamic virtual-cell problem
- MaxToki (a Geneformer descendant) shows a trajectory model can surface real, testable aging drivers — the temporal version of the virtual cell. Most single-cell foundation models remain snapshot-based; aging forces the shift to modeling cell-state OVER TIME.
- Lab tie-in: Human Cell Simulator (dynamic, predictive human cell models) /project/human-cell-simulator/ ; REEF for validating predicted drivers /project/reef-imaging-farm/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- Corrected a blog overstatement: the "AI safe-zone for reprogramming" framing is not supported by the peer-reviewed review; reframed honestly (AI role is forward-looking). No fabrication.
- Avoided repeating recent digests (Jul 8-15): Biomni/generalist agents, C2S-Scale, interactome/AlphaFold, AI drug-discovery economics, Claude Science, genome FMs, HEX/spatial proteomics.
