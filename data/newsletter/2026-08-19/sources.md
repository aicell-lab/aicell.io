# Newsletter sources — 2026-08-19 (compiled UTC 2026-08-19T20:05Z)

Theme: **AI for the regulatory genome — reading what non-coding DNA *does*, and
what a mutation *breaks*.** Protein-coding exons are ~1–2% of the genome; the rest
is regulatory "dark matter," and it is where the large majority of disease-associated
variants sit. A supervised sequence→function track learned to predict regulatory
activity straight from DNA — **Enformer** (expression from long-range sequence),
**Borzoi** (base-resolution RNA-seq coverage: transcription, splicing, polyA) — while
**AlphaMissense** cracked the *coding* side (missense pathogenicity). **AlphaGenome**
(2026) unifies the regulatory side: one model, ~1 Mb of context at single-base
resolution, many modalities. And the honest frontier is sharp: these models still
**capture promoters but miss distal enhancers**, and predict *personal-genome*
variation poorly — a prove-it story at genome scale. Lab hook: the **virtual cell**
needs a genotype→cell-state module, and it must be open, callable, and validated.

## Provenance / method
- Web research (WebSearch + WebFetch), each anchor cross-checked by two independent
  research agents against **Crossref**, **PubMed / Europe PMC**, **Semantic Scholar**,
  and official DeepMind sources.
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  returns **HTTP 402 Insufficient credits** (getxapi out of credits ~8 weeks; **10th
  straight skipped sweep**). The Grok `x_search` replacement is wired but the xAI team
  account has **no credits yet** (403). Flagged to Wei.

## Anchors (all verified — venue / DOI / byline / status)
- **Enformer** — Avsec Ž, … **Kelley DR (senior)**, "Effective gene expression
  prediction from sequence by integrating long-range interactions," ***Nature Methods*
  18:1196–1203, 2021**, DOI 10.1038/s41592-021-01252-x (PMID 34608324). **Peer-reviewed.**
- **Borzoi** — Linder J, … **Kelley DR (senior)**, "Predicting RNA-seq coverage from DNA
  sequence as a unifying model of gene regulation," ***Nature Genetics*, online 8 Jan
  2025**, DOI 10.1038/s41588-024-02053-6 (PMID 39779956). **Peer-reviewed** (was bioRxiv
  10.1101/2023.08.30.555582).
- **AlphaMissense** — Cheng J, … **Avsec Ž (senior/last)** (Hassabis, Kohli among senior
  authors), "Accurate proteome-wide missense variant effect prediction with AlphaMissense,"
  ***Science* 381, eadg7492, 2023**, DOI 10.1126/science.adg7492 (PMID 37733863). **Peer-reviewed.**
- **AlphaGenome** — Avsec Ž (first), … **Kohli P (senior)**, "Advancing regulatory variant
  effect prediction with AlphaGenome," ***Nature*, published 28 Jan 2026**, DOI
  10.1038/s41586-025-10014-0. **Peer-reviewed** (bioRxiv preprint 10.1101/2025.06.25.661532,
  Jun 2025; DeepMind API preview announced 25 Jun 2025). 27 authors, Google DeepMind.
- **Honest-frontier** — Karollus A, Mauermeier T, **Gagneur J (senior)**, "Current
  sequence-based models capture gene expression determinants in promoters but mostly ignore
  distal enhancers," ***Genome Biology* 24:56, 2023**, DOI 10.1186/s13059-023-02899-9
  (PMC10045630). **Peer-reviewed** (open access). TU Munich.
  - Companion (personal-genome angle): "Personal transcriptome variation is poorly explained
    by current genomic deep learning models," ***Nature Genetics*, 30 Nov 2023**, DOI
    10.1038/s41588-023-01574-w (Ioannidis lab; widely cited as "Sasse et al." — co-first-author
    ordering NOT fully verified, so cite by venue/lab, not the shorthand).
- **GWAS-non-coding framing** — Schipper M & **Posthuma D (senior)**, "Demystifying
  non-coding GWAS variants: an overview of computational tools and methods," ***Human
  Molecular Genetics*, 2022**, DOI 10.1093/hmg/ddac198. Safe wording: "roughly 90% (the
  large majority) of GWAS trait-associated variants fall in non-coding regions."

## Verification discipline (numbers stated ONLY where character-verified)
- **Enformer:** abstract says it integrates long-range interactions "**up to 100 kb away**"
  and gives "**more accurate variant effect predictions** … for both natural genetic variants
  and saturation mutagenesis (MPRA)." The **~200 kb input window** (196,608 bp) is from the
  paper body/methods, **not** the abstract → phrase as "an input window of about 200,000 bases,
  reaching regulatory signals up to 100 kb away," don't quote "200 kb" as an abstract number.
