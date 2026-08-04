# Newsletter sources — 2026-08-04

Theme: **The cell's fingerprint — image-based (morphological) profiling foundation
models.** Segmentation tells you *where* the cells are (our Jul 19 digest); the next
layer up turns those pixels into *meaning* — a phenotypic fingerprint you can compare,
cluster, and query. 2025–26 delivered a proteome-aware vision foundation model that
reads protein localization and morphology from Human Protein Atlas images and
generalizes **zero-shot** across resolution, channels, and species (**SubCell**), plus
an unusually candid field that names exactly what's still hard: models trained on one
imaging setup don't transfer when the **channels don't match** (**CHAMMI-75**), and the
open problems of temporal/3D data, quality control, and feature interpretation remain
(**image-based profiling review**, Carpenter/Broad camp). A lab-core story — this is the
**measurement layer** beneath the virtual cell, and it sits on the lab's home turf
(HPA imaging; KTH's own Emma Lundberg lab; the BioImage Model Zoo sharing culture).

## Provenance / method
- Web research (WebSearch + WebFetch). X/Twitter sweep **skipped**: `scripts/lab-x.py
  monitor --since-hours 24 --min-likes 30` again returns **HTTP 402 Insufficient
  credits** (getxapi out of credits **~5 weeks**); `search`/`discover` gated.
  x-breaking stays disabled. Flagged to Wei again for a credit top-up.
- **De-dup / variety (important):** the imaging lane has appeared, but this angle has
  **not**. Jul 19 ("Segmentation Grows Up") was **instance segmentation** (Cellpose-SAM,
  CellSAM — *outlining* cells). Jul 21 was **microscopy VLMs** (language/reports).
  Aug 1 was **clinical pathology** (tissue/diagnosis). Jul 26 was **spatial
  transcriptomics** (omics). Aug 2 was the **virtual cell** (predicting perturbation
  from omics). **Image-based / morphological profiling — turning a cell's picture into
  a quantitative phenotypic fingerprint (Cell Painting / HPA, self-supervised ViTs) —
  has not been a theme** in this run. It is the distinct *measurement* layer: not where
  the cell is, not its transcriptome, but what its image says about its state.
- **Verification discipline:** two anchors are **primary-fetched and peer-reviewed**
  (CHAMMI-75 = ICLR 2026, fetched from arXiv abstract; image-based profiling review =
  arXiv, fetched). SubCell is a **bioRxiv preprint** (labeled as such) but is
  extensively corroborated across multiple sources (bioRxiv, PMC, CZI Virtual Cells
  Platform, ResearchGate, an Uppsala seminar page) that agree on scale and architecture;
  it is also deployed on the CZI Virtual Cells Platform. The Cell Systems 2026
  "compositional foundation models" piece is **named for framing only** (cell.com 403s
  WebFetch) — no load-bearing numbers taken from it.

## Item 1 — Capability: SubCell reads phenotype from the picture (ANCHOR, preprint, corroborated)
- Source: Ankit Gupta, Zoe Wefers, Konstantin Kahnert, Jan N. Hansen, Mohini K. Misra,
  Will Leineweber, Anthony Cesnik, Dan Lu, Ulrika Axelsson, Frederic Ballllosera,
  Russ B. Altman, Theofanis Karaletsos, Emma Lundberg, "SubCell: Proteome-aware vision
  foundation models for microscopy capture single-cell biology," **bioRxiv
  2024.12.06.627299** (v1 Dec 2024; v2 30 Oct 2025; *preprint*). DOI
  10.1101/2024.12.06.627299. Also on the **CZI Virtual Cells Platform**
  (virtualcellmodels.cziscience.com/model/subcell) and PMC12636579.
  Affiliations: **KTH Royal Institute of Technology**, Stanford, Chan Zuckerberg
  Initiative / CZ Biohub.
- Corroborated facts (multiple sources agree; preprint — reported by authors):
  - **What it is:** a suite of **self-supervised Vision Transformer** models for
    fluorescence microscopy that "accurately capture cellular morphology, protein
    localization, cellular organization, and biological function." Trained on the
    **proteome-wide Human Protein Atlas** single-cell images — protein expression and
    spatial distribution of **more than 13,000 genes across 37 cell lines** — with a
    **novel proteome-aware learning objective** (multitask framework).
  - **Architecture:** ViT, 12 layers / 12 heads / hidden size 768 / patch size 16;
    outputs **feature embeddings** encoding protein-localization patterns for downstream
    tasks.
  - **Zero-shot generalization (the headline):** "without fine-tuning, SubCell produces
    robust representations of cell morphology and protein localization across diverse
    independent datasets that vary greatly in image resolution, channel markers, cell
    types, and even species."
  - **Downstream tasks:** "localization classification, cell cycle modeling, drug
    response prediction, and mechanism-of-action identification"; generalizes to
    OpenCell, JUMP Cell Painting, drug-treated breast-cancer cells.
  - **Science output:** enables "the first image-based multiscale map of subcellular
    protein organization" and a proteome-wide hierarchical map "directly learned from
    image data," and "enriches protein sequence representations for functional genomics."

## Item 2 — The channel wall: CHAMMI-75 (ANCHOR, ICLR 2026, primary-fetched)
- Source (fetched): Vidit Agrawal, John Peters, Tyler N. Thompson, Mohammad Vali Sanian,
  Chau Pham, Nikita Moshkov, Arshad Kazi, Aditya Pillai, Jack Freeman, Byunguk Kang,
  Samouil L. Farhi, Ernest Fraenkel, Ron Stewart, Lassi Paavolainen, Bryan A. Plummer,
  **Juan C. Caicedo**, "CHAMMI-75: Pre-training multi-channel models with heterogeneous
  microscopy images," **arXiv:2512.20833**; v1 23 Dec 2025, v2 3 Mar 2026; **ICLR 2026**.
- Verified facts / verbatim:
  - **The problem:** morphology models are usually "trained with a single microscopy
    imaging type," yielding "specialized models that cannot be reused across biological
    studies because the technical specifications do not match" — e.g. a "different number
    of channels." The goal is models that are "channel-adaptive and can process any
    microscopy image type."
  - **The resource:** an "open access dataset of heterogeneous, multi-channel microscopy
    images from **75 diverse biological studies**," curated from public sources.
  - **The result:** "training with CHAMMI-75 can improve performance in multi-channel
    bioimaging tasks primarily because of its high diversity in microscopy modalities,"
    paving "the way to create the next generation of cellular morphology models."
    (Specific per-benchmark tables are in the full paper; not quoted here.)

## Item 3 — The honest frontier: image-based profiling review (ANCHOR, primary-fetched)
- Source (fetched): Erik Serrano, John Peters, Jesko Wagner, Rebecca E. Graham, … (21
  authors) incl. **Anne E. Carpenter, Shantanu Singh, Juan C. Caicedo, Gregory P. Way**,
  "Progress and new challenges in image-based profiling," **arXiv:2508.05800**; v1 7 Aug
  2025, v2 14 Nov 2025; CC BY 4.0. (Review from the Broad Cell-Painting camp.)
- Verified facts / verbatim:
  - Scope: image-based profiling turns microscopy into "thousands of unbiased
    measurements that reveal phenotypic patterns"; "deep learning has fundamentally
    reshaped the field."
  - Advances named: single-cell analysis, "robust similarity metrics," and expansion
    into "optical pooled screening, temporal imaging, and 3D organoid profiling," plus
    "the growth of public benchmarks and open-source software ecosystems."
  - **Open challenges (verbatim):** the field "still faces substantial challenges,
    particularly in developing methods for emerging temporal and 3D data modalities,
    establishing robust quality control standards and workflows, and interpreting the
    processed features." A new Table 2 (v2) "compares the performance between classical
    vs. deep-learned features."

## Context / framing (named, not load-bearing)
- **Cell Painting's foundation-model moment / compositional direction:** "From
  modality-specific to compositional foundation models for cell biology," *Cell Systems*
  (2026), S2405-4712(26)00016-5 — argues most models assume the fixed 5-channel Cell
  Painting panel and stumble on other modalities, pushing toward **assay-agnostic,
  open, benchmarked, compositional** models. (Named for framing; cell.com blocks fetch.)
- **Scaling SSL:** masked-autoencoder ViTs scaled to ~1.9B params on ~16M Cell Painting
  images (Kenyon-Dean et al., "Phenom"/OpenPhenom line) show profiling quality improves
  with scale; **Cell-DINO** (PMC12826486) explores DINOv2 embeddings; a confounder-aware
  model on 13M+ images across 107k compounds reports SOTA MoA/target prediction on unseen
  compounds (per the Cell Systems review). Named for direction, not exact numbers.
- **JUMP-CP** remains the central pre-training/benchmarking substrate (six dyes, eight
  compartments, five channels, 20×); standardized retrieval benchmarks (mAP on JUMP-CP,
  gene–gene retrieval on RxRx3-core) are becoming the norm.

## Lab connections (for "why it matters")
- **The measurement layer of the virtual cell.** A [virtual cell](/project/human-cell-simulator/)
  must be judged against *what a real cell actually does* — and for imaging, that ground
  truth is a phenotypic fingerprint read from the picture. This is precisely the readout
  Aug 3 gestured at ("judge a molecule by what it does to a cell"). Morphological-profiling
  FMs are how you turn an image into that signal.
- **Home turf: HPA + KTH.** SubCell is trained on the **Human Protein Atlas** and comes
  out of **Emma Lundberg's lab (KTH)** — the same institution and imaging substrate the
  lab works with; the [Human Cell Simulator](/project/human-cell-simulator/) program uses
  HPA imaging as a data engine.
- **Share the model *and* the honest test.** CHAMMI-75 and the profiling review embody the
  open-benchmark culture the lab champions via the
  [BioImage Model Zoo](/project/bioimage-model-zoo/) and AI4Life — publish the model, the
  dataset, and the limitation together.
- **Segmentation → profiling pipeline.** Jul 19's segmentation is the first stage; these
  FMs are the second — the [Agent-Lens](/project/agent-lens/) / self-driving-microscope
  loop needs both to turn raw frames into decisions.

## De-dup check
- Recent digests: Aug 3 small-molecule drug design; Aug 2 virtual cell (interpretable);
  Aug 1 pathology; Jul 31 self-driving labs; Jul 30 RNA design; Jul 29 cryo-ET; Jul 28
  genomic-FM eval; Jul 27 strategy; Jul 26 spatial; Jul 25 antibody; Jul 24 open science;
  Jul 21 microscopy VLMs; Jul 19 segmentation. **Image-based / morphological profiling
  foundation models (phenotype-from-picture) has not been a theme** — it is the distinct
  measurement layer above segmentation and orthogonal to the omics/VLM/pathology angles.
  Clear to run.
