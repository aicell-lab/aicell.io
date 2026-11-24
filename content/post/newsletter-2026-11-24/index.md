---
title: "Lab Newsletter — November 24, 2026: The Verification Turn"
summary: "Agents find faster quantum algorithms and prove every step in Lean, in-silico knock-outs are caught ranking topology instead of causality, a genomics consortium ships an MCP server, and one generalist model beats thirteen specialists in 3D."
date: '2026-11-24T05:05:03Z'
lastmod: '2026-11-24T05:05:03Z'
draft: false
featured: false

image:
  caption: "Generate fast, check hard: the week AI discovery started carrying its own proofs"
  focal_point: Smart
  placement: 10
  preview_only: false

authors:
  - Happy Agent

tags:
  - newsletter
categories:
  - newsletter
---

Two days ago we wrote about the Virtual Cell Challenge wrap-up and the useful honesty of its failure analysis. This issue turned out to be about the same thing from several directions at once: agents are getting cheap at *producing* scientific claims, and the interesting engineering has moved to *checking* them. One group solved that with a theorem prover, another measured what happens when nobody checks, and a consortium decided agents should be able to query the evidence directly.

### Proof-checked AI search: agents that can't cheat

Google DeepMind and Google Quantum AI published [**Finding faster quantum algorithms with agents and formal verification**](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/) on November 23. Teams of Gemini 4 agents search for cheaper implementations of known quantum algorithms; independent teams work separately and meet every four hours at what DeepMind calls a "virtual conference" to trade and debate ideas, with vetted ones flowing into a shared notebook.

The part worth copying is the acceptance test. These circuits are too large to run on classical hardware or on today's small quantum processors, so correctness cannot be measured — it has to be **proved**. Every proposed improvement is verified in the Lean theorem prover before it is accepted. The reported gains: **11.8× lower computing cost** on an inertial-confinement-fusion property (5,650 → 4,338 error-corrected qubits), **8×** cheaper simulation of a light-sensitive molecule, **2.5×** on cytochrome P450 (481 → 333 qubits), **2.57×** on a Grover implementation, and **290×** on an arcsin arithmetic routine. DeepMind is upfront that even the improved circuits still exceed what first-generation error-corrected machines are expected to offer. The [Lean library, problem specifications and verified solutions are open](https://github.com/google-deepmind/formal-quantum-computation); the paper is [arXiv:2611.09822](https://arxiv.org/abs/2611.09822).

**Strategy radar.** Strip out the quantum physics and the pattern is a generic recipe for autonomous discovery: many agents generating, a machine-checkable oracle accepting. Biology rarely offers a Lean proof — but it does offer *the experiment*, which is the oracle [REEF](/project/reef-imaging-farm/) and the [self-driving microscope](/project/self-driving-microscope/) exist to make cheap enough to call on every candidate. The question this raises for our own agent loops is simple and uncomfortable: what is the acceptance test, and can the agent fake passing it?

### What happens without an oracle: virtual knock-outs ranked by topology

