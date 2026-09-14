# Newsletter sources — September 14, 2026

**Theme:** **Predicting the 3D genome from sequence** — deep-learning models that take DNA (or 1D
epigenomic tracks) and predict how the genome *folds* in three dimensions: chromatin contact maps,
topologically associating domains (TADs), loops, compartments, and enhancer-promoter contacts.
"Folding the Genome." The arc: predict genome folding from sequence alone and learn the CTCF
grammar (Akita) → do it at megabase scale with transfer learning and read variants through it
(DeepC) → go multiscale and cell-type-specific, kilobase to whole chromosome (Orca) → predict
cell-type-specific organization de novo and run in-silico genetic screens in disease (C.Origami) →
generalize across cell types from cheap epigenomic tracks with a GAN for realism (Epiphany) →
close the loop to gene expression using the 3D contacts via graph attention networks (GraphReg).

**Why now / editorial:** the genome isn't a string — it's a folded 3D object, and where a gene sits
in that fold decides which enhancers reach it. After a run of sequence/molecule and systems topics,
this is a distinct *structural* object: not the linear regulatory code (Aug 19) or basecalling
(Sep 7), but the **spatial architecture** of the genome, predicted directly from sequence, and the
in-silico structural screens it unlocks. Strong journal verifiability (Nat Methods ×2, Nat Genet,
Nat Biotech, Genome Biol, Genome Res) and a clean methodological progression (sequence→fold →
multiscale/cell-type → from-epigenome → fold→function).

**Dedup guard:** Distinct from **Aug 19** (regulatory "dark matter" / variant effect on the *linear*
sequence→expression map), **Aug 9** (genome *language* models), **Sep 6** (gene *regulatory*
networks — transcription-factor circuits), and **Sep 7** (genome *reading* — basecalling/variant
calling). Today's object is the **three-dimensional folding of chromatin** predicted from sequence.
3D genome / Hi-C / chromatin architecture has **never** been a newsletter theme (grep of all posts
returns only incidental mentions).

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on `monitor`
(--since-hours 24 --min-likes 30). ~37th consecutive skip (>five weeks). **Surrogate run (new):**
per avid-pony's guidance, ran a hypha-search sweep (`source=hackernews` + `source=web`) on virtual
cell / AI-agent discovery / single-cell FM queries — service healthy (`/health` ok, `failed: []`),
but results were general/lagged HN chatter with nothing breaking or lab-specific. Useful as a
partial X stand-in; nothing actionable surfaced today. Grok-based X replacement still awaiting credits.

**Verification:** all 6 anchors verified via **NCBI E-utilities** (esearch DOI→PMID, efetch abstract
XML), full `AbstractText` captured; DOI + PMID + journal + year recorded. Only abstract-verified
verbatim quotes used below.

---

## Framing + the founding move — fold from sequence alone

### Fudenberg, Kelley & Pollard — Akita — VERIFIED (PMID 33046897)
- Fudenberg G, Kelley DR, Pollard KS. "Predicting 3D genome folding from DNA sequence with Akita."
  *Nature Methods* 17:1111–1117, 2020. DOI 10.1038/s41592-020-0958-x.
- ABSTRACT-VERIFIED (verbatim): "**the human genome sequence folds in three dimensions into a rich
  variety of locus-specific contact patterns.**"; "**how a given DNA sequence encodes a particular
  locus-specific folding pattern remains unknown.**"; "**Here we present a convolutional neural
  network, Akita, that accurately predicts genome folding from DNA sequence alone.**";
  "**Representations learned by Akita underscore the importance of an orientation-specific grammar
  for CTCF binding sites.**"; "**we demonstrate how Akita can be used to perform in silico saturation
  mutagenesis, interpret eQTLs, make predictions for structural variants and probe species-specific
  genome folding.**"; "**these results enable decoding genome function from sequence through
  structure.**"
- USE: the founding move — a CNN that maps sequence → contact map, learning the *orientation-specific
  CTCF grammar* that shapes loops and domains, and enabling in-silico mutagenesis / variant / eQTL
  interpretation. "Decoding genome function from sequence through structure." Sets up the theme.

## Section 1 — Megabase scale + variant interpretation

### Schwessinger et al. — DeepC — VERIFIED (PMID 33046896)
- Schwessinger R, Gosden M, Downes D, Brown DC, Oudelaar AM, Telenius J, Teh YW, Lunter G, Hughes JR.
  "DeepC: predicting 3D genome folding using megabase-scale transfer learning." *Nature Methods*
  17:1118–1124, 2020. DOI 10.1038/s41592-020-0960-3.
