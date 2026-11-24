# Newsletter 2026-11-24 — sources

Run time: 2026-11-24T05:05Z. Window since last digest: 2026-11-22 → 2026-11-24
(plus two catch-up items from earlier in November that previous digests did not cover).

## X (Twitter) sweep — FAILED (HTTP 402)

```
scripts/lab-x.py monitor --since-hours 24 --min-likes 30
scripts/lab-x.py discover
→ error: getxapi returned HTTP 402 'Insufficient credits'
```
The getxapi account is still out of credits (same as 2026-11-22). No X data this run,
no `search` topic sweeps, and **no new accounts added to `x-accounts.md`** — the
living watch-list could not be extended. Noted in the post. Research below is
web + Crossref + bioRxiv feeds only.

## Items used in the digest

1. **Finding faster quantum algorithms with agents and formal verification** —
   https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/
   — Google DeepMind + Google Quantum AI, blog dated 2026-11-23; paper
   https://arxiv.org/abs/2611.09822 (Shirobokov, Jaderberg, Babbush et al.); code
   https://github.com/google-deepmind/formal-quantum-computation
   — Why relevant: teams of Gemini 4 agents search for circuit optimisations, every
   accepted improvement proved in Lean. The template for AI discovery with a machine-
   checkable acceptance test — directly relevant to how we gate agent output in REEF /
   Agent-Lens. Fetched 2026-11-24.
   Numbers (from the blog): 11.8× lower computing cost on an inertial-confinement-fusion
   property (5,650 → 4,338 error-corrected qubits); 8× cheaper photochemistry simulation;
   2.5× on cytochrome P450 (481 → 333 qubits); 2.57× on a Grover implementation; 290× on
   an arcsin arithmetic routine. Agents met at a "virtual conference" every four hours.
   Caveat stated by DeepMind: these circuits still exceed what first-generation
   error-corrected machines are expected to offer.

2. **Zero-shot virtual knock-out rankings do not recover causal genes from observational
   single-cell data** — DOI https://doi.org/10.64898/2026.11.21.768293 ·
   https://www.biorxiv.org/content/10.64898/2026.11.21.768293v1
   — Cui, Li, Zhou, Zhang, Xu, Li, Zhang (Shanxi Medical University and collaborators),
   posted 2026-11-23. Abstract retrieved via Crossref API 2026-11-24.
   — Why relevant: a negative result on in-silico perturbation — the exact failure mode
   the Virtual Cell Challenge wrap-up flagged, measured directly. Relevant to Human Cell
   Simulator.
   Numbers (from the abstract): scTenifoldKnk (R and Python), CellOracle, Geneformer
   compared on 438 real, 3,585 synthetic and 330 DepMap knock-outs. Top-20 lists for
   *different* knock-outs overlapped by a median of 12–14 of 20 vs 0.08 expected by
   chance. Displacement tracked out-degree R² = 0.825 (0.852 with six more features).
   Planted-causal-gene recovery for scTenifoldKnk: AUROC 0.538 / 0.528. CellOracle
   displacement vs data-built network: rho = −0.212, P = 0.556. Geneformer shift vs token
   coverage: +0.41, +0.40, −0.27. Against DepMap essentiality, scTenifoldpy 0.5.1 AUROC
   0.459 (95% CI 0.357–0.566). Detection rate (no network needed) gained +0.129
   (95% CI 0.0017–0.2543).

3. **The IGVF Data Portal: a repository for insights into genome function** —
   https://doi.org/10.64898/2026.11.18.767169 · posted 2026-11-23 (Jou, Shen, Lin, Dong,
   Whaling, Jolanki et al.) — and **The IGVF Catalog Knowledge Graph** —
   https://doi.org/10.64898/2026.11.20.768224 · posted 2026-11-23 (Dong, Whaling, Jou,
   Shen, Lin, Jolanki et al.). Abstracts retrieved via Crossref API 2026-11-24.
   — Why relevant: a major consortium resource shipping *agent access* as a first-class
   interface (MCP server, OpenAPI). This is the BioEngine / Hypha "agent-readable
   infrastructure" thesis arriving in genomics.
   Numbers: portal https://data.igvf.org/ holds over 240 TB as of November 2026, reachable
   by browser, API "as well as via agentic tools". Catalog v1.3: nearly 3 billion nodes
   across 14 entity types, more than 8.6 billion edges across 31 relationship types,
   657 IGVF datasets, ArangoDB, 86 OpenAPI endpoints, Python and R clients, and a Model
   Context Protocol (MCP) server for LLM-assisted querying. Updated quarterly.

