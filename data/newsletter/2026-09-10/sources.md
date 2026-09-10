# Newsletter sources — September 10, 2026

**Theme:** **AI for antibiotic / antimicrobial discovery** — machine learning to find, design, and mine new
antibacterials against the resistance crisis: screening existing libraries for antibacterial activity,
targeting priority pathogens, opening the black box for new chemical classes, generatively designing
antimicrobial peptides, and mining the microbiome's own arsenal at planetary scale. "An Antibiotic in the
Machine." The arc: DL screening of chemical libraries (Stokes/halicin) → targeting one hard Gram-negative
pathogen (Liu/abaucin) → explainable GNNs → a new structural class (Wong) → deep generative + MD design
(Das) → mining gut-microbiome AMPs with NLP models (Ma) → the global-microbiome AMP catalog, AMPSphere
(Santos-Júnior).

**Dedup guard:** Distinct from Aug 3 ("The Third Molecule" — *generative de novo design* of small-molecule
drugs broadly). Today is specifically **antibacterial discovery**: ML *screening/prediction* of
antibacterial activity (halicin, abaucin, Wong) plus AMP generation/mining — a topic (antibiotics /
antimicrobial peptides / microbiome-derived drugs) that has **never** been a newsletter theme, and
halicin/abaucin/AMPSphere have never been mentioned. Adjacent but separate from Sep 5 (protein *design*),
Sep 8 (protein *engineering*), Sep 9 (ML *force fields*). One anchor (Das) uses generative models + MD, tying
lightly to Sep 9 without repeating it.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on `monitor` (min-likes 30,
since-hours 24). ~33rd consecutive skip (>five weeks). Grok replacement wired, awaiting xAI credits.

All 6 anchors verified against **raw Europe PMC `abstractText` JSON** (fetched directly via curl — no
summarizer), with DOI/title/author/journal/year confirmed. Only abstract-verified verbatim quotes used.

---

## Framing + the landmark — screening libraries with deep learning

### Stokes et al. — halicin, a deep-learning antibiotic — VERIFIED
- Stokes JM, Yang K, Swanson K, … Collins JJ. "A Deep Learning Approach to Antibiotic Discovery." *Cell*
  180:688–702, 2020. DOI 10.1016/j.cell.2020.01.021.
- ABSTRACT-VERIFIED (verbatim): "**Due to the rapid emergence of antibiotic-resistant bacteria, there is a
  growing need to discover new antibiotics. To address this challenge, we trained a deep neural network
  capable of predicting molecules with antibacterial activity.**"; "**we discovered a molecule from the Drug
  Repurposing Hub—halicin—that is structurally divergent from conventional antibiotics and displays
  bactericidal activity against a wide phylogenetic spectrum of pathogens including Mycobacterium
  tuberculosis and carbapenem-resistant Enterobacteriaceae.**"; "**from a discrete set of 23 empirically
  tested predictions from >107 million molecules curated from the ZINC15 database, our model identified
  eight antibacterial compounds that are structurally distant from known antibiotics.**"
- USE: the hook (resistance crisis) + the landmark result — a DNN predicts antibacterial activity, finds
  halicin (a repurposed molecule structurally unlike known antibiotics) plus 8 novel ZINC15 hits.

## Section 1 — Aiming at a priority pathogen

### Liu et al. — abaucin, targeting A. baumannii — VERIFIED
- Liu G, Catacutan DB, Rathod K, … Stokes JM. "Deep learning-guided discovery of an antibiotic targeting
  Acinetobacter baumannii." *Nature Chemical Biology* 19:1342–1350, 2023. DOI 10.1038/s41589-023-01349-8.
- ABSTRACT-VERIFIED (verbatim): "**Acinetobacter baumannii is a nosocomial Gram-negative pathogen that often
  displays multidrug resistance.**"; "**machine learning methods allow for the rapid exploration of chemical
  space, increasing the probability of discovering new antibacterial molecules. Here we screened ~7,500
  molecules for those that inhibited the growth of A. baumannii in vitro.**"; "**we discovered abaucin, an
  antibacterial compound with narrow-spectrum activity against A. baumannii.**"; "**abaucin could control an
  A. baumannii infection in a mouse wound model.**"
- USE: the targeted-discovery story — train on ~7,500 growth-inhibition measurements, predict new
  structures, find abaucin: *narrow-spectrum* against a WHO priority Gram-negative pathogen (mechanism via
  LolE). Precision, not just breadth.

## Section 2 — Opening the black box, finding a new class

### Wong et al. — explainable deep learning, a new structural class — VERIFIED
- Wong F, Zheng EJ, Valeri JA, … Collins JJ. "Discovery of a structural class of antibiotics with
  explainable deep learning." *Nature* 626:177–185, 2024. DOI 10.1038/s41586-023-06887-8.
- ABSTRACT-VERIFIED (verbatim): "**Deep learning approaches have aided in exploring chemical spaces; these
  typically use black box models and do not provide chemical insights.**"; "**We determined the antibiotic
  activities and human cell cytotoxicity profiles of 39,312 compounds and applied ensembles of graph neural
  networks to predict antibiotic activity and cytotoxicity for 12,076,365 compounds.**"; "**one is selective
  against methicillin-resistant S. aureus (MRSA) and vancomycin-resistant enterococci, evades substantial
  resistance, and reduces bacterial titres in mouse models**"; "**machine learning models in drug discovery
  can be explainable, providing insights into the chemical substructures that underlie selective antibiotic
  activity.**"
