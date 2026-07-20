# Newsletter sources — 2026-07-20 (fetched UTC 2026-07-20T03:03:28Z)

Theme: Design, build, test — and safeguard? Generative AI can finally design proficient enzymes, autonomous biofoundries close the design-build-test loop, yet a census of biology-AI models finds safeguards are the rare exception.

## Item 1 — Generative AI can finally design enzymes
- "Generative AI for Enzyme Design and Biocatalysis" (Middendorf & Ferruz), arXiv:2602.03779 (3 Feb 2026) — https://arxiv.org/abs/2602.03779 — FETCHED (abstract). "After more than one decade of low success rates for computationally designed enzymes, generative AI models are now frequently used for designing proficient enzymes"; mature enough "to create and optimize enzymes for industrial applications"; emphasis on experimentally-validated models; broader generative-AI + experimental testing + "community assessment to inform the next generation of models."
- Function-driven de novo design + "synzymes" (non-natural reactions): MDPI Molecules Dec 2025 — https://www.mdpi.com/1420-3049/31/1/45 ; SCIEPublish "Generative AI for Function-Driven De Novo Enzyme Design" — https://www.sciepublish.com/article/pii/701 . Models cited: AlphaFold2, RoseTTAFold, ProGen, ESM-2 (predict structure/stability/function); ProteinGAN/VAEs (de novo sequences); RL for mutation selection.
- Lab tie-in: generative modeling — ProtiCelli /publication/sun-2026-proteome-wide/

## Item 2 — Autonomous biofoundries close the loop
- "AI-powered biofoundries for protein engineering and metabolic engineering" — ScienceDirect 2026 — https://www.sciencedirect.com/science/article/pii/S0958166925001247 — (via search) couples generative design with automation to accelerate the design-build-test-learn cycle; concrete example: a low-cost liquid-handling robot automated expression, purification, and screening of PET-degrading (PETase) enzymes in 96-well plates; trajectory toward autonomous protein-engineering platforms with minimal human intervention.
- Lab tie-in: REEF (design->run->measure loop; automation) /project/reef-imaging-farm/ ; Self-driving Microscope /project/self-driving-microscope/

## Item 3 — But safeguards are the rare exception (biology-AI census)
- Epoch AI "Expanding our analysis of biological AI models" (commissioned by Sentinel Bio) — https://epoch.ai/publications/expanding-our-analysis-of-biological-ai-models — FETCHED. 1,196 biological AI models cataloged across 9 categories (protein engineering + small-biomolecule design ~half; genetic modification 13%; general-purpose incl. ESM3/Evo 2 ~13%). Bottleneck: "compute does not appear to be the primary bottleneck"; progress "more constrained by data availability and quality than by raw compute." SAFEGUARDS RARE: only 3.2% of all models have any documented safeguards (35% among "notable," driven by frontier LLMs at 95% vs 1.4% of other models); 2.5% have documented risk assessments. Accessibility mostly open (58% open inference code, 46% share training data, 23% open weights). Base models: ESM-2 most common (58 models); Protein Data Bank most-used dataset (159 models).
- Lab tie-in: safety-first, human-in-the-loop agents (REEF refusals) /project/reef-imaging-farm/ ; FAIR/agent-readable infra — BioImage Model Zoo /project/bioimage-model-zoo/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- Corrected: "synzymes/function-driven/autonomous experimentation" are NOT in the Middendorf&Ferruz abstract — attributed to the MDPI/SCIEPublish reviews instead. Epoch's finding is "data quality > compute," NOT a "UniRef50 slowdown" (that phrasing was from a different/older analysis) — used the accurate framing. No fabrication.
- Avoided repeating recent digests (Jul 13-19): segmentation FMs, VCC/data-decides, LAP/agent-instrument, microbiome FMs, MaxToki/aging, Biomni.
