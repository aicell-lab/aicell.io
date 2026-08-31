# Newsletter sources — August 31, 2026

**Theme:** AI for cryo-EM conformational heterogeneity — recovering a *distribution of shapes* (and
the motion between them) from millions of noisy 2D single-particle images, instead of averaging every
molecule into one consensus map ("A Thousand Frozen Poses"). The EXPERIMENTAL-imaging counterpart to
Aug 11 (/post/newsletter-2026-08-11/, "After the Fold, the Motion" — protein motion *predicted from
sequence* via generative MD emulators): same target (the conformational landscape), opposite route
(recovered from real pictures). Horizon / strategy-radar: structure determination is "solved" for
static folds; the frontier is ensembles and dynamics — the substrate a virtual cell must reproduce.

**Dedup guard:** Distinct from Jul 29 (/post/newsletter-2026-07-29/, cryo-ET / visual proteomics —
tomography of whole cells + particle PICKING) and from Aug 11 (predicted ensembles). This is
single-particle continuous-heterogeneity RECONSTRUCTION. Also considered but REJECTED for today: an
HPA subcellular-localization theme — Aug 4 (/post/newsletter-2026-08-04/, "The Cell's Fingerprint")
already covers HPA image localization (SubCell/Lundberg). [HPA anchors were fully verified and are
BANKED for a future distinct "citizen-science / competition → self-supervised annotation" digest that
would feature Wei Ouyang's own first-author Nat Methods 2019 HPA-competition paper.]

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on monitor AND discover; ~22nd
consecutive skip (>three weeks). Grok replacement wired, awaiting xAI credits.

All anchors verified by two parallel general-purpose subagents against Crossref / Europe PMC / arXiv,
with VERBATIM abstracts. Only abstract-verified quotes are used. Caveats per anchor below.

---

## Section 1 — The breakthrough: reconstruct the whole distribution

### cryoDRGN — neural nets recover continuous heterogeneity — VERIFIED
- Zhong, E.D., Bepler, T., Berger, B. & Davis, J.H. "CryoDRGN: reconstruction of heterogeneous cryo-EM
  structures using neural networks." *Nature Methods* **18**(2):176–185, 2021. DOI:
  10.1038/s41592-020-01049-4. First author Ellen D. Zhong; senior/corresponding Bonnie Berger &
  Joseph H. Davis; all MIT.
- ABSTRACT-VERIFIED (verbatim): "**many imaged protein complexes exhibit conformational and
  compositional heterogeneity that poses a major challenge to existing three-dimensional
  reconstruction methods**"; "**Here, we present cryoDRGN, an algorithm that leverages the
  representation power of deep neural networks to directly reconstruct continuous distributions of 3D
  density maps and map per-particle heterogeneity of single-particle cryo-EM datasets**"; "**Using
  cryoDRGN, we uncovered residual heterogeneity in high-resolution datasets of the 80S ribosome and
  the RAG complex, revealed a new structural state of the assembling 50S ribosome, and visualized
  large-scale continuous motions of a spliceosome complex.**"

## Section 2 — Modeling motion explicitly

### 3DFlex — a motion-based neural network — VERIFIED
- Punjani, A. & Fleet, D.J. "3DFlex: determining structure and motion of flexible proteins from
  cryo-EM." *Nature Methods* **20**(6):860–870, 2023. DOI: 10.1038/s41592-023-01853-8. Two authors
  (Univ. Toronto / Vector Institute / Structura Biotechnology — the company behind cryoSPARC; the
  record names "Structura Biotechnology," not the product "cryoSPARC").
- ABSTRACT-VERIFIED (verbatim): "**We introduce Three-Dimensional Flexible Refinement (3DFlex), a
  motion-based neural network model for continuous molecular heterogeneity for cryo-EM data**";
  "**3DFlex exploits knowledge that conformational variability of a protein is often the result of
  physical processes that transport density over space and tend to preserve local geometry**"; "**From
  two-dimensional image data, 3DFlex enables the determination of high-resolution 3D density, and
  provides an explicit model of a flexible protein's motion over its conformational landscape**";
  "**3DFlex can improve 3D density resolution beyond the limits of existing methods because particle
  images contribute coherent signal over the conformational landscape.**"

### DynaMight — deformations + an honest caveat (open source, RELION-5) — VERIFIED
- Schwab, J., Kimanius, D., Burt, A., Dendooven, T. & Scheres, S.H.W. "DynaMight: estimating molecular
  motions with improved reconstruction from cryo-EM images." *Nature Methods* **21**(10):1855–1862,
  2024. DOI: 10.1038/s41592-024-02377-5. First author Johannes Schwab; senior Sjors H. W. Scheres;
  MRC Laboratory of Molecular Biology, Cambridge. Open access (CC BY).
- ABSTRACT-VERIFIED (verbatim, via Europe PMC PMC11466895): "**How to deal with continuously flexing
  molecules is one of the biggest outstanding challenges in single-particle analysis of proteins from
  cryogenic-electron microscopy (cryo-EM) images**"; "**Here, we present DynaMight, a software tool
  that estimates a continuous space of conformations in a cryo-EM dataset by learning three-dimensional
  deformations of a Gaussian pseudo-atomic model of a consensus structure for every particle image**";
  "**Inversion of the learned deformations is then used to obtain an improved reconstruction of the
  consensus structure**"; HONEST CAVEAT (verbatim): "**how regularization of the three-dimensional
  deformations through the use of atomic models may lead to important artifacts due to model bias**";
  "**DynaMight is distributed as free, open-source software, as part of RELION-5.**"

## Section 3 — The honest frontier + lab hook

### CryoBench — the ground-truth/benchmark reckoning — VERIFIED (title/authors/year; abstract mostly paraphrased)
- Jeon, M., Raghu, R., Astore, M., Woollard, G., Feathers, R., Kaz, A., Hanson, S.M., Cossio, P. &
  Zhong, E.D. "CryoBench: Diverse and challenging datasets for the heterogeneity problem in cryo-EM."
  **arXiv:2408.05526**, 2024 (submitted 10 Aug 2024; rev. Jan 2025). Senior author Ellen D. Zhong.
  Project page: cryobench.cs.princeton.edu.
- CITATION CAUTION: the export-API abstract was rate-limited; a WebFetch PARAPHRASED the abstract, so
  only the two short fragments below are quoted verbatim — everything else is described in our words.
  Do NOT assert a conference venue (NeurIPS 2024 D&B is likely but was NOT confirmed) — cite the arXiv
  id only.
- VERBATIM fragments: CryoBench is "**a suite of datasets, metrics, and benchmarks for heterogeneous
  reconstruction in cryo-EM**"; the authors hope it will be a "**foundational resource for accelerating
  algorithmic development and evaluation**."
- PARAPHRASE (not quoted): motivated by the observation that progress is limited by the absence of
  standardized benchmarks with ground truth and reliable validation metrics; provides five datasets
  spanning conformational heterogeneity (antibody-complex motions, molecular-dynamics simulations) and
  compositional heterogeneity (e.g., ribosome assembly states); analyzes state-of-the-art neural and
  non-neural reconstruction tools and their noise sensitivity; proposes new quantitative metrics.

### Frontier + lab hook
- Frontier / prove-it (/post/newsletter-2026-07-27/): a recovered "motion" is a *model* of the data,
  not a direct observation — DynaMight itself warns of "artifacts due to model bias," and CryoBench
  exists precisely because the field lacked ground truth to tell a real conformational change from an
  algorithm's hallucination. Trust the arrow only when metrics + orthogonal evidence agree.
- Symmetry with Aug 11 (/post/newsletter-2026-08-11/): motion PREDICTED from sequence (generative MD
  emulators) vs motion RECOVERED from images (cryo-EM heterogeneity) — two roads to the same
  conformational landscape; a virtual cell will want both, cross-checked.
- Lab hook: conformational dynamics is the molecular raw material of a virtual cell — the Human Cell
  Simulator (/project/human-cell-simulator/) and the virtual-cell horizon (/post/newsletter-2026-08-15/);
  and the whole field runs on OPEN, callable tools (cryoDRGN, RELION-5, cryoSPARC/3DFlex) — the
  BioImage Model Zoo (/project/bioimage-model-zoo/) / BioEngine (/project/bioengine/) ethos of
  publishing the model *and* the benchmark, not a black box.
