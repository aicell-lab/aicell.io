---
title: BioImage Model Zoo — FAIR AI Models for Microscopy
summary: A community-driven, fully open repository where standardized deep-learning models can be shared, tested in the browser, and deployed across imaging tools.
tags:
  - AI
  - deep learning
  - models
  - FAIR
  - model zoo
  - bioimaging
  - open source
date: '2026-06-01T00:00:00Z'

external_link: ''

image:
  caption: BioImage Model Zoo
  focal_point: Smart

links:
  - icon: globe
    icon_pack: fas
    name: Website
    url: https://bioimage.io
  - icon: github
    icon_pack: fab
    name: Code
    url: https://github.com/bioimage-io/bioimage.io
  - icon: paper
    icon_pack: fab
    name: Preprint
    url: https://www.biorxiv.org/content/10.1101/2022.06.07.495102v1

url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
slides: ''
---

The [BioImage Model Zoo](https://bioimage.io) is a community-driven, fully open resource where standardized, pre-trained deep-learning models can be **shared, explored, tested directly in the browser, and deployed** in many end-user tools — including ilastik, deepImageJ, QuPath, StarDist, ImJoy, and ZeroCostDL4Mic. A shared model standard makes these models cross-compatible, so a model contributed once can be reused everywhere.

The AICell Lab leads the **user services and cloud infrastructure** behind the Zoo: the model-upload and testing pipelines, and the [BioEngine](/project/bioengine) backend that runs the in-browser "test run" feature. Our goal is to make deep-learning methods for microscopy findable, accessible, interoperable, and reusable (FAIR) across the whole bioimaging ecosystem. This effort grew out of the now-completed [AI4Life](/project/ai4life) project and continues as a living community platform.

Recent additions push the Zoo further into the browser: **in-browser model testing**
on cloud or HPC GPUs via [BioEngine](/project/bioengine) (no install, no local GPU);
a **collaborative annotation layer** with AI-assisted segmentation (Cellpose and
Cellpose-SAM); and an **agent skill** that lets any AI assistant guide a researcher
through contributing a model end to end — packaging, validating, and submitting it.
Much of this runs entirely client-side via Pyodide/WebAssembly, backed by
[Hypha](/project/hypha) Cloud.

Read more in our [preprint](https://www.biorxiv.org/content/10.1101/2022.06.07.495102v1).
