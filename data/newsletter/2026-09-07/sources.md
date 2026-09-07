# Newsletter sources — September 7, 2026

**Theme:** **AI for reading the genome itself** — deep-learning basecalling (raw signal → DNA) and variant
calling (reads → an individual's genetic variants). The upstream *infrastructure* layer that produces the
genome every other omics analysis assumes. "Reading the Genome, Base by Base." The arc: variant calling as
image recognition (DeepVariant) → end-to-end nanopore basecalling (Chiron) → variant calling for noisy
single-molecule reads (Clairvoyante) → haplotype-aware long-read calling in hard regions (PEPPER-Margin-
DeepVariant) → transformer-polished HiFi consensus (DeepConsensus) → the community prove-it benchmark
(precisionFDA Truth Challenge V2 / Genome in a Bottle).

**Dedup guard:** Distinct from Aug 9 (genome *language models* — self-supervised sequence modeling of an
already-assembled genome), Aug 19 (regulatory genomics / variant-*effect* prediction — what a variant
*does*), and Aug 24 (genome-*editing* outcome prediction — CRISPR repair). This is the layer *before* all
of those: turning raw sequencer output into an accurate genome and its variants. Not imaging (Aug 22
already covered super-res/restoration incl. Deep-STORM; broadly imaging-saturated this month), not
molecular design (Sep 5), not networks (Sep 6). A fresh "omics infrastructure" pivot.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on monitor (min-likes 30,
since-hours 24) and search. ~30th consecutive skip (>five weeks). Grok replacement wired, awaiting xAI
credits.

All 6 anchors verified against **raw Europe PMC `abstractText` JSON** (fetched directly via curl — no
summarizer), with DOI/title/author/journal/year confirmed. Only abstract-verified verbatim quotes used.

---

## Framing + the reframing that started it

### DeepVariant (Poplin et al.) — variant calling as image recognition — VERIFIED
- Poplin R, Chang PC, Alexander D, … DePristo MA. "A universal SNP and small-indel variant caller using
  deep neural networks." *Nature Biotechnology* 36:983–987, 2018. DOI 10.1038/nbt.4235.
- ABSTRACT-VERIFIED (verbatim): "**Despite rapid advances in sequencing technologies, accurately calling
  genetic variants present in an individual genome from billions of short, errorful sequence reads remains
  challenging.**"; "**a deep convolutional neural network can call genetic variation in aligned next-
  generation sequencing read data by learning statistical relationships between images of read pileups
  around putative variant and true genotype calls.**"; "**The approach, called DeepVariant, outperforms
  existing state-of-the-art tools.**"; "**The learned model generalizes across genome builds and mammalian
  species, allowing nonhuman sequencing projects to benefit from the wealth of human ground-truth
  data.**"
- USE: the hook (billions of errorful reads → an accurate genome is hard) + the key reframing: turn read
  pileups into *images* and let a CNN see the variants. Generalizes across species. Foundational.

## Section 1 — Reading raw signal end to end

### Chiron (Teng et al.) — end-to-end nanopore basecalling — VERIFIED
- Teng H, Cao MD, Hall MB, Duarte T, Wang S, Coin LJM. "Chiron: translating nanopore raw signal directly
  into nucleotide sequence using deep learning." *GigaScience* 7(5):giy037, 2018. DOI
  10.1093/gigascience/giy037.
- ABSTRACT-VERIFIED (verbatim): "**Sequencing by translocating DNA fragments through an array of nanopores
  is a rapidly maturing technology that offers faster and cheaper sequencing than other approaches.
  However, accurately deciphering the DNA sequence from the noisy and complex electrical signal is
  challenging.**"; "**we report Chiron, the first deep learning model to achieve end-to-end basecalling
  and directly translate the raw signal to DNA sequence without the error-prone segmentation step.**";
  "**Trained with only a small set of 4,000 reads, we show that our model provides state-of-the-art
  basecalling accuracy, even on previously unseen species.**"; "**Chiron achieves basecalling speeds of
  more than 2,000 bases per second using desktop computer graphics processing units.**"
- USE: the even-more-upstream step — raw electrical signal → bases, end-to-end, no hand-built
  segmentation. The "reading the physical molecule" angle.

## Section 2 — Calling variants from noisy single-molecule reads

### Clairvoyante (Luo et al.) — VERIFIED
- Luo R, Sedlazeck FJ, Lam TW, Schatz MC. "A multi-task convolutional deep neural network for variant
  calling in single molecule sequencing." *Nature Communications* 10:998, 2019. DOI
  10.1038/s41467-019-09025-z.
- ABSTRACT-VERIFIED (verbatim): "**The accurate identification of DNA sequence variants is an important,
  but challenging task in genomics. It is particularly difficult for single molecule sequencing, which has
  a per-nucleotide error rate of ~5-15%.**"; "**we developed Clairvoyante, a multi-task five-layer
  convolutional neural network model for predicting variant type (SNP or indel), zygosity, alternative
  allele and indel length from aligned reads.**"; "**we present 3,135 variants that are missed using
  Illumina but supported independently by both PacBio and Oxford Nanopore reads.**"
- USE: variant calling when reads themselves are 5–15% wrong; long reads reach variants short reads miss
  (3,135 of them). Open-source.

## Section 3 — Long reads into the hard parts of the genome

### PEPPER-Margin-DeepVariant (Shafin et al.) — VERIFIED
- Shafin K, Pesout T, Chang PC, … Paten B. "Haplotype-aware variant calling with PEPPER-Margin-DeepVariant
  enables high accuracy in nanopore long-reads." *Nature Methods* 18:1322–1332, 2021. DOI
  10.1038/s41592-021-01299-w.
- ABSTRACT-VERIFIED (verbatim): "**Long-read sequencing has the potential to transform variant detection
  by reaching currently difficult-to-map regions and routinely linking together adjacent variations to
  enable read-based phasing.**"; "**we introduce a haplotype-aware variant calling pipeline, PEPPER-Margin-
  DeepVariant, that produces state-of-the-art variant calling results with nanopore data.**"; "**produces
  high-quality single-nucleotide variants in segmental duplications and low-mappability regions where
  short-read-based genotyping fails.**"; "**contiguously spanning between 85% and 92% of annotated genes
  across six samples.**"
- USE: long reads unlock the genome's dark, hard-to-map regions (segmental duplications) where short reads
  fail; haplotype phasing. The "finish the genome" step.

## Section 4 — Polishing the reads with a transformer

### DeepConsensus (Baid et al.) — VERIFIED
- Baid G, Cook DE, Shafin K, … Carroll A. "DeepConsensus improves the accuracy of sequences with a gap-
  aware sequence transformer." *Nature Biotechnology* 41:232–238, 2023. DOI 10.1038/s41587-022-01435-7.
- ABSTRACT-VERIFIED (verbatim): "**Circular consensus sequencing with Pacific Biosciences (PacBio)
  technology generates long (10-25 kilobases), accurate 'HiFi' reads by combining serial observations of a
  DNA molecule into a consensus sequence.**"; "**We introduce DeepConsensus, which uses an alignment-based
  loss to train a gap-aware transformer-encoder for sequence correction. Compared to pbccs, DeepConsensus
  reduces read errors by 42%.**"; "**This increases the yield of PacBio HiFi reads at Q20 by 9%, at Q30 by
  27% and at Q40 by 90%.**"
- USE: a transformer (the same architecture family behind LLMs) applied to error-correct reads; 42% fewer
  errors, big yield gains at high quality. The "transformers reach genomics too" note.

## Section 5 — The community prove-it standard

### precisionFDA Truth Challenge V2 (Olson et al.) — VERIFIED
- Olson ND, Wagner J, McDaniel J, … Zook JM. "PrecisionFDA Truth Challenge V2: Calling variants from short
  and long reads in difficult-to-map regions." *Cell Genomics* 2(5):100129, 2022. DOI
  10.1016/j.xgen.2022.100129.
- ABSTRACT-VERIFIED (verbatim): "**The precisionFDA Truth Challenge V2 aimed to assess the state of the art
  of variant calling in challenging genomic regions.**"; "**20 challenge participants applied their
  variant-calling pipelines and submitted 64 variant call sets for one or more sequencing technologies
  (Illumina, PacBio HiFi, and Oxford Nanopore Technologies).**"; "**Submissions were evaluated following
  best practices for benchmarking small variants with updated Genome in a Bottle benchmark sets.**";
  "**graph-based and machine learning methods scoring best for short-read and long-read datasets,
  respectively. With machine learning approaches, combining multiple sequencing technologies performed
  particularly well.**"
- USE: the referee — a blind, technology-diverse benchmark on Genome in a Bottle truth sets; ML methods win
  for long reads; multi-technology combos best. The prove-it discipline, applied to genome reading.

## Section 6 — Lab hook + horizon
- This is the *foundation layer*: every downstream story we tell — genome LMs (Aug 9), variant effect
  (Aug 19), editing outcomes (Aug 24), a virtual cell's genotype
  (/post/newsletter-2026-08-15/, /project/human-cell-simulator/) — assumes an accurate genome and variant
  set. AI is what produces it, from noisy physical signal up.
- A recurring pattern the digest loves: *reframe the problem so a general architecture fits*. DeepVariant
  turns variant calling into image recognition (a CNN), DeepConsensus turns read correction into a
  transformer task — the same move as [seeing read pileups](/post/newsletter-2026-09-02/) or
  [spectra as language](/post/newsletter-2026-09-04/). General AI tools, pointed at biology's raw data.
- Open, callable, benchmarked: DeepVariant, Chiron, Clairvoyante, PEPPER-Margin-DeepVariant and
  DeepConsensus are open source; precisionFDA/Genome in a Bottle is the public truth set — the same
  publish-the-model-and-the-test ethos behind the BioImage Model Zoo (/project/bioimage-model-zoo/) +
  BioEngine (/project/bioengine/) and the recurring benchmark discipline (/post/newsletter-2026-07-27/).
  Model serving over a standard interface (a variant caller you can call like a service) is exactly the
  BioEngine pattern.
