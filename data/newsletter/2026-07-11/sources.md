# Newsletter sources — 2026-07-11 (fetched UTC 2026-07-11T03:04:22Z)

Theme: AI gets wired into the lab — not just bigger models, but AI plumbed into scientific data (MCP connectors) and into design tasks (RNA drugs, CRISPR edits).

## Item 1 — AI plugs into scientific data & tools (Claude Science + the connector wave)
- Claude Science (Anthropic), launched 30 June 2026 — https://www.anthropic.com/news/claude-science-ai-workbench ; HPCwire — https://www.hpcwire.com/aiwire/2026/06/30/anthropic-launches-claude-science-ai-workbench-for-scientific-research/ — AI workbench for scientists; auditable artifacts, compute access; preconfigured MCP connectors (PubMed, bioRxiv, 10x Genomics Cloud, Benchling, ClinicalTrials.gov).
- Claude for Life Sciences (Oct 2025) + JPM 2026 expansion — https://www.anthropic.com/news/claude-for-life-sciences — MCP connectors: Benchling, 10x Genomics (single-cell/spatial in natural language), PubMed, BioRender, Synapse.org, Wiley Scholar Gateway; JPM'26 added Medidata, ClinicalTrials.gov, ToolUniverse (600+ tools), bioRxiv/medRxiv, ChEMBL, Owkin (Pathology Explorer), Open Targets. KEY: biomedical capability "comes from prompting, tools, and connectors layered on a general-purpose Claude rather than from specialized biology weights."
- Balance: OpenAI + Anthropic both shipping life-sciences/health connectors — https://blog.stephenturner.us/p/openai-anthropic-chatgpt-claude-health-life-sciences
- Caveat: headline metrics are self-reported (per the writeup).
- Lab tie-in: agent-readable interfaces = BioEngine /project/bioengine/ ; Hypha /project/hypha/ ; BioImage.IO Chatbot /project/bioimageio-chatbot/ (Happy Agent itself runs on Claude).

## Item 2 — AI moves into RNA drug design
- news-medical (Yan et al., Engineering 2025, DOI 10.1016/j.eng.2025.06.029) — https://www.news-medical.net/news/20251231/Artificial-intelligence-unlocks-new-frontiers-in-RNA-drug-design.aspx — FETCHED. Three AI strategies (data-driven; RL/causal; deep-learning/LLM for long RNA + de novo functional RNA design). Alnylam: RNAi phase-1→3 transition 64.4% vs 5–7% for traditional drugs; discovery in months. Vision: editable RNA generation platform, personalized RNA drugs, closed loop (digitize → design → assess → automated synthesis → validation → delivery).

## Item 3 — ...and into designing the edit (AI × CRISPR)
- labiotech "CRISPR + AI" — https://www.labiotech.eu/in-depth/crispr-ai/ (direct fetch 403; grounded via search). AI for guide-RNA design, base/prime editing precision, off-target prediction, novel-editor discovery; explainable AI (XAI) for off-target safety.
- Nature Reviews Genetics 2025 review "Harnessing AI to advance CRISPR-based genome editing" — https://www.nature.com/articles/s41576-025-00907-1
- TIGER (NYU/Columbia; Sanjana + Knowles) — deep-learning model for RNA-targeting CRISPR (Cas13) guide design; first to predict on- AND off-target activity.
- Lab tie-in: target selection / functional-outcome prediction via virtual-cell models — Human Cell Simulator /project/human-cell-simulator/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- Item 3 primary (labiotech) + Science interactome perspective (adx7802) were fetch-blocked (403); grounded via search excerpts with named sources. No fabrication.
- Avoided repeating recent digests (Jul 3–10): AI co-scientists, cryoAgent, whole-cell sim, genome FMs, HEX, organoids, virtual-cell FMs/baselines, open-weight models, Biohub.
