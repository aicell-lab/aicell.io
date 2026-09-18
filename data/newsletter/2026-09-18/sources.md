# Newsletter sources — 2026-09-18

Theme: **Predicting protein subcellular localization** — where in the cell a protein
lives, from its sequence and from microscopy images. Deeply lab-core: the field grew
out of the Human Protein Atlas (HPA) Cell Atlas, which the lab's own work helped build.
Distinct from Sep 2 (protein *function* prediction / dark proteome), Aug 4 (morphological
profiling / Cell Painting), Aug 16 (segmentation), Sep 15 (registration): this is about
the spatial *address* of the proteome.

All six anchors verified via NCBI E-utilities (esearch DOI→PMID, efetch abstract XML).
Fetched 2026-09-18T03:00Z.

## Anchors (NCBI-verified; abstracts captured)

### Sequence-based branch
1. **DeepLoc: prediction of protein subcellular localization using deep learning**
   — Almagro Armenteros, Sønderby, Sønderby, Nielsen, Winther. *Bioinformatics* (2017).
   DOI 10.1093/bioinformatics/btx431 | PMID 29036616.
   Why: founding move — an RNN + attention predicting localization "relying only on
   sequence information," no homology needed → works for novel proteins and variants.

2. **Light attention predicts protein location from the language of life**
   — Stärk, Dallago, Heinzinger, Rost. *Bioinformatics Advances* (2021).
   DOI 10.1093/bioadv/vbab035 | PMID 36700108.
   Why: protein-language-model embeddings replace expensive MSAs; a "light attention"
   head beats the prior SOTA "by about 8 percentage points (Q10)." The PLM era arrives.

3. **DeepLoc 2.0: multi-label subcellular localization prediction using protein
   language models** — Thumuluri, Almagro Armenteros, Johansen, Nielsen, Winther.
   *Nucleic Acids Research* (2022). DOI 10.1093/nar/gkac278 | PMID 35489069.
   Why: multi-location prediction + interpretability (attention along the sequence, plus
   accurate prediction of nine protein sorting-signal types); PLM-based SOTA, sequence-only.

### Image-based branch (Human Protein Atlas / cell imaging — the lab's home turf)
4. **Deep learning is combined with massive-scale citizen science to improve large-scale
   image classification** — Sullivan, Winsnes, ..., Lundberg. *Nature Biotechnology* (2018).
   DOI 10.1038/nbt.4225 | PMID 30125267.
   Why: HPA Cell Atlas images classified via a mini-game in EVE Online (Project Discovery)
   — 322,006 gamers, ~33M classifications — plus a deep-learning Loc-CAT across 29 patterns.
   The lab's HPA lineage; open-science + community at planetary scale.

5. **Analysis of the Human Protein Atlas Image Classification competition**
   — Ouyang, Winsnes, ..., Lundberg. *Nature Methods* (2019).
   DOI 10.1038/s41592-019-0658-6 | PMID 31780840.
   Why: lab-authored (W. Ouyang). A Kaggle challenge on HPA images — 2,172 teams,
   imbalanced multi-label — whose winning models beat the prior HPA effort by ~20% and
   double as classifiers, feature extractors, and pretrained nets. A community benchmark.

6. **Self-supervised deep learning encodes high-resolution features of protein
   subcellular localization (cytoself)** — Kobayashi, Cheveralls, Leonetti, Royer.
   *Nature Methods* (2022). DOI 10.1038/s41592-022-01541-z | PMID 35879608.
   Why: fully self-supervised localization profiling on 1,311 OpenCell proteins → a
   localization atlas from coarse classes to individual protein-complex signatures, with
   no annotations. Representation learning meets the spatial proteome.

## Horizon radar (strategy note)
- Subcellular localization is a load-bearing layer for the **virtual cell**: a faithful
  cell model must know not just which proteins exist but *where* they sit and how that
  shifts with state. cytoself's self-supervised atlas is exactly the kind of learned
  spatial representation such a model needs — ties to the lab's human-cell-simulator.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/discover` returns HTTP 402
  "Insufficient credits" (getxapi out of credits; ~41st consecutive skip).
- Anchor verification: NCBI E-utilities (esearch→efetch); all six DOIs resolved to a PMID
  with matching title + abstract. Only verbatim quoted phrases used in the post.
- Dedup: subcellular-localization prediction has NOT been a prior nightly theme (checked the
  full content/post/newsletter-* slug list). Distinct from Sep 2 / Aug 4 / Aug 16 / Sep 15.
- Note on lab-authored anchors (#4, #5): cited neutrally as seminal, published field
  milestones; the post is authored by Happy Agent, not re-attributed to those authors.
