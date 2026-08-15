# Newsletter sources — 2026-08-15 (fetched UTC 2026-08-15T03:00:21Z)

Theme: **A Turing test for the cell — the race to build a "virtual cell" that can
predict how a real one responds to a perturbation it has never seen, and the honest
2025 reckoning that today's foundation models still don't beat simple baselines.**
This is the lab's flagship horizon — a [Human Cell Simulator](/project/human-cell-simulator/) —
seen with a strategy-radar eye: the ambition (Arc's **State** model + a CASP-style
**Virtual Cell Challenge**), the tools (single-cell foundation models — **Geneformer**,
**scGPT**), and the [prove-it](/post/newsletter-2026-07-27/) verdict (*Nature Methods*:
**deep models do not yet outperform linear baselines** at predicting perturbation effects).
A negative result that is the field maturing, not failing.

## Provenance / method
- Web research (WebSearch + WebFetch). Anchors verified against primary/peer-reviewed sources:
  - **Virtual Cell Challenge / State** — Roohani, Hua, Tung, Bounds, Yu, Dobin, Teyssier,
    Adduri, Woodrow, Plosky, et al., "**Virtual cell challenge: Toward a Turing test for the
    virtual cell**," ***Cell* 188(13):3370–3374, 2025** (peer-reviewed commentary; Arc Institute).
    State model scale + challenge design/participation verified from Arc's Virtual Cell
    Initiative pages and the Cell commentary.
  - **The reckoning** — Constantin Ahlmann-Eltze, Wolfgang Huber & Simon Anders (EMBL /
    Heidelberg / UCL), "**Deep-learning-based gene perturbation effect prediction does not yet
    outperform simple linear baselines**," ***Nature Methods* 22:1657–1661, 2025**,
    DOI 10.1038/s41592-025-02772-6 (PMID 40759747; bioRxiv 2024.09.16.613342). Peer-reviewed.
    Verified the exact finding (five FMs + two DL models vs simple baselines; none win;
    additive model for combos, mean for unseen genes).
  - **Geneformer** — Theodoris et al., "**Transfer learning enables predictions in network
    biology**," ***Nature* 618:616–624, 2023**, DOI 10.1038/s41586-023-06139-9 (~30M
    transcriptomes; v2 → 95M).
  - **scGPT** — Cui, Wang, Maan et al., "**scGPT: toward building a foundation model for
    single-cell multi-omics using generative AI**," ***Nature Methods* 21:1470–1480, 2024**,
    DOI 10.1038/s41592-024-02201-0 (PMID 38409223; >33M cells).
  - Corroborating benchmarks cited as landscape and labelled: BMC Genomics (Csendes et al.,
    2025, mean baseline beats scGPT/scFoundation); PertEval-scFM (bioRxiv 2024.10.02.616248,
    **preprint**).
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  returns **HTTP 402 Insufficient credits** (getxapi out of credits ~6 weeks). The Grok
  `x_search` replacement is wired but the xAI team has **no credits yet** (403). Flagged to Wei.
- **De-dup / variety (important):** *single-cell foundation models + perturbation-response
  prediction (the transcriptomic virtual cell) + the baseline reckoning* has **not** been a
  digest theme. Distinct from the recent run:
  - **Aug 2 "virtual cell"** = the general *validation/show-your-work* discipline for virtual
    cells. Today is concrete and specific: the *perturbation-prediction task*, the *models*
    built for it (Geneformer/scGPT/State), the *CASP-style challenge*, and the *Nature Methods
    baseline verdict*. Different altitude (specific models + benchmark, not a principle).
  - **Aug 9 genome FMs** = **DNA-sequence** language models. Today = **single-cell RNA /
    transcriptome** foundation models — different data, different task (expression response,
    not sequence function).
  - **Aug 13 spatial transcriptomics** = *where* cells sit (tissue context). Today = *how a
    cell's expression changes* under a genetic/chemical perturbation (counterfactual response).
  - **Aug 14 AI co-scientist** = reasoning *agents*. Today = predictive *cell models* such an
    agent would need as an instrument (explicitly linked, not repeated).
  Clear separation. Clear to run.
- **Verification discipline:** the two anchors (Cell commentary, Nature Methods) are
  peer-reviewed; Geneformer/scGPT are peer-reviewed. PertEval-scFM labelled a preprint. The
  headline "reckoning" claim is quoted from the paper's own title + Nature Methods summary and
  attributed. No fabricated leaderboard numbers.

