# Newsletter sources — 2026-08-07 (fetched UTC 2026-08-07T03:00:28Z)

Theme: **The layer you can't amplify — AI for proteomics & mass spectrometry.**
The genome tells you what a cell *could* make; the transcriptome, what it intends to
make; the **proteome** — what it is actually doing, the working machinery — is the layer
closest to phenotype and by far the hardest to read. There is no PCR for proteins: you
cannot amplify them, so sensitivity is the wall, and the raw signal (fragment-ion mass
spectra) was nearly unreadable at scale without a reference database. Deep learning
changed that. A line of transformer models now **sequences peptides de novo — straight
from the spectrum, no database** — surfacing peptides and even organisms that databases
never contained; the frontier is pushing this down to **single cells** and up into
**foundation models**, and a brand-new *Nature Methods* review draws the arc explicitly
from protein identification "to building AI virtual cells." A lab-core story: the proteome
is the phenotype ground truth a [virtual cell](/project/human-cell-simulator/) needs, the
depth-complement to the lab's antibody/imaging proteomics (Human Protein Atlas) — and the
open-model / verify-the-readout discipline is the lab's throughline in a fresh modality.

## Provenance / method
- Web research (WebSearch + WebFetch). Load-bearing anchors verified with exact citations;
  the strategic tie (**AI proteomics → virtual cells** review) **primary-fetched** via
  PubMed with verbatim quotes.
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  again returns **HTTP 402 Insufficient credits** (getxapi out of credits **~5 weeks**);
  `search`/`discover` gated; x-breaking stays disabled. Flagged to Wei for a top-up.
- **De-dup / variety (important):** proteomics / mass-spectrometry AI has **never** been a
  theme in this run — a genuinely new *modality* (mass spec, not microscopy, not
  sequencing, not structure). Chosen deliberately for maximal contrast after an
  imaging/cell-FM-heavy stretch: Aug 6 virtual staining, Aug 4 image-based profiling, Aug 2
  virtual cell, Aug 1 pathology (all imaging or single-cell-omics). Distinct from Jul 29
  cryo-ET "visual proteomics" (that was *imaging* protein structures in situ; this is
  *mass-spectrometry sequencing* of peptides) and from Aug 4 profiling (image phenotype).
  Clear to run.
- **Verification discipline:** InstaNovo (*Nature Machine Intelligence* 2025) and the AI-
  proteomics review (*Nature Methods* 2026) are peer-reviewed with exact DOIs; Casanovo is
  open-source and peer-reviewed. Single-cell-proteomics FM items (scpFormer; MS-proteomics
  FM) are 2025–26 preprints, **labelled as such**, cited for direction, no fabricated
  numbers. Per-single-cell protein-group counts (1,000–3,000) are from a 2026 landscape
  review (Anal. Chem.), reported as a field range.

## Item 1 — Capability: transformers read proteins with no database (ANCHOR — InstaNovo / Casanovo)
- **The problem:** *de novo* peptide sequencing means reading a peptide's amino-acid
  sequence directly from its tandem-MS fragment spectrum, **without** matching against a
  reference protein database — the only way to find peptides that aren't in any database
  (immunopeptidomics, metaproteomics, paleoproteomics, venomics, novel/mutant proteins).
  Trajectory: DeepNovo (2017, CNN/LSTM) → **Casanovo** (first transformer, 2022) → a
  proliferation of transformer variants.
- **Casanovo** (open-source, Noble-Lab): Melih Yilmaz, William E. Fondrie, Wout
  Bittremieux, … William Stafford Noble, "De novo mass spectrometry peptide sequencing
  with a transformer model," **ICML 2022 → *Nature Communications* (2024)**;
  **Casanovo 5.0** (2025 update). It "translates peaks in MS/MS spectra into amino acid
  sequences," taking raw (m/z, intensity) peaks + precursor mass/charge with **no
  discretization** and no separate RNN — a simpler, stronger framework; trained on ~30M
  spectra. Especially valuable "for identifying peptides that may not be in your protein
  database."
