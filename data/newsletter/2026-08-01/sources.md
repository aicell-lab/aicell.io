# Newsletter sources — 2026-08-01

Theme: **Proof under the microscope.** Computational-pathology foundation models are
crossing from *capability* (reading slides, drafting reports — which we covered Jul 21)
to *clinical evidence*: prospective studies and even a randomized controlled trial, and
they're starting to **show their reasoning** rather than emit an opaque label. A tissue-
image story squarely in the lab's wheelhouse (bioimaging + the Human Protein Atlas'
image↔molecular link), and a fresh evidence-level angle distinct from recent digests.

## Provenance / method
- Web research (WebSearch + WebFetch). X/Twitter sweep **skipped**: `scripts/lab-x.py
  monitor --since-hours 24 --min-likes 30` again returns **HTTP 402 Insufficient
  credits** (getxapi out of credits ~4+ weeks); `search`/`discover` gated. x-breaking
  stays disabled. Flagged to Wei for a credit top-up.
- **De-dup / variety:** Jul 21 ("When the Microscope Learns to Talk") covered pathology
  FMs at the **capability** level — TITAN drafting reports, an oncology FM fusing slides
  + clinical text. This digest deliberately takes the **next, distinct** angle:
  **prospective/RCT-level clinical evidence** and **interpretability** (show-your-work
  diagnosis), plus the **image↔molecular** frontier. Also distinct from Jul 26 spatial
  (histology→gene-expression inference) and Jul 29 cryo-ET (structural). The last 9 days
  covered open science, antibody design, spatial, strategy, genomic-FM eval, cryo-ET,
  RNA, self-driving labs — none is whole-slide-diagnosis evidence. Clear to run.
- **Verification discipline:** the two load-bearing anchors **primary-fetched from
  arXiv** (2605.25878; 2505.20510) with verbatim quotes. The context item (mSTAR) and
  the FDA-clearance / federated framing are **multi-source corroborated** via the 2026
  digital-pathology review (PMC) and Nature listings. **PulmoFoundation is a preprint
  (v2, 17 Jul 2026, HTML labeled "experimental")** — its prospective/RCT numbers are
  reported *as by the authors, not yet peer-reviewed*, and labeled as such in the post.

## Item 1 — From AUC to RCT: PulmoFoundation (ANCHOR, primary-fetched, PREPRINT)
- Source (fetched): Guo, Zhang, Ma, ... Hao Chen (26 authors), "A Clinically Validated
  Foundation Model for Comprehensive Lung Pathology Interpretation," **arXiv:2605.25878**
  [eess.IV], v1 25 May 2026, **v2 17 Jul 2026** (HTML labeled experimental).
  https://arxiv.org/abs/2605.25878
- Verified facts / verbatim (reported by authors; preprint):
  - "PulmoFoundation" — a lung-pathology FM built on **Virchow2** via **subspecialty-
    specific pretraining** on **~40,000 diagnostic H&E whole-slide images**; evaluated on
    **~26,000 WSIs** across **32 clinically relevant tasks** (molecular-marker prediction,
    survival prediction, core diagnosis across biopsy / frozen-section / resection).
  - **Prospective study:** *"In a registered prospective study of 1,357 patients across 11
    diagnostic tasks, our model achieved an average AUC of 92.3%."*
  - **Crossover RCT:** eight pathologists, **5,264 case-reader pairs**; reader accuracy
    **91.7% with AI vs 83.2% without**; inter-rater agreement rose "from moderate
    (kappa = 0.55) to substantial (kappa = 0.76)."
  - Motivation/gap the authors state: existing pan-cancer FMs "lack subspecialty-level
    depth and have not been ... prospectively validated in real-world settings."
  - **Caveat (stated in post):** preprint, not peer-reviewed; numbers are the authors'.