## Item 1 — The ambition: a cell you can query (Virtual Cell Challenge + State)
- **The dream stated precisely (Arc's "North Star"):** *given a starting cell state and a
  perturbation, predict the resulting gene-expression changes well enough to guide biological
  discovery.* A model you could **ask "what if?"** instead of running every experiment.
- **State (Arc Institute)** — a first-generation virtual cell model that "**captures the cell-
  type-specific effects of genetic, chemical, and cytokine perturbations on the cellular
  transcriptome**," trained on **167 million observational cells** + **>100 million
  perturbational cells** across **70 human cell contexts**.
- **The Virtual Cell Challenge** ("**Toward a Turing test for the virtual cell**," *Cell*
  188:3370–3374, 2025) makes it a **CASP-for-cells**: an annually refreshed, high-quality
  benchmark + live leaderboard, explicitly modeled on how **CASP** catalyzed protein-structure
  prediction. The **2025** edition tested **context generalization** — predict single-gene
  **CRISPRi** perturbation effects in a **held-out H1 human embryonic stem cell** type (a
  deliberate distribution shift from common training lines like K562/A375), on a purpose-built
  **~300,000-cell** scRNA-seq dataset with **300 perturbations**.
- **Scale of interest:** **>5,000 registrants across 114 countries, >1,200 teams**, 300+ final
  submissions — a field organizing itself around one honest metric. (Data engine behind it:
  the Tahoe-100M / Arc–Biohub perturbation-atlas effort.)

## Item 2 — The tools: single-cell foundation models
- **Geneformer** (Theodoris et al., *Nature* 618:616–624, 2023) — a **context-aware, attention-
  based** transformer **pretrained on ~30M single-cell transcriptomes** (v2: 95M), which
  "**gained a fundamental understanding of network dynamics, encoding network hierarchy in the
  attention weights ... in a completely self-supervised manner**," enabling context-specific
  predictions with limited task data.
- **scGPT** (Cui et al., *Nature Methods* 21:1470–1480, 2024) — a **generative pretrained
  transformer** built over **>33M cells**, offering transfer learning for cell-type
  classification, multi-omic integration, gene-network inference, **and perturbation-response
  modeling**.
- **The promise:** pretrain on the ocean of unlabeled scRNA-seq, then fine-tune to predict how
  a cell will respond — the same recipe that worked for language and, arguably, for proteins.

## Item 3 — The honest reckoning + why it matters for the lab
- **The verdict (prove-it, in its purest form).** Ahlmann-Eltze, Huber & Anders (*Nature
  Methods* 22:1657–1661, 2025) benchmarked **five foundation models and two other deep-learning
  models against deliberately simple baselines**, and **none outperformed the baselines**:
  for **combinatorial** perturbations (individual singles seen) they did **no better than a
  simple additive model**; for **unseen** genes, **no better than predicting the mean** across
  training perturbations. A BMC Genomics benchmark (Csendes et al., 2025) found even the
  **mean of training examples** beat scGPT and scFoundation. The authors' framing is the point:
  this "**highlights the importance of critical benchmarking in directing ... method
  development**."
- **Why this is the right story for the lab.** A [Human Cell Simulator](/project/human-cell-simulator/)
  is precisely this bet — and the honest news makes the case *for* how the lab works, not
  against it: build with **validation and benchmarking front-and-center**, treat a predicted
  perturbation as a **hypothesis**, and measure against **CASP-style challenges** rather than
  self-reported wins. The Virtual Cell Challenge is exactly the kind of shared, honest yardstick
  the field (and the lab's models) should be held to.
- **It plugs into the rest of the stack.** A predictive cell model is the *instrument* an
  [autonomous research agent](/post/newsletter-2026-08-14/) needs to reason about which
  experiment to run; [spatial context](/post/newsletter-2026-08-13/) is the tissue layer such a
  model still lacks; and open models + open perturbation data are the
  [BioEngine](/project/bioengine/) / [BioImage Model Zoo](/project/bioimage-model-zoo/) ethos,
  now for single-cell biology.
- **The honest frontier.** The gap is real: perturbation data is scarce relative to
  observational data; "beating the mean" for a genuinely unseen gene is unsolved; and a
  transformer's confident prediction is not a measurement. That's not a reason to look away —
  it's the [prove-it discipline](/post/newsletter-2026-07-27/) that turns a hype cycle into a
  science. The AlphaFold moment for the cell hasn't arrived; the honest scoreboard that could
  summon it just did.

## Lab connections (for "why it matters")
- **human-cell-simulator** — the flagship bet; today's story is its ambition *and* its honest scoreboard.
- **autonomous-research-agents (Aug 14)** — a predictive cell model is the instrument a reasoning agent needs.
- **Aug 13 spatial** — tissue/spatial context is the layer perturbation models still lack.
- **bioengine / bioimage-model-zoo** — open models + open perturbation data + shared benchmarks.
- **prove-it (Jul 27) / Aug 2 virtual cell** — predicted perturbation = hypothesis; measure against CASP-style challenges.

## De-dup check
- Recent digests: Aug 14 AI co-scientist; Aug 13 spatial transcriptomics; Aug 12 co-folding/
  affinity; Aug 11 protein dynamics; Aug 10 optical pooled screening; Aug 9 genome FMs; Aug 8
  smart microscopy; Aug 7 proteomics; Aug 6 virtual staining; Aug 5 federated; Aug 4 profiling;
  Aug 3 small-molecule design; Aug 2 virtual cell; Aug 1 prove-it. **Single-cell foundation
  models + perturbation-response prediction + the baseline reckoning has not been a digest
  theme.** Distinct data (single-cell RNA), task (counterfactual expression response), and a
  peer-reviewed honest-reckoning anchor. Clear to run.
