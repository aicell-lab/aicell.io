# Newsletter sources — September 15, 2026

**Theme:** **Deep-learning image registration / alignment** — models that learn to *line images up*,
predicting the spatial transformation (a deformation field) that maps one image onto another, in one
fast forward pass instead of a slow per-pair optimization. "The Art of Alignment." The arc: learn
registration as a function that outputs a deformation field (VoxelMorph) → train it *unsupervised*
from image similarity alone, no ground-truth deformations (DLIR) → add cycle-consistency to preserve
topology (CycleMorph) → swap the CNN for a transformer's long-range receptive field, with
diffeomorphic + Bayesian-uncertainty variants (TransMorph) → make it contrast/modality-agnostic by
training only on synthesized shapes (SynthMorph) → carry the same idea into spatial omics, aligning
and stacking tissue slices with optimal transport (PASTE).

**Why now / editorial:** a deliberate pivot back to the lab's **imaging** core after a 15-day
molecular/omics streak (Sep 1 spatial proteomics was the last imaging-forward digest; Sep 2–14 ran
protein/genome/omics). Registration is the quiet, load-bearing step *underneath* most of the lab's
imaging: multiplexed tissue imaging (the 40-color CODEX/CyCIF of [Sep 1](/post/newsletter-2026-09-01/))
must be aligned cycle-to-cycle; live-cell movies must be drift-corrected; serial sections must be
stacked into 3D; and spatial-omics slices must be integrated into an atlas. It's also a clean AI story
— reframing a classical optimization problem as a learned function — and it ends on **optimal
transport** (PASTE), the recurring lab primitive we flagged in the [cell-cell-communication digest](/post/newsletter-2026-09-13/).

**Dedup guard:** Never a newsletter theme. Distinct from **Aug 22** (image *restoration* /
super-resolution — recovering signal, not spatial correspondence), **Aug 16** (*segmentation* FMs —
delineating objects, not aligning frames), **Aug 25** (cell *tracking* — temporal identity, not a
dense deformation field), and **Sep 1 / Aug 13** (spatial transcriptomics — *measuring* space; today
is *aligning* it). PASTE is the one spatial-omics anchor and it appears here specifically as an
*alignment/integration* method, a role it did not play in the Aug 13 spatial digest.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on `monitor`
(--since-hours 24 --min-likes 30). ~38th consecutive skip (>five weeks). **Surrogate run:** hypha-search
sweep (`source=hackernews`, horizon queries) — service healthy (`failed: []`). Surfaced two horizon
signals worth radar-noting but not breaking/lab-specific: *"GenBio launches a virtual biological
cell"* and *"CZI launches RBio: reasoning model trained on virtual-cell simulations."* Nothing
actionable for today; both are virtual-cell items to watch. `discover` blocked by the same credit issue.

**Verification:** all 6 anchors verified via **NCBI E-utilities** (esearch DOI→PMID, efetch abstract
XML), full `AbstractText` captured; DOI + PMID + journal + year recorded. Only abstract-verified
verbatim quotes used below. (Anchors 1–5 are the DL-registration methods literature — IEEE TMI /
Medical Image Analysis; anchor 6 is Nature Methods.)

---

## Framing + the founding move — registration as a learned function

### Balakrishnan et al. — VoxelMorph — VERIFIED (PMID 30716034)
- Balakrishnan G, Zhao A, Sabuncu MR, Guttag J, Dalca AV. "VoxelMorph: A Learning Framework for
  Deformable Medical Image Registration." *IEEE Transactions on Medical Imaging* 38(8):1788–1800,
  2019. DOI 10.1109/TMI.2019.2897538.
- ABSTRACT-VERIFIED (verbatim): "**We present VoxelMorph, a fast learning-based framework for
  deformable, pairwise medical image registration.**"; "**Traditional registration methods optimize
  an objective function for each pair of images, which can be time-consuming for large datasets or
  rich deformation models.**"; "**we formulate registration as a function that maps an input image
  pair to a deformation field that aligns these images. We parameterize the function via a
  convolutional neural network (CNN), and optimize the parameters of the neural network on a set of
  images.**"; "**Given a new pair of scans, VoxelMorph rapidly computes a deformation field by
  directly evaluating the function.**"; "**the unsupervised model's accuracy is comparable to
  state-of-the-art methods, while operating orders of magnitude faster.**"
- USE: the founding move — stop re-optimizing for every image pair; *learn* a function (a CNN) that
  emits the deformation field in one forward pass. Unsupervised via image-matching loss, optionally
  aided by segmentations, and "orders of magnitude faster." Sets up the whole theme: registration as
  amortized inference.

