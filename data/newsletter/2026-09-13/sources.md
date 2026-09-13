# Newsletter sources — September 13, 2026

**Theme:** **Cell–cell communication inference** — computational methods that reconstruct the
*intercellular* signaling network (which cell type sends which ligand to which receptor on which
neighbor, and what it does downstream) from single-cell and spatial transcriptomics. "How Cells
Talk." The arc: a curated ligand-receptor repository + statistics that respect multi-subunit
complexes (CellPhoneDB) → quantitative signaling-network inference with pattern recognition
(CellChat) → link a ligand to the *target genes* it switches on (NicheNet) → put the
conversations back in space via optimal transport (SpaOTsc) → spatial CCC at scale with
ligand/receptor competition and directionality (COMMOT) → graph neural networks that learn how a
cell's *niche* shapes its expression, beyond receptor-ligand (NCEM).

**Why now / editorial:** deliberate pivot after an eight-day molecular/sequence streak
(protein design Sep 5, GRNs Sep 6, genome reading Sep 7, protein engineering Sep 8, force fields
Sep 9, antibiotics Sep 10, knowledge graphs Sep 11, mRNA design Sep 12). This is **systems cell
biology** — the *social* layer above the single cell — and it sits at the intersection of the
lab's single-cell + spatial interests. Strong journal verifiability (Nat Protoc, Nat Commun ×2,
Nat Methods ×2, Nat Biotech) and a clean methodological progression (statistics → networks →
downstream effect → space → optimal transport → graph neural nets).

**Dedup guard:** Distinct from **Sep 6** (gene *regulatory* networks — the *intracellular*
circuit of transcription factors) and **Aug 13** (spatial transcriptomics — *where* cells are and
how to map RNA in tissue). Today's object is the **intercellular signaling network**: the
inferred conversations *between* cells. Cell-cell communication has **never** been a newsletter
theme (grep of all newsletter posts returns none). Also distinct from Aug 15 (single-cell FMs)
and Sep 3 (multi-omics integration).

**X/Twitter sweep:** SKIPPED — getxapi HTTP 402 "Insufficient credits" on `monitor`
(--since-hours 24 --min-likes 30). ~36th consecutive skip (>five weeks). Grok-based replacement
wired, awaiting xAI credits. `discover` not run (same credit block).

**Verification:** all 6 anchors verified via **NCBI E-utilities** (esearch DOI→PMID, efetch
abstract XML), full `AbstractText` captured; DOI + PMID + journal + year recorded. Only
abstract-verified verbatim quotes used below.

---

## Framing + the founding move — a ligand-receptor repository + statistics

### Efremova et al. — CellPhoneDB — VERIFIED (PMID 32103204)
- Efremova M, Vento-Tormo M, Teichmann SA, Vento-Tormo R. "CellPhoneDB: inferring cell-cell
  communication from combined expression of multi-subunit ligand-receptor complexes." *Nature
  Protocols* 15:1484–1506, 2020. DOI 10.1038/s41596-020-0292-x.
- ABSTRACT-VERIFIED (verbatim): "**Cell-cell communication mediated by ligand-receptor complexes
  is critical to coordinating diverse biological processes, such as development, differentiation
  and inflammation.**"; "**we developed CellPhoneDB, a novel repository of ligands, receptors and
  their interactions.**"; "**our database takes into account the subunit architecture of both
  ligands and receptors, representing heteromeric complexes accurately.**"; "**We integrated our
  resource with a statistical framework that predicts enriched cellular interactions between two
  cell types from single-cell transcriptomics data.**"
- USE: the founding move — you can't read a conversation without a dictionary of words. A curated
  repository that respects that receptors and ligands are often *multi-subunit complexes*, plus a
  permutation-statistics test for which cell-type pairs show enriched interaction. Public, code +
  web interface. Sets up "the cell's social network."

## Section 1 — From pairs to a quantitative signaling network

