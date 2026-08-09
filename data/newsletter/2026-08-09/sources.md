# Newsletter sources — 2026-08-09 (fetched UTC 2026-08-09T03:00:37Z)

Theme: **The grammar of the genome — DNA foundation models learn to read the whole
genome and to write new ones.** For years we could read *genes* — the ~2% of DNA that
codes for protein — but the other ~98%, the noncoding regulatory genome that decides
when, where and how much, stayed largely dark; and while we could read, write and edit
DNA, we could not *compose* it. Two landmark 2026 *Nature* papers moved both walls at
once: **AlphaGenome** (Google DeepMind) reads the regulatory genome at single-base
resolution over a megabase of context, and **Evo 2** (Arc Institute + NVIDIA) writes and
designs DNA across all three domains of life — with wet-lab-validated designed sequences.
The honest frontier is just as important: independent benchmarks show foundation models
still lose tissue-specific regulatory grammar to specialist tools, cell-type specificity
and rare variants remain unreliable, and generative genome design forces biosafety to the
front. A horizon story: this is the **genome layer** of a [virtual cell](/project/human-cell-simulator/)
and the substrate of automated discovery — and the same prove-it / safeguard discipline
the lab keeps insisting on.

## Provenance / method
- Web research (WebSearch + WebFetch). Evo 2 facts **primary-fetched** from Arc Institute's
  own pages (arcinstitute.org/news/evo2 and /news/evo-2-one-year-later) with verbatim
  quotes; AlphaGenome publication + expert framing **primary-fetched** from the Science
  Media Centre expert-reaction page. AlphaGenome architecture/benchmark numbers grounded via
  search excerpts of the paper + secondary coverage (biorxiv PDF direct fetch 403'd; Nature
  auth-walled) — no fabricated numbers.
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  **and** `scripts/lab-x.py discover` both return **HTTP 402 Insufficient credits** (getxapi
  out of credits **~5 weeks**); `search` gated; x-breaking stays disabled. Flagged to Wei.
- **De-dup / variety (important):** genome-scale DNA *foundation models* — reading the
  regulatory genome + generative genome design — has **not** been the theme of a digest.
  Deliberately chosen as a **non-imaging, distinct-molecule** contrast after an
  imaging-heavy stretch (Aug 8 smart microscopy, Aug 6 virtual staining, Aug 4 profiling,
  Aug 1 pathology). Distinct molecule from Aug 7 (proteins/mass-spec), Jul 30 (RNA/mRNA
  design), Aug 3 (small molecules). **Complementary, not duplicative, to Jul 28 "Two
  Ledgers"** — that digest was the *evaluation reckoning* (do genomic FMs beat baselines on
  held-out tests?); today is the *two frontier 2026 models* and what read/write-the-genome
  now means, with the eval caveat explicitly carried forward and linked. Clear to run.
- **Verification discipline:** both anchors are **peer-reviewed in *Nature* (2026)** with
  exact DOIs. Evo 2's >90% BRCA1 accuracy and designed-sequence validation (16/285) are
  from Arc's own reporting. AlphaGenome's 24/26 result and track counts are from the paper /
  secondary coverage, reported as such. The benchmarking dichotomy is from a peer-reviewed
  *Nature Communications* 2025 study. Preprints/blogs used only for framing, labelled.

## Item 1 — Read the other 98%: AlphaGenome (ANCHOR — Nature 2026, peer-reviewed)
- **Source:** "Advancing regulatory variant effect prediction with AlphaGenome," **Demis
  Hassabis & Pushmeet Kohli et al. (Google DeepMind), *Nature* (2026)**, DOI
  10.1038/s41586-025-10014-0; published **16:00 UK, Wed 28 January 2026**.
- Verified facts:
  - **What it does:** predicts regulatory features directly from DNA sequence — variant
    effects, RNA splice sites, chromatin accessibility, gene expression — across many cell
    types. Processes **1 Mb** of input sequence and outputs at **single-base resolution**,
    predicting **5,930 human (1,128 mouse) genome tracks** across **11 output types**.
  - **The tradeoff it broke:** base-resolution models (SpliceAI) were limited to short
    inputs (<=10 kb), missing distal regulation; long-context models (Enformer, Borzoi)
    reached 200-500 kb only at coarse 32-128 bp resolution. AlphaGenome claims both at once —
    U-Net-style encoder -> transformers -> decoder into task-specific heads.
  - **2D splicing representation:** a distinctive 2D track that captures which genomic
    positions interact — "parallels AlphaFold's pairwise amino acid representations" — so it
    can see a 1-bp splice donor and 500-kb-distant regulatory context together.
  - **Benchmark:** "matched or exceeded the strongest available external model on **24 of 26
    variant-effect evaluations**." The regulatory genome spans ~98% of human DNA; AlphaGenome
    reads most of it at single-base resolution.
  - **Verbatim (expert reaction, Science Media Centre):** Dr Robert Goldstone (Francis Crick
    Institute): "This level of resolution, particularly for non-coding DNA, is a breakthrough
    that moves the technology from theoretical interest to practical utility." Dr Xianghua Li
    (KCL), on limits: "For important medical tasks, current AI models are still not reliable
    enough for patient care."

