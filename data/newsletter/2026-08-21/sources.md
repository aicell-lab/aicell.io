# Newsletter sources — August 21, 2026

**Theme:** Self-driving labs / physical autonomous experimentation — "The Lab That Runs Itself."
The physical-machinery complement to the Aug 14 reasoning-agent piece (the mind that wonders) and
the July 31 decision-layer piece (the agent decides). Today: the actual robots that close the
design→make→test→analyze loop — and an honest audit of what they have delivered.

**X/Twitter sweep:** SKIPPED (getxapi out of credits — HTTP 402; 12th consecutive skip). Grok-based
replacement wired, awaiting xAI credits.

All anchors verified by two parallel general-purpose subagents against Crossref / PubMed / Europe PMC /
Semantic Scholar. Only abstract-verified numbers/quotes used in the post; body-only details flagged below
and NOT quoted as abstract.

---

## Section 1 — The closed loop, from Adam to Coscientist

### Robot Scientist "Adam" — VERIFIED
- King, R.D. et al. "The Automation of Science." *Science* **324**(5923):85–89, 3 April 2009.
- DOI: 10.1126/science.1165620 · PMID: 19342587 · Peer-reviewed Research Article.
- First author Ross D. King (corresponding/lead); Stephen G. Oliver senior co-PI; Amanda Clare last in byline.
- ABSTRACT-VERIFIED: "Adam has autonomously generated functional genomics hypotheses about the yeast
  *Saccharomyces cerevisiae* and experimentally tested these hypotheses by using laboratory automation";
  "We have confirmed Adam's conclusions through manual experiments"; formalization "involves over 10,000
  different research units in a nested treelike structure, 10 levels deep, that relates the 6.6 million
  biomass measurements to their logical description."
- NOT abstract (body-only — do NOT quote as abstract): any count of genes / orphan enzymes; phrase "without
  human intellectual intervention."

### Robot Scientist "Eve" — VERIFIED
- Williams, K. … King, R.D. "Cheaper faster drug development validated by the repositioning of drugs against
  neglected tropical diseases." *Journal of The Royal Society Interface* **12**(104):20141289, March 2015.
- DOI: 10.1098/rsif.2014.1289 · PMID: 25652463 · PMCID: PMC4345494 · Peer-reviewed.
- Kevin Williams first author; Ross D. King senior/last author.
- ABSTRACT-VERIFIED: Eve "uses artificial intelligence (AI) techniques to discover scientific knowledge
  through cycles of experimentation"; "integrates and automates library-screening, hit-confirmation, and lead
  generation through cycles of quantitative structure activity relationship learning and testing"; "One
  validated discovery is that the anti-cancer compound TNP-470 is a potent inhibitor of dihydrofolate reductase
  from the malaria-causing parasite *Plasmodium vivax*."
- CORRECTION to earlier brief: validated finding is **TNP-470 vs P. vivax DHFR**, NOT triclosan. Do not write triclosan.

### Coscientist — VERIFIED
- Boiko, D.A. … Gomes, G. "Autonomous chemical research with large language models." *Nature*
  **624**:570–578, 20 December 2023.
- DOI: 10.1038/s41586-023-06792-0 · PMID: 38123806 · Peer-reviewed. Gomes senior (Carnegie Mellon).
- ABSTRACT-VERIFIED: a GPT-4-driven system that "autonomously designs, plans and performs complex
  experiments"; tools include "internet and documentation search, code execution and experimental automation";
  demonstrated on "six diverse tasks"; "successful reaction optimization of palladium-catalysed cross-couplings."
- NOT abstract (body-only — do NOT quote as abstract): Suzuki / Sonogashira reaction names; "robotic liquid handlers."

## Section 2 — The honest ledger (A-Lab and the correction)

### A-Lab — VERIFIED, WITH AUTHOR CORRECTION (critical)
- Szymanski, N.J. … Ceder, G. Current title: "An autonomous laboratory for the accelerated synthesis of
  **inorganic** materials." *Nature* **624**:86–91, 29 November 2023.
