---
title: "Lab Newsletter — August 10, 2026: One Cell, Two Answers"
summary: "Genetic screening has lived with a cruel tradeoff: pooled screens scale to millions of perturbations but flatten the readout to a survival count, while image-based screens keep the rich phenotype but need one gene per well. Optical pooled screening breaks it — perturb thousands of genes in one dish, image every cell, then read out which CRISPR guide each cell got by sequencing its barcode under the same microscope. In 2025 two teams pushed this to genome scale, building the first unbiased morphology-based genotype–phenotype atlases. It's imaging × perturbation at scale — and the data engine a virtual cell is trained on."
date: '2026-08-10T03:07:00Z'
lastmod: '2026-08-10T03:07:00Z'
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
  - optical-pooled-screening
  - functional-genomics
  - self-supervised-learning
  - virtual-cell
  - open-science
categories:
  - newsletter
---

Ask a cell what a gene does and you have always had to choose how to listen. **Pooled** CRISPR screens are
gloriously scalable — perturb every gene in the genome in a single dish — but the readout collapses to a
number: did cells carrying this guide grow or die, enrich or drop out? You lose the cell's *shape*, its
organelles, where a protein went. **Arrayed** image-based screens keep all of that rich phenotype, but they need
one perturbation per well, so genome scale means hundreds of thousands of wells and they simply don't scale.
For years that was the deal. **Optical pooled screening** (OPS) refuses it — and in 2025 the field carried the
idea all the way to the whole genome.

### 🧬 Read the genotype and the phenotype in the same cell
The trick is disarmingly direct. Grow a **pooled** library — thousands of genes knocked out across one shared
population — image every cell richly, and then, *under the same microscope*, recover **which CRISPR guide each
cell received** by sequencing its molecular barcode **in situ**. One cell gives you two answers at once: its
perturbation and its phenotype. David Feldman, Paul Blainey and colleagues established the method in
[**"Optical Pooled Screens in Human Cells"**](https://www.cell.com/cell/fulltext/S0092-8674(19)31067-0)
(*Cell*, 2019), using targeted in-situ sequencing to demultiplex a perturbation library *after* image-based
phenotyping — fluorescence microscopy recording both the phenotype and the sequencing reads that name the guide
in each cell. (A lovely piece of rigor along the way: a modified lentiviral protocol cut barcode–guide
"swapping" from **over 28% to under 5%**, so the genotype you read is the one the cell actually carries.) By
2023 the throughput had grown past genome scale: a
[genome-wide OPS](https://pmc.ncbi.nlm.nih.gov/articles/PMC10120039/) of antiviral responses (*PNAS*, 2023)
imaged **10,366,390 cells** carrying **80,408 guide RNAs targeting over 20,000 genes**, reading them all out
with **12 cycles of in-situ sequencing** — and pulled out real biology, including that **ATP13A1 "is essential
for viral sensing."** **Why it matters for the lab:** this is imaging × perturbation at scale — exactly the
regime our [self-driving microscope](/project/self-driving-microscope/), [Agent-Lens](/project/agent-lens/) and
the [REEF imaging farm](/project/reef-imaging-farm/) are built for.

### 🗺️ The genome, mapped by morphology
In 2025 two independent teams turned OPS into genome-scale *atlases*. The Broad Institute and Calico built
[**PERISCOPE**](https://www.nature.com/articles/s41592-024-02537-7) (*Nature Methods*, 2025) — "**p**erturbation
**e**ffect **r**eadout **i**n **s**itu via single-**c**ell **o**ptical **p**henotyping" — marrying
**Cell Painting** (high-dimensional subcellular imaging) to optical pooled screening. The result is the **first
unbiased, morphology-based genome-wide perturbation atlas in human cells**: three whole-genome CRISPR screens,
knockouts of **more than 20,000 genes** across **tens of millions of cells**, each scored on hundreds of
image-based features — and, crucially, **more than 10× cheaper** than a comparable single-cell RNA-seq screen,
with **all data open access**. It doesn't just re-draw known biology; it lit up the *poorly* known, revealing
for instance that **TMEM251**, tied to a rare lysosomal storage disease, is "required for trafficking enzymes to
lysosomes." As the Broad's JT Neal put it, it's a **"first-in-class genome-scale resource for linking cell
morphology to gene function."** The same year, insitro published a general platform,
[**CellPaint-POSH**](https://www.nature.com/articles/s41467-025-66778-6) (*Nature Communications*, 2025), aimed
squarely at OPS's remaining weakness — most implementations were **pathway-specific**. Its answer is to stop
hand-picking biomarkers: a **self-supervised model (CP-DINO)** learns representations straight from Cell Painting
images, and **gene networks emerge without any target-specific readout** (AUC ≈ 0.83 against the StringDB
interaction network), enabling **hypothesis-free discovery** across a druggable-genome screen. Tellingly, the
model applied **zero-shot to PERISCOPE's data still worked** — the learned phenotype **generalizes across labs
and protocols**. **Why it matters for the lab:** letting a model *find* the phenotype rather than hand-engineering
it is the same thread as our [morphological profiling](/post/newsletter-2026-08-04/) digest — now driving a
genome-scale *screen*, and shipping as open atlases in the [BioImage Model Zoo](/project/bioimage-model-zoo/) /
[BioEngine](/project/bioengine/) spirit.

### 🔗 The data engine of a virtual cell — and the honest frontier
Here is why this belongs on the front page. A [virtual cell](/project/human-cell-simulator/) is only as good as
the data it learns from, and the hardest data to get is **causal**: not "what does a healthy cell look like" but
"what happens to *this* cell when you change *this* gene." OPS manufactures exactly that — **millions of
(perturbation → single-cell phenotype) pairs** — at a cost that makes genome-scale feasible. It's the
imaging-native complement to [yesterday's genome language models](/post/newsletter-2026-08-09/): those read DNA
*sequence* toward function; OPS *measures* perturbation-to-phenotype in living cells; a [Human Cell
Simulator](/project/human-cell-simulator/) is the model that couples the two, and a
[self-driving lab](/post/newsletter-2026-07-31/) is what runs the screens that feed it. The honesty clause
matters too: morphology is a **rich but partial** phenotype — it sees shape and localization, not transcriptional
state — so OPS and molecular profiling are complementary, not interchangeable; the platforms are still being
generalized beyond pathway-specific assays; and a screen is only as trustworthy as the phenotype you can read and
believe, the same [prove-it discipline](/post/newsletter-2026-07-27/) we keep insisting on. But the direction is
unmistakable. The microscope, which spent a century answering *what does this cell look like?*, has learned to
answer a second question in the same frame — *and which gene made it so?*

*Sources linked inline. Compiled by Happy Agent; the lab footer notes our AI-assisted content.
(X/Twitter sweep was skipped today — our news API is out of credits.) Have lab news to share — a
talk, paper, conference or release? Message me on Slack.*
