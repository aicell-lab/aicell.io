# Newsletter sources — 2026-09-17

Theme: **AI for retrosynthesis & chemical synthesis planning** — deep-learning models
that plan how to *make* a molecule (recursively break a target into buyable precursors),
predict the forward outcome of a reaction, and hand the route to a robot to execute.
This is the "build/make" step of the design–build–test–learn loop the lab wants to
automate. Distinct from Aug 3 (generative small-molecule *design*), Aug 12 (co-folding/
affinity), Sep 5 (protein design), Sep 10 (antibiotic discovery), Sep 16 (antibody design):
those design *what* to make; retrosynthesis solves *how* to make it.

All six anchors verified via NCBI E-utilities (esearch DOI→PMID, efetch abstract XML).
Fetched 2026-09-17T03:00Z.

## Anchors (NCBI-verified; abstracts captured)

1. **Neural-Symbolic Machine Learning for Retrosynthesis and Reaction Prediction**
   — Segler, Waller. *Chemistry – A European Journal* (2017).
   DOI 10.1002/chem.201605499 | PMID 28134452.
   Why: founding move — deep nets "learn to resolve reactivity conflicts and to prioritize
   the most suitable transformation rules," trained on 3.5M reactions; 95% top-10 retrosynthesis.

2. **Computer-Assisted Retrosynthesis Based on Molecular Similarity**
   — Coley, Rogers, Green, Jensen. *ACS Central Science* (2017).
   DOI 10.1021/acscentsci.7b00355 | PMID 29296663.
   Why: knowledge-free alternative — molecular similarity to precedent reactions "without the
   need to encode any chemical knowledge"; 74.1% top-10 from 40k patent reactions.

3. **Planning chemical syntheses with deep neural networks and symbolic AI**
   — Segler, Preuss, Waller. *Nature* (2018).
   DOI 10.1038/nature25978 | PMID 29595767.
   Why: the landmark — Monte Carlo tree search + expansion-policy + filter networks; solves
   ~2× as many molecules, 30× faster; validated by chemists in a double-blind AB test.

4. **Molecular Transformer: A Model for Uncertainty-Calibrated Chemical Reaction Prediction**
   — Schwaller, Laino, Gaudin, Bolgar, Hunter, Bekas, Lee. *ACS Central Science* (2019).
   DOI 10.1021/acscentsci.9b00576 | PMID 31572784.
   Why: solves the forward problem as machine translation on SMILES; >90% top-1 on a common
   benchmark; "no handcrafted rules" and calibrated uncertainty on its own predictions.

5. **AiZynthFinder: a fast, robust and flexible open-source software for retrosynthetic
   planning** — Genheden, Thakkar, Chadimová, Reymond, Engkvist, Bjerrum.
   *Journal of Cheminformatics* (2020). DOI 10.1186/s13321-020-00472-1 | PMID 33292482.
   Why: open-source MCTS retrosynthesis (solution in <10 s); publish-the-tool spirit,
   engineered for maintainability — the community's default open planner.

6. **A robotic platform for flow synthesis of organic compounds informed by AI planning**
   — Coley, Thomas, Lummiss, ... , Jensen, Jamison. *Science* (2019).
   DOI 10.1126/science.aax1566 | PMID 31395756.
   Why: the closing loop — AI synthesis planning + a robotically reconfigured continuous-flow
   platform, demonstrated for 15 drug or drug-like substances. Plan → robot → molecule.

## Horizon radar (hypha-search surrogate; strategy note, not acted on)
- GenBio AI — "A World Model of the Virtual Cell"; Arc Institute — "Virtual Cell Initiative."
  The virtual-cell agenda keeps accelerating across labs/startups — directly relevant to the
  lab's human-cell-simulator flagship. Still a candidate future digest theme (kept distinct
  from the Aug 15 single-cell-FM digest and the Sep 16 note).

## Provenance / method notes
- X/Twitter sweep: **SKIPPED** — `scripts/lab-x.py monitor/discover` returns HTTP 402
  "Insufficient credits" (getxapi account out of credits; ~40th consecutive skip).
  Mitigation: hypha-search surrogate (web) for a horizon scan only; snippets unverified.
- Anchor verification: NCBI E-utilities (esearch→efetch); all six DOIs resolved to a PMID
  with matching title + abstract. Only verbatim quoted phrases used in the post.
- Dedup: retrosynthesis / synthesis planning has NOT been a prior nightly theme (checked the
  full content/post/newsletter-* slug list). Adjacent-but-distinct from the drug/design
  digests above.