- DOI: 10.1038/s41586-023-06734-w · PMID: 38030721 · Peer-reviewed. Gedeon (Gerbrand) Ceder senior (Berkeley/LBNL).
- **Author Correction:** 19 January 2026, DOI: 10.1038/s41586-025-09992-y.
- Original abstract reported synthesis of **41 novel compounds from 58 targets** over 17 days, title said
  "novel materials." After materials chemists (notably Robert Palgrave, UCL, and Leslie Schoop) publicly
  challenged the structural characterization / novelty claims, the correction revised the headline to
  **"36 compounds from a set of 57 targets"** over **"17 days of continuous operation,"** and the title from
  "novel materials" to "inorganic materials."
- **USE THE CORRECTED FIGURES: 36 of 57 targets over 17 days.** Do not cite the superseded 41/58 as current.
- Paper corrected, NOT retracted; the core autonomous-synthesis result survives; targets drawn from the
  Materials Project and Google DeepMind (GNoME) predictions.
- This correction is the post's honest-frontier beat: running autonomously is the easy half; verifying and
  reproducing what a robot made is the hard half.

## Section 3 — Bringing it to living cells

### Self-driving-lab review (framing) — VERIFIED (abstract-verified, incl. biology)
- Tobias, A.V. & Wahab, A. "Autonomous 'self-driving' laboratories: a review of technology and policy
  implications." *Royal Society Open Science* **12**(7), 2025. DOI: 10.1098/rsos.250646 · PMID: 40852582 · Peer-reviewed Review.
- ABSTRACT-VERIFIED: SDLs "combine artificial intelligence (AI) and laboratory automation to perform research
  in chemistry, materials science and biological sciences. Today's most capable SDLs automate nearly the entire
  scientific method, from hypothesis generation, experimental design, experiment execution and data analysis, to
  drawing conclusions and updating hypotheses for subsequent rounds of optimization or discovery."
- (Also verified but abstract paywalled — title only, do NOT quote: Abolhasani, M. & Kumacheva, E. "The rise of
  self-driving labs in chemical and materials sciences." *Nature Synthesis* 2:483–492, 2023,
  DOI 10.1038/s44160-022-00231-0.)

### Virtual Lab — biology autonomous-agent example — VERIFIED
- Swanson, K., Wu, W., Bulaong, N.L., Pak, J.E., Zou, J. "The Virtual Lab of AI agents designs new SARS-CoV-2
  nanobodies." *Nature* **646**(8085):716–723, 2025 (epub 29 Jul 2025).
- DOI: 10.1038/s41586-025-09442-9 · PMID: 40730228 · Peer-reviewed (was a Nov 2024 bioRxiv preprint first).
- James Zou senior (Stanford).
- ABSTRACT-VERIFIED: "an artificial intelligence (AI)–human research collaboration"; an "LLM Principal
  Investigator agent guiding a team of LLM scientist agents"; "created a novel computational nanobody design
  pipeline that incorporates the protein language model ESM, the protein folding model AlphaFold-Multimer and
  the computational biology software Rosetta and designed 92 new nanobodies"; "two new nanobodies exhibit
  improved binding to the recent JN.1 or KP.3 variants."
- Caveat: LLM-agent lab-in-the-loop (computational design + human validation), not a fully robotic closed loop.

## Lab connections
- Aug 14 (/post/newsletter-2026-08-14/) — the reasoning/hypothesis layer (Google AI co-scientist, FutureHouse Robin): the mind.
- July 31 (/post/newsletter-2026-07-31/) — the decision layer (the agent decides which experiment to run next).
- Lab projects: REEF Imaging Farm (/project/reef-imaging-farm/), Agent-Lens (/project/agent-lens/),
  Self-driving Microscope (/project/self-driving-microscope/), Autonomous Research Agents
  (/project/autonomous-research-agents/), BioEngine (/project/bioengine/).
- Prove-it discipline (/post/newsletter-2026-07-27/).
