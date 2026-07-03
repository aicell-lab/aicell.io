# Newsletter sources — 2026-07-03 (fetched UTC 2026-07-03T03:03:14Z)

Theme: From prediction to the bench — AI moving from reading/predicting to DOING real experiments (design→wet-lab validation, agents acting on instruments), with an honest reality check.

## Item 1 — Biohub's world model of protein biology (design → lab-validated binders)
- Biohub news — https://biohub.org/news/world-model-of-protein-biology/ — FETCHED. Components: ESMC (protein LM, ~2.8B sequences), ESMFold2 (structure/design engine), ESM Atlas (6.8B sequences, 1.1B predicted structures). Designed lab-validated binders vs 5 cancer/immunology targets (EGFR, PDGFRβ, PD-L1, CTLA-4, CD45) in DAYS vs typical 3–4 years; hit rates 36–88% (minibinders), 15–29% (antibody formats); PD-L1 binders restored T-cell signaling; ESMFold2 beat AlphaFold3 on antibody–antigen pose. Alex Rives (Head of Science) quote; Priscilla Chan quote. Open/free.
- GEN coverage — https://www.genengnews.com/topics/artificial-intelligence/biohub-releases-protein-biology-world-model-to-address-disease/

## Item 2 — "Thinking microscopes": agentic AI turns instruments into co-scientists
- npj Computational Materials 2026 — https://www.nature.com/articles/s41524-026-02077-y — Jamali, Aghazadeh, Kacher, "Thinking microscopes: agentic AI and the future of electron microscopy" (12, 149; DOI 10.1038/s41524-026-02077-y). Networks of specialized LLM agents (plan, analyze, simulate, critique) integrated with the microscope → from passive characterization tool to "co-scientist"; Georgia Tech connecting cloud agentic AI to microscopes at the Institute for Matter and Systems.
- Phys.org — https://phys.org/news/2026-05-agentic-ai-electron-microscopes.html
- Lab tie-in: Agent-Lens /project/agent-lens/ ; Self-driving Microscope /project/self-driving-microscope/ ; REEF /project/reef-imaging-farm/

## Item 3 — Reality check: "co-pilot to lab-pilot", and the validation gap ("scAInce")
- Hartung review (PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12426084/ — FETCHED. "co-pilot to lab-pilot"; "If automated literature synthesis accelerates the reading of science, autonomous laboratories promise to accelerate the doing." Caveats: DeepMind GNoME predicted ~380,000 crystals but independent labs validated <5% ("gap between computational novelty and practical synthesis"); risk of "agenda drift toward machine-tractable problems"; "hype can outpace verification when metrics are ill-defined." Central question: "not whether science will accelerate but whose science."
- Lab tie-in: REEF first live agent-run experiment /post/reef-first-live-demo/ (physical-world validation) ; ProtiCelli /publication/sun-2026-proteome-wide/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled. Web/primary sources only.
- Avoided repeating: rBio/soft-verification, self-driving-labs-industrial, virtual-cell gaps (Jul 2); agent harness/benchmarks, virtual-cell world models (Jul 1); RNA structure, pathology FMs, ProtiCelli deep-dive (Jun 30).
