# Newsletter sources — August 23, 2026

**Theme:** AI-reconstructed connectomics from electron microscopy ("Wiring the Brain") — the extreme case
of AI reading images at petascale, on open platforms, with humans in the loop. Fresh domain (not covered
before); horizon / strategy-radar. Ties to the lab's large-model-serving + open-tools + prove-it identity.

**X/Twitter sweep:** SKIPPED (getxapi out of credits — HTTP 402; 14th consecutive skip, two full weeks).
Grok-based replacement wired, awaiting xAI credits.

All anchors verified by two parallel general-purpose subagents against Crossref / Europe PMC / PubMed, with
abstracts obtained. Only abstract-verified numbers/quotes used in the post; body-only flagged and NOT quoted.

---

## Section 1 — The reconstruction problem (why AI was the unlock)

### Flood-filling networks (FFN) — VERIFIED
- Januszewski, M. … Jain, V. "High-precision automated reconstruction of neurons with flood-filling networks."
  *Nature Methods* **15**(8):605–610, 2018. DOI: 10.1038/s41592-018-0049-4 · PMID: 30013046 · Research article.
- First author Michał Januszewski; **senior/last author Viren Jain** (Google); Winfried Denk second-to-last.
- ABSTRACT-VERIFIED (verbatim): a convolutional neural network with a **recurrent pathway** for iterative
  extension of neurites; evaluated on serial block-face EM of a **zebra finch** brain; achieved a
  **mean error-free neurite path length of 1.1 mm**, with **only four mergers in a test set of 97 mm** of path
  length — **"an order of magnitude better"** than previous approaches, at "substantially increased computational
  costs."
- NOTE: abstract gives NO accuracy percentage; the metric is "mean error-free neurite path length," NOT
  "expected run length." Do not quote a % accuracy as abstract-sourced.

## Section 2 — The first whole brain (and the human scale arriving)

### FlyWire adult Drosophila connectome (flagship) — VERIFIED
- Dorkenwald, S. … Seung, H.S. & Murthy, M. (co-senior). "Neuronal wiring diagram of an adult brain."
  *Nature* **634**(8032):124–138, 2024. DOI: 10.1038/s41586-024-07558-y · PMID: 39358518 · Research article.
- ABSTRACT-VERIFIED (verbatim): **"139,255 neurons"** and **"5 × 10⁷ chemical synapses"** (~50 million),
  reconstructed from an adult female *Drosophila melanogaster*; resource incorporates annotations of cell classes
  and types.
- CORRECTIONS: use **139,255** (NOT "~130,000"); **~50 million** synapses (the figure "54.5 million" is NOT
  abstract-verified — do not cite). AI segmentation + community proofreading are NOT described in this abstract —
  attribute that framing to the FlyWire *Nature Methods* paper below, not here.

### FlyWire annotation companion — VERIFIED
- Schlegel, P. … Jefferis, G.S.X.E. "Whole-brain annotation and multi-connectome cell typing of Drosophila."
  *Nature* **634**(8032):139–152, 2024. DOI: 10.1038/s41586-024-07686-5 · PMID: 39358521 · Research article.
- ABSTRACT-VERIFIED: **"8,453 annotated cell types"** across the "approximately 140,000 neuron FlyWire whole-brain
  connectome"; of these, 3,643 previously proposed (hemibrain) and 4,581 new; ~one-third of hemibrain cell types
  could not be reliably reidentified.

### H01 human cortex fragment — VERIFIED
- Shapson-Coe, A. … Lichtman, J.W. (senior/last), Jain, V. (co-senior, second-to-last). "A petavoxel fragment of
  human cerebral cortex reconstructed at nanoscale resolution." *Science* **384**(6696):eadk4858, 2024.
  DOI: 10.1126/science.adk4858 · PMID: 38723085 · Research article.
- ABSTRACT-VERIFIED (verbatim): **~1 cubic millimeter** of human **temporal cortex**; **about 57,000 cells**;
  **about 150 million synapses**; **about 230 mm of blood vessels**; the reconstruction **comprises 1.4 petabytes**;
  glia outnumber neurons **2:1** (oligodendrocytes most common); rare powerful axonal inputs of **up to 50 synapses**.
- CORRECTION: it is **57,000 CELLS, not neurons** (neurons are a minority; glia 2:1). Axon total-length figures are
  BODY-ONLY. "Petavoxel" (title) = voxels, distinct from the 1.4-petabyte data size.

## Section 3 — The honest frontier + lab hook

### Proofreading burden — VERIFIED
- Dorkenwald, S. … Seung, H.S. "FlyWire: online community for whole-brain connectomics." *Nature Methods*
  **19**(1):119–128, 2022. DOI: 10.1038/s41592-021-01330-0 · PMID: 34949809 · Research article.
- ABSTRACT-VERIFIED (verbatim): "**Proofreading of whole-brain automated reconstructions will require many
  person-years of effort, due to the huge volumes of data involved.**" → human-in-the-loop at data scale.

### Connectome ≠ function — VERIFIED
- Bargmann, C.I. & Marder, E. "From the connectome to brain function." *Nature Methods* **10**(6):483–490, 2013.
  DOI: 10.1038/nmeth.2451 · PMID: 23866325 · Peer-reviewed Perspective.
- ABSTRACT-VERIFIED: asks "what information is needed beyond connectivity diagrams to understand the function of
  nervous systems"; highlights "the importance of **neuronal dynamics and neuromodulation**, and the existence of
  parallel circuits." → the wiring map is necessary, not sufficient.

## Lab connections
- BioImage Model Zoo (/project/bioimage-model-zoo/), BioEngine (/project/bioengine/), ImJoy (/project/imjoy/) —
  serving large models over massive image volumes; open, callable, community-validatable.
- Virtual cell (/post/newsletter-2026-08-15/) — a wiring diagram is a structural prior for a dynamic model, as a
  static structure is for its ensemble (/post/newsletter-2026-08-11/).
- Prove-it discipline (/post/newsletter-2026-07-27/); image restoration (/post/newsletter-2026-08-22/) —
  AI reading images as the through-line.
