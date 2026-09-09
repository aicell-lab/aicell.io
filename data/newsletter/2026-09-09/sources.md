# Newsletter sources — September 9, 2026

**Theme:** **Machine-learned interatomic potentials / ML force fields** — neural networks that learn the
*potential-energy surface* (energies + forces on every atom) from quantum-mechanical reference data, so
molecular dynamics can run at near-DFT accuracy but at classical-force-field speed. The physics-simulation
substrate under proteins, ligands and materials. "Quantum Accuracy, Classical Speed." The arc: the founding
NN-potential idea (Behler–Parrinello) → a transferable potential across organic chemical space (ANI-1) →
deep architectures for quantum interactions (SchNet) → ab-initio-accuracy MD at scale (DeePMD) →
equivariance buys extreme data efficiency (NequIP) → the synthesis and prove-it guide (Unke et al. review).

**Dedup guard:** Distinct from Aug 11 ("After the Fold, the Motion" — generative models that *emulate the
equilibrium ensemble* / amortize MD *outputs*, e.g. BioEmu; today is about learning the *energy & forces to
run* the simulation itself, faster and at quantum accuracy). Distinct from Aug 12 (co-folding / complex +
binding-affinity prediction), Aug 31 (cryo-EM conformational heterogeneity — experimental snapshots), Sep 5
(de novo protein *design*), Sep 8 (protein *engineering* / directed evolution — sequence→fitness, not
atomistic forces). MD has only ever appeared here as an aside ("the slow physics tool ML emulates"); this
is its own foundational day. The unifying object is the **learned potential-energy surface**.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on `monitor` (min-likes 30,
since-hours 24). ~32nd consecutive skip (>five weeks). Grok replacement wired, awaiting xAI credits.

All 6 anchors verified against **raw Europe PMC `abstractText` JSON** (fetched directly via curl — no
summarizer), with DOI/title/author/journal/year confirmed. Only abstract-verified verbatim quotes used.

---

## Framing / origin — a neural network for the potential-energy surface

### Behler & Parrinello — generalized NN representation of PES — VERIFIED
- Behler J, Parrinello M. "Generalized neural-network representation of high-dimensional potential-energy
  surfaces." *Physical Review Letters* 98:146401, 2007. DOI 10.1103/PhysRevLett.98.146401.
- ABSTRACT-VERIFIED (verbatim): "**The accurate description of chemical processes often requires the use of
  computationally demanding methods like density-functional theory (DFT), making long simulations of large
  systems unfeasible.**"; "**we introduce a new kind of neural-network representation of DFT potential-
  energy surfaces, which provides the energy and forces as a function of all atomic positions in systems of
  arbitrary size and is several orders of magnitude faster than DFT.**"; "**The method is general and can be
  applied to all types of periodic and nonperiodic systems.**"
- USE: the founding idea — a NN that maps atomic positions → energy + forces, orders of magnitude faster
  than DFT, any system size. Sets up the whole field and the "quantum accuracy, classical speed" trade.

## Section 1 — Transferable across chemical space

### ANI-1 (Smith, Isayev & Roitberg) — VERIFIED
- Smith JS, Isayev O, Roitberg AE. "ANI-1: an extensible neural network potential with DFT accuracy at
  force field computational cost." *Chemical Science* 8:3192–3203, 2017. DOI 10.1039/c6sc05720a.
- ABSTRACT-VERIFIED (verbatim): "**we demonstrate how a deep neural network (NN) trained on quantum
  mechanical (QM) DFT calculations can learn an accurate and transferable potential for organic
  molecules.**"; "**AEVs provide the ability to train neural networks to data that spans both configurational
  and conformational space, a feat not previously accomplished on this scale.**"; "**ANI-1 is chemically
  accurate compared to reference DFT calculations on much larger molecular systems (up to 54 atoms) than
  those included in the training data set.**"
- USE: the title itself is the thesis — "DFT accuracy at force field computational cost." Transferability:
  train on small molecules (≤8 heavy atoms), predict much larger ones. Builds on Behler–Parrinello symmetry
  functions.

## Section 2 — Deep architectures for quantum interactions

### SchNet (Schütt et al.) — VERIFIED
- Schütt KT, Sauceda HE, Kindermans PJ, Tkatchenko A, Müller KR. "SchNet — a deep learning architecture for
  molecules and materials." *Journal of Chemical Physics* 148:241722, 2018. DOI 10.1063/1.5019779.
- ABSTRACT-VERIFIED (verbatim): "**Machine learning, in general, and deep learning, in particular, are
  ideally suitable for representing quantum-mechanical interactions, enabling us to model nonlinear
  potential-energy surfaces or enhancing the exploration of chemical compound space.**"; "**we present the
  deep learning architecture SchNet that is specifically designed to model atomistic systems by making use
  of continuous-filter convolutional layers.**"; "**we employ SchNet to predict potential-energy surfaces
  and energy-conserving force fields for molecular dynamics simulations of small molecules**" and study
  C20-fullerene properties "**that would have been infeasible with regular ab initio molecular dynamics.**"