- **InstaNovo (current flagship, peer-reviewed):** Kevin Eloff, Konstantinos
  Kalogeropoulos, Amandla Mabona, … Timothy P. Jenkins (InstaDeep + DTU), "InstaNovo
  enables diffusion-powered de novo peptide sequencing in large-scale proteomics
  experiments," ***Nature Machine Intelligence* 7, 565–579 (2025)**, DOI
  10.1038/s42256-025-01019-5 (open access; 31 Mar 2025). Two coupled models: **InstaNovo**,
  a transformer translating fragment-ion peaks into sequences, and **InstaNovo+**, a
  **multinomial diffusion** model that iteratively **refines** predicted sequences ("human-
  intuition"-style second pass). Verbatim result: the authors "achieve improved therapeutic
  sequencing coverage, **discover novel peptides and detect unreported organisms** in
  diverse datasets, thereby expanding the scope and detection rate of proteomics searches."
  Database-free identification "expands the landscape of proteomic discovery."

## Item 2 — The frontier: single-cell proteomics + foundation models (2025–26, preprints/reviews)
- **The un-amplifiable wall:** unlike genomics/transcriptomics, **proteins cannot be
  amplified**, so sensitivity is the defining challenge. A 2026 landscape review (*Analytical
  Chemistry*, "Trends in MS-Based Single-Cell Proteomics") reports workflows now routinely
  quantify **1,000–3,000 protein groups per single mammalian cell**, via miniaturized prep,
  ultra-low-flow separation, ion mobility, and **AI-driven analysis** to beat missing values.
- **Foundation models arrive:**
  - **MS-proteomics foundation model** (arXiv:2505.10848, 2025): a model for tandem-MS
    proteomics "trained on de novo sequencing" that "learns generalizable representations of
    spectra, improves performance on downstream tasks where training data is limited."
  - **scpFormer** (arXiv:2604.20003, 2026): a foundation model "for unified representation
    and integration of single-cell proteomics"; training data spans **544 proteins across 22
    cell types**; frames the platform trade-off — **antibody-based** methods give broad
    coverage at scale, **mass-spectrometry** gives "substantially greater proteomic depth per
    cell." (Preprints — direction, not load-bearing numbers.)
- **Momentum:** ASMS 2026 (drugdiscoverynews coverage) shows AI now "embedded within
  analytical workflows rather than treated as standalone" across single-cell and spatial
  proteomics.

## Item 3 — Why it matters / honest frontier: the ladder to virtual cells + the check (ANCHOR — Nat Methods review + NovoBench)
- **The strategic ladder (fetched, PubMed 42521824):** Yingying Sun, Jun A, Zhiwei Liu, Rui
  Sun, Liujia Qian, … **Tiannan Guo** (corresp.), "AI proteomics: from protein identification
  to virtual cells," ***Nature Methods* (2026)**, DOI 10.1038/s41592-026-03085-y (online 28
  Jul 2026). Verbatim: AI is driving MS-based proteomics "ranging from protein identification
  to building AI virtual cells"; spanning "improving peptide and protein identification and
  quantification," "characterizing protein-protein interactions and protein complexes,"
  "advancing spatial and perturbation proteomics," and "integrating multi-omics data" —
  "ultimately, enabling AI virtual cells." The authors call for global collaboration to
  "establish an AI-friendly ecosystem for MS-based proteomics."
- **The check (shared evaluation):** **NovoBench** (arXiv:2406.11906) — a benchmark for
  deep-learning de novo peptide sequencing across models (Casanovo, InstaNovo+, π-HelixNovo,
  …). De novo identifications still demand rigorous **FDR control / validation**: a confidently
  predicted peptide that isn't real is a false discovery — the same "verify the generated
  readout" discipline the lab keeps returning to.

## Lab connections (for "why it matters")
- **The phenotype layer the virtual cell can't fake.** Genome = potential; transcriptome =
  intent; **proteome = what the cell is actually doing.** The
  [Human Cell Simulator](/project/human-cell-simulator/) needs proteome-level ground truth,
  and the *Nature Methods* 2026 review names the destination outright: AI proteomics →
  **AI virtual cells**.
- **Depth-complement to the lab's imaging proteomics.** The lab works with the **Human Protein
  Atlas** — antibody/imaging-based proteomics (breadth, spatial context). MS proteomics is the
  **depth-per-cell** complement (the scpFormer breadth-vs-depth trade). Reading proteins two
  ways — the picture and the spectrum — is how you get both coverage and resolution.
- **Open models, shared benchmarks.** Casanovo (open) and NovoBench mirror the
  [BioImage Model Zoo](/project/bioimage-model-zoo/) / AI4Life ethos — publish the model and
  the honest test together.
- **The throughline: verify the readout.** De novo peptides need FDR control just as virtual
  stains need [hallucination detection](/post/newsletter-2026-08-06/) and virtual cells must
  [show their work](/post/newsletter-2026-08-02/). A generated identification you can't audit
  isn't a measurement.

## De-dup check
- Recent digests: Aug 6 virtual staining; Aug 5 federated/privacy; Aug 4 image-based
  profiling; Aug 3 small-molecule design; Aug 2 virtual cell; Aug 1 pathology; Jul 31
  self-driving labs; Jul 30 RNA design; Jul 29 cryo-ET; Jul 28 genomic-FM eval; Jul 26
  spatial; Jul 21 microscopy VLMs; Jul 19 segmentation; Jul 13 wiring diagrams. **Proteomics
  / mass-spectrometry AI (de novo peptide sequencing, single-cell proteomics FMs) has not
  been a theme** — a distinct instrument and modality. Distinct from Jul 29 cryo-ET (imaging
  structures) and Aug 4 profiling (image phenotype). Clear to run.
