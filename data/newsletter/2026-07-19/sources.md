# Newsletter sources — 2026-07-19 (fetched UTC 2026-07-19T03:02:47Z)

Theme: Segmentation grows up — cell-segmentation foundation models reach a superhuman generalist (Cellpose-SAM), honest 2026 benchmarks show no single winner (and why open comparison matters), and the frontier moves into 3D.

## Item 1 — Cell segmentation's generalist: Cellpose-SAM
- Cellpose-SAM — bioRxiv (Apr 2025) — https://www.biorxiv.org/content/10.1101/2025.04.28.651001v1 — (grounded via search) merges SAM's pretrained transformer backbone with the Cellpose framework; trained on 22,826 images / 3,341,254 ROIs integrating Cellpose, Cellpose Nuclei, Omnipose, TissueNet, LiveCell, YeaZ, DeepBacs, NeurIPS-2022, MoNuSeg, etc. Substantially outperforms inter-human agreement / approaches the human-consensus bound. Made robust to channel shuffling, cell size, shot noise, downsampling, blur. Key insight: the segmentation FRAMEWORK (Cellpose) matters as much as the pretrained backbone (SAM). Already used in commercial spatial platforms (Bruker CosMx, Vizgen MERSCOPE).
- CellSAM — Nature Methods 2025 — https://www.nature.com/articles/s41592-025-02879-w

## Item 2 — The 2026 benchmark reality: no model wins everywhere
- "Revisiting foundation models for cell instance segmentation" — MIDL 2026 — https://arxiv.org/abs/2603.17845 — FETCHED. Benchmarks CellPoseSAM, CellSAM, µSAM/PathoSAM, CellPose3 vs general SAM/SAM3 across 36 datasets, 4 modalities (fluorescence, label-free, histopathology; cell + nucleus). Introduces Automatic Prompt Generation (APG): derives point prompts from µSAM decoder predictions (no retraining). Central finding: "none of the SAM-based microscopy foundation models combine all three adaptation strategies" (automatic prompts + custom decoder + finetuning) — APG fills the gap. Results: CellPoseSAM and APG rank top-three across all four modalities; SAM3 "performed well – though not yet competitive with domain-specific foundation models" and was prompt-sensitive (did not even recognize the text prompt "nucleus"). Performance correlated with domain-specific training-data size. (SAM2 dropped — inferior to SAM here.) APG code in the open micro-sam repo.
- Live-microscopy + spatial-omics benchmark (Apr 2026) — https://www.biorxiv.org/content/10.64898/2026.04.18.719315v1.full — different models win on different modalities (Cellpose-SAM strong on phase contrast; SAM-based on fluorescence cell culture; Mesmer/InstanSeg on CODEX).
- Lab tie-in: BioImage Model Zoo (share + TEST models in the browser) /project/bioimage-model-zoo/ ; Simon's SAM3 concept-aware segmentation work.

## Item 3 — The frontier moves into 3D
- "A Multimodal 3D Foundation Model for Light Sheet Fluorescence Microscopy" — arXiv:2605.26026 (Scheinfeld, Zhang et al.) — FETCHED (partial; PDF). Few-shot segmentation, classification, and deblurring for light-sheet volumes; self-supervised (DINO/iBOT/BERT-style); builds on the Cellpose/SAM/StarDist lineage; uses Allen Brain data; U-Net/Swin-UNETR/MONAI backbones; code public. Addresses the 2D limitation flagged by the MIDL benchmark.
- Lab tie-in: Self-driving Microscope /project/self-driving-microscope/ ; BioEngine (deploy/serve models) /project/bioengine/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- Cellpose-SAM is Apr 2025; framed as the established generalist. 3D light-sheet FM PDF only partially machine-readable — described at a high level, no invented figures.
- Avoided repeating recent digests (Jul 11-18): VCC results/data-decides, LAP/agent-instrument, microbiome FMs, MaxToki/aging, Biomni, C2S-Scale.
