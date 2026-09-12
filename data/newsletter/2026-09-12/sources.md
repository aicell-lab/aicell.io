# Newsletter sources — September 12, 2026

**Theme:** **AI for mRNA / RNA therapeutic design** — deep learning to *design the message
itself*: the 5′UTR that sets translation, the secondary structure that sets stability, the
codons that set expression and immunogenicity, and programmable RNA logic. "Writing the
Messenger." The arc: learn the grammar of the 5′UTR from a massively parallel assay and design
new ones (Optimus 5-Prime / Sample) → generalize prediction to any-length UTRs and interpret
disease variants (Karollus frame-pooling) → make the molecule *last* by designing its structure
("superfolder" mRNAs / Wayment-Steele) → jointly optimize codons **and** structure at genome
scale, with vaccine payoff (LinearDesign) → a 5′UTR **language/foundation model** (UTR-LM) →
RNA that *computes*: deep-learned programmable switches (Angenent-Mari).

**Why now / editorial:** mRNA went from lab curiosity to a delivered medicine in the COVID
vaccines, and the design of the molecule — not just the protein it encodes — is now a machine-
learning problem with public assays and benchmarks. After a week largely about proteins,
small molecules and biomedical knowledge graphs, this is the **RNA-as-medicine** slot of the
central dogma: how AI writes a better messenger. Strong journal verifiability (Nature, Nat
Biotech, Nat Mach Intell, Nat Comms, NAR, PLoS Comp Biol), real translational impact, and a
clean design-loop narrative (predict → design → verify) that mirrors the lab's own build-and-
measure ethos.

**Dedup guard:** Distinct from **Aug 20** (RNA *structure* prediction as a biophysics/base-pair
problem) and **Sep 7** (*reading* the genome — DNA sequence models / variant effect). Today's
object is the **engineered mRNA molecule as a therapeutic**: UTR translation control, hydrolytic
stability, codon/structure co-design, and programmable RNA switches. Also distinct from Aug 21
("The Lab That Runs Itself" — autonomous agents) and the Sep 5–11 protein/small-molecule/
knowledge-graph run. mRNA/UTR design has appeared only incidentally before, never as a theme.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on `monitor`
(--since-hours 24 --min-likes 30) plus topic `search`. ~35th consecutive skip (>five weeks).
Grok-based replacement wired, awaiting xAI credits. `discover` not run (same credit block).

**Verification note:** Europe PMC was returning **HTTP 503 (Service Temporarily Unavailable)**
during this run, so all 6 anchors were verified against **NCBI E-utilities** instead — `esearch`
(DOI→PMID) then `efetch` (`rettype=abstract`, XML), parsing the article title, journal, year and
full `AbstractText` (with section labels). Only abstract-verified verbatim quotes are used below.
DOIs and PMIDs recorded for each.

---

## Framing + the founding move — learn the 5′UTR, then design it

### Sample et al. — Optimus 5-Prime — VERIFIED (NCBI eutils; PMID 31267113)
- Sample PJ, Wang B, Reid DW, Presnyak V, McFadyen IJ, Morris DR, Seelig G. "Human 5′ UTR design
  and variant effect prediction from a massively parallel translation assay." *Nature
  Biotechnology* 37:803–809, 2019. DOI 10.1038/s41587-019-0164-5.
- ABSTRACT-VERIFIED (verbatim): "**we combine polysome profiling of a library of 280,000
  randomized 5′ untranslated regions (UTRs) with deep learning to build a predictive model that
  relates human 5′ UTR sequence to translation.**"; "**we use this same model, coupled with
  genetic algorithms, to engineer new 5′ UTRs that accurately direct specified levels of ribosome
  loading**"; "**the same approach can be extended to chemically modified RNA, an important
  feature for applications in mRNA therapeutics**"; "**We evaluate 35,212 5′ UTRs containing
  human genetic variants and identify 45 single-nucleotide variants (SNVs) associated with human
  diseases that substantially change ribosome loading.**"
- USE: the founding move — a massively parallel assay (280k random UTRs) + deep learning →
  a model that both *predicts* translation and, with genetic algorithms, *designs* UTRs for a
  target ribosome load; explicitly extensible to modified RNA for mRNA therapeutics; and it reads
  disease variants. Predict → design → interpret, all from one assay.

## Section 1 — Generalize prediction, interpret the clinic

### Karollus, Avsec & Gagneur — frame pooling / any-length MRL — VERIFIED (PMID 33970899)
- Karollus A, Avsec Ž, Gagneur J. "Predicting mean ribosome load for 5′UTR of any length using
  deep learning." *PLoS Computational Biology* 17:e1008982, 2021. DOI 10.1371/journal.pcbi.1008982.
