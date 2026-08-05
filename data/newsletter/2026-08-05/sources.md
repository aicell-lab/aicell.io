# Newsletter sources — 2026-08-05

Theme: **Move the model, not the data — federated & privacy-preserving learning
for biomedicine.** The bottleneck for AI in medicine isn't architecture, it's
*access*: the richest data (patient scans, clinical genomes, hospital records) is
siloed, sensitive, and legally impossible to pool. The answer taking shape flips the
usual recipe — instead of moving data to a central model, you move the model to the
data. 2025–26 shows this is no longer theoretical: a **foundation model pre-trained
across 16 institutions in 9 countries without centralizing a single image**
(UltraFedFM), decentralized "swarm" learning validated across hospitals, and an
honest 2026 literature reminding everyone that **privacy is not automatic** — it's an
engineering budget you spend. A lab-infrastructure story: this is the training-layer
version of the lab's "distribute the compute, share the model" thesis
(Hypha / BioEngine), and the frontier a lab member works on directly.

## Provenance / method
- Web research (WebSearch + WebFetch). X/Twitter sweep **skipped**: `scripts/lab-x.py
  monitor --since-hours 24 --min-likes 30` again returns **HTTP 402 Insufficient
  credits** (getxapi out of credits **~5 weeks**); `search`/`discover` gated.
  x-breaking stays disabled. Flagged to Wei again for a credit top-up.
- **De-dup / variety (important):** federated / privacy-preserving learning has **not**
  been a theme in this run. Recent digests skew generative design (Jul 23/25/30, Aug 3),
  virtual cell (Aug 2), imaging models (Jul 19/21/29, Aug 1/4), agents/self-driving labs
  (Jul 31), genomic-FM evaluation (Jul 28), spatial (Jul 26). **Considered and rejected
  today's obvious pick — DNA/genome FMs (AlphaGenome, Evo 2)** — because it overlaps
  heavily with **Jul 28 "Two Ledgers"** (genomic-FM held-out evaluation); re-running it
  so soon would re-tread that lane. Federated/privacy is a genuinely distinct axis: not
  *what* model, but *how you get the data to train it*. Clear to run.
- **Verification discipline:** the flagship (**UltraFedFM**) is **peer-reviewed** (npj
  Digital Medicine, a Nature Portfolio journal) and **primary-fetched from arXiv**
  (2411.16380) with verbatim quotes and exact numbers. Swarm-learning anchors are
  peer-reviewed (Nature Medicine 2022; a 2025 multi-center study, PMC). The honest-
  frontier reviews are 2026 peer-reviewed venues (npj Digital Medicine; Radiology: AI),
  quoted from search-surfaced text. nature.com abstracts 403/redirect WebFetch, so
  numbers are taken from the arXiv version and PMC/secondary corroboration.

## Item 1 — Capability: a foundation model built across data it never pooled (ANCHOR, peer-reviewed, primary-fetched)
- Source (fetched, arXiv): Yuncheng Jiang, Chun-Mei Feng, Jinke Ren, … Shaohua Zhou,
  Shuguang Cui, Zhen Li (18 authors), "From Pretraining to Privacy: Federated Ultrasound
  Foundation Model with Self-Supervised Learning," **arXiv:2411.16380**; published in
  **npj Digital Medicine (2025)**, DOI 10.1038/s41746-025-02085-0 (PMID 41272022; PMC12638949).
- Verified facts / verbatim:
  - **UltraFedFM** is "an innovative privacy-preserving ultrasound foundation model,"
    collaboratively **pre-trained via federated learning across 16 distributed medical
    institutions in 9 countries**.
  - **Scale:** one server + 16 clients holding **1,015,754 unlabeled ultrasound images**,
    spanning **19 systemic organs** and **10 ultrasound imaging modalities**.
  - **Mechanism:** each client pre-trains a local model on its private data via pixel-
    level reconstruction; **only local model parameters are uploaded** to learn the global
    model — "this process does not expose the underlying data from any client," ensuring
    GDPR-style compliance.
  - **Performance:** "an average area under the receiver operating characteristic curve
    (AUROC) of **0.927** for disease diagnosis" and a **dice similarity coefficient (DSC)
    of 0.878** for lesion segmentation; evaluated on 8 organs (pancreas, gallbladder,
    liver, lung, colorectum, breast, heart, fetal organs).
  - **Clinical bar:** "UltraFedFM surpasses the diagnostic accuracy of mid-level
    ultrasonographers (4–8 years of experience)" and **matches expert sonographers (10+
    years)** in joint diagnosis of 8 common systemic diseases.