4. **SubCellSeg: A generalist model for subcellular structure segmentation in 3D
   fluorescence microscopy** — https://doi.org/10.64898/2026.11.10.765799 ·
   https://www.biorxiv.org/content/10.64898/2026.11.10.765799v1 — posted 2026-11-11.
   Mishra, Samudre, Khan, Borensztejn, Hookway, Thirstrup, Chen (ISAS Dortmund),
   Rafelski, Viana — Allen Institute for Cell Science. CC-BY 4.0. Fetched 2026-11-24.
   — Why relevant: direct companion to the μSAM2 item in the Nov 22 digest, and a
   BioImage Model Zoo-shaped result (one generalist beats the specialist zoo).
   Numbers: 13 subcellular structures; mean Dice 0.909 vs 0.773 for structure-specific
   specialists, beating each specialist on its own structure; zero-shot generalisation to
   new morphologies, microscopes, drug-perturbed cells and hiPSC-derived cardiomyocytes;
   fine-tuning from pretrained weights with 10% of labels (16 images) beat from-scratch
   training on the full set. Ships in the napari plugin `allencell-segmenter-ml`; code
   https://github.com/AllenCell/SubCellSeg

5. **AutoDNA — An AI-native experimental laboratory for autonomous biomolecular
   operations** — Nature, published 2026-11-04. Wu, Wang, Wang et al.
   https://doi.org/10.1038/s41586-026-11228-6 (title + authors + journal verified via
   Crossref API 2026-11-24; the Nature page itself is behind an SSO redirect).
   Project page https://ipads.sjtu.edu.cn/autodna/ · code https://github.com/IPADS-X/AutoDNA
   Secondary coverage used for detail (two independent sources, cross-checked):
   - Lab Manager, 2026-11-09:
     https://www.labmanager.com/ai-agents-coordinate-more-than-20-instrument-types-in-autonomous-biology-lab-36254
     (note: Lab Manager states the article was produced with generative-AI assistance and
     editorial review — treated as secondary, only for facts corroborated elsewhere)
   - Global Self-Driving Lab Landscape watch entry:
     https://sdl-map.discoverylabs.nl/watch/ (entry /entry/sjtu-autodna/)
   — Why relevant: closest published analogue to REEF / the self-driving microscope.
   Missed by our Nov 12 and Nov 22 digests, so carried here as catch-up.
   Facts corroborated by BOTH secondary sources: Shanghai Jiao Tong University; multi-agent
   architecture with a central planner over specialised agents (literature, reagents,
   protocols, code, hardware, hypotheses); more than 20 instrument types across nucleic-acid
   synthesis, transcription, amplification and sequencing; humans mainly restock reagents
   and labware; four demonstrations — enzymatic DNA synthesis matching expert-optimised
   yields, concurrent protocols 3.2× faster, a complete DNA data-storage write-and-recover
   cycle, and detection of a clinically relevant KRAS G13D mutation; code released on GitHub
   (sdl-map says Apache 2.0).
   NOT fully agreed between sources: the operation count — sdl-map says 11,382 hardware
   operations for the data-storage cycle, Lab Manager says "over 11,000 experimental steps"
   overall. The post uses the conservative "more than 11,000", attributed.

6. **Human Frontier Mission — global launch 2026-11-24** — press release via PR Newswire,
   2026-11-21, read at
   https://finance.yahoo.com/technology/ai/articles/next-frontier-ai-human-frontier-160000701.html
   (Morningstar copy https://www.morningstar.com/news/pr-newswire/20261121cn03510/... returned
   403). Site: https://hf-mission.com/ · programme dossier
   https://hf-mission.com/static/frontier/programme/index.html
   — Why relevant: a public, open-record attempt at exactly the "experts set the challenge,
   agents run the experiments" loop the lab is building toward.
   Facts from the release: organised by the "Human Frontier Mission Committee"; announced
   from Seattle on Nov 21 for a Nov 24 global launch; reported snapshot of 2,391 experiments
   across 54 challenges in 12 fields, 23 studies active; experts set challenges and define
   how progress is judged, agents generate and test candidates, the experiment record is
   published; example areas include global weather forecasting, traffic-signal coordination,
   wind power and storage scheduling, lung cell identification, and steel fatigue prediction;
   researchers can propose questions, share evidence or evaluation methods, and help assess
   results. Contact hi@hf-mission.com, X @HFMission.
   CAVEATS verified by us, and stated in the post: this is a **paid press release**, not an
   institutional announcement; the release names no individual committee members, no quotes
   and no funding; the landing page lists only affiliations members come *from* (Novix Lab,
   Google, Microsoft, HKU, CMU, Tsinghua, Johns Hopkins, Stanford, Imperial, Oxford, Cornell,
   Meta, Apple, PKU, Westlake) and explicitly does not claim institutional sponsorship; and
   the public challenge counter on the landing page was unpopulated (rendered as "–") when we
   fetched it on 2026-11-24. The 2,391/54/12 figures therefore come from the release only and
   we could not independently verify them.

## Checked and not used

- KTH/SciLifeLab/DDLS: no new announcement in the window (DDLS annual conference items are
  from Nov 3–10 and the agentic-AI postdoc ad was already covered on Nov 12).
- Microsoft "expanded AI for scientific research labs, Nov 22" — only found on AI-generated
  aggregator sites (emergent.sh); no primary Microsoft source located, so dropped.
- Nature Methods "Computational methods for cell–cell communication via single cells"
  (review, Nov 20) — solid but thin for a digest item.
- Arc Institute / Biohub / CZI: nothing new since the Virtual Cell Challenge wrap-up
  covered on Nov 22.
