# Newsletter sources — September 8, 2026

**Theme:** **AI-guided protein engineering / directed evolution** — using machine learning to predict the
*fitness* of protein variants (how a mutation changes activity, stability, binding) and to steer directed
evolution toward improved versions of *existing* proteins. "Climbing the Fitness Landscape." The arc:
the ML-guided directed-evolution paradigm (Yang/Wu/Arnold review) → predict mutation effects unsupervised
from evolutionary sequences (DeepSequence) → learned protein representations for engineering (UniRep) →
data-efficient engineering from a handful of assays (Low-N) → combining evolutionary + assay-labeled data
for fitness (Hsu et al.) → closing the wet-lab loop on real enzymes (Wu/Arnold, GB1 + new-to-nature
carbene chemistry).

**Dedup guard:** Distinct from Sep 5 (de novo protein *design* — inventing new proteins/backbones from
scratch); this is *improving existing* proteins by navigating their mutational landscape. Distinct from
Sep 2 (protein *function annotation* — GO terms / dark proteome), Aug 19 (regulatory-genomics variant-
*effect* prediction on DNA/expression, not protein fitness), Aug 12 (co-folding / binding-affinity
prediction), Aug 11 (conformational ensembles), Aug 15 (single-cell perturbation FMs). The unifying object
here is the **sequence→fitness map** of one protein and how ML lets you climb it with far fewer experiments.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on monitor (min-likes 30,
since-hours 24) and search. ~31st consecutive skip (>five weeks). Grok replacement wired, awaiting xAI
credits.

All 6 anchors verified against **raw Europe PMC `abstractText` JSON** (fetched directly via curl — no
summarizer), with DOI/title/author/journal/year confirmed. Only abstract-verified verbatim quotes used.

---

## Framing — the ML-guided directed-evolution paradigm

### Yang, Wu & Arnold — machine-learning-guided directed evolution — VERIFIED
- Yang KK, Wu Z, Arnold FH. "Machine-learning-guided directed evolution for protein engineering."
  *Nature Methods* 16:687–694, 2019. DOI 10.1038/s41592-019-0496-6.
- ABSTRACT-VERIFIED (verbatim): "**Protein engineering through machine-learning-guided directed evolution
  enables the optimization of protein functions.**"; "**Machine-learning approaches predict how sequence
  maps to function in a data-driven manner without requiring a detailed model of the underlying physics or
  biological pathways.**"; "**Such methods accelerate directed evolution by learning from the properties
  of characterized variants and using that information to select sequences that are likely to exhibit
  improved properties.**"
