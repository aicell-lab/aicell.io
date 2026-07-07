# Newsletter sources — 2026-07-07 (fetched UTC 2026-07-07T05:38:59Z)

Theme: Big money meets the hard tests — industry pours billions into agentic labs + biology foundation models, while honest benchmarks (linear baselines, unseen splits, cross-modality transfer) keep the field humble.

## Item 1 — Industry goes all-in on agentic labs + biology foundation models
- NVIDIA + Eli Lilly Co-Innovation Lab — https://nvidianews.nvidia.com/news/nvidia-and-lilly-announce-co-innovation-lab-to-reinvent-drug-discovery-in-the-age-of-ai — FETCHED. Up to $1B over 5 yrs; next-gen biology/chemistry foundation+frontier models on NVIDIA BioNeMo; connects Lilly's agentic wet labs to computational dry labs for 24/7 "scientist-in-the-loop" experimentation; robotics/physical AI; Vera Rubin infra; Lilly "AI factory". Announced JPM Jan 12 2026 (frame as 2026-long trend, not breaking). Quotes: Jensen Huang, David Ricks.
- YC agentic drug startups (2026) — https://www.ycombinator.com/companies/industry/drug-discovery-and-delivery — multi-agent "Scientific Agent" companies on biological FMs (ESM-3, RFdiffusion, Boltz-2, AlphaFold).
- NVIDIA + Thermo Fisher (from search): intelligent instruments / autonomous labs, multi-agent NeMo workflows generating protocols + running experiments.

## Item 2 — Virtual cells scale; simple baselines stay stubbornly competitive
- pdpspectra "Virtual Cell Models in 2026" — https://pdpspectra.com/blog/virtual-cell-models-ai-2026/ — FETCHED. "Naive baselines that predict the dataset mean are stubbornly hard to beat on the wrong metric"; "a model that cannot beat the mean on the right metric has learned nothing worth deploying"; "Generalization across perturbations is the actual test, and it is brutal" (unseen perturbations AND unseen cell types = the hard split). STATE (Arc): ~170M observational + 100M+ perturbational cells, 70 cell lines. Virtual Cell Challenge: 5,000+ registrants, 114 countries, 1,200+ teams ("you do not run a global competition to evaluate something you already know how to evaluate").
- Community model catalog — https://github.com/OmicsML/awesome-foundation-model-single-cell-papers (X-Cell, SCALE, PerturbGen, scDFM, xVERSE, Tahoe-x1).
- Benchmark caution (from search): "Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines" (Nature Methods 2025).

## Item 3 — Image-based (Cell Painting) profiling reaches for assay-agnostic foundation models
- Review (Way et al., 2026) "Advances in image-based profiling methods" — https://arxiv.org/abs/2508.05800 (also Mol Syst Biol 10.1038/s44320-026-00197-7) — shift CNN → self-supervised ViT FMs; transformer segmentation CellSAM/CellViT; open benchmarks + software as reproducibility drivers; channel/modality adaptation is the key hurdle (most models assume the 5-channel Cell Painting panel; poor cross-modality transfer). Direct PDF fetch failed to parse; grounded via search excerpts + corresponding author G. Way (CU Anschutz).
- Confounder-aware FM — https://www.nature.com/articles/s44303-025-00116-9 (npj Imaging) — trained on 13M+ Cell Painting images, 107k compounds; SOTA MoA/target prediction seen (0.66/0.65 ROC-AUC) and unseen compounds (0.65/0.73); motivation = accessibility for labs lacking specialized equipment.
- Cell Systems (Feb 2026) "From modality-specific to compositional foundation models for cell biology" — https://www.cell.com/cell-systems/abstract/S2405-4712(26)00016-5
- Cell Painting Gallery (Broad, open) — 656 TB image + numerical data.
- Lab tie-in: BioImage Model Zoo /project/bioimage-model-zoo/ ; BioEngine /project/bioengine/ ; ProtiCelli /publication/sun-2026-proteome-wide/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- Dropped: "Beyond SMILES: Evaluating Agentic Systems for Drug Discovery" (arXiv 2602.10163) — WITHDRAWN by arXiv (license); not cited.
- Avoided repeating recent digests (Jul 1–3): agent harness/benchmarks, virtual-cell world models, rBio, self-driving-labs-industrial framing, Biohub protein world model, thinking microscopes, scAInce.
