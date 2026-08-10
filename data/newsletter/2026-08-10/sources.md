# Newsletter sources — 2026-08-10 (fetched UTC 2026-08-10T03:00:11Z)

Theme: **The screen that reads both the perturbation and the phenotype — optical
pooled screening (OPS): image-based genetic screening at genome scale.** For decades
genetic screening faced a hard tradeoff: *pooled* screens scale to millions of
perturbations but collapse the readout to a survival/enrichment count — you lose the
cell's shape, its subcellular detail, the actual phenotype; *arrayed* image screens
keep the rich phenotype but need one perturbation per well, so they don't scale. OPS
breaks the tradeoff: perturb thousands of genes in a single pooled dish, image every
cell richly, then read out *which* CRISPR guide each cell received by sequencing the
barcode **in situ, under the same microscope**. In 2025 two independent teams pushed
this to genome scale — building the first unbiased, morphology-based genome-wide
genotype–phenotype atlases. A lab-core story: OPS is imaging × perturbation at scale
(the lab's [self-driving microscope](/project/self-driving-microscope/) /
[Agent-Lens](/project/agent-lens/) / [REEF](/project/reef-imaging-farm/) territory) and
it is the **data engine** a [virtual cell](/project/human-cell-simulator/) is trained
on — millions of (perturbation → single-cell phenotype) pairs.