- ABSTRACT-VERIFIED (verbatim): "**Predicting the impact of noncoding genetic variation requires
  interpreting it in the context of three-dimensional genome architecture.**"; "**We have developed
  deepC, a transfer-learning-based deep neural network that accurately predicts genome folding from
  megabase-scale DNA sequence.**"; "**DeepC predicts domain boundaries at high resolution, learns the
  sequence determinants of genome folding and predicts the impact of both large-scale structural and
  single base-pair variations.**"
- USE: the co-published sibling (same NatMeth issue) — transfer learning lets a model see *megabase*
  context, resolve domain boundaries, and, crucially, read the 3D impact of variants from a single
  base pair up to large structural rearrangements. 3D architecture as the missing context for
  noncoding variant interpretation.

## Section 2 — Multiscale and cell-type-specific

### Zhou — Orca — VERIFIED (PMID 35551308)
- Zhou J. "Sequence-based modeling of three-dimensional genome architecture from kilobase to
  chromosome scale." *Nature Genetics* 54:725–734, 2022. DOI 10.1038/s41588-022-01065-4.
- ABSTRACT-VERIFIED (verbatim): "**a sequence-based deep-learning approach, Orca, that predicts
  directly from sequence the 3D genome architecture from kilobase to whole-chromosome scale.**";
  "**Orca captures the sequence dependencies of structures including chromatin compartments and
  topologically associating domains, as well as diverse types of interactions from CTCF-mediated to
  enhancer-promoter interactions and Polycomb-mediated interactions with cell-type specificity.**";
  "**Orca enables various applications including predicting structural variant effects on multiscale
  genome organization and it recapitulated effects of experimentally studied variants at varying
  sizes (300 bp to 90 Mb).**"; "**Orca enables in silico virtual screens to probe the sequence basis
  of 3D genome organization at different scales.**"
- USE: the multiscale leap — one model spanning *kilobase to whole chromosome*, capturing
  compartments, TADs, and multiple interaction types with cell-type specificity; recapitulates
  variant effects across five orders of magnitude in size (300 bp → 90 Mb) and enables in-silico
  virtual screens of the sequence basis of folding.

## Section 3 — De novo cell-type prediction + in-silico genetic screens

### Tan et al. — C.Origami — VERIFIED (PMID 36624151)
- Tan J, Shenker-Tauris N, Rodriguez-Hernaez J, Wang E, Sakellaropoulos T, Boccalatte F, Thandapani P,
  Skok J, Aifantis I, Fenyö D, Xia B, Tsirigos A. "Cell-type-specific prediction of 3D chromatin
  organization enables high-throughput in silico genetic screening." *Nature Biotechnology*
  41:1140–1150, 2023. DOI 10.1038/s41587-022-01612-8.
- ABSTRACT-VERIFIED (verbatim): "**Experimental methods for measuring three-dimensional chromatin
  organization, such as Hi-C, are costly and have technical limitations, restricting their broad
  application particularly in high-throughput genetic perturbations.**"; "**We present C.Origami, a
  multimodal deep neural network that performs de novo prediction of cell-type-specific chromatin
  organization using DNA sequence and two cell-type-specific genomic features-CTCF binding and
  chromatin accessibility.**"; "**We further developed an in silico genetic screening approach to
  assess how individual DNA elements may contribute to chromatin organization and to identify
  putative cell-type-specific trans-acting regulators**"; "**Applying this approach to leukemia cells
  and normal T cells, we demonstrate that cell-type-specific in silico genetic screening … can be
  used to systematically discover novel chromatin regulation circuits in both normal and
  disease-related biological systems.**"
- USE: the disease/screening payoff — a multimodal net (sequence + CTCF + accessibility) predicts
  cell-type-specific organization de novo, then powers *in-silico genetic screens* that find the DNA
  elements and trans-acting regulators shaping architecture — demonstrated in leukemia vs normal T
  cells. Cheap, high-throughput hypothesis generation where Hi-C is costly.

## Section 4 — Generalizing from epigenomic tracks

