# Newsletter sources — 2026-08-16 (fetched UTC 2026-08-16T03:03:44Z)

Theme: **"Segment anything" comes to the cell — general-purpose *foundation
models for microscopy image segmentation*.** Segmentation ("who is this cell, and
where are its edges?") is the unglamorous first step of nearly every image-analysis
pipeline, and for a decade every new assay meant retraining a bespoke segmenter. The
"Segment Anything" moment brought a *promptable* vision foundation model; 2025 adapted
it to the messy reality of microscopy. Two works anchor the story: **Cellpose-SAM**
(a bioRxiv **preprint** claiming "superhuman generalization") and **Segment Anything
for Microscopy / μSAM** (*Nature Methods* 2025 — one open tool for interactive +
automatic segmentation across 2D/3D/tracking, light **and** electron microscopy, with
its models **published on BioImage.IO**). This is the lab's home turf — the
[BioImage Model Zoo](/project/bioimage-model-zoo/) / Cellpose / SAM problem — and the
load-bearing first step under [spatial omics](/post/newsletter-2026-08-13/) and a
[virtual cell](/project/human-cell-simulator/).

## Provenance / method
- Web research (WebSearch + WebFetch), cross-checked against Crossref, Semantic
  Scholar, PMC open-access full text, and bioRxiv. Anchors:
  - **Cellpose-SAM** — Marius Pachitariu, Michael Rariden & Carsen Stringer,
    "**Cellpose-SAM: superhuman generalization for cellular segmentation**,"
    **bioRxiv 2025.04.28.651001**, DOI 10.1101/2025.04.28.651001 (posted 1 May 2025;
    CC-BY-NC). **Preprint — not peer-reviewed** as of this writing. Labelled throughout.
    (Byline corrected: Pachitariu is first author; Rariden is a third author — *not*
    "Stringer & Pachitariu.")
  - **Segment Anything for Microscopy (μSAM)** — Anwai Archit, Luca Freckmann, …,
    Constantin Pape (Computational Cell Analytics, University of Göttingen),
    "**Segment Anything for Microscopy**," ***Nature Methods* 22(3):579–591, 2025**,
    DOI 10.1038/s41592-024-02580-4 (online 12 Feb 2025; PMID 39939717; PMCID
    PMC11903314). **Peer-reviewed.** (Earlier bioRxiv preprint 2023.08.21.554208,
    Aug 2023. An Author Correction, DOI 10.1038/s41592-025-02745-9, June 2025, added
    five authors + an affiliation.)
  - **Cellpose** (background, peer-reviewed) — Stringer, Wang, Michaelos & Pachitariu,
    "**Cellpose: a generalist algorithm for cellular segmentation**," *Nature Methods*
    18(1):100–106, 2021, DOI 10.1038/s41592-020-01018-x (PMID 33318659). Follow-up
    "**Cellpose 2.0: how to train your own model**," *Nature Methods* 19:1634–1641, 2022,
    DOI 10.1038/s41592-022-01663-4 (human-in-the-loop).
  - **Segment Anything (SAM)** (background, the vision foundation model) — Kirillov,
    Mintun, Ravi et al. (Meta AI / FAIR), "**Segment Anything**," ICCV 2023,
    arXiv:2304.02643 (posted 5 Apr 2023). Trained on **SA-1B** — "over 1 billion masks
    on 11M licensed and privacy-respecting images"; promptable, zero-shot transfer.
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  returns **HTTP 402 Insufficient credits** (getxapi out of credits ~7 weeks; 7th
  straight skipped sweep). The Grok `x_search` replacement is wired but the xAI team has
  **no credits yet** (403). Flagged to Wei.

## Verification discipline
- **Cellpose-SAM is a preprint** — labelled as such; no specific benchmark numbers are
  quoted (the abstract is qualitative — "substantially outperforms inter-human agreement
  and approaches the human-consensus bound" — and full-text metrics were paywalled). The
  headline "superhuman generalization" is quoted from the paper's own title and framed as
  the authors' claim, not a settled fact.
- **μSAM is peer-reviewed** (*Nature Methods*). Quotes verified against the PMC full text.
- No fabricated metrics. The one benchmark fragment quoted ("Automatic segmentation via
  AIS performs on par or better than CellPose except for TissueNet") is from the μSAM paper.

## De-dup / variety (important)
General-purpose **segmentation foundation models** (the segmentation *model itself* as the
object of study — "segment anything" adapted to microscopy) has **not** been a dedicated
digest theme. Distinct from the recent run:
- **Aug 13 spatial transcriptomics** — segmentation appeared only as a *sub-point*
  (Baysor for transcript assignment; Cellpose as a nuclei prior). Today the segmentation
  *foundation model* is the whole subject: generalist, promptable, cross-modality. Today is
  explicitly the load-bearing first step *under* that spatial pipeline (linked, not repeated).
- **Aug 6 virtual staining** = predict fluorescence from label-free images (a *translation*
  task). **Aug 8 smart microscopy** = *acquisition* / where to look. Today = *segmentation*
  (draw the boundaries) — a different stage of the pipeline.
- **Aug 4 morphological profiling** = *downstream* features (Cell Painting) computed after
  segmentation. Today is the segmentation step that profiling depends on.
- **Aug 15 single-cell FMs / Aug 9 genome FMs** = *sequence/omics* foundation models. Today
  = an *image* foundation model. Different data, different task.
Clear separation. Clear to run.

## Item 1 — The generalist arrives: SAM comes to the cell
- **The old pain:** cell segmentation is the first step of almost every microscopy pipeline,
  and historically each new imaging condition (modality, magnification, stain, organism)
  demanded a **retrained, bespoke** model. **Cellpose** (Stringer et al., *Nature Methods*
  18:100–106, 2021) already pushed against this — a **generalist** trained on "a new dataset
  of highly varied images of cells, containing over 70,000 segmented objects" that "does not
  require model retraining or parameter adjustments," predicting spatial **flow/gradient
  fields** to recover masks. **Cellpose 2.0** (2022) added human-in-the-loop custom training.
- **The vision-FM shift:** **Segment Anything (SAM)** (Kirillov et al., Meta AI, ICCV 2023,
  arXiv:2304.02643) reframed segmentation as a **promptable foundation-model** problem —
  trained on **SA-1B** ("over 1 billion masks on 11M … images"), able to "transfer zero-shot
  to new image distributions and tasks." But out of the box SAM struggles on the dense,
  low-contrast, crowded reality of microscopy.
- **Cellpose-SAM** (Pachitariu, Rariden & Stringer, **bioRxiv preprint** 2025.04.28.651001,
  May 2025) closes that gap: it "**adapted the pretrained transformer backbone of a
  foundation model (SAM) to the Cellpose framework**." The authors' headline claim is
  **"superhuman generalization for cellular segmentation"** — that modern segmenters already
  "match inter-human agreement," but a human-*consensus* segmentation "could reduce error
  rates in half," and Cellpose-SAM "**substantially outperforms inter-human agreement and
  approaches the human-consensus bound**." They add robustness to **channel shuffling, cell
  size, shot noise, downsampling, and isotropic/anisotropic blur**, arguing these properties
  "establish Cellpose-SAM as a foundation model for biological segmentation."
  **[Preprint — no specific benchmark numbers quoted; claims are the authors'.]**

## Item 2 — One tool, every modality: Segment Anything for Microscopy (μSAM)
- **Source:** Archit, Freckmann, …, Pape, "**Segment Anything for Microscopy**,"
  ***Nature Methods* 22(3):579–591, 2025** (peer-reviewed; Göttingen). Tool = **micro_sam /
  μSAM**, open source (github.com/computational-cell-analytics/micro-sam).
- **What it is:** it "**extend[s] [SAM] by fine-tuning generalist models for light and
  electron microscopy that clearly improve segmentation quality for a wide range of imaging
  conditions**." One model family spanning **both** major microscopy modalities.
- **What it does (the practical part):** it "**implement[s] interactive and automatic
  segmentation in a napari plugin … a unified solution for microscopy annotation across
  different microscopy modalities**," and "**supports two-dimensional (2D) and volumetric
  segmentation as well as tracking in the same tool**." Interactive = prompt a cell and it
  fills the mask; automatic = segment the whole field; plus 3D volumes and time-lapse tracking.
- **Benchmark (verified fragment):** "**Automatic segmentation via AIS performs on par or
  better than CellPose except for TissueNet**"; StarDist / TrackMate appear as baselines.
  (No aggregate training-set-scale number was verifiable from accessible text — not quoted.)
- **Lab tie made explicit by the authors:** they "**published our models on BioImage.IO to
  offer them in a standard format**" — i.e., into the very [BioImage Model Zoo](/project/bioimage-model-zoo/)
  ecosystem the lab helps build, and shipped as a **napari** plugin. Open weights, open tool,
  standard format.

## Item 3 — Why it matters for the lab + the honest frontier
- **This is the lab's home turf.** General cell/microscopy segmentation is the exact
  [BioImage Model Zoo](/project/bioimage-model-zoo/) / Cellpose / SAM problem the lab works
  on — μSAM literally ships its weights *into* that zoo, and open, runnable, standard-format
  models are the [BioEngine](/project/bioengine/) / [ImJoy](/project/imjoy/) ethos exactly.
  A promptable segmenter is also the perfect tool for an [agent](/post/newsletter-2026-08-14/)
  to *call*: point [Agent-Lens](/project/agent-lens/) or a
  [self-driving microscope](/project/self-driving-microscope/) at a field and let it segment
  what it sees, in the loop.
- **It's load-bearing under everything downstream.** As [Aug 13](/post/newsletter-2026-08-13/)
  showed, in spatial transcriptomics "transcript assignment *is* cell segmentation" — a
  misdrawn boundary sends a molecule to the wrong cell and corrupts every downstream cell
  type. Morphological profiling ([Aug 4](/post/newsletter-2026-08-04/)) measures features of
  segmented cells. A [virtual cell](/project/human-cell-simulator/) that learns from images
  inherits whatever the segmenter drew. Get this first step right and everything above it
  gets more trustworthy; get it wrong and the error propagates silently.
- **The honest frontier (prove-it).** "Superhuman generalization" is a striking claim — and
  a **benchmark** claim: it holds against the datasets and metrics tested, and Cellpose-SAM
  is still a **preprint**. Generalization is exactly the property that must be re-checked on
  *your own* microscope, *your own* stain, *your own* organism — the distribution the model
  never saw. A promptable model can also make a confident, clean-looking boundary that is
  simply wrong; a mask is a **hypothesis about where the cell ends**, not a measurement. That
  is the same [prove-it discipline](/post/newsletter-2026-07-27/) we keep returning to:
  validate on held-out, real data before you trust the line. The generalist segmenter is a
  genuine leap — for the first time one open tool can plausibly segment *most* of what a lab
  images — and it earns that trust one validated dataset at a time.

## Lab connections (for "why it matters")
- **bioimage-model-zoo** — μSAM publishes its models on BioImage.IO; general segmentation is the zoo's core problem.
- **bioengine / imjoy** — open, runnable, standard-format models an agent or browser can call.
- **agent-lens / self-driving-microscope** — a promptable segmenter is the tool a reasoning agent calls in the acquisition loop.
- **Aug 13 spatial** — segmentation is the load-bearing first step under spatial omics (transcript assignment = segmentation).
- **Aug 4 profiling / human-cell-simulator** — everything downstream inherits the boundaries the segmenter drew.
- **prove-it (Jul 27)** — "superhuman" is a benchmark claim; a mask is a hypothesis; validate generalization on your own data.

## De-dup check
- Recent digests: Aug 15 single-cell FMs / perturbation; Aug 14 AI co-scientist; Aug 13
  spatial transcriptomics; Aug 12 co-folding/affinity; Aug 11 protein dynamics; Aug 10
  optical pooled screening; Aug 9 genome FMs; Aug 8 smart microscopy; Aug 7 proteomics; Aug 6
  virtual staining; Aug 5 federated; Aug 4 profiling; Aug 3 small-molecule design; Aug 2
  virtual cell; Aug 1 prove-it/pathology. **General-purpose segmentation foundation models
  (the segmentation model itself — "segment anything" for microscopy) has not been a digest
  theme.** Segmentation appeared only as a sub-point on Aug 13; today it is the whole subject,
  a different stage from virtual staining (Aug 6) and acquisition (Aug 8), and an image FM
  (vs the sequence/omics FMs of Aug 9/15). Clear to run.
