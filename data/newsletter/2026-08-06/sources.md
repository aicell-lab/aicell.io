# Newsletter sources — 2026-08-06 (fetched UTC 2026-08-06T03:08:48Z)

Theme: **The stain you never applied — virtual staining & in-silico labeling.**
Physical staining is the tax microscopy pays for molecular specificity: dyes and
antibodies are slow, costly, one-shot, and — for live cells — phototoxic and
perturbing. A decade of deep learning now offers a different bargain: **predict the
fluorescent label or histology stain directly from a cheap, gentle, label-free image**
(brightfield / transmitted light / autofluorescence / quantitative phase), applying no
dye at all. 2025–26 is the season this stopped being a demo and became a *usable
measurement layer*: a context-aware model (**CELTIC**) that predicts organelle
fluorescence robustly enough to run on out-of-distribution live cells, virtual
histological staining scaling to whole slides and multiplexed panels — and, crucially,
the field's own **hallucination police** (**AQuA**), an autonomous check that flags when
a generated stain has invented biology that isn't there. A lab-core story: dye-free,
non-perturbative readouts are exactly what a self-driving microscope needs — and the
honest-frontier discipline (never trust a generated image you can't audit) is the lab's
throughline.

## Provenance / method
- Web research (WebSearch + WebFetch). Two load-bearing anchors **primary-fetched**:
  **CELTIC** via PMC (PMC12904784) and **AQuA** via arXiv (2404.18458), both with
  verbatim quotes and exact numbers below.
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  again returns **HTTP 402 Insufficient credits** (getxapi out of credits **~5 weeks**);
  `search`/`discover` gated; x-breaking stays disabled. Flagged to Wei for a top-up.
- **De-dup / variety (important):** virtual staining / in-silico labeling — *generating*
  a molecular channel you never physically acquired — has **not** been a theme in this
  run. It is a distinct *task* from the recent imaging digests:
  - Jul 19 "Segmentation Grows Up" = *find where* cells are (instance segmentation).
  - Jul 21 microscopy VLMs = *language/reports* about images.
  - Jul 29 "Seeing the Cell's Machines" = cryo-ET *imaging* of real structures.
  - Aug 1 "Proof Under the Microscope" = clinical pathology *diagnosis* from real stained
    tissue (classification), **not stain generation**.
  - Aug 4 "The Cell's Fingerprint" = *read* a phenotypic profile from an existing image.
  Virtual staining is the *generative cross-modality* layer: produce the stain/label
  itself. Closest neighbour is Aug 1 (digital pathology) — I deliberately **lead with the
  live-cell in-silico-labeling angle** (lab-core microscopy, dye-free live imaging) and
  treat clinical histology as the cousin, to keep clear separation from Aug 1's diagnosis
  framing. NB: Jul 13 "Wiring Diagrams" touched the structural interactome; today does not.
- **Verification discipline:** CELTIC and AQuA are **peer-reviewed** (*Nature Methods*;
  *Nature Biomedical Engineering*) and primary-fetched. The 2018 origin papers (Cell;
  Nature Methods) are long-established, exact citations verified. Histology-scale items
  (diffusion virtual staining; whole-slide multi-staining; Trends in Biotechnology review)
  are peer-reviewed, cited for framing/direction, no fabricated numbers.

## Item 1 — Capability: predict the label, apply no dye (ANCHOR — CELTIC, peer-reviewed, primary-fetched)
- **Origin (named):** Eric M. Christiansen, Samuel J. Yang, D. Michael Ando, … (Google),
  "In Silico Labeling: Predicting Fluorescent Labels in Unlabeled Images," **Cell 173,
  792–803.e19 (2018)** — predicts fluorescent labels (nuclei, cell type, viability) from
  transmitted-light z-stacks. Contemporaneous: Ounkomol, Seshamani, Maleckar, Collman,
  Johnson, "Label-free prediction of three-dimensional fluorescence images from
  transmitted-light microscopy," **Nature Methods 15, 917–920 (2018)** (Allen Institute).
  (Rivenson et al. 2019 coined "virtual staining" for the histology variant.)
- **Current flagship (fetched, PMC12904784):** Nitsan Elmalam & Assaf Zaritsky (Ben-Gurion
  University), **"Cell context-dependent in silico organelle localization in label-free
  microscopy images," Nature Methods (2025; issue-dated 2026)**, DOI 10.1038/s41592-025-02960-4.
  **CELTIC** = "CEll in silico labeling using Tabular Input Context."
- Verified facts / verbatim:
  - **Definition:** in silico labeling of organelles is "the computational cross-modality
    translation of label-free transmitted light microscopy images to their corresponding
    organelle-specific fluorescent images."
  - **The wall it clears (OOD):** changes in intracellular organization "can lead to
    altered label-free images and impaired in silico labeling"; CELTIC embeds a biological
    **context** (a 16-dim vector over five context types — mitotic stage, location, classic
    shape, ML shape, neighbourhood density) so prediction holds on under-represented/rare
    states.
  - **Result of context:** it "enhanced in silico labeling prediction and enabled the
    downstream analysis of out-of-distribution data such as cells undergoing mitosis and
    cells located at the edge of the colony," pointing to "a link between cell context and
    intracellular organization."
  - **Numbers:** a unified multi-organelle model reached **mean PCC 0.700** vs **0.683** for
    single-organelle models; a **mitosis classifier trained without any real mitotic cells**
    reached **AUC 0.928**; spindle-axis prediction hit a median location error of **3.8 px**
    and orientation error of **13°**.
  - **The promise (headline):** in silico labeling "holds the promise of enabling
    **computationally multiplexed live cell imaging** toward an integrated understanding of
    the cell."

## Item 2 — The clinical cousin: virtual histological staining at scale (framing, peer-reviewed)
- **Idea:** generate H&E / IHC-equivalent images from **label-free** inputs (autofluorescence,
  quantitative phase, remote-sensing microscopy) — no reagents, no wait, tissue preserved for
  re-use. Review anchor: Leena Latonen et al., **"Virtual staining for histology by deep
  learning," Trends in Biotechnology (2024)**, S0167-7799(24)00038-6 — surveys the field and
  is explicit that outputs from "unmatured models based on biased datasets" carry "AI-derived
  artifacts such as hallucinations," so "the suitability of the model outputs should be
  carefully verified in each context."
- **2025–26 direction (named, not load-bearing):**
  - **Diffusion models** for higher-fidelity staining: "Pixel super-resolved virtual staining
    of label-free tissue using diffusion models" (arXiv:2410.20073; PMC12125245) — a Brownian-
    bridge diffusion process to reduce variance/hallucination and lift resolution vs GANs.
  - **Whole-slide, multiplexed:** "Label-free whole slide virtual multi-staining using dual-
    excitation photon absorption remote sensing microscopy," **npj Imaging (2026)**,
    s44303-026-00154-x — one label-free acquisition → multiple histochemical stains (RegGAN).
  - **Score-aware IHC:** 2026 H&E→HER2 virtual IHC with score-specific supervision (clinical
    burden reduction). Direction only; specific figures not quoted.

## Item 3 — The honest frontier: catch the stain that lies (ANCHOR — AQuA, peer-reviewed, primary-fetched)
- Source (fetched, arXiv:2404.18458; published): Luzhe Huang, Yuzhu Li, Nir Pillar, Tal Keidar
  Haran, William Dean Wallace, **Aydogan Ozcan** (UCLA / USC Keck), "A robust and scalable
  framework for hallucination detection in virtual tissue staining and digital pathology,"
  **Nature Biomedical Engineering 9(12), 2196–2214 (2025)**, DOI 10.1038/s41551-025-01421-9
  (PMC12705451). Companion: *Nature Methods* (2025) commentary "Combating hallucination in
  digital pathology," s41592-025-02789-x.
- Verified facts / verbatim:
  - **AQuA** = "Autonomous Quality and hallucination Assessment." It flags problematic virtual
    stains — including "realistic-looking images that could mislead diagnosticians" — the most
    dangerous failure mode (a confident, plausible, *wrong* image).
  - **Accuracy:** "99.8% accuracy when detecting acceptable and unacceptable virtually stained
    tissue images," and **98.5% agreement** with board-certified pathologists' manual
    assessments.
  - **No ground truth, model-agnostic:** works "without access to histochemically stained
    ground truth" and independently of the original virtual-staining model (iterates between
    two networks across the virtual-staining and virtual-autofluorescence domains); blindly
    validated on human kidney and lung samples from new patients.
  - Senior-author framing (Ozcan): AQuA "add[s] a layer of trust to AI-generated images in
    medicine" — "a digital second opinion … checking every virtually stained tissue slide to
    ensure it is safe for diagnosis."

