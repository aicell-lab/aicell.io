---
title: "Lab Newsletter — September 18, 2026: Where Proteins Live"
summary: "A protein's job depends on its address — the same molecule means one thing in the nucleus and another at the membrane. Today's digest is about teaching machines to find that address, and it runs close to the lab's own roots in the Human Protein Atlas. Almagro Armenteros et al.'s DeepLoc predicted localization 'relying only on sequence information,' using 'a recurrent neural network … and an attention mechanism.' Stärk et al. swapped alignments for language-model embeddings, their 'light attention' beating the state of the art 'by about 8 percentage points.' DeepLoc 2.0 went multi-label with protein language models and 'highly accurate prediction of nine different types of protein sorting signals.' On the image side, Sullivan et al. turned the HPA Cell Atlas into a video-game mini-game — '322,006 gamers' making 'nearly 33 million classifications.' Ouyang et al. ran the HPA competition, where '2,172 teams' produced models that beat the prior effort 'by ~20%.' And Kobayashi et al.'s cytoself learned a localization atlas 'fully self-supervised,' 'from coarse classes … to the subtle localization signatures of individual protein complexes.' Every protein has an address — and we can predict it."
date: '2026-09-18T03:00:15Z'
lastmod: '2026-09-18T03:00:15Z'
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
  - subcellular-localization
  - bioimaging
  - protein-atlas
  - deep-learning
categories:
  - newsletter
---

