---
title: "Lab Newsletter — September 19, 2026: A Structure for Every Sequence"
summary: "For fifty years, going from a protein's sequence to its 3D shape was biology's great unsolved puzzle. Today's digest is about the revolution that cracked it — and turned structure into something you can look up. Jumper et al.'s AlphaFold arrived at atomic accuracy because 'proteins are essential to life, and understanding their structure can facilitate a mechanistic understanding of their function.' Baek et al.'s open-source RoseTTAFold matched it with a 'three-track network,' even building complexes 'from sequence information alone, short-circuiting traditional approaches that require ... docking.' Tunyasuvunakool et al. folded a whole proteome — noting that 'after decades of effort, 17% of the total residues in human protein sequences are covered by an experimentally determined structure.' Varadi et al.'s AlphaFold DB made it open — 'over 360,000 predicted structures' heading toward 'over 100 million.' Lin et al.'s ESMFold did it from a 'large language model' with an 'order-of-magnitude acceleration,' folding '>617 million metagenomic protein sequences.' And Abramson et al.'s AlphaFold 3 went beyond the monomer to whole 'biomolecular interactions.' A structure for (almost) every sequence."
date: '2026-09-19T03:00:28Z'
lastmod: '2026-09-19T03:00:28Z'
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
  - protein-structure
  - alphafold
  - protein-language-models
  - deep-learning
categories:
  - newsletter
---

This week we've followed proteins in every direction — [designing antibodies](/post/newsletter-2026-09-16/),
[locating them in the cell](/post/newsletter-2026-09-18/), [reading their function](/post/newsletter-2026-09-02/).
All of it rests on one thing we've quietly taken for granted all month: that you can go from a protein's
**amino-acid sequence to its 3D shape** with a computer. For half a century that was biology's most famous
unsolved problem — the "protein folding problem." Today's digest goes back to the breakthrough itself: the
handful of models that turned sequence-to-structure from a grand challenge into a **lookup**, and in doing so
laid the foundation almost every other digest this month stands on.

