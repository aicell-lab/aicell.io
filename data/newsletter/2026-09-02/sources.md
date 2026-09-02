# Newsletter sources — September 2, 2026

**Theme:** AI for **protein function prediction** — reading a protein's *job* (Enzyme
Commission numbers, Gene Ontology terms, residue-level sites) from its sequence and/or
structure. The "dark proteome" problem: structure prediction (AlphaFold/ESMFold) gave us
the *fold* at genome scale, but a fold is not a function — vast numbers of proteins remain
functionally uncharacterized. "What the Fold Won't Tell You."

**Dedup guard:** Distinct from the structure/design run — Aug 12 (co-folding + affinity),
Aug 18 (de novo protein *design*), Aug 20 (RNA structure), Aug 11 (conformational
*ensembles* / MD emulation), Aug 31 (cryo-EM heterogeneity). Those are all about *shape*;
this is about *function/annotation* from sequence/structure. Distinct from Aug 9 (genome
language models) and Aug 19 (regulatory genomics / variant effect) — those read DNA;
this reads proteins for their catalytic/biological role. Distinct from Aug 7 (de novo
peptide sequencing / MS proteomics).

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on monitor, search,
AND discover (all three endpoints). ~24th consecutive skip (>three weeks). Grok replacement
wired, awaiting xAI credits. (Note: hypha-search metasearch now available as a partial
discovery replacement.)

All anchors verified by two parallel general-purpose subagents against Crossref + Europe PMC
(core `abstractText`), with VERBATIM abstract quotes. Only abstract-verified quotes are used.

---

## Framing — structure at scale, function still dark

