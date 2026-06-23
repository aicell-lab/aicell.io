---
title: Hypha — Distributed Computing for AI-Powered Science
summary: Open-source framework that connects AI models, data, and instruments into shared workspaces — the backbone of the lab's platforms.
tags:
  - AI
  - distributed computing
  - agents
  - infrastructure
  - open source
date: '2026-06-01T00:00:00Z'

external_link: ''

image:
  caption: Hypha
  focal_point: Smart

links:
  - icon: globe
    icon_pack: fas
    name: Website
    url: https://docs.amun.ai
  - icon: github
    icon_pack: fab
    name: Code
    url: https://github.com/amun-ai/hypha

url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

Modern science is increasingly built from many moving parts — AI models, large datasets, compute clusters, and laboratory instruments — that rarely live in the same place. **Hypha** is our open-source framework for connecting them. It lets researchers and AI agents call remote functions, services, and models as if they were local, organising everything into unified *virtual workspaces*.

Hypha is the backbone of much of what the lab builds: it powers cloud model serving in [BioEngine](/project/bioengine), instant model testing in the [BioImage Model Zoo](https://bioimage.io), autonomous microscopy in [Agent-Lens](/project/agent-lens), and agent-ready biological data. Its companion libraries — `hypha-rpc`, `hypha-core`, and `hypha-compute` — make it easy to expose any Python or browser service to the network and to AI agents over standards like the Model Context Protocol.

Learn more in the [documentation](https://docs.amun.ai) or try the public server at [hypha.aicell.io](https://hypha.aicell.io).