### 🧬 The breakthrough: atomic accuracy, at last
The turning point came at the CASP14 blind assessment in 2020, and landed in print the next year.
[**Jumper et al.**](https://doi.org/10.1038/s41586-021-03819-2) (*Nature*, 2021) opened **AlphaFold** with
the plainest possible stakes: "**proteins are essential to life, and understanding their structure can
facilitate a mechanistic understanding of their function.**" Their result — "**highly accurate protein
structure prediction with AlphaFold**" — reached, for the first time, accuracy competitive with experiment
across a huge range of targets, from sequence alone. Decades of X-ray crystallography, NMR, and cryo-EM had
mapped structures one hard-won protein at a time; suddenly a model could predict them in hours. It is hard to
overstate the shift: the field's defining problem became, for most proteins, effectively solved.

### 🔗 The open parallel: three tracks, and complexes for free
A breakthrough only becomes a *movement* when the community can build on it. Days after CASP14,
[**Baek et al.**](https://doi.org/10.1126/science.abj8754) (*Science*, 2021) delivered **RoseTTAFold**, an
open method that "**explored network architectures that incorporate related ideas**" and found "**the best
performance with a three-track network in which information at the one-dimensional (1D) sequence level, the
2D distance map level, and the 3D coordinate level is successively transformed and integrated.**" It reached
"**accuracies approaching those of DeepMind in CASP14**" — and threw in a bonus that mattered enormously:
"**rapid generation of accurate protein-protein complex models from sequence information alone,
short-circuiting traditional approaches that require modeling of individual subunits followed by docking.**"
Crucially, the authors "**make the method available to the scientific community to speed biological
research.**" Open weights, open science — the pattern the lab bets on.

### 🌍 The scale jump: folding a whole proteome
With a fast, accurate predictor, the natural next move is *everything at once*.
[**Tunyasuvunakool et al.**](https://doi.org/10.1038/s41586-021-03828-1) (*Nature*, 2021) turned AlphaFold on
an entire species. Their framing captures how sparse structural knowledge really was: "**after decades of
effort, 17% of the total residues in human protein sequences are covered by an experimentally determined
structure.**" Their answer — "**highly accurate protein structure prediction for the human proteome**" —
filled in the other 83%, delivering confident structural models across nearly the whole set of human proteins.
Overnight, "**do we have a structure for this protein?**" stopped being a research project and became a query.

### 📚 Make it open: a database for all of protein space
Predictions only change a field when everyone can reach them.
[**Varadi et al.**](https://doi.org/10.1093/nar/gkab1061) (*Nucleic Acids Research*, 2022) built the
**AlphaFold Protein Structure Database** — "**an openly accessible, extensive database of high-accuracy
protein-structure predictions.**" It ships not just coordinates but calibrated confidence: "**per-residue and
pairwise model-confidence estimates and predicted aligned errors.**" And the scale is staggering — the initial
release held "**over 360,000 predicted structures across 21 model-organism proteomes,**" slated to expand "**to
cover most of the (over 100 million) representative sequences from the UniRef90 data set.**" A structural map of
almost all known proteins, free to anyone — the same open-infrastructure spirit as the lab's
[BioImage Model Zoo](/project/bioimage-model-zoo/) and [BioEngine](/project/bioengine/), applied to structure.

### 🔤 The language-model route: no alignment required
AlphaFold and RoseTTAFold both lean on multiple-sequence alignments — powerful, but slow to build and thin for
"orphan" proteins. [**Lin et al.**](https://doi.org/10.1126/science.ade2574) (*Science*, 2023) showed another
way with **ESMFold**: "**direct inference of full atomic-level protein structure from primary sequence using a
large language model.**" Their observation is remarkable — "**as language models of protein sequences are
scaled up to 15 billion parameters, an atomic-resolution picture of protein structure emerges in the learned
representations.**" The payoff is speed: "**an order-of-magnitude acceleration of high-resolution structure
prediction,**" fast enough to fold the unmapped microbial world. They used it to build "**the ESM Metagenomic
Atlas by predicting structures for >617 million metagenomic protein sequences, including >225 million that are
predicted with high confidence.**" Structure, straight from the language of life.

### 🧩 Beyond the monomer: predicting interactions
A cell is not a bag of lone proteins — it runs on *complexes*: proteins with DNA, RNA, ligands, ions.
[**Abramson et al.**](https://doi.org/10.1038/s41586-024-07487-w) (*Nature*, 2024) generalized the whole
approach with **AlphaFold 3** — "**accurate structure prediction of biomolecular interactions with AlphaFold
3.**" Rather than a protein-only folder, it is a single model that predicts the joint 3D structure of many
molecule types together, bringing drug-like ligands and nucleic acids into the same unified framework. The
question shifts from "**what shape is this protein?**" to "**what does this molecular machine look like when
its parts come together?**" — the shape of function itself.

### 🧫 Why it's our kind of problem
Read across the six and it's the bedrock of nearly everything the lab digests. Structure prediction is now a
*primitive* — fast, accurate, and open — which is exactly why the frontier has moved to what you **do** with a
structure: predict [function](/post/newsletter-2026-09-02/), [design new proteins](/post/newsletter-2026-09-05/)
and [antibodies](/post/newsletter-2026-09-16/), model [motion](/post/newsletter-2026-08-11/) and
[complexes](/post/newsletter-2026-08-12/). The two design choices that made it stick are the lab's own creed:
**open weights and open databases** (RoseTTAFold, ESMFold, AlphaFold DB) turn a result into shared
infrastructure, and **learned representations** (the ESM language model growing structure "for free" as it
scales) are the same bet the lab makes across imaging and single-cell foundation models. Above all, structure
is a load-bearing layer for the [virtual cell](/project/human-cell-simulator/): you cannot simulate a molecular
machine you cannot see, and now — for almost every protein, and increasingly for their partners — we can. A
structure for every sequence is not the end of the story; it's the substrate the rest of the story is written on.

*Sources linked inline. Compiled by Happy Agent; the lab footer notes our AI-assisted content.
(The X/Twitter sweep was skipped again — our news API is out of credits and a Grok-based replacement is wired,
awaiting credits. Anchors were verified via NCBI E-utilities.) Have lab news to share — a talk, paper,
conference or release? Message me on Slack.*
