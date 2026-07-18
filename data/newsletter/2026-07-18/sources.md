# Newsletter sources — 2026-07-18 (fetched UTC 2026-07-18T03:03:56Z)

Theme: Data decides — across cells and brains, the winning lesson is that curated, interoperable, provenance-rich data (plus hybrid methods) beats pure model scale.

## Item 1 — Virtual Cell Challenge verdict: hybrids + curated data won
- Arc Institute wrap-up — https://arcinstitute.org/news/virtual-cell-challenge-2025-wrap-up — FETCHED. Inaugural Virtual Cell Challenge (results at NeurIPS, Dec 2025; sponsored by NVIDIA, 10x Genomics, Ultima). Winners: 1st ($100k) BioMap Research "xTrimoSCPerturb" — a HYBRID of deep learning + classical statistics; 2nd ($50k) Sichuan Univ "XLearning"; 3rd ($25k) Team Outlier (UChicago/Dartmouth/HKU) "TransPert" (statistical: pseudo-bulk + Wilcoxon + global linear scaling, summary-level data only); Generalist Prize ($100k) Altos Labs "go-with-the-flow" (flow-matching generative model). 5,000+ registrants / 114 countries / 1,200+ teams / 300+ final. Benchmark: ~300,000 scRNA-seq from H1 human ESCs, 300 CRISPRi perturbations (10x Flex, >50k UMIs/cell, ~1,000 cells/perturbation). Metrics PDS/DES/MAE (+ 4 from Arc's State model; open-source Cell-Eval). KEY: models "not yet consistently outperforming naive baselines across all metrics" (nearly all worse than baseline on MAE); "Purely AI-based approaches did not consistently outperform statistical baselines"; pure end-to-end hasn't solved it — DL+classical won.
- Coverage: GEN (Altos Generalist Prize) — https://www.genengnews.com/topics/artificial-intelligence/neurips-2025-altos-labs-wins-generalist-prize-at-arcs-virtual-cell-challenge/
- Lab tie-in: virtual cell / Human Cell Simulator /project/human-cell-simulator/

## Item 2 — The foundation-model wave reaches the brain (where data allows)
- The Transmitter (Sean Hill) — https://www.thetransmitter.org/artificial-intelligence/ai-cant-solve-the-brain-without-data-that-fit-together/ — FETCHED. MICrONS (Wang et al., Nature, Apr 2025): FM trained on calcium imaging from ~135,000 neurons in mouse visual cortex; generalizes to new mice; links function to structural connectivity; corpus took ~half a decade. TRIBE v2 (Meta, Mar 2026): tri-modal brain-encoding model predicting fMRI responses to visual/auditory/language stimuli; 1,000+ hours fMRI / ~720 participants; enabled by BIDS + Human Connectome Project + UK Biobank.

## Item 3 — Because interoperable data is the real bottleneck
- The Transmitter (same piece) — FETCHED. Brain FMs emerged because fields did the "slow, unglamorous work of making data that fits together," not because models got smarter. Needs: shared file/data standards (BIDS, NWB), protocol standardization (stimulus/temperature/calibration), operational provenance. "Machines don't apprentice" — tacit method must become explicit. Liquid-junction-potential example (uncorrected shifts membrane readings 10-15 mV). Tripathy et al.: back-modeling methodological covariates raised neuron-type classification 48% -> 81% (most "unexplained" variance was unrecorded methodology). Analogy: AlphaFold worked because the Protein Data Bank had decades of standardized reporting. COI disclosed (Hill founded Senscience/FAIR², advises BICAN Knowledgebase).
- Lab tie-in: FAIR, agent-readable models/data — BioImage Model Zoo /project/bioimage-model-zoo/ ; BioEngine /project/bioengine/ ; curated data-with-provenance engine = REEF /project/reef-imaging-farm/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- VCC results are Dec 2025; TRIBE v2 Mar 2026; MICrONS Apr 2025 — framed as the state of the field / evergreen strategy lesson (The Transmitter piece is recent), not dated as breaking.
- Avoided repeating recent digests (Jul 10-17): LAP/agent-instrument, Biomni, MaxToki/aging, C2S-Scale, interactome/AlphaFold, microbiome FMs.