- ABSTRACT-VERIFIED (verbatim): "**a model was trained on a massively parallel reporter assay to
  predict mean ribosome load (MRL)**"; "**we introduced frame pooling, a novel neural network
  operation that enabled the development of an MRL prediction model for 5′UTRs of any length**";
  "**Variant interpretation is demonstrated on a 5′UTR variant of the gene HBB associated with
  beta-thalassemia**"; "**our model, released open source, could help pinpoint pathogenic genetic
  variants.**"
- USE: the generalization + prove-it beat — a new neural op ("frame pooling") lifts the fixed-
  length MPRA model to UTRs of *any* length, and the payoff is clinical: interpreting a
  beta-thalassemia HBB variant. Open source. Shows the design model doubles as a variant reader.

## Section 2 — Make the molecule last: design for stability

### Wayment-Steele et al. — "superfolder" mRNAs — VERIFIED (PMID 34520542)
- Wayment-Steele HK, Kim DS, Choe CA, Nicol JJ, Wellington-Oguri R, Watkins AM, Parra Sperberg RA,
  Huang P-S, Participants Eterna, Das R. "Theoretical basis for stabilizing messenger RNA through
  secondary structure design." *Nucleic Acids Research* 49:10604–10617, 2021. DOI
  10.1093/nar/gkab764.
- ABSTRACT-VERIFIED (verbatim): "**RNA hydrolysis presents problems in manufacturing, long-term
  storage, world-wide delivery and in vivo stability of messenger RNA (mRNA)-based vaccines.**";
  "**A general strategy to stabilize mRNA is to redesign RNAs to form double-stranded regions,
  which are protected from in-line cleavage**"; "**Here, we present simple calculations for
  estimating RNA stability against hydrolysis, and a model that links the average unpaired
  probability of an mRNA, or AUP, to its overall hydrolysis rate.**"; "**We test the accuracy of
  a variety of RNA structure prediction packages … and we find these calculations enable design
  of stabilized mRNAs with lower AUP**"; "**We describe two designs of mRNAs coding for a model
  protein and the SARS-CoV-2 spike protein with low AUP, which we term 'superfolder' mRNAs.**";
  "**Increases in in vitro mRNA half-life by at least two-fold appear immediately achievable.**"
- USE: the stability beat — the manufacturing/shelf-life problem of mRNA vaccines is *hydrolysis*,
  and it can be attacked by *designing structure*: minimize the average unpaired probability (AUP)
  to slow cleavage. "Superfolder" mRNAs, ≥2× half-life, tied directly to the spike-protein vaccine.
  Design isn't only about expression level — it's about the molecule surviving to be delivered.

## Section 3 — Co-optimize codons AND structure, at genome scale

### Zhang et al. — LinearDesign — VERIFIED (PMID 37130545)
- Zhang H, Zhang L, Lin A, … Mathews DH, Zhang B, Huang L. "Algorithm for optimized mRNA design
  improves stability and immunogenicity." *Nature* 621:396–403, 2023. DOI
  10.1038/s41586-023-06127-z.
- ABSTRACT-VERIFIED (verbatim): "**the mRNA sequence design problem is exceptionally difficult
  because of the exponentially large search space—for example, there are around 2.4 × 10^632
  candidate mRNA sequences for the SARS-CoV-2 spike protein.**"; "**Here we provide … a
  principled, systematic approach by reformulating this task as a lattice parsing problem, in
  which the lattice represents the entire design space and parsing recursively finds the optimal
  design.**"; "**Our algorithm LinearDesign finds an optimal mRNA design for the spike protein in
  just 11 minutes, and can concurrently optimize stability and codon usage.**"; "**LinearDesign
  substantially improves mRNA half-life and protein expression, and profoundly increases antibody
  titre by up to 128 times in mice compared to the codon-optimization benchmark.**"
- USE: the flagship — a hard combinatorial problem (2.4×10^632 sequences for one protein) solved
  by borrowing *lattice parsing from computational linguistics* to co-optimize codons **and**
  secondary structure in 11 minutes; the wet-lab payoff is enormous (up to **128×** antibody titre
  in mice). AI as an algorithmic breakthrough with a vaccine at the end of it.

## Section 4 — A foundation model for the untranslated region

