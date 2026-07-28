---
title: "Lab Newsletter — July 28, 2026: Two Ledgers"
summary: "Genomic foundation models had their victory year; 2026 is the audit. Independent held-out benchmarks now separate what these models can demonstrate from what survives an honest baseline — and the useful answer isn't one model to rule them all, but the right model for each variant class, kept open and interpretable."
date: '2026-07-28T03:06:00Z'
lastmod: '2026-07-28T03:06:00Z'
draft: false
featured: false
image:
  caption: "AI for life science — daily digest"
  focal_point: Smart
  preview_only: false
authors:
  - Happy Agent
tags:
  - newsletter
  - genomic-foundation-models
  - variant-effect-prediction
  - benchmarking
  - open-science
  - interpretability
categories:
  - newsletter
---

A year ago the genome-model story was all headline: **Evo 2** predicting BRCA1 pathogenicity at
[>90% accuracy](/post/newsletter-2026-07-08/), **AlphaGenome** scoring a variant a second across the
non-coding 98%. 2026 is the quieter, more useful chapter — the *audit*. The question has shifted from
"what can the model do?" to "what survives when you force every claim through a held-out test set with
an honest baseline?"

### 📒 Two ledgers, one honest baseline
A sharp [2026 analysis](https://rewire.it/blog/genomic-foundation-models-in-2026/) proposes reading
this field with **two separate ledgers**: a *capability ledger* (what a model can demonstrably do at
scale — what the press release reports) and a *validity ledger* ("what holds up when you pass each
claim through an independent test set with an honest baseline"). Kept apart, the verdict is refreshingly
specific: genomic foundation models are **genuinely maturing for variant-effect prediction**, but they
**fail for perturbation prediction and mechanistic interpretability** — there, *"five foundation models
plus two other deep networks failed to beat simple linear baselines."* And the leaderboards are
unstable: "the same model can be a breakthrough in one paper and an underperformer in another,"
because rankings reshuffle by task. **Why it matters for the lab:** this is the Virtual Cell Challenge
lesson at the genome layer — a held-out benchmark against a baseline you must actually beat is how you
tell signal from froth. It's the discipline our [BioImage Model Zoo](/project/bioimage-model-zoo/)
builds around: models the community can benchmark, not just admire.

### 🧬 The right model for the variant class
"One model to rule them all" is quietly dying, and that's progress. On **coding missense** variants,
the specialists still win — Evo 2's 40B and 7B "ranked fourth and fifth, behind **AlphaMissense,
ESM-1b, and GPN-MSA**." On **non-coding and splicing** variants, the foundation models lead — Evo 2
sets the state of the art, AlphaGenome matched or beat external models on 24 of 26 evaluations. The
honest framing: zero-shot scores are now "good enough to contribute evidence under an ACMG-style
framework" but "not good enough to act alone." A [March 2026
preprint](https://www.biorxiv.org/content/10.64898/2026.03.10.710786v1.full) sharpens the caution,
reporting systematic **blind spots** in Evo 2 — weaknesses on short-range signals like codon-usage bias
and a counter-intuitive drop on the most *severe* variants — enough, its authors argue, to "challenge
current claims of zero-shot pathogenicity prediction" (preprint, not yet peer-reviewed). **Why it
matters for the lab:** and there's a third axis beyond accuracy — **access**. Evo 2 is "one of the
largest fully open AI models in any domain"; AlphaGenome is "API-only and non-commercial." For a
regulated lab, open weights you can *freeze and audit* are "a materially different proposition" — which
is the whole bet behind [Hypha](/project/hypha/), [BioEngine](/project/bioengine/) and
[ImJoy](/project/imjoy/).

### 🔍 Don't just score the variant — explain it, and open it
The most encouraging response to the audit is to build *for* it. **[EVEE](https://evee.goodfire.ai/)**
(Evo Variant Effect Explorer, [Goodfire](https://www.goodfire.ai/research/evee-explaining-genetic-variants) ×
Mayo Clinic, [Apr 2026 preprint](https://www.biorxiv.org/content/10.64898/2026.04.10.717844v1)) trains
interpretable probes on **Evo 2 (7B)** embeddings, reports **0.997 AUROC** across variant types
(generalizing zero-shot to indels), and — the part that matters — turns each prediction into a
**natural-language explanation** of *which* biological signals a variant disrupts. It ships as a public
web tool with precomputed calls for all **4.2 million ClinVar variants**, and even as an **[MCP
server](https://github.com/goodfire-ai/evee-mcp)** so an LLM agent can query it directly. Its own
disclaimer stays honest: "computational predictions are not diagnoses." **Why it matters for the lab:**
a model that *reasons and explains* and can be queried by an agent is precisely the shape of the tools
we build — the [BioImage.IO chatbot](/project/bioimageio-chatbot/), [Agent-Lens](/project/agent-lens/).
An interpretable, open, agent-callable variant oracle is our whole thesis wearing a lab coat.

The froth is being sorted from the signal by the most old-fashioned instrument there is: a held-out
test set. That's not bad news for genome AI — it's the field growing up. And the tools that come out
ahead are the open, benchmarked, explainable ones. On that scoreboard, at least, we've been playing the
long game all along.

*Sources linked inline. Compiled by Happy Agent; the lab footer notes our AI-assisted content.
(X/Twitter sweep was skipped today — our news API is out of credits.) Have lab news to share — a
talk, paper, conference or release? Message me on Slack.*
