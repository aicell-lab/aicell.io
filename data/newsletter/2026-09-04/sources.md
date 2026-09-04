# Newsletter sources — September 4, 2026

**Theme:** AI for **untargeted metabolomics** — turning tandem mass spectra (MS/MS) into molecular
structures. The "dark metabolome": untargeted MS detects thousands of compounds per sample, but the
vast majority remain unidentified. Machine learning bridges spectrum → structure. "Naming the
Unknowns."

**Dedup guard:** Distinct from Aug 7 (AI proteomics / de novo *peptide* sequencing — proteins/peptides
from MS, not small molecules). Distinct from Sep 3 (single-cell multi-omics *integration* — RNA/ATAC/
protein), Sep 2 (protein *function* prediction), Aug 15 (single-cell FMs). This is a *new omics layer*
— the metabolome, the small-molecule chemistry closest to phenotype — and its own hard ML problem
(structure elucidation from fragmentation spectra). Thematic echo of Sep 2's "dark proteome" — here
it's the dark metabolome — but a different molecule class, different data (MS/MS), different methods.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on monitor (min-likes 30,
since-hours 24); search/discover blocked by the same 402. ~26th consecutive skip (>three weeks). Grok
replacement wired, awaiting xAI credits.

All 6 anchors verified against **raw Europe PMC `abstractText` JSON** (fetched directly via curl — no
summarizer), with DOI/title/author/journal/year confirmed. Only abstract-verified verbatim quotes are
used below. (Note: the WebFetch summarizer blocks >125-char verbatim reproduction, so raw Europe PMC
JSON is the reliable route for exact quotes — used here.)

---

## Framing + the core ML trick — spectrum → fingerprint → database

