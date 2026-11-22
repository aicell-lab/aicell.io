---
title: "Lab Newsletter — November 22, 2026: The Virtual Cell Gets Its Report Card"
summary: "A challenge winner closes 44% of the gap to a real experiment, μSAM2 takes segmentation into 3D, autonomous labs become a national challenge, and 25.5 million brain cells go public."
date: '2026-11-22T05:08:05Z'
lastmod: '2026-11-22T05:08:05Z'
draft: false
featured: false

image:
  caption: "Scoring the virtual cell: a benchmark, a microscope and a national challenge"
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

Ten days ago we wrote that the Virtual Cell Challenge had closed its hardest round and that winners were due. They arrived — along with the most useful thing a competition can produce, which is a clear account of what did *not* work. Plus a segmentation foundation model that finally takes the third dimension seriously, autonomous labs promoted to a national challenge, and a quarter of a brain's worth of cells released to anyone who wants them.

### The virtual cell gets scored — and the score is honest

Arc Institute published the [2026 Virtual Cell Challenge wrap-up](https://arcinstitute.org/news/virtual-cell-challenge-2026-wrap-up) on November 19. **Illumina's BioInsight AI Lab took first place** and $100,000 with a score of 0.4399; **FlowState**, two independent researchers, took second ($50,000, 0.3348); and **X-team** from Xaira Therapeutics took third ($25,000, 0.3263). Prizes were split between cash and NVIDIA Brev credits. Participation was serious: more than 5,441 people registered, 1,469 teams pushed 26,827 entries at the validation leaderboard, and 805 teams filed a final entry. ([Illumina's own account](https://www.prnewswire.com/news-releases/illumina-wins-virtual-cell-challenge-powered-by-billion-cell-atlas-302946270.html); [GenomeWeb](https://www.genomeweb.com/technology/sequencing/single-cell/gnw-virtual-cell-challenge-winners-20261120/); [TIME](https://time.com/article/2026/11/20/scientists-are-pursuing-the-dream-of-a-virtual-cell/))

What we appreciate is that Arc refuses to let 0.44 be read as 44% correct. The scale puts 0 at the cell-context mean and 1 at an *independent replicate of the real experiment*, so the winning entry closed 44% of the distance between "assume nothing happened" and "do the experiment twice" — and Arc states plainly this does "not represent accuracy."

Three findings are worth carrying around:

- **Reference data beat architecture.** All three podium pipelines were modular rather than end-to-end, and all three worked by transferring *measured* responses from other cell lines into the new one. The winner's CellularAI is a statistical transfer framework — covariate-adjusted regression for per-gene log fold changes, random-effects meta-analysis weighted by control-cell similarity, then SVD plus ridge regression to adapt to the held-out line.
- **Private data was not required.** FlowState reached second place on public data alone: 222 perturbation-response datasets from 128 studies covering 86 cellular contexts.
- **The models are still too generic.** Predicted cross-line cosine similarity ran 0.77–0.89 where the measured value was 0.55; line-specific slopes came in at 0.02–0.13 against 1.02 for a true replicate. And everyone over-called differential expression — measured medians were 22–44 genes per target, while entries called anywhere from 122 to 4,200.

In other words: today's virtual cells are good at the average cell and bad at *this* cell. That gap is a measurement problem as much as a modelling one, which is exactly the seam our [Human Cell Simulator](/project/human-cell-simulator/) work sits on. The Challenge returns next summer.

### μSAM2: segmentation stops pretending biology is flat

Anwai Archit, Constantin Pape and 12 colleagues in Göttingen, Würzburg, Singapore and Sydney posted [**Segment Anything for Microscopy 2**](https://www.biorxiv.org/content/10.64898/2026.11.12.766082v1) on November 17. It adapts SAM2 to **joint 2D and 3D segmentation** across light *and* electron microscopy, and widens the job description: automatic and interactive segmentation, dedicated mitochondria and nuclei models for EM, pixel and object classification from few annotations, and cell tracking in 2D and 3D time-lapse. Training annotations covered more than 23 million cells and nuclei and 1.6 million cellular structures, and everything ships in the μSAM napari plugin.

The framing is a fair criticism of where we all were: prior image foundation models were trained on 2D, struggled with volumetric structure, and covered a narrow band of tasks. Volumetric data is where most of our users actually live, so this is close to home for the [BioImage Model Zoo](/project/bioimage-model-zoo/) — μSAM's lineage runs through our [AI4Life](/project/ai4life/) collaboration with the Pape group. One caveat: the preprint abstract makes state-of-the-art claims without published benchmark numbers, so the comparison tables are worth reading in the full text before anyone quotes a figure. Simon Britzelli's SAM work is the obvious place for this to land.

### "AI-driven autonomous laboratories" is now a national challenge

The US Department of Energy's Genesis Mission published its slate of [National Science and Technology Challenges](https://www.energy.gov/undersecretaryforscience/genesis-mission/genesis-mission-national-science-and-technology-challenges) across November 13 and 16. Two names stand out from a list otherwise occupied by grids, reactors and critical minerals: **"Achieving AI-Driven Autonomous Laboratories"** (posted November 16) and **"Scaling the Biotechnology Revolution"** (November 13). The biotechnology challenge describes AI integrating genomics, multi-omics, imaging, dynamics and phenomics data to establish genotype–phenotype relationships *and steer autonomous experiments*; the autonomous-laboratories challenge is about automating experimental workflows so they generate more data for models and produce more repeatable experiments.

**Strategy radar:** when a national programme writes down "autonomous laboratories" as a named objective alongside the power grid, the architecture we have been building in [REEF](/project/reef-imaging-farm/) and the [self-driving microscope](/project/self-driving-microscope/) stops being a research bet and starts being infrastructure other people will specify requirements for. Worth watching what interfaces and standards come out of it.

### A funded, closed-loop lab for mRNA formulation

A smaller and more concrete version of the same idea landed in Eindhoven. On November 19, TU/e announced that Nadia Erkamp, Tom de Greef and the startup Nanoworx won a **€500,000 ChemistryNL PPS-I grant** for a [self-driving laboratory for autonomous lipid-nanoparticle development](https://www.tue.nl/en/news-and-events/news-overview/19-11-2026-chemistrynl-grant-for-self-driving-laboratory-to-accelerate-mrna-medicine-development) — the carriers that get mRNA into cells. Robotic experimentation is paired with Bayesian optimisation, so the system chooses the next formulation, assesses several properties at once and drops weak candidates early. The target is to compress optimisation from months to weeks while cutting material use by roughly 90%.

De Greef's framing is the cleanest one-line case for this whole field we have read lately: *"AI can now generate new ideas faster than any scientist could ever test them. In biology, though, an idea only counts once it has been proven in the lab."*

### 25.5 million cells, openly shared

On November 12 the BRAIN Initiative Cell Atlas Network released its first major output: a cross-species cellular atlas of the **basal ganglia**, in a package of 26 studies across *Cell Press* journals, from a consortium of more than 50 institutions in nine countries. The numbers: **25.5 million cells** molecularly profiled — 21.0 million human, 3.0 million macaque, 1.5 million marmoset — plus a Slide-tags striatum map that places 92,100 cells back in their original positions. Findings include a new neuron type (STR D2 SMYD2-HTR7) carrying elevated schizophrenia risk, six molecular zones in the human striatum, and evidence that cell-type expression can predict age. All of it is being shared openly through brain-bican.org with tools to visualise and map new data onto the reference. ([Allen Institute](https://alleninstitute.org/news/scientists-create-landmark-cellular-atlas-of-one-of-the-brains-most-important-regions); milestone paper: Ecker et al., *"From the human genome to the human brain cell atlas," Cell*, November 12, 2026)

The same day, *Nature Methods* published [PANGEA](https://www.nature.com/articles/s41592-026-03295-4), a remapped human cell atlas of 12.6 million cells used to categorise multicellular disease responses. Two reference atlases in one day is a reminder of which side of the virtual-cell equation is currently moving fastest.

### On the tools we build with

Four frontier models landed inside this window. The one with a primary announcement worth linking is Google's [Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) on November 18, pitched at fast end-to-end task completion across complex software work. For a lab whose platforms — [Hypha](/project/hypha/), [BioEngine](/project/bioengine/), [Agent-Lens](/project/agent-lens/) — are increasingly driven by agents rather than people, the relevant metric is no longer chat quality but how reliably a model finishes a long tool-using task without supervision. Worth a re-benchmark of our own agent loops.

---

**Why it matters for the lab.** The Challenge wrap-up and the brain atlas point the same direction from opposite ends. The best virtual-cell models won by carefully transferring *measured* responses, and they still fail at context specificity; meanwhile the biggest releases of the fortnight were measurements — 25.5 million cells, openly shared. The binding constraint on a virtual cell is still data from real instruments, and the leverage sits with whoever can generate it in a closed loop. That is the bet behind REEF, Agent-Lens and the self-driving microscope, and this fortnight a national programme and a Dutch consortium placed it too.

*A note on sourcing: the X/Twitter sweep that normally feeds this digest could not run — the getxapi account returned HTTP 402, out of credits — so this issue is built from web and Crossref search only, and no new accounts were added to the watch-list this run. Every source is listed in the repository alongside this post.*
