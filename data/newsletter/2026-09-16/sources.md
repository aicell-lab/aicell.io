# Newsletter sources — 2026-09-16

Theme: **AI for antibody design & engineering** — deep-learning models that predict
antibody structure, learn the "language" of the immune repertoire, generate new
antibody sequences, and optimize therapeutic antibodies. Distinct from Sep 5
(general de novo protein design) and Sep 8 (directed evolution of arbitrary proteins):
antibodies are a specialized, medically enormous subdomain with their own models,
data (OAS), and design constraints (the six hypervariable CDR loops, developability).

All six anchors verified via NCBI E-utilities (esearch DOI→PMID, efetch abstract XML).
Fetched 2026-09-16T03:05Z.

## Anchors (NCBI-verified; abstracts captured)

1. **DeepAb — Antibody structure prediction using interpretable deep learning**
   — Ruffolo, Guerra, Mahajan, Sulam, Gray. *Patterns* (2022).
   DOI 10.1016/j.patter.2021.100406 | PMID 35199061.
   Why: the CDR-loop prediction challenge; interpretable DL for antibody Fv structure.
   The founding structure-prediction move.

2. **IgFold — Fast, accurate antibody structure prediction from deep learning on a
   massive set of natural antibodies** — Ruffolo, Chu, Mahajan, Gray.
   *Nature Communications* (2023). DOI 10.1038/s41467-023-38063-x | PMID 37185622.
   Why: language model pre-trained on 558M natural antibody sequences + graph networks;
   AlphaFold-quality structures in under 25 s; predicted 1.4M paired structures.

3. **AbLang — an antibody language model for completing antibody sequences**
   — Olsen, Moal, Deane. *Bioinformatics Advances* (2022).
   DOI 10.1093/bioadv/vbac046 | PMID 36699403.
   Why: antibody-specific LM (trained on OAS) beats general PLM (ESM-1b) on
   antibody-specific tasks like restoring missing residues. Specialized > general, here.

4. **IgLM — Infilling language modeling for antibody sequence design**
   — Shuai, Ruffolo, Gray. *Cell Systems* (2023).
   DOI 10.1016/j.cels.2023.10.001 | PMID 37909045.
   Why: generative, text-infilling LM (558M sequences) that re-designs variable-length
   spans with bidirectional context → synthetic antibody libraries with developability.

5. **Efficient evolution of human antibodies from general protein language models**
   — Hie, Shanker, Xu, Bruun, Weidenbacher, Tang, Wu, Pak, Kim.
   *Nature Biotechnology* (2024). DOI 10.1038/s41587-023-01763-2 | PMID 37095349.
   Why: general PLMs suggest evolutionarily plausible mutations with NO antigen/structure
   info; affinity-matured 7 antibodies, ≤20 variants over 2 rounds, up to 160-fold gains.
   Resolves the general-vs-specialized tension in the lab's favor (few-shot, wet-lab-cheap).

6. **Optimization of therapeutic antibodies by predicting antigen specificity from
   antibody sequence via deep learning** — Mason, Friedensohn, Weber, Jordi, Wagner,
   Meng, Ehling, Bonati, Dahinden, Gainza, Correia, Reddy. *Nature Biomedical
   Engineering* (2021). DOI 10.1038/s41551-021-00699-9 | PMID 33859386.
   Why: DL predicts antigen specificity from sequence → escape low-throughput full-length
   antibody screening; in-silico exploration of a vast sequence space for developable leads.

## Horizon radar (hypha-search surrogate; strategy note, not acted on)
- Cell — "Virtual Cell Challenge: Toward a Turing test for the virtual cell"
  (cell.com/cell/fulltext/S0092-8674(25)00675-0) and "How to build the virtual cell
  with artificial intelligence" (S0092-8674(24)01332-1). The virtual-cell agenda is
  crystallizing into a benchmarked community challenge — directly relevant to the lab's
  human-cell-simulator flagship. Candidate future digest theme (kept distinct from the
  Aug 15 single-cell-FM digest).
- CZ Biohub — "Virtual staining for real cells" (biohub.org/blog) — active follow-on to
  the Aug 6 virtual-staining digest; no new primary paper to anchor today.

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/discover` returns HTTP 402
  "Insufficient credits" (getxapi account out of credits; ~39th consecutive skip).
  x-breaking workflow remains effectively idle. Mitigation: hypha-search surrogate
  (web source) for a horizon scan only; snippets unverified → not used as claims.
- Anchor verification: NCBI E-utilities (esearch→efetch), all six DOIs resolved to a
  PMID with a matching title + abstract. Only verbatim quoted phrases used in the post.
- Dedup check: antibody design has NOT been a prior nightly theme. Adjacent-but-distinct
  from Sep 5 (de novo protein design), Sep 8 (directed evolution), Sep 2 (protein
  function prediction), Aug 12 (co-folding/affinity). Confirmed against the full
  content/post/newsletter-* slug list.
