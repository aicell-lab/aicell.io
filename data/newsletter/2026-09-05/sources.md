# Newsletter sources — September 5, 2026

**Theme:** **De novo protein design** — generative AI that *invents* new proteins (backbones, sequences,
binders, enzymes) rather than predicting or annotating existing ones. "Designing Life's Missing Parts."
The arc: physics-based proof it's possible (Top7) → invert a structure predictor to dream new proteins
(hallucination) → robustly design the sequence for a backbone (ProteinMPNN) → generate backbones &
function by diffusion (RFdiffusion) → program protein space with constraints/prompts (Chroma) → the
predictor that both enabled and validates it all (AlphaFold2).

**Dedup guard:** Distinct from the recent protein arc — Sep 2 (protein *function* prediction / dark
proteome), Aug 12 (co-folding / complex + affinity *prediction*), Aug 11 (conformational *ensembles*).
Those all predict/annotate proteins that already exist. This is *generative design* — creating proteins
that never existed in nature. Distinct from Aug 20 (RNA design — different molecule). Complements the
structural-biology thread and the lab's open/callable/benchmarked ethos.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on monitor (min-likes 30,
since-hours 24) and search. ~28th consecutive skip (>four weeks). Grok replacement wired, awaiting xAI
credits.

All 6 anchors verified against **raw Europe PMC `abstractText` JSON** (fetched directly via curl — no
summarizer), with DOI/title/author/journal/year confirmed. Only abstract-verified verbatim quotes used.

---

## Framing + proof it's possible

### Top7 (Kuhlman & Baker) — physics-based de novo fold — VERIFIED
- Kuhlman B, Dantas G, Ireton GC, Varani G, Stoddard BL, Baker D. "Design of a novel globular protein
  fold with atomic-level accuracy." *Science* 302:1364–1368, 2003. DOI 10.1126/science.1089427.
- ABSTRACT-VERIFIED (verbatim): "**A major challenge of computational protein design is the creation of
  novel proteins with arbitrarily chosen three-dimensional structures.**"; "**we used a general
  computational strategy that iterates between sequence design and structure prediction to design a
  93-residue alpha/beta protein called Top7 with a novel sequence and topology.**"; "**Top7 was found
  experimentally to be folded and extremely stable, and the x-ray crystal structure of Top7 is similar
  (root mean square deviation equals 1.2 angstroms) to the design model.**"; "**The ability to design a
  new protein fold makes possible the exploration of the large regions of the protein universe not yet
  observed in nature.**"
- USE: the historical anchor — long before deep learning, physics-based design already produced a real,
  stable, never-before-seen fold. Sets up "the protein universe not yet observed in nature."

## Section 1 — Inverting the predictor: hallucination

### Hallucination (Anishchenko et al.) — VERIFIED
- Anishchenko I, Pellock SJ, Chidyausiku TM, … Baker D. "De novo protein design by deep network
  hallucination." *Nature* 600:547–552, 2021. DOI 10.1038/s41586-021-04184-w.
- ABSTRACT-VERIFIED (verbatim): "**we investigate whether the information captured by such networks is
  sufficiently rich to generate new folded proteins with sequences unrelated to those of the naturally
  occurring proteins used in training the models.**"; "**We generate random amino acid sequences … We
  then carry out Monte Carlo sampling in amino acid sequence space, optimizing the contrast (Kullback-
  Leibler divergence) between the inter-residue distance distributions predicted by the network and
  background distributions.**"; "**We obtained synthetic genes encoding 129 of the network-'hallucinated'
  sequences, and expressed and purified the proteins in Escherichia coli; 27 of the proteins yielded
  monodisperse species with circular dichroism spectra consistent with the hallucinated structures.**";
  "**deep networks trained to predict native protein structures from their sequences can be inverted to
  design new proteins, and such networks and methods should contribute alongside traditional physics-
  based models to the de novo design of proteins with new functions.**"
- USE: the deep-learning turn — a structure predictor run *backwards* to dream new proteins; wet-lab
  validated. The "inverted to design" idea.

## Section 2 — Designing the sequence for a backbone

### ProteinMPNN (Dauparas et al.) — VERIFIED
- Dauparas J, Anishchenko I, Bennett N, … Baker D. "Robust deep learning-based protein sequence design
  using ProteinMPNN." *Science* 378:49–56, 2022. DOI 10.1126/science.add2187.
- ABSTRACT-VERIFIED (verbatim): "**Although deep learning has revolutionized protein structure
  prediction, almost all experimentally characterized de novo protein designs have been generated using
  physically based approaches such as Rosetta.**"; "**On native protein backbones, ProteinMPNN has a
  sequence recovery of 52.4% compared with 32.9% for Rosetta.**"; "**The amino acid sequence at different
  positions can be coupled between single or multiple chains, enabling application to a wide range of
  current protein design challenges.**"; "**rescuing previously failed designs, which were made using
  Rosetta or AlphaFold, of protein monomers, cyclic homo-oligomers, tetrahedral nanoparticles, and
  target-binding proteins.**"
