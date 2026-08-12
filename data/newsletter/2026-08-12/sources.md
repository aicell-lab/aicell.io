# Newsletter sources — 2026-08-12 (fetched UTC 2026-08-12T03:00:39Z)

Theme: **The handshake — from folding one protein to predicting how molecules
*bind*, and how *tightly*.** AlphaFold solved the single fold; the 2024–25 frontier
is **co-folding**: predicting the joint structure of *complexes* (protein + protein,
DNA/RNA, small molecules, ions) in one unified model — and then, with **Boltz-2**,
predicting **binding affinity** at an accuracy approaching physics-based free-energy
perturbation (FEP) but ~1000× faster. A horizon story: a cell is a *network of
interactions*, so a [virtual cell](/project/human-cell-simulator/) needs the wiring
and its strengths, not just the parts; fast affinity makes agent-driven
[in-silico screening](/project/autonomous-research-agents/) practical; and the
open-source Boltz line carries the [BioImage Model Zoo](/project/bioimage-model-zoo/)
ethos to molecular interactions. Natural progression from the recent run: parts
([Aug 3 design](/post/newsletter-2026-08-03/)) → motion
([Aug 11 dynamics](/post/newsletter-2026-08-11/)) → **interactions (today)**.

## Provenance / method
- Web research (WebSearch + WebFetch). All three anchors are peer-reviewed / established
  and grounded in **primary sources**:
  - **AlphaFold3** — *Nature* 2024 (PMID 38718835), verified title, citation, DOI, and
    the exact capability/accuracy claims from the PubMed/Nature abstract.
  - **Boltz-1** — MIT Jameel Clinic / MIT News + bioRxiv (PMC11601547, PMID 39605745);
    team, license, accuracy-vs-AF3/Chai-1, and 30–60 s runtime from MIT's own pages.
  - **Boltz-2** — bioRxiv 2025.06.14.659707 (MIT CSAIL + Jameel Clinic + Recursion);
    the FEP-accuracy/1000× claim, MIT-license open source, and the FEP+/CASP16/Polaris
    benchmark numbers from Boltz's site, MIT, and Recursion's release. The antibody
    caveat (still lags AF3) is reported explicitly.
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  returns **HTTP 402 Insufficient credits** (getxapi out of credits ~6 weeks). A
  replacement using **xAI Grok's `x_search` Agent-Tools API** is wired but the xAI team
  has **no credits yet** (403 permission-denied) — pending a top-up. Flagged to Wei.
- **De-dup / variety (important):** *molecular complex prediction (co-folding) + binding
  affinity* has **not** been a digest theme. Distinct from the recent run:
  - **Jul 23 "AI Designs the Parts" / Jul 25 "Designed to Bind"** = protein/binder
    *design* (invent a new sequence/structure). Today = predict the *structure and
    strength* of an interaction between existing molecules. (Jul 25 touched binders by
    *design*; today is *prediction + affinity ranking* — the screening side.)
  - **Aug 11 "After the Fold, the Motion"** = one protein's conformational *ensemble*.
    Today = how *two-or-more* molecules dock, and how tightly. Different object (complex
    vs single chain), different axis (affinity vs dynamics).
  - **Aug 3 "The Third Molecule"** = generative small-molecule *design*. Today's affinity
    model is the *scoring/ranking* half that a generative designer needs — explicitly
    framed as complementary (Boltz-2 + a generative model = a full design loop).
  - **Aug 9 genome FMs / Aug 10 optical pooled screening / Aug 2 virtual cell** = DNA
    sequence, cellular phenotype. Today is the molecular-interaction layer beneath them.
  Clear separation. Clear to run.
- **Verification discipline:** AF3 is peer-reviewed (*Nature* 2024). Boltz-1 is
  peer-reviewed-adjacent (bioRxiv + MIT, widely used) and **labelled a preprint**;
  Boltz-2 is a **June 2025 bioRxiv preprint** — labelled as such; its headline numbers
  are quoted from the authors/benchmarks and attributed, not asserted as independent fact.
  Chai-1 cited only as the first closed AF3 replication (context).

## Item 1 — Co-folding: one model for the whole complex (AlphaFold3)
- **Source:** Josh Abramson, ... John Jumper et al., "**Accurate structure prediction of
  biomolecular interactions with AlphaFold 3**," ***Nature* 630(8016):493–500, 2024**,
  DOI 10.1038/s41586-024-07487-w (PMID 38718835; Addendum s41586-024-08416-7).
- Verified facts:
  - **What changed:** a **diffusion-based architecture** that **directly generates atomic
    coordinates** and **minimizes the role of MSAs**, capable of predicting the **joint
    structure of complexes** — "proteins, nucleic acids, small molecules, ions and
    modified residues" — in one unified model.
  - **Accuracy:** "far greater accuracy for **protein–ligand** interactions compared with
    state-of-the-art docking tools, much higher accuracy for **protein–nucleic acid**
    interactions ... and substantially higher **antibody–antigen** prediction accuracy
    compared with AlphaFold-Multimer v2.3" — "high-accuracy modelling across biomolecular
    space ... within a single unified deep-learning framework."
  - **Openness (the catch):** at release AF3 was **not fully open-source** and **not for
    commercial use** (free non-commercial server; inference code later on GitHub for
    academic use) — which is exactly what motivated the open replications below.