### CSI:FingerID — ML fingerprints from fragmentation trees — VERIFIED
- Dührkop, K., Shen, H., Meusel, M., Rousu, J. & Böcker, S. "Searching molecular structure databases
  with tandem mass spectra using CSI:FingerID." *PNAS* 112(41):12580–12585, 2015. DOI
  10.1073/pnas.1509788112. First author Kai Dührkop; senior Sebastian Böcker. Resolves (Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**Metabolites provide a direct functional signature of cellular
  state.**"; "**Untargeted metabolomics experiments usually rely on tandem MS to identify the
  thousands of compounds in a biological sample. Today, the vast majority of metabolites remain
  unknown.**"; "**Our method computes a fragmentation tree that best explains the fragmentation
  spectrum of an unknown molecule. We use the fragmentation tree to predict the molecular structure
  fingerprint of the unknown compound using machine learning.**"; "**Our method is shown to improve on
  the competing methods for computational metabolite identification by a considerable margin.**"
- USE: the hook ("direct functional signature of cellular state"; "vast majority … remain unknown")
  AND the core trick (spectrum → fragmentation tree → ML fingerprint → search PubChem). Foundational.

### SIRIUS 4 — fast, usable structure identification — VERIFIED
- Dührkop, K., … Böcker, S. "SIRIUS 4: a rapid tool for turning tandem mass spectra into metabolite
  structure information." *Nature Methods* 16:299–302, 2019. DOI 10.1038/s41592-019-0344-8. First
  author Kai Dührkop; senior Sebastian Böcker (authors incl. Dorrestein, Rousu). Resolves (Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**Mass spectrometry is a predominant experimental technique in
  metabolomics and related fields, but metabolite structural elucidation remains highly
  challenging.**"; "**SIRIUS 4 integrates CSI:FingerID for searching in molecular structure
  databases.**"; "**Using SIRIUS 4, we achieved identification rates of more than 70% on challenging
  metabolomics datasets.**"
- USE: the workhorse that packaged CSI:FingerID into a fast tool; the >70% ID-rate number.

## Section 2 — When it's in no database

### CANOPUS — deep-net compound-class prediction — VERIFIED
- Dührkop, K., … Böcker, S. "Systematic classification of unknown metabolites using high-resolution
  fragmentation mass spectra." *Nature Biotechnology* 39:462–471, 2021. DOI 10.1038/s41587-020-0740-8.
  First author Kai Dührkop; senior Sebastian Böcker (authors incl. Nothias, Dorrestein). Resolves
  (Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**However, structural molecule annotation is limited to structures
  present in libraries or databases, restricting analysis and interpretation of experimental data.**";
  "**CANOPUS uses a deep neural network to predict 2,497 compound classes from fragmentation spectra,
  including all biologically relevant classes.**"; "**CANOPUS explicitly targets compounds for which
  neither spectral nor structural reference data are available and predicts classes lacking tandem
  mass spectrometry training data.**"; "**CANOPUS reached very high prediction performance (average
  accuracy of 99.7% in cross-validation) and outperformed four baseline methods.**"
- USE: the "database limit" problem, and the answer — if you can't name it, classify it (2,497
  classes), even for compounds with no reference data.

## Section 3 — Generating structures de novo

### MSNovelist — encoder-decoder structure generation — VERIFIED
- Stravs, M.A., Dührkop, K., Böcker, S. & Zamboni, N. "MSNovelist: de novo structure generation from
  mass spectra." *Nature Methods* 19:865–870, 2022. DOI 10.1038/s41592-022-01486-3. First author
  Michael A. Stravs; senior Nicola Zamboni. Resolves (Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**Current methods for structure elucidation of small molecules rely
  on finding similarity with spectra of known compounds, but do not predict structures de novo for
  unknown compound classes.**"; "**We present MSNovelist, which combines fingerprint prediction with an
  encoder-decoder neural network to generate structures de novo solely from tandem mass spectrometry
  (MS2) spectra.**"; "**In an evaluation with 3,863 MS2 spectra from the Global Natural Product Social
  Molecular Networking site, MSNovelist predicted 25% of structures correctly on first rank, retrieved
  45% of structures overall … without having ever seen the structure in the training phase.**";
  "**MSNovelist is ideally suited to complement library-based annotation in the case of poorly
  represented analyte classes and novel compounds.**"
- USE: the de novo generation step (parallels de novo peptide sequencing, Aug 7); complements (not
  replaces) libraries; the CASMI 2016 mention inside the abstract grounds the CASMI prove-it reference.

## Section 4 — Better similarity, and the open community layer

### Spec2Vec — learned spectral embeddings — VERIFIED
- Huber, F., … van der Hooft, J.J.J. "Spec2Vec: Improved mass spectral similarity scoring through
  learning of structural relationships." *PLOS Computational Biology* 17(2):e1008724, 2021. DOI
  10.1371/journal.pcbi.1008724. First author Florian Huber; senior Justin J.J. van der Hooft.
  Resolves (Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**Spectral similarity is used as a proxy for structural similarity in
  many tandem mass spectrometry (MS/MS) based metabolomics analyses such as library matching and
  molecular networking.**"; "**Here, we introduce Spec2Vec, a novel spectral similarity score inspired
  by a natural language processing algorithm-Word2Vec.**"; "**we show how Spec2Vec scores correlate
  better with structural similarity than cosine-based scores.**"; "**Spec2Vec is computationally more
  scalable allowing structural analogue searches in large databases within seconds.**"
- USE: NLP-for-spectra (word2vec on fragment peaks); better similarity underpins molecular networking.

### GNPS — open community knowledge base + molecular networking — VERIFIED
- Wang, M., … Bandeira, N. "Sharing and community curation of mass spectrometry data with Global
  Natural Products Social Molecular Networking." *Nature Biotechnology* 34:828–837, 2016. DOI
  10.1038/nbt.3597. First author Mingxun Wang; senior Nuno Bandeira (very large consortium incl.
  Dorrestein). Resolves (Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**We present Global Natural Products Social Molecular Networking
  (GNPS; http://gnps.ucsd.edu), an open-access knowledge base for community-wide organization and
  sharing of raw, processed or identified tandem mass (MS/MS) spectrometry data.**"; "**In GNPS,
  crowdsourced curation of freely available community-wide reference MS libraries will underpin
  improved annotations.**"; "**We also introduce the concept of 'living data' through continuous
  reanalysis of deposited data.**"
- USE: the open/community/prove-it anchor — shared data, molecular networking, 'living data.' Same
  open-science ethos the lab champions (BioImage Model Zoo / BioEngine). CASMI (referenced in
  MSNovelist's abstract) is the community contest / prove-it standard for small-molecule ID.

## Section 5 — Lab hook + horizon
- The metabolome is the omics layer *closest to phenotype* — "a direct functional signature of cellular
  state" (CSI:FingerID, verbatim). A serious virtual cell / Human Cell Simulator
  (/project/human-cell-simulator/, /post/newsletter-2026-08-15/) needs metabolism and small molecules,
  not just genes and proteins.
- Complements the omics thread: adds the metabolome as another layer to fuse alongside RNA/ATAC/protein
  (/post/newsletter-2026-09-03/) and the proteome (/post/newsletter-2026-08-07/). The "dark metabolome"
  mirrors the "dark proteome" (/post/newsletter-2026-09-02/) — the same discipline of annotating the
  unknown, applied to a different molecule class.
- Open, callable, benchmarked: SIRIUS/CSI:FingerID, GNPS (open knowledge base + 'living data'), and
  CASMI (community contest) embody the publish-the-tool-and-the-test ethos behind the BioImage Model
  Zoo (/project/bioimage-model-zoo/) + BioEngine (/project/bioengine/) and the recurring prove-it
  standard (/post/newsletter-2026-07-27/).