## Item 2 — A pattern, not a one-off: swarm (server-less) learning across hospitals (ANCHOR, peer-reviewed)
- **The landmark:** Oliver Lester Saldanha, … Jakob Nikolas Kather, "Swarm learning for
  decentralized artificial intelligence in cancer histopathology," **Nature Medicine 28,
  1232–1239 (2022)**, DOI 10.1038/s41591-022-01768-5 (PMID 35469069; open access) — a
  decentralized, privacy-preserving framework (no central aggregation server; blockchain-
  brokered parameter merging, HPE Swarm Learning) that trained clinically relevant
  molecular-biomarker classifiers on **colorectal-cancer cohorts from Northern Ireland,
  Germany, and the US** and validated on **two independent UK datasets**, each site keeping
  its slides local. The reference point that made server-less collaborative clinical AI
  credible. (NB: distinct from Warnat-Herresthal et al., *Nature* 2021, the original
  swarm-learning method paper — not cited here to avoid conflation.)
- **The 2025 multi-center validation:** a blockchain-based **swarm learning** diagnostic
  study for knee-fracture image analysis pulled images from **4 independent hospitals**
  (China, Dec 2013–Jul 2023), **4,581 patients**, and built an explainable distributed SL
  model, comparing it against centralized AI and clinicians in real-world use. PMC12267170.
  "Swarm learning … enables collaborative model training through secure parameter
  aggregation while preserving data locality." Shows the decentralized recipe now runs at
  clinical scale across institutions.

## Item 3 — The honest frontier: privacy is engineered, not automatic (ANCHOR, 2026 reviews)
- **DP deployment caveat** — "Differential privacy for medical deep learning: methods,
  tradeoffs, and deployment implications," **npj Digital Medicine (Jan 2026)**,
  s41746-025-02280-z. Verbatim: once a model is trained with DP, "privacy guarantees
  remain tied to how often the model or the underlying dataset is accessed — multiple
  users querying a DP-trained model, or repeated inference … incrementally consume the
  **privacy budget through composition of privacy loss**." (Privacy is a finite resource
  you spend, not a property you install.)
- **Leakage + tradeoffs** — "Privacy-preserving Federated Learning and Uncertainty
  Quantification in Medical Imaging," **Radiology: Artificial Intelligence (2026)**,
  10.1148/ryai.240637. Verbatim: federated learning "remains **vulnerable to information
  leakage through gradient updates**, and privacy-preserving strategies such as
  differential privacy and homomorphic encryption reduce this risk but **introduce
  accuracy and efficiency trade-offs**."
- **Confidentiality is conditional** — a **May 2026** imaging-FL review (Springer,
  *Arch. Comput. Methods Eng.*, s11831-026-10629-0): only model updates are shared,
  "thereby reducing direct exposure of raw patient data … **however, confidentiality is
  not automatic and depends on additional safeguards**."

## Context / framing (named, not load-bearing)
- **Federated foundation models survey** — "Open challenges and opportunities in
  federated foundation models towards biomedical healthcare," *BioData Mining* (2024/25),
  10.1186/s13040-024-00414-9: FL + FMs is "a promising strategy to harness their
  analytical power while safeguarding the privacy of sensitive medical data."
- **Genomics/EHR federated frameworks** named for breadth (MultiProg EHR prognosis;
  DP-SGD medical-imaging frameworks) — direction, not load-bearing numbers.

## Lab connections (for "why it matters")
- **The training-layer twin of the lab's infrastructure thesis.** [Hypha](/project/hypha/)
  and [BioEngine](/project/bioengine/) are built to run and serve models across
  *distributed* compute — "move the compute/model, share the result." Federated learning
  is that same principle at the *training* layer: move the model to the data, never the
  data to the model.
- **Past the data-access wall.** The [Human Cell Simulator](/project/human-cell-simulator/)
  and the lab's bioimaging models will ultimately need to learn from data locked inside
  hospitals, atlases, and consortia that legally cannot be centralized. Federated /
  privacy-preserving learning is the route to that data without moving it.
- **A lab frontier, directly.** Privacy-preserving / federated learning for genomics and
  sensitive biomedical data is an active lab research direction — this digest is the
  field's state of the art around it.
- **Share the model, not the data.** The [BioImage Model Zoo](/project/bioimage-model-zoo/)
  / AI4Life ethos — distribute reusable, benchmarked models — rhymes with the federated
  premise: the model travels; the data stays home.

## De-dup check
- Recent digests: Aug 4 image-based profiling; Aug 3 small-molecule design; Aug 2 virtual
  cell; Aug 1 pathology; Jul 31 self-driving labs; Jul 30 RNA design; Jul 29 cryo-ET; Jul
  28 genomic-FM eval; Jul 27 strategy; Jul 26 spatial; Jul 25 antibody; Jul 24 open
  science. **Federated / privacy-preserving learning — the data-access axis — has not been
  a theme.** Distinct from Aug 1 (pathology models) and Jul 28 (genomic-FM eval): this is
  about *how you assemble training data across silos*, not which model wins a benchmark.
  Clear to run.
