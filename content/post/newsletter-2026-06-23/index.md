---
title: "Lab Newsletter — June 23, 2026"
summary: "This week in AI for life science: agent-readable bioimage AI, a Model Zoo glow-up, the 2026 DDLS postdoc decisions, and foundation models that read cells."
date: '2026-06-23T06:00:00Z'
lastmod: '2026-06-23T06:00:00Z'
draft: false
featured: false
authors:
  - aicell-lab
tags:
  - newsletter
categories:
  - newsletter
---

A short digest of what's caught our eye lately — from our own software stack to the
wider world of AI for cell biology and bioimaging. Everything below links to its
source.

- **BioEngine gets agent-readable.** Our group has a new preprint out,
  [*BioEngine: scalable execution and adaptation of bioimage AI through agent-readable interfaces*](https://www.biorxiv.org/content/10.64898/2026.04.19.719496v1)
  (bioRxiv, April 2026). It describes how BioEngine — built on Hypha — lets both
  people and AI agents run and adapt bioimage AI models through interfaces that
  agents can read and call directly. It's a step toward the kind of autonomous,
  tool-using analysis pipelines we keep gesturing at in this newsletter.

- **A Model Zoo glow-up.** AI4Life ran a week-long hackathon at EMBL Heidelberg to
  upgrade the [BioImage Model Zoo](https://ai4life.eurobioimaging.eu/hackathon-summary-bioimage-model-zoo-enhancements/).
  Highlights: a new internal model uploader (no more leaning on Zenodo) with
  authenticated contributions, CI moved to the `collection-bioimage-io` repo, and
  BioEngine now launchable on Slurm/Apptainer and other HPC backends. One nice
  detail — quantizing a 3D U-Net cut batch inference from 60 ms to 30 ms.

- **2026 DDLS postdoc decisions land.** SciLifeLab and the Wallenberg
  [DDLS Research School](https://www.scilifelab.se/data-driven/ddls-research-school/ddls-research-school-postdoc-call-2026/)
  reach their funding decision on June 15 for the 2026 call: 22 fellowships (15
  academic, 7 industrial), each 2 MSEK over two years, with employment starting
  October 1. Cell & Molecular Biology is one of the four strategic areas — squarely
  the neighbourhood we work in.

- **A single-cell model you can interrogate.** *Nature Communications* published
  [an interpretable single-cell foundation model](https://www.nature.com/articles/s41467-026-70071-5)
  trained on roughly 68 million cells with about 500 million parameters. The pitch
  is interpretability — being able to ask *why* the model places a cell in a given
  state — which matters a lot if these models are to inform real biology rather than
  just rank well on benchmarks.

- **Toward compositional foundation models.** A *Cell Systems* perspective,
  [*From modality-specific to compositional foundation models for cell biology*](https://www.cell.com/cell-systems/abstract/S2405-4712(26)00016-5),
  argues for modular models that compose across modalities — chromatin accessibility,
  protein abundance, spatial transcriptomics, microscopy images, and text — into a
  shared picture of cellular behaviour, rather than training one monolith per data
  type.

**Why it matters for the lab:** agent-readable infrastructure (BioEngine/Hypha) and
the BioImage Model Zoo are exactly the rails the field needs as foundation models for
cells move from single-modality demos toward composable, interpretable systems — and
the DDLS call is where the next people to build them get funded.
