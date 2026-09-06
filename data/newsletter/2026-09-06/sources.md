# Newsletter sources — September 6, 2026

**Theme:** **Gene regulatory network (GRN) inference** — reconstructing the cell's *wiring diagram* (which
transcription factors regulate which genes) from expression / multi-omic data, and using it to *simulate*
perturbations in silico. "The Wiring Diagram of a Cell." The arc: tree-based inference from bulk data
(GENIE3) → community benchmark & wisdom-of-crowds (DREAM5) → single-cell GRNs (SCENIC) → a rigorous
single-cell benchmark (BEELINE) → GRNs that let you *perturb a cell in silico* (CellOracle) → multiomic,
enhancer-driven GRNs (SCENIC+).

**Dedup guard:** Distinct from Aug 27 (RNA velocity / cell-state *dynamics* — where a cell is going, not
its regulatory wiring), Aug 19 (regulatory *genomics* / variant-effect prediction — sequence→activity,
not network reconstruction), Sep 3 (multi-omics *integration* — fusing layers, not inferring causal TF→
gene edges), Aug 15 (single-cell FMs / perturbation prediction via learned embeddings — here it's
*mechanistic* network-based in silico perturbation). This is the *causal structure* layer: who regulates
whom, and what happens if you knock a TF out.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on monitor (min-likes 30,
since-hours 24) and search. ~29th consecutive skip (>four weeks). Grok replacement wired, awaiting xAI
credits.

All 6 anchors verified against **raw Europe PMC `abstractText` JSON** (fetched directly via curl — no
summarizer), with DOI/title/author/journal/year confirmed. Only abstract-verified verbatim quotes used.

---

## Framing + foundational method

### GENIE3 (Huynh-Thu et al.) — tree-based GRN inference — VERIFIED
- Huynh-Thu VA, Irrthum A, Wehenkel L, Geurts P. "Inferring regulatory networks from expression data
  using tree-based methods." *PLoS ONE* 5(9):e12776, 2010. DOI 10.1371/journal.pone.0012776.
- ABSTRACT-VERIFIED (verbatim): "**One of the pressing open problems of computational systems biology is
  the elucidation of the topology of genetic regulatory networks (GRNs) using high throughput genomic
  data.**"; "**we present GENIE3, a new algorithm for the inference of GRNs that was best performer in the
  DREAM4 In Silico Multifactorial challenge.**"; "**GENIE3 decomposes the prediction of a regulatory
  network between p genes into p different regression problems.**"; "**The importance of an input gene in
  the prediction of the target gene expression pattern is taken as an indication of a putative regulatory
  link.**"; "**It doesn't make any assumption about the nature of gene regulation, can deal with
  combinatorial and non-linear interactions, produces directed GRNs, and is fast and scalable.**"
- USE: the foundational trick — turn network inference into p regression problems; feature importance =
  regulatory edge. Still the engine inside SCENIC (as GRNBoost2). Sets up "what is a GRN / why hard."

## Section 1 — The benchmark that made it a science

### DREAM5 (Marbach et al.) — wisdom of crowds — VERIFIED
- Marbach D, Costello JC, Küffner R, … DREAM5 Consortium, … Stolovitzky G. "Wisdom of crowds for robust
  gene network inference." *Nature Methods* 9:796–804, 2012. DOI 10.1038/nmeth.2016.
- ABSTRACT-VERIFIED (verbatim): "**Reconstructing gene regulatory networks from high-throughput data is a
  long-standing challenge.**"; "**we performed a comprehensive blind assessment of over 30 network
  inference methods on Escherichia coli, Staphylococcus aureus, Saccharomyces cerevisiae and in silico
  microarray data.**"; "**We observed that no single inference method performs optimally across all data
  sets. In contrast, integration of predictions from multiple inference methods shows robust and high
  performance across diverse data sets.**"; "**We experimentally tested 53 previously unobserved
  regulatory interactions in E. coli, of which 23 (43%) were supported.**"; "**Our results establish
  community-based methods as a powerful and robust tool for the inference of transcriptional gene
  regulatory networks.**"
- USE: the prove-it/community anchor — blind assessment of 30+ methods; no single winner; ensembles win;
  and the honesty of experimentally testing predictions (43% of new edges confirmed).

## Section 2 — Into single cells

### SCENIC (Aibar et al.) — single-cell GRN inference — VERIFIED
- Aibar S, González-Blas CB, Moerman T, Huynh-Thu VA, … Aerts S. "SCENIC: single-cell regulatory network
  inference and clustering." *Nature Methods* 14:1083–1086, 2017. DOI 10.1038/nmeth.4463.
- ABSTRACT-VERIFIED (verbatim): "**We present SCENIC, a computational method for simultaneous gene
  regulatory network reconstruction and cell-state identification from single-cell RNA-seq data.**"; "**we
  demonstrate that cis-regulatory analysis can be exploited to guide the identification of transcription
  factors and cell states.**"; "**SCENIC provides critical biological insights into the mechanisms driving
  cellular heterogeneity.**"
