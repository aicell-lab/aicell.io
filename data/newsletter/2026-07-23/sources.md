# Newsletter sources — 2026-07-23 (fetched UTC 2026-07-23T03:03:32Z)

Theme: AI designs biology's parts — proteins to see with, genomes to program with — and the tools to physically build them are finally catching up.

## Item 1 — NovoTags: AI-designed proteins to see inside living cells
- phys.org — https://phys.org/news/2026-07-ai-proteins-scientists-cells.html — FETCHED. NovoTags: de novo fluorescent protein tags designed from scratch that bind Janelia Fluor (JF) dyes to image specific proteins in human cells. Science 2026 (Tran et al., "De novo design of orthogonal far-red, orange, and green fluorophore-binding proteins for multiplexed imaging," DOI 10.1126/science.aeb0822). Collaboration: Baker Lab (Institute for Protein Design), Lavis Lab (Janelia, JF dyes), Mahamid Group (EMBL, microscopy). Pipeline: RFdiffusion (backbones) -> LigandMPNN (sequences) -> AlphaFold/RoseTTAFold (filter) -> yeast display/FACS/NGS screening. Enables multicolor (far-red/orange/green, complementing HaloTag/SNAP-tag), live STED, fluorescence-lifetime imaging (FLIM); color + lifetime could track up to ~30 proteins at once. NovoSplit = inducible split version ("molecular switch" assembling only when target dye present; dye as "molecular glue") -> basis for inducible cryo-CLEM tags for in-cell structural biology. Sequences + dyes freely available. Key: "designed proteins can modulate a fluorophore's photophysical properties."
- Lab tie-in: bioimaging / super-resolution / in-cell structural imaging — Self-driving Microscope /project/self-driving-microscope/ ; ProtiCelli (imaging proteins) /publication/sun-2026-proteome-wide/

## Item 2 — AI can now write genomes
- Nature feature "AI can write genomes — how long until it creates synthetic life?" — https://www.nature.com/articles/d41586-026-00681-y — generative models (Evo 2) design DNA on demand; question of synthetic life.
- DNA-Diffusion — Nature Genetics 2025 — https://www.nature.com/articles/s41588-025-02441-6 — generative framework designs compact, cell-type-specific regulatory elements; demonstrated endogenous reactivation of AXIN2 (leukemia-protective gene) in its native context.
- 2025 Cell proof-of-concept — https://www.sciencedaily.com/releases/2025/05/250508112324.htm — first generative-AI-designed synthetic DNA controlling gene expression in healthy mammalian (mouse) cells.
- Review: "Generative AI for synthetic biology: designing parts, circuits, and genomes" — Cell Systems 2026 — https://www.cell.com/cell-systems/abstract/S2405-4712(26)00015-3

## Item 3 — Sidewinder: finally building what AI designs
- IEEE Spectrum (Elie Dolgin, 26 May 2026) — https://spectrum.ieee.org/faster-dna-synthesis-sidewinder — FETCHED. Sidewinder (Caltech, Kaihang Wang lab): assembles many genetic sequences at once in one tube. Precision: 1 wrong junction per 10 million assembly events (vs ~1 per 10-30 for conventional). Uses cheap mass-produced oligos + molecular "barcodes" ("page numbers") so fragments link only with intended neighbors; PyWinder algorithm generates barcodes in minutes on a laptop. Demo: used Evo 2 to redesign a 12,500-letter E. coli sequence in silico, then built it error-free. Brian Hie (Evo 2): a project that took a month "in a few days"; Gorochowski: "a step change... maybe even small genomes." Company Genyro (Wang, Robinson, Hie, Woolfson).
- Lab tie-in: the design-build-test loop for biology — REEF /project/reef-imaging-farm/ ; generative modeling infra — BioEngine /project/bioengine/

## Provenance notes
- X sweep (lab-x.py monitor/search/discover): NOT run — getxapi HTTP 402 (out of credits; re-checked today, still 402). x-breaking remains disabled.
- Item 2 grounded via search + primary links (Nature feature, Nature Genetics, Cell/ScienceDaily). NovoTags + Sidewinder richly fetched. No fabrication.
- Avoided repeating recent digests (Jul 16-22): protein dynamics/RareAgent, microscopy VLMs, enzyme design, segmentation FMs, VCC/data, microbiome, aging.