- USE: the framing — directed evolution (Arnold's Nobel-winning idea) + ML; learn the sequence→function
  map from tested variants, use it to pick better mutants. Sets up "fitness landscape."

## Section 1 — Reading the mutational landscape, unsupervised

### DeepSequence (Riesselman et al.) — VERIFIED
- Riesselman AJ, Ingraham JB, Marks DS. "Deep generative models of genetic variation capture the effects
  of mutations." *Nature Methods* 15:816–822, 2018. DOI 10.1038/s41592-018-0138-4.
- ABSTRACT-VERIFIED (verbatim): "**The functions of proteins and RNAs are defined by the collective
  interactions of many residues, and yet most statistical models of biological sequences consider sites
  nearly independently.**"; "**DeepSequence … predicted the effects of mutations across a variety of deep
  mutational scanning experiments substantially better than existing methods based on the same evolutionary
  data.**"; "**The model, learned in an unsupervised manner solely on the basis of sequence information, is
  grounded with biologically motivated priors, reveals the latent organization of sequence families, and
  can be used to explore new parts of sequence space.**"
- USE: you can predict a mutation's effect from evolutionary sequences *alone*, no labels — a latent
  variable model that captures higher-order residue interactions; benchmarked on deep mutational scanning.

## Section 2 — Learned representations for engineering

### UniRep (Alley et al.) — VERIFIED
- Alley EC, Khimulya G, Biswas S, AlQuraishi M, Church GM. "Unified rational protein engineering with
  sequence-based deep representation learning." *Nature Methods* 16:1315–1322, 2019. DOI
  10.1038/s41592-019-0598-1.
- ABSTRACT-VERIFIED (verbatim): "**we apply deep learning to unlabeled amino-acid sequences to distill the
  fundamental features of a protein into a statistical representation that is semantically rich and
  structurally, evolutionarily and biophysically grounded.**"; "**the simplest models built on top of this
  unified representation (UniRep) are broadly applicable and generalize to unseen regions of sequence
  space.**"; "**Our data-driven approach predicts the stability of natural and de novo designed proteins,
  and the quantitative function of molecularly diverse mutants … UniRep further enables two orders of
  magnitude efficiency improvement in a protein engineering task.**"
- USE: the representation-learning turn — a protein language model whose learned features power downstream
  engineering; two-orders-of-magnitude efficiency. (Precursor to ESM-scale PLMs.)

## Section 3 — Engineering from tiny data

### Low-N (Biswas et al.) — VERIFIED
- Biswas S, Khimulya G, Alley EC, Esvelt KM, Church GM. "Low-N protein engineering with data-efficient
  deep learning." *Nature Methods* 18:389–396, 2021. DOI 10.1038/s41592-021-01100-y.
- ABSTRACT-VERIFIED (verbatim): "**Protein engineering … is limited by the lack of experimental assays
  that are consistent with the design goal and sufficiently high throughput to find rare, enhanced
  variants.**"; "**we introduce a machine learning-guided paradigm that can use as few as 24 functionally
  assayed mutant sequences to build an accurate virtual fitness landscape and screen ten million sequences
  via in silico directed evolution.**"; "**As demonstrated in two dissimilar proteins, GFP from Aequorea
  victoria (avGFP) and E. coli strain TEM-1 β-lactamase, top candidates from a single round are diverse and
  as active as engineered mutants obtained from previous high-throughput efforts.**"
- USE: the payoff on data efficiency — 24 assayed variants → a virtual fitness landscape → screen 10M
  in silico; validated on avGFP and β-lactamase. The "few experiments, big search" story.

## Section 4 — Fusing evolution and experiment

### Hsu et al. — evolutionary + assay-labeled fitness models — VERIFIED
- Hsu C, Nisonoff H, Fannjiang C, Listgarten J. "Learning protein fitness models from evolutionary and
  assay-labeled data." *Nature Biotechnology* 40:1114–1122, 2022. DOI 10.1038/s41587-021-01146-5.
- ABSTRACT-VERIFIED (verbatim): "**Machine learning-based models of protein fitness typically learn from
  either unlabeled, evolutionarily related sequences or variant sequences with experimentally measured
  labels.**"; "**we propose a simple combination approach that is competitive with, and on average
  outperforms more sophisticated methods. Our approach uses ridge regression on site-specific amino acid
  features combined with one probability density feature from modeling the evolutionary data.**"; "**our
  analysis highlights the importance of systematic evaluations and sufficient baselines.**"
- USE: the sober methods lesson — a *simple* model (ridge regression + one evolutionary feature) beats
  fancier ones; and the prove-it discipline (systematic evaluation, strong baselines) the digest admires.

## Section 5 — Closing the loop at the bench

### Wu, Kan, Arnold et al. — ML-assisted combinatorial directed evolution — VERIFIED
- Wu Z, Kan SBJ, Lewis RD, Wittmann BJ, Arnold FH. "Machine learning-assisted directed protein evolution
  with combinatorial libraries." *PNAS* 116:8852–8858, 2019. DOI 10.1073/pnas.1901979116.
- ABSTRACT-VERIFIED (verbatim): "**Combinatorial sequence space can be quite expensive to sample
  experimentally, but machine-learning models trained on tested variants provide a fast method for testing
  sequence space computationally.**"; "**We validated this approach on a large published empirical fitness
  landscape for human GB1 binding protein, demonstrating that machine learning-guided directed evolution
  finds variants with higher fitness than those found by other directed evolution approaches.**"; "**fixed
  seven mutations in two rounds of evolution to identify variants for selective catalysis with 93% and 79%
  ee (enantiomeric excess).**"
- USE: the real wet-lab loop — ML picks combinatorial libraries; GB1 benchmark; then engineers a
  new-to-nature carbene Si–H insertion enzyme with high stereoselectivity. Design→build→test→learn made real.

## Section 6 — Lab hook + horizon
- This is the *engineer/optimize* complement to Sep 5's *design from scratch*: navigate the mutational
  landscape of an existing protein to improve activity, stability or selectivity. Reading (Sep 2 function),
  writing (Sep 5 design), and *evolving* (today) are three verbs on the same molecule.
- The design→build→test→learn loop these methods run is exactly what a
  [self-driving lab](/post/newsletter-2026-08-21/) automates and what an
  [AI co-scientist](/post/newsletter-2026-08-14/) orchestrates — ML proposes variants, the bench tests a
  few, the model updates. Low-N's "24 assays → 10M in silico" is the automated-discovery dream in miniature.
- Fitness landscapes are also a piece of the [virtual cell](/project/human-cell-simulator/): to simulate or
  re-engineer a pathway you need to predict how each mutation changes a protein's behavior.
- Open, benchmarked ethos: DeepSequence and UniRep are open source; deep mutational scanning datasets and
  the GB1 landscape are the public yardsticks — the same publish-the-model-*and*-the-test spirit behind the
  BioImage Model Zoo (/project/bioimage-model-zoo/) + BioEngine (/project/bioengine/) and the recurring
  benchmark discipline (/post/newsletter-2026-07-27/).
