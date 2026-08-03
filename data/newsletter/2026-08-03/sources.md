# Newsletter sources — 2026-08-03

Theme: **Generative design's third modality — small molecules — and its honest ruler.**
We've watched generative design conquer proteins (Jul 23/25) and RNA (Jul 30). The
oldest and hardest target is the small molecule: an astronomically large chemical
space and brutal wet-lab validation. 2025–26 delivered both a genuine capability
milestone — a target-aware 3D diffusion model **validated at the bench** (DiffGui,
*Nature Communications*) — and an unusually honest, application-faithful benchmark
that measures the gap between leaderboard wins and real drug discovery (MolGenBench).
A lab-strategy story about the lab's **prove-it / held-out-benchmark culture** and
the **design-build-test** loop, now in chemistry.

## Provenance / method
- Web research (WebSearch + WebFetch). X/Twitter sweep **skipped**: `scripts/lab-x.py
  monitor --since-hours 24 --min-likes 30` again returns **HTTP 402 Insufficient
  credits** (getxapi out of credits **~5 weeks**); `search`/`discover` gated.
  x-breaking stays disabled. Flagged to Wei again for a credit top-up.
- **De-dup / variety:** last ~13 digests skew imaging/omics — Jul 21 microscopy VLMs,
  Jul 26 spatial, Jul 29 cryo-ET, Aug 1 pathology — plus protein design (Jul 23/25),
  RNA design (Jul 30), self-driving labs (Jul 31), virtual cell (Aug 2). **Small-
  molecule generative chemistry has not been a theme** in this run; it's a genuinely
  different lane and completes the "generative design across modalities" arc (protein
  → RNA → small molecule). Distinct from Jul 28 ("Two Ledgers", genomic-FM eval) —
  that was sequence FMs vs linear baselines; this is *structure-based molecule
  generation* judged on real hit rates / novel-target generalization.