## Item 2 — Show your work: CPathAgent (ANCHOR, primary-fetched)
- Source (fetched): Yuxuan Sun, Yixuan Si, Chenglu Zhu, Kai Zhang, Zhongyi Shui, Bowen
  Ding, Tao Lin, Lin Yang, "CPathAgent: An Agent-based Foundation Model for Interpretable
  High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic,"
  **arXiv:2505.20510** [cs.CV], v1 26 May 2025, v2 28 Oct 2025.
  https://arxiv.org/abs/2505.20510
- Verified facts / verbatim:
  - Unifies **patch-, region-, and whole-slide** analysis in one agent-based model;
    instead of jumping to an answer it **navigates the slide autonomously** — low-mag
    overview, then zooming into suspicious regions — generating **step-by-step, navigable
    diagnostic summaries**.
  - Verbatim: pathologists "systematically examine slides at low magnification to obtain
    an overview before progressively zooming in on suspicious regions"; and prior
    "existing models directly output final diagnoses without revealing the underlying
    reasoning process."
  - Introduces **PathMMU-HR2**, "the first expert-validated benchmark for large region
    analysis" (the intermediate scale between patch and whole slide).

## Item 3 — The frontier: image↔molecular, and privacy (context, multi-source)
- mSTAR: "A multimodal knowledge-enhanced whole-slide pathology foundation model,"
  **Nature Communications** (Dec 2025). https://www.nature.com/articles/s41467-025-66220-x
  - Reported: integrates **three modalities — pathology slides, expert reports, and gene-
    expression profiles** — in one framework; **26,169 slide-level modality pairs across
    32 cancer types, >116M patch images**. The step beyond image+text (Jul 21's TITAN /
    oncology FM) to **image + molecular** — the imaging↔omics bridge.
- 2026 digital-pathology review (context/corroboration): "What's new in digital and
  computational pathology 2026," **PMC13183467**.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC13183467/
  - Corroborated framing: 2026 has expanding **FDA clearances** (Paige Prostate; HER2,
    PD-L1, Ki-67 quantification; cervical cytology) — tools that **augment**, not replace,
    pathologists (flag ROIs, quantify biomarkers). **Federated learning** approaches
    enable "more robust and privacy-preserving model development" without pooling patient
    slides. Honest frontier: inter-observer subjectivity (kappa ~0.4–0.7 for most tumor
    grading) motivates the tools; rare-disease / disease-specific cohorts remain data-scarce.
- Landscape names (established, cited for context): **UNI**, **Virchow / Virchow2**
  (Paige), **CONCH**, **Prov-GigaPath** (1.3B tiles), **TITAN** (multimodal whole-slide;
  covered Jul 21).

## Lab connections (for "why it matters")
- **Human Protein Atlas heritage.** The lab's roots are tissue microscopy + antibody-based
  proteomics — image ↔ molecular. mSTAR fusing slides with gene expression is exactly that
  bridge at foundation-model scale; whole-slide FMs are BioImage-Model-Zoo territory in a
  clinical modality ([BioImage Model Zoo](/project/bioimage-model-zoo/), AI4Life).
- **Prove-it, at a new evidence level.** The lab's benchmark culture (held-out tests,
  honest baselines — Jul 27/28) now meets **prospective + RCT** evidence. That's the bar
  clinical AI has to clear, and it's the discipline the lab champions.
- **Interpretable, agent-shaped tools.** CPathAgent that reasons and *shows its work* is
  the shape of the lab's agent stack ([BioImage.IO chatbot](/project/bioimageio-chatbot/),
  [Agent-Lens](/project/agent-lens/)) — models you can inspect, not just trust.
- **Privacy-preserving / federated** model-building for patient data is a lab interest
  (federated / privacy-preserving AI) — building clinical models without centralizing slides.

## De-dup check
- Recent digests: Jul 31 self-driving labs; Jul 30 RNA FMs; Jul 29 cryo-ET; Jul 28
  genomic-FM eval; Jul 27 strategy; Jul 26 spatial; Jul 25 antibody; Jul 24 open science;
  Jul 21 pathology **capability** (TITAN / multimodal report-drafting). This digest is the
  **evidence + interpretability + molecular** angle — a deliberate next step, not a repeat.
  Clear to run.
