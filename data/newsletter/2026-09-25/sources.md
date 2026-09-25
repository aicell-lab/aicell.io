# Newsletter sources — 2026-09-25

Theme: **Reading a cell's future from live images** — deep learning that predicts a
cell's fate, cycle stage, lineage choice, and disease-relevant behavior from
(often label-free) live-cell and brightfield microscopy, frequently *before*
molecular markers or reporters reveal it. This is the lab's imaging/live-microscopy
core — the perception layer under Agent-Lens, the REEF farm, and the self-driving
microscope — and it connects to the virtual cell (predict phenotype from a cell's
observable state).

Distinct from prior nightly themes: Aug 25 (cell *tracking* / lineage
reconstruction — following cells, not predicting their future), Aug 6 (virtual
staining / in-silico labeling — translating contrast, not forecasting fate), Aug 16
(segmentation foundation models), Sep 23 (cell-type annotation from transcriptomes).
Today is specifically **predictive phenotyping from live imaging**.

All six anchors verified via NCBI E-utilities (esearch/efetch abstract XML). Fetched
2026-09-25T03:01Z. Canonical DOI confirmed per record. Only verbatim quoted phrases
are used in the post.

## Anchors (NCBI-verified; abstracts captured)

1. **Deep Learning Automates the Quantitative Analysis of Individual Cells in
   Live-Cell Imaging Experiments (DeepCell)** — Van Valen, Kudo, ..., Covert.
   *PLoS Computational Biology* (2016). DOI 10.1371/journal.pcbi.1005177 |
   PMID 27814364.
   Why: the substrate. Deep CNNs "robustly segment the cytoplasms of mammalian
   cells … from phase contrast images without the need for a fluorescent cytoplasmic
   marker," across "multiple cell types across the domains of life" — you can't
   predict a cell's future until you can reliably see and measure every cell over
   time.

2. **Prospective identification of hematopoietic lineage choice by deep learning**
   — Buggenthin, Buettner, ..., Marr. *Nature Methods* (2017).
   DOI 10.1038/nmeth.4182 | PMID 28218899.
   Why: the headline result. A network "prospectively predicts lineage choice in
   differentiating primary hematopoietic progenitors using image patches from
   brightfield microscopy and cellular movement," and — the striking part — "lineage
   choice can be detected up to three generations before conventional molecular
   markers are observable." The cell's future is written in its shape and motion.

3. **Deep Learning Neural Networks Highly Predict Very Early Onset of Pluripotent
   Stem Cell Differentiation** — Waisman, La Greca, ..., Guberman. *Stem Cell
   Reports* (2019). DOI 10.1016/j.stemcr.2019.02.004 | PMID 30880077.
   Why: how early. A CNN on "transmitted light microscopy images" distinguishes
   pluripotent from early-differentiating cells "with an accuracy higher than 99%,"
   and "successful prediction started just 20 min after the onset of
   differentiation" — long before conventional assays would register the change.

4. **Convolutional Neural Networks Can Predict Retinal Differentiation in Retinal
   Organoids** — Kegeles, Naumov, ..., Baranov. *Frontiers in Cellular
   Neuroscience* (2020). DOI 10.3389/fncel.2020.00171 | PMID 32719585.
   Why: 3D, and non-invasive. A CNN predicts organoid fate "based on bright-field
   imaging," "before the onset of reporter gene expression," beating a human expert
   ("84% vs. 67 ± 6% of correct predictions") — "the first demonstration of CNN's
   ability to classify stem cell-derived tissue in vitro."

5. **Reconstructing cell cycle and disease progression using deep learning**
   — Eulenberg, Köhler, ..., Wolf, Theis. *Nature Communications* (2017).
   DOI 10.1038/s41467-017-00623-3 | PMID 28878212.
   Why: recover a *continuous* hidden process from raw images. Deep CNNs "combined
   with nonlinear dimension reduction enable reconstructing biological processes,"
   demonstrated by "reconstructing the cell cycle of Jurkat cells and disease
   progression in diabetic retinopathy" — and fast enough "for on-the-fly analysis
   in an imaging flow cytometer."

6. **Interpretable deep learning uncovers cellular properties in label-free live
   cell images that are predictive of highly metastatic melanoma** — Zaritsky,
   Jamieson, ..., Danuser. *Cell Systems* (2021). DOI 10.1016/j.cels.2021.05.003 |
   PMID 34077708.
   Why: prediction *and* interpretation. A generative network plus supervised ML
   classifies xenografts as "efficient" or "inefficient" metastatic and generates
   "in silico cell images that amplify the critical predictive cell properties,"
   revealing "pseudopodial extensions and increased light scattering as hallmark
   properties of metastatic cells" — patterns "too subtle to be identified in the
   raw imagery by a human expert." Answers the "black box" criticism head-on.

## Horizon radar (strategy note)
- This is the **perception layer of the self-driving microscope**: if a model can
  read fate/state from live images in real time, the microscope can *decide* where
  and when to look, image, or intervene — exactly the closed loop Agent-Lens and the
  REEF farm are built for.
- Predictive live imaging is a route to the **virtual cell** that doesn't need
  omics: forecast a cell's phenotype from its observable morphology and dynamics,
  cheaply and non-invasively, at scale.
- Zaritsky's interpretable/generative approach is the antidote to the "black box"
  worry the lab keeps flagging — the same value behind its work on transparent,
  reusable models (BioImage Model Zoo, BioEngine).

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/search/discover` returns
  HTTP 402 "Insufficient credits" (getxapi out of credits; ~48th consecutive skip;
  Grok-based replacement wired, awaiting a credit decision).
- Anchor verification: NCBI E-utilities; all six PMIDs have matching title +
  abstract; canonical DOI confirmed (note: PubMed records list cited-reference DOIs
  too — the first/journal-matching DOI is the article's own). Only verbatim quoted
  phrases are used.
- Dedup: predictive phenotyping from live imaging has NOT been a prior nightly theme
  (checked the full content/post/newsletter-* slug list). Distinct from Aug 25, Aug 6,
  Aug 16, Sep 23.