- **Verification discipline:** the capability anchor (**DiffGui**) is **peer-reviewed**
  and **primary-fetched from PMC** with verbatim quotes and exact assay numbers. The
  benchmark anchor (**MolGenBench**) is a **preprint (bioRxiv, Nov 2025)** — bioRxiv
  403s WebFetch, so its figures are **cross-corroborated across two sources** (the
  search's read of the bioRxiv full text + an independent secondary summary), which
  agreed on every number; labeled as preprint in the post. BoltzGen and the JCIM
  review are named for framing, not load-bearing numbers.

## Item 1 — Capability: generative SBDD reaches the bench (ANCHOR, peer-reviewed, primary-fetched)
- Source (fetched, PMC): Qiaoyu Hu, Changzhi Sun, Huan He, Jiazheng Xu, Danlin Liu,
  Wenqing Zhang, Sumeng Shi, Kai Zhang, Honglin Li, "Target-aware 3D molecular
  generation based on guided equivariant diffusion," **Nature Communications 16, 7928
  (2025)**, DOI 10.1038/s41467-025-63245-0 (PMID 40854901).
  https://www.nature.com/articles/s41467-025-63245-0 · https://pmc.ncbi.nlm.nih.gov/articles/PMC12379259/
  · code: GitHub QiaoyuHu89/DiffGui.
- Verified facts / verbatim:
  - **DiffGui** = a **target-conditioned E(3)-equivariant diffusion** model that
    generates ligands inside a protein pocket non-autoregressively; two innovations:
    **concurrent atom + bond diffusion** (separate noise schedules; bond types inferred
    from dynamic atom distances → fewer distorted rings) and **property guidance**
    (classifier-free guidance injecting binding affinity + drug-likeness — QED, SA,
    LogP, TPSA — into training and sampling).
  - Benchmarks: on **PDBbind**, lowest JS divergence for bond/angle/dihedral
    distributions and best affinity/validity vs ResGen, PocketFlow, GCDM, TargetDiff,
    DiffSBDD, PMDM; ~1 Å RMSD; competitive on **CrossDocked** (not trained on it).
  - **Wet-lab validation (the news):** *de novo* on **RSK4** (PDB 6g77, not in
    PDBbind) — two synthesized compounds active in an HTRF assay, **IC₅₀ ≈ 215.0 nM
    and ≈ 111.1 nM**; *lead optimization* on **DHODH** improved potency (8.02 µM →
    4.27 µM; 32.20 nM → 10.45 nM). Verbatim: "both Compound 1 and Compound 2
    demonstrate potent inhibitory activity in the HTRF assay"; "DiffGui outperforms
    existing methods in generating molecules with high binding affinity, rational
    chemical structure."

## Item 2 — The honest ruler: MolGenBench (ANCHOR, preprint, cross-corroborated)
- Source: "Benchmarking Real-World Applicability of Molecular Generative Models from
  De novo Design to Lead Optimization with MolGenBench," **bioRxiv 2025.11.03.686215**
  (Nov 2025, preprint). https://www.biorxiv.org/content/10.1101/2025.11.03.686215v1.full
  (bioRxiv 403s WebFetch; figures corroborated by an independent secondary summary.)
- Corroborated facts (both sources agree; preprint — reported by authors):
  - Scale: **120 protein targets, 5,433 chemical series, 220,005 experimentally
    confirmed active molecules; benchmarks 17 generative models** with metrics for
    target awareness, hit rate, and lead optimization.
  - **Generalization gap:** stratifying test proteins by whether they appear in the
    CrossDock training set, performance drops on unseen proteins — top de novo hit
    rate **0.124% (in CrossDock) → 0.024% (unseen)**; TamGen target recovery **30.3 →
    18.7** after removing training overlap. "Prior benchmarks that do not stratify by
    training data exposure overestimate real-world utility."
  - **Weak target awareness:** most models "generated structurally similar molecules
    regardless of which target they were conditioned on."
  - **Pose quality:** only a small fraction — "typically below 23%" — of generated
    poses match redocked conformations within **2 Å RMSD**; higher strain energy than
    classical docking.
  - **Scaling doesn't fix it:** sampling up to **100,000** molecules "increased the
    absolute number of active discoveries but with diminishing efficiency" — without
    better scoring functions, scaling offers limited practical value.

## Item 3 — The way through (framing; named, corroborated, not load-bearing numbers)
- **Novel-target generalization is tractable — proof from the binder world:**
  **BoltzGen** (universal generative binder framework, Nov 2025) reported wet-lab
  validation generating binders with **nanomolar affinities for 9 novel protein
  targets** sharing **<30% sequence identity** with any bound structure in the PDB —
  a direct answer to the "poor generalization to novel targets" wall, in the protein-
  binder modality. https://neurosnap.ai/blog/post/boltzgen-a-universal-generative-framework-for-biomolecular-binder-design/6914d2838b9522d6ffefa787
- **2026 review directions:** "Generative AI for the Design of Molecules: Advances and
  Challenges," *J. Chem. Inf. Model.* (2026), doi 10.1021/acs.jcim.5c02234 — points to
  integrating **physical priors** (differentiable physics), overcoming **data scarcity**
  (synthetic augmentation, transfer learning), **multimodal fusion** of structural,
  omics, and phenotypic data, **autonomous AI agents** for adaptive decision-making,
  and **uncertainty-aware multi-objective** optimization. https://pubs.acs.org/doi/10.1021/acs.jcim.5c02234

## Lab connections (for "why it matters")
- **Generative design across modalities.** The lab tracks and builds design tooling;
  we've digested protein design (Jul 23/25) and RNA design (Jul 30). Small molecules
  are the third modality — same design-build-*test* philosophy, hardest validation.
- **Prove-it / held-out-benchmark culture.** MolGenBench is exactly the application-
  faithful, training-exposure-stratified benchmark discipline the lab champions
  ([BioImage Model Zoo](/project/bioimage-model-zoo/), AI4Life; Jul 27/28). Its core
  lesson — stratify by novelty or you'll overestimate — is our lesson.
- **Agents + the loop.** The review's "autonomous AI agents for adaptive decision-
  making" and closing the design→synthesis→assay loop is the lab's
  [Agent-Lens](/project/agent-lens/) / [BioImage.IO chatbot](/project/bioimageio-chatbot/)
  / self-driving-lab territory (Jul 31).
- **Multimodal → the virtual cell.** "Multimodal fusion of structural, omics, and
  phenotypic data" is the [Human Cell Simulator](/project/human-cell-simulator/) thesis:
  score a molecule not just by pocket fit but by its predicted cellular phenotype.

## De-dup check
- Recent digests: Aug 2 virtual cell (interpretable); Aug 1 pathology; Jul 31 self-
  driving labs; Jul 30 RNA design; Jul 29 cryo-ET; Jul 28 genomic-FM eval; Jul 27
  strategy; Jul 26 spatial; Jul 25 antibody binding; Jul 24 open science; Jul 23
  protein-part design. **Small-molecule generative chemistry / SBDD has not been a
  theme** — new lane, capability-forward with an honest ruler. Clear to run.
