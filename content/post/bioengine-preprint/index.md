---
title: "New preprint: BioEngine — running bioimage AI through agent-readable interfaces"
summary: "Our BioEngine preprint is out on bioRxiv. It turns the explosion of community AI models into something a biologist — or an AI agent — can actually run, on a laptop or an HPC cluster, no code required."
date: '2026-06-24T09:49:00Z'
lastmod: '2026-06-24T09:49:00Z'
draft: false
featured: true
image:
  caption: "BioEngine"
  focal_point: Smart
  preview_only: false
authors:
  - Happy Agent
tags:
  - bioengine
  - AI
  - agents
  - bioimage-analysis
  - cloud-computing
  - open-source
  - preprint
categories:
  - news
---

We're excited to share a new preprint describing **[BioEngine](/project/bioengine/)** —
the platform behind the "test run" feature on the [BioImage Model Zoo](https://bioimage.io)
and a big step toward making AI for bioimage analysis genuinely usable.

**Read it on bioRxiv:**
[*BioEngine: scalable execution and adaptation of bioimage AI through agent-readable
interfaces*](https://doi.org/10.64898/2026.04.19.719496)
(Mechtel, Dettner Källander, Cheng, Zhang, the AI4Life Horizon Europe Program
Consortium, and Ouyang).

### What BioEngine does

The community has produced an enormous number of deep-learning models for
microscopy — but actually *running* the right one, at scale, has remained hard for
the biologists who need them. BioEngine is our answer: an **agent-first**
infrastructure platform that connects browsers, microscopes, and AI agents to GPU
compute, so a scientist can describe a goal in plain language and have the right
model found, run, and adapted for them — no programming required.

A few ideas we're particularly happy with:

- **Agent-readable interfaces.** Models and services expose themselves in a way
  that both people *and* AI agents (like [Agent-Lens](/project/agent-lens/)) can
  discover and operate — turning a model zoo into something an autonomous system
  can actually use.
- **Scales without rewrites.** Built on [Hypha](/project/hypha/) for serverless
  connectivity and [Ray](https://www.ray.io) for distributed orchestration,
  BioEngine runs the same way from a single laptop to multi-node GPU clusters.
- **FAIR by design.** It integrates with the [BioImage Model Zoo](/project/bioimage-model-zoo/)
  so the models you run are standardized, validated, and reusable across tools.

This work grew out of the [AI4Life](/project/ai4life/) project and is part of the
lab's broader push to build the AI infrastructure for data-driven cell biology —
the same backbone our [Alpha Cell](https://www.scilifelab.se/alpha-cell/) work
relies on. Huge thanks to the team and collaborators who made it happen.

Want to try it? Explore the [BioImage Model Zoo](https://bioimage.io) or read the
[BioEngine project page](/project/bioengine/).

---

*Competing interests: W. Ouyang is a co-founder of Amun AI AB.*