- USE: the single-cell turn — network reconstruction AND cell-state identification together; cis-
  regulatory (motif) analysis to prune spurious edges. Note GENIE3/GRNBoost2 is its inference engine.

## Section 3 — The honest single-cell benchmark

### BEELINE (Pratapa et al.) — VERIFIED
- Pratapa A, Jalihal AP, Law JN, Bharadwaj A, Murali TM. "Benchmarking algorithms for gene regulatory
  network inference from single-cell transcriptomic data." *Nature Methods* 17:147–154, 2020. DOI
  10.1038/s41592-019-0690-6.
- ABSTRACT-VERIFIED (verbatim): "**We present a systematic evaluation of state-of-the-art algorithms for
  inferring gene regulatory networks from single-cell transcriptional data.**"; "**We develop an
  evaluation framework called BEELINE.**"; "**We find that the area under the precision-recall curve and
  early precision of the algorithms are moderate.**"; "**Techniques that do not require pseudotime-ordered
  cells are generally more accurate.**"; "**BEELINE will aid the development of gene regulatory network
  inference algorithms.**"
- USE: the referee for single-cell GRN — accuracy is "moderate" (refreshingly honest), concrete guidance
  (pseudotime-free methods do better). The prove-it discipline the digest keeps returning to.

## Section 4 — From inference to in silico perturbation

### CellOracle (Kamimoto et al.) — VERIFIED
- Kamimoto K, Stringa B, Hoffmann CM, Jindal K, Solnica-Krezel L, Morris SA. "Dissecting cell identity
  via network inference and in silico gene perturbation." *Nature* 614:742–751, 2023. DOI
  10.1038/s41586-022-05688-9.
- ABSTRACT-VERIFIED (verbatim): "**Cell identity is governed by the complex regulation of gene expression,
  represented as gene-regulatory networks.**"; "**Here we use gene-regulatory networks inferred from
  single-cell multi-omics data to perform in silico transcription factor perturbations, simulating the
  consequent changes in cell identity using only unperturbed wild-type data.**"; "**we simulate and
  experimentally validate a previously unreported phenotype that results from the loss of noto, an
  established notochord regulator.**"; "**CellOracle can be used to analyse the regulation of cell identity
  by transcription factors, and can provide mechanistic insights into development and differentiation.**"
- USE: the payoff — a GRN isn't just a diagram, it's a *simulator*; knock out a TF in silico from wild-type
  data alone and predict the phenotype (then validate at the bench). Direct virtual-cell / automated-
  discovery hook.

## Section 5 — Multiomic, enhancer-driven GRNs

### SCENIC+ (Bravo González-Blas et al.) — VERIFIED
- Bravo González-Blas C, De Winter S, Hulselmans G, … Aerts S. "SCENIC+: single-cell multiomic inference
  of enhancers and gene regulatory networks." *Nature Methods* 20:1355–1367, 2023. DOI
  10.1038/s41592-023-01938-4.
- ABSTRACT-VERIFIED (verbatim): "**Joint profiling of chromatin accessibility and gene expression in
  individual cells provides an opportunity to decipher enhancer-driven gene regulatory networks
  (GRNs).**"; "**SCENIC+ predicts genomic enhancers along with candidate upstream transcription factors
  (TFs) and links these enhancers to candidate target genes.**"; "**To improve both recall and precision
  of TF identification, we curated and clustered a motif collection with more than 30,000 motifs.**"; "**we
  use SCENIC+ to study the dynamics of gene regulation along differentiation trajectories and the effect
  of TF perturbations on cell state.**"
- USE: the frontier — add chromatin (ATAC) so edges run TF→enhancer→gene, not just TF→gene; ties back to
  the multi-omics thread (Sep 3). Enhancer-level mechanism.

## Section 6 — Lab hook + horizon
- A GRN is the *causal wiring diagram* of a cell — precisely the layer a virtual cell / Human Cell
  Simulator (/project/human-cell-simulator/, /post/newsletter-2026-08-15/) needs beyond static layers
  (Sep 3 multi-omics) and dynamics (Aug 27 RNA velocity). Structure = who controls whom.
- In silico perturbation (CellOracle) = simulate the experiment before running it — the mechanistic cousin
  of the automated-discovery / AI-agents horizon (/post/newsletter-2026-08-14/,
  /post/newsletter-2026-08-21/): predict a TF knockout, then let a self-driving lab test it.
- Complements design week: Sep 5 designs the *parts* (proteins); GRN inference maps the *circuit* they run
  in. Reading (function, Sep 2) + writing (design, Sep 5) + wiring (today) = the systems view.
- Open, callable, benchmarked: GENIE3/SCENIC/SCENIC+/CellOracle are open source; DREAM5 and BEELINE are
  the public prove-it standards (and both are candid that accuracy is "moderate" / no single method wins)
  — the same publish-the-model-and-the-test ethos behind the BioImage Model Zoo
  (/project/bioimage-model-zoo/) + BioEngine (/project/bioengine/) and the recurring benchmark discipline
  (/post/newsletter-2026-07-27/).
