# Newsletter sources — 2026-08-08 (fetched UTC 2026-08-08T03:00:15Z)

Theme: **The microscope that chooses its moment — smart / self-driving microscopy,
AI in the acquisition loop.** Live imaging is destructive: every frame spends photons
and phototoxicity, so you cannot watch everything at high resolution all the time. The
intelligence that matters is *when* to spend the budget. A microscope now runs a model
**on-the-fly, at the instrument**, watches gently, and switches to the slow/expensive
modality only at the instant something happens — and, at the frontier, closes the loop
to *act* on the cell and drive it to a target state. The field matured in 2025-26: it
grew a taxonomy (quality-, event-, target-, information-, outcome-driven), landed
peer-reviewed self-driving instruments, and named its honest limit (still
semi-autonomous, needs prior knowledge of what to watch for). A lab-core story: this is
exactly the [self-driving microscope](/project/self-driving-microscope/) /
[Agent-Lens](/project/agent-lens/) / [REEF](/project/reef-imaging-farm/) micro-loop —
the millisecond decision loop *under* the macro agentic loop — and the lab co-authored
the field's deep-learning-for-microscopy roadmap.

## Provenance / method
- Web research (WebSearch + WebFetch). Two load-bearing anchors **primary-fetched**:
  the **outcome-driven / closed-loop optogenetics** paper (via PMC, Nat Commun) with
  verbatim quotes + numbers, and the **self-driving Brillouin / protein-aggregation**
  paper (PMC12289965 + press) with verbatim quotes + accuracies.
- **X/Twitter sweep skipped:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
  **and** `scripts/lab-x.py discover` both return **HTTP 402 Insufficient credits**
  (getxapi out of credits **~5 weeks**); `search` gated; x-breaking stays disabled.
  Flagged to Wei for a top-up.
- **De-dup / variety (important):** smart / self-driving *acquisition* — AI controlling
  the microscope in real time (what/when/how to image) — has **not** been a theme in this
  run. It is distinct from the recent imaging digests, which are all *post-acquisition* or
  *macro-loop*:
  - Aug 6 virtual staining = *compute* a molecular channel after the image is taken.
  - Aug 4 image-based profiling = *read* a phenotype from an existing image.
  - Jul 31 "The Agent Decides" = the *macro* reasoning loop (an agent choosing which
    experiment to run), not the instrument's real-time acquisition control.
  - Jul 21 microscopy VLMs = *language/reports* about images.
  - Jul 19 segmentation = *find where* cells are.
  This digest is the **micro-loop**: closed-loop control *at the instrument*, in
  milliseconds — deciding when to spend the imaging budget and, at the frontier, acting on
  the sample. Clear separation. Clear to run.
- **Verification discipline:** both anchors are **peer-reviewed** (*Nature Communications*,
  2025) with exact DOIs and primary-fetched. The 2026 taxonomy review (*npj Imaging*) and
  the *Small Methods* 2026 review are peer-reviewed, cited for framing/definition (primary
  direct-fetch blocked by Nature/Wiley auth walls; grounded via search excerpts, no
  fabricated numbers). Mahecic et al. (*Nature Methods* 2022) is the well-established
  event-driven origin. Roboscope (bioRxiv 2024) is a **preprint**, labelled as such,
  cited for the genericity direction only.

## Item 1 — Capability: watch gently, strike fast (ANCHOR — self-driving Brillouin, peer-reviewed, primary-fetched)
- **The origin (event-driven acquisition):** Dora Mahecic et al., "Event-driven
  acquisition for content-enriched microscopy," **Nature Methods (2022)**. On-the-fly CNN
  predicts the onset of a division event and triggers a switch from gentle monitoring to
  high-spatiotemporal-resolution imaging only for the event's duration — reported
  **~5x reduction in photobleaching**. Established the two-mode pattern: Mode 1 (gentle,
  continuous, low-damage watch) -> detect -> Mode 2 (high-res burst) -> return.
