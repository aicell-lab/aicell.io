# Newsletter sources — 2026-07-28

Theme: **Two Ledgers** — the 2026 *evaluation reckoning* for genomic foundation
models. After the celebratory year (Evo 2 / AlphaGenome predicting variants), 2026's
story is the benchmark check: independent held-out tests separate what the models can
*demonstrate* from what *survives an honest baseline*, the field converges on "right
model for the right variant class," and the constructive response is open, interpretable,
agent-queryable tooling (EVEE).

## Provenance / method
- Web research (WebSearch + WebFetch). X/Twitter sweep **skipped**: `scripts/lab-x.py
  monitor` still returns **HTTP 402 Insufficient credits** (getxapi out of credits for
  ~3+ weeks). x-breaking stays disabled.
- **De-dup:** Jul 8 covered Evo 2 / AlphaGenome in a *celebratory* register (">90% BRCA1
  accuracy", genome writing); Jul 23 covered genome *design/synthesis*. This digest is the
  **opposite pole** — the critical evaluation / benchmarking wave — and is distinct.
- **Verification note:** biorxiv.org blocked WebFetch (HTTP 403) for both preprints, so the
  two preprint items are corroborated via **multiple secondary sources** (the developers'
  own research pages, the live web tools, and independent write-ups) rather than a primary
  full-text fetch. Preprint claims are labeled as such in the post. The load-bearing
  analytical anchor (rewire.it) **was** fully fetched.

## Item 1 — The reckoning: "what survives a held-out test set" (ANCHOR, fully fetched)
- Source (fetched twice): rewire.it, "Genomic Foundation Models in 2026: Two Ledgers, and
  What Survives a Held-Out Test Set." https://rewire.it/blog/genomic-foundation-models-in-2026/
- Verified facts / verbatim:
  - Two accounting systems: a **capability ledger** (demonstrable scale — what marketing
    reports) vs a **validity ledger** — "what holds up when you pass each claim through an
    independent test set with an honest baseline."
  - Divided verdict: foundation models are **genuinely maturing for variant effect
    prediction** but **fail for perturbation prediction and mechanistic interpretability**,
    where trivial linear baselines still win — "five foundation models plus two other deep
    networks failed to beat simple linear baselines on perturbation response."
  - Leaderboards unstable: "the same model can be a breakthrough in one paper and an
    underperformer in another"; rankings reshuffle by task category.
  - Clinical line: zero-shot scores "are now good enough to contribute evidence under an
    ACMG-style framework" but "not good enough to act alone. The maturity here is real, and
    it is bounded." Retrospective AUROC on ClinVar splits "is not prospective clinical
    utility." Guidance: "use the right model for the variant class, and anchor it to the
    benchmark that resembles your case."
  - Access as a third axis: **Evo 2** = "one of the largest fully open AI models in any
    domain" (weights, code, OpenGenome2). **AlphaGenome** = "API-only and non-commercial" —
    "a materially different proposition from open weights you can freeze and audit" for a
    regulated diagnostic lab.

## Item 2 — Which model wins where (rankings; from the fetched anchor + Jul-8-established)
- Source: same rewire.it analysis (fetched).
- Verified facts:
  - **Coding SNVs (missense):** specialists still lead — Evo 2's 40B / 7B "ranked fourth and
    fifth, behind **AlphaMissense, ESM-1b, and GPN-MSA**."
  - **Noncoding / splicing:** foundation models lead — Evo 2 "surpassed other models on both
    SNVs and non-SNVs," "highest zero-shot performance on exonic and intronic splice variant
    effect prediction," "new state of the art for BRCA1 noncoding SNVs." AlphaGenome "matched
    or exceeded the strongest available external models on 24 of 26 evaluations" (a count of
    evaluations won, not an effect size).
  - Evo 2 spec (established Jul 8, re-confirmed): 7B / 40B, 9.3T-nucleotide training,
    1M-token context; a documented blind spot — "no correlation between its likelihood and
    viral protein fitness for viruses that infect human hosts" (those sequences excluded
    from training).
- Critical-benchmark preprint (cited by title, **preprint, not primary-fetched**):
  "Benchmarking DNA Foundation Models: Biological Blind Spots in Evo2 Variant-Effect
  Prediction," bioRxiv 2026.03.10.710786 (Mar 2026).
  https://www.biorxiv.org/content/10.64898/2026.03.10.710786v1.full — WebSearch summary
  reports systematic blind spots in short-range signals (e.g. **codon-usage bias**) and a
  counterintuitive severity pattern (well on mild pathogenic variants, worse on
  moderate/severe), concluding these "challenge current claims of zero-shot pathogenicity
  prediction and raise concerns regarding the clinical readiness of such models." Stated in
  the post **as a preprint caution**, no precise figures asserted as verified.

## Item 3 — The constructive response: EVEE (interpretable + open; multi-source corroborated)
- Sources (secondary, corroborating — biorxiv full text was 403):
  - Developer research page (Goodfire): "Explaining 4.2 million genetic variants with
    state-of-the-art, interpretable predictions."
    https://www.goodfire.ai/research/evee-explaining-genetic-variants
  - Live web tool: https://evee.goodfire.ai/
  - Preprint (title/venue/date): Pearce et al., "EVEE: Interpretable variant effect
    prediction from genomic foundation model embeddings," bioRxiv 2026.04.10.717844 (Apr 2026).
    https://www.biorxiv.org/content/10.64898/2026.04.10.717844v1
  - MCP server: https://github.com/goodfire-ai/evee-mcp
- Corroborated facts (consistent across the sources above):
  - Built on **Evo 2 (7B)** embeddings; supervised annotation probes quantify per-variant
    disruptions, then a frontier reasoning model synthesizes **natural-language
    explanations**. Key trick: **covariance-based sequence pooling** (vs mean pooling).
  - Precomputed predictions + on-demand explanations for **all ~4.2M ClinVar variants**;
    reported **0.997 overall AUROC** (839k ClinVar variants), zero-shot to indels **0.991**;
    robust across conservation; transfers to DMS for BRCA1/BRCA2/TP53/LDLR.
  - Developed **in collaboration with Mayo Clinic**; full per-variant table (4.25M rows,
    ~4,900 probe outputs) archived on Zenodo; also exposed as an **MCP server** so LLM agents
    (e.g. Claude) can query predictions/interpretations. Disclaimer on the tool:
    "Computational predictions are not diagnoses."

## Lab connections (for "why it matters")
- The Virtual Cell Challenge lesson at the **genome layer**: held-out benchmarks + honest
  baselines are how you separate signal from hype — the lab's benchmarked, community-owned
  model culture (**BioImage Model Zoo**, **BioEngine**).
- **Open, version-lockable weights you can freeze and audit** are becoming a *clinical*
  requirement — exactly the open-infrastructure bet (**Hypha / ImJoy / BioEngine**).
- EVEE-as-MCP (an agent-queryable variant oracle for Claude) is literally the shape of the
  lab's agent stack (**BioImage.IO chatbot**, **Agent-Lens**) — models that reason *and*
  explain, kept inspectable.

## De-dup check
- Recent digests: Jul 27 ecosystem/strategy (money+rules+autonomy); Jul 26 spatial; Jul 25
  antibody design; Jul 24 open science; Jul 23 genome *writing*; Jul 8 Evo2/AlphaGenome
  *celebratory*. **No prior digest** took the critical-evaluation / held-out-benchmark angle
  on genomic FMs. Clear to run. (Complements — does not repeat — Jul 27's "prove it" theme:
  that was money/regulation; this is scientific benchmarking.)
