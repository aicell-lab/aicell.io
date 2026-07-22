# Newsletter sources — 2026-07-22 (fetched UTC 2026-07-22T03:03:49Z)

Theme: In motion, on trial — AI moves from static structure to protein dynamics, and from confident predictions to ones the wet lab validates (or refutes).

## Item 1 — AI models proteins in motion (beyond static AlphaFold)
- "Learning Structure, Energy, and Dynamics: A Survey of AI for Protein Dynamics" — arXiv:2604.25244v1 (2026) — https://arxiv.org/html/2604.25244v1 — FETCHED. After AlphaFold/ESMFold nailed single structures, the frontier is CONFORMATIONAL ENSEMBLES: function depends "not on a single static structure but on an ensemble of interconverting conformations." Approaches: AlphaFlow (fine-tunes AlphaFold/ESMFold with flow-matching for ensembles); BioEmu (diffusion model integrating experimental stability measurements); Str2Str/ConfDiff/ESMDiff/IDPFold/SimpleFold; Boltzmann Generators (BG/TBG/SBG/PROSE — learn proposal density + likelihood for importance-reweighting); trajectory methods MDGen/ConfRover (kinetics). Goal: approximate the Boltzmann distribution p(x)∝exp(-E/kBT) as a cheaper surrogate for MD (femtosecond steps = prohibitively expensive).
- Context: "Beyond static structures" review — Briefings in Bioinformatics 2025 — https://academic.oup.com/bib/article/26/4/bbaf340/8202937 ; "From possibility to precision in macromolecular ensemble prediction" — Nature Methods 2026 — https://www.nature.com/articles/s41592-026-03084-z
- Lab tie-in: generative modeling — ProtiCelli /publication/sun-2026-proteome-wide/ ; dynamics is the molecular analog of the temporal virtual cell (Human Cell Simulator /project/human-cell-simulator/)

## Item 2 — The catch: dynamics is data-starved (and hard to trust)
- Same survey (FETCHED). Open problems: "scarcity of dynamic structural data" + PDB conformational bias; purely data-driven models "often struggle to produce physically realistic ensembles"; reliability of reweighting diagnosed via effective sample size (low ESS = poor overlap); broader challenges = scalability, thermodynamic consistency, kinetic fidelity, integration with experimental constraints. Early MSA-perturbation heuristics give limited, non-Boltzmann diversity and only at inference time.

## Item 3 — Predictions on trial: rare-disease repurposing agents (validated AND refuted)
- RareAgent — arXiv:2510.05764 ("Self-Evolving Reasoning for Drug Repurposing in Rare Diseases") — https://arxiv.org/abs/2510.05764 — (PDF didn't parse; grounded via search) multi-agent, self-evolving reasoning (builds on Reflexion/Self-Refine/Tree-of-Thoughts) for rare-disease repurposing, moving beyond static knowledge-graph + GNN inference (DRKG/PrimeKG).
- Context (via search): <10% of thousands of rare diseases have approved therapies. Validated example: HealX's Sulindac (AI-identified) — FDA IND + Orphan Drug, Phase 2a for fragile X. NEGATIVE validation matters too: a 2026 study used virtual screening + zebrafish phenotyping to argue AGAINST repurposing 4-phenylbutyrate for STXBP1-related disorders. "No single algorithm — network proximity, diffusion, or ML — reliably outperforms" -> ensemble/fusion consensus. FDA maturing an AI/real-world-data repurposing framework, but confirmatory trials still required.
- Lab tie-in: autonomous research agents /project/autonomous-research-agents/ ; the propose->validate loop = REEF /project/reef-imaging-farm/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- RareAgent PDF was binary/unparseable; grounded via search excerpts + arXiv metadata (no fabricated results). Protein-dynamics survey richly fetched.
- Avoided repeating recent digests (Jul 15-21): microscopy VLMs, enzyme design, segmentation FMs, VCC/data, microbiome, aging, Biomni.
