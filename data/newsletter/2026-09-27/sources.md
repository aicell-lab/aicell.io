# Newsletter sources — 2026-09-27

Theme: **Predicting the spectrum** — deep learning for mass-spectrometry-based
proteomics. Learn to predict a peptide's MS/MS fragmentation spectrum (and retention
time, ion mobility) from its sequence alone; use those predictions to build in-silico
spectral libraries and to power data-independent acquisition (DIA) at proteome scale.
The proteome is the cell's working-parts inventory — reading it faster and deeper is
a data layer under the virtual cell.

Distinct from Aug 7 (AI proteomics / *de novo peptide sequencing* — reading a spectrum
back to a sequence) and Sep 4 (metabolomics). Today is the *forward* problem —
sequence → predicted spectrum — and its use in DIA library-free workflows.

Verified via **Europe PMC** REST API (core result: title, journal, year, PMID,
abstractText). NOTE: NCBI E-utilities esearch was down at run time (HTTP 500,
"Cannot connect to SOLR"), so Europe PMC was used as the independent verification
source. Fetched 2026-09-27T03:01Z. Only verbatim quoted phrases are used in the post.

## Anchors (Europe PMC-verified; abstracts captured)

1. **pDeep: Predicting MS/MS Spectra of Peptides with Deep Learning** — Zhou, Han,
   ..., Yang. *Analytical Chemistry* (2017). DOI 10.1021/acs.analchem.7b02566 |
   PMID 29125736.
   Why: an early DL spectrum predictor. A "deep neural network-based model" using
   "bidirectional long short-term memory (BiLSTM)" predicts HCD/ETD/EThcD spectra
   "with >0.9 median Pearson correlation coefficients," and can even distinguish
   "extremely similar peptides … (GG = N, AG = Q, or even I = L)."

2. **Prosit: proteome-wide prediction of peptide tandem mass spectra by deep
   learning** — Gessulat, Schmidt, ..., Wilhelm. *Nature Methods* (2019).
   DOI 10.1038/s41592-019-0426-7 | PMID 31133760.
   Why: the headline. Trained on "550,000 tryptic peptides and 21 million high-quality
   tandem mass spectra," Prosit gives "retention time and fragment ion intensity
   predictions that exceed the quality of the experimental data," yielding "more
   identifications at >10× lower false discovery rates," and can generate "spectral
   libraries for data-independent acquisition."

3. **High-quality MS/MS spectrum prediction for data-dependent and data-independent
   acquisition data analysis (DeepMass:Prism)** — Tiwary, Levy, ..., Cox. *Nature
   Methods* (2019). DOI 10.1038/s41592-019-0427-6 | PMID 31133761.
   Why: fragmentation "within the uncertainty of measurement," with the finding that
   "peptide fragmentation depends on long-range interactions within a peptide
   sequence"; predicted DIA spectra are "nearly equivalent to the use of spectra from
   experimental libraries."

4. **In silico spectral libraries by deep learning facilitate data-independent
   acquisition proteomics (DeepDIA)** — Yang, Liu, ..., Zhu. *Nature Communications*
   (2020). DOI 10.1038/s41467-019-13866-z | PMID 31919359.
   Why: removes the DDA bottleneck. In-silico libraries "comparable to … experimental
   libraries" can be "built directly from protein sequence databases," breaking "the
   limitation of DDA on peptide/protein detection."

5. **DIA-NN: neural networks and interference correction enable deep proteome
   coverage in high throughput** — Demichev, Messner, ..., Ralser. *Nature Methods*
   (2020). DOI 10.1038/s41592-019-0638-x | PMID 31768060.
   Why: the DIA analysis workhorse — "exploits deep neural networks and new
   quantification and signal correction strategies," "particularly beneficial for
   high-throughput applications," enabling "deep and confident proteome coverage when
   used in combination with fast chromatographic methods."

6. **AlphaPeptDeep: a modular deep learning framework to predict peptide properties
   for proteomics** — Zeng, Zhou, ..., Mann. *Nature Communications* (2022).
   DOI 10.1038/s41467-022-34904-3 | PMID 36433986.
   Why: the unifying framework — predicts "retention time, ion mobility and fragment
   intensities of a peptide just from the amino acid sequence," represents PTMs "in a
   generic manner," uses "transfer learning" to avoid large datasets, and extends to
   "a HLA peptide prediction model to improve HLA peptide identification" (tying to
   the Sep 20 immunopeptidomics digest).

## Horizon radar (strategy note)
- Deep-learning spectral prediction is a quiet force-multiplier for **omics
  throughput**: library-free DIA means deeper, faster proteomes from the same
  instrument — more data per experiment, exactly what data-hungry cell models need.
- The proteome is a **data layer of the virtual cell** (what proteins are present, at
  what abundance, with what modifications). It complements the lab's imaging-based
  proteomics heritage (Human Protein Atlas) with the MS-based view.
- The open-tool pattern recurs (Prosit in ProteomicsDB; AlphaPeptDeep's "model shop";
  DIA-NN) — shared, reusable models over bespoke pipelines, the lab's BioEngine /
  model-zoo ethos.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/search/discover` returns
  HTTP 402 "Insufficient credits" (getxapi out of credits; ~50th consecutive skip;
  Grok-based replacement wired, awaiting a credit decision).
- Anchor verification: **Europe PMC** REST core API (NCBI esearch/SOLR was returning
  HTTP 500 at run time). All six DOIs resolved to a record with matching title +
  abstract + PMID. Only verbatim quoted phrases are used.
- Dedup: DL spectral prediction / DIA for MS proteomics has NOT been a prior nightly
  theme (checked the full content/post/newsletter-* slug list). Distinct from Aug 7
  (de novo sequencing), Sep 4 (metabolomics).