## Item 2 — Democratizing it: Boltz-1 (open, AF3-level) → Boltz-2 (adds affinity)
- **Boltz-1** — Jeremy Wohlwend, Gabriele Corso, Saro Passaro, Regina Barzilay & Tommi
  Jaakkola (MIT Jameel Clinic), "**Boltz-1: Democratizing Biomolecular Interaction
  Modeling**," bioRxiv 2024.11.19.624167 (PMC11601547, PMID 39605745), **Nov 2024**.
  - **First fully open-source, commercially usable** model reaching **AlphaFold3-reported
    accuracy** — training + inference code, weights, datasets, benchmarks under **MIT
    license**. Predicts **protein, RNA, DNA, and small-molecule** structures.
  - **Speed:** a biomolecular complex prediction in **~30–60 seconds** (Corso) at AF3-level
    accuracy. Named for the **Boltzmann distribution**. Benchmarked to **match Chai-1**
    (the first closed-but-public AF3 replication) — "and therefore AlphaFold3."
- **Boltz-2 (ANCHOR)** — MIT CSAIL + Jameel Clinic + **Recursion**, "**Boltz-2: Towards
  Accurate and Efficient Binding Affinity Prediction**," bioRxiv **2025.06.14.659707**,
  **June 2025** (open source, **MIT license**, incl. training code).
  - **The leap:** the **first biomolecular co-folding model to jointly predict structure
    *and* binding affinity** — "goes beyond AlphaFold3 and Boltz-1." The **first deep-
    learning model to approach the accuracy of physics-based FEP** while running **~1000×
    faster**, making accurate **in-silico virtual screening** practical for early drug
    discovery.
  - **Benchmarks (attributed to the authors):** on the **FEP+ (OpenFE)** affinity
    benchmark (targets held out of training), **average Pearson ≈ 0.62** — comparable to
    the OpenFE FEP pipeline, >1000× faster. In the **CASP16 affinity challenge**, run
    **out-of-the-box with no fine-tuning**, it **outperformed all submitted methods** across
    **140 protein–ligand pairs**. On **Polaris-ASAP**, matched the **top-5** contenders
    with no fine-tuning or physics relaxation.
  - **Honest caveat:** on an **antibody structure** benchmark Boltz-2 improves over Boltz-1
    but **still lags AlphaFold3** — not uniformly superior.
  - **Full loop demonstrated:** coupling Boltz-2 with a **generative small-molecule model**
    yielded **diverse, synthesizable, high-affinity binders** for **TYK2**, as estimated by
    **absolute FEP** simulations — a design→score→refine loop end-to-end.

## Item 3 — Why it matters for the lab + the honest frontier
- **The wiring of a virtual cell.** A [Human Cell Simulator](/project/human-cell-simulator/)
  is not a bag of isolated parts — it is a **network of interactions**: which proteins bind
  which partners, which drug touches which pocket, how tightly. Co-folding predicts the
  *edges* of that network and affinity puts *weights* on them. If [Aug 11](/post/newsletter-2026-08-11/)
  put *motion* under the parts, this puts *connections and their strengths* between them —
  the layer a cell model needs to reason about signalling and perturbation.
- **Affinity makes agents useful.** Fast, accurate affinity turns
  [autonomous research agents](/project/autonomous-research-agents/) into practical
  drug-discovery loops: an agent can screen or **generate** candidate molecules
  ([Aug 3](/post/newsletter-2026-08-03/)), **score** them with a co-folding+affinity model,
  and send only the best to the bench — the Boltz-2 + generative-model loop, in miniature.
- **Open models, runnable.** Boltz ships weights + **training** code under MIT license — the
  same open, buildable-on ethos as [BioImage Model Zoo](/project/bioimage-model-zoo/) /
  [BioEngine](/project/bioengine/), now for molecular interactions. That's what lets a lab
  *fine-tune* to its own chemistry rather than query a black box.
- **The honest frontier (prove-it).** Affinity predictions are **hypotheses**, not verdicts:
  Boltz-2 *approaches* FEP (Pearson ≈ 0.62 is useful for ranking, not a binding constant),
  still **lags AF3 on antibodies**, and every predicted binder in the TYK2 demo was **checked
  by FEP** before being believed. That's the same [prove-it discipline](/post/newsletter-2026-07-27/)
  the lab keeps insisting on — a predicted complex, like a generated stain or a virtual cell,
  earns trust only when validated against physics or experiment.

## Lab connections (for "why it matters")
- **human-cell-simulator** — interactions + affinities are the wiring/weights a virtual cell needs.
- **autonomous-research-agents** — fast affinity → practical in-silico screening / design loops.
- **Aug 3 small-molecule design** — generative design (propose) + co-folding affinity (score) = full loop.
- **Aug 11 dynamics / Jul 23–25 design** — parts → motion → interactions; and prediction vs design.
- **bioimage-model-zoo / bioengine** — open, fine-tunable models, now for molecular interactions.
- **prove-it (Jul 27)** — affinity is a hypothesis; validate with FEP/experiment; antibodies still lag.

## De-dup check
- Recent digests: Aug 11 protein dynamics; Aug 10 optical pooled screening; Aug 9 genome FMs;
  Aug 8 smart microscopy; Aug 7 proteomics; Aug 6 virtual staining; Aug 5 federated; Aug 4
  profiling; Aug 3 small-molecule design; Aug 2 virtual cell; Aug 1 prove-it/pathology; Jul 31
  self-driving labs; Jul 30 RNA; Jul 29 cryo-ET; Jul 28 genomic-FM eval; Jul 27 prove-it;
  Jul 25 binder design; Jul 23 protein design. **Molecular complex prediction (co-folding) +
  binding affinity has not been a digest theme.** Distinct object (complex vs single chain/
  cell/genome) and axis (affinity/interaction). Clear to run.
