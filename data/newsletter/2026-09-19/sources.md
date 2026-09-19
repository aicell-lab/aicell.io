# Newsletter sources — 2026-09-19

Theme: **The protein structure-prediction revolution** — the leap from sequence to
3D structure (AlphaFold2, RoseTTAFold, ESMFold, AlphaFold3) and the open databases it
produced. This has been the *substrate* under many prior digests but never its own
subject. Distinct from Aug 11 (conformational *ensembles* built on top of AF), Aug 12
(co-folding of *complexes* + affinity), Sep 2 (protein *function* / dark proteome),
Sep 5 (de novo *design*), Sep 18 (subcellular *localization*): today is the core
monomer sequence→structure breakthrough and the infrastructure it created.

All six anchors verified via NCBI E-utilities (esearch DOI→PMID, efetch abstract XML).
Fetched 2026-09-19T03:00Z.

## Anchors (NCBI-verified; abstracts captured)

1. **Highly accurate protein structure prediction with AlphaFold**
   — Jumper, Evans, Pritzel, ..., Hassabis. *Nature* (2021).
   DOI 10.1038/s41586-021-03819-2 | PMID 34265844.
   Why: the breakthrough (CASP14, 2020). "Proteins are essential to life, and
   understanding their structure can facilitate a mechanistic understanding of their
   function." Sequence→atomic-accuracy structure, solving a ~50-year grand challenge.

2. **Accurate prediction of protein structures and interactions using a three-track
   neural network** — Baek, DiMaio, Anishchenko, ..., Baker. *Science* (2021).
   DOI 10.1126/science.abj8754 | PMID 34282049.
   Why: the open-source parallel (RoseTTAFold) — a "three-track network" fusing 1D
   sequence, 2D distance-map, 3D coordinate levels; "accuracies approaching those of
   DeepMind in CASP14"; makes protein-protein complexes "from sequence information
   alone, short-circuiting traditional approaches that require ... docking"; released
   to the community.

3. **Highly accurate protein structure prediction for the human proteome**
   — Tunyasuvunakool, Adler, ..., Hassabis. *Nature* (2021).
   DOI 10.1038/s41586-021-03828-1 | PMID 34293799.
   Why: the scale jump. "After decades of effort, 17% of the total residues in human
   protein sequences are covered by an experimentally determined structure" — AF2
   filled in the rest, folding a whole proteome.

4. **AlphaFold Protein Structure Database: massively expanding the structural coverage
   of protein-sequence space with high-accuracy models** — Varadi, Anyango, ...,
   Velankar. *Nucleic Acids Research* (2022). DOI 10.1093/nar/gkab1061 | PMID 34791371.
   Why: open data at scale. "Openly accessible" DB; "over 360,000 predicted structures
   across 21 model-organism proteomes, which will soon be expanded to cover most of the
   (over 100 million) representative sequences from the UniRef90 data set." The lab's
   open-infrastructure ethos, realised for structures.

5. **Evolutionary-scale prediction of atomic-level protein structure with a language
   model** — Lin, Akin, Rao, ..., Rives. *Science* (2023).
   DOI 10.1126/science.ade2574 | PMID 36927031.
   Why: the language-model route (ESMFold). "Direct inference of full atomic-level
   protein structure from primary sequence using a large language model," scaled to
   "15 billion parameters," an "order-of-magnitude acceleration" (no MSA) → the ESM
   Metagenomic Atlas of ">617 million metagenomic protein sequences."

6. **Accurate structure prediction of biomolecular interactions with AlphaFold 3**
   — Abramson, Adler, Dunger, ..., Jumper. *Nature* (2024).
   DOI 10.1038/s41586-024-07487-w | PMID 38718835.
   Why: beyond the monomer — AF3 predicts complexes spanning proteins, nucleic acids,
   ligands and ions in one unified model. Structure prediction becomes a general
   biomolecular-interaction engine. (PubMed abstract is truncated; only the verified
   title is quoted verbatim.)

## Horizon radar (strategy note)
- Structure prediction is now a *solved-enough* primitive that the frontier has moved
  to what you *do* with a structure: function, complexes, dynamics, design, and
  ultimately the **virtual cell**. A cell model that reasons mechanistically needs the
  structures of its parts — AF/ESM give a first draft of nearly all of them, at
  proteome/metagenome scale. This is why "predict-then-reason" (structure as a learned
  substrate) keeps recurring across the lab's radar.
- Open weights + open databases (RoseTTAFold, ESMFold, AlphaFold DB) are the same
  publish-the-model/publish-the-data pattern behind BioImage Model Zoo + BioEngine.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/discover` returns HTTP 402
  "Insufficient credits" (getxapi out of credits; ~42nd consecutive skip).
- Anchor verification: NCBI E-utilities (esearch→efetch); all six DOIs resolved to a
  PMID with matching title + abstract. Only verbatim quoted phrases are used in the post.
- Dedup: the core sequence→structure prediction breakthrough has NOT been a prior
  nightly theme (checked the full content/post/newsletter-* slug list). Distinct from
  Aug 11 / Aug 12 / Sep 2 / Sep 5 / Sep 18.