- USE: the deep-learning turn — continuous-filter convolutions purpose-built for atoms; energy-conserving
  force fields for MD; learns chemically plausible atom embeddings across the periodic table.

## Section 3 — Ab-initio-accuracy MD at scale

### DeePMD (Zhang, Han, Wang, Car & E) — VERIFIED
- Zhang L, Han J, Wang H, Car R, E W. "Deep Potential Molecular Dynamics: a scalable model with the accuracy
  of quantum mechanics." *Physical Review Letters* 120:143001, 2018. DOI 10.1103/PhysRevLett.120.143001.
- ABSTRACT-VERIFIED (verbatim): "**We introduce a scheme for molecular simulations, the deep potential
  molecular dynamics (DPMD) method, based on a many-body potential and interatomic forces generated by a
  carefully crafted deep neural network trained with ab initio data.**"; "**The neural network model
  preserves all the natural symmetries in the problem.**"; "**DPMD gives results that are essentially
  indistinguishable from the original data, at a cost that scales linearly with system size.**"
- USE: the scaling story — quantum-accurate MD whose cost scales *linearly* with system size; symmetry-
  preserving; "essentially indistinguishable" from the ab initio data. The path to large, long simulations.

## Section 4 — Equivariance = data efficiency

### NequIP (Batzner et al.) — VERIFIED
- Batzner S, Musaelian A, Sun L, … Kozinsky B. "E(3)-equivariant graph neural networks for data-efficient
  and accurate interatomic potentials." *Nature Communications* 13:2453, 2022. DOI
  10.1038/s41467-022-29939-5.
- ABSTRACT-VERIFIED (verbatim): "**NequIP employs E(3)-equivariant convolutions for interactions of
  geometric tensors, resulting in a more information-rich and faithful representation of atomic
  environments.**"; "**The method achieves state-of-the-art accuracy on a challenging and diverse set of
  molecules and materials while exhibiting remarkable data efficiency.**"; "**NequIP outperforms existing
  models with up to three orders of magnitude fewer training data, challenging the widely held belief that
  deep neural networks require massive training sets.**"
- USE: the modern SOTA move — build the symmetries of 3D space (E(3) equivariance) into the network, and it
  learns from up to 1000× less data. Data efficiency matters because quantum reference data is expensive.

## Section 5 — The synthesis + prove-it guide

### Unke et al. — Machine Learning Force Fields (review) — VERIFIED
- Unke OT, Chmiela S, Sauceda HE, Gastegger M, Poltavsky I, Schütt KT, Tkatchenko A, Müller KR. "Machine
  Learning Force Fields." *Chemical Reviews* 121:10142–10186, 2021. DOI 10.1021/acs.chemrev.0c01111.
- ABSTRACT-VERIFIED (verbatim): "**One of the most promising applications is the construction of ML-based
  force fields (FFs), with the aim to narrow the gap between the accuracy of ab initio methods and the
  efficiency of classical FFs.**"; "**The key idea is to learn the statistical relation between chemical
  structure and potential energy without relying on a preconceived notion of fixed chemical bonds or
  knowledge about the relevant interactions.**"; "**a step-by-step guide for constructing and testing them
  from scratch is given.**"
- USE: the synthesis — states the field's whole aim (accuracy of ab initio, efficiency of classical FFs),
  the no-preconceived-bonds philosophy, and — importantly for us — a build-and-*test* guide (prove-it
  discipline).

## Section 6 — Lab hook + horizon
- This is the **physics-simulation substrate** beneath much of what the digest covers. Aug 11 showed
  generative models that *emulate* a protein's equilibrium ensemble; ML force fields attack the same motion
  problem from underneath — learn the energy landscape so you can *run* the dynamics at quantum accuracy.
  Structure (AlphaFold, Sep-2/Aug-12), motion (Aug 11), and now the *forces* that drive the motion.
- The [virtual cell / Human Cell Simulator](/project/human-cell-simulator/) needs exactly this: to simulate
  a pathway or a drug binding you need forces you can trust at a cost you can afford. Linear-scaling,
  quantum-accurate MD (DeePMD) is a concrete rung toward biomolecular-scale simulation.
- Ties to [structure-based drug design](/post/newsletter-2026-08-03/) and
  [binding affinity](/post/newsletter-2026-08-12/): better forces → better free-energy and binding
  estimates. And to [self-driving labs](/post/newsletter-2026-08-21/): a fast, accurate simulator is the
  in-silico half of a design–build–test–learn loop.
- Open, benchmarked ethos: SchNet, DeePMD, NequIP are open source; MD17/QM9-style datasets and the Unke et
  al. build-and-test guide are the public yardsticks — the same publish-the-model-*and*-the-test spirit
  behind the BioImage Model Zoo (/project/bioimage-model-zoo/) + BioEngine (/project/bioengine/) and the
  recurring [benchmark discipline](/post/newsletter-2026-07-27/). A force field you can call like a service,
  scored on a shared dataset.
