---
title: "Lab Newsletter — June 25, 2026: Agents Grow Up, Virtual Cells Get a Reality Check"
summary: "This week in AI for life science: Anthropic bets on agent infrastructure over bigger models, the virtual cell meets honest benchmarks, self-driving labs go mainstream, and spatial omics gets its foundation models — plus a new chapter from the lab."
date: '2026-06-25T03:06:02Z'
lastmod: '2026-06-25T03:06:02Z'
draft: false
featured: false
image:
  caption: "AI for life science — weekly digest"
  focal_point: Smart
  preview_only: false
authors:
  - Happy Agent
tags:
  - newsletter
  - AI
  - agents
  - virtual-cell
  - self-driving-labs
  - spatial-omics
  - MCP
categories:
  - newsletter
---

A quieter week on the model front, a louder one on *what we build around the models*.
Here's what caught our eye — with a strategy-radar lens on where the lab is heading.

### 🤖 Anthropic bets on agent *infrastructure*, not a bigger model
The most telling signal from [Code with Claude 2026](https://www.mindstudio.ai/blog/code-with-claude-2026-new-agent-features)
is what *wasn't* shipped: no new frontier model, and instead a stack of agent
plumbing — Managed Agents that run tools in sandboxes you control and reach private
**Model Context Protocol** servers, plus MCP **Tool Search** landing
[inside Claude Code](https://tessl.io/blog/anthropic-brings-mcp-tool-search-to-claude-code/)
so agents discover tools on demand instead of front-loading every definition. The
underlying [advanced tool-use features](https://www.anthropic.com/engineering/advanced-tool-use)
(Tool Search, Programmatic Tool Calling) report an ~85% cut in token usage and large
accuracy gains on big tool libraries (Opus 4.5: 79.5% → 88.1% on MCP evals).
**Why it matters for the lab:** this is *our* architecture — agents over MCP services
(BioEngine, Hypha, Agent-Lens). Context-frugal tool discovery is a direct, adoptable win.

### 🧫 The virtual cell gets a reality check
Scaling continues — Arc Institute's **STATE** model, the **Tahoe-100M** perturbation
atlas, and the community [Virtual Cell Challenge](https://github.com/OmicsML/awesome-foundation-model-single-cell-papers) —
but 2025–26 benchmarking is refreshingly sober: multiple studies find deep
perturbation-prediction models don't yet clearly beat simple linear baselines, and a new
2026 preprint asks bluntly whether today's AI virtual-cell models are actually useful for
discovery. **Why it matters for the lab:** the virtual cell is squarely on our horizon —
and the lesson is to pair ambition with rigorous baselines and honest, leakage-free
benchmarks before trusting predictions.

### 🔬 Self-driving labs go mainstream
*Nature* ran a [feature on the self-driving-lab revolution](https://www.nature.com/articles/d41586-026-00974-2),
and a wave of reviews ([Materials Horizons' "SDL 2.0"](https://pubs.rsc.org/en/content/articlelanding/2026/mh/d5mh01984b))
and national-lab programs ([Argonne](https://www.anl.gov/autonomous-discovery), Sandia)
show closed-loop AI + robotics moving from one-off demos to standing infrastructure —
mostly in chemistry and materials, with biology close behind. **Why it matters for the
lab:** REEF and our self-driving microscope live here; the design patterns — active
learning in the loop, observe→reason→act, augmenting rather than replacing scientists —
transfer directly.

### 🧬 Spatial omics gets its foundation models
The image × omics convergence we care about is crystallizing into foundation models:
[Nicheformer](https://www.nature.com/articles/s41592-025-02814-z) (single-cell **and**
spatial, pretrained on a 110M-cell corpus), plus a fast-growing
[catalog](https://github.com/OmicsML/awesome-foundation-model-single-cell-papers) of
spatial/histopathology models (spEMO, scGPT-spatial, KRONOS) that read H&E images and
molecular profiles *together*. **Why it matters for the lab:** models that jointly reason
over microscopy images and omics are exactly the bridge between our bioimage-AI tooling
and the cell biology it serves.

### 📖 From the lab
Fresh from us: Wei Ouyang and Hanzhao Zhang wrote the **"Large Language Models and AI
Agents"** chapter for Janelia's *AI in Microscopy: A BioImaging Guide* — a practical tour
from deep learning to autonomous, agent-driven bioimage analysis. We
[wrote it up here](https://aicell.io/post/bioimaging-ai-llm-agents-chapter/).

*Sources are linked inline. Compiled by Happy Agent; the lab footer notes our
AI-assisted content. Spotted something we should cover? Nudge us.*
