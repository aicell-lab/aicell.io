---
title: "Lab Newsletter — November 12, 2026: Virtual Cells Get a War Chest"
summary: "A catch-up issue covering six quiet weeks: $1.8 billion for AI-ready biology, the Virtual Cell Challenge closing its zero-shot round, autonomous labs going industrial, and two dates on our own calendar."
date: '2026-11-12T11:53:25Z'
lastmod: '2026-11-12T11:53:25Z'
draft: false
featured: false

image:
  caption: "Six weeks of AI for life science, caught up in one issue"
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

A confession before the news: this digest has been quiet since September 29. Our nightly pipeline was pointed at an agent runtime that no longer existed after a migration, so it fired faithfully every morning into nothing. That's fixed, and the schedule is running again. Rather than pretend the gap away, here is one catch-up issue covering what we would have written about between then and now.

### Biology's data problem gets a $1.8 billion answer

On October 7, Biohub announced an expansion of its Virtual Biology Initiative into what it calls the largest coordinated commitment to generating AI-ready biological data to date: **$1.8 billion** in money, data, compute and measurement technology. The US Department of Energy brings more than $500 million over five years through its Genesis Mission; the NIH coordinates repositories built on comparable prior investment; Google DeepMind, Isomorphic Labs and Meta add $300 million between them; Biohub itself commits $500 million, with $400 million aimed squarely at new measurement technology — cryo-electron tomography, and microscopy able to image millions to billions of cells in living tissue. The Allen Institute, Broad, Gladstone, the Human Cell Atlas, the Human Protein Atlas and the Wellcome Sanger Institute are shaping strategy. ([Biohub](https://biohub.org/news/virtual-biology-initiative-expansion/))

The framing is worth noticing: the bottleneck named here is not models or compute, but *measurements* — and specifically imaging at scale.

### The Virtual Cell Challenge closed its hardest round yet

Arc Institute's 2026 Virtual Cell Challenge took final submissions on **November 5**, with winners due mid-to-late November. This year's task is genuinely harder than the first: zero-shot prediction of CRISPRi knockdown responses across **six cell lines** from different tissues, where entrants see a new cellular context only unperturbed and never see a measured perturbation response in it. Three lines drive the live leaderboard, three are held back for final scoring, and ranking aggregates six metrics rather than one. For scale, the inaugural round drew over 5,000 registrants from 114 countries. ([Arc Institute](https://arcinstitute.org/news/virtual-cell-challenge-2026))

### Autonomous labs stop being a demo

Also on October 7, Danaher said it will launch its first AI-powered autonomous lab, housed at Abcam and running a continuous design-make-test-learn loop: AI proposes affinity reagents, the lab builds and tests them, results sharpen the next design. Robotic orchestration comes via Automata. The claimed numbers — up to 8× faster discovery, up to tenfold more reagents per year — sit in a press release thick with forward-looking caveats, and operation at scale is only anticipated in early 2027. Still, the shape is the one we recognise from [REEF](/project/reef-imaging-farm/) and the [self-driving microscope](/project/self-driving-microscope/), now with an industrial budget behind it. ([Danaher](https://investors.danaher.com/2026-10-07-Danaher-Accelerates-Life-Sciences-Research-with-New-AI-powered-Autonomous-Lab))

### "Autonomous virtual scientists" gets a literature review

*npj Drug Discovery* published a review on October 12 — Zhao, Fang, Mao and colleagues, *The rise of agentic AI in drug discovery from static tools to autonomous virtual scientists* ([doi:10.1038/s44386-026-00075-0](https://doi.org/10.1038/s44386-026-00075-0)). The title alone marks a shift: the interesting question in the field has moved from *which model* to *which agent architecture*, and from tools a scientist drives to systems that plan their own next experiment. That is the same transition our [autonomous research agents](/project/autonomous-research-agents/) work is chasing from the academic side.

### DDLS met in Stockholm

The fifth **DDLS Annual Conference** gathered over 300 researchers on November 10, across the programme's four strategic areas — infection, cell and molecular biology, evolution and biodiversity, and precision medicine. Heidi Törmänen Persson reported that 43 of a planned 50 Fellows have now started or accepted positions across eleven partner organisations, with a DDLS alumni programme coming in 2027. Johannes Cairns floated a hypothetical "AlphaInfection" — a predictive model of pathogen, microbiota and host. ([SciLifeLab](https://www.scilifelab.se/news/from-tropical-ecology-to-human-health-researchers-meet-at-ddls-annual-conference/))

Timely for us: we have just welcomed [Argyrios Kerezis](/authors/argyrios/) as a DDLS industrial PhD student.

### Two dates from our own corner

**November 18, 14:00 CET** — Joanna Hård is speaking in the RI-SCALE webinar *Making bioimaging data discoverable, accessible and understandable with AI*, alongside Teresa Zulueta-Coarasa of EMBL-EBI's BioImage Archive. The session covers training a foundation model on a large cryo-ET dataset, and AI assistants that help researchers navigate an image archive and run jobs like cell counting and segmentation — territory adjacent to the [BioImage Model Zoo](/project/bioimage-model-zoo/) and the [BioImage.IO Chatbot](/project/bioimageio-chatbot/). ([EGI](https://www.egi.eu/event/webinar-ri-scale-making-bioimaging-data-discoverable-accessible-and-understandable-with-ai))

**November 29** is the deadline for a Digital Futures–funded postdoc in the Koplev Lab at KTH/SciLifeLab, on agentic AI for spatial biology of the human gut — autonomous systems that write and run bioinformatics workflows, judge the output and propose testable hypotheses. It runs in collaboration with our lab. ([posting](https://www.biotecnika.com/agentic-ai-postdoc-kth-scilifelab-sweden/))

---

**Why it matters for the lab.** Two of the biggest stories of these six weeks — a near-$2bn bet whose largest single line item is *measurement*, and an autonomous lab built as a closed design-make-test-learn loop — say that the field's constraint is moving from modelling to the instrumented generation of data. That is precisely the seam our imaging, automation and agent infrastructure sits on.

*A note on sourcing: the X/Twitter sweep that normally feeds this digest could not run — the API account is out of credits — so this issue is built from web and Crossref search only. Sources for every item are listed in the repository alongside this post.*
