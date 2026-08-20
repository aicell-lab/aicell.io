# Newsletter sources — 2026-08-20 (compiled UTC 2026-08-20T20:20Z)

Theme: **AI and RNA — the harder fold, and the messenger we can already write.**
After a run on proteins (design, dynamics, folding) and DNA (regulatory genome), RNA
is the untouched pillar. Two honest halves: **structure prediction**, where RNA is
protein folding's *harder, data-scarce sibling* — AlphaFold3 extended structure
prediction to nucleic-acid complexes, RhoFold+ built an RNA-specific language-model
predictor, yet the CASP15 community verdict is blunt: *"the prediction of RNA
three-dimensional structures remains an unsolved problem,"* and deep-learning methods
there were **significantly worse** than the top non-deep-learning groups; and **design**,
where the impact is already immense — LinearDesign optimizes an mRNA vaccine sequence in
minutes and lifted antibody titres up to 128× in mice, RNA language models (RiNALMo) and
5′UTR models (Sample & Seelig) learn to read and write translation. Lab hook: RNA is a
core module of any [virtual cell](/post/newsletter-2026-08-15/); the bottleneck is
**data scarcity**, which is exactly why open, shared, standard-format models and data
matter — and the prove-it discipline is baked into the field's own CASP scorecard.

## Provenance / method
- Web research (WebSearch + WebFetch), each anchor cross-checked by two independent
  research agents against **Crossref**, **PubMed / Europe PMC**, and **Semantic Scholar**
  (abstracts pulled from Crossref JATS / Europe PMC core records; publisher pages paywalled).
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  returns **HTTP 402 Insufficient credits** (getxapi out of credits ~8 weeks; **11th
  straight skipped sweep**). The Grok `x_search` replacement is wired but the xAI team
  account has **no credits yet** (403). Flagged to Wei.

## Anchors (all verified — venue / DOI / byline / status)
- **AlphaFold3** — Abramson J (first), … **Hassabis D & Jumper JM (senior; Jumper last/corr.)**,
  "Accurate structure prediction of biomolecular interactions with AlphaFold 3," ***Nature*
  630:493–500, published 8 May 2024**, DOI 10.1038/s41586-024-07487-w (PMID 38718835).
  **Peer-reviewed.** Google DeepMind + Isomorphic Labs.
- **RhoFold+** — Shen T (first), … **Li Y (senior/corr., CUHK)** (senior-author tail also
  incl. Peng Yin, James J. Collins), "Accurate RNA 3D structure prediction using a language
  model-based deep learning approach," ***Nature Methods* 21:2287–2298, 21 Nov 2024**,
  DOI 10.1038/s41592-024-02487-0 (PMID 39572716). **Peer-reviewed** (preprint arXiv:2207.01586,
  "E2Efold-3D"). Affiliations CUHK / Zelixir Biotech / SIAT / ASU Biodesign.
- **CASP15 RNA assessment (honest frontier)** — Das R (first), … **Westhof E (senior/last)**
  (incl. Kretsch, Simpkin, Rigden, Miao), "Assessment of three-dimensional RNA structure
  prediction in CASP15," ***Proteins: Struct. Funct. Bioinform.* 91:1747–1770, 24 Oct 2023**,
  DOI 10.1002/prot.26602 (PMID 37876231). **Peer-reviewed** (bioRxiv 10.1101/2023.04.25.538330).
- **LinearDesign** — Zhang H (first), … **Huang L (senior; conceived & directed)** (co-corr.
  Li H, Mathews DH, Zhang Y, Huang L), "Algorithm for optimized mRNA design improves stability
  and immunogenicity," ***Nature* 621:396–403, published 2 May 2023**, DOI
  10.1038/s41586-023-06127-z (PMID 37130545). **Peer-reviewed.** Baidu Research USA + Oregon
  State + StemiRNA Therapeutics + U. Rochester.
