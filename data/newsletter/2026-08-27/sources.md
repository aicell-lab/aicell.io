# Newsletter sources — August 27, 2026

**Theme:** RNA velocity & cell-state dynamics — inferring the *direction* of cell fate from static
single-cell snapshots ("The Arrow Inside a Snapshot"). The MOLECULAR counterpart to Aug 25's
imaging-based cell tracking: instead of watching cells move frame to frame, read the arrow of time
out of a single sequencing snapshot via the ratio of unspliced to spliced mRNA. A FRESH domain,
distinct from Aug 15 (single-cell FMs / perturbation-response prediction — this is dynamics/direction
inference, not perturbation prediction) and Aug 25 (imaging lineage tracking). Horizon /
strategy-radar: cell-state dynamics is the raw material of a virtual cell (human-cell-simulator), and
these are open, callable tools (cellrank.org, scVelo). Local Stockholm tie: the origin paper's senior
author, Sten Linnarsson, is at Karolinska Institutet + SciLifeLab.

**Note on cadence:** the Aug 26 nightly slot was missed (session spanned the day boundary; X API
still down). This digest is published as the Aug 27 (current-day) digest — one digest, dated the real
current UTC day. No back-dated Aug 26 post was fabricated.

**X/Twitter sweep:** SKIPPED — getxapi out of credits (HTTP 402) on monitor, search, AND discover;
now the 18th consecutive skip (>two weeks). Grok-based replacement wired, awaiting xAI credits.

All anchors verified by two parallel general-purpose subagents against Crossref / Europe PMC, with
VERBATIM abstracts obtained. Only abstract-verified numbers/quotes are used in the post. Note: the
critique's abstract (Bergen 2021) speaks generally of "limitations and potential pitfalls" — specific
failure modes are body-only and NOT quoted as abstract; the citable explicit-limitation quote comes
from the scVelo abstract instead.

---

## Section 1 — The idea: direction from a still image (KI / SciLifeLab origin)

### RNA velocity — the origin — VERIFIED
- La Manno, G. … Linnarsson, S. & Kharchenko, P.V. "RNA velocity of single cells." *Nature*
  **560**(7719):494–498, 2018. DOI: 10.1038/s41586-018-0414-6 (confirmed ‑6, NOT ‑5).
- **Senior/corresponding: Sten Linnarsson — Karolinska Institutet, Stockholm, Sweden (+ SciLifeLab,
  Solna); email sten.linnarsson@ki.se** — and Peter V. Kharchenko (Harvard Medical School). Local
  Stockholm/SciLifeLab tie confirmed.
- ABSTRACT-VERIFIED (verbatim): "**RNA abundance is a powerful indicator of the state of individual
  cells**"; "**RNA velocity—the time derivative of the gene expression state—can be directly estimated
  by distinguishing between unspliced and spliced mRNAs in common single-cell RNA sequencing
  protocols**"; "**RNA velocity is a high-dimensional vector that predicts the future state of
  individual cells on a timescale of hours**"; validated in "**the neural crest lineage**" and
  "**the developing mouse hippocampus.**"

## Section 2 — Making it robust, then deep

### scVelo — dynamical model, transient states — VERIFIED
- Bergen, V., Lange, M., Peidli, S., Wolf, F.A. & Theis, F.J. "Generalizing RNA velocity to transient
  cell states through dynamical modeling." *Nature Biotechnology* **38**(12):1408–1414, 2020.
  DOI: 10.1038/s41587-020-0591-3. Senior author Fabian J. Theis (Helmholtz Munich).
- ABSTRACT-VERIFIED (verbatim): "**errors in velocity estimates arise if the central assumptions of a
  common splicing rate and the observation of the full splicing dynamics with steady-state mRNA levels
  are violated**"; "**scVelo, a method that overcomes these limitations by solving the full
  transcriptional dynamics of splicing kinetics using a likelihood-based dynamical model**"; "**This
  generalizes RNA velocity to systems with transient cell states, which are common in development and
  in response to perturbations.**"

### CellRank — fate mapping combining trajectory + velocity + uncertainty — VERIFIED
- Lange, M. … Pe'er, D. & Theis, F.J. "CellRank for directed single-cell fate mapping." *Nature
  Methods* **19**:159–170, 2022. DOI: 10.1038/s41592-021-01346-6. First author Marius Lange; senior
  Fabian Theis & Dana Pe'er. Tool: https://cellrank.org
