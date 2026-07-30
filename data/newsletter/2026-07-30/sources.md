# Newsletter sources — 2026-07-30

Theme: **RNA foundation models — reading *and* writing the cell's messenger.**
Genome models (Jul 8) and structural/visual proteomics (Jul 29) bracket a layer we
had not put a digest on: **RNA**. 2025–2026 turned RNA into something a model can
both *read* (structure/function from sequence) and *write* (de novo design of
functional RNAs — aptamers, guide RNAs, therapeutic transcripts). A deliberate move
to the transcript layer of the virtual cell after a fortnight on genomics-eval,
imaging, design and strategy. Deliberately avoided a 4th "AI agents" story and a 3rd
protein-design story for topical variety.

## Provenance / method
- Web research (WebSearch + WebFetch). X/Twitter sweep **skipped**: `scripts/lab-x.py
  monitor --since-hours 24 --min-likes 30` still returns **HTTP 402 Insufficient
  credits** (getxapi out of credits ~4 weeks); topic `search` and `discover` likewise
  gated. x-breaking stays disabled. Flagged to Wei for a credit top-up.
- **De-dup:** last 10 digests (Jul 20–29) covered design/safety, microscopy-VLMs,
  protein dynamics, protein/enzyme/antibody design, open science, genome *writing*,
  spatial, strategy, genomic-FM *evaluation*, and cryo-ET *visual proteomics*. **No
  prior digest** took RNA foundation models / generative RNA design as its focus.
  Clear to run, and it fills a genuine gap in the virtual-cell arc (genome → **RNA** →
  protein → structure/image).
- **Verification discipline:** RNA-FM / RhoFold+ **primary-fetched** (GitHub, published
  in Nature Methods). RNAGenesis and EVA **corroborated across multiple secondary
  sources** (GitHub project pages, bioRxiv listings via search, independent write-ups)
  because bioRxiv / OpenReview full text blocked WebFetch (403 / browser-verification
  gate). Preprints are labeled as such. **Dropped unverified numbers:** an early search
  reported an RNAGenesis aptamer "K_D 4.02 nM" and a "2.5× editing" figure; a second
  corroboration search **could not confirm** either, so neither is asserted — only the
  corroborated wet-lab claim (HEK293T sgRNA editing ≥ wild-type) is stated.

## Item 1 — Reading RNA: RNA-FM / RhoFold+ (ANCHOR, primary-fetched, published)
- Sources (fetched): GitHub ml4bio/RNA-FM and the RhoFold+ repo/readme; published as
  **Nature Methods**. RNA-FM: "Interpretable RNA foundation model from unannotated data
  for highly accurate RNA structure and function predictions" (2022). RhoFold+: Shen et
  al., "Accurate RNA 3D structure prediction using a language-model-based deep learning
  approach," **Nature Methods** (2024). MIT-licensed.
- Verified facts:
  - **RNA-FM** is a BERT-style RNA language model (12 transformer layers) pretrained by
    masked-language-modeling on **~23.7M non-coding RNA sequences** (RNAcentral100),
    yielding 640-dimensional per-nucleotide embeddings that transfer to structure and
    function tasks **without evolutionary/MSA input**.
  - **RhoFold+** couples RNA-FM embeddings to a geometry-aware network to predict RNA
    **3D tertiary structure** end-to-end from a single sequence, reaching state-of-the-art
    accuracy on RNA-Puzzles and CASP-style RNA targets in seconds — a structure-prediction
    story for RNA analogous to what AlphaFold did for protein.
  - Both open-source (MIT). Establishes the *read* side: sequence → structure/function.

## Item 2 — Writing RNA: RNAGenesis (unified understanding + de novo design; corroborated)
- Sources (secondary, corroborating — bioRxiv full text 403): GitHub project (zaixizhang /
  RNAGenesis project page), bioRxiv listing via search, independent write-ups (CBIRT).
  Title (as cited): "RNAGenesis: Foundation Model for Enhanced RNA Sequence Generation and
  Structural Insights," bioRxiv (2024/2025). **~1B parameters.**