- **RiNALMo (RNA foundation model)** — Penić RJ (first), … **Šikić M (senior/last)**,
  "RiNALMo: general-purpose RNA language models can generalize well on structure prediction
  tasks," ***Nature Communications* 16:5671, published 1 Jul 2025**, DOI
  10.1038/s41467-025-60872-5 (PMID 40593636). **Peer-reviewed.** (Note: RNA-FM, Chen et al.,
  bioRxiv 10.1101/2022.08.06.503062, remains a **preprint** → used RiNALMo as the peer-reviewed
  FM anchor.)
- **5′UTR deep learning** — Sample PJ (first), … **Seelig G (senior/last)**, "Human 5′ UTR
  design and variant effect prediction from a massively parallel translation assay," ***Nature
  Biotechnology* 37:803–809, 2019**, DOI 10.1038/s41587-019-0164-5 (PMID 31267113). **Peer-reviewed.**

## Verification discipline (numbers stated ONLY where character-verified)
- **AlphaFold3:** abstract's comparative wording is **qualitative only** — "far greater accuracy
  for protein–ligand interactions … **much higher accuracy for protein–nucleic acid interactions
  compared with nucleic-acid-specific predictors** … substantially higher antibody–antigen
  prediction accuracy." **No numeric figures in the abstract**, and the abstract says "nucleic
  acids" / "protein–nucleic acid," it **does NOT use the word "RNA"** or give an RNA-specific
  number. → Frame AF3 as extending structure prediction to **nucleic-acid (incl. RNA) complexes**
  with "much higher accuracy for protein–nucleic-acid interactions"; DO NOT invent an AF3 RNA
  accuracy number, DO NOT claim the abstract singles out RNA.
- **RhoFold+:** RNA language-model predictor of **single-chain RNA** 3D structure; RNA LM
  "**pretrained on ~23.7 million RNA sequences**" (abstract-verified; the exact 23,735,169 and the
  name "RNA-FM" are **body-only** → quote "~23.7 million"). Abstract: "superiority of RhoFold+ over
  existing methods, **including human expert groups**" on RNA-Puzzles and CASP15 natural RNA
  targets; validated by cross-family / cross-type / time-censored benchmarks. **No RMSD/TM-score %
  in the abstract** → no accuracy number quoted.
- **CASP15 RNA (honest frontier — the spine):** quote VERBATIM — "**The prediction of RNA
  three-dimensional structures remains an unsolved problem.**" and "**predictions from deep learning
  approaches were significantly worse than these top ranked groups, which did not use deep
  learning.**" (top groups AIchemy_RNA2, Chen, RNAPolis/GeneSilico). "**42 predictor groups / 12
  RNA-containing targets**" also abstract-verified if needed. This is the honest-frontier anchor —
  as of CASP15 (2023), DL had NOT beaten expert/physics methods for RNA. Attribute to the
  assessment, not to me.
- **LinearDesign:** abstract-verified — "**~2.4 × 10^632 candidate mRNA sequences** for the
  SARS-CoV-2 spike protein"; finds an optimal design "**in just 11 minutes**"; "**concurrently
  optimize stability and codon usage**"; "profoundly increases antibody titre **by up to 128 times**
  in mice compared to the codon-optimization benchmark" (COVID-19 + varicella-zoster mRNA vaccines).
  Half-life / protein-expression fold-numbers are **body-only** → NOT quoted. It is a **4-institution
  collaboration** — do NOT attribute to "Baidu alone."
- **RiNALMo:** abstract-verified — "**the largest RNA language model to date, with 650M parameters
  pre-trained on 36M non-coding RNA sequences**"; "state-of-the-art results on several downstream
  tasks" and generalizes secondary-structure prediction to "**unseen RNA families**" (qualitative;
  no benchmark % in abstract).
- **Sample & Seelig 5′UTR:** abstract-verified — a library of "**280,000 randomized 5′ UTRs**" +
  deep learning; tested "**35,212** truncated human 5′ UTRs and **3,577** naturally occurring
  variants"; found "**45 single-nucleotide variants** associated with human diseases that
  substantially change ribosome loading"; extends to chemically modified RNA for mRNA therapeutics.
