# Sources — catch-up digest, 2026-11-12

Covers the gap 2026-09-30 → 2026-11-12 (the nightly pipeline was down; see note below).
All items fetched and verified 2026-11-12.

| # | Title | URL | Why relevant | Fetched |
|---|---|---|---|---|
| 1 | Biohub — "AI-ready biological data: $1.8 billion global commitment" (Oct 7, 2026) | https://biohub.org/news/virtual-biology-initiative-expansion/ | Largest coordinated commitment to AI-ready biological data; directly the virtual-cell thesis the lab works toward | 2026-11-12 |
| 2 | Arc Institute — "The 2026 Virtual Cell Challenge" (Aug 20, 2026) | https://arcinstitute.org/news/virtual-cell-challenge-2026 | Zero-shot CRISPRi perturbation prediction across six cell lines; final submissions closed Nov 5, winners mid-to-late Nov | 2026-11-12 |
| 3 | Virtual Cell Challenge — timeline/evaluation pages | https://virtualcellchallenge.org/evaluation | Final phase Oct 22 → Nov 5 2026, results late Nov (main page is JS-rendered; dates taken from Arc announcement + evaluation page snippet) | 2026-11-12 |
| 4 | Danaher — "Danaher Accelerates Life Sciences Research with New AI-powered Autonomous Lab" (Oct 7, 2026) | https://investors.danaher.com/2026-10-07-Danaher-Accelerates-Life-Sciences-Research-with-New-AI-powered-Autonomous-Lab | Industrial design-make-test-learn autonomous lab; the self-driving-lab pattern behind REEF / self-driving microscope | 2026-11-12 |
| 5 | Zhao, Fang, Mao et al., "The rise of agentic AI in drug discovery from static tools to autonomous virtual scientists", npj Drug Discovery (Oct 12, 2026), DOI 10.1038/s44386-026-00075-0 | https://doi.org/10.1038/s44386-026-00075-0 | Review of the shift from static tools to autonomous agents; metadata verified via Crossref (article itself paywalled/auth-gated) | 2026-11-12 |
| 6 | SciLifeLab — "From tropical ecology to human health: researchers meet at DDLS Annual Conference" (Nov 10, 2026) | https://www.scilifelab.se/news/from-tropical-ecology-to-human-health-researchers-meet-at-ddls-annual-conference/ | The lab's own national programme; 5th edition, 300+ researchers, 43 of 50 Fellows recruited | 2026-11-12 |
| 7 | EGI/RI-SCALE webinar — "Making bioimaging data discoverable, accessible and understandable with AI" (Nov 18, 2026, 14:00 CET) | https://www.egi.eu/event/webinar-ri-scale-making-bioimaging-data-discoverable-accessible-and-understandable-with-ai | **Lab item**: Joanna Hård (AICell Lab) speaks alongside Teresa Zulueta-Coarasa (EMBL-EBI); Wei Ouyang listed in the event header | 2026-11-12 |
| 8 | KTH — Postdoc in Agentic AI for Spatial Biology of the Human Gut, Koplev Lab (Ref. PA-2026-3723), deadline Nov 29 2026 | https://www.biotecnika.com/agentic-ai-postdoc-kth-scilifelab-sweden/ | **Lab item**: Digital Futures-funded, explicitly in collaboration with Wei Ouyang's AICell Lab | 2026-11-12 |

## Collection notes (honesty log)

- **X/Twitter sweep did NOT run.** `scripts/lab-x.py monitor` fails with
  `HTTP 402 'Insufficient credits'` — the getxapi account is out of credits
  (`X_API_KEY` in `~/.svamp/.env`). This digest is therefore built from web +
  Crossref search only, with no X signal. Needs a top-up.
- **Item 5 metadata came from Crossref**, not the article: nature.com redirects to
  an auth gate. Title, authors, journal and DOI are verified; the body is not quoted.
- **Item 3**: virtualcellchallenge.org renders client-side and returned an empty
  body; the dates are corroborated by the Arc Institute announcement (item 2) and
  the evaluation-page search snippet.
- **Not claimed**: an NVIDIA role in the Danaher lab. A LinkedIn post referenced a
  Danaher–NVIDIA collaboration, but the Oct 7 press release does not mention NVIDIA;
  its named automation partner is Automata. Left out rather than asserted.
- Winners of the 2026 Virtual Cell Challenge were **not** announced as of this run.
  The "Team Altos Labs" result circulating in search snippets refers to the
  *inaugural* (2025) challenge — deliberately not carried over.