- Corroborated facts (consistent across sources):
  - Architecture: a **BERT-style bidirectional encoder** for RNA understanding + a
    **query-based latent-space compression** (Perceiver-style) feeding a **diffusion-guided
    decoder** for generation — one model spanning sequence understanding, de novo design,
    and structure-aware tasks.
  - Ranks **1st on 11 of 13 BEACON benchmark tasks**; on generation/design it outperforms
    prior RNA models including **RNA-FM** and the genomic model **Evo2** on the reported
    tasks.
  - Introduces **RNATx-Bench**, a therapeutics-oriented benchmark aggregating **>100,000
    experimentally validated RNAs** across modalities — ASOs, siRNAs, shRNAs, circRNAs,
    aptamers, and UTR variants.
  - **Wet-lab validation:** designed **CRISPR guide RNAs (sgRNAs)** validated in **HEK293T**
    cells targeting **EGFP and B2M**, achieving editing efficiency **equal to or better than
    wild-type** guides. (Aptamer designs were assessed by structural/computational metrics;
    **no measured K_D is asserted** — see verification note.)
  - Open model/code released by the authors.

## Item 3 — The freshest frontier: EVA, long-context full-length RNA design (Mar 2026 preprint)
- Sources (corroborating): bioRxiv "A Long-Context Generative Foundation Model Deciphers
  RNA Design Principles," **bioRxiv 2026.03.17.712398** (Mar 2026); GitHub **GENTEL-lab/EVA**
  (Apache-2.0). bioRxiv full text via search summary (page itself 403 to direct WebFetch).
  **Labeled preprint, not peer-reviewed.**
- Corroborated facts:
  - **EVA** ("Evolutionary Versatile Architect") is a **~1.4B-parameter decoder-only
    Transformer with a Mixture-of-Experts backbone** and an **8,192-token context window**
    (vs ~1,024 in prior RNA models) — enabling **full-length transcript** modeling without
    truncation.
  - Trained on **OpenRNA v1**: **114 million full-length RNA sequences (~231.3B nucleotides)**
    spanning structural, regulatory, coding and viral RNAs across the tree of life.
  - Jointly optimizes **autoregressive generation + masked infilling** (de novo synthesis and
    context-constrained redesign); **explicitly conditions on RNA type and taxonomic lineage**.
  - Reports state-of-the-art across **mutation-effect prediction, conditional generation, and
    functional RNA design**. All data, weights, and code released (Apache-2.0) — open science.
- Lighter context mentions (search-only, cited by name for landscape, not load-bearing):
  **AIDO.RNA** (GenBio, ~1.6B params, ~42M ncRNA, an "RNA-as-foundation" model in the AIDO
  suite) and **RiboDiffusion** (diffusion-based RNA inverse folding — sequence design for a
  target backbone). Cited as landscape only.

## Lab connections (for "why it matters")
- **The virtual cell's messenger layer.** The lab's arc runs genome → RNA → protein →
  structure/image. RNA is the layer between the genome models we covered (Jul 8, Evo2 /
  AlphaGenome) and the proteome/visual-proteomics work (Jul 29). A readable-and-writable RNA
  model is a missing piece of a whole-cell simulator
  ([Human Cell Simulator](/project/human-cell-simulator/)).
- **Open weights, community benchmarks** — RNA-FM (MIT), RNAGenesis (open), EVA (Apache-2.0)
  are all open, with new community benchmarks (BEACON, RNATx-Bench). That is exactly the
  lab's mode: benchmarked, community-owned models
  ([BioImage Model Zoo](/project/bioimage-model-zoo/), [BioEngine](/project/bioengine/)).
- **Design as programmable medicine.** RNATx-Bench's modalities (ASO/siRNA/aptamer/mRNA/gRNA)
  are the RNA-therapeutics stack; a generative model that proposes functional guide RNAs and
  gets them wet-lab-validated is design-build-test in the therapeutic loop the lab cares about.

## De-dup check
- Recent digests: Jul 29 cryo-ET / visual proteomics; Jul 28 genomic-FM evaluation; Jul 27
  ecosystem/strategy; Jul 26 spatial; Jul 25 antibody design; Jul 24 open science; Jul 23
  genome writing; Jul 22 protein dynamics; Jul 21 microscopy VLMs; Jul 20 design+safety.
  **No prior digest** covered RNA foundation models / generative RNA design. Distinct;
  fills the RNA gap in the virtual-cell layer stack.