- **Current flagship (fetched, PMC12289965):** Khalid A. Ibrahim, Camille Cathala, Carlo
  Bevilacqua, Lely Feletti, Robert Prevedel, Hilal A. Lashuel, Aleksandra Radenovic
  (EPFL + EMBL), **"Self-driving microscopy detects the onset of protein aggregation and
  enables intelligent Brillouin imaging," Nature Communications (2025)**, DOI
  10.1038/s41467-025-60912-0 (published 24 Jul 2025; PMC12289965).
- Verified facts / verbatim:
  - **The problem:** Brillouin microscopy reveals biomechanical properties (elasticity)
    but is **slow**, so it cannot casually chase a fast, unpredictable process like protein
    aggregation. You must know *when* to point it.
  - **The unlock:** "a self-driving microscope that uses deep learning to predict the onset
    of aggregation from a **single fluorescence image** of soluble protein, achieving
    **91% accuracy**," and triggers "optimized multimodal imaging when aggregation is
    imminent, enabling intelligent Brillouin microscopy of this dynamic biomechanical
    process." A real-time classifier detects mature aggregates at **97% accuracy from
    brightfield** and switches modality — "exclusively label-free and non-invasive."
  - First-author framing (Khalid A. Ibrahim): "This is the first publication that shows the
    impressive potential for self-driving systems to incorporate label-free microscopy
    methods, which should allow more biologists to adopt rapidly evolving smart microscopy
    techniques."

## Item 2 — The field grows a taxonomy + chases genericity (framing, peer-reviewed + preprint)
- **Taxonomy (npj Imaging 2026 review):** "Smart microscopy: adaptive microscope control
  to improve the way we see life," **npj Imaging (2026)**, s44303-026-00145-y. Classifies
  smart-microscopy approaches by experimental goal — **"quality-, event-, target-,
  information- or outcome-driven"** — and discusses the corresponding analysis + control
  strategies, plus "the growing role of community-driven efforts in making smart microscopy
  more accessible." (Direct fetch blocked by Nature auth; grounded via search excerpt.)
- **Super-resolution angle (Small Methods 2026 review):** L. Ward et al., "Self-Driving
  Microscopes: AI Meets Super-Resolution Microscopy," **Small Methods (2026)**, DOI
  10.1002/smtd.202401757 — reviews ML that automates super-resolution microscopy,
  "enabling the microscope to autonomously make decisions on **what, when, and how to
  image**." (Wiley auth wall; grounded via search excerpt.)
- **The honest limit (genericity):** current event-driven systems are "so far... only
  semi-autonomous, requiring prior knowledge of which sample features to monitor," and are
  "heavily tailored to their attached microscopy setup and biological application." The
  **Roboscope** (bioRxiv 2024, "Smart and Fast Microscopy for Generic Event-Driven
  Acquisition") targets exactly this — a hardware-agnostic, generic event-of-interest
  detector that "keeps the training set small." (Preprint — direction, not load-bearing.)

## Item 3 — From watching to acting: outcome-driven closed loop + the check (ANCHOR — peer-reviewed, primary-fetched)
- **Source (fetched):** Josiah B. Passmore, Alfredo Rates, Jakob Schröder, ... Carlas S.
  Smith, Ihor Smal, **Lukas C. Kapitein** (Utrecht University), "Closed-loop optogenetic
  control of cell biology enables outcome-driven microscopy," **Nature Communications
  (2025)**, DOI 10.1038/s41467-025-67848-5 (open access, CC BY 4.0; code
  UU-cellbiology/UU_SmartMicroscopy).
- Verified facts / verbatim:
  - **The paradigm shift:** beyond passive observation — "'outcome-driven' microscopy, a
    framework combining smart microscopy with optogenetics to control cell biological
    processes," aiming to "actively control biological processes themselves to achieve
    user-defined outcomes," using "optogenetics and real-time feedback to achieve automated
    spatiotemporal control of subcellular cell biology."
  - **Validated on two systems:** (1) **cell migration** — optogenetically guided single
    and multiple HT1080 cells along predefined paths (RAC1 effector TIAM1; SAM-based
    segmentation; trajectory-tracking controller) for **>10 hours**, keeping the centroid
    within **~2.5 um** of the target path, with active collision avoidance between cells;
    (2) **nucleocytoplasmic transport** — controlling nuclear/cytosolic protein levels
    (LEXY export system; gain-scheduled PID) to setpoints with **error consistently under
    10%**; seven cells of varying expression brought to the same nuclear setpoint, each
    needing distinct irradiance.
- **The check (why the discipline still applies):** a microscope that *acts* on a live
  sample is a controller in a feedback loop — it can drive the cell to a wrong state as
  confidently as a right one. The same "verify the readout / trust is something you build
  in" throughline the lab keeps returning to (hallucination-checked stains; models that
  show their work) applies to the control loop, not just the image.