- ABSTRACT-VERIFIED (verbatim): "**Computational trajectory inference enables the reconstruction of
  cell state dynamics from single-cell RNA sequencing experiments**"; "**CellRank … for single-cell
  fate mapping in diverse scenarios, including regeneration, reprogramming and disease, for which
  direction is unknown**"; "**combines the robustness of trajectory inference with directional
  information from RNA velocity, taking into account the gradual and stochastic nature of cellular
  fate decisions, as well as uncertainty in velocity vectors.**"

### veloVI — deep generative velocity + uncertainty (2024) — VERIFIED
- Gayoso, A. … Theis, F.J. & Yosef, N. "Deep generative modeling of transcriptional dynamics for RNA
  velocity analysis in single cells." *Nature Methods*, 2024. DOI: 10.1038/s41592-023-01994-w.
  Senior authors Fabian Theis & Nir Yosef.
- ABSTRACT-VERIFIED (verbatim): "**veloVI (velocity variational inference), a deep generative modeling
  framework for estimating RNA velocity**"; "**veloVI learns a gene-specific dynamical model of RNA
  metabolism and provides a transcriptome-wide quantification of velocity uncertainty**"; "**veloVI's
  posterior velocity uncertainty can be used to assess whether velocity analysis is appropriate for a
  given dataset.**"

### CellRank 2 — scale + multiview + metabolic labeling (2024) — VERIFIED
- Weiler, P., Lange, M., Klein, M., Pe'er, D. & Theis, F. "CellRank 2: unified fate mapping in
  multiview single-cell data." *Nature Methods*, 2024. DOI: 10.1038/s41592-024-02303-9.
- ABSTRACT-VERIFIED (verbatim): "**a versatile and scalable framework to study cellular fate using
  multiview single-cell data of up to millions of cells in a unified fashion**"; "**we enable
  estimating cell-specific transcription and degradation rates from metabolic-labeling data**."

## Section 3 — The honest frontier + lab hook

### The critique (caveat anchor) — VERIFIED
- Bergen, V., Soldatov, R.A., Kharchenko, P.V. & Theis, F.J. "RNA velocity—current challenges and
  future perspectives." *Molecular Systems Biology* **17**(8):e10282, 2021. DOI: 10.15252/msb.202110282.
- ABSTRACT-VERIFIED (verbatim): "**RNA velocity has enabled the recovery of directed dynamic
  information from single-cell transcriptomics by connecting measurements to the underlying kinetics
  of gene expression**"; "**discuss various examples illustrating limitations and potential pitfalls,
  and provide guidance on how the ensuing challenges may be addressed.**" (Specific failure modes are
  body-only — NOT quoted as abstract.)

### Frontier + lab hook
- Frontier: velocity is a *hypothesis about direction* — it rests on splicing-kinetics assumptions
  that can break (scVelo abstract); the field's own review flags "limitations and potential pitfalls"
  (Bergen 2021); the 2024 deep-learning turn's headline contribution is literally *knowing when to
  trust it* — veloVI quantifies "whether velocity analysis is appropriate for a given dataset." The
  prove-it discipline (/post/newsletter-2026-07-27/): a velocity arrow earns trust only when the model
  says its own uncertainty is low and orthogonal evidence agrees.
- Two ways to read the arrow of time in a cell — pairs with Aug 25 (/post/newsletter-2026-08-25/):
  imaging tracking WATCHES the cell move; RNA velocity INFERS the move from a single snapshot. Same
  question (where is this cell going next?), opposite data.
- Lab hook: cell-state dynamics is the raw substrate of a virtual cell — the Human Cell Simulator
  (/project/human-cell-simulator/) and the perturbation/virtual-cell horizon (/post/newsletter-2026-08-15/);
  metabolic-labeling rates (CellRank 2) are dynamics you can actually *measure*, the ground truth an
  autonomous lab (/project/self-driving-microscope/, /project/reef-imaging-farm/, /project/agent-lens/)
  could generate at scale. Open/callable tools (cellrank.org, scVelo) = the BioEngine
  (/project/bioengine/) / open-model-serving ethos.