### Jin et al. — CellChat — VERIFIED (PMID 33597522)
- Jin S, Guerrero-Juarez CF, Zhang L, Chang I, Ramos R, Kuan C-H, Myung P, Plikus MV, Nie Q.
  "Inference and analysis of cell-cell communication using CellChat." *Nature Communications*
  12:1088, 2021. DOI 10.1038/s41467-021-21246-9.
- ABSTRACT-VERIFIED (verbatim): "**Understanding global communications among cells requires
  accurate representation of cell-cell signaling links and effective systems-level analyses of
  those links.**"; "**we develop CellChat, a tool that is able to quantitatively infer and analyze
  intercellular communication networks from single-cell RNA-sequencing (scRNA-seq) data.**";
  "**CellChat predicts major signaling inputs and outputs for cells and how those cells and signals
  coordinate for functions using network analysis and pattern recognition approaches.**"; "**Through
  manifold learning and quantitative contrasts, CellChat classifies signaling pathways and
  delineates conserved and context-specific pathways across different datasets.**"
- USE: the network turn — not just "do A and B interact" but a *quantitative* signaling network:
  inputs/outputs per cell, pattern recognition, manifold learning, and conserved-vs-context-specific
  pathways compared across datasets. Systems-level analysis of the conversation.

## Section 2 — From a signal to its downstream effect

### Browaeys, Saelens & Saeys — NicheNet — VERIFIED (PMID 31819264)
- Browaeys R, Saelens W, Saeys Y. "NicheNet: modeling intercellular communication by linking
  ligands to target genes." *Nature Methods* 17:159–162, 2020. DOI 10.1038/s41592-019-0667-5.