- **Borzoi:** predicts **cell-/tissue-specific RNA-seq coverage** from sequence and scores
  variant effects across **transcription, splicing and polyadenylation**. "Base-resolution" is
  an accurate descriptor of the model but is **not** an abstract quote — use as descriptor, not
  as a quotation.
- **AlphaMissense:** an **adaptation of AlphaFold** fine-tuned on population variant frequencies;
  classifies "**89%** of missense variants as likely benign or likely pathogenic" — the **only**
  quotable abstract number. The "**~71 million** possible missense variants" and the
  benign/pathogenic/uncertain split (~57/32/11) are **NOT abstract-verifiable** → do not state as
  abstract facts. Covers the **protein-coding / missense** side (complement to the regulatory models).
- **AlphaGenome:** input **up to 1,000,000 bp (1 Mb)** at **single base-pair resolution** — the
  headline is *long-range context AND base resolution together*. Predicts a broad set of regulatory
  modalities (expression / RNA-seq coverage, splicing incl. sites/usage/junctions, chromatin
  accessibility, TF binding, histone marks, TSS/TES, 3D contact maps); DeepMind states **11
  modalities**. Benchmarks (verified): "**outperformed best external models on 22 of 24**
  single-sequence predictions" and "**matched or exceeded top models on 24 of 26** variant-effect
  evaluations." Released as a **non-commercial research API preview**; builds on Enformer,
  complements AlphaMissense. **DO NOT quote:** adoption stats (~3000 scientists / 1M requests/day)
  and "trained in 4 hours / half of Enformer's compute" — **DeepMind blog/press only**, mark as
  DeepMind-reported if used; architecture details (U-Net+transformer) unverified → omit.