## Item 2 — Write across all of life: Evo 2 (ANCHOR — Nature 2026, peer-reviewed, primary-fetched)
- **Source:** Garyk Brixi, Matthew G. Durrant, Jason Ku, ... (co-senior **Patrick Hsu**,
  Arc/UC Berkeley; **Brian Hie**, Stanford/Arc), "Genome modeling and design across all
  domains of life with Evo 2," ***Nature* (2026)**, DOI 10.1038/s41586-026-10176-5 (Arc
  Institute + NVIDIA; published ~4 Mar 2026). Preprint Feb 2025.
- Verified facts (Arc's own pages, verbatim where quoted):
  - **Scale:** **7B and 40B** parameter models; trained on **over 9.3 trillion nucleotides**
    from **over 128,000 whole genomes** / **>100,000 species** across **all three domains of
    life** (bacteria, archaea, eukaryotes + phage/metagenomic); **1 million nucleotide**
    context; architecture **StripedHyena 2**; >2,000 NVIDIA H100 GPUs. 30x more data than Evo
    1; reasons over 8x as many nucleotides. "the largest fully open biological AI model to
    date."
  - **Read + write + compose:** Patrick Hsu — "the models have enabled machines to read,
    write, and think in the language of nucleotides." Evo 2 "can design new genomes as long
    as those of simple bacteria."
  - **Wet-lab validation of designed DNA:** "**16 of 285 tested designs successfully
    propagated and inhibited growth of the appropriate bacterial strains**" — designed
    sequences that actually worked in cells, not just in silico.
  - **Variant effects:** over **90% accuracy** classifying BRCA1 mutations (benign vs
    pathogenic) with no task-specific training; widely reported to set state of the art on
    noncoding BRCA1 variants zero-shot (secondary coverage; reported as such).
  - **Biosafety:** the team **excluded pathogens infecting humans** from the base dataset and
    "ensured the model would not return productive answers to queries about these pathogens";
    red-teaming; Stanford's Tina Hernandez-Boussard assisted with responsible development.
    Open weights/code/data via Arc GitHub + NVIDIA BioNeMo.

## Item 3 — The honest grammar + the safeguard (benchmark + biosafety)
- **The dichotomy (peer-reviewed):** "Benchmarking DNA foundation models for genomic and
  genetic tasks," ***Nature Communications* (2025)**, s41467-025-65823-8 — on QTL benchmarks
  (eQTL, sQTL), **specialized models (AlphaGenome, Enformer) are the clear winners**;
  foundation models learn a general, context-free sense of what makes a sequence "broken,"
  but specialists still capture the tissue-specific regulatory grammar that decides whether a
  variant is *functional* in a particular cell type. **Cell-type specificity and rare
  variants remain open** (echoed by AlphaGenome's own stated limits).
- **The safeguard:** generative genome models make biosafety a first-class design
  constraint, not an afterthought — Evo 2's pathogen exclusion + red-teaming is the template.
  This is the [Design, Build, Test — and Safeguard](/post/newsletter-2026-07-20/) question in
  its sharpest form: automated design of biology needs alignment before capability outruns it.
- **The prove-it throughline:** the same discipline as the genomic-FM
  [evaluation reckoning](/post/newsletter-2026-07-28/) and the
  [prove-it year](/post/newsletter-2026-07-27/) — hold foundation models to held-out,
  task-relevant tests; capability claims are cheap, calibrated benchmarks are not.

## Lab connections (for "why it matters")
- **The genome layer of the virtual cell.** Arc explicitly frames Evo as one piece of a stack
  toward **virtual cell models** that predict how cells respond to perturbations; the vision
  is to couple a genome model with RNA-seq, gene-regulatory and signaling networks into a
  multimodal framework. That is precisely the missing sequence-to-function layer of the
  [Human Cell Simulator](/project/human-cell-simulator/).
- **Automated discovery.** Generative genome design + zero-shot variant interpretation +
  agentic mining of public data is the [automated-discovery](/project/autonomous-research-agents/)
  horizon named directly by the field.
- **Open models, shared and runnable.** Evo 2 ships fully open (weights, code, data via GitHub
  + BioNeMo) — the [BioImage Model Zoo](/project/bioimage-model-zoo/) / AI4Life /
  [BioEngine](/project/bioengine/) ethos, extended from images to genomes.
- **Prove-it + safeguard.** Held-out evaluation ([Jul 28](/post/newsletter-2026-07-28/)) and
  biosafety-by-design ([Jul 20](/post/newsletter-2026-07-20/)) are the lab's throughline; a
  model that can *compose* biology must be judged and safeguarded, not just admired.

## De-dup check
- Recent digests: Aug 8 smart microscopy; Aug 7 proteomics; Aug 6 virtual staining; Aug 5
  federated/privacy; Aug 4 image profiling; Aug 3 small-molecule design; Aug 2 virtual cell;
  Aug 1 pathology; Jul 31 self-driving labs; Jul 30 RNA/mRNA; Jul 29 cryo-ET; Jul 28 genomic-FM
  *eval*; Jul 27 prove-it; Jul 26 spatial; Jul 20 biosecurity. **Genome-scale DNA foundation
  models (read the regulatory genome + generative genome design) has not been a digest theme.**
  Distinct molecule from Aug 7 (protein), Jul 30 (RNA), Aug 3 (small molecule); non-imaging
  contrast to the recent run; complementary (not duplicative) to Jul 28's evaluation reckoning,
  which is explicitly carried forward and linked. Clear to run.
