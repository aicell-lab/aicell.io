# Newsletter sources — 2026-07-14 (fetched UTC 2026-07-14T03:03:52Z)

Theme: AI learns the language of the lab — translating cells into testable hypotheses, human intent into reproducible pipelines, and samples into acquisition decisions.

## Item 1 — A cell-language model proposes a lab-validated cancer lead (C2S-Scale)
- Google blog — https://blog.google/innovation-and-ai/products/google-gemma-ai-cancer-therapy-discovery/ — FETCHED. Cell2Sentence-Scale 27B (C2S-Scale): 27B-param foundation model on Google's open Gemma, by Google DeepMind + Yale; treats single-cell data as "sentences" so LLMs can reason over cells. Tasked to find a "conditional amplifier" of immune signal, it flagged CK2 inhibitor silmitasertib (CX-4945) — predicting increased antigen presentation ONLY in "immune-context-positive" setting. Genuinely novel (CK2 inhibition "has not been reported in the literature to explicitly enhance MHC-I expression"). Validated in UNSEEN human neuroendocrine cells: silmitasertib alone = no effect; low-dose interferon = modest; combined = ~50% synergistic increase in antigen presentation (cold→hot). Open on HuggingFace/GitHub/bioRxiv. Released 17 Oct 2025 (framed as landmark example, not this-week news).
- Coverage: Drug Discovery World — https://www.ddw-online.com/google-ai-model-reveals-new-way-to-improve-immunotherapy-38114-202510/ ; AIM — https://analyticsindiamag.com/ai-news-updates/google-deepmind-and-yale-unveil-27b-parameter-ai-model-that-identifies-new-cancer-therapy-pathway/
- Lab tie-in: virtual cell / Human Cell Simulator /project/human-cell-simulator/ ; ProtiCelli /publication/sun-2026-proteome-wide/

## Item 2 — Plain language -> reproducible image analysis (agentic microscopy)
- Agentic-J (June 2026 preprint; via search) — turns a plain-language request ("segment the nuclei, track the cells, quantify per condition") into executable ImageJ/Fiji workflows; specialized sub-agents for plugin management, code gen, debugging, QA, statistical reporting; every decision logged into a documented, reproducible project.
- "Thinking microscopes" (Georgia Tech; npj Computational Materials 2026) — https://www.nature.com/articles/s41524-026-02077-y — agents embedded in instruments to plan/adapt/analyze.
- Lab tie-in: Agent-Lens /project/agent-lens/ ; ImageJ.JS /project/imagej-js/ ; BioImage.IO Chatbot /project/bioimageio-chatbot/

## Item 3 — Microscopes that decide what to image (self-driving acquisition)
- Self-Driving Microscopes review (Ward et al., Cambridge; Small Methods 2026) — https://onlinelibrary.wiley.com/doi/full/10.1002/smtd.202401757 — ML to automate super-resolution: the microscope decides what/when/how to image; motivation = super-res is laborious, low-throughput, needs frequent manual intervention.
- Self-driving microscopy for protein aggregation (Nature Communications 2025) — https://www.nature.com/articles/s41467-025-60912-0 — label-free, low-light-dose to minimize phototoxicity; captures transient processes in long-term live-cell imaging.
- Lab tie-in: Self-driving Microscope /project/self-driving-microscope/ ; REEF /project/reef-imaging-farm/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- C2S-Scale released Oct 2025; framed as a landmark example of the paradigm, not dated as breaking. Agentic-J grounded via search (no direct URL surfaced); described, not linked. SYNAPS-I real-time engine considered but dropped (fetch 403 + off-domain/beamline).
- Avoided repeating recent digests (Jul 6-13): interactome/AlphaFold, CellVQ, AI drug-discovery economics, Claude Science, AI co-scientists, whole-cell sim, genome FMs.
