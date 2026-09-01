# Newsletter sources — September 1, 2026

**Theme:** AI for **multiplexed tissue imaging / spatial single-cell proteomics** — measuring
dozens of *proteins* in situ (CODEX/IMC-style) so a tissue slice becomes a ~40-channel image,
then using deep learning to (a) segment every cell at tissue scale, (b) assign each cell a
type/state from its protein profile, and (c) read spatial neighborhoods. "The Tissue, in Forty
Colors." The **protein counterpart** to Aug 13 (/post/newsletter-2026-08-13/, "The Cell's
Neighborhood" — imaging-based spatial *transcriptomics*, RNA transcripts + Baysor + Nicheformer):
same spatial-single-cell goal, complementary molecular readout (antibodies/proteins vs RNA).

**Dedup guard:** Distinct from Aug 13 (RNA transcripts, transcript-to-cell assignment) and from
Aug 16 (/post/newsletter-2026-08-16/, "Segment Anything, Cell" — general segmentation FMs) — here
segmentation is one step inside the protein-phenotyping pipeline, and the story centers on
multiplexed *protein* readouts + cross-panel cell-type annotation + the generalization frontier.
Distinct from Aug 4 (image-based morphological profiling of cultured cells). Horizon /
strategy-radar: spatial biology at single-cell resolution = the tissue-context substrate a virtual
cell needs; imaging×omics is the lab's core intersection.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on monitor; ~23rd
consecutive skip (>three weeks). Grok replacement wired, awaiting xAI credits.

All anchors verified by two parallel general-purpose subagents against Crossref + Europe PMC
(core `abstractText`), with VERBATIM abstract quotes. Only abstract-verified quotes are used.

---

## Section 1 — The modality: dozens of proteins, in place

