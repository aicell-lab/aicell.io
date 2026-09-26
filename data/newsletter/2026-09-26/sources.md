# Newsletter sources — 2026-09-26

Theme: **Mapping the cell's wiring** — AI for protein–protein interaction (PPI) and
protein-complex prediction at proteome scale (the interactome). A cell is not a bag
of parts but a *network* of interacting proteins; discovering that network — which
proteins touch, and what machines they build — is a building block of the virtual
cell. Covers the reference database, the coevolution signal, sequence-based deep
learning predictors, network-aware models, and structure-based (AlphaFold/RoseTTAFold)
complex prediction.

Distinct from Aug 12 (co-folding / affinity for a *given* pair — predicting one
complex's structure) and Sep 19 (single-chain structure prediction). Today is
**discovering the interaction network itself, at scale.** Local angle: two anchors
are from the Elofsson group at Stockholm University / SciLifeLab (Bryant et al.),
close collaborators' territory.

All six anchors verified via NCBI E-utilities (esearch DOI→PMID, efetch abstract
XML). Fetched 2026-09-26T03:01Z. Only verbatim quoted phrases are used in the post.

## Anchors (NCBI-verified; abstracts captured)

1. **STRING v11: protein-protein association networks …** — Szklarczyk, Gable, ...,
   von Mering. *Nucleic Acids Research* (2019). DOI 10.1093/nar/gky1131 |
   PMID 30476243.
   Why: the reference map. "Proteins and their functional interactions form the
   backbone of the cellular machinery," and STRING aims "to achieve a comprehensive
   and objective global network, including direct (physical) as well as indirect
   (functional) interactions" — now across "5090" organisms. The atlas of the
   interactome that everything else is measured against.

2. **Protein interaction networks revealed by proteome coevolution** — Cong,
   Anishchenko, Ovchinnikov, Baker. *Science* (2019). DOI 10.1126/science.aaw6718 |
   PMID 31296772.
   Why: a physical signal for interaction. Using "coevolution between 5.4 million
   pairs of proteins in Escherichia coli" (and 3.9M in M. tuberculosis) plus
   structure modeling, they "predict protein-protein interactions (PPIs) with an
   accuracy that benchmark studies suggest is considerably higher than that of
   proteome-wide two-hybrid and mass spectrometry screens," finding "hundreds of
   previously uncharacterized PPIs."

3. **D-SCRIPT translates genome to phenome with sequence-based, structure-aware,
   genome-scale predictions of protein-protein interactions** — Sledzieski, Singh,
   Cowen, Berger. *Cell Systems* (2021). DOI 10.1016/j.cels.2021.08.010 |
   PMID 34536380.
   Why: deep learning from sequence alone. "An interpretable and generalizable
   deep-learning model, which predicts interaction between two proteins using only
   their sequence and maintains high accuracy with limited training data and across
   species" — the "inter-protein contact map … has significant overlap with the
   ground truth," and it scales to non-model organisms ("genome-to-phenome").

4. **Topsy-Turvy: integrating a global view into sequence-based PPI prediction** —
   Singh, Devkota, ..., Berger. *Bioinformatics* (2022).
   DOI 10.1093/bioinformatics/btac258 | PMID 35758793.
   Why: fuse "bottom-up" sequence features with "top-down" network patterns via
   transfer learning; "genome-scale, interpretable PPI prediction for non-model
   organisms with no existing experimental PPI data," and — key for scale — "running
   Topsy-Turvy … screens is feasible for whole genomes, and thus these methods scale
   to settings where other methods (e.g. AlphaFold-Multimer) might be infeasible."

5. **Improved prediction of protein-protein interactions using AlphaFold2** —
   Bryant, Pozzati, Elofsson. *Nature Communications* (2022).
   DOI 10.1038/s41467-022-28865-w | PMID 35273146. *(Stockholm Univ / SciLifeLab)*
   Why: structure-based PPI. Applying "AlphaFold2 for the prediction of heterodimeric
   protein complexes … together with optimised multiple sequence alignments" gives
   "models with acceptable quality (DockQ ≥ 0.23) for 63% of the dimers," and a
   predicted-DockQ score distinguishes "interacting from non-interacting proteins
   with state-of-art accuracy" — identifying "51% of all interacting pairs at 1% FPR."

6. **Computed structures of core eukaryotic protein complexes** — Humphreys, Pei,
   ..., Baker. *Science* (2021). DOI 10.1126/science.abm4805 | PMID 34762488.
   Why: the proteome-scale payoff. Combining "proteome-wide amino acid coevolution
   analysis and deep-learning–based structure modeling" (RoseTTAFold + AlphaFold),
   they screen "8.3 million pairs of yeast proteins, identify 1505 likely to
   interact, and build structure models for 106 previously unidentified assemblies
   and 806 that have not been structurally characterized" — complexes touching
   "almost all key processes in eukaryotic cells."

## Horizon radar (strategy note)
- The interactome is a core layer of the **virtual cell**: to simulate a cell you
  need its wiring diagram — which proteins interact, and the machines they assemble.
  This is the network substrate under the lab's human-cell-simulator.
- A recurring tension: **structure-based (AlphaFold/RoseTTAFold) vs. sequence/
  network-based** methods. The former is accurate but heavy; the latter (D-SCRIPT,
  Topsy-Turvy) scales to whole genomes and non-model species where AlphaFold-Multimer
  is infeasible. The lab's infrastructure bet (BioEngine) is exactly about making the
  heavy methods runnable at scale.
- Open reference resources (STRING) mirror the lab's open-data ethos (BioImage Model
  Zoo, BioEngine) — shared maps beat private ones.
- Local angle: Bryant & Elofsson (Stockholm Univ / SciLifeLab) — AI-for-structure
  work in the lab's own backyard.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/search/discover` returns
  HTTP 402 "Insufficient credits" (getxapi out of credits; ~49th consecutive skip;
  Grok-based replacement wired, awaiting a credit decision).
- Anchor verification: NCBI E-utilities; all six DOIs resolved to a PMID with matching
  title + abstract. Only verbatim quoted phrases are used.
- Dedup: proteome-scale PPI / interactome prediction has NOT been a prior nightly
  theme (checked the full content/post/newsletter-* slug list). Distinct from Aug 12
  (co-folding a given pair), Sep 19 (single-chain structure), Sep 11 (biomedical
  knowledge graphs — different kind of network).