- **Data-scarcity framing:** it is well-established (and reinforced by CASP15 + AF3-on-RNA reviews,
  e.g. PMC11804252 / a *Structure* review) that RNA structure prediction lags protein prediction
  chiefly because there are **far fewer experimental RNA structures** to train on — safe to state
  qualitatively ("far fewer experimental RNA structures to learn from"), NO fabricated count.
- **2025–26 note (do NOT over-cite):** DRfold2 (*PLOS Biology* 2026, DOI 10.1371/journal.pbio.3003659)
  is peer-reviewed but its numbers are **not abstract-verified here** → mention only qualitatively or
  omit. NuFold / "LM-augmented AF3" peer-review status **UNVERIFIED** → do not cite.
- **No fabricated numbers anywhere.** "RNA central to medicine (mRNA vaccines, RNA-targeted drugs)"
  is a safe paraphrase grounded in the LinearDesign + RiNALMo abstracts; do NOT assert a specific
  count of FDA-approved RNA drugs (unverified).

## De-dup / variety (important)
**RNA — 3D structure prediction + therapeutic/mRNA design — has NOT been a digest theme.** A fresh
biomolecule after the protein + DNA run:
- **Aug 18 protein design / Aug 11 dynamics / Aug 12 co-folding** = **proteins**. Today = **RNA**, a
  different biomolecule with a *different and harder* story: where AlphaFold triumphed for proteins,
  the field's own CASP15 verdict is that RNA structure prediction is "**unsolved**" and DL *lagged* —
  the deliberate counterpoint to the Aug 18 protein-design triumph.