## Lab connections (for "why it matters")
- **This *is* the lab's instrument.** The [self-driving microscope](/project/self-driving-microscope/),
  [Agent-Lens](/project/agent-lens/) and the [REEF imaging farm](/project/reef-imaging-farm/)
  are built on exactly this micro-loop: watch live cells gently, decide in real time when to
  spend the imaging budget, and act. Event-driven acquisition is how you keep cells alive and
  still catch the rare, fast moment.
- **The micro-loop under the macro-loop.** Jul 31 ("The Agent Decides") was the *macro*
  agentic loop — an agent choosing which experiment to run. This is the *micro* loop, at the
  instrument, in milliseconds: what/when/how to image. A self-driving lab needs both, nested.
- **Dye-free + event-driven compound.** Aug 6 virtual staining computes molecular channels
  without dye; smart acquisition decides *when* to grab them. Together: watch live cells
  longer, gentler, and only spend resolution at the moment that matters — the readout a
  [virtual cell](/project/human-cell-simulator/) needs is the *right* data at the *right*
  instant, not merely more data.
- **Open models at the microscope.** UU_SmartMicroscopy ships its code open; this is the
  [BioImage Model Zoo](/project/bioimage-model-zoo/) / [ImJoy](/project/imjoy/) /
  [BioEngine](/project/bioengine/) ethos — the model that drives the instrument, shared and
  runnable, not locked to one rig (the Roboscope genericity problem).
- **The lab is on the record here.** The lab co-authored **"Roadmap on deep learning for
  microscopy"** (Volpe, Wählby, Tian, **Wei Ouyang**, et al., *Journal of Physics: Photonics*
  8, 012501, 2026; DOI 10.1088/2515-7647/ae0fd1) — mapping DL across microscopy; smart /
  self-driving acquisition is a live frontier within that map.
- **The throughline: a system that acts must be trustworthy.** [Prove it](/post/newsletter-2026-07-28/);
  [show your work](/post/newsletter-2026-08-02/); [check the generated readout](/post/newsletter-2026-08-06/).
  An acquisition loop that acts on a live sample is held to the same bar.

## De-dup check
- Recent digests: Aug 7 proteomics; Aug 6 virtual staining; Aug 5 federated/privacy; Aug 4
  image-based profiling; Aug 3 small-molecule design; Aug 2 virtual cell; Aug 1 pathology;
  Jul 31 self-driving *labs* (macro agentic loop); Jul 30 mRNA; Jul 29 cryo-ET; Jul 28
  genomic-FM eval; Jul 26 spatial; Jul 21 microscopy VLMs; Jul 19 segmentation. **Smart /
  self-driving *acquisition* — AI controlling the microscope in real time — has not been a
  theme.** Distinct from Jul 31 (macro experiment-choosing loop), Aug 6 (post-acquisition
  channel synthesis) and Aug 4 (reading a profile from an existing image): this is real-time
  closed-loop *acquisition control at the instrument*. Clear to run.
