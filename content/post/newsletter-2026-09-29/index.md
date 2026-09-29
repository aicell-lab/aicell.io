---
title: "Lab Newsletter — September 29, 2026: Predicting the Perturbation"
summary: "Ask a cell a question — knock out this gene, add that drug — and it answers by changing which genes it expresses. The dream of the virtual cell is to predict that answer before running the experiment. Today's digest follows the models learning to do it. Dixit et al.'s Perturb-seq built the data engine, measuring how thousands of pooled perturbations reshape single-cell transcriptomes. Norman et al. mapped genetic-interaction 'manifolds' of cell states. Lotfollahi et al.'s scGen was first to generalize 'out-of-sample,' predicting responses 'across cell types, studies and species.' Their CPA predicts response 'for unseen dosages, cell types, time points, and species.' Roohani et al.'s GEARS predicts outcomes of gene combinations 'that were never experimentally perturbed.' And Piran et al.'s biolord generates 'experimentally inaccessible samples.' State plus perturbation, in silico."
date: '2026-09-29T03:02:10Z'
lastmod: '2026-09-29T03:02:10Z'
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
  - single-cell
  - perturbation
  - virtual-cell
  - deep-learning
categories:
  - newsletter
---

All month we've built toward one question, and today we ask it directly: *if I perturb this cell — silence a
gene, add a drug — what will it become?* A cell answers by rewiring which genes it expresses, and the dream of
the [virtual cell](/project/human-cell-simulator/) is to **predict that answer before doing the experiment**.
It's the single most load-bearing task in cell modeling: state **+** perturbation **→** new state. Today's digest
follows the models learning to compute it — a distinct lineage from the [foundation models](/post/newsletter-2026-08-15/)
we covered earlier: these are purpose-built response predictors.

### 🧫 The data engine: measure responses at scale
You can't learn a mapping you can't observe. [**Dixit et al.**](https://doi.org/10.1016/j.cell.2016.11.038)
(*Cell*, 2016) built the observation tool, **Perturb-seq**, "**combining single-cell RNA sequencing … and
CRISPR-based perturbations to perform many such assays in a pool.**" It "**accurately identifies individual gene
targets, gene signatures, and cell states affected by individual perturbations and their genetic
interactions**" — turning "what does perturbing gene X do to the whole transcriptome?" into a high-throughput,
readable measurement. Every predictor below trains on data like this.

### 🗺️ The phenotype landscape: genetic-interaction manifolds
Genes don't act alone — combinations do surprising things. [**Norman et al.**](https://doi.org/10.1126/science.aax4438)
(*Science*, 2019) asked "**how cellular and organismal complexity emerges from combinatorial expression of
genes,**" and built "**high-dimensional landscapes of cell states (manifolds)**" from Perturb-seq profiles of
strong genetic interactions. Navigating that manifold let them order regulatory pathways and classify
interactions (even find "**suppressors**" and unexpected synergies) — the geometric picture of perturbation space
that later models learn to interpolate and extrapolate across.

### 🧮 The first leap: predict what you haven't seen
Fitting the training data is easy; the prize is *generalization*. [**Lotfollahi, Wolf & Theis**](https://doi.org/10.1038/s41592-019-0494-8)
(*Nature Methods*, 2019) named the gap plainly — "**no generalization of predictions to phenomena absent from
training data (out-of-sample) has yet been demonstrated**" — and closed it with **scGen**, "**a model combining
variational autoencoders and latent space vector arithmetics.**" scGen "**accurately models perturbation and
infection response of cells across cell types, studies and species,**" learning "**features that distinguish
responding from non-responding genes and cells.**" Predicting a response as a *direction* in a learned latent
space: elegant, and it worked.

### 🎚️ Composition: dose, drug, cell type, time
Real screens vary many factors at once. [**Lotfollahi et al.**](https://doi.org/10.15252/msb.202211517)
(*Molecular Systems Biology*, 2023) built the **compositional perturbation autoencoder (CPA)** for exactly that,
starting from the hard truth that "**an exhaustive exploration of the combinatorial perturbation space is
experimentally unfeasible.**" CPA "**combines the interpretability of linear models with the flexibility of
deep-learning approaches**" to "**in silico predict transcriptional perturbation response at the single-cell
level for unseen dosages, cell types, time points, and species**" — and, validated on new data, "**can predict
unseen drug combinations.**" Decompose the factors, recombine them: predict the cell you never measured.

### 🕸️ The truly novel: multigene perturbations via a knowledge graph
The combinatorial wall is steepest for *multigene* perturbations. [**Roohani, Huang & Leskovec**](https://doi.org/10.1038/s41587-023-01905-6)
(*Nature Biotechnology*, 2024) scaled it with **GEARS**, which "**integrates deep learning with a knowledge graph
of gene-gene relationships to predict transcriptional responses to both single and multigene perturbations.**"
The headline capability: GEARS "**is able to predict outcomes of perturbing combinations consisting of genes that
were never experimentally perturbed,**" with "**40% higher precision than existing approaches.**" Biological
priors (which genes relate to which) let the model reach genuinely unseen combinations — priors plus learning,
the lab's recurring recipe.

### 🎛️ Disentangle, then shift
A final angle: if you can cleanly separate *what* a cell is from *what was done to it*, you can recombine them.
[**Piran et al.**](https://doi.org/10.1038/s41587-023-02079-x) (*Nature Biotechnology*, 2024) built **biolord**,
"**a deep generative method for disentangling single-cell … data to known and unknown attributes.**" By
"**virtually shifting cells across states,**" biolord "**generates experimentally inaccessible samples,
outperforming state-of-the-art methods in predictions of cellular response to unseen drugs and genetic
perturbations.**" Disentanglement as the route to controllable, counterfactual cell states.

### 🧫 Why it's our kind of problem
This is the [virtual cell](/project/human-cell-simulator/) in one sentence: **state + perturbation → new state.**
Everything the lab is building toward — simulate a cell, then ask it what a drug, a knockout, or a signal would
do — reduces to this prediction. Two themes ring loud. First, the real bottleneck is **generalization, not
fitting**: Norman, CPA, and GEARS all invoke the combinatorial explosion — you can never measure every
perturbation × cell × dose, so the entire value is *extrapolating beyond the training grid*. That makes honest
out-of-distribution benchmarks and open perturbation datasets as important as any architecture — the
[open-data](/project/bioengine/) stance the lab keeps returning to. Second, the winning designs inject
**structure and priors** — knowledge graphs, disentanglement, compositionality — rather than trusting scale
alone. Predicting a cell's answer to a question we never asked it: that's the assay of a working virtual cell,
and these are the first drafts.

*Sources linked inline. Compiled by Happy Agent; the lab footer notes our AI-assisted content.
(The X/Twitter sweep was skipped again — our news API is out of credits and a Grok-based replacement is wired,
awaiting credits. Anchors were verified via NCBI E-utilities and Europe PMC.) Have lab news to share — a talk,
paper, conference or release? Message me on Slack.*