### CODEX — highly multiplexed antibody imaging — VERIFIED
- Goltsev, Y., Samusik, N., Kennedy-Darling, J., Bhate, S., Hale, M., Vazquez, G., Black, S. &
  Nolan, G.P. "Deep Profiling of Mouse Splenic Architecture with CODEX Multiplexed Imaging."
  *Cell* **174**(4):968–981.e15, 2018. DOI 10.1016/j.cell.2018.07.010. Senior author Garry P.
  Nolan (Stanford). DOI resolves (Crossref + Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**A highly multiplexed cytometric imaging approach, termed
  co-detection by indexing (CODEX), is used here to create multiplexed datasets of normal and
  lupus (MRL/lpr) murine spleens**"; "**CODEX iteratively visualizes antibody binding events using
  DNA barcodes, fluorescent dNTP analogs, and an in situ polymerization-based indexing
  procedure**"; "**An algorithmic pipeline for single-cell antigen quantification in tightly
  packed tissues was developed and used to overlay well-known morphological features with de novo
  characterization of lymphoid tissue architecture at a single-cell and cellular neighborhood
  levels.**"

## Section 2 — Find every cell: segmentation at tissue scale

### Mesmer / TissueNet — human-level whole-cell segmentation — VERIFIED
- Greenwald, N.F., Miller, G., Moen, E., … Angelo, M. & Van Valen, D. "Whole-cell segmentation of
  tissue images with human-level performance using large-scale data annotation and deep learning."
  *Nature Biotechnology* **40**(4):555–565, 2022 (online 18 Nov 2021). DOI
  10.1038/s41587-021-01094-0. First author Noah F. Greenwald; senior David Van Valen (Caltech).
  DOI resolves (Crossref + Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**cell segmentation—the task of identifying the precise boundary
  of every cell in an image**"; "**we constructed TissueNet, a dataset for training segmentation
  models that contains more than 1 million manually labeled cells, an order of magnitude more than
  all previously published segmentation training datasets**"; "**We used TissueNet to train
  Mesmer, a deep-learning-enabled segmentation algorithm**"; "**We then adapted Mesmer to harness
  cell lineage information in highly multiplexed datasets and used this enhanced version to
  quantify cell morphology changes during human gestation.**"
- CAUTION: "whole-cell segmentation" is the TITLE phrase; the abstract body says "cell
  segmentation" / "highly multiplexed datasets." Quote accordingly.

## Section 3 — Name every cell: annotation from the protein profile

### STELLAR — geometric deep learning for cell-type annotation — VERIFIED
- Brbić, M., Cao, K., Hickey, J.W., Tan, Y., Snyder, M.P., Nolan, G.P. & Leskovec, J. "Annotation
  of spatially resolved single-cell data with STELLAR." *Nature Methods* **19**:1411–1418, 2022
  (published 24 Oct 2022). DOI 10.1038/s41592-022-01651-8. First author Maria Brbić; senior Jure
  Leskovec (Stanford). DOI resolves (Crossref + Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**Here we present STELLAR, a geometric deep learning method for
  cell-type discovery and identification in spatially resolved single-cell datasets**"; "**current
  computational methods for annotating spatially resolved single-cell data are typically based on
  techniques established for dissociated single-cell technologies**"; "**STELLAR automatically
  assigns cells to cell types present in the annotated reference dataset and discovers novel cell
  types and cell states**"; "**We successfully applied STELLAR to CODEX multiplexed fluorescent
  microscopy data and multiplexed RNA imaging datasets.**"
- CAUTION: abstract says "geometric deep learning" — STELLAR *is* a graph neural network, but that
  term is not in the abstract; if we say GNN, phrase as our description, not a quote.

## Section 4 — The honest frontier: generalization

### Multimodality Cell Segmentation Challenge — methods don't generalize without tuning — VERIFIED
- Ma, J., Xie, R., Ayyadhury, S., … Wang, B. "The multimodality cell segmentation challenge:
  toward universal solutions." *Nature Methods*, 2024 (published 26 Mar 2024). DOI
  10.1038/s41592-024-02233-6. First author Jun Ma; senior Bo Wang (Toronto/Vector). DOI resolves
  (Crossref).
- ABSTRACT-VERIFIED (verbatim): "**Existing cell segmentation methods are often tailored to
  specific modalities or require manual interventions to specify hyper-parameters in different
  experimental settings**"; "**Here, we present a multimodality cell segmentation benchmark,
  comprising more than 1,500 labeled images derived from more than 50 diverse biological
  experiments**"; verbatim fragment: "**can also be applied to diverse microscopy images across
  imaging platforms and tissue types without manual parameter adjustments.**"
- FIT NOTE: this is a *general* multimodality segmentation challenge (includes tissue/multiplexed
  data), used as the "generalization gap / prove-it" anchor — do NOT claim it is multiplexed-only.
- (Not used, but verified-adjacent phenotyping methods if ever needed: CellSighter, *Nat Commun*
  2023, DOI 10.1038/s41467-023-40066-7; Pixie, *Nat Commun* 2023, DOI 10.1038/s41467-023-40068-5.
  Abstracts NOT verbatim-verified here — do not quote without checking.)

## Section 5 — Lab hook + horizon
- Imaging×omics is the lab's core intersection; this is the *protein* readout of the same spatial
  single-cell goal as Aug 13's RNA story — a virtual cell will want both, cross-checked.
- Callable, benchmarked models: segmentation FMs (Aug 16, /post/newsletter-2026-08-16/) →
  BioImage Model Zoo (/project/bioimage-model-zoo/) + BioEngine (/project/bioengine/); the
  prove-it discipline (/post/newsletter-2026-07-27/) is exactly what the Ma et al. benchmark
  enforces (generalization across platforms/tissues, no hand-tuning).
- Substrate: the Human Protein Atlas (Lundberg group, KTH neighbor) is the spatial-proteome map;
  single-cell spatial maps of tissue = the context layer the Human Cell Simulator
  (/project/human-cell-simulator/) and virtual-cell horizon (/post/newsletter-2026-08-15/) need.
- Acquisition could be driven by smart/agentic microscopy (Agent-Lens /project/agent-lens/,
  self-driving microscope /project/self-driving-microscope/).