- **Karollus 2023 (honest frontier):** paraphrase (verified as the paper's claims, not verbatim) —
  SOTA models (notably Enformer) **capture promoter determinants but fail to capture the causal
  effects of distal enhancers**, especially at longer distances; effective long-range integration
  is far more limited than the nominal receptive field. A **correlative-training** critique. The
  companion Nat Genet 2023 paper: current models predict **personal-genome** expression variation
  poorly and can get the **direction of a variant's effect wrong** (paraphrase).
- **GWAS:** state **"~90% (the large majority)"** non-coding — do NOT assert a single exact %; some
  fine-mapped analyses go to ~95% (upper-end, context-dependent). No fabricated numbers anywhere.
- **Nice verified thread:** **Žiga Avsec** is first author on **Enformer** (2021) and **AlphaGenome**
  (2026), and senior/last author on **AlphaMissense** (2023) — one researcher across the arc.

## De-dup / variety (important)
AI for the **regulatory genome / non-coding variant-effect prediction** (supervised
sequence→function) has **not** been a dedicated digest theme, and is a clean omics pivot after
the recent imaging + protein run:
- **Aug 9 "The Grammar of the Genome"** = **generative genome *language* models** (Evo /
  DNA LMs learning sequence distributions). Today = **supervised sequence→function prediction**
  (expression, splicing, chromatin) and **variant-effect** scoring — a *different track* (predict
  activity & mutation impact, not generate/model sequence). Explicitly distinguished.
- **Jul 28** = **benchmarking / evaluation reckoning of genome FMs**. Today = the regulatory
  **prediction models themselves** (Enformer→Borzoi→AlphaGenome) + a *specific* variant-effect
  limitation literature (Karollus) — different altitude.
- **Aug 18 protein design** = *molecular structure / synthesis*. Today = *genome regulation /
  function prediction*. Different biomolecule, different problem (AlphaMissense here is the
  *coding* complement, framed as such).
- **Aug 16/17 imaging FMs** = images. Today = DNA sequence → regulatory activity. Distinct data.
- **Aug 2 / Aug 15 virtual cell** = today supplies the **genotype→cell-state** module a virtual
  cell needs; linked as a component, not repeated.
Clear separation. Clear to run.

## Item 1 — Reading what DNA does (Enformer, Borzoi)
- **The problem:** ~98% of the genome doesn't code for protein; it *regulates* — enhancers,
  promoters, splice signals. Reading that "dark matter" from sequence is the goal.
- **Enformer** (Avsec et al., *Nat Methods* 2021; senior Kelley) — a transformer that predicts gene
  expression and chromatin state from DNA over an **~200 kb input window**, integrating regulatory
  interactions **up to 100 kb away**, and gives **more accurate variant-effect predictions** than
  prior CNNs (validated against natural variants + MPRA saturation mutagenesis).
- **Borzoi** (Linder et al., *Nat Genet* 2025; senior Kelley) — predicts **cell-/tissue-specific
  RNA-seq coverage** from sequence at base-pair resolution, unifying **transcription, splicing and
  polyadenylation** in one model, and scoring variant effects across all of them.

## Item 2 — The variant question (why it matters; AlphaMissense the coding complement)
- **Where disease hides:** roughly **90%** of GWAS trait-/disease-associated variants fall in
  **non-coding** regions (Schipper & Posthuma 2022) — i.e., in exactly the regulatory sequence these
  models try to read. Interpreting a non-coding variant means predicting how it changes regulation.
- **The coding side is further along:** **AlphaMissense** (Cheng et al., *Science* 2023; senior
  Avsec) — an **AlphaFold adaptation** that classifies **89%** of all possible human missense
  variants as likely benign or likely pathogenic. But that's the **protein-coding** slice; the
  **non-coding regulatory** variant is the harder, less-solved problem — which is where the
  sequence→function models come back in.

## Item 3 — AlphaGenome + the honest frontier (prove-it at genome scale)
- **AlphaGenome** (Avsec et al., *Nature*, Jan 2026; senior Kohli; Google DeepMind) — the unifying
  leap: one DNA sequence model over **up to 1 Mb of context at single-base resolution** (previous
  models traded long range against fine resolution; this does both), predicting a broad set of
  regulatory modalities (expression, splicing incl. junctions, chromatin accessibility, TF binding,
  histone marks, TSS/TES, 3D contacts — DeepMind: 11 modalities). Benchmarks: **22/24** single-sequence
  and **24/26** variant-effect evaluations at or above the best external models. Released as a
  **non-commercial research API preview**; builds on Enformer, complements AlphaMissense.
- **The honest frontier (prove-it).** Scale hasn't closed the gap that matters most:
  - **Karollus et al.** (*Genome Biol* 2023, Gagneur lab) — SOTA models **capture promoters but
    largely ignore distal enhancers**; their effective long-range reach is far shorter than their
    nominal window, so predicting a *distal* variant's effect "rarely leads to meaningful results."
  - A 2023 *Nature Genetics* study (Ioannidis lab) — current models predict **personal-genome**
    expression variation poorly and can get a variant's **direction of effect wrong**.
  - The root critique is **correlative training**: models learn from evolutionary differences
    *between genes*, so causal generalization to *new variants* is not guaranteed.
- **Why it matters for the lab.** (1) The **virtual cell** ([Aug 2](/post/newsletter-2026-08-02/) /
  [Aug 15](/post/newsletter-2026-08-15/)) needs a **genotype→cell-state** module; reading the
  regulatory genome is that module, and it's a [foundation-model-for-biology](/project/bioimage-model-zoo/)
  problem. (2) These large models need **open, standard-format, callable serving** — the
  [BioEngine](/project/bioengine/) / Model Zoo ethos, now for genomics. (3) The same **prove-it
  discipline** the digest keeps returning to: a predicted variant effect is a **hypothesis**, validated
  only when an MPRA or a functional assay agrees — and here the models are demonstrably strongest on the
  easy (promoter) cases and weakest on the hard (distal, personal) ones.

## Lab connections (for "why it matters")
- **virtual cell (Aug 2 / Aug 15)** — the genome→cell-state module a virtual cell needs.
- **bioimage-model-zoo / bioengine** — open, callable model serving, now for genomics FMs.
- **Aug 9 genome LMs** — sibling track (generative), today = supervised function/variant prediction.
- **Aug 5 privacy/genomics** — personal genomes are exactly where these models struggle; privacy + variant interpretation meet.
- **prove-it (Jul 27)** — a predicted variant effect is a hypothesis; validate with MPRA/functional assays.

## De-dup check
Recent digests: Aug 18 protein design; Aug 17 pathology FMs; Aug 16 segmentation FMs; Aug 15
single-cell FMs; Aug 14 AI co-scientist; Aug 13 spatial transcriptomics; Aug 12 co-folding; Aug 11
protein dynamics; Aug 10 optical pooled screening; Aug 9 genome language models; Aug 8 smart
microscopy; Aug 7 proteomics; Aug 6 virtual staining; Aug 5 federated; Aug 4 profiling; Aug 3
small-molecule design; Aug 2 virtual cell; Aug 1 prove-it/pathology. **Regulatory-genome / non-coding
variant-effect prediction has not been a digest theme.** Distinct from the Aug 9 generative genome LMs
(supervised function vs generative LM) and the Jul 28 benchmarking piece; a clean omics pivot after the
imaging (16/17) + protein (18) run. Clear to run.