### Yang et al. — Epiphany — VERIFIED (PMID 37280678)
- Yang R, Das A, Gao VR, Karbalayghareh A, Noble WS, Bilmes JA, Leslie CS. "Epiphany: predicting Hi-C
  contact maps from 1D epigenomic signals." *Genome Biology* 24:134, 2023. DOI
  10.1186/s13059-023-02934-9.
- ABSTRACT-VERIFIED (verbatim): "**Recent deep learning models that predict the Hi-C contact map from
  DNA sequence achieve promising accuracy but cannot generalize to new cell types**"; "**We propose
  Epiphany, a neural network to predict cell-type-specific Hi-C contact maps from widely available
  epigenomic tracks.**"; "**Epiphany uses bidirectional long short-term memory layers to capture
  long-range dependencies and optionally a generative adversarial network architecture to encourage
  contact map realism.**"; "**Epiphany shows excellent generalization to held-out chromosomes within
  and across cell types, yields accurate TAD and interaction calls, and predicts structural changes
  caused by perturbations of epigenomic signals.**"
- USE: the generalization beat — names the weakness of sequence-only models (they don't transfer to
  new cell types) and answers with a biLSTM (+ optional GAN for realism) that predicts Hi-C from
  *widely available epigenomic tracks*, generalizing across cell types and predicting perturbation
  effects. From "one model per genome" toward portable, cell-type-aware prediction.

## Section 5 — Closing the loop: 3D contacts → gene expression

### Karbalayghareh, Sahin & Leslie — GraphReg — VERIFIED (PMID 35396274)
- Karbalayghareh A, Sahin M, Leslie CS. "Chromatin interaction-aware gene regulatory modeling with
  graph attention networks." *Genome Research* 32:930–944, 2022. DOI 10.1101/gr.275870.121.
- ABSTRACT-VERIFIED (verbatim): "**Linking distal enhancers to genes and modeling their impact on
  target gene expression are longstanding unresolved problems in regulatory genomics**"; "**we
  present a new deep learning approach called GraphReg that exploits 3D interactions from chromosome
  conformation capture assays to predict gene expression from 1D epigenomic data or genomic DNA
  sequence.**"; "**By using graph attention networks to exploit the connectivity of distal elements
  up to 2 Mb away in the genome, GraphReg more faithfully models gene regulation and more accurately
  predicts gene expression levels than the state-of-the-art deep learning methods for this task.**";
  "**Feature attribution used with GraphReg accurately identifies functional enhancers of genes, as
  validated by CRISPRi-FlowFISH and TAP-seq assays**"
- USE: the payoff — the fold matters *because* it decides which enhancers reach which genes. GraphReg
  turns the 3D contact graph into a *graph attention network* that predicts expression from epigenome
  or sequence, out-predicting prior CNNs and the activity-by-contact model, with attributions
  validated by CRISPRi-FlowFISH/TAP-seq. Structure → function, and a graph-nets thread back to the
  [knowledge-graph digest](/post/newsletter-2026-09-11/).

## Section 6 — Lab hook + horizon
- The through-line: **the genome is a 3D object, and AI can predict its shape from sequence.** Where
  a gene sits in the fold — which enhancers loop to it, which TAD walls contain it — is as important
  as the letters themselves, and these models make that architecture predictable, mutable in silico,
  and cheap to screen. The trajectory is the lab's: from single-purpose CNNs → multiscale, cell-type-
  specific, *graph*-based models that connect structure to function.
- Ties to lab interests: graph neural/attention nets (GraphReg) echo the
  [knowledge-graph digest](/post/newsletter-2026-09-11/) and [cell-cell communication GNNs](/post/newsletter-2026-09-13/)
  — biology keeps becoming graphs. In-silico genetic screens (Orca, C.Origami) are exactly the kind
  of cheap, hypothesis-generating *dry-lab* experiment that pairs with the lab's
  [self-driving-lab](/post/newsletter-2026-08-21/) ambitions.
- Open + benchmarked ethos: these models are open and measured on shared Hi-C/Micro-C benchmarks —
  the publish-the-model-*and*-the-data spirit behind the [BioImage Model Zoo](/project/bioimage-model-zoo/)
  and [BioEngine](/project/bioengine/).
- Horizon / strategy radar: 3D genome prediction is a load-bearing layer for a
  [virtual cell](/project/human-cell-simulator/) — a faithful cell model must know not just its gene
  sequences but how the genome is *packed and looped* in each cell type, and how a variant reshapes
  that architecture. A concrete instance of sequence → structure → function, end to end.
