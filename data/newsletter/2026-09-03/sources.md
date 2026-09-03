# Newsletter sources — September 3, 2026

**Theme:** AI for **single-cell multi-omics integration** — fusing the different molecular
"layers" of the same cell (chromatin accessibility, RNA, surface protein) into one coherent
representation of cell state. Distinct problem from measuring any single modality: the AI job is
*stitching* modalities that live in different feature spaces, with different noise, sometimes not
even measured in the same cells. "The Cell in Every Language."

**Dedup guard:** Distinct from Aug 15 (single-cell FMs / *perturbation* prediction — one modality,
predicting response) and Aug 27 (RNA velocity / cell-state *dynamics* — one modality, over time).
Distinct from Aug 13 (spatial transcriptomics) and Sep 1 (multiplexed tissue *imaging* / spatial
proteomics) — those are *spatial* single-modality maps; today is *molecular-layer fusion* of
dissociated single cells. Distinct from Sep 2 (protein *function* prediction from sequence). Related
but not overlapping: the "virtual cell" horizon (Aug 15) — integration is a *building block* for it,
not the same story.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on monitor (min-likes 30,
since-hours 24). ~25th consecutive skip (>three weeks). search/discover also blocked by the same 402.
Grok replacement wired, awaiting xAI credits.

All 6 anchors verified against **raw Europe PMC `abstractText` JSON** (fetched directly, no
summarizer) AND cross-checked by two parallel general-purpose subagents against Crossref + Europe PMC
for DOI/title/author/journal/year/volume/pages. All metadata agrees across both sources. Only
abstract-verified verbatim quotes are used below.

---

## Framing — why fusion is its own problem

