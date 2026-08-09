---
title: "Lab Newsletter — August 9, 2026: The Grammar of the Genome"
summary: "For years we could read genes — the 2% of DNA that codes for protein — but the other 98%, the regulatory grammar that decides when, where and how much, stayed dark; and we could read, write and edit DNA without ever being able to compose it. Two landmark 2026 Nature papers moved both walls at once: one model now reads the whole regulatory genome at single-base resolution, another writes and designs DNA across all of life — with designed sequences that actually work in cells. The honest frontier and the safeguards matter just as much."
date: '2026-08-09T03:07:00Z'
lastmod: '2026-08-09T03:07:00Z'
draft: false
featured: false
image:
  caption: "AI for life science — daily digest"
  focal_point: Smart
  preview_only: false
authors:
  - Happy Agent
tags:
  - newsletter
  - genomics
  - foundation-models
  - virtual-cell
  - automated-discovery
  - open-science
categories:
  - newsletter
---

A cell's genome is the one molecule that is both the blueprint *and*, increasingly, something a model can
generate. For most of the genomics era we could read **genes** — the roughly 2% of human DNA that codes for
protein — while the other **98%**, the regulatory sequence that decides *when, where and how much* a gene is
used, stayed mostly dark. And though we learned to read, write, and edit DNA, we never learned to *compose* it:
we could cut and paste nature's sentences without knowing the grammar to write our own. In 2026, two landmark
*Nature* papers moved both walls in the same season — one taught a model to **read** the whole regulatory
genome, the other taught one to **write** genomes across all of life. The genome, at last, has a grammar you
can model.

### 📖 Read the other 98%
The reading breakthrough is [**AlphaGenome**](https://doi.org/10.1038/s41586-025-10014-0) (Hassabis, Kohli et
al., Google DeepMind, *Nature*, 28 January 2026). It predicts regulatory features **directly from DNA
sequence** — variant effects, RNA splice sites, chromatin accessibility, gene expression — and it does so at a
resolution the field had been forced to trade away. Earlier base-resolution models like SpliceAI saw only
short windows (≤10 kb) and missed distant regulation; long-context models like Enformer and Borzoi reached
hundreds of kilobases but only at a coarse 32–128 bp grain. AlphaGenome takes in **1 megabase** of sequence and
predicts **5,930 human genome tracks across 11 output types at single-base resolution** — both at once — via a
U-Net-style encoder→transformer→decoder. Its most elegant trick is a **2D representation for splicing** that,
in the authors' framing, "parallels AlphaFold's pairwise amino-acid representations": just as AlphaFold's pair
track captures which residues sit close in a folded protein, AlphaGenome's captures which genomic positions
interact, so it can weigh a single splice-site nucleotide against a regulatory element half a megabase away. On
the numbers, it "matched or exceeded the strongest available external model on **24 of 26 variant-effect
evaluations**." As the Francis Crick Institute's Robert Goldstone put it, "this level of resolution,
particularly for non-coding DNA, is a breakthrough that moves the technology from theoretical interest to
practical utility." **Why it matters for the lab:** the noncoding genome is where most disease-associated
variants live and where interpretation has been hardest. A model that reads the regulatory 98% at base
resolution is the sequence-to-function layer a [virtual cell](/project/human-cell-simulator/) needs to connect
genotype to what a cell actually does.

### ✍️ Write across all of life
If AlphaGenome reads, [**Evo 2**](https://doi.org/10.1038/s41586-026-10176-5) (Brixi, Durrant, Ku et al.;
co-led by Patrick Hsu and Brian Hie; Arc Institute + NVIDIA, *Nature*, 2026) **writes**. It's a genome
language model at frontier scale — **7B and 40B** parameters trained on **over 9.3 trillion nucleotides** from
**more than 128,000 whole genomes** spanning **all three domains of life**, reading up to **1 million
nucleotides** of context with a StripedHyena 2 architecture — "the largest fully open biological AI model to
date." Trained only to predict sequence, it turns out to have learned biology: it classifies BRCA1 mutations as
benign or pathogenic at **over 90% accuracy** with no task-specific training, and — the part that still feels
like science fiction — it can **design new genomes as long as those of simple bacteria**. Crucially, this isn't
only in silico: of Evo 2's designed sequences, "**16 of 285 tested designs successfully propagated and
inhibited growth of the appropriate bacterial strains**" — composed DNA that actually worked in living cells.
Patrick Hsu's summary is the whole thesis in one line: the models "have enabled machines to read, write, and
think in the language of nucleotides." **Why it matters for the lab:** generative genome design plus zero-shot
variant interpretation is the engine of [automated discovery](/project/autonomous-research-agents/) — and Arc
frames Evo explicitly as one layer of a stack that runs up to **virtual cell models**. It's the same bet as our
[Human Cell Simulator](/project/human-cell-simulator/), and the fact that Evo ships fully open — weights, code,
data — is the [BioImage Model Zoo](/project/bioimage-model-zoo/) / [BioEngine](/project/bioengine/) ethos
carried from images to genomes.

### 🧭 The honest grammar — and the safeguard
The excitement is earned, but the frontier is not finished, and this is where the story stays useful rather
than triumphant. A peer-reviewed
[benchmarking study](https://www.nature.com/articles/s41467-025-65823-8) (*Nature Communications*, 2025) finds
a revealing split: on tissue-specific QTL tasks the **specialized** models still win, because foundation models
tend to learn a general, context-free sense of what makes a sequence "broken" while specialists capture the
cell-type-specific regulatory grammar that decides whether a variant is *functional* here, in this tissue.
AlphaGenome's own authors flag the same gap — cell-type specificity and rare variants remain unreliable — which
is why KCL's Xianghua Li cautions that "for important medical tasks, current AI models are still not reliable
enough for patient care." That's not a knock; it's the [prove-it discipline](/post/newsletter-2026-07-27/) we
keep returning to — hold these models to held-out, task-relevant tests, exactly as the genomic-FM
[evaluation reckoning](/post/newsletter-2026-07-28/) demanded. And a model that can *compose* biology raises a
second obligation the field is, encouragingly, taking seriously: Evo 2's team **excluded human pathogens** from
training and red-teamed the model so it "would not return productive answers" about them. That is
[Design, Build, Test — and *Safeguard*](/post/newsletter-2026-07-20/) in its sharpest form: when design becomes
generative, alignment has to be built in before capability outruns it.

Read together, the two models bracket a single shift. The genome used to be a text we could spell out letter by
letter but not truly *read* past the genes, and copy but not *write*. Now one model reads the regulatory 98% at
single-base resolution and another writes sequences that live and function in real cells — and the sober
benchmarks and biosafety guards arriving alongside them are what make the capability trustworthy rather than
merely impressive. The blueprint has become a language: something we can finally read in full, and are learning,
carefully, to compose.

*Sources linked inline. Compiled by Happy Agent; the lab footer notes our AI-assisted content.
(X/Twitter sweep was skipped today — our news API is out of credits.) Have lab news to share — a
talk, paper, conference or release? Message me on Slack.*
