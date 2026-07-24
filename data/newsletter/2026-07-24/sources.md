# Newsletter sources — 2026-07-24 (fetched UTC 2026-07-24T03:03:29Z)

Theme: Open by design — a real contest is forming over whether science's AI stack (workbenches, agents, models) is open and model-agnostic or vendor-owned, and why the lab bets open.

## Item 1 — OpenScience: an open, model-agnostic science workbench
- MarkTechPost (5 Jul 2026) — https://www.marktechpost.com/2026/07/05/synthetic-sciences-releases-openscience-an-open-source-model-agnostic-ai-workbench-for-machine-learning-biology-physics-and-chemistry-research/ — FETCHED. OpenScience (Synthetic Sciences): open-source (Apache-2.0), browser workbench + local agent runtime; runs on your own infra with your own API keys, no account needed ("your keys stay on your machine"); model-agnostic, routed per-request (Claude/GPT/Gemini/GLM/Kimi/DeepSeek/local fine-tunes). Full research loop in one session: literature, hypothesis, code, experiment, analysis, write-up. 250+ editable skills; 30+ scientific databases as tools (UniProt, PDB, ChEMBL, arXiv...); specialist agents (research/biology/physics/ml). Explicitly positioned as the open alternative to Anthropic's Claude Science (proprietary, Claude-only, 60+ curated skills, runs on lab machines). Noted weakness: agent not sandboxed (use containers/VMs). Install: npm i -g @synsci/openscience.
- Claude Science (for contrast) — https://www.anthropic.com/news/claude-science-ai-workbench

## Item 2 — The contest: open vs proprietary (and open can be frontier)
- Same MarkTechPost comparison: both run the loop / render science inline / prioritize reproducibility; core difference = "openness and model choice."
- Open agents can be frontier: Biomni (general-purpose biomedical AI agent, Science 2026; open) — https://biomni.stanford.edu ; Agentic-J (open multi-agent ImageJ/Fiji assistant) — https://arxiv.org/abs/2606.02080 ; broad open-agent ecosystem — https://github.com/caramaschiHG/awesome-ai-agents-2026
- Lab tie-in: open, agent-readable infra — BioEngine /project/bioengine/ ; Hypha /project/hypha/

## Item 3 — Why the lab bets open: access, sovereignty, reproducibility
- "Open biology and AI: need for the Global South" — MR Online (21 Jul 2026, perspective) — https://mronline.org/2026/07/21/open-biology-and-ai-need-for-the-global-south/ — equity/access argument for open scientific AI.
- Model-agnostic + local-data + open-source = data sovereignty, no vendor lock-in, deployability at one's own institute; reproducibility.
- Lab tie-in: ImJoy (runs in the browser, no install) /project/imjoy/ ; BioImage Model Zoo (free, testable in-browser) /project/bioimage-model-zoo/ ; BioEngine (deployable at a facility's own institute) /project/bioengine/ ; BioImage.IO Chatbot /project/bioimageio-chatbot/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- Biomni was covered in depth in the Jul 15 digest; referenced here as an example of open agents, not re-reported. MR Online item is a perspective/opinion piece (framing, not a result). OpenScience specifics are reported claims from the fetched source.
- Avoided repeating recent digests (Jul 17-23): NovoTags/genome-writing, protein dynamics, microscopy VLMs, enzyme design, segmentation FMs, LAP/agent-instrument.
