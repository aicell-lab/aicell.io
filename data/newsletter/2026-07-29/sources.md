# Newsletter sources — 2026-07-29

Theme: **Visual proteomics** — building a *molecular atlas of the cell, in situ*.
Cryo-electron tomography (cryo-ET) can now image molecular machines inside intact
cells; the dream is to identify every one directly from the picture. The bottleneck
was never really the microscope — it's **pattern recognition in near-noise 3D volumes**,
and that's where AI + open community data are breaking through. A deliberate pivot to an
*imaging* modality after a fortnight heavy on omics/design/strategy/evaluation.

## Provenance / method
- Web research (WebSearch + WebFetch). X/Twitter sweep **skipped**: `scripts/lab-x.py
  monitor` still returns **HTTP 402 Insufficient credits** (getxapi out of credits ~4 weeks).
  x-breaking stays disabled.
- **De-dup:** last 9 digests covered design/genomics/spatial/strategy/evaluation; **no**
  recent digest touched cryo-ET / in-cell structural biology / visual proteomics. Distinct.
  Also deliberately *avoided* re-running the "foundation models lose to linear baselines"
  benchmarking story (that was Jul 28 *Two Ledgers*), even though a fresh virtual-cell
  benchmark (VCBench, Jun 2026) surfaced — too close to yesterday.
- Verification: two anchors **primary-fetched** (arXiv review; AITom via PMC). Two anchors
  (Chlamydomonas dataset; CZII challenge) **corroborated across multiple secondary sources**
  (journal fulltext listing, PubMed, EMPIAR, GitHub, CZ Biohub blog, Kaggle/Virtual Cells
  Platform) because cell.com / biorxiv full text blocked WebFetch (403).

## Item 1 — The open in-cell atlas: 1,829 Chlamydomonas tomograms (fresh flagship)
- Source: "Toward community-driven visual proteomics with large-scale cryo-electron
  tomography of *Chlamydomonas reinhardtii*," **Molecular Cell**, online **Dec 19, 2025**
  (2026 print issue), DOI 10.1016/j.molcel.2025.11.029. PubMed 41421337.
  https://www.cell.com/molecular-cell/fulltext/S1097-2765(25)00970-0
  Senior authors: Jürgen M. Plitzko, Benjamin D. Engel, Abhay Kotecha (lead Ron Kelley et al.).
- Verified facts (multi-source consistent):
  - **1,829 annotated tomograms** of the green alga *C. reinhardtii*, prepared by
    **cryo-plasma-FIB milling**, released as a **community resource** spanning the breadth of
    organelles, with accompanying raw data.
  - Validated by **subtomogram averaging** of complexes from **>3 MDa to ~200 kDa** — 80S
    ribosomes, Rubisco, nucleosomes, microtubules, clathrin, photosystem II, mitochondrial
    ATP synthase — **majority reaching sub-nanometer resolution**.
  - Open data: raw tilt series in **EMPIAR (EMPIAR-11830)**; community annotations on GitHub
    (Chromatin-Structure-Rhythms-Lab/ChlamyAnnotations). Explicit aim: an *example for open
    sharing* of large-scale cryo-ET datasets.

## Item 2 — Crowdsourcing the pattern-recognition bottleneck: CZII particle-picking challenge
- Sources: CZ Imaging Institute, "Crowdsourcing to solve problems in CryoET"
  https://www.czbiohub.org/life-science/crowdsourcing-solve-problems-cryoet/ ;
  "Open-source Tools for CryoET Particle Picking ML Competitions" (bioRxiv 2024.11.04.621608);
  "Lessons learned from a Kaggle challenge for particle picking in cryo-ET" (bioRxiv
  2025.11.03.686153, Nov 2025); CZII CryoET Object Identification dataset on the CZI
  **Virtual Cells Platform** https://virtualcellmodels.cziscience.com/dataset/czii-cryoet
