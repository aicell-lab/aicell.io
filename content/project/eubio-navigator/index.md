---
title: Euro-BioImaging Research Navigator — AI for Access
summary: An AI assistant that helps scientists find the right imaging technologies and facilities across the Euro-BioImaging network from plain-language questions.
tags:
  - AI
  - agents
  - LLM
  - RAG
  - bioimaging
  - infrastructure
date: '2026-05-06T00:00:00Z'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: Euro-BioImaging Research Navigator
  focal_point: Smart

links:
  - icon: globe
    icon_pack: fas
    name: Try it
    url: https://navigator.bioimage.io
  - icon: github
    icon_pack: fab
    name: Code
    url: https://github.com/aicell-lab/eubio-navigator
  - icon: building
    icon_pack: fas
    name: Access Portal
    url: https://eap.eurobioimaging.eu

url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
slides: ''
---

Finding the right microscope — or the right facility — shouldn't require knowing
the map of European imaging infrastructure by heart. The **Euro-BioImaging
Research Navigator** is an AI-powered assistant for the
[Euro-BioImaging Access Portal](https://eap.eurobioimaging.eu) that answers
plain-language research questions like *"Which nodes offer MINFLUX in Europe?"* or
*"I need cryo-EM for structural biology — where can I go?"* and returns grounded,
ranked recommendations.

Built as part of the EU-funded **"AI for Access"** project, the Navigator uses a
**retrieval-first** architecture: the language model generates focused search
queries, a deterministic BM25 lookup retrieves real records from the facility
database, and an agent synthesizes the answer — so recommendations stay grounded
in actual data, with honest fallback when something isn't in the database. It
supports streaming responses, visible reasoning steps, multi-turn conversation and
interactive clarification.

The Navigator is **[live at navigator.bioimage.io](https://navigator.bioimage.io)**,
deployed on Kubernetes on the KTH cluster, with frontend integration into the
Euro-BioImaging Access Portal underway. It continues the lab's work — alongside
[AI4Life](/project/ai4life/) and the [BioImage Model Zoo](/project/bioimage-model-zoo/) —
on making bioimaging infrastructure open, findable and AI-accessible.
