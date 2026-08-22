# Newsletter sources — August 22, 2026

**Theme:** Deep learning for microscopy image restoration — denoising, deconvolution, super-resolution
("Seeing More With Less Light"). The lab's bioimaging core (AI4Life / BioImage Model Zoo / ImJoy).
Distinct from virtual staining (Aug 6), smart microscopy (Aug 8), segmentation FMs (Aug 16),
cryo-ET/visual proteomics (Jul 29) — this is about *recovering signal*, and the phototoxicity tradeoff
that ties it to live-cell imaging and the self-driving microscope (Aug 21).

**X/Twitter sweep:** SKIPPED (getxapi out of credits — HTTP 402; 13th consecutive skip). Grok-based
replacement wired, awaiting xAI credits.

All anchors verified by two parallel general-purpose subagents against Crossref / Europe PMC / PubMed /
Semantic Scholar / arXiv, with verbatim abstracts obtained. Only abstract-verified numbers/quotes are used
in the post; body-only details flagged and NOT quoted as abstract.

---

## Section 1 — Restoring signal from almost nothing (denoising / restoration)

### CARE (content-aware image restoration) — VERIFIED
- Weigert, M. … Myers, E.W. "Content-aware image restoration: pushing the limits of fluorescence microscopy."
  *Nature Methods* **15**(12):1090–1097, 2018. DOI: 10.1038/s41592-018-0216-7 · PMID: 30478326 · Research article.
- First author Martin Weigert; **senior/last author Eugene W. Myers** (NOT Jug — Florian Jug is co-senior #20,
  Loic Royer #19, but Myers is last author). Correction to earlier brief.
- ABSTRACT-VERIFIED (verbatim): images can be "restored even if **60-fold fewer photons** are used during
  acquisition"; "near isotropic resolution can be achieved with up to **tenfold under-sampling** along the axial
  direction"; "tubular and granular structures smaller than the diffraction limit can be resolved at
  **20-times-higher frame rates**"; demonstrated on "eight concrete examples"; open source in "Python, FIJI, and
  KNIME"; trade-offs among "imaging speed, spatial resolution, light exposure, and imaging depth." All three
  fold-numbers ARE in the abstract — safe to quote.

### Noise2Void — VERIFIED
- Krull, A., Buchholz, T-O., Jug, F. "Noise2Void – Learning Denoising from Single Noisy Images." *2019 IEEE/CVF
  CVPR*, pp. 2124–2132. DOI: 10.1109/CVPR.2019.00223 · arXiv 1811.10980 · Peer-reviewed conference paper.
- Krull first author; Jug senior/last.
- ABSTRACT-VERIFIED: N2V "does not require noisy image pairs, nor clean target images"; "allows us to train
  directly on the body of data to be denoised"; motivated by biomedical data where "acquisition of training
  targets, clean or noisy, is frequently not possible."
- IMPORTANT (do NOT overstate): the abstract explicitly says N2V "cannot be expected to outperform methods that
  have more information," and performance "drops in moderation." Present it as a principled tradeoff, not a
  benchmark winner. Specific PSNR/dataset numbers are body-only.

## Section 2 — Beyond the diffraction limit (super-resolution / cross-modality)

### Deep-STORM — VERIFIED
- Nehme, E., Weiss, L.E., Michaeli, T., Shechtman, Y. "Deep-STORM: super-resolution single-molecule microscopy
  by deep learning." *Optica* **5**(4):458(–464), 2018. DOI: 10.1364/OPTICA.5.000458 · Peer-reviewed (no PMID; Optica).
- Nehme first author; Shechtman senior/last.
- ABSTRACT-VERIFIED: "ultra-fast, precise, **parameter-free**"; "state-of-the-art resolution under challenging
  signal-to-noise conditions and **high emitter densities**"; "**significantly faster** than existing approaches";
  trainable on simulated or experimental data; "no prior information on the shape of the underlying structure is
  required."

### Cross-modality super-resolution (Ozcan lab) — VERIFIED (with brief correction)
- Wang, H. … Ozcan, A. "Deep learning enables cross-modality super-resolution in fluorescence microscopy."
  *Nature Methods* **16**(1):103–110, 2019 (online Dec 2018). DOI: 10.1038/s41592-018-0239-0 · PMID: 30559434 · Research article.
- Wang first author; Ozcan senior/last.
- ABSTRACT-VERIFIED: a GAN transforms diffraction-limited inputs into super-resolved outputs — **confocal →
  STED-matched resolution**; TIRF → TIRF-SIM-matched; and improves **low-numerical-aperture widefield to
  high-numerical-aperture widefield resolution**; no PSF estimation / numerical model required; output "without
  any iterations or parameter search."
- CORRECTION to earlier brief: it is NOT "widefield → confocal-like." The confocal transform targets STED;
  the widefield transform is low-NA → high-NA widefield.

### DFCAN / DFGAN (recent SOTA) — VERIFIED
- Qiao, C. … Li, Dong. "Evaluation and development of deep neural networks for image super-resolution in optical
  microscopy." *Nature Methods* **18**(2):194–202, 2021. DOI: 10.1038/s41592-020-01048-5 · PMID: 33479522 · Research article.
- Qiao first author; **Dong Li senior** (co-corresponding with Qionghai Dai). Correction: "Tao Xu" is NOT an author.
- ABSTRACT-VERIFIED: provides an extensive LR–SR image-pair dataset via multimodality SIM; introduces the
  **deep Fourier channel attention network (DFCAN)** that exploits frequency-content differences; enables robust
  SIM-quality reconstruction under low SNR; "**DFCAN achieves comparable image quality to SIM over a tenfold
  longer duration in multicolor live-cell imaging**" (the 10× longevity figure is abstract-verified).

## Section 3 — The honest frontier (hallucination) + lab hook

### Belthangady & Royer review — VERIFIED
- Belthangady, C. & Royer, L.A. "Applications, promises, and pitfalls of deep learning for fluorescence image
  reconstruction." *Nature Methods* **16**(12):1215–1225, 2019. DOI: 10.1038/s41592-019-0458-z · PMID: 31285623 · REVIEW.
- ABSTRACT-VERIFIED (verbatim): "Despite its successes, deep learning also poses substantial challenges and has
  limits"; "We discuss key questions, including how to obtain training data, whether **discovery of unknown
  structures is possible**, and the danger of **inferring unsubstantiated image details**."
- Use "inferring unsubstantiated image details" and "whether discovery of unknown structures is possible" as the
  abstract-verified caution. The words "hallucinate," "artifacts," and "need for validation" are BODY-ONLY —
  present those as paraphrase, not abstract quotes.

## Lab connections
- AI4Life (/project/ai4life/), BioImage Model Zoo (/project/bioimage-model-zoo/), ImJoy (/project/imjoy/) —
  open, standard-format, callable restoration models that anyone can run AND validate.
- Self-driving microscope (/project/self-driving-microscope/), Agent-Lens (/project/agent-lens/),
  BioEngine (/project/bioengine/) — less light = gentler, longer live imaging = enabler of autonomy.
- Aug 21 self-driving labs (/post/newsletter-2026-08-21/); Aug 8 smart microscopy (/post/newsletter-2026-08-08/);
  Aug 6 virtual staining (/post/newsletter-2026-08-06/); prove-it discipline (/post/newsletter-2026-07-27/).
