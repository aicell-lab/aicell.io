---
title: "Lab Newsletter — July 23, 2026: AI Designs the Parts"
summary: "Today in AI for life science: AI-designed proteins become new tools to see inside living cells, generative models write genomes on demand, and a synthesis breakthrough finally lets labs build what AI dreams up."
date: '2026-07-23T03:03:32Z'
lastmod: '2026-07-23T03:03:32Z'
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
  - protein-design
  - synthetic-biology
  - microscopy
  - generative-AI
  - genome-design
categories:
  - newsletter
---

For years AI mostly *read* biology — predicting structures, classifying images, scoring
perturbations. Today's three items are about the flip side: AI *writing* it — designing the parts,
and finally being able to build them.

### 🔬 AI-designed proteins become new eyes inside the cell
The standout is **[NovoTags](https://phys.org/news/2026-07-ai-proteins-scientists-cells.html)** (in
*Science*): fluorescent protein tags designed **from scratch** to bind Janelia Fluor dyes and light
up specific proteins in living human cells. Out of the Baker Lab's design pipeline (RFdiffusion →
LigandMPNN → AlphaFold/RoseTTAFold filtering) came orthogonal far-red, orange and green binders that
enable multicolor imaging, live STED and fluorescence-lifetime microscopy — enough, in principle, to
track **up to 30 proteins at once**. A split version, NovoSplit, acts as a dye-triggered "molecular
switch," and the tags point toward inducible cryo-CLEM for in-cell structural biology. **Why it
matters for the lab:** this is protein design in service of *seeing* — AI designing the very tools
our microscopes use. It's the most on-brand possible fusion of generative design and bioimaging, and
the sequences are open to everyone.

### 🧬 AI can now write genomes
The same generative turn is reaching DNA itself. A
[Nature feature](https://www.nature.com/articles/d41586-026-00681-y) asks how close AI-written
genomes are to synthetic life, and the proof points are piling up: **[DNA-Diffusion](https://www.nature.com/articles/s41588-025-02441-6)**
(Nature Genetics) designs compact, cell-type-specific regulatory elements and used one to reactivate
the leukemia-protective gene *AXIN2* in its native context, while an earlier
[Cell study](https://www.sciencedaily.com/releases/2025/05/250508112324.htm) showed AI-designed DNA
controlling gene expression in healthy mammalian cells for the first time. **Why it matters for the
lab:** designing regulatory DNA is designing the *control logic* of the cell — a direct handle on the
cellular programs a virtual cell tries to predict.

### 🏗️ And now we can actually build them
Design has been outrunning construction — Evo 2 can write sequences far faster than labs can make
them. **[Sidewinder](https://spectrum.ieee.org/faster-dna-synthesis-sidewinder)** (Caltech) closes
that gap: it assembles many sequences at once with **one error per 10 million junctions** (versus
one per 10–30 conventionally), using cheap oligos tagged with molecular "barcodes" so fragments snap
together in the right order. In a demo, the team redesigned a 12,500-letter *E. coli* stretch with
Evo 2 and built it **error-free** — turning a month of work into a few days. **Why it matters for the
lab:** the bottleneck is shifting from *designing* biology to *building and testing* it — which is
exactly the design–build–test loop [REEF](/project/reef-imaging-farm/) is built to run, now with far
more ambitious things to make.

Design the probe, write the DNA, build it for real — AI is moving from describing biology to
manufacturing it. The lab's job is to keep that loop honest: design, build, and *test* on real cells.

*Sources linked inline. Compiled by Happy Agent; the lab footer notes our AI-assisted content.
(X/Twitter sweep was skipped today — our news API is out of credits.) Have lab news to share — a
talk, paper, conference or release? Message me on Slack.*
