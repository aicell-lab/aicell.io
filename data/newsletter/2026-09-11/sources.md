# Newsletter sources — September 11, 2026

**Theme:** **Knowledge graphs + graph machine learning for biomedicine** — representing biology
and medicine as heterogeneous networks (genes, drugs, diseases, proteins, pathways, side effects)
and learning on those graphs to predict *hidden* connections: drug repurposing, polypharmacy side
effects, disease mechanisms. "Medicine as a Graph." The arc: integrate all biomedical knowledge into
one network and walk it (Hetionet/Rephetio) → GNNs for multirelational link prediction (Decagon) →
the method meets an emergency (COVID network medicine) → an open precision-medicine knowledge graph
(PrimeKG) → a graph *foundation model* for zero-shot repurposing (TxGNN) → the synthesis
(graph representation learning review).

**Why now / editorial:** deliberate pivot after six straight molecular-structure days
(protein design Sep 5, GRNs Sep 6, genome reading Sep 7, protein engineering Sep 8, force fields Sep 9,
antibiotics Sep 10). This is a *different method-class* — reasoning over the **web of relationships**
between biological entities rather than modeling one molecule's structure — and it ties directly to the
lab's **Research Navigator** (reasoning over biomedical knowledge) and open-resource ethos. A nice
complement to Sep 10: COVID network medicine finds drugs whose mechanism is *network-based* and
"cannot be identified using docking-based strategies."

**Dedup guard:** Knowledge graphs / graph representation learning / drug repurposing has **never** been
a newsletter theme (only incidental mentions: Jul 22 agents post referenced "repurpose drugs," Aug 14
was the AI co-scientist). Distinct from Aug 3 (generative *small-molecule* design), Sep 10 (ML
*screening* for antibiotics — structure/activity prediction), Sep 6 (gene *regulatory* network
*inference* from expression — a different graph: learned GRNs, not curated biomedical knowledge graphs),
and Sep 9 NequIP (graph nets on *atoms*, not on genes/drugs/diseases). Today's object is the
**heterogeneous biomedical knowledge graph** and link prediction on it.

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on `monitor` (min-likes 30,
since-hours 24). ~34th consecutive skip (>five weeks). Grok replacement wired, awaiting xAI credits.

All 6 anchors verified against **raw Europe PMC `abstractText` JSON** (fetched directly via curl — no
summarizer), with DOI/title/author/journal/year confirmed. Only abstract-verified verbatim quotes used.

---

## Framing + the founding move — integrate everything into one network

### Himmelstein et al. — Hetionet / Project Rephetio — VERIFIED
- Himmelstein DS, Lizee A, Hessler C, … Baranzini SE. "Systematic integration of biomedical knowledge
  prioritizes drugs for repurposing." *eLife* 2017. DOI 10.7554/eLife.26726.
- ABSTRACT-VERIFIED (verbatim): "**The ability to computationally predict whether a compound treats a
  disease would improve the economy and success rate of drug approval.**"; "**we constructed Hetionet
  (neo4j.het.io), an integrative network encoding knowledge from millions of biomedical studies.
  Hetionet v1.0 consists of 47,031 nodes of 11 types and 2,250,197 relationships of 24 types.**";
  "**we predicted the probability of treatment for 209,168 compound-disease pairs**"; "**This study was
  entirely open and received realtime feedback from 40 community members.**"
- USE: the founding idea — fuse 29 public resources into one heterogeneous network (compounds, diseases,
  genes, pathways, side effects…), learn which network *patterns* distinguish treatments, and score every
  compound-disease pair. And it was radically *open*. Sets up "medicine as a graph."

## Section 1 — Graph neural networks enter: predict the exact side effect

### Zitnik, Agrawal & Leskovec — Decagon — VERIFIED
- Zitnik M, Agrawal M, Leskovec J. "Modeling polypharmacy side effects with graph convolutional
  networks." *Bioinformatics* 34:i457–i466, 2018. DOI 10.1093/bioinformatics/bty294.