- USE: the explainability turn — GNNs whose learned *substructure rationales* reveal *why* a molecule is
  antibacterial, screened across 12M compounds; yields a new structural class selective for MRSA/VRE that
  evades resistance. Prove-it + interpretability.

## Section 3 — Designing antimicrobials, not just screening them

### Das et al. — deep generative models + MD — VERIFIED
- Das P, Sercu T, Wadhawan K, … Mojsilovic A. "Accelerated antimicrobial discovery via deep generative
  models and molecular dynamics simulations." *Nature Biomedical Engineering* 5:613–623, 2021. DOI
  10.1038/s41551-021-00689-x.
- ABSTRACT-VERIFIED (verbatim): "**The de novo design of antimicrobial therapeutics involves the exploration
  of a vast chemical repertoire to find compounds with broad-spectrum potency and low toxicity.**"; "**The
  method leverages guidance from classifiers trained on an informative latent space of molecules modelled
  using a deep generative autoencoder, and screens the generated molecules using deep-learning classifiers
  as well as physicochemical features derived from high-throughput molecular dynamics simulations.**";
  "**Within 48 days, we identified, synthesized and experimentally tested 20 candidate antimicrobial
  peptides, of which two displayed high potency against diverse Gram-positive and Gram-negative pathogens
  … and a low propensity to induce drug resistance**."
- USE: the generative flip (and a bridge to Sep 9's MD) — a generative autoencoder proposes AMPs, DL
  classifiers + MD-derived features screen them; two potent, low-toxicity, pore-forming peptides in 48 days.

## Section 4 — Mining the microbiome's own arsenal

### Ma et al. — AMPs from the human gut microbiome — VERIFIED
- Ma Y, Guo Z, Xia B, … Wang J. "Identification of antimicrobial peptides from the human gut microbiome
  using deep learning." *Nature Biotechnology* 40:921–931, 2022. DOI 10.1038/s41587-022-01226-0.
- ABSTRACT-VERIFIED (verbatim): "**The human gut microbiome encodes a large variety of antimicrobial
  peptides (AMPs), but the short lengths of AMPs pose a challenge for computational prediction. Here we
  combined multiple natural language processing neural network models, including LSTM, Attention and BERT,
  to form a unified pipeline for candidate AMP identification from human gut microbiome data.**"; "**Of
  2,349 sequences identified as candidate AMPs, 216 were chemically synthesized, with 181 showing
  antimicrobial activity (a positive rate of >83%).**"; "**the potential of machine learning approaches for
  mining functional peptides from metagenome data**."
- USE: nature already makes antibiotics — mine them. NLP models (LSTM/Attention/BERT) read microbiome
  sequence; 181/216 synthesized candidates active (>83%), several potent against resistant Gram-negatives.

## Section 5 — At planetary scale: an open catalog

### Santos-Júnior et al. — AMPSphere, the global-microbiome AMP catalog — VERIFIED
- Santos-Júnior CD, Torres MDT, Duan Y, … de la Fuente-Nunez C, Coelho LP. "Discovery of antimicrobial
  peptides in the global microbiome with machine learning." *Cell* 187:3761–3778, 2024. DOI
  10.1016/j.cell.2024.05.013.
- ABSTRACT-VERIFIED (verbatim): "**Novel antibiotics are urgently needed to combat the antibiotic-resistance
  crisis. We present a machine-learning-based approach to predict antimicrobial peptides (AMPs) within the
  global microbiome and leverage a vast dataset of 63,410 metagenomes and 87,920 prokaryotic genomes … to
  create the AMPSphere, a comprehensive catalog comprising 863,498 non-redundant peptides**"; "**we
  synthesized and tested 100 AMPs against clinically relevant drug-resistant pathogens and human gut
  commensals both in vitro and in vivo. A total of 79 peptides were active, with 63 targeting pathogens.**";
  "**our approach identified nearly one million prokaryotic AMP sequences, an open-access resource for
  antibiotic discovery.**"
- USE: the scale capstone — ML over 63,410 metagenomes → 863,498 candidate AMPs (AMPSphere), 79/100 tested
  active; and, crucially for us, an *open-access* catalog. Discovery as public infrastructure.

## Section 6 — Lab hook + horizon
- The through-line is that AI *widens where we look* for medicines: old drug libraries (halicin), vast
  virtual chemical space (Wong's 12M, abaucin), and the microbiome itself (Ma, AMPSphere). Same move the
  digest keeps meeting — a general learner pointed at a search space too big for humans.
- Ties to this week's molecular thread: Sep 5 (protein *design*), Sep 8 (protein *engineering*), Sep 9 (ML
  *force fields* — Das literally uses MD-derived features). Antibiotic discovery is where those tools meet a
  clinical stakes.
- The [design→build→test→learn](/post/newsletter-2026-08-21/) loop is explicit here: predict → synthesize →
  assay in vitro/in vivo → refine. A [self-driving lab](/post/newsletter-2026-08-21/) is the natural engine.
- Open, benchmarked, callable ethos: AMPSphere is an open catalog; these models and growth-inhibition
  datasets are shared yardsticks — the same publish-the-model-*and*-the-data spirit behind the BioImage
  Model Zoo (/project/bioimage-model-zoo/) + BioEngine (/project/bioengine/) and the recurring
  [benchmark discipline](/post/newsletter-2026-07-27/). A resistance-crisis answer built as public
  infrastructure, not a locked pipeline.