## Provenance / method
- Web research (WebSearch + WebFetch). Anchors verified across primary + fetchable
  secondary: PERISCOPE atlas numbers + TMEM251 discovery **primary-fetched** from
  Broad/phys.org coverage; the genome-wide antiviral OPS scaling paper
  **primary-fetched** from PMC (PMC10120039) with exact sgRNA/cell counts and the
  ATP13A1 finding; CellPaint-POSH (insitro) and the foundational Feldman/Blainey *Cell*
  2019 method grounded via search excerpts of the papers + secondary coverage (Nature
  and Broad news direct-fetch 403'd / auth-walled — no fabricated numbers).
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  **and** `scripts/lab-x.py discover` both return **HTTP 402 Insufficient credits**
  (getxapi out of credits **~5 weeks**); `search` gated; x-breaking stays disabled.
  Flagged to Wei for a top-up.
- **De-dup / variety (important):** *optical pooled screening as a modality* — pooled
  genetic perturbation read out by imaging + in-situ barcode sequencing — has **not**
  been a digest theme. It is distinct from the recent run:
  - **Aug 4 image-based profiling** = *read a phenotype from an existing image*
    (morphological representation learning). OPS *uses* profiling as the readout, but
    the story here is the **pooled genetic screen**: thousands of CRISPR perturbations
    in one dish, each cell's *genotype* recovered by in-situ sequencing. It answers
    "which gene does what," not "what does this image look like."
  - **Aug 8 smart microscopy** = real-time *acquisition control* at the instrument. OPS
    is *what you screen*, not *when you image*.
  - **Aug 9 genome foundation models** = *sequence* → function. OPS supplies the
    *experimental phenotype* labels those models and virtual cells ultimately need.
  - **Jul 31 self-driving labs** = the macro experiment-choosing loop. OPS is a
    concrete high-throughput assay such a lab would run.
  Clear separation. Clear to run.
- **Verification discipline:** PERISCOPE (*Nature Methods* 2025) and the genome-wide
  antiviral OPS (*PNAS* 2023) are **peer-reviewed** with exact DOIs and primary-verified
  numbers. CellPaint-POSH is **peer-reviewed** (*Nature Communications* 2025); its
  CP-DINO/AUC figures are from the paper/secondary coverage, reported as such. The
  Feldman/Blainey *Cell* 2019 foundational method is peer-reviewed and well established.
  No preprints load-bearing.

## Item 1 — The idea: read genotype and phenotype in the same cell (ANCHOR — Cell 2019 + PNAS 2023, peer-reviewed, primary-verified)
- **The tradeoff OPS breaks:** pooled CRISPR screens scale to millions of perturbations
  but reduce phenotype to an enrichment/survival count (you cannot see cell shape or
  subcellular detail); arrayed image-based screens keep rich phenotype but need one
  perturbation per well and do not scale. OPS keeps both: rich imaging of every cell in
  a pooled library, with the perturbation identity recovered *in situ*.
- **The foundational method:** David Feldman, Avtar Singh, ... Feng Zhang, **Paul C.
  Blainey**, "Optical Pooled Screens in Human Cells," ***Cell* (2019)**, S0092-8674(19)31067-0.
  Introduced **targeted in situ sequencing to demultiplex a library of genetic
  perturbations following image-based phenotyping** — fluorescence microscopy records
  both the phenotype *and* the sequencing reads that identify the CRISPR guide in each
  cell. Demonstrated on p65/NF-κB nuclear translocation across three cell lines (core
  NF-κB members as hits; MED12/MED24 as regulators of p65 retention time via time-lapse).
  Key artifact fix: a modified lentiviral packaging protocol cut barcode–sgRNA swapping
  from **>28% to <5%**. Detailed protocol: **Nature Protocols (2022)**, s41596-021-00653-8.
- **Scaled to genome-wide (primary-fetched, PMC10120039):** "A genome-wide optical
  pooled screen reveals regulators of cellular antiviral responses," ***PNAS* (2023)**,
  DOI 10.1073/pnas.2210623120. Increased throughput **"by over fourfold"**; a library of
  **80,408 sgRNAs targeting over 20,000 genes** (454 nontargeting) imaged across
  **10,366,390 cells**, with **12 cycles of in situ SBS** (sequencing by synthesis) to
  read out all sgRNAs. Found regulators of IRF3 translocation, Sendai-virus localization,
  and peroxisomal biogenesis; a key finding: **ATP13A1** (an ER-localized P5A-type ATPase)
  **"is essential for viral sensing,"** required for targeting MAVS to mitochondrial
  membranes. "Over an order of magnitude more genomic perturbations than demonstrated
  previously" with an in-situ SBS readout.

## Item 2 — Genome-scale morphology atlases arrive (ANCHOR — two independent 2025 papers, peer-reviewed)
- **PERISCOPE (Broad + Calico, primary-fetched numbers):** "A genome-wide atlas of human
  cell morphology," ***Nature Methods* (2025)**, DOI 10.1038/s41592-024-02537-7.
  **PERISCOPE = "perturbation effect readout in situ via single-cell optical
  phenotyping."** Combines **Cell Painting** (high-dimensional subcellular imaging) with
  **Optical Pooled Screening** (barcoded CRISPR + in-situ sequencing). The team built the
  **first unbiased, morphology-based genome-wide perturbation atlas in human cells** —
  **three whole-genome CRISPR screens**, CRISPR–Cas9 knockouts of **>20,000 genes** across
  **>30 million cells** (paper abstract), each cell scored on **hundreds of image-based
  features**; five-color Cell Painting followed by four-color in-situ sequencing to assign
  perturbations. It is **"more than 10× less expensive"** than comparable high-dimensional
  approaches like single-cell RNA-seq, and **all data are open access**. It "illustrated
  known biology" and characterized **poorly-understood genes** — e.g. uncovering that
  **TMEM251** (linked to a rare lysosomal storage disease) is **"required for trafficking
  enzymes to lysosomes."** Verbatim (JT Neal): a **"first-in-class genome-scale resource
  for linking cell morphology to gene function."**
- **CellPaint-POSH (insitro):** "A pooled Cell Painting CRISPR screening platform enables
  de novo inference of gene function by self-supervised deep learning," ***Nature
  Communications* (2025)**, s41467-025-66778-6 (Sivanandan, Leitmann et al.). Builds a
  **general** OPS-compatible Cell Painting platform (**POSH = "Pooled Optical Screening in
  Human cells"**) for hypothesis-free reverse-genetic screening via multiplexed
  morphological profiling, arguing prior OPS implementations "remain pathway-specific." Key
  result: **combining rich morphology with self-supervised deep learning (CP-DINO), gene
  networks emerge without target-specific biomarkers** — "unbiased discovery of gene
  function." Benchmarked with StringDB as ground truth: **AUC-ROC ≈ 0.83** (TPR ≈ 0.55 at
  5% FPR). They ran a **druggable-genome discovery screen**, and showed **CP-DINO applied
  zero-shot to PERISCOPE data** generalizes "across laboratories and protocols" — direct
  evidence the representations transfer. (Figures from paper/secondary coverage.)
- **The convergence:** two independent teams (Broad/Calico; insitro) built genome-scale
  image-based perturbation atlases in the **same year** — a signal the modality has matured
  from proof-of-concept to genome-scale infrastructure. Both note OPS's core advantage:
  quantitative assessment of phenotypes invisible to molecular profiling (morphology,
  subcellular localization), at higher throughput than arrayed imaging, with **no need to
  physically sort cells or predefine the phenotype**.

## Item 3 — Why it matters for the lab + the honest frontier
- **The data engine of a virtual cell.** OPS produces millions of **(genetic perturbation →
  single-cell phenotype)** pairs — precisely the causal, at-scale training signal a
  [Human Cell Simulator](/project/human-cell-simulator/) needs to learn how a cell responds
  when you change its genome. This is the imaging-native complement to Aug 9's *sequence*
  models: genome models read DNA → function; OPS measures perturbation → phenotype; a
  virtual cell couples them.
- **Imaging × perturbation is the lab's home turf.** Running genome-scale pooled optical
  screens — gentle live imaging, in-situ readout, closed-loop acquisition — is exactly what
  [Agent-Lens](/project/agent-lens/), the [self-driving microscope](/project/self-driving-microscope/)
  and the [REEF imaging farm](/project/reef-imaging-farm/) are built to do; smart
  acquisition (Aug 8) decides *when* to image these screens well.
- **Let the model find the biology.** CellPaint-POSH's self-supervised CP-DINO turns raw
  Cell Painting images into representations that recover gene networks **without hand-labels
  or target-specific biomarkers** — the same "learn the phenotype, don't hand-engineer it"
  thread as Aug 4's morphological foundation models, now driving a *screen*.
- **Open atlases, runnable.** PERISCOPE ships fully open access; a genome-scale
  genotype–phenotype atlas that anyone can mine is the
  [BioImage Model Zoo](/project/bioimage-model-zoo/) / [BioEngine](/project/bioengine/) /
  AI4Life ethos extended to perturbation data — and the discovery substrate for
  [autonomous research agents](/project/autonomous-research-agents/).
- **The honest frontier.** Morphology is a rich but *partial* phenotype — it sees shape and
  localization, not transcriptional state; OPS and molecular profiling are complementary,
  not interchangeable. Platforms are still being generalized beyond pathway-specific assays
  (the explicit motivation for CellPaint-POSH). And a screen is only as good as the
  phenotype you can read and *trust* — the same prove-it / trustworthy-readout discipline the
  lab keeps returning to ([Aug 2](/post/newsletter-2026-08-02/), [Jul 27](/post/newsletter-2026-07-27/)).

## Lab connections (for "why it matters")
- **human-cell-simulator** — OPS is the perturbation→phenotype data engine; genome-scale
  genotype–phenotype maps are the training signal.
- **self-driving-microscope / agent-lens / reef-imaging-farm** — imaging × perturbation at
  scale is the instrument's job; screens are what a self-driving imaging lab runs.
- **bioimage-model-zoo / bioengine** — open atlases + open self-supervised models, shared
  and runnable.
- **autonomous-research-agents** — genome-scale screens as the discovery substrate.
- **Throughline** — self-supervised representation (Aug 4), sequence models (Aug 9),
  trustworthy readouts (Aug 2 / Jul 27), macro self-driving loop (Jul 31).

## De-dup check
- Recent digests: Aug 9 genome foundation models; Aug 8 smart microscopy; Aug 7 proteomics;
  Aug 6 virtual staining; Aug 5 federated/privacy; Aug 4 image-based profiling; Aug 3
  small-molecule design; Aug 2 virtual cell; Aug 1 pathology; Jul 31 self-driving labs;
  Jul 30 RNA; Jul 29 cryo-ET; Jul 28 genomic-FM eval; Jul 27 prove-it; Jul 26 spatial.
  **Optical pooled screening as a modality — pooled genetic perturbation read out by imaging
  + in-situ barcode sequencing — has not been a digest theme.** Distinct from Aug 4 (reading
  a profile from an image), Aug 8 (acquisition control) and Aug 9 (sequence models): this is
  the *screen* that recovers both the perturbation and the phenotype in every cell. Clear to run.