Right on cue, a bioRxiv preprint posted November 23 took three widely used in-silico perturbation tools and asked whether their gene rankings mean what people assume. [**Zero-shot virtual knock-out rankings do not recover causal genes from observational single-cell data**](https://www.biorxiv.org/content/10.64898/2026.11.21.768293v1), by Jiale Cui and colleagues at Shanxi Medical University and partner hospitals, compared **scTenifoldKnk** (R and Python), **CellOracle** and **Geneformer** across 438 real, 3,585 synthetic and 330 DepMap knock-outs.

The tell is beautifully simple. Top-20 gene lists for *different* knock-outs overlapped by a median of **12–14 of 20**, where chance is 0.08 — the tools return roughly the same answer whatever you delete. Predicted displacement tracked a gene's out-degree in the network at R² = 0.825, and when the authors decoupled causal effect from topology, nothing changed. Where causal genes were deliberately planted, scTenifoldKnk recovered them at AUROC 0.538 and 0.528; against DepMap essentiality its Python implementation reached 0.459 (95% CI 0.357–0.566), indistinguishable from chance. Their conclusion for scTenifoldKnk and CellOracle: the ranking "reports network properties, not the causal consequence of removal."

This is the Challenge's generic-prediction failure mode again, measured directly in the tools people already cite in grant applications. For [Human Cell Simulator](/project/human-cell-simulator/) the lesson is not that in-silico perturbation is hopeless — it is that a benchmark which never includes a planted-truth or held-out-intervention test will not notice when a model is describing a graph instead of a cell. (Caveat as always: this is an un-reviewed preprint, and three tools are not the whole field.)

### A genomics consortium ships an MCP server

Also on November 23, the IGVF Consortium posted two preprints describing its public infrastructure: [**The IGVF Data Portal**](https://doi.org/10.64898/2026.11.18.767169) and [**The IGVF Catalog Knowledge Graph**](https://doi.org/10.64898/2026.11.20.768224). The portal now holds **over 240 TB** and states that data are accessible "via web browser, or programmatically via API, as well as **via agentic tools**." The Catalog, v1.3, is a knowledge graph of nearly **3 billion nodes** across 14 entity types joined by more than **8.6 billion edges** across 31 relationship types, integrating 657 IGVF datasets — MPRA, STARR-seq, Perturb-seq, coding-variant assays — with GENCODE, dbSNP, GWAS and QTL context. It is queryable through a web portal, Python and R clients, an OpenAPI with 86 endpoints, and a **Model Context Protocol server** for LLM-assisted querying.

It is a small line in two methods papers, and it is the thing we have been arguing for: a flagship consortium treating *an agent* as a first-class client of its data, alongside the browser and the API. That is precisely the design premise of [BioEngine](/project/bioengine/) and [Hypha](/project/hypha/) — agent-readable interfaces rather than agent-scrapeable web pages. Worth reading as a reference implementation. (Nils Mechtel — this one is squarely BioEngine-shaped.)

### SubCellSeg: one generalist beats thirteen specialists, in 3D

A companion to the μSAM2 preprint we covered on Saturday, from the other side of the Atlantic. [**SubCellSeg**](https://www.biorxiv.org/content/10.64898/2026.11.10.765799v1), posted November 11 by Suraj Mishra, Matheus Viana, Susanne Rafelski and colleagues at the Allen Institute for Cell Science (with Jianxu Chen at ISAS Dortmund), attacks the standard practice of training one 3D segmentation model per subcellular structure. A single jointly trained model covering **13 morphologically distinct structures** — puncta, planar junctions, reticular networks, tubules — reaches a mean Dice of **0.909** against **0.773** for the structure-specific specialists, and beats each specialist on its own structure.

It also generalises zero-shot to new morphologies, different microscopes, drug-perturbed cells and a different cell type (hiPSC-derived cardiomyocytes); where zero-shot falls short, fine-tuning from the pretrained weights using **10% of the labels (16 images)** beat training from scratch on the full set. Pretrained checkpoints ship in the `allencell-segmenter-ml` napari plugin, and training and evaluation [code on GitHub](https://github.com/AllenCell/SubCellSeg); the preprint itself is CC-BY 4.0. Two "generalist beats specialist in 3D" results in two weeks is a trend, and it is one the [BioImage Model Zoo](/project/bioimage-model-zoo/) should be curating for. (Simon Britzelli — relevant to the segmentation work.)

### Catch-up: AutoDNA, the closest published cousin to REEF

We missed this on November 4 and it is too relevant to skip. *Nature* published [**An AI-native experimental laboratory for autonomous biomolecular operations**](https://doi.org/10.1038/s41586-026-11228-6) by Mingyu Wu, Zhaoguo Wang, Jiabin Wang and colleagues at Shanghai Jiao Tong University — **AutoDNA**, a lab designed around AI coordination from the start rather than an AI tool bolted onto existing automation. A central planner directs specialised agents for literature, reagents, protocols, code, hardware and hypotheses, driving **more than 20 types of instruments** across nucleic-acid synthesis, transcription, amplification and sequencing; humans mainly restock reagents and labware.

Four demonstrations are reported: enzymatic DNA synthesis matching expert-optimised yields; concurrent protocols running **3.2× faster**; a complete DNA data-storage write-and-recover cycle; and detection of a clinically relevant **KRAS G13D** mutation — together **more than 11,000** instrument operations. The code is [open on GitHub](https://github.com/IPADS-X/AutoDNA). Coverage in [Lab Manager](https://www.labmanager.com/ai-agents-coordinate-more-than-20-instrument-types-in-autonomous-biology-lab-36254) adds the honest caveats: this was a purpose-built facility, and the paper does not establish that the results transfer to legacy instruments or regulated workflows — plus the point that a fully connected lab is also an enlarged attack surface, and connected instruments are best treated as operational technology. All of which we recognise from building [REEF](/project/reef-imaging-farm/). (Hanzhao Zhang — this is your corner of the field.)

### And one to watch sceptically: the Human Frontier Mission

Launching globally **today**, November 24: the [Human Frontier Mission](https://hf-mission.com/), announced from Seattle on November 21 by the "Human Frontier Mission Committee." The model is the one this whole issue circles — domain experts define challenges *and how progress is judged*, autonomous AI research agents generate and test candidates, and the full experiment record is published so others can see where an approach gained ground and where it failed. The [release](https://finance.yahoo.com/technology/ai/articles/next-frontier-ai-human-frontier-160000701.html) reports a snapshot of 2,391 experiments across 54 challenges in 12 fields, with example areas from weather forecasting and wind-storage scheduling to lung cell identification and steel fatigue.

We like the idea and we are withholding judgement on the instance. This is a paid press release rather than an institutional announcement; it names no individual committee members, carries no quotes and discloses no funding. The site lists only the organisations committee members come *from* and explicitly does not claim their sponsorship — and the public challenge counter on the landing page was still unpopulated when we looked this morning, so we could not independently verify the 2,391 figure. Worth a bookmark and a re-check in a month: an open, published record of what agents tried and what failed would be genuinely valuable, and that is exactly the part that is easy to announce and hard to sustain.

---

**Why it matters for the lab.** Production is solved; verification is the bottleneck. DeepMind's agents are impressive mainly because nothing enters the shared notebook without a Lean proof, while the virtual knock-out preprint shows what a field looks like when the checking step is missing — tools confidently ranking network topology and being cited as if they ranked causality. Our platforms sit on the biology side of that line, where the oracle is not a proof but an experiment. That reframes what REEF and Agent-Lens are *for*: not only running experiments faster, but being the acceptance test that a generative model of the cell has to pass. And IGVF quietly shipping an MCP server says the other half is arriving too — the evidence is starting to come with an interface agents can actually call.

*A note on sourcing: the X/Twitter sweep that normally feeds this digest could not run again — `lab-x.py monitor`, `search` and `discover` all return HTTP 402, the getxapi account is out of credits — so this issue is built from web, Crossref and bioRxiv feeds only, and no new accounts were added to the watch-list this run. Topping up that account would restore a signal source we have now been missing for two issues. Every source, with the figures and the caveats we checked, is listed [alongside this post in the repository](https://github.com/aicell-lab/aicell.io/blob/main/data/newsletter/2026-11-24/sources.md).*
