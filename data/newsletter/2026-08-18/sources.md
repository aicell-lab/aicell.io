# Newsletter sources — 2026-08-18 (compiled UTC 2026-08-18T19:40Z)

Theme: **De novo protein design — generative AI that *invents* proteins.** The
inverse of structure prediction: instead of reading a sequence to guess its fold,
these models are asked for a fold (or a function, or a plain-language brief) and
they *write the protein* to match. Three landmark tools define the generative
toolkit — **ProteinMPNN** (sequence design / inverse folding), **RFdiffusion**
(diffusion over backbones), and **Chroma** (a *programmable* generative model) —
**ESM3** turns design into "prompting" a protein language model across sequence,
structure and function, the field's coming-of-age was sealed by the **2024 Nobel
Prize in Chemistry**, and the frontier is now designed *catalysis*: a 2025 *Nature*
paper designs working **metallohydrolase enzymes** with **RFdiffusion2**. The lab
hook: this is the **design → build → test** loop and the open **model-serving**
ethos the lab keeps betting on — and the prove-it discipline (a designed protein
is a *hypothesis* until the crystal structure or assay confirms it).

## Provenance / method
- Web research (WebSearch + WebFetch), each anchor cross-checked by two independent
  research agents against **Crossref** (api.crossref.org), **PubMed**, **Semantic
  Scholar**, and official press releases (publisher pages often paywalled).
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  returns **HTTP 402 Insufficient credits** (getxapi out of credits ~8 weeks; **9th
  straight skipped sweep**; `discover` also 402). The Grok `x_search` replacement is
  wired but the xAI team account has **no credits yet** (403). Flagged to Wei.

## Anchors (all verified — venue / DOI / byline / peer-review status)
- **ProteinMPNN** — Dauparas J, … **Baker D (senior)**, "Robust deep learning–based
  protein sequence design using ProteinMPNN," ***Science* 378(6615):49–56, 2022**,
  DOI 10.1126/science.add2187 (PMID 36108050). **Peer-reviewed.**
- **RFdiffusion** — Watson JL, … **Baker D (senior)**, "De novo design of protein
  structure and function with RFdiffusion," ***Nature* 620(7976):1089–1100, 2023**,
  DOI 10.1038/s41586-023-06415-8 (PMID 37433327). **Peer-reviewed.**
- **Chroma** — Ingraham JB, … **Grigoryan G (senior)**, "Illuminating protein space
  with a programmable generative model," ***Nature* 623(7989):1070–1078, 2023**,
  DOI 10.1038/s41586-023-06728-8 (PMID 37968394). **Peer-reviewed.** (Generate Biomedicines.)
- **ESM3** — Hayes T, … **Rives A (senior)**, "Simulating 500 million years of
  evolution with a language model," ***Science* 387(6736), 21 Feb 2025**,
  DOI 10.1126/science.ads0018 (PMID 39818825). **Peer-reviewed** (bioRxiv preprint
  10.1101/2024.07.01.600583, Jul 2024). EvolutionaryScale.
- **2024 Nobel Prize in Chemistry** — Royal Swedish Academy of Sciences press release
  (nobelprize.org/prizes/chemistry/2024). One half **David Baker** *"for computational
  protein design"*; other half jointly **Demis Hassabis & John Jumper** *"for protein
  structure prediction."*
- **Current pulse (peer-reviewed)** — Kim D, … **Baker D (senior)**, "Computational
  design of metallohydrolases," ***Nature*, online 3 Dec 2025** (print 649:246–253),
  DOI 10.1038/s41586-025-09746-w. **Peer-reviewed.** De novo **zinc metallohydrolase**
  enzymes designed with **RFdiffusion2**, catalytic activity + crystal structures
  confirmed experimentally.
  - Underlying method (**preprint — labelled**): Krishna R & Baker D (corresp.), "Atom
    level enzyme active site scaffolding using RFdiffusion2," **bioRxiv
    10.1101/2025.04.09.648075** (Apr 2025). Code released 15 Sep 2025 (Rosetta Commons).

## Verification discipline (numbers stated ONLY where character-verified)
- **ProteinMPNN:** native-backbone **sequence recovery 52.4% (ProteinMPNN) vs 32.9%
  (Rosetta)** — both figures verbatim in the abstract; safe to quote. It *rescues
  previously failed designs* (monomers, cyclic homo-oligomers, tetrahedral
  nanoparticles, target binders) validated by X-ray/cryo-EM. No specific
  solubility/expression % is stated → **not quoted**.