## Section 1 — Unsupervised, no ground-truth deformations

### de Vos et al. — DLIR — VERIFIED (PMID 30579222)
- de Vos BD, Berendsen FF, Viergever MA, Sokooti H, Staring M, Išgum I. "A deep learning framework
  for unsupervised affine and deformable image registration." *Medical Image Analysis* 52:128–143,
  2019. DOI 10.1016/j.media.2018.11.010.
- ABSTRACT-VERIFIED (verbatim): "**Image registration, the process of aligning two or more images,
  is the core technique of many (semi-)automatic medical image analysis tasks.**"; "**Thus far
  training of ConvNets for registration was supervised using predefined example registrations.
  However, obtaining example registrations is not trivial.**"; "**we propose the Deep Learning Image
  Registration (DLIR) framework for unsupervised affine and deformable image registration.**"; "**In
  the DLIR framework ConvNets are trained for image registration by exploiting image similarity
  analogous to conventional intensity-based image registration.**"; "**By stacking multiple of these
  ConvNets into a larger architecture, we are able to perform coarse-to-fine image registration.**"
- USE: the "where does the training signal come from" beat — you can't hand-label deformation fields,
  so DLIR trains purely on *image similarity*, exactly like classical intensity-based registration,
  and stacks networks for coarse-to-fine affine+deformable alignment. Names precisely why supervised
  registration is impractical and how self-supervision fixes it.

## Section 2 — Preserving topology with cycle-consistency

### Kim et al. — CycleMorph — VERIFIED (PMID 33827038)
- Kim B, Kim DH, Park SH, Kim J, Lee JG, Ye JC. "CycleMorph: Cycle consistent unsupervised deformable
  image registration." *Medical Image Analysis* 71:102036, 2021. DOI 10.1016/j.media.2021.102036.
- ABSTRACT-VERIFIED (verbatim): "**the existing deep learning methods still have limitations in the
  preservation of original topology during the deformation with registration vector fields.**";
  "**we present a cycle-consistent deformable image registration, dubbed CycleMorph.**"; "**The cycle
  consistency enhances image registration performance by providing an implicit regularization to
  preserve topology during the deformation.**"; "**The proposed method is so flexible that it can be
  applied for both 2D and 3D registration problems for various applications, and can be easily
  extended to multi-scale implementation to deal with the memory issues in large volume
  registration.**"
- USE: the "don't tear the tissue" beat — a raw deformation field can fold or rip anatomy; enforcing
  that mapping A→B then B→A returns you home (cycle consistency) implicitly regularizes toward
  *topology-preserving* deformations. A physically-meaningful constraint, 2D/3D, multi-scale for big
  volumes.

## Section 3 — Transformers, diffeomorphisms, and calibrated uncertainty

### Chen et al. — TransMorph — VERIFIED (PMID 36156420)
- Chen J, Frey EC, He Y, Segars WP, Li Y, Du Y. "TransMorph: Transformer for unsupervised medical
  image registration." *Medical Image Analysis* 82:102615, 2022. DOI 10.1016/j.media.2022.102615.
- ABSTRACT-VERIFIED (verbatim): "**the performances of ConvNets may be limited by a lack of explicit
  consideration of the long-range spatial relationships in an image.**"; "**Transformers may be a
  strong candidate for image registration because their substantially larger receptive field enables
  a more precise comprehension of the spatial correspondence between moving and fixed images.**";
  "**we present TransMorph, a hybrid Transformer-ConvNet model for volumetric medical image
  registration.**"; "**the diffeomorphic variants ensure the topology-preserving deformations, and
  the Bayesian variant produces a well-calibrated registration uncertainty estimate.**"; "**the
  proposed Transformer-based model leads to a substantial performance improvement over the baseline
  methods.**"
- USE: the architecture beat — alignment is fundamentally about *long-range* correspondence between
  moving and fixed images, exactly where a transformer's wide receptive field beats a CNN's local
  one. Plus two extras the lab cares about: diffeomorphic variants (guaranteed topology preservation)
  and a Bayesian variant that reports *how confident* the alignment is — uncertainty you can act on.

## Section 4 — Registration without ever seeing a real image

### Hoffmann et al. — SynthMorph — VERIFIED (PMID 34587005)
- Hoffmann M, Billot B, Greve DN, Iglesias JE, Fischl B, Dalca AV. "SynthMorph: Learning
  Contrast-Invariant Registration Without Acquired Images." *IEEE Transactions on Medical Imaging*
  41(3):543–558, 2022. DOI 10.1109/TMI.2021.3116879.