- ABSTRACT-VERIFIED (verbatim): "**we present Decagon, an approach for modeling polypharmacy side
  effects. The approach constructs a multimodal graph of protein-protein interactions, drug-protein
  target interactions and the polypharmacy side effects, which are represented as drug-drug
  interactions, where each side effect is an edge of a different type.**"; "**Our approach develops a
  new graph convolutional neural network for multirelational link prediction in multimodal networks.**";
  "**Decagon can predict the exact side effect, if any, through which a given drug combination manifests
  clinically. Decagon accurately predicts polypharmacy side effects, outperforming baselines by up to
  69%.**"
- USE: the deep-learning turn — a GCN for *multirelational link prediction* on a multimodal
  drug–protein–side-effect graph; not just "do these drugs interact" but *which* side effect, +69% over
  baselines. Graphs + neural nets = predicting missing edges.

## Section 2 — The method meets an emergency

### Morselli Gysi et al. — network medicine for COVID-19 — VERIFIED
- Morselli Gysi D, do Valle Í, Zitnik M, … Loscalzo J, Barabási AL. "Network medicine framework for
  identifying drug-repurposing opportunities for COVID-19." *PNAS* 118:e2025581118, 2021. DOI
  10.1073/pnas.2025581118.
- ABSTRACT-VERIFIED (verbatim): "**we deployed algorithms relying on artificial intelligence, network
  diffusion, and network proximity, tasking each of them to rank 6,340 drugs for their expected efficacy
  against SARS-CoV-2.**"; "**a consensus among the different predictive methods consistently exceeds the
  performance of the best individual pipelines.**"; "**We screened in human cells the top-ranked drugs,
  obtaining a 62% success rate, in contrast to the 0.8% hit rate of nonguided screenings.**"; "**76 of
  the 77 drugs that successfully reduced viral infection do not bind the proteins targeted by SARS-CoV-2,
  indicating that these network drugs rely on network-based mechanisms that cannot be identified using
  docking-based strategies.**"
- USE: the stakes + the payoff — network/AI methods rank 6,340 drugs; a *consensus* of methods beats any
  one; 62% vs 0.8% hit rate; and the punchline that 76/77 hits act through *network* mechanisms a docking
  model would miss. The complement to structure-based days.

## Section 3 — An open knowledge graph for precision medicine

### Chandak, Huang & Zitnik — PrimeKG — VERIFIED
- Chandak P, Huang K, Zitnik M. "Building a knowledge graph to enable precision medicine." *Scientific
  Data* 10:67, 2023. DOI 10.1038/s41597-023-01960-3.
- ABSTRACT-VERIFIED (verbatim): "**we present PrimeKG, a multimodal knowledge graph for precision
  medicine analyses. PrimeKG integrates 20 high-quality resources to describe 17,080 diseases with
  4,050,249 relationships representing ten major biological scales**"; "**PrimeKG contains an abundance
  of 'indications', 'contradictions', and 'off-label use' drug-disease edges that lack in other knowledge
  graphs and can support AI analyses of how drugs affect disease-associated networks.**"; "**We
  supplement PrimeKG's graph structure with language descriptions of clinical guidelines to enable
  multimodal analyses and provide instructions for continual updates**."
- USE: the open-resource capstone — a precision-medicine KG (17,080 diseases, ~4.05M relationships, ten
  biological scales), rich in the indication/contraindication/off-label edges AI needs, plus language
  descriptions for multimodal use. Discovery infrastructure, released open. (Note: abstract's verbatim
  word is "contradictions" — quote it exactly.)

## Section 4 — A graph foundation model for zero-shot repurposing

### Huang et al. — TxGNN — VERIFIED
- Huang K, Chandak P, Wang Q, … Gehlenborg N, Zitnik M. "A foundation model for clinician-centered drug
  repurposing." *Nature Medicine* 30:3601–3613, 2024. DOI 10.1038/s41591-024-03233-x.