- **RFdiffusion:** RoseTTAFold fine-tuned on structure-**denoising** → generative
  backbone model. Abstract-named design categories: unconditional/topology-constrained
  monomers, **protein binders, symmetric oligomers, enzyme active-site scaffolding,
  symmetric motif scaffolding for therapeutic & metal-binding proteins**. Abstract says
  "**hundreds**" of designs experimentally characterized — **no exact count / success-%
  is quotable**; a designed binder–influenza-haemagglutinin complex matched the design
  model by cryo-EM.
- **Chroma:** programmable diffusion model conditioned on **symmetries, substructure,
  shape, semantics, and natural-language prompts**; frames design as Bayesian inference
  under constraints. **310 proteins** experimentally characterized (highly expressed,
  fold, favourable biophysics) — the **310** figure is verbatim; safe to quote.
- **ESM3:** multimodal generative protein LM over **sequence + structure + function**;
  scales **1.4B / 7B / 98B** params. Generated **esmGFP**, a bright green fluorescent
  protein at **58% sequence identity to the nearest known fluorescent protein** (96
  mutations over 229 aa), **36% to *A. victoria* wild-type GFP**; closest natural
  protein eqFP578 (~53% identity). The "**equivalent to >500 million years of natural
  evolution**" figure is the **authors' ESTIMATE** (from GFP diversification rate) —
  attribute as *"the authors estimate,"* never as measured fact. **ESM3-open** weights
  released; esmGFP sequence public-domain, plasmids in Addgene.
