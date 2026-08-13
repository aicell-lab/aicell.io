# Newsletter sources — 2026-08-13 (fetched UTC 2026-08-13T03:00:16Z)

Theme: **The cell's neighborhood — reading gene expression *in place*, in intact
tissue, and the AI it takes to make sense of the map.** Single-cell RNA-seq
dissociates tissue into a suspension and throws away every cell's address.
**Imaging-based spatial transcriptomics** (MERFISH, seqFISH, in-situ sequencing,
Xenium/CosMx) keeps each transcript pinned to its location at **subcellular
resolution** — but it turns biology into a hard *imaging* problem: you must
**segment** each cell and **assign every mRNA to the right one** (Baysor, Cellpose),
then learn what the arrangement *means* — the niche, the neighborhood — with spatial
**foundation models** like **Nicheformer**. A horizon story squarely at the lab's
imaging×omics intersection: segmentation is a [bioimage](/project/bioimage-model-zoo/)
problem; spatial context is what a [virtual cell](/project/human-cell-simulator/)
is missing; and the microscope that captures it is exactly our
[self-driving](/project/self-driving-microscope/) territory.

## Provenance / method
- Web research (WebSearch + WebFetch). Two grounded anchors:
  - **Nicheformer** — peer-reviewed in ***Nature Methods* 2025** (DOI 10.1038/s41592-025-02814-z,
    PMID 41168487; Nat Methods 22:2525–2538; Theis lab). Verified title, venue, authors,
    the SpatialCorpus-110M composition, the MLM architecture, and the headline finding
    (dissociated-only models fail to recover spatial microenvironments) from the paper /
    bioRxiv / repo pages.
  - **Cell segmentation in imaging-based spatial transcriptomics (Baysor)** — ***Nature
    Biotechnology*** (DOI 10.1038/s41587-021-01044-w). Verified the problem statement
    (mis-segmentation → mRNA misassignment → downstream errors) and Baysor's approach
    (joint likelihood of transcriptional composition + morphology; RNA-only or image-prior
    mode; paired with Cellpose nuclei).
  - **MERFISH** cited as the established imaging-based method ("thousands of RNA species in
    single cells" via combinatorial error-robust barcodes over multiple imaging rounds) —
    Chen/Zhuang et al., *Science* 2015; described at the level supported by sources, no
    invented numbers.
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  returns **HTTP 402 Insufficient credits** (getxapi out of credits ~6 weeks). The Grok
  `x_search` replacement is wired but the xAI team has **no credits yet** (403). Flagged to Wei.
- **De-dup / variety (important):** *spatial transcriptomics / spatial omics + the imaging AI
  to resolve it* has **not** been a digest theme. Distinct from the recent run:
  - **Aug 10 "One Cell, Two Answers" (optical pooled screening)** = imaging × **CRISPR
    perturbation** + in-situ *barcode* sequencing to demultiplex a screen. Today = imaging of
    **endogenous** transcripts in **native, unperturbed tissue** to map cell state *in place*.
    Both are "imaging × RNA in situ," but different purpose (functional screen vs tissue atlas),
    different molecule read (guide barcodes vs native mRNA), different axis (perturbation→
    phenotype vs spatial context). Explicitly distinguished, not repeated.
  - **Aug 9 genome FMs / Aug 11 protein dynamics / Aug 12 co-folding** = DNA sequence / single
    protein motion / molecular complexes. Today jumps up two scales to **tissue** and **spatial
    neighborhood**.
  - **Aug 2 "virtual cell"** = validating a cell model. Today supplies the **spatial/tissue
    context** such a model currently lacks (a cell's behaviour depends on its neighbours).
  - **Aug 6 virtual staining** = image→image (predict a stain). Today's imaging problem is
    **segmentation + transcript assignment** (image+RNA→cell identity), a different task.
  Clear separation. Clear to run.
- **Verification discipline:** Nicheformer is **peer-reviewed** (*Nature Methods* 2025).
  Baysor is **peer-reviewed** (*Nature Biotechnology*). MERFISH is a long-established method.
  Supporting tools (Cellpose, Bering/GNN, JSTA, IS3G) cited only as landscape and labelled.
  No fabricated cell counts or benchmark numbers beyond what the sources state.

## Item 1 — Keep the address: imaging-based spatial transcriptomics + the segmentation problem
- **Why it's new:** scRNA-seq gives deep, whole-transcriptome profiles but **dissociates**
  the tissue — every cell loses *where it was* and *who it was next to*. Imaging-based spatial
  transcriptomics keeps the map: **MERFISH** "identifies thousands of RNA species in single
  cells using combinatorial, error-robust fluorescence barcodes read out over multiple imaging
  rounds," placing "individual RNA transcripts on a map of the cell at **subcellular
  resolution**" — something bulk and even single-cell sequencing cannot do. (Companion methods:
  seqFISH, in-situ sequencing, and commercial platforms Xenium / CosMx.)
- **The catch is an imaging-AI problem:** "inaccurate cell segmentation procedures lead to
  **misassignment of mRNAs to individual cells**, which can introduce errors in downstream
  analysis." Reading the map correctly means **segmenting each cell** and **assigning each
  transcript** to the right one — a microscopy segmentation problem, not a sequencing one.
- **Baysor** (*Nature Biotechnology*, DOI 10.1038/s41587-021-01044-w) is a leading answer:
  it "optimizes 2D or 3D cell boundaries considering the **joint likelihood of transcriptional
  composition and cell morphology**," operating either from **RNA alone** or with **image-based
  priors** (e.g. nuclei segmented by **Cellpose**, a membrane stain as prior, transcripts
  assigned in a Bayesian framework). Reported to yield "better segmentation accuracy, increased
  number of cells detected, and improved molecular resolution" — recovering cells (e.g.
  endothelial cells, astrocytes) that boundary-only methods miss. Newer GNN methods (**Bering**)
  and graph-partitioning (**IS3G**) push the same frontier.