### ESM-2 / ESMFold — protein LM structure at metagenomic scale — VERIFIED (background/hook)
- Lin, Z., … Rives, A. "Evolutionary-scale prediction of atomic-level protein structure with
  a language model." *Science* 379(6637):1123–1130, 2023. DOI 10.1126/science.ade2574. First
  author Zeming Lin; senior Alexander Rives. Resolves (Crossref + Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**We demonstrate direct inference of full atomic-level
  protein structure from primary sequence using a large language model**"; "**We apply this
  capability to construct the ESM Metagenomic Atlas by predicting structures for >617 million
  metagenomic protein sequences, including >225 million that are predicted with high
  confidence, which gives a view into the vast breadth and diversity of natural proteins.**"
- USE: the hook — we can now fold hundreds of millions of proteins, but folding ≠ knowing what
  they DO. The "vast breadth and diversity" is exactly the dark proteome function prediction
  must annotate.

## Section 1 — Function from sequence alone

### DeepGOPlus — CNN + sequence similarity → GO terms — VERIFIED
- Kulmanov, M. & Hoehndorf, R. "DeepGOPlus: improved protein function prediction from
  sequence." *Bioinformatics* 36(2):422–429, 2020 (online 2019-07-27). DOI
  10.1093/bioinformatics/btz595. Resolves (Crossref + Europe PMC). (Year nuance: Crossref
  online 2019 vs. issue 2020 — cite 2020 issue.)
- ABSTRACT-VERIFIED (verbatim): "**We developed a novel method for predicting protein
  functions from sequence alone which combines deep convolutional neural network (CNN) model
  with sequence similarity based predictions**"; "**We evaluate the performance of DeepGOPlus
  using the CAFA3 evaluation measures and achieve an Fmax of 0.390, 0.557 and 0.614 for BPO,
  MFO and CCO evaluations, respectively**"; "**DeepGOPlus can annotate around 40 protein
  sequences per second on common hardware.**"

### ProteInfer — CNN predicts EC + GO from unaligned sequence, in-browser — VERIFIED
- Sanderson, T., Bileschi, M.L., Belanger, D. & Colwell, L.J. "ProteInfer, deep neural
  networks for protein functional inference." *eLife* 12:e80942, 2023 (2023-02-27). DOI
  10.7554/eLife.80942. First author Theo Sanderson; senior Lucy J. Colwell. Resolves
  (Crossref + Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**Here we introduce ProteInfer, which instead employs deep
  convolutional neural networks to directly predict a variety of protein functions - Enzyme
  Commission (EC) numbers and Gene Ontology (GO) terms - directly from an unaligned amino acid
  sequence**"; "**This approach provides precise predictions which complement alignment-based
  methods, and the computational efficiency of a single neural network permits novel and
  lightweight software interfaces, which we demonstrate with an in-browser graphical interface
  for protein function prediction in which all computation is performed on the user's personal
  computer with no data uploaded to remote servers.**"
- USE: complements (not replaces) alignment; the in-browser, local-compute UI is an
  open/accessible-tools angle that fits the lab's ethos.

## Section 2 — Enzymes: getting the EC number right

### CLEAN — contrastive learning for enzyme function — VERIFIED
- Yu, T., Cui, H., Li, J.C., Luo, Y., Jiang, G. & Zhao, H. "Enzyme function prediction using
  contrastive learning." *Science* 379(6639):1358–1363, 2023 (2023-03-31). DOI
  10.1126/science.adf2465. First author Tianhao Yu; senior Huimin Zhao. Resolves (Crossref +
  Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**We present a machine learning algorithm named CLEAN
  (contrastive learning-enabled enzyme annotation) to assign EC numbers to enzymes with better
  accuracy, reliability, and sensitivity compared with the state-of-the-art tool BLASTp**";
  "**The contrastive learning framework empowers CLEAN to confidently (i) annotate understudied
  enzymes, (ii) correct mislabeled enzymes, and (iii) identify promiscuous enzymes with two or
  more EC numbers-functions that we demonstrate by systematic in silico and in vitro
  experiments**"; "**We anticipate that this tool will be widely used for predicting the
  functions of uncharacterized enzymes.**"
- USE: beats BLASTp (alignment); the (ii) correct-mislabeled and (iii) promiscuous-enzyme
  points show AI doing more than lookup. In-vitro validation is a strength to note.

## Section 3 — Function from structure

### DeepFRI — graph conv nets on structure + LM features, residue-level — VERIFIED
- Gligorijević, V., … Bonneau, R. "Structure-based protein function prediction using graph
  convolutional networks." *Nature Communications* 12:3168, 2021 (2021-05-26). DOI
  10.1038/s41467-021-23303-9. First author Vladimir Gligorijević; senior Richard Bonneau.
  Resolves (Crossref + Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**Here, we introduce DeepFRI, a Graph Convolutional Network
  for predicting protein functions by leveraging sequence features extracted from a protein
  language model and protein structures**"; "**It outperforms current leading methods and
  sequence-based Convolutional Neural Networks and scales to the size of current sequence
  repositories**"; "**Class activation mapping allows function predictions at an unprecedented
  resolution, allowing site-specific annotations at the residue-level in an automated
  manner.**"
- USE: bridges to the structure era (uses structures + LM embeddings); residue-level = *where*
  the function lives, not just *that* it exists. Natural pairing with ESMFold structures.

## Section 4 — The honest frontier: how do we know it's right?

### CAFA3 — community assessment of function prediction — VERIFIED
- Zhou, N., … Radivojac, P. & Friedberg, I. "The CAFA challenge reports improved protein
  function prediction and new functional annotations for hundreds of genes through
  experimental screens." *Genome Biology* 20:244, 2019 (2019-11-19). First author Naihui Zhou;
  senior Iddo Friedberg. DOI 10.1186/s13059-019-1835-8. Resolves (Crossref + Europe PMC).
- ABSTRACT-VERIFIED (verbatim): "**The Critical Assessment of Functional Annotation (CAFA) is
  an ongoing, global, community-driven effort to evaluate and improve the computational
  annotation of protein function**"; "**In a novel and major new development, computational
  predictions and assessment goals drove some of the experimental assays, resulting in new
  functional annotations for more than 1000 genes**"; "**We conclude that while predictions of
  the molecular function and biological process annotations have slightly improved over time,
  those of the cellular component have not.**"
- USE: the prove-it anchor — a community benchmark with EXPERIMENTAL validation, and an honest
  admission that not every category has improved. Same discipline as CryoBench (Aug 31) and
  the Ma multimodality benchmark (Sep 1).

## Section 5 — Lab hook + horizon
- The unknown/dark proteome is the **parts list** a virtual cell needs: to simulate a cell you
  must know what each protein DOES, not just its shape. Ties to the Human Cell Simulator
  (/project/human-cell-simulator/) and the virtual-cell horizon (/post/newsletter-2026-08-15/).
- Structure→function pairing: ESMFold folds the metagenome; DeepFRI reads function off those
  structures — the two halves of "annotate everything."
- Substrate/neighbor: the Human Protein Atlas (KTH) maps where proteins are and (increasingly)
  what they do — spatial + functional annotation together.
- Open, callable, benchmarked models: ProteInfer's local/in-browser UI and CLEAN/DeepFRI as
  callable tools fit the BioImage Model Zoo (/project/bioimage-model-zoo/) + BioEngine
  (/project/bioengine/) ethos; CAFA is the prove-it standard (/post/newsletter-2026-07-27/).