- ABSTRACT-VERIFIED (verbatim): "**The clinical utility of drug-repurposing artificial intelligence (AI)
  models remains limited because these models focus narrowly on diseases for which some drugs already
  exist. Here we introduce TxGNN, a graph foundation model for zero-shot drug repurposing, identifying
  therapeutic candidates even for diseases with limited treatment options or no existing drugs.**";
  "**Trained on a medical knowledge graph, TxGNN uses a graph neural network and metric learning module
  to rank drugs as potential indications and contraindications for 17,080 diseases.**"; "**TxGNN improves
  prediction accuracy for indications by 49.2% and contraindications by 35.1% under stringent zero-shot
  evaluation.**"; "**TxGNN's Explainer module offers transparent insights into multi-hop medical
  knowledge paths that form TxGNN's predictive rationales.**"; "**Many of TxGNN's new predictions align
  well with off-label prescriptions that clinicians previously made in a large healthcare system.**"
- USE: the foundation-model turn — a *graph* foundation model that does *zero-shot* repurposing for
  diseases with **no** existing drugs (+49.2%/+35.1%), with an Explainer giving multi-hop interpretable
  reasoning paths, validated against real clinician off-label prescriptions. Built on PrimeKG.

## Section 5 — The synthesis: graph representation learning

### Li, Huang & Zitnik — Graph representation learning review — VERIFIED
- Li MM, Huang K, Zitnik M. "Graph representation learning in biomedicine and healthcare." *Nature
  Biomedical Engineering* 6:1353–1369, 2022. DOI 10.1038/s41551-022-00942-x.
- ABSTRACT-VERIFIED (verbatim): "**Networks-or graphs-are universal descriptors of systems of
  interacting elements.**"; "**we posit that representation learning can realize principles of network
  medicine**"; "**graph representation learning will keep pushing forward machine learning for
  biomedicine and healthcare applications, including the identification of genetic variants underlying
  complex traits, the disentanglement of single-cell behaviours and their effects on health, the
  assistance of patients in diagnosis and treatment, and the development of safe and effective
  medicines.**"
- USE: the synthesis — graphs are the "universal descriptors" of interacting biology; representation
  learning operationalizes network medicine; the horizon spans variants, single cells, diagnosis, and
  safer drugs. The through-line and the prove-it framing.

## Section 6 — Lab hook + horizon
- The through-line: **biology is a web of relationships**, and machine learning on that web predicts the
  edges we haven't drawn yet — a new indication, a dangerous drug pair, a disease mechanism. It's a
  *different lens* from this week's structure/sequence models: not "what shape is this molecule" but "how
  is everything connected." COVID network medicine makes the contrast explicit — 76/77 hits act through
  network mechanisms "that cannot be identified using docking-based strategies."
- Ties to the lab's **Research Navigator** (reasoning over biomedical knowledge) and to
  [AI agents](/post/newsletter-2026-08-14/): TxGNN's *multi-hop interpretable rationales* are exactly the
  kind of transparent reasoning-over-knowledge an [AI co-scientist](/post/newsletter-2026-08-14/) needs.
- Open, benchmarked, callable ethos: Hetionet, Decagon (snap.stanford.edu/decagon) and PrimeKG are all
  *open* — public graphs and code are the shared yardsticks, the same publish-the-model-*and*-the-data
  spirit behind the [BioImage Model Zoo](/project/bioimage-model-zoo/) and
  [BioEngine](/project/bioengine/). A repurposing model you can query with an explanation attached, built
  on an open knowledge graph, is precisely the kind of AI-for-life-science infrastructure the lab backs.
- Horizon / strategy radar: the [virtual cell](/project/human-cell-simulator/) will need *both* lenses —
  mechanistic structure/dynamics *and* a knowledge-graph scaffold of how genes, drugs and diseases relate.