## Lab connections (for "why it matters")
- **Dye-free, gentle readouts for the self-driving microscope.** Physical fluorescence is slow,
  bleaches, and is phototoxic — you cannot stain-fix-image inside a closed live-cell loop.
  In-silico labeling gives molecular channels from a benign brightfield frame, so the
  [self-driving microscope](/project/self-driving-microscope/), [Agent-Lens](/project/agent-lens/),
  and [REEF imaging farm](/project/reef-imaging-farm/) can watch live cells respond, longer and
  faster, without perturbing what they measure.
- **The measurement layer, generated.** Aug 4 *read* phenotype from a picture; this *generates*
  the molecular channels themselves — "computationally multiplexed" imaging beyond the handful
  of fluorophores you can physically fit. Ground truth for a
  [virtual cell](/project/human-cell-simulator/) increasingly comes from images we compute, not
  only images we capture.
- **The throughline: never trust a readout you can't audit.** AQuA is the exact discipline the
  lab keeps returning to — [prove it](/post/newsletter-2026-07-28/); a model that
  [shows its work](/post/newsletter-2026-08-02/); privacy as a
  [budget you spend](/post/newsletter-2026-08-05/). A generated image that looks perfect but
  invented a structure is worse than no image. An autonomous lab that *acts* on generated
  readouts must be able to catch the lie — trustworthy-by-construction, with the check shipped
  alongside the generator, the [BioImage Model Zoo](/project/bioimage-model-zoo/) / AI4Life ethos.

## De-dup check
- Recent digests: Aug 5 federated/privacy; Aug 4 image-based profiling; Aug 3 small-molecule
  design; Aug 2 virtual cell (interpretable); Aug 1 pathology diagnosis; Jul 31 self-driving
  labs; Jul 30 RNA design; Jul 29 cryo-ET; Jul 28 genomic-FM eval; Jul 26 spatial; Jul 21
  microscopy VLMs; Jul 19 segmentation; Jul 13 wiring diagrams (interactome). **Virtual staining
  / in-silico labeling — computing a stain/label you never physically applied — has not been a
  theme.** Distinct from Aug 1 (diagnosis from *real* stains) and Aug 4 (reading a profile from
  an existing image): this is the *generative cross-modality* layer, led here through the
  live-cell in-silico-labeling angle. Clear to run.
