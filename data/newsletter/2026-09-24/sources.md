# Newsletter sources — 2026-09-24

Theme: **Will this molecule bind?** — deep-learning scoring functions and
binding-affinity prediction for structure-based **virtual screening**. Given a
protein target and a library of candidate molecules, learn to rank which ones bind
(and how tightly) fast enough to triage millions of compounds. Covers the two main
routes: **3D structure-based** scoring (CNNs on the protein–ligand complex) and
**sequence/graph-based** drug–target affinity (no 3D structure needed).

This is a deliberate gap-fill: on Sep 19 (protein structure) we noted docking/scoring
was deferred because the headline pose-prediction papers (DiffDock/EquiBind) are
arXiv-only; today's anchors are all peer-reviewed and PubMed-indexed. Distinct from
Aug 3 (de novo *generation* of molecules), Aug 12 (co-folding a *given* complex +
affinity from structure prediction), Sep 10 (antibiotic discovery), Sep 21 (drug
*response* in cancer cells). Today = the *screening/scoring* engine that ranks
candidates against a target.

All six anchors verified via NCBI E-utilities (esearch DOI→PMID, efetch abstract
XML). Fetched 2026-09-24T03:01Z. Only verbatim quoted phrases are used in the post.

## Anchors (NCBI-verified; abstracts captured)

### Structure-based (3D CNN on the protein–ligand complex)
1. **Protein-Ligand Scoring with Convolutional Neural Networks (gnina/CNN scoring)**
   — Ragoza, Hochuli, Idrobo, Sunseri, Koes. *J Chem Inf Model* (2017).
   DOI 10.1021/acs.jcim.6b00740 | PMID 28368587.
   Why: the founding CNN scoring paper — "a comprehensive three-dimensional (3D)
   representation of a protein-ligand interaction" learned by CNN, which
   "outperforms the AutoDock Vina scoring function when ranking poses both for pose
   prediction and virtual screening."

2. **KDEEP: Protein-Ligand Absolute Binding Affinity Prediction via 3D-Convolutional
   Neural Networks** — Jiménez, Škalič, Martínez-Rosell, De Fabritiis. *J Chem Inf
   Model* (2018). DOI 10.1021/acs.jcim.7b00650 | PMID 29309725.
   Why: fast, accurate absolute-affinity prediction — "state-of-the-art" on PDBbind
   core (Pearson 0.82) with "each prediction taking a fraction of a second"; also
   candid that "accuracy is still very sensitive to the specific protein used."

3. **Development and evaluation of a deep learning model for protein-ligand binding
   affinity prediction (Pafnucy)** — Stępniewska-Dziubińska, Zielenkiewicz,
   Siedlecki. *Bioinformatics* (2018). DOI 10.1093/bioinformatics/bty374 |
   PMID 29757353.
   Why: represents the complex "with a 3D grid" and uses "a 3D convolution … treating
   the atoms of both proteins and ligands in the same manner"; open-source; beat
   classical scoring functions on CASF-2013 and the Astex Diverse Set.

4. **OnionNet: a Multiple-Layer Intermolecular-Contact-Based Convolutional Neural
   Network for Protein-Ligand Binding Affinity Prediction** — Zheng, Fan, Mu.
   *ACS Omega* (2019). DOI 10.1021/acsomega.9b01997 | PMID 31592466.
   Why: contact-based features "grouped into different distance ranges to cover both
   the local and nonlocal interaction information," and — importantly for screening —
   robust when scoring "complexes generated from docking simulations instead of
   experimentally determined PDB structures."

### Sequence / graph-based (drug–target affinity, no 3D structure)
5. **DeepDTA: deep drug-target binding affinity prediction** — Öztürk, Özgür,
   Ozkirimli. *Bioinformatics* (2018). DOI 10.1093/bioinformatics/bty593 |
   PMID 30423097.
   Why: predicts a *continuum* of affinity "using only sequence information of both
   targets and drugs" via CNNs on 1D representations — no 3D structure required —
   framing that "protein-ligand interactions assume a continuum of binding strength
   values … and predicting this value still remains a challenge."

6. **GraphDTA: predicting drug-target binding affinity with graph neural networks**
   — Nguyen, Le, Quinn, Nguyen, Le, Venkatesh. *Bioinformatics* (2021).
   DOI 10.1093/bioinformatics/btaa921 | PMID 33119053.
   Why: represents "drugs as graphs and uses graph neural networks," arguing strings
   are "not a natural way to represent molecules"; motivated by **drug repurposing**
   ("finding new uses for already approved drugs"). Molecular graphs, the same
   representation behind the lab's [drug-design] and drug-response digests.

## Horizon radar (strategy note)
- Virtual screening is one leg of the AI-for-discovery loop the lab cares about:
  **generate** candidates (Aug 3) → **score/screen** against a target (today) →
  **predict response** in cells (Sep 21). Learned scoring functions are the fast
  triage that makes screening large libraries tractable.
- Recurring caveat across all six: **generalization**. KDEEP's "accuracy is still
  very sensitive to the specific protein," OnionNet's stress-test on docked (not
  crystal) poses — the field's real bottleneck is honest benchmarks and out-of-
  distribution targets, not raw correlation on PDBbind. An argument for the lab's
  open-benchmark / shared-infrastructure stance.
- Two representational routes (3D-grid CNNs vs. sequence/graph nets) mirror a theme
  the lab returns to: when structure is available, use it; when it isn't, learn from
  sequence — the same trade-off seen in protein structure prediction.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/search/discover` returns
  HTTP 402 "Insufficient credits" (getxapi out of credits; ~47th consecutive skip;
  Grok-based replacement wired, awaiting a credit decision).
- Anchor verification: NCBI E-utilities (esearch→efetch); all six DOIs resolved to a
  PMID with matching title + abstract. Only verbatim quoted phrases are used.
- Dedup: DL scoring / binding-affinity for virtual screening has NOT been a prior
  nightly theme (checked the full content/post/newsletter-* slug list). Distinct from
  Aug 3, Aug 12, Sep 10, Sep 21.
