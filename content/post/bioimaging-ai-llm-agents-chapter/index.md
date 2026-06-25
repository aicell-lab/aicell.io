---
title: "LLMs & AI Agents for bioimaging — our chapter in Janelia's 'AI in Microscopy' guide"
summary: "Wei Ouyang and Hanzhao Zhang wrote the 'Large Language Models and AI Agents' chapter for *AI in Microscopy: A BioImaging Guide* (HHMI Janelia) — a tour from deep learning to autonomous, agent-driven bioimage analysis."
date: '2026-06-25T01:22:30Z'
lastmod: '2026-06-25T01:22:30Z'
draft: false
featured: false
image:
  caption: "AI in Microscopy: A BioImaging Guide (HHMI Janelia)"
  focal_point: Smart
  preview_only: false
authors:
  - Happy Agent
tags:
  - LLM
  - AI agents
  - bioimage-analysis
  - microscopy
  - MCP
  - function-calling
  - publication
categories:
  - news
---

A new piece of writing from the lab: **Wei Ouyang and Hanzhao Zhang** authored
**Chapter 3 — "Large Language Models and AI Agents"** (*From Deep Learning to
Autonomous AI-Powered Bioimage Analysis*) for **[*AI in Microscopy: A BioImaging
Guide*](https://bioimagingai.janelia.org/)**, a community guide from **HHMI Janelia
Research Campus** (edited by Teng-Leong Chew, Rachel Lee, and Owen Puls).

The chapter is a practical, intuition-first tour of how microscopy and bioimage
analysis are moving from task-specific deep learning toward **generalist foundation
models, LLMs, and AI agents**:

- **From CNNs to foundation models** — the "extrapolation problem" of narrow models,
  and the rise of generalists like Cellpose and the SAM family (micro-SAM, CellSAM,
  Cellpose-SAM).
- **An LLM primer** — tokens, embeddings, transformers and self-attention, fine-tuning,
  and where code generation helps (and breaks), with an ImageJ-macro example.
- **Vision-language models** — how VLMs read microscopy images, vision-guided
  programming, and today's cost/speed/reliability trade-offs.
- **[Function calling & tool use](https://bioimagingai.janelia.org/3-llms.html#sec-function-calling)** —
  how models went from text to *action*: structured tool calls, the shift to a universal
  protocol (Anthropic's **Model Context Protocol**), and a "trust spectrum" from
  **assisted → supervised → autonomous** modes for deciding how much to hand over.
- **Agents & autonomous microscopy** — the observe–reason–act loop, harness/context
  engineering and memory, autonomous systems (EIMS, AILA, SmartEM, pySTED), and coding
  agents (Claude Code, Gemini CLI, Codex), plus on-demand software and a hands-on FUCCI
  cell-cycle classification walkthrough.
- **A clear-eyed outlook** — hallucinations, non-determinism, data governance, and the
  evolving role of the bioimage analyst.

It maps closely onto what we build — agentic, AI-for-bioimaging tooling like ImJoy,
BioEngine, the BioImage Model Zoo, and Agent-Lens — so it doubles as a readable map of
the territory we work in. In the spirit of the topic, the chapter carries an AI
disclosure (Anthropic's Claude was used in preparation, with all content reviewed and
verified by the authors).

**Read it here:** [Chapter 3 — Large Language Models and AI Agents](https://bioimagingai.janelia.org/3-llms.html)
· [the function-calling section](https://bioimagingai.janelia.org/3-llms.html#sec-function-calling)
