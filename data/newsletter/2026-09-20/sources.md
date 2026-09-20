# Newsletter sources — 2026-09-20

Theme: **AI for immune recognition** — predicting which peptides are *presented* on
MHC molecules and which T-cell receptors (TCRs) *recognize* them. This is the T-cell
arm of adaptive immunity, distinct from Sep 16 (antibody/B-cell design). Central to
cancer immunotherapy (neoantigens), vaccines, and autoimmunity. Distinct from Sep 2
(protein function), Sep 5 (protein design), Sep 16 (antibodies), Sep 19 (structure
prediction): today is sequence→immune-recognition prediction (peptide–MHC + TCR–pMHC).

All six anchors verified via NCBI E-utilities (esearch DOI→PMID, efetch abstract XML).
Fetched 2026-09-20T03:00Z.

## Anchors (NCBI-verified; abstracts captured)

### Antigen presentation branch (which peptides are shown to T cells)
1. **NetMHCpan-4.1 and NetMHCIIpan-4.0: improved predictions of MHC antigen
   presentation ...** — Reynisson, Alvarez, Paul, Peters, Nielsen. *Nucleic Acids
   Research* (2020). DOI 10.1093/nar/gkaa379 | PMID 32406916.
   Why: the field-standard pan-allele predictor. MHC molecules "present peptides to T
   cells," and "the binding between MHC and antigenic peptides is the most selective
   step in the antigen presentation pathway" — so predicting it is foundational.

2. **MHCflurry 2.0: Improved Pan-Allele Prediction of MHC Class I-Presented Peptides by
   Incorporating Antigen Processing** — O'Donnell, Rubinsteyn, Laserson. *Cell Systems*
   (2020). DOI 10.1016/j.cels.2020.06.010 | PMID 32711842.
   Why: open-source; goes beyond binding to model "antigen processing steps that occur
   prior to MHC binding," trained on mass-spec-identified naturally presented ligands.

### T-cell recognition branch (which TCRs bind a given peptide–MHC)
3. **Quantifiable predictive features define epitope-specific T cell receptor
   repertoires** — Dash, Fiore-Gartland, ..., Thomas. *Nature* (2017).
   DOI 10.1038/nature22383 | PMID 28636592.
   Why: the TCRdist paper — TCRs that recognize the same epitope share "quantifiable
   predictive features," making TCR specificity partly learnable/predictable. The
   conceptual foundation for computational TCR–pMHC prediction.

4. **DeepTCR is a deep learning framework for revealing sequence concepts within T-cell
   repertoires** — Sidhom, Larman, Pardoll, Baras. *Nature Communications* (2021).
   DOI 10.1038/s41467-021-21879-w | PMID 33707415.
   Why: deep learning "to model highly complex TCR sequencing data by learning a joint
   representation of a TCR by its CDR3 sequences and V/D/J gene usage" — representation
   learning for immunogenomics.

5. **NetTCR-2.0 enables accurate prediction of TCR-peptide binding by using paired
   TCRα and β sequence data** — Montemurro, ..., Nielsen. *Communications Biology*
   (2021). DOI 10.1038/s42003-021-02610-3 | PMID 34508155.
   Why: sequence-based TCR–peptide binding predictor; notably candid that "current
   public bulk CDR3β-pMHC binding data overall is of low quality" and that progress
   hinges on paired α/β data — an honest lesson about data quality and benchmarking.

6. **Deep learning-based prediction of the T cell receptor-antigen binding specificity
   (pMTnet)** — Lu, ..., Wang. *Nature Machine Intelligence* (2021).
   DOI 10.1038/s42256-021-00383-2 | PMID 36003885.
   Why: transfer-learning model for TCR–neoantigen specificity, motivated by cancer —
   "neoantigens play a key role in the recognition of tumor cells by T cells ... only a
   small proportion of neoantigens truly elicit T cell responses." The clinical tie-in.

## Horizon radar (strategy note)
- Immune recognition is, at heart, a **representation-learning problem on biological
  sequences** — the same bet the lab makes with protein/genome language models and
  imaging foundation models. The recurring lesson (NetTCR-2.0, pMTnet) is that **data
  scarcity and quality**, not model class, gate progress — an argument for the lab's
  open-data / shared-benchmark ethos (BioImage Model Zoo, BioEngine).
- Neoantigen–TCR prediction is a direct line to **personalized cancer immunotherapy**;
  paired with spatial/tissue imaging it points toward *spatial immunology* — where a T
  cell meets its target, in situ — a natural fit for the lab's imaging platforms.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/discover` returns HTTP 402
  "Insufficient credits" (getxapi out of credits; ~43rd consecutive skip).
- Anchor verification: NCBI E-utilities (esearch→efetch); all six DOIs resolved to a
  PMID with matching title + abstract. Only verbatim quoted phrases are used in the post.
- Dedup: immune-recognition / TCR–pMHC / MHC-presentation prediction has NOT been a
  prior nightly theme (checked the full content/post/newsletter-* slug list). Distinct
  from Sep 16 (antibodies), Sep 2 (function), Sep 19 (structure).
- Also verified but not used (kept as backups): GLIPH2 (Huang, Nat Biotechnol 2020,
  10.1038/s41587-020-0505-4, PMID 32341563); ERGO (Springer, Front Immunol 2020,
  10.3389/fimmu.2020.01803, PMID 32983088).
