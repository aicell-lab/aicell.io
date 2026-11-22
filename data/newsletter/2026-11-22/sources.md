# Sources — Lab Newsletter 2026-11-22

Window covered: 2026-11-12 → 2026-11-22 (since the previous digest).
All items below were fetched and read during the run on 2026-11-22 (UTC).

**X/Twitter sweep: NOT AVAILABLE.** `scripts/lab-x.py monitor --since-hours 24 --min-likes 30`
and `scripts/lab-x.py discover` both returned `HTTP 402 Insufficient credits` from getxapi —
the X API account is out of credits. No X signal fed this issue, and no new accounts were
added to `x-accounts.md` this run. This issue is built from web + Crossref search only.

---

## Used in the digest

1. **Virtual Cell Challenge 2026: Winners and Wrap-Up** — Arc Institute, published 2026-11-19
   https://arcinstitute.org/news/virtual-cell-challenge-2026-wrap-up
   *Why relevant:* resolves the challenge round we covered on Nov 12; direct read on the state of
   the art in virtual-cell / perturbation prediction — the Human Cell Simulator project's field.
   Fetched 2026-11-22.

2. **Illumina Wins Virtual Cell Challenge, Powered by Billion Cell Atlas** — Illumina via PR Newswire, 2026-11-19
   https://www.prnewswire.com/news-releases/illumina-wins-virtual-cell-challenge-powered-by-billion-cell-atlas-302946270.html
   *Why relevant:* the winner's own account of the model and training data. Corroborating source.

3. **Scientists Are Pursuing the Dream of a 'Virtual Cell'** — TIME, 2026-11-20
   https://time.com/article/2026/11/20/scientists-are-pursuing-the-dream-of-a-virtual-cell/
   *Why relevant:* mainstream framing of the result. Corroborating source.

4. **Arc Institute Names Winners for 2026 Virtual Cell Challenge** — GenomeWeb, 2026-11-20
   https://www.genomeweb.com/technology/sequencing/single-cell/gnw-virtual-cell-challenge-winners-20261120/
   *Why relevant:* trade-press confirmation of placings. Corroborating source.

5. **Segment Anything for Microscopy 2 (μSAM2)** — Archit, Teuber, Griebel, … Pape; bioRxiv,
   posted 2026-11-17, DOI 10.64898/2026.11.12.766082
   https://www.biorxiv.org/content/10.64898/2026.11.12.766082v1
   *Why relevant:* foundation model for 2D+3D microscopy segmentation, tracking and classification
   from the Pape group (an AI4Life collaborator) — squarely BioImage Model Zoo / bioimage-analysis
   territory. Fetched 2026-11-22.

6. **Genesis Mission National Science and Technology Challenges** — US Department of Energy,
   page last updated 2026-11-12; individual challenges posted 2026-11-13 and 2026-11-16
   https://www.energy.gov/undersecretaryforscience/genesis-mission/genesis-mission-national-science-and-technology-challenges
   *Why relevant:* a national programme now names "Achieving AI-Driven Autonomous Laboratories"
   and "Scaling the Biotechnology Revolution" as explicit challenges — strategy radar for REEF and
   the self-driving microscope. Fetched 2026-11-22.

7. **ChemistryNL grant for self-driving laboratory to accelerate mRNA medicine development** —
   TU Eindhoven, 2026-11-19
   https://www.tue.nl/en/news-and-events/news-overview/19-11-2026-chemistrynl-grant-for-self-driving-laboratory-to-accelerate-mrna-medicine-development
   *Why relevant:* a concrete, funded closed-loop autonomous lab in Europe (€500k, LNP/mRNA);
   same architecture as REEF applied to formulation. Fetched 2026-11-22.

8. **Scientists create landmark cellular atlas of one of the brain's most important regions** —
   Allen Institute, 2026-11-12
   https://alleninstitute.org/news/scientists-create-landmark-cellular-atlas-of-one-of-the-brains-most-important-regions
   *Why relevant:* BICAN's first major release — 25.5M cells, 26 papers, cross-species reference
   atlas, openly shared. The measurement side of the virtual-cell problem. Fetched 2026-11-22.

9. **From the human genome to the human brain cell atlas** — Ecker et al., *Cell*, 2026-11-12
   (milestone paper of the BICAN package); and **Toward an integrated framework for a human and
   mammalian brain cell atlas** — BICAN, *Cell*, 2026-11-12. Cited via the Allen Institute release above.

10. **PANGEA: an integrated cell atlas across diverse biological contexts** — *Nature Methods*,
    2026-11-12, https://www.nature.com/articles/s41592-026-03295-4
    *Why relevant:* remapped human cell atlas (12.6M cells) used to categorise multicellular
    disease responses. **Note:** full text was paywalled (303 redirect to idp.nature.com); only the
    public abstract snippet was read, so the digest cites it in one sentence and claims nothing
    beyond the abstract.

11. **Introducing Gemini 4 Neon** — Google, 2026-11-18
    https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
    *Why relevant:* advanced-AI-tools bucket — the agent/coding frontier the lab's own agent stack
    builds on. Primary vendor announcement. Fetched 2026-11-22.

12. **Latest AI Model Releases — November 2026** — aireleasetracker.com
    https://aireleasetracker.com/latest
    *Why relevant:* used only to enumerate which models landed in the window (Gemini 4 Hydrogen
    Nov 12, Qwen4-Max Nov 16, GPT-6.2 Astra/Sol Nov 17, Gemini 4 Neon Nov 18). Third-party
    aggregator with no primary links; only the Gemini 4 Neon release is asserted in the digest,
    on the strength of Google's own post above.

## Checked, not used

13. **Robot Scientists: how AI and Autonomous Laboratories are Transforming Scientific Discovery**
    — Ross King lecture, KTH AlbaNova FA31, 2026-11-12
    https://www.kth.se/en/student/kalender/robot-scientists-how-ai-and-autonomous-laboratories-are-transforming-scientific-discovery-1.1506858
    *Dropped:* the event had already happened by publication; local colour only.

14. **Multimodal cell foundation models require synergistic integration** — *Nature Machine
    Intelligence*, 2026-11-09, https://www.nature.com/articles/s42256-026-01328-3
    *Dropped:* dated just before the window and paywalled.

15. **RI-SCALE webinar, Making bioimaging data discoverable… with AI** (Joanna Hård), 2026-11-18
    https://www.egi.eu/event/webinar-ri-scale-making-bioimaging-data-discoverable-accessible-and-understandable-with-ai
    *Dropped:* already announced in the 2026-11-12 digest, and now past.