### Chu et al. — UTR-LM — VERIFIED (PMID 38855263)
- Chu Y, Yu D, Li Y, Huang K, Shen Y, Cong L, Zhang J, Wang M. "A 5′ UTR language model for
  decoding untranslated regions of mRNA and function predictions." *Nature Machine Intelligence*
  6:449–460, 2024. DOI 10.1038/s42256-024-00823-9.
- ABSTRACT-VERIFIED (verbatim): "**Here we introduced a language model for 5′ UTR, which we refer
  to as the UTR-LM.**"; "**The UTR-LM was pretrained on endogenous 5′ UTRs from multiple species
  and was further augmented with supervised information including secondary structure and minimum
  free energy.**"; "**The UTR-LM outperformed the best-known benchmark by up to 5% for predicting
  the mean ribosome loading, and by up to 8% for predicting the translation efficiency and the
  mRNA expression level.**"; "**we designed a library of 211 novel 5′ UTRs with top predicted
  values … The wet-lab validation showed that our top designs achieved a 32.5% increase in
  protein production level relative to well-established 5′ UTRs optimized for therapeutics.**"
- USE: the foundation-model turn — a self-supervised **5′UTR language model** pretrained across
  species and augmented with structure/MFE, beating task-specific benchmarks (+5% MRL, +8% TE and
  expression) and, crucially, *designing* 211 new UTRs that beat a therapeutic-grade baseline by
  **32.5%** in the wet lab. The same pretrain-then-design recipe reshaping the rest of biology,
  aimed at the messenger. (Kexin Huang, a TxGNN author from yesterday's digest, is a coauthor.)

## Section 5 — RNA that computes: programmable switches

### Angenent-Mari et al. — deep learning for RNA switches — VERIFIED (PMID 33028812)
- Angenent-Mari NM, Garruss AS, Soenksen LR, Church G, Collins JJ. "A deep learning approach to
  programmable RNA switches." *Nature Communications* 11:5057, 2020. DOI
  10.1038/s41467-020-18677-1.
- ABSTRACT-VERIFIED (verbatim): "**we investigate Deep Neural Networks (DNN) to predict toehold
  switch function as a canonical riboswitch model in synthetic biology.**"; "**To facilitate DNN
  training, we synthesize and characterize in vivo a dataset of 91,534 toehold switches spanning
  23 viral genomes and 906 human transcription factors.**"; "**DNNs trained on nucleotide
  sequences outperform (R2 = 0.43–0.70) previous state-of-the-art thermodynamic and kinetic models
  (R2 = 0.04–0.15) for toehold switch function prediction.**"; "**we introduce a new
  visualization method, VIS4Map, to successfully identify sequence and structural elements that
  correlate with toehold switch function, enabling model interpretability and providing structural
  insights.**"
- USE: the horizon beat — RNA isn't only a passive template; it can be *programmable logic*. Deep
  nets predict **toehold switch** function far better (R²=0.43–0.70) than thermodynamic/kinetic
  models (R²=0.04–0.15) from a 91,534-switch in-vivo dataset, with interpretable attention maps
  (VIS4Map). Designing the message extends from *how much* protein to *when and whether* — RNA
  diagnostics and smart therapeutics.

## Section 6 — Lab hook + horizon
- The through-line: **the messenger is a designable molecule.** Deep learning now writes the parts
  of an mRNA that the protein sequence doesn't specify — the 5′UTR that tunes translation, the
  structure that resists hydrolysis, the codon/structure choices that set expression and
  immunogenicity, and even programmable switch logic. Predict → design → measure, on public assays.
- The recipe is the lab's recipe: a **massively parallel assay** feeds a model that is then run
  *in reverse* to design new sequences, and the wet lab checks the design (Sample's genetic
  algorithms, UTR-LM's 211-UTR library, LinearDesign's 128× titre). That build-and-measure loop is
  exactly the [self-driving-lab](/post/newsletter-2026-08-21/) ethos.
- Open + benchmarked: Karollus and UTR-LM are open source; the field is measured on shared MPRA
  benchmarks (mean ribosome load, translation efficiency) — the publish-the-model-*and*-the-data
  spirit behind the [BioImage Model Zoo](/project/bioimage-model-zoo/) and
  [BioEngine](/project/bioengine/).
- Horizon / strategy radar: mRNA design is a concrete, high-impact instance of *foundation models
  for biology* (UTR-LM) meeting *sequence design* — a rung toward a [virtual cell](/project/human-cell-simulator/)
  that must model not just what a molecule is but how efficiently it is *made* and how long it
  survives. And it connects to yesterday's [knowledge-graph digest](/post/newsletter-2026-09-11/)
  through a shared author (Kexin Huang) — the same people building the reasoning layer are building
  the design layer.
