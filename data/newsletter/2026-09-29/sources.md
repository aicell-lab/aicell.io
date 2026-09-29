# Newsletter sources — 2026-09-29

Theme: **Predicting the perturbation** — models that predict how a cell's
transcriptome responds to a genetic or chemical perturbation it may never have seen.
Given a cell's state and a perturbation (a gene knockout/activation, a drug, a dose),
predict the new state. This is the *operational* definition of the virtual cell, and
directly the lab's human-cell-simulator problem.

**Dedup guard:** Distinct from Aug 15 (single-cell *foundation models* — Geneformer,
scGPT — general pretrained transformers whose perturbation ability is emergent).
Today's anchors are **purpose-built perturbation-response predictors** (a different
lineage: VAEs, compositional autoencoders, knowledge-graph GNNs, disentanglement),
plus the experimental data engine (Perturb-seq) they learn from. Also distinct from
Sep 21 (drug *response* in cancer cell lines — IC50/sensitivity) and Sep 6 (GRN
inference).

Verified via NCBI E-utilities + Europe PMC (esearch/efetch and REST core). Fetched
2026-09-29T03:02Z. Only verbatim quoted phrases are used in the post.

## Anchors (verified; abstracts captured)

1. **Perturb-Seq: Dissecting Molecular Circuits with Scalable Single-Cell RNA
   Profiling of Pooled Genetic Screens** — Dixit, Parnas, ..., Regev. *Cell* (2016).
   DOI 10.1016/j.cell.2016.11.038 | PMID 27984732.
   Why: the data engine. "Combining single-cell RNA sequencing … and CRISPR-based
   perturbations to perform many such assays in a pool," it "accurately identifies
   individual gene targets, gene signatures, and cell states affected by individual
   perturbations and their genetic interactions" — the measurement that makes learning
   possible.

2. **Exploring genetic interaction manifolds constructed from rich single-cell
   phenotypes** — Norman, Horlbeck, ..., Weissman. *Science* (2019).
   DOI 10.1126/science.aax4438 | PMID 31395745.
   Why: the conceptual leap to *combinations*. "How cellular and organismal complexity
   emerges from combinatorial expression of genes is a central question"; they build
   "high-dimensional landscapes of cell states (manifolds)" from Perturb-seq to order
   pathways and classify genetic interactions — the phenotype space later models learn
   to navigate.

3. **scGen predicts single-cell perturbation responses** — Lotfollahi, Wolf, Theis.
   *Nature Methods* (2019). DOI 10.1038/s41592-019-0494-8 | PMID 31363220.
   Why: the first out-of-sample predictor. "Accurately modeling cellular response to
   perturbations is a central goal of computational biology," yet "no generalization …
   to phenomena absent from training data (out-of-sample) has yet been demonstrated."
   scGen "combin[es] variational autoencoders and latent space vector arithmetics" and
   "accurately models perturbation and infection response of cells across cell types,
   studies and species."

4. **Predicting cellular responses to complex perturbations in high-throughput screens
   (CPA)** — Lotfollahi, Klein, ..., Theis. *Molecular Systems Biology* (2023).
   DOI 10.15252/msb.202211517 | PMID 37154091.
   Why: composition and dose. "An exhaustive exploration of the combinatorial
   perturbation space is experimentally unfeasible," so CPA "combines the
   interpretability of linear models with the flexibility of deep-learning approaches"
   to "in silico predict transcriptional perturbation response at the single-cell level
   for unseen dosages, cell types, time points, and species," including "unseen drug
   combinations."

5. **Predicting transcriptional outcomes of novel multigene perturbations with GEARS**
   — Roohani, Huang, Leskovec. *Nature Biotechnology* (2024).
   DOI 10.1038/s41587-023-01905-6 | PMID 37592036.
   Why: predict the truly unseen. Facing "the combinatorial explosion in the number of
   possible multigene perturbations," GEARS "integrates deep learning with a knowledge
   graph of gene-gene relationships" and "is able to predict outcomes of perturbing
   combinations consisting of genes that were never experimentally perturbed,"
   reporting "40% higher precision than existing approaches."

6. **Disentanglement of single-cell data with biolord** — Piran, Cohen, ..., Nitzan.
   *Nature Biotechnology* (2024). DOI 10.1038/s41587-023-02079-x | PMID 38225466.
   Why: representation-first. Biolord "disentangl[es] single-cell multi-omic data to
   known and unknown attributes," and "by virtually shifting cells across states …
   generates experimentally inaccessible samples, outperforming state-of-the-art
   methods in predictions of cellular response to unseen drugs and genetic
   perturbations."

## Horizon radar (strategy note)
- This *is* the virtual cell's core computation: **state + perturbation → new state.**
  Everything the lab's human-cell-simulator aims at reduces to predicting a cell's
  response to an intervention it hasn't been shown.
- The universal bottleneck is **combinatorial explosion + out-of-distribution
  generalization** (Norman, CPA, GEARS all say it): you can never measure every
  perturbation × cell × dose, so the value is entirely in *generalizing* beyond the
  training grid — a data/benchmark problem as much as a model one.
- Structure-vs-scale echoes: knowledge graphs (GEARS) inject biological priors;
  disentanglement (biolord) and compositional models (CPA) impose structure so models
  extrapolate. Priors + representation learning — the lab's recurring bet.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/search/discover` returns
  HTTP 402 "Insufficient credits" (getxapi out of credits; ~52nd consecutive skip;
  Grok-based replacement wired, awaiting a credit decision).
- Anchor verification: NCBI E-utilities + Europe PMC (both used; NCBI/Europe PMC each
  had transient hiccups, cross-checked). All six DOIs resolved to a record with
  matching title + abstract + PMID. Only verbatim quoted phrases are used.
- Dedup: dedicated single-cell perturbation-response prediction has NOT been a prior
  nightly theme. Distinct from Aug 15 (foundation models), Sep 21 (cancer drug
  response), Sep 6 (GRN inference). A candidate "linear-baseline benchmark" paper was
  considered but dropped — could not be cleanly verified as peer-reviewed at run time.