- Verified facts:
  - **Particle picking** (hand-labeling every macromolecule) is a major cryo-ET bottleneck —
    "can take months" — blocking routine *in situ* structure determination.
  - CZII ran a **3-month Kaggle challenge**, six particle types across hundreds of
    experimental tomograms; **>1,000 participants**; winning models **outperformed existing
    state-of-the-art** (data augmentation was decisive).
  - All tomograms + ground truth + winners' annotations released **open (CC0) on the CryoET
    Data Portal**; open tools **Copick** (storage-agnostic API) and **MONAI 3D U-Net**
    notebooks. Six particle types: apo-ferritin, β-amylase, β-galactosidase, ribosome,
    thyroglobulin, virus-like particle.
  - Notable: hosted on CZI's **Virtual Cells Platform** — visual proteomics feeding the
    virtual-cell effort.

## Item 3 — AI across the whole pipeline (the synthesis + an open toolkit)
- Source A (primary-fetched): Zhou, Hu, Lee, Z. Hong Zhou, Demetri Terzopoulos, "Review of
  Deep Learning Applications to Structural Proteomics Enabled by Cryogenic Electron Microscopy
  and Tomography," **arXiv:2507.19565** (submitted 25 Jul 2025, CC0).
  https://arxiv.org/abs/2507.19565
  - Verified: DL now spans the pipeline — **particle picking** (Topaz, crYOLO, CryoSegNet),
    **denoising** (Topaz-Denoise), **missing-wedge correction** (IsoNet, U-Net),
    **orientation-bias** (spIsoNet, cryoPROS), **subtomogram averaging** (TomoNet),
    **automated atomic model building** (ModelAngelo, DeepTracer, CryoREAD). Applied "from
    HIV virus-like particles to in situ ribosomal complexes"; addresses "low signal-to-noise
    ratios, preferred orientation artifacts, and missing-wedge problems."
- Source B (primary-fetched, PMC): Zhan, Zeng, Uddin, **Min Xu** (CMU), "AITom: AI-guided
  cryo-electron tomography image analyses toolkit," **J Struct Biol** 217(2):108207 (May 2025),
  DOI 10.1016/j.jsb.2025.108207. https://pmc.ncbi.nlm.nih.gov/articles/PMC12934263/
  - Verified: open-source **end-to-end cryo-ET AI platform** (simulation → preprocessing →
    picking → segmentation → classification → alignment/averaging), emphasizing subtomogram
    classification/segmentation; integrates template-based, template-free, and deep-learning
    (incl. few-shot, domain adaptation) methods; GPU-accelerated.
- Honest frontier (from the visual-proteomics literature, stated as open challenge, not a
  claim): only a *handful* of molecular species are reliably identified in crowded, low-SNR
  cytoplasm so far; the full "molecular atlas / molecular sociology of the cell" is not solved.

## Lab connections (for "why it matters")
- **Imaging as measurement at molecular resolution:** seeing proteins *in situ* is the
  structural ground truth beneath **whole-cell modeling** ([Human Cell Simulator](/project/human-cell-simulator/)).
  It complements the lab's fluorescence / **Human Protein Atlas** imaging (which says *where*
  a protein is) with structural *identity* (which machine it belongs to).
- **Open data + open AI tools + community benchmarking** is exactly the lab's mode —
  [BioImage Model Zoo](/project/bioimage-model-zoo/), [BioEngine](/project/bioengine/), AI4Life.
  A crowdsourced, openly-benchmarked particle picker is a BioImage-Model-Zoo story in a
  different modality.
- A **molecular atlas of the cell** is precisely what a virtual cell would want to simulate —
  the CZII dataset literally living on a *Virtual Cells Platform* makes the link concrete.

## De-dup check
- Recent digests: Jul 28 genomic-FM evaluation; Jul 27 ecosystem/strategy; Jul 26 spatial;
  Jul 25 antibody design; Jul 24 open science; Jul 23 genome writing; Jul 22 protein dynamics;
  Jul 21 microscopy VLMs; Jul 20 enzyme design. **No prior digest** covered cryo-ET / in-cell
  structural biology / visual proteomics. Clear to run.
