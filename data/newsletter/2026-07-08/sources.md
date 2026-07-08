# Newsletter sources — 2026-07-08 (fetched UTC 2026-07-08T03:04:07Z)

Theme: The building blocks of a virtual cell — AI is learning to read/write the genome, infer the proteome from ordinary images, and model 3D tissue.

## Item 1 — Genome foundation models come of age (read + write DNA; decode the dark genome)
- Evo 2 (Arc Institute + NVIDIA), Nature 2026 — https://www.nature.com/articles/s41586-026-10176-5 ; phys.org — https://phys.org/news/2026-03-evo-ai-genetic-code-domains.html — FETCHED. 9.3T nucleotides, 128,000+ genomes, 100,000+ species; 1M-nt context; trained on 2,000+ H100s. >90% accuracy on BRCA1 benign/pathogenic; designs synthetic genomes "as long as simple bacteria" + functional synthetic bacteriophages. Fully open (data + code + weights); in NVIDIA BioNeMo. Patrick Hsu quote.
- AlphaGenome (Google DeepMind), Nature Jan 2026 — https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/ — FETCHED. Input up to 1,000,000 bp at single-bp resolution; predicts thousands of regulatory readouts (splicing, accessibility, RNA levels, TF binding, 3D contacts) + variant effects (~1s). Beat top models on 22/24 sequence + 24/26 variant tasks; trained in 4h, half Enformer's compute. Targets the non-coding 98% (complements AlphaMissense). API (research-only). T-ALL/TAL1 example. Lareau: "a milestone for the field."

## Item 2 — HEX: virtual spatial proteomics from an ordinary H&E slide
- "AI-enabled virtual spatial proteomics from histopathology" (Stanford), PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC12823406/ — FETCHED. Model = HEX ("H&E to protein expression"). Predicts 40 protein biomarkers (immune/structural/functional) from standard H&E → virtual CODEX maps. Trained/validated on 819,000 image tiles / 382 tumor samples. Motivation: spatial proteomics is costly/complex/hard to scale; H&E is the clinical gold standard → low-cost scalable spatial biology. NSCLC (2,298 patients, 6 cohorts): +22% prognostic accuracy, +24–39% immunotherapy response prediction vs conventional biomarkers.
- Lab tie-in: ProtiCelli (image-based proteome simulation) /publication/sun-2026-proteome-wide/ ; Human Cell Simulator /project/human-cell-simulator/

## Item 3 — AI + organoids: modeling 3D tissue
- Review, Trends in Biotechnology 2026 — https://www.cell.com/trends/biotechnology/fulltext/S0167-7799(26)00009-0 — direct fetch 403 (paywall); grounded via search excerpt. ML + math modeling for organoid research; image-based readouts foundational (snapshot microscopy for morphology; live-cell imaging → rich time series); highlights deep visual proteomics revealing in vivo-like phenotype of orthotopically transplanted human colon organoids (Cell Systems 2025).
- Lab tie-in: live-cell imaging / REEF /project/reef-imaging-farm/ ; Self-driving Microscope /project/self-driving-microscope/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits). x-breaking remains disabled.
- Evo 2 / AlphaGenome are early-2026 (Nature); framed as the state of genome-FMs (building blocks), not breaking news.
- Avoided repeating recent digests (Jul 1–7): agents/harness, virtual-cell world models & baselines, rBio, self-driving-labs-industrial, Biohub protein world model, thinking microscopes, image-based profiling FMs.