## Item 2 — Make sense of the map: spatial foundation models (Nicheformer, ANCHOR)
- **Source:** Anna C. Schaar, Alejandro Tejada-Lapuerta, ... **Fabian J. Theis** et al.,
  "**Nicheformer: a foundation model for single-cell and spatial omics**," ***Nature Methods*
  22:2525–2538 (2025)**, DOI 10.1038/s41592-025-02814-z (PMID 41168487; bioRxiv 2024.04.15.589472).
- Verified facts:
  - **What it is:** a **transformer** foundation model that **generalizes single-cell FM
    approaches to the spatial setting**, learning a **cell representation that captures spatial
    context** (niche, neighbourhood) — trained with a **masked-language-modeling** objective,
    encoding cell type / assay / modality covariates, with cross-species (human+mouse ortholog)
    embeddings.
  - **Data — SpatialCorpus-110M:** pretrained on **>110 million cells** across **73 organs/
    tissues** from human and mouse, including **~53.8 million cells measured with image-based
    spatial technologies** (plus ~57 million dissociated) — a corpus that pairs dissociated and
    spatially-resolved data.
  - **Downstream tasks:** spatial **cell-type / niche / region** label prediction, **neighborhood
    cell density** and **composition** prediction — excelling in linear-probing and fine-tuning,
    especially spatial composition/label prediction.
  - **Headline finding:** "**models trained only on dissociated data fail to recover the
    complexity of spatial microenvironments**," underscoring the need for multiscale integration;
    Nicheformer can **transfer spatial context to plain scRNA-seq** (predict the spatial context
    of dissociated cells).
  - **Open:** code + pretraining weights openly available (Hugging Face **theislab/Nicheformer**,
    GitHub, Mendeley Data).

## Item 3 — Why it matters for the lab + the honest frontier
- **Segmentation is a bioimage problem — our home turf.** The bottleneck in spatial
  transcriptomics isn't sequencing; it's **segmenting cells in an image** and assigning
  molecules to them. That is exactly the [BioImage Model Zoo](/project/bioimage-model-zoo/) /
  Cellpose / SAM-segmentation world — the kind of cell-segmentation work the lab does (incl.
  concept-aware segmentation) — now load-bearing for omics.
- **Spatial context is what a virtual cell is missing.** A [Human Cell
  Simulator](/project/human-cell-simulator/) that treats cells as independent samples misses the
  central spatial truth Nicheformer quantifies: **a cell's state depends on its neighbours**.
  If [Aug 12](/post/newsletter-2026-08-12/) added molecular *interactions* and
  [Aug 11](/post/newsletter-2026-08-11/) added *motion*, this adds **tissue context and niche** —
  the level at which disease actually unfolds.
- **It's a microscopy acquisition.** Imaging-based spatial transcriptomics is multi-round
  imaging of a sample — precisely what a [self-driving microscope](/project/self-driving-microscope/) /
  [Agent-Lens](/project/agent-lens/) / [REEF farm](/project/reef-imaging-farm/) automate, and the
  complement to [Aug 10's](/post/newsletter-2026-08-10/) in-situ readout.
- **Open, runnable models.** Nicheformer ships weights; segmentation models are open — the
  [BioEngine](/project/bioengine/) ethos, now spanning the imaging *and* omics halves of a spatial
  pipeline.
- **The honest frontier (prove-it).** Spatial is powerful but partial: imaging-based panels are
  **targeted** (hundreds–thousands of genes, not the whole transcriptome); **segmentation errors
  propagate** into every downstream call (garbage assignment → garbage cell types); and a
  foundation model's predicted spatial context is a **hypothesis** to validate, not a
  measurement. Same [prove-it discipline](/post/newsletter-2026-07-27/): a map is only as good as
  the boundaries you draw on it.

## Lab connections (for "why it matters")
- **bioimage-model-zoo / segmentation** — transcript assignment hinges on cell segmentation (Cellpose/SAM); the lab's home turf.
- **human-cell-simulator** — spatial context / niche is the missing tissue-scale layer under a virtual cell.
- **self-driving-microscope / agent-lens / reef-imaging-farm** — imaging-based spatial is an automated microscopy acquisition.
- **Aug 10 optical pooled screening** — complementary in-situ imaging×RNA (perturbation screen vs native tissue map).
- **bioengine** — open, runnable models across the imaging+omics pipeline.
- **prove-it (Jul 27)** — segmentation errors propagate; predicted context is a hypothesis; targeted panels ≠ whole transcriptome.

## De-dup check
- Recent digests: Aug 12 co-folding/affinity; Aug 11 protein dynamics; Aug 10 optical pooled
  screening; Aug 9 genome FMs; Aug 8 smart microscopy; Aug 7 proteomics; Aug 6 virtual staining;
  Aug 5 federated; Aug 4 profiling; Aug 3 small-molecule design; Aug 2 virtual cell; Aug 1
  prove-it. **Spatial transcriptomics / spatial omics + the imaging AI to resolve it has not been
  a digest theme.** Distinct scale (tissue/neighbourhood), distinct task (segmentation + spatial
  context), explicitly separated from Aug 10's perturbation screen. Clear to run.