- **Nobel:** citation wording exact ("computational protein design" / "protein structure
  prediction"). **"AlphaFold" is my own gloss**, not part of the official citation.
- **Metallohydrolases (current pulse):** state as *"the **RFdiffusion2 method**, used in a
  2025 Nature paper on metallohydrolase design"* — the Nature paper's title is
  "Computational design of metallohydrolases," NOT a paper titled "RFdiffusion2" (avoid the
  C&EN-style conflation). RFdiffusion2 benchmark: **scaffolded all 41/41** diverse active
  sites in silico **vs 16/41** for prior SOTA — from the **bioRxiv preprint** (labelled).
- **AVOIDED:** an unverified "RFdiffusion3, Dec 2025" claim surfaced in secondary coverage
  — **NOT cited** (no DOI/paper confirmed). No fabricated numbers anywhere.

## De-dup / variety (important)
De novo / **generative protein design** (inventing new proteins) has **not** been a
dedicated digest theme. It is the *inverse* of the recent protein digests, and a
different modality from the small-molecule one:
- **Aug 11 "After the Fold, the Motion"** = protein **dynamics** (MD, conformational
  ensembles) — *analysing how existing proteins move*. Today = *creating new proteins
  that never existed*. Opposite direction (analysis vs synthesis).
- **Aug 12 "The Handshake"** = **co-folding / binding-affinity** prediction — *predicting
  interactions of existing molecules*. Today = *generating* the molecule itself.
- **Aug 3 small-molecule design** = generative design of **small molecules** (chemistry).
  Today = generative design of **proteins/macromolecules** (different modality, different
  models — diffusion over backbones + protein LMs). Linked as siblings, not repeats.
- **Aug 15 single-cell FMs / Aug 9 genome FMs** = sequence/omics FMs for *cells/genomes*;
  ESM3 here is a *protein* LM used **generatively** to design new proteins — different aim.
- **Aug 16/17 image FMs** = imaging. Today = structural/sequence generative design. Distinct.
Clear separation. Clear to run.

## Item 1 — The inverse problem, learned (ProteinMPNN, RFdiffusion, Chroma)
- **The flip:** structure *prediction* reads a sequence → fold. Protein *design* runs it
  backwards: specify the fold (or function, or a brief) → have a model *write* a sequence
  and/or backbone that realises it. Deep generative models made the inverse problem tractable.
- **ProteinMPNN** (Dauparas et al., *Science* 2022) — **inverse folding**: given a target
  backbone, design a sequence that folds to it. Message-passing NN; **52.4% vs 32.9%**
  native-sequence recovery over Rosetta, and — the headline — it **rescued designs that had
  failed** with physics-based methods, confirmed by X-ray/cryo-EM. The workhorse.
- **RFdiffusion** (Watson et al., *Nature* 2023, Baker lab) — **diffusion over protein
  backbones**, built by fine-tuning RoseTTAFold on denoising. Generates binders, symmetric
  oligomers, **enzyme active-site scaffolds**, metal-binding proteins; "hundreds"
  experimentally characterised; a designed anti-influenza binder matched its design model by
  cryo-EM. Design-by-denoising.
- **Chroma** (Ingraham et al., *Nature* 2023, senior author Grigoryan; Generate Biomedicines)
  — a **programmable** generative model: condition generation on symmetry, substructure,
  shape, semantics, even **natural-language prompts**; design framed as Bayesian inference
  under constraints. **310 proteins** characterised, highly expressed and well-folded.

## Item 2 — Language as the substrate (ESM3)
- **ESM3** (Hayes et al., *Science* 2025, EvolutionaryScale) — a **multimodal generative
  protein language model** that reasons jointly over **sequence, structure and function**,
  so you can "prompt" a protein the way you prompt a chatbot and sample designs that satisfy
  the constraints. Scaled to **98B parameters**.
- **The demo that landed:** **esmGFP**, a new bright green fluorescent protein at **58%
  identity to the nearest known fluorescent protein** — the authors **estimate** it as
  equivalent to **>500 million years** of natural evolution's worth of divergence. A protein
  evolution *could* have made but didn't. **ESM3-open** weights + the esmGFP sequence were
  released publicly.

## Item 3 — From backbone to catalysis + the prove-it / build–test hook
- **Field coming-of-age:** the **2024 Nobel Prize in Chemistry** — half to **David Baker**
  for *computational protein design*, half to **Hassabis & Jumper** for *protein structure
  prediction* (AlphaFold, my gloss). Design and prediction, honoured together.
- **The 2025 frontier — designed *function*:** "Computational design of metallohydrolases"
  (Kim et al., *Nature*, online 3 Dec 2025, Baker lab) uses the **RFdiffusion2** method to
  design de novo **zinc metallohydrolase enzymes** from quantum-chemistry active-site
  geometries — with catalytic activity and crystal structures confirmed in the wet lab. The
  RFdiffusion2 method (bioRxiv preprint, labelled) scaffolds **all 41/41** benchmark active
  sites vs **16/41** for the prior best. Making a *fold* is now table stakes; making a
  *catalyst* is the new bar.
- **Why it matters for the lab.** (1) **Open model serving** — designed-protein models are
  exactly the large models that need FAIR, standard-format, callable serving: the
  [BioImage Model Zoo](/project/bioimage-model-zoo/) / [BioEngine](/project/bioengine/) ethos,
  now for generative structural biology. (2) **The build–test half of design→build→test** —
  a designed sequence is a *prediction* until it's synthesised and assayed; the lab's
  [autonomous experimentation](/project/agent-lens/) (Agent-Lens, REEF) and
  [agentic-science](/project/hypha/) infrastructure are the loop that closes it. (3) The
  same **prove-it discipline** the digest keeps returning to: a design that "looks folded" is
  a hypothesis about matter, validated only when the crystal structure or the enzyme assay
  agrees.

## Lab connections (for "why it matters")
- **bioimage-model-zoo / bioengine** — open, standard-format serving of large AI-for-bio models, now generative-design models too.
- **agent-lens / REEF / hypha (agentic science)** — the design→build→test loop; the wet-lab "test" that turns a design into a result.
- **prove-it (Jul 27) / Aug 1 pathology** — a confident model output is a hypothesis; validate it in the physical world.
- **Aug 3 small-molecule design** — sibling modality (chemistry); today = proteins.
- **Aug 11 dynamics / Aug 12 binding** — the *analysis* side; today is the *synthesis* side (inverse problem).

## De-dup check
Recent digests: Aug 17 pathology FMs; Aug 16 cell-segmentation FMs; Aug 15 single-cell FMs;
Aug 14 AI co-scientist; Aug 13 spatial transcriptomics; Aug 12 co-folding/affinity; Aug 11
protein dynamics; Aug 10 optical pooled screening; Aug 9 genome FMs; Aug 8 smart microscopy;
Aug 7 proteomics; Aug 6 virtual staining; Aug 5 federated; Aug 4 profiling; Aug 3
small-molecule design; Aug 2 virtual cell; Aug 1 prove-it/pathology. **Generative / de novo
protein design has not been a digest theme.** It is the *inverse* of the Aug 11/12 protein
analysis pieces and a different modality from the Aug 3 small-molecule design piece. Clear to run.
