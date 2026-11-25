# Newsletter sources — 2026-11-25

Run: nightly `lab-newsletter` (prod mode). All items below were fetched and read
during this run; figures in the post are copied from these sources.

**Note on the X sweep:** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`,
`scripts/lab-x.py search` and `scripts/lab-x.py discover` all returned
`HTTP 402 'Insufficient credits'` — the getxapi account behind `X_API_KEY` is out of
credits (third consecutive issue affected: 2026-11-22, 2026-11-24, 2026-11-25).
No X signal this run and **no new accounts added** to `x-accounts.md`. This issue is
built from first-party web, GitHub API, PyPI API, CISA KEV feed, bioRxiv, Nature and
press sources only.

---

## Lead item — agent-discovered zero-day in bioimaging software

1. **Attackers' AI Agents Found a Zero-Day in Medical-Imaging Software** — The Hacker News, Ravie Lakshmanan, 2026-11-21.
   https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html
   Why relevant: autonomous pentest agents (Cairn framework) found and exploited a 0-day in
   MONAI Label — open-source *bioimage/medical-imaging annotation server* software, i.e. the
   same software class as the lab's model-serving stack. Reporting based on an Amazon Threat
   Intelligence / AWS Security Blog report (2026-11-20). China-nexus attribution at *moderate
   confidence* only; Amazon's reconstruction is not independently verified.
   Fetched 2026-11-25.

2. **CISA Known Exploited Vulnerabilities catalog** (machine-readable feed, fetched directly) — catalog `dateReleased` 2026-11-24T17:47:46Z, 1,795 entries.
   https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
   Verbatim entry fields for **CVE-2026-133968**: vendorProject "Project MONAI", product
   "MONAI Label", `dateAdded` **2026-11-23**, `dueDate` **2026-11-26**, cwes `["CWE-24"]`,
   `forensicTriage: Yes`, `knownRansomwareCampaignUse: Unknown`; requiredAction cites BOD 26-04.
   (Same day CISA also added CVE-2026-134624, N-able MailAssure SSRF — not lab-relevant.)
   Fetched 2026-11-25. **Primary source — this is the strongest fact in the issue.**

3. **GHSA-qc22-rmgc-vg94** — MONAI Label path traversal in datastore upload endpoints.
   https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94
   Affected `<= 0.8.5`, patched **0.8.6**, CWE-22, severity critical, published 2026-11-18 by
   ericspod, fix in PR #1915. `PUT /datastore/image` took an unvalidated caller-supplied image
   ID, joined it to the datastore dir and `shutil.copy()`'d into it. Auth off by default
   (`MONAI_LABEL_AUTH_ENABLE=False`). Credits: garciadias (reporter), originally reported by
   `@aws-sec-vdp`. Fetched 2026-11-25.

4. **MONAI Label GitHub releases** (GitHub API, fetched directly): `/repos/Project-MONAI/MONAILabel/releases`
   - **0.8.7** published **2026-11-25T03:32:03Z** — "This is a security release. All MONAI Label
     server deployments should upgrade." Fixes **GHSA-j5c7-p3x5-gw2x** (critical): task requests
     (`/train`, `/scoring`, `/batch/infer`) accepted a client-supplied `bundle_path` that was
     added to the `PYTHONPATH` of the task process → RCE; path now comes only from the registered
     bundle trainer; **affects 0.6.0–0.8.6**. Also GHSA-cgpr-79vx-xr5x (medium, DICOMweb datastore
     path confinement, affects ≤ 0.8.6) and GHSA-5c65-q9f6-h62q (high, session upload traversal,
     fixed in 0.8.6). Reporter credits: @xuxiaoyuspallow, @baeseungwon1010, @b-abderrahmane.
   - **0.8.6** published 2026-11-22T01:29:24Z — CVE-2026-133968 + session-upload traversal (PR #1942).
   https://github.com/Project-MONAI/MONAILabel/releases
   Fetched 2026-11-25.

5. **PyPI `monailabel` JSON API** (fetched directly) — confirms upload timestamps independently of GitHub:
   0.8.5 → 2024-11-25T23:22:11Z · **0.8.6 → 2026-11-22T01:27:24Z** · **0.8.7 → 2026-11-25T03:17:29Z** (latest).
   https://pypi.org/pypi/monailabel/json
   Note: this corrects The Hacker News' 2026-11-21 statement that no patched release existed —
   true when written, superseded two days later.

## Verification & provenance for agent-run science

6. **An auditable harness for biomolecular dynamics simulations by AI agents** (MDClaw) — bioRxiv, posted 2026-11-11, doi 10.64898/2026.11.09.765490, CC-BY-NC-ND 4.0.
   https://www.biorxiv.org/content/10.64898/2026.11.09.765490v1
   Matsunaga, Wu, Zhang, Kumari, Enomoto, Homma, Hatakeyama, Shinobu — RIKEN R-CCS, Saitama
   University, University of Osaka, RIKEN BDR. Validating tools + a DAG inspect each stage before
   execution and log every stage, so trajectories trace back to inputs and settings. Benchmarked
   on MDDataBench; **four open-weight models passed all three runs on 81–100% of 31 test systems**;
   ablation without the DAG surfaced **11 runs scored as successful that had skipped minimization
   or equilibration, or simulated a different structure**. COI: Y.M. advises Epsilon Molecular
   Engineering. Funding: JST, RIKEN TRIP. Un-reviewed preprint. Fetched 2026-11-25.

7. **An AI agent guides a pipeline for selective protein interaction inhibitors from discovery across targets to preclinical evaluation** (Bivexia) — bioRxiv, posted **2026-11-24**, doi 10.64898/2026.11.23.768516.
   https://www.biorxiv.org/content/10.64898/2026.11.23.768516v1
   Somaya Abdel-Rahman & Moustafa Gabr, Columbia University Irving Medical Center. Agent's
   decision rules fixed in advance; every prospective pick **cryptographically committed before
   testing**. Reported: nominated compound binds LAG-3 at nanomolar affinity, blocks LAG-3↔tau and
   LAG-3↔amyloid-β while sparing MHC class II and FGL1; reduced tau and amyloid-β burden in
   independent cohorts across two mouse models; same rules applied to other targets gave
   **3/9 hits on PrPᶜ and 2/9 on LRP1, none in random controls**. No competing interests declared.
   Un-reviewed preprint. Fetched 2026-11-25.

8. **Alpöge's proof of the Riemann hypothesis** — Wikipedia (current-event article, last edit 2026-11-25), used as a timeline aggregator; the underlying facts cited below.
   https://en.wikipedia.org/wiki/Alp%C3%B6ge%27s_proof_of_the_Riemann_hypothesis
   Levent Alpöge (mathematician at Anthropic) released a formal proof **2026-11-20** plus a
   four-page "Remark"; Lean development 2026-10-06 → 2026-11-16; **~17 million lines of Lean**;
   Lean FRO + Mathlib Initiative endorsement **2026-11-21** ("We have full confidence that
   Alpöge's proof of the Riemann Hypothesis is correct"), resting on four criteria (correct
   statement from vetted Mathlib definitions, compilation to an export file, no redefinition of
   the statement, clears every known proof checker). No human-readable prose proof as of
   2026-11-24. Independent Lean checks: Andrew Sutherland (most tests passed, one still running
   as of 2026-11-23), Michael Rubinstein. Named criticism: Andrew Granville (clarity of the
   sketch; release timing one day after Anthropic's IPO), Maksym Radziwiłł (a formalization
   lacks human comprehension); Terence Tao's preliminary read: "appears to use the full power of
   modern developments on the Langlands program and arithmetic geometry". Alpöge on X: the
   250,000-page prose figure was a joke (clarified 2026-11-23). Clay Mathematics Institute still
   lists the problem as unsolved. Fetched 2026-11-25.
   Corroborating press: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-mathematician-claims-to-have-solved-167-year-old-math-problem-with-claude-riemann-hypothesis-proof-allegedly-discovered-but-remains-unconfirmed
   · https://phys.org/news/2026-11-anthropic-claude-math-greatest-riddle.html
   · https://siliconangle.com/2026/11/20/anthropic-researcher-claims-to-have-proven-riemann-hypothesis-using-claude/

## Virtual cell — the horizon

9. **Scientists Are Pursuing the Dream of a 'Virtual Cell'** — TIME, Veronique Greenwood, 2026-11-20.
   https://time.com/article/2026/11/20/scientists-are-pursuing-the-dream-of-a-virtual-cell/
   Arc Institute announced Virtual Cell Challenge winners **2026-11-19**. ~1,000 teams in final
   judging (≈3× last year), >1,600 models submitted in earlier rounds. Prizes: $100k Illumina
   (proprietary Billion Cell Atlas), $50k FlowState (Khodaveisi & Bagheri, public data only),
   $25k Xaira Therapeutics (proprietary data). Hani Goodarzi (Arc / UCSF, challenge lead) on a
   reliable in-silico replacement: "the north star for us, for at least this phase"; on
   proprietary-data advantage: "It shows". Shana Kelley (Northwestern / CZ Biohub): cells hold
   "billions of molecules inside of them, and thousands of different processes", training needs
   in the "billions, maybe trillions, of datasets", ~10× more data within 18 months. Eyal
   Ben David (Illumina, Billion Cell Atlas): "Biological data has to be made. It's not found."
   Top-three models captured broad trends but faltered on cell-type-specific responses.
   CZ Biohub Virtual Biology Initiative launched April 2026; NIH Bio Genesis Mission July 2026.
   Fetched 2026-11-25.
   Related, same news cycle: https://www.nytimes.com/2026/11/18/science/ai-virtual-human-cells.html
   · https://arcinstitute.org/virtual-cell-initiative · https://virtualcellchallenge.org/

## Imaging & omics methods

10. **Space-map: 3D single-cell atlas reconstruction from serial sections** — *Nature Methods*, published online 2026-11-19, doi 10.1038/s41592-026-03310-8, PMID 43058204, Open Access.
    https://www.nature.com/articles/s41592-026-03310-8
    Rongduo Han, Cihan Ruan, Michael P. Snyder et al. Multi-scale feature matching (LoFTR deep +
    SIFT classical) plus LDDMM for global reconstruction preserving local micro-anatomy; outputs
    per-layer Imaris-ready TIFF stacks, aligned coordinate tables, cell-type-coloured 3D previews.
    HuBMAP tissue mapping center; human intestine serial sections — 20 serial sections of one colon
    polyp → ~1.9M cells in ~2 min on a laptop; also serial Xenium transcriptomics ~2.9M cells.
    Best overall alignment accuracy among tested methods; reduced cumulative distortion.
    Code: https://github.com/czhu/space-map · Research Briefing: doi 10.1038/s41592-026-03309-1
    Fetched 2026-11-25.

## Checked, not used this issue

- **Where single-cell foundation models help** (bioRxiv v3, 2026-11-19) — FM embeddings did not beat
  principal components within species; in-silico knockouts met the predefined criterion in none of
  46 tests. https://www.biorxiv.org/content/10.64898/2026.11.03.763968v3 — overlaps heavily with the
  virtual-knock-out item already covered in the 2026-11-24 issue; held for a future digest.
- **MicroBioAgent** (bioRxiv 2026-11-17) https://www.biorxiv.org/content/10.64898/2026.11.17.767465v1 — noted, thinner than the items above.
- **Alpha Cell postdoc in AI modelling of cellular dynamics** (Avlant Nilsson, SciLifeLab/KI; LinkedIn, 2026-11-12) — ecosystem note, not news enough for an item.
- Lab repo activity checked via GitHub API: `aicell-lab/bioengine` last push 2026-11-24T21:23Z (no
  tagged release); `bioimage-io/core-bioimage-io-python`, `bioimage-io/collection`, `bioimage-io/bioimage.io`
  all pushed 2026-11-24 (no releases). Nothing announceable yet.