This week we've watched AI design [antibodies](/post/newsletter-2026-09-16/) and
[plan syntheses](/post/newsletter-2026-09-17/). Today we come home — to a question the lab has
worked on since its beginning: **where in the cell does a protein live?** A kinase at the plasma
membrane, in the nucleus, or in a mislocalized aggregate is, functionally, three different stories;
the same amino-acid sequence can mean health or disease depending on its *address*. Mapping that
address across the whole proteome is the mission of the [Human Protein Atlas](https://www.proteinatlas.org)
Cell Atlas — and today's digest traces how deep learning learned to **predict subcellular
localization**, from sequence and from images.

### 🧬 The founding move: localization from sequence alone
Classical predictors leaned on annotated homologues — useless for a truly novel protein.
[**Almagro Armenteros et al.**](https://doi.org/10.1093/bioinformatics/btx431) (*Bioinformatics*,
2017) set out from exactly that gap: "**for novel proteins where no annotated homologues exist, and
for predicting the effects of sequence variants, it is desirable to have methods for predicting
protein properties from sequence information only.**" Their **DeepLoc** answered with "**deep neural
networks to predict protein subcellular localization relying only on sequence information.**" At its
core is "**a recurrent neural network that processes the entire protein sequence and an attention
mechanism identifying protein regions important for the subcellular localization.**" No database
lookup — just the sequence, and a model that points to *which residues* decide the destination.

### 🗣️ The language of life replaces the alignment
DeepLoc still needed rich evolutionary features. [**Stärk et al.**](https://doi.org/10.1093/bioadv/vbab035)
(*Bioinformatics Advances*, 2021) removed that cost by leaning on protein language models. They noted
the bottleneck — machine learning "**narrows the gap through predictions from expert-designed input
features leveraging information from multiple sequence alignments (MSAs) that is resource expensive to
generate**" — then showed "**embeddings from protein language models for competitive localization
prediction without MSAs.**" Their architecture, a "**softmax weighted aggregation mechanism with linear
complexity in sequence length referred to as light attention,**" "**significantly outperformed the
state-of-the-art … by about 8 percentage points (Q10).**" A pretrained language model, it turns out,
already knows a great deal about where a protein goes.

### 🏷️ Many addresses at once, and *why*
Real proteins often live in more than one place, and a good predictor should say so — and explain
itself. [**Thumuluri et al.**](https://doi.org/10.1093/nar/gkac278) (*Nucleic Acids Research*, 2022)
delivered that with **DeepLoc 2.0**, "**an update to the popular tool DeepLoc with multi-localization
prediction and improvements in both performance and interpretability.**" It "**achieve[s]
state-of-the-art performance … by using a pre-trained protein language model,**" and, usefully, "**uses
sequence input rather than relying on slower protein profiles.**" Two interpretability wins matter for
biology: "**an attention output along the sequence and highly accurate prediction of nine different
types of protein sorting signals**" — the model doesn't just name the compartment, it points to the
address label the cell itself reads.

### 🎮 The image side, at planetary scale: citizen science
Sequence is only half the story — the Cell Atlas is built from *microscopy images*, and annotating
them is a mountain of work. [**Sullivan et al.**](https://doi.org/10.1038/nbt.4225) (*Nature
Biotechnology*, 2018) met it with a genuinely unusual pairing. Using "**the publicly available data
set from the Cell Atlas of the Human Protein Atlas,**" they "**integrated an image-classification task
into a mainstream video game (EVE Online) as a mini-game, named Project Discovery.**" The scale is
staggering: "**participation by 322,006 gamers over 1 year provided nearly 33 million classifications
of subcellular localization patterns, including patterns that were not previously annotated by the
HPA.**" They paired the crowd with a machine — "**an automated Localization Cellular Annotation Tool
(Loc-CAT)**" that "**classifies proteins into 29 subcellular localization patterns and can deal
efficiently with multi-localization proteins.**" Humans and models, learning the cell together.

### 🏆 A community benchmark for the hardest patterns
To push the image models further, the HPA turned the problem into an open competition.
[**Ouyang et al.**](https://doi.org/10.1038/s41592-019-0658-6) (*Nature Methods*, 2019) — work from
our own group — analyzed it: "**pinpointing subcellular protein localizations from microscopy images
is easy to the trained eye, but challenging to automate.**" The response was enormous — "**over 3
months, 2,172 teams participated,**" wrestling with "**training on highly imbalanced classes and
predicting multiple labels per image.**" The payoff was real progress: "**the winning models far
outperformed our previous effort at multi-label classification of protein localization patterns by
~20%,**" and, importantly, "**these models can be used as classifiers to annotate new images, feature
extractors to measure pattern similarity or pretrained**" networks — reusable infrastructure, not just
a leaderboard. A benchmark that left the field better armed.

### 🧠 No labels at all: a self-supervised atlas of localization
The frontier is learning localization *without* the labels entirely. [**Kobayashi et al.**](https://doi.org/10.1038/s41592-022-01541-z)
(*Nature Methods*, 2022) reached it with **cytoself**, "**a deep-learning approach for fully
self-supervised protein localization profiling and clustering**" whose "**self-supervised training
scheme … does not require preexisting knowledge, categories or annotations.**" Trained "**on images of
1,311 endogenously labeled proteins from the OpenCell database,**" cytoself "**reveals a highly resolved
protein localization atlas that recapitulates major scales of cellular organization, from coarse
classes, such as nuclear and cytoplasmic, to the subtle localization signatures of individual protein
complexes.**" A model that discovers the cell's spatial vocabulary on its own — and clusters proteins
into organelles and complexes it was never told about.

### 🧫 Why it's our kind of problem
Read across the six and the arc is the lab's own history and future in one line: **from sequence-only
predictors to language-model embeddings, and from hand-labeled images to community-scale annotation to
fully self-supervised atlases.** This is where much of the lab's science begins — the
[Human Protein Atlas](https://www.proteinatlas.org) Cell Atlas — and it threads directly into what the
lab builds now: the same imaging that feeds [Agent-Lens](/project/agent-lens/) and the
[REEF farm](/project/reef-imaging-farm/) is exactly what these localization models consume, and open,
reusable classifiers are the [BioImage Model Zoo](/project/bioimage-model-zoo/) and
[BioEngine](/project/bioengine/) idea in miniature. The move toward *self-supervised* representations
(cytoself, the language-model localizers) is the same bet the lab makes across
[single-cell](/post/newsletter-2026-09-03/) and imaging foundation models. And above all, localization
is a load-bearing layer for the [virtual cell](/project/human-cell-simulator/): you cannot simulate a
cell you cannot spatially map. Knowing *where* every protein lives — and how that changes with
state — is a prerequisite for modeling *what the cell does*. The address is part of the function.

*Sources linked inline. Compiled by Happy Agent; the lab footer notes our AI-assisted content.
(The X/Twitter sweep was skipped again — our news API is out of credits and a Grok-based replacement is
wired, awaiting credits. Anchors were verified via NCBI E-utilities.) Have lab news to share — a talk,
paper, conference or release? Message me on Slack.*
