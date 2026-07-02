# Newsletter sources — 2026-07-02 (fetched UTC 2026-07-02T03:00Z)

Theme: Grounding the virtual cell — how AI's biology is made trustworthy (verification, closed-loop experiments, honest gaps).

## Item 1 — rBio: reasoning about cells with a virtual cell as verifier (CZI)
- CZI blog — https://chanzuckerberg.com/blog/rbio-reasoning-ai-model/ — FETCHED. Soft verification (rewards proportional to likelihood answer is correct); distills TranscriptFormer (112M cells, 12 species); on PerturbQA beats SUMMER (ICLR 2025) and QWEN2.5 baseline; conversational query model; led by Theofanis Karaletsos & Ana-Maria Istrate.
- VentureBeat — https://venturebeat.com/ai/chan-zuckerberg-initiatives-rbio-uses-virtual-cells-to-train-ai-bypassing-lab-work — "first AI trained to reason about cell biology using virtual simulations rather than lab experiments."
- Code — https://github.com/czi-ai/rbio — based on Qwen2.5-3B-Instruct; hard/soft verifier variants; MIT license on CZI mods.
- Preprint — Istrate et al., "rbio-1: training scientific reasoning LLMs with biological world models as soft verifiers" (2025) bioRxiv https://doi.org/10.1101/2025.08.18.670981

## Item 2 — Self-driving labs cross into industrial infrastructure (2026)
- ChemCopilot 2026 — https://www.chemcopilot.com/blog/self-driving-labs-the-rise-of-autonomous-chemical-discovery-in-2026 — FETCHED. Closed-loop 3-layer stack (cognitive brain = Bayesian optimization + generative AI; physical hands; analytical eyes); "compressing decades of R&D into days"; 500-iteration DoE in a weekend; augment-not-replace "AI co-scientist" framing; on-prem workcells vs cloud-lab SaaS.
- C&EN (June 2026) — https://cen.acs.org/physical-chemistry/computational-chemistry/Self-driving-labs-changing-chemists/104/web/2026/06 — further reading (fetch blocked 406); reports the "who gets credit for AI-discovered reactions" attribution debate.
- Lab tie-in: REEF first live agent-run experiment — /post/reef-first-live-demo/ ; REEF project /project/reef-imaging-farm/

## Item 3 — The honest gaps in the virtual cell (reality check)
- pdpspectra 2026 analysis — https://pdpspectra.com/blog/virtual-cell-models-ai-2026/ — FETCHED. Three structural gaps: generalization to unseen perturbations, context dependence, batch effects/technical confounds ("worse than no model, because it is confident and plausible"). Benchmark problem (aggregate correlation gameable). "Judge any model by its performance on the hard split, not the demo"; "the gaps are more interesting than the press releases." Scale: Tahoe-100M (100M cells, ~60k drug-cell interactions, 50 lines, 1,200 drugs, ~50x prior public data); Arc Virtual Cell Atlas (300M+); CELLxGENE ~170M; Virtual Cell Challenge (5,000+ registrants, 114 countries, 1,200+ teams).
- OmicsML community model catalog — https://github.com/OmicsML/awesome-foundation-model-single-cell-papers
- Lab tie-in: ProtiCelli — /publication/sun-2026-proteome-wide/ ; Human Cell Simulator /project/human-cell-simulator/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run this cycle — getxapi HTTP 402 (out of credits). x-breaking workflow remains disabled. Web/primary sources only today.
- Avoided repeating: agent harness/benchmarks & virtual-cell world models (Jul 1), RNA structure & pathology FMs & ProtiCelli deep-dive (Jun 30).
