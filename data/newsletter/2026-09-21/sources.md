# Newsletter sources — 2026-09-21

Theme: **Deep learning for cancer drug-response prediction (precision oncology)** —
predicting whether/how much a tumor will respond to a drug from its molecular profile
(mutations, copy number, expression, methylation) plus the drug's chemical structure.
A pivot away from the recent protein-structure/immunity run toward phenotype/response
prediction. Distinct from Sep 3 (multi-omics *integration* per se), Aug 15 (single-cell
FMs / *transcriptomic* perturbation prediction), Sep 11 (biomedical knowledge graphs):
today is the specific task of predicting *drug sensitivity* (IC50 / response) in cancer.

All six anchors verified via NCBI E-utilities (esearch DOI→PMID, efetch abstract XML).
Fetched 2026-09-21T03:00Z.

## Anchors (NCBI-verified; abstracts captured)

1. **A Landscape of Pharmacogenomic Interactions in Cancer** — Iorio, Knijnenburg, ...,
   Garnett. *Cell* (2016). DOI 10.1016/j.cell.2016.06.017 | PMID 27397505.
   Why: the data foundation (GDSC). Maps "cancer-driven alterations identified in 11,289
   tumors from 29 tissues" onto "1,001 molecularly annotated human cancer cell lines
   ... correlated with sensitivity to 265 drugs" — the resource nearly every predictor
   trains on, and the evidence that genotype partly encodes drug response.

2. **Cancer Drug Response profile scan (CDRscan): A Deep Learning Model That Predicts
   Drug Effectiveness from Cancer Genomic Signature** — Chang, ..., Shin.
   *Scientific Reports* (2018). DOI 10.1038/s41598-018-27214-6 | PMID 29891981.
   Why: an early move — a two-step convolutional model linking "genomic profiles of 787
   human cancer cell lines and structural profiles of 244 drugs" to responsiveness.

3. **Predicting drug response of tumors from integrated genomic profiles by deep neural
   networks (DeepDR)** — Chiu, ..., Chen, Chuang. *BMC Medical Genomics* (2019).
   DOI 10.1186/s12920-018-0460-9 | PMID 30704458.
   Why: integrates mutation + expression via deep nets, and is candid about the crux —
   "due to essential differences between cell lines and tumors, ... the translation into
   predicting drug response in tumors remains challenging." The cell-line→patient gap.

4. **MOLI: multi-omics late integration with deep neural networks for drug response
   prediction** — Sharifi-Noghabi, ..., Ester. *Bioinformatics* (2019).
   DOI 10.1093/bioinformatics/btz318 | PMID 31510700.
   Why: asks *how* to fuse omics. "Historically, gene expression has been shown to be
   the most informative data for drug response prediction," but late-integrating
   mutation/CNV/expression improves accuracy and clinical relevance.

5. **DeepCDR: a hybrid graph convolutional network for predicting cancer drug response**
   — Liu, Wei, Yang, Zeng. *Bioinformatics* (2020).
   DOI 10.1093/bioinformatics/btaa822 | PMID 33381841.
   Why: brings the *drug* into the model as a molecular graph — "integrates multi-omics
   profiles of cancer cells and explores intrinsic chemical structures of drugs" — so
   the model can generalize across both cells and compounds.

6. **Predicting Drug Response and Synergy Using a Deep Learning Model of Human Cancer
   Cells (DrugCell)** — Kuenzi, ..., Ideker. *Cancer Cell* (2020).
   DOI 10.1016/j.ccell.2020.09.014 | PMID 33096023.
   Why: the interpretable climax — "an interpretable deep learning model of human cancer
   cells trained on the responses of 1,235 tumor cell lines to 684 drugs," where "tumor
   genotypes induce states in cellular subsystems that are integrated with drug structure
   to predict response," and which extends to drug *synergy* (combinations). A "visible"
   network mirroring real cell biology — mechanistic ML, close to the lab's virtual-cell
   spirit.

## Horizon radar (strategy note)
- Drug-response prediction is a concrete instance of the **virtual cell** promise:
  given a cell's molecular state and a perturbation (a drug), predict the phenotype.
  DrugCell's "visible neural network" (structured to mirror cellular subsystems) is
  exactly the mechanistic-plus-learned hybrid the lab's human-cell-simulator envisions.
- The recurring blocker is **generalization from cell lines to patients** (DeepDR,
  Sakellaropoulos): a data/benchmark problem, not only a model problem — an argument for
  the lab's open-data / shared-benchmark stance.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/discover` returns HTTP 402
  "Insufficient credits" (getxapi out of credits; ~44th consecutive skip).
- Anchor verification: NCBI E-utilities (esearch→efetch); all six DOIs resolved to a
  PMID with matching title + abstract. Only verbatim quoted phrases are used in the post.
- Dedup: cancer drug-response / sensitivity prediction has NOT been a prior nightly
  theme (checked the full content/post/newsletter-* slug list). Distinct from Sep 3 /
  Aug 15 / Sep 11.
- Also verified but not used (backups): PaccMann (Manica, Mol Pharm 2019,
  10.1021/acs.molpharmaceut.9b00520, PMID 31618586); Sakellaropoulos (Cell Reports 2019,
  10.1016/j.celrep.2019.11.017, PMID 31825821 — clinical-cohort validation).