- USE: the "given a shape, what sequence folds into it?" step; the 52.4% vs 32.9% recovery number; it
  rescues designs that other methods failed on.

## Section 3 — Generating structure & function directly (diffusion)

### RFdiffusion (Watson et al.) — VERIFIED
- Watson JL, Juergens D, Bennett NR, … Baker D. "De novo design of protein structure and function with
  RFdiffusion." *Nature* 620:1089–1100, 2023. DOI 10.1038/s41586-023-06415-8.
- ABSTRACT-VERIFIED (verbatim): "**a general deep-learning framework for protein design that enables
  solution of a wide range of design challenges, including de novo binder design and design of higher-
  order symmetric architectures, has yet to be described.**"; "**by fine-tuning the RoseTTAFold structure
  prediction network on protein structure denoising tasks, we obtain a generative model of protein
  backbones that achieves outstanding performance on unconditional and topology-constrained protein
  monomer design, protein binder design, symmetric oligomer design, enzyme active site scaffolding and
  symmetric motif scaffolding.**"; "**The accuracy of RFdiffusion is confirmed by the cryogenic electron
  microscopy structure of a designed binder in complex with influenza haemagglutinin that is nearly
  identical to the design model.**"; "**In a manner analogous to networks that produce images from user-
  specified inputs, RFdiffusion enables the design of diverse functional proteins from simple molecular
  specifications.**"
- USE: the diffusion breakthrough (image-generation math applied to backbones); binders, enzymes,
  symmetric assemblies; cryo-EM-confirmed influenza-binder as the proof.

## Section 4 — Programming protein space with constraints

### Chroma (Ingraham et al.) — VERIFIED
- Ingraham JB, Baranov M, Costello Z, … (Generate Biomedicines). "Illuminating protein space with a
  programmable generative model." *Nature* 623:1070–1078, 2023. DOI 10.1038/s41586-023-06728-8.
- ABSTRACT-VERIFIED (verbatim): "**Three billion years of evolution has produced a tremendous diversity
  of protein molecules, but the full potential of proteins is likely to be much greater.**"; "**we
  introduce Chroma, a generative model for proteins and protein complexes that can directly sample novel
  protein structures and sequences, and that can be conditioned to steer the generative process towards
  desired properties and functions.**"; "**Chroma achieves protein design as Bayesian inference under
  external constraints, which can involve symmetries, substructure, shape, semantics and even natural-
  language prompts.**"; "**The experimental characterization of 310 proteins shows that sampling from
  Chroma results in proteins that are highly expressed, fold and have favourable biophysical
  properties.**"
- USE: the "programmable / prompt-conditioned" framing; design-as-Bayesian-inference; natural-language
  prompts for proteins (a nice tie to the agentic/LLM thread); 310 proteins characterized.

## Section 5 — The predictor that enabled & validates it all

### AlphaFold2 (Jumper et al.) — VERIFIED
- Jumper J, Evans R, Pritzel A, … Hassabis D. "Highly accurate protein structure prediction with
  AlphaFold." *Nature* 596:583–589, 2021. DOI 10.1038/s41586-021-03819-2.
- ABSTRACT-VERIFIED (verbatim): "**the structures of around 100,000 unique proteins have been determined,
  but this represents a small fraction of the billions of known protein sequences.**"; "**Here we provide
  the first computational method that can regularly predict protein structures with atomic accuracy even
  in cases in which no similar structure is known.**"; "**We validated an entirely redesigned version of
  our neural network-based model, AlphaFold, in the challenging 14th Critical Assessment of protein
  Structure Prediction (CASP14), demonstrating accuracy competitive with experimental structures.**"
- USE: the prediction↔design duality — the same deep-learning revolution that predicts structure is what
  designers *invert* (hallucination, RFdiffusion) and *validate* against (fold the design in silico,
  check it returns to the target). CASP14 = the prove-it benchmark.

## Section 6 — Lab hook + horizon
- De novo design is the *generative* complement to the recent protein-prediction thread: Sep 2 (function),
  Aug 12 (co-folding/affinity), Aug 11 (ensembles) all read existing proteins; this *writes* new ones.
- Horizon: a virtual cell / Human Cell Simulator (/project/human-cell-simulator/,
  /post/newsletter-2026-08-15/) is not just descriptive — design lets us build custom sensors, binders and
  enzymes to *probe and rewire* cells; agentic design (Chroma's natural-language prompts) ties to the AI-
  agents horizon (/post/newsletter-2026-08-28/, /post/newsletter-2026-08-14/).
- Open, callable, benchmarked: RFdiffusion, ProteinMPNN, Chroma are open source; AlphaFold/CASP14 is the
  public prove-it standard — the same publish-the-model-and-the-test ethos behind the BioImage Model Zoo
  (/project/bioimage-model-zoo/) + BioEngine (/project/bioengine/) and the recurring benchmark discipline
  (/post/newsletter-2026-07-27/). Designs are validated *in silico* by folding them back — prediction and
  design as two directions of one map.