- **Aug 19 regulatory genome / Aug 9 genome LMs** = **DNA** sequence→function (expression, splicing,
  variants *from DNA*). Today = **RNA** 3D structure and mRNA/therapeutic design — a different
  molecule and a different problem (fold + design, not DNA regulatory prediction). (Aug 19 touched
  splicing *prediction from DNA*; today's RNA work is structure/design, not splicing.)
- **Aug 3 small-molecule design** = chemistry. Today = RNA macromolecule structure + design.
- **Aug 2 / Aug 15 virtual cell** = today supplies the **RNA module** (structure, translation,
  RNA therapeutics) a virtual cell needs; linked, not repeated.
Clear separation. Clear to run.

## Item 1 — The harder fold (AlphaFold3, RhoFold+, and the CASP15 verdict)
- **The problem:** predicting a molecule's 3D shape from sequence. For proteins, AlphaFold solved it;
  for **RNA**, it's harder — RNA is floppier, its folds are stabilized by subtle non-canonical pairs,
  and there are **far fewer experimental RNA structures** to learn from.
- **AlphaFold3** (Abramson et al., *Nature* 2024; senior Hassabis/Jumper) — extended structure
  prediction beyond proteins to **nucleic-acid complexes, ligands, ions and modified residues**, with
  the abstract claiming "**much higher accuracy for protein–nucleic-acid interactions**" than
  nucleic-acid-specific predictors (qualitative; no RNA-specific number).
- **RhoFold+** (Shen et al., *Nature Methods* 2024; senior Yu Li) — an **RNA language-model-based**
  predictor of single-chain RNA 3D structure, its LM **pretrained on ~23.7 million RNA sequences**;
  reported to surpass existing methods "**including human expert groups**" on RNA-Puzzles and CASP15
  natural targets, and to generalize across families.
- **The honest frontier** (Das et al., CASP15 assessment, *Proteins* 2023; senior Westhof): as of the
  last community bake-off, "**the prediction of RNA three-dimensional structures remains an unsolved
  problem**," and — strikingly — "**predictions from deep learning approaches were significantly worse
  than these top ranked groups, which did not use deep learning.**" RNA is where AI's structure story
  is *not yet* won.

## Item 2 — The messenger we can already write (LinearDesign, RiNALMo, 5′UTR)
- **Design outruns prediction.** Even without perfect structure prediction, AI is already reshaping how
  we *design* RNA — and that is where the human impact is immediate (mRNA vaccines, RNA-based drugs).
- **LinearDesign** (Zhang et al., *Nature* 2023; project lead Huang; 4-institution collab) — jointly
  optimizes **codon usage and mRNA secondary-structure stability**; out of "**~2.4 × 10^632** candidate
  mRNA sequences" for the SARS-CoV-2 spike, it finds an optimal design "**in just 11 minutes**," and the
  designs raised **antibody titres up to 128× in mice** vs the codon-optimization benchmark (COVID-19 +
  varicella-zoster vaccines).
- **Reading and writing translation:** **Sample & Seelig** (*Nature Biotechnology* 2019) trained deep
  learning on "**280,000 randomized 5′ UTRs**" to predict and design how an mRNA is translated (and
  flagged **45 disease variants** that shift ribosome loading); **RiNALMo** (Penić et al., *Nature
  Communications* 2025; senior Šikić) is a **650M-parameter RNA language model** pretrained on **36M
  ncRNA sequences** that generalizes to **unseen RNA families** — an open, general-purpose RNA foundation
  model.

## Item 3 — Why it matters for the lab (the RNA module, data scarcity, prove-it)
- **The virtual cell needs an RNA module.** RNA sits at the center of the cell — transcription, splicing,
  translation, regulation, structure — so any [virtual cell](/post/newsletter-2026-08-15/) or
  [foundation-model-for-biology](/project/bioimage-model-zoo/) program needs to model RNA structure,
  translation and design, not just proteins and DNA.
- **Data scarcity is the bottleneck — and the argument for openness.** RNA prediction lags protein
  prediction largely because there are **far fewer experimental RNA structures** to train on. That makes
  **open, shared, standard-format data and callable models** — the [BioEngine](/project/bioengine/) /
  Model Zoo ethos — not a nicety but the path forward for RNA.
- **The prove-it discipline is built into the field's own scorecard.** CASP15 says RNA structure
  prediction is "unsolved" and that deep learning hasn't yet beaten expert methods — a rare, refreshing
  case where the frontier is honest about itself. A predicted RNA fold, like a designed mRNA, is a
  [hypothesis](/post/newsletter-2026-07-27/) until an experiment agrees. Design already saves lives;
  prediction still has to earn its place.

## Lab connections (for "why it matters")
- **virtual cell (Aug 2 / Aug 15)** — RNA (structure, translation, regulation) is a core module.
- **bioimage-model-zoo / bioengine** — open, callable, standard-format models + data; the answer to RNA's data scarcity.
- **Aug 18 protein design** — deliberate counterpoint: proteins solved, RNA "unsolved" (CASP15).
- **Aug 19 regulatory genome / Aug 9 genome LMs** — DNA-side siblings; today = the RNA molecule itself.
- **prove-it (Jul 27)** — a predicted fold / designed mRNA is a hypothesis until validated.

## De-dup check
Recent digests: Aug 19 regulatory genome; Aug 18 protein design; Aug 17 pathology FMs; Aug 16
segmentation FMs; Aug 15 single-cell FMs; Aug 14 AI co-scientist; Aug 13 spatial transcriptomics; Aug 12
co-folding; Aug 11 protein dynamics; Aug 10 optical pooled screening; Aug 9 genome LMs; Aug 8 smart
microscopy; Aug 7 proteomics; Aug 6 virtual staining; Aug 5 federated; Aug 4 profiling; Aug 3
small-molecule design; Aug 2 virtual cell; Aug 1 prove-it/pathology. **RNA (3D structure prediction +
therapeutic/mRNA design) has not been a digest theme** — a fresh biomolecule, and a deliberately
different (harder, unsolved, data-scarce) story from the protein pieces. Clear to run.
