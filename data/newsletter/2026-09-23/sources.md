# Newsletter sources — 2026-09-23

Theme: **Teaching machines to name cells** — automated cell-type annotation and
reference atlases in single-cell biology. From the vision of a complete catalogue
of human cell types, to the reference atlases that realize it, to the ML methods
that annotate a new dataset by reference instead of by hand. This is the *data
foundation* under the virtual cell: you cannot model, or simulate, a cell you
cannot first name.

Distinct from prior nightly themes: Aug 15 (single-cell foundation models /
*perturbation* prediction), Sep 3 (single-cell multi-omics *integration* — fusing
modalities), Aug 27 (RNA velocity / cell-state dynamics), Aug 13 (spatial
transcriptomics methods). Today is specifically the **annotation / cell-typing /
reference-mapping** task.

All six anchors verified via NCBI E-utilities (esearch DOI→PMID, efetch abstract
XML). Fetched 2026-09-23T03:00Z. Only verbatim quoted phrases are used in the post.

## Anchors (NCBI-verified; abstracts captured)

1. **The Human Cell Atlas** — Regev, Teichmann, Lander, ..., Human Cell Atlas
   Meeting Participants. *eLife* (2017). DOI 10.7554/eLife.27041 | PMID 29206104.
   Why: the vision. "The time is ripe to complete the 150-year-old effort to
   identify all cell types in the human body," aiming "to define all human cell
   types in terms of distinctive molecular profiles" with "a commitment to open
   data, code, and community." The north star for cell-typing.

2. **The Tabula Sapiens: A multiple-organ, single-cell transcriptomic atlas of
   humans** — The Tabula Sapiens Consortium. *Science* (2022).
   DOI 10.1126/science.abl4896 | PMID 35549404.
   Why: a concrete reference atlas — "a human reference atlas comprising nearly
   500,000 cells from 24 different tissues and organs," enabling "molecular
   characterization of more than 400 cell types." The reference that annotation
   methods map onto.

3. **Reference-based analysis of lung single-cell sequencing reveals a transitional
   profibrotic macrophage (SingleR)** — Aran, Looney, ..., Bhattacharya. *Nature
   Immunology* (2019). DOI 10.1038/s41590-018-0276-y | PMID 30643263.
   Why: an early, influential automated annotator — "a novel computational
   framework for the annotation of scRNA-seq by reference to bulk transcriptomes
   (SingleR)" — and a case where automated typing revealed a real, disease-relevant
   cell subgroup ("a disease-associated subgroup with a transitional gene expression
   profile").

4. **Cross-tissue immune cell analysis reveals tissue-specific features in humans
   (CellTypist)** — Domínguez Conde, Xu, ..., Teichmann. *Science* (2022).
   DOI 10.1126/science.abl5197 | PMID 35549406.
   Why: a modern, scalable annotator — "CellTypist, a machine learning tool for
   rapid and precise cell type annotation" — built to "systematically resolve immune
   cell heterogeneity across tissues" by "leveraging a common reference dataset."

5. **Probabilistic harmonization and annotation of single-cell transcriptomics data
   with deep generative models (scANVI)** — Xu, Lopez, ..., Yosef. *Molecular
   Systems Biology* (2021). DOI 10.15252/msb.20209620 | PMID 33491336.
   Why: the deep-generative route. Names the goal — "to achieve a common ontology of
   cell types and states" and "to automatically assign cell type labels in a new
   dataset based on existing annotations" — and introduces "single-cell ANnotation
   using Variational Inference (scANVI), a semi-supervised variant of scVI designed
   to leverage existing cell state annotations."

6. **Mapping single-cell data to reference atlases by transfer learning (scArches)**
   — Lotfollahi, Naghipourfar, ..., Theis. *Nature Biotechnology* (2022).
   DOI 10.1038/s41587-021-01001-7 | PMID 34462589.
   Why: query-to-reference mapping as transfer learning — "single-cell architectural
   surgery (scArches)" maps new datasets "on top of a reference" "without sharing
   raw data," and even "retains coronavirus disease 2019 (COVID-19) disease variation
   when mapping to a healthy reference, enabling the discovery of disease-specific
   cell states." Federated, privacy-aware atlas building.

## Horizon radar (strategy note)
- Cell-type annotation is the **labeling layer of the virtual cell**: the lab's
  human-cell-simulator needs a shared, machine-readable ontology of cell states
  before it can model transitions between them. Reference atlases (HCA, Tabula
  Sapiens) are that substrate.
- scArches' "map without sharing raw data" is the same **privacy-preserving,
  decentralized** principle behind the lab's Safe Colab and BioEngine — reference
  models as shareable public goods while primary data stays local.
- The open-reference + open-tool pattern (HCA's "open data, code, and community";
  scvi-tools; CellTypist) mirrors the lab's BioImage Model Zoo / BioEngine ethos:
  shared references beat every-lab-reinvents-the-wheel.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/search/discover` returns
  HTTP 402 "Insufficient credits" (getxapi out of credits; ~46th consecutive skip;
  a Grok-based replacement is wired, awaiting a credit decision).
- Anchor verification: NCBI E-utilities (esearch→efetch); all six DOIs resolved to a
  PMID with matching title + abstract. Only verbatim quoted phrases are used.
- Dedup: cell-type annotation / reference-atlas mapping has NOT been a prior nightly
  theme (checked the full content/post/newsletter-* slug list). Distinct from Aug 15,
  Sep 3, Aug 27, Aug 13.
- Note: the Sept 22 nightly slot was missed (session idle); this is the Sept 23 run
  on the real current UTC date.
