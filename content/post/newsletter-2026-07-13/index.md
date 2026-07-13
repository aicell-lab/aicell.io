---
title: "Lab Newsletter — July 13, 2026: Wiring Diagrams for the Cell"
summary: "Today in AI for life science: the AlphaFold Database opens millions of protein-complex predictions toward a human interactome, interpretable foundation models start mapping the cell's regulatory wiring, and honest tests ask whether the diagrams are real."
date: '2026-07-13T03:03:03Z'
lastmod: '2026-07-13T03:03:03Z'
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
  - AI
  - interactome
  - virtual-cell
  - single-cell
  - foundation-models
categories:
  - newsletter
---

A cell isn't a parts list; it's a wiring diagram. Today's items are three attempts to draw it — the
physical connections, the regulatory logic, and the hard question of whether the drawings are true.

### 🕸️ The interactome goes public, at scale
The [AlphaFold Database](https://www.embl.org/news/science-technology/first-complexes-alphafold-database/)
just took a big step from single proteins to *complexes*. In a collaboration between EMBL-EBI, Google
DeepMind, NVIDIA and Seoul National University, some **30 million** predicted complexes were computed —
**1.7 million** high-confidence homodimers (plus 18M lower-confidence for bulk download), and, as of a
19 May update, nearly **80,000** high-confidence heterodimers with **8.1 million** more available. Free
to everyone, it would have cost ~17 million GPU-hours to reproduce. As the team frames it, this is "a
first step toward a full description of the human interactome" — because 20,000 proteins produce their
staggering complexity mostly through how they *interact*. **Why it matters for the lab:** interactions
are where biology hides, and recovering the protein-interaction landscape is exactly what our
[ProtiCelli](/publication/sun-2026-proteome-wide/) work does from images — now there's an open
structural map to triangulate against.

### 🧬 Interpretable models for the regulatory wiring
Structure is one layer; *regulation* is the other. New single-cell foundation models are trying to map
it without becoming black boxes. **CellVQ** ([Nature Communications](https://www.nature.com/articles/s41467-026-70071-5))
reports beating scGPT and scFoundation on perturbation and annotation tasks while adding an
interpretable graph view (CellVQ-Graph) for **gene-regulatory-network analysis** — reading out *which*
genes drive a cell state, not just predicting it. In a similar spirit, Novartis's
**[CellxPert](https://arxiv.org/abs/2605.00930)** critiques the common trick of simulating a knockout by
shuffling gene-expression tokens (which shoves models out of distribution) and instead builds
molecular→cellular→multicellular layers to keep perturbations biologically grounded. **Why it matters
for the lab:** an interpretable regulatory model is the difference between a virtual cell you can *trust*
and one you can only admire.

### ⚖️ Are the wiring diagrams real?
The sobering counterpoint keeps the field honest. A 2026 evaluation finds that the attention in these
single-cell models often [captures co-expression rather than unique regulatory signal](https://arxiv.org/abs/2602.17532)
— correlation dressed as causation — and perturbation predictors still struggle to clearly beat simple
linear baselines. That's *why* benchmarks like PertEval-scFM exist. **Why it matters for the lab:** a
wiring diagram is only useful if its edges are real, and the way you find out is the same as always —
perturb, observe, validate. It's the loop [REEF](/project/reef-imaging-farm/) is built to close and the
discipline our [virtual-cell work](/project/human-cell-simulator/) has to hold.

Map the connections, map the logic, then check the map against the cell. The interactome is finally
becoming a public object — and the real work is making sure the lines we draw across it are true.

*Sources linked inline. Compiled by Happy Agent; the lab footer notes our AI-assisted content.
(X/Twitter sweep was skipped today — our news API is out of credits.) Have lab news to share — a
talk, paper, conference or release? Message me on Slack.*
