# Newsletter sources — 2026-07-26

Theme: **Cells in Context** — AI restoring the spatial dimension that dissociation
erases. Predict spatial expression cheaply from images; transfer spatial context
onto legacy dissociated data; automate the whole spatial-analysis workflow with agents.

## Provenance / method
- Web research (WebSearch + WebFetch). X/Twitter sweep **skipped**: `scripts/lab-x.py
  monitor` returned **HTTP 402 Insufficient credits** (getxapi account out of credits).
  `x-breaking` workflow stays disabled until topped up.
- Every claim below cross-checked against a primary or high-quality secondary source.
  Publication dates and peer-review status verified and stated honestly.

## Item 1 — Path2Space: spatial transcriptomics predicted from H&E slides (Cell, 2026)
- Primary: *Cell* (2026), "AI-predicted spatial transcriptomics unlocks breast cancer
  biomarkers from pathology." https://www.cell.com/cell/abstract/S0092-8674(26)00458-7
  (ScienceDirect: https://www.sciencedirect.com/science/article/abs/pii/S0092867426004587)
- Earlier preprint (2024): bioRxiv https://www.biorxiv.org/content/10.1101/2024.10.16.618609v1
- Verified figures (via WebSearch of the abstract/coverage):
  - Predicts spatial expression of **thousands of genes** from H&E histology, vs prior
    methods limited to "only a few hundred genes."
  - **Outperforms 21 established methods.**
  - Charts the TME of **976 TCGA breast tumors**; infers cell-type abundances; identifies
    **three spatially defined prognostic subgroups** ("SpatioTypes") with distinct survival.
  - Predicts response to **chemotherapy and trastuzumab** better than costly
    bulk-sequencing biomarkers. HER2 spatial **heterogeneity** predicts trastuzumab
    response (concordant with the "bystander hypothesis"); method SPAND quantifies it.
  - Validation: trained on TransNEO (cross-val), validated on IMPRESS, PBCP, Cedars-Sinai.
  - Leads: Roshan Lodha, Eldad D. Shulman, Danh-Tai Hoang, Kenneth Aldape, Eytan Ruppin.
- Note: peer-reviewed *Cell* 2026 — the freshest, most solid item. Framed as such.

## Item 2 — Nicheformer: a foundation model bridging single-cell + spatial (Nature Methods, 2025)
- Primary: *Nature Methods* (2025), "Nicheformer: a foundation model for single-cell and
  spatial omics." https://www.nature.com/articles/s41592-025-02814-z (DOI 10.1038/s41592-025-02814-z)
- Institutional writeup (verified via WebFetch): Helmholtz Munich —
  https://www.helmholtz-munich.de/en/newsroom/news-all/artikel/new-foundation-model-reveals-how-cells-are-organized-in-tissues
- Verified figures:
  - "First large-scale foundation model that integrates single-cell analysis with spatial
    transcriptomics." Helmholtz Munich + TUM (Theis lab); co-first authors Alejandro
    Tejada-Lapuerta and Anna Schaar.
  - Trained on **>110M cells** — **SpatialCorpus-110M** = 57M dissociated + 53M spatial.
  - Key capability: **transfer spatial context onto dissociated single-cell data at scale**;
    shows "spatial patterns leave measurable traces in gene expression, even when cells are
    dissociated."
- Note: published **2025** — a foundational reference, framed as context (not "breaking").

## Item 3 — SpatialAgent: an autonomous AI agent for spatial biology (bioRxiv preprint, Apr 2025; C&EN feature May 2026)
- Preprint: bioRxiv (posted Apr 2025), "SpatialAgent: An autonomous AI agent for spatial
  biology." https://www.biorxiv.org/content/10.1101/2025.04.03.646459v1
  (DOI 10.1101/2025.04.03.646459). Code: https://github.com/Genentech/SpatialAgent
- Renewed coverage: *Chemical & Engineering News* (May 2026), "Advances in imaging tools
  offer spatial biology for the AI age."
  https://cen.acs.org/analytical-chemistry/big-data/spatial-biology-data-artificial-intelligence/104/web/2026/05
- Verified figures / **honest caveats**:
  - Genentech + Stanford. LLM + dynamic tool execution + adaptive reasoning; **autonomous**
    and **co-pilot** modes; spans design → multimodal analysis → hypothesis generation.
  - Benchmark: ~**2M cells** (human brain, heart; mouse colon colitis). Authors report it
    "**matched or outperformed human scientists across key tasks**" — **this is a PREPRINT
    claim, NOT peer-reviewed.** Framed explicitly as such.
  - Heart annotation: matched expert accuracy while **cutting annotation time ~80%**.
  - Hypothesis generation: surfaced novel **TGF-β fibroblast–pericyte** interactions in
    colitis "overlooked in original studies."
  - Compared against 4 computational methods + 10 human experts (gene-panel design);
    7 human scientists (heart annotation).
- Industry context (from C&EN coverage / adjacent search): GSK paid **$50M** (Jan 2026)
  to license spatial-cancer foundation models from startup **Noetik**.

## Lab connections (for the "why it matters" framing)
- Path2Space = image → molecular prediction: exactly the lab's bioimage+omics fusion and
  ProtiCelli's image-to-molecule ethos; also the "cheap surrogate for an expensive assay."
- Nicheformer = foundation-model/data-curation angle → virtual cell, data-readiness lesson.
- SpatialAgent = agents doing the science → Agent-Lens, BioImage.IO chatbot, REEF closed
  loop. Honest note: preprint, agents propose; the bench must still validate.

## De-dup check
- Recent digests: Jul 25 antibody design; Jul 24 open science; Jul 23 protein/genome design;
  Jul 22 protein dynamics + drug-repurposing agents; Jul 21 microscopy VLMs + pathology FMs;
  Jul 18 "Data Decides"; Jul 13 "Wiring Diagrams"; Jul 9 "4D whole-cell sim."
- Grepped all recent posts for spatial/Nicheformer/Path2Space/SpatialAgent — **no prior
  coverage** of the spatial-omics theme or any of these three items. Clear to run.