### Argelaguet review — the conceptual map — VERIFIED
- Argelaguet, R., Cuomo, A.S.E., Stegle, O. & Marioni, J.C. "Computational principles and challenges
  in single-cell data integration." *Nature Biotechnology* 39(10):1202–1215, 2021. DOI
  10.1038/s41587-021-00895-7. First author Ricard Argelaguet; senior John C. Marioni. Resolves
  (Crossref + Europe PMC agree; abstract from Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**The development of single-cell multimodal assays provides a
  powerful tool for investigating multiple dimensions of cellular heterogeneity, enabling new insights
  into development, tissue homeostasis and disease.**"; "**A key challenge in the analysis of
  single-cell multimodal data is to devise appropriate strategies for tying together data across
  different modalities.**"; "**Although existing integration strategies exploit similar mathematical
  ideas, they typically have distinct goals and rely on different principles and assumptions.**";
  "**Consequently, new definitions and concepts are needed to contextualize existing methods and to
  enable development of new methods.**"
- USE: the framing anchor — integration is not one task but a family; sets up why several methods
  below coexist.

## Section 1 — Paired modalities, fused per cell

### Seurat WNN — weighted-nearest-neighbor multimodal analysis — VERIFIED
- Hao, Y., … Satija, R. "Integrated analysis of multimodal single-cell data." *Cell*
  184(13):3573–3587.e29, 2021. DOI 10.1016/j.cell.2021.04.048. First author Yuhan Hao; senior Rahul
  Satija. Resolves (Crossref + Europe PMC agree; abstract from Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**The simultaneous measurement of multiple modalities represents an
  exciting frontier for single-cell genomics and necessitates computational methods that can define
  cellular states based on multimodal data.**"; "**Here, we introduce 'weighted-nearest neighbor'
  analysis, an unsupervised framework to learn the relative utility of each data type in each cell,
  enabling an integrative analysis of multiple modalities.**"; "**We apply our procedure to a CITE-seq
  dataset of 211,000 human peripheral blood mononuclear cells (PBMCs) with panels extending to 228
  antibodies to construct a multimodal reference atlas of the circulating immune system.**"; "**Our
  approach represents a broadly applicable strategy to analyze single-cell multimodal datasets and to
  look beyond the transcriptome toward a unified and multimodal definition of cellular identity.**"
- USE: the intuitive anchor — *learn how much each modality is worth, per cell*; 211k-cell CITE-seq
  reference; "beyond the transcriptome … unified and multimodal definition of cellular identity" is
  the thesis line.

### totalVI — probabilistic joint RNA + protein — VERIFIED
- Gayoso, A., … Yosef, N. "Joint probabilistic modeling of single-cell multi-omic data with
  totalVI." *Nature Methods* 18(3):272–282, 2021. DOI 10.1038/s41592-020-01050-x. First author Adam
  Gayoso; senior Nir Yosef. Resolves (Crossref + Europe PMC agree; abstract from Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**The paired measurement of RNA and surface proteins in single cells
  with cellular indexing of transcriptomes and epitopes by sequencing (CITE-seq) is a promising
  approach to connect transcriptional variation with cell phenotypes and functions.**"; "**However,
  combining these paired views into a unified representation of cell state is made challenging by the
  unique technical characteristics of each measurement.**"; "**Here we present Total Variational
  Inference (totalVI ...), a framework for end-to-end joint analysis of CITE-seq data that
  probabilistically represents the data as a composite of biological and technical factors, including
  protein background and batch effects.**"
- USE: the "unique technical characteristics" line names the core difficulty; totalVI models bio +
  technical jointly. Part of scvi-tools (open/callable).

## Section 2 — More layers, and missing ones

### MultiVI — deep generative RNA + chromatin, handles missing modalities — VERIFIED
- Ashuach, T., Gabitto, M.I., Koodli, R.V., Saldi, G.A., Jordan, M.I. & Yosef, N. "MultiVI: deep
  generative model for the integration of multimodal data." *Nature Methods* 20(8):1222–1231, 2023.
  DOI 10.1038/s41592-023-01909-9. First author Tal Ashuach; senior Nir Yosef. Resolves (Crossref +
  Europe PMC agree; abstract from Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**Jointly profiling the transcriptome, chromatin accessibility and
  other molecular properties of single cells offers a powerful way to study cellular diversity.**";
  "**Here we present MultiVI, a probabilistic model to analyze such multiomic data and leverage it to
  enhance single-modality datasets.**"; "**MultiVI creates a joint representation that allows an
  analysis of all modalities included in the multiomic input data, even for cells for which one or
  more modalities are missing.**"
- USE: extends the joint-model idea to RNA+ATAC and, crucially, *imputes missing modalities* — you can
  fold single-modality data into a shared space. Also scvi-tools.

## Section 3 — Across datasets, without pairing

### GLUE — graph-linked unified embedding, unpaired multi-omics + regulatory inference — VERIFIED
- Cao, Z.-J. & Gao, G. "Multi-omics single-cell data integration and regulatory inference with
  graph-linked embedding." *Nature Biotechnology* 40(10):1458–1466, 2022. DOI
  10.1038/s41587-022-01284-4. First author Zhi-Jie Cao; senior Ge Gao. Resolves (Crossref + Europe
  PMC agree; open access CC BY, PMC9546775).
- ABSTRACT-VERIFIED (verbatim): "**Despite the emergence of experimental methods for simultaneous
  measurement of multiple omics modalities in single cells, most single-cell datasets include only one
  modality.**"; "**A major obstacle in integrating omics data from multiple modalities is that
  different omics layers typically have distinct feature spaces.**"; "**Here, we propose a
  computational framework called GLUE (graph-linked unified embedding), which bridges the gap by
  modeling regulatory interactions across omics layers explicitly.**"; "**Systematic benchmarking
  demonstrated that GLUE is more accurate, robust and scalable than state-of-the-art tools for
  heterogeneous single-cell multi-omics data.**"; "**We applied GLUE to various challenging tasks,
  including triple-omics integration, integrative regulatory inference and multi-omics human cell atlas
  construction over millions of cells, where GLUE was able to correct previous annotations.**"
- USE: the "most datasets include only one modality" + "distinct feature spaces" lines motivate
  unpaired integration; GLUE uses prior regulatory graph to link layers; atlas-scale, corrected
  annotations. Open on GitHub.

## Section 4 — The honest frontier: which integration actually works?

### scIB benchmark — Luecken & Theis — VERIFIED
- Luecken, M.D., … Theis, F.J. "Benchmarking atlas-level data integration in single-cell genomics."
  *Nature Methods* 19(1):41–50, 2022. DOI 10.1038/s41592-021-01336-8. First author Malte D. Luecken;
  senior Fabian J. Theis. Resolves (Crossref + Europe PMC agree; Crossref also carried the full
  abstract, matching Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**Single-cell atlases often include samples that span locations,
  laboratories and conditions, leading to complex, nested batch effects in data.**"; "**To guide
  integration method choice, we benchmarked 68 method and preprocessing combinations on 85 batches of
  gene expression, chromatin accessibility and simulation data from 23 publications, altogether
  representing >1.2 million cells distributed in 13 atlas-level integration tasks.**"; "**We evaluated
  methods according to scalability, usability and their ability to remove batch effects while retaining
  biological variation using 14 evaluation metrics.**"; "**Overall, scANVI, Scanorama, scVI and scGen
  perform well, particularly on complex integration tasks, while single-cell ATAC-sequencing
  integration performance is strongly affected by choice of feature space.**"
- USE: the prove-it anchor — the central tension (remove batch effects WHILE retaining biological
  variation), 68×85×>1.2M scale, 14 metrics. Same discipline as CAFA (Sep 2), the Ma benchmark
  (Sep 1), CryoBench (Aug 31).

## Section 5 — Lab hook + horizon
- A cell's state is written across ALL its layers — chromatin (what it *can* read), RNA (what it *is*
  reading), protein (what's *doing the work*). Integration builds the multi-layer definition of a cell
  a virtual cell / Human Cell Simulator (/project/human-cell-simulator/, /post/newsletter-2026-08-15/)
  actually needs — not just the transcriptome.
- imaging×omics: spatial modalities are *more layers to fuse* — the RNA map (/post/newsletter-2026-08-13/)
  and the protein map (/post/newsletter-2026-09-01/) are exactly the kind of data these frameworks are
  starting to stitch together. Multi-omics integration is the molecular counterpart of the lab's core.
- Open, callable, benchmarked: totalVI/MultiVI ship in scvi-tools; GLUE is open on GitHub; scIB is the
  public yardstick — the same ethos as serving models via BioImage Model Zoo
  (/project/bioimage-model-zoo/) + BioEngine (/project/bioengine/), and the recurring prove-it standard
  (/post/newsletter-2026-07-27/).