- ABSTRACT-VERIFIED (verbatim): "**We introduce a strategy for learning image registration without
  acquired imaging data, producing powerful networks agnostic to contrast introduced by magnetic
  resonance imaging (MRI).**"; "**Learning-based techniques are fast at test time but limited to
  registering images with contrasts and geometric content similar to those seen during training.**";
  "**We propose to remove this dependency on training data by leveraging a generative strategy for
  diverse synthetic label maps and images that exposes networks to a wide range of variability,
  forcing them to learn more invariant features.**"; "**training on arbitrary shapes synthesized from
  noise distributions results in competitive performance, removing the dependency on acquired data of
  any kind.**"
- USE: the generalization beat — the Achilles' heel of learned registration is that it doesn't
  transfer across imaging contrasts/modalities. SynthMorph trains *only on synthesized* label maps
  and images (even shapes from noise), forcing contrast-*invariant* features — one model that aligns
  arbitrary contrasts it never saw. A striking data-free training idea that echoes the lab's interest
  in synthetic-data and simulation-driven learning.

## Section 5 — The lab tie-in: aligning space itself

### Zeira et al. — PASTE — VERIFIED (PMID 35577957)
- Zeira R, Land M, Strzalkowski A, Raphael BJ. "Alignment and integration of spatial transcriptomics
  data." *Nature Methods* 19:567–575, 2022. DOI 10.1038/s41592-022-01459-6.
- ABSTRACT-VERIFIED (verbatim): "**Spatial transcriptomics (ST) measures mRNA expression across
  thousands of spots from a tissue slice while recording the two-dimensional (2D) coordinates of each
  spot.**"; "**We introduce probabilistic alignment of ST experiments (PASTE), a method to align and
  integrate ST data from multiple adjacent tissue slices.**"; "**PASTE computes pairwise alignments
  of slices using an optimal transport formulation that models both transcriptional similarity and
  physical distances between spots.**"; "**PASTE further combines pairwise alignments to construct a
  stacked 3D alignment of a tissue.**"; "**the PASTE integrated slice improves the identification of
  cell types and differentially expressed genes.**"
- USE: the payoff / lab hook — the same alignment problem, now in *spatial omics*: stack adjacent
  tissue slices into a 3D whole and integrate them into one consensus map. And it's built on **optimal
  transport** (transcriptional similarity + physical distance), the recurring primitive from the
  [cell-cell-communication digest](/post/newsletter-2026-09-13/). Alignment is what turns a pile of
  2D slices into a 3D atlas — a direct rung toward the virtual cell.

## Section 6 — Lab hook + horizon
- The through-line: **before you can compare, track, or integrate images, you have to line them up —
  and AI turned that slow, per-pair optimization into a fast learned function.** The methodological
  arc mirrors the lab's instincts: reframe an optimization as amortized inference (VoxelMorph),
  supervise it with the data's own structure (DLIR), constrain it with physically-meaningful
  regularizers (CycleMorph's topology), upgrade the architecture for long-range correspondence
  (TransMorph), remove the data dependency with synthesis (SynthMorph), and carry it into new
  modalities (PASTE).
- Ties to lab interests: registration is the hidden prerequisite of the
  [multiplexed tissue imaging](/post/newsletter-2026-09-01/) and spatial-omics threads (cycles must
  align; slices must stack), and of the [REEF imaging farm](/project/reef-imaging-farm/) and
  [Agent-Lens](/project/agent-lens/) pipelines (live-cell drift correction, multi-position stitching).
  Uncertainty-aware registration (TransMorph's Bayesian variant) is exactly the kind of
  *confidence-reporting* an autonomous microscope needs to decide when to re-image.
- Optimal-transport thread: PASTE's OT formulation is the same primitive behind SpaOTsc/COMMOT
  ([Sep 13](/post/newsletter-2026-09-13/)) — worth tracking as a unifying tool across the lab's
  single-cell + spatial + imaging work.
- Open + benchmarked ethos: VoxelMorph, TransMorph, SynthMorph and PASTE are all open-source with
  public code — the shared-resource spirit behind the [BioImage Model Zoo](/project/bioimage-model-zoo/)
  and [BioEngine](/project/bioengine/).
- Horizon / strategy radar: building a [virtual cell](/project/human-cell-simulator/) from imaging
  means fusing many partial views — timepoints, channels, sections, modalities — into one coherent,
  registered whole. Alignment is the connective tissue of that data engine. (Radar note from the
  surrogate sweep: GenBio's "virtual biological cell" and CZI's RBio reasoning-on-virtual-cell-sims
  are two more entrants in the virtual-cell race to watch.)