- ABSTRACT-VERIFIED (verbatim): "**Computational methods that model how gene expression of a cell
  is influenced by interacting cells are lacking.**"; "**We present NicheNet
  (https://github.com/saeyslab/nichenetr), a method that predicts ligand-target links between
  interacting cells by combining their expression data with prior knowledge on signaling and gene
  regulatory networks.**"; "**We applied NicheNet to tumor and immune cell microenvironment data
  and demonstrate that NicheNet can infer active ligands and their gene regulatory effects on
  interacting cells.**"
- USE: the "so what does the signal *do*" beat — most methods stop at receptor binding; NicheNet
  chains the ligand through *prior* signaling + gene-regulatory networks to predict the *target
  genes* it switches on in the receiver. Connects the intercellular layer (today) to the
  intracellular GRN layer (Sep 6). A conversation with consequences.

## Section 3 — Putting the conversation back in space

### Cang & Nie — SpaOTsc — VERIFIED (PMID 32350282)
- Cang Z, Nie Q. "Inferring spatial and signaling relationships between cells from single cell
  transcriptomic data." *Nature Communications* 11:2084, 2020. DOI 10.1038/s41467-020-15968-5.
- ABSTRACT-VERIFIED (verbatim): "**Single-cell RNA sequencing (scRNA-seq) provides details for
  individual cells; however, crucial spatial information is often lost.**"; "**We present SpaOTsc,
  a method relying on structured optimal transport to recover spatial properties of scRNA-seq data
  by utilizing spatial measurements of a relatively small number of genes.**"; "**The cell-cell
  communications are then obtained by 'optimally transporting' signal senders to target signal
  receivers in space.**"; "**Using partial information decomposition, we next compute the
  intercellular gene-gene information flow to estimate the spatial regulations between genes across
  cells.**"
- USE: the space beat — signaling is local, but scRNA-seq throws away position. SpaOTsc uses
  *optimal transport* to reconstruct a spatial metric and then "optimally transports" senders to
  receivers, recovering *where* the conversations happen and the intercellular gene-gene information
  flow. The bridge from dissociated data to spatial signaling.

## Section 4 — Spatial cell-cell communication at scale

### Cang et al. — COMMOT — VERIFIED (PMID 36690742)
- Cang Z, Zhao Y, Almet AA, Stabell A, Ramos R, Plikus MV, Atwood SX, Nie Q. "Screening cell-cell
  communication in spatial transcriptomics via collective optimal transport." *Nature Methods*
  20:218–228, 2023. DOI 10.1038/s41592-022-01728-4.
- ABSTRACT-VERIFIED (verbatim): "**incorporation of the spatial information and complex biochemical
  processes required in the reconstruction of CCC remains a major challenge.**"; "**we present
  COMMOT (COMMunication analysis by Optimal Transport) to infer CCC in spatial transcriptomics,
  which accounts for the competition between different ligand and receptor species as well as
  spatial distances between cells.**"; "**A collective optimal transport method is developed to
  handle complex molecular interactions and spatial constraints.**"; "**we introduce downstream
  analysis tools to infer spatial signaling directionality and genes regulated by signaling using
  machine learning models.**"; "**We apply COMMOT to simulation data and eight spatial datasets
  acquired with five different technologies**."
- USE: the scale/rigor beat — CCC in true spatial transcriptomics, with *collective* optimal
  transport handling ligand/receptor *competition* and physical distance, plus ML to infer signaling
  *direction* and regulated genes. Validated across eight datasets / five technologies. The mature
  spatial method.

## Section 5 — Graph neural networks: learn the niche's effect

### Fischer, Schaar & Theis — NCEM — VERIFIED (PMID 36302986)
- Fischer DS, Schaar AC, Theis FJ. "Modeling intercellular communication in tissues using spatial
  graphs of cells." *Nature Biotechnology* 41:332–336, 2023. DOI 10.1038/s41587-022-01467-z.
- ABSTRACT-VERIFIED (verbatim): "**Models of intercellular communication in tissues are based on
  molecular profiles of dissociated cells, are limited to receptor-ligand signaling and ignore
  spatial proximity in situ.**"; "**We present node-centric expression modeling, a method based on
  graph neural networks that estimates the effects of niche composition on gene expression in an
  unbiased manner from spatial molecular profiling data.**"; "**We recover signatures of molecular
  processes known to underlie cell communication.**"
- USE: the deep-learning/horizon beat — NCEM names the limits of the prior generation (dissociated
  profiles, receptor-ligand-only, no space) and answers with *graph neural networks*: model each
  cell as a node and learn, unbiased, how its *niche composition* shapes its gene expression. From
  hand-curated ligand-receptor lists to learned, spatial, graph-based communication.

## Section 6 — Lab hook + horizon
- The through-line: **a tissue is a conversation.** A cell's behavior isn't set only by its own
  genome (Sep 6's intracellular circuit) but by the signals arriving from its neighbors — and that
  intercellular network can be *inferred* from the same single-cell and spatial data the lab already
  works with. The field's trajectory is the lab's trajectory: from curated priors + statistics →
  networks → *learned*, spatial, graph-based models (NCEM).
- Ties to lab interests: the [spatial](/post/newsletter-2026-08-13/) and single-cell threads meet
  here; graph neural networks (NCEM) echo the [knowledge-graph digest](/post/newsletter-2026-09-11/)
  — biology keeps turning into graphs, and representation learning keeps being the right tool.
- Open + benchmarked ethos: CellPhoneDB, CellChat, NicheNet and COMMOT are all *open* tools with
  public code/web interfaces — the shared-resource spirit behind the
  [BioImage Model Zoo](/project/bioimage-model-zoo/) and [BioEngine](/project/bioengine/).
- Horizon / strategy radar: cell-cell communication is a load-bearing layer for the
  [virtual cell](/project/human-cell-simulator/) — a faithful cell model must simulate not just
  what happens *inside* a cell but how cells *coordinate* in a tissue. And optimal transport (SpaOTsc,
  COMMOT) is a recurring, powerful primitive worth tracking across the lab's single-cell + spatial work.
