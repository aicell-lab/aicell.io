---
title: REEF Imaging Farm
summary: A self-driving cell-biology lab where AI agents plan, run and adapt live-cell experiments across a cluster of instruments.
tags:
  - active
  - deep learning
  - AI
  - microscopy
  - bioimaging
  - augmented microscopy
  - robotics
  - lab automation
date: '2024-06-01T00:00:00Z'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: "REEF Imaging Farm"
  focal_point: Smart

links:
  - icon: github
    icon_pack: fab
    name: Code
    url: https://github.com/aicell-lab/reef-imaging

url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

slides:
---

**REEF is a self-driving cell-biology lab.** It is an automated imaging farm where AI agents plan,
run and adapt live-cell experiments across a whole cluster of instruments, with a human able to
watch and step in at any point.

The idea at its heart is simple: a scientist should be able to *describe* an experiment in plain
language and have the lab carry it out. Under the hood, REEF brings together multiple microscopes
and fluidic systems, robotic arms, liquid-handling robots and automated incubators into one
coordinated system. AI analyzes the images as they are captured and feeds decisions back to the
hardware, so an experiment can adapt while it runs, minimize phototoxicity, and catch rare events
in living cells.

### The farm in action

The robotic arm moving a plate between the incubator and the microscope, part of a fully automated
imaging run:

<iframe src="https://drive.google.com/file/d/1_LsVB4SHRl9jfhwdTQ8yX3l1bakRNWWI/preview" width="100%" height="460" allow="autoplay" allowfullscreen frameborder="0" style="border-radius:8px;"></iframe>

### What it is for

- Automated widefield and fluorescence imaging at scale
- Long-term live-cell imaging and cell tracking
- Spatial-omics and multiplexed imaging
- Real-time, AI-augmented analysis with feedback control, automatically adjusting field of view,
  illumination and other conditions on the fly

The near-term goal is massive, high-quality image-data generation. The longer-term goal is
experiments that a scientist can simply talk to.

### A live, agent-run experiment (CZI 2026)

In 2026, REEF ran a **live, fully agent-controlled wet-lab experiment** on stage during an
**invited talk at CZI (the Chan Zuckerberg Initiative)**. A researcher typed a single
natural-language request, to study how osmotic pressure affects living cells and then attempt a
*rescue* to see if the changes reverse, and an AI agent orchestrated the whole lab remotely,
streaming images to a live viewer in real time. No manual pipetting, no clicking through software:
one prompt, and the farm ran the experiment on real cells, end to end, catching and recovering from
the inevitable live hiccups along the way. It worked, and the osmotic change was confirmed
reversible.

We wrote up the experience, including a short interview with the agent that ran it, here:
**[One Prompt, a Whole Lab: A Live Agent-Run Experiment on REEF](/post/reef-first-live-demo/)**.

That run was made possible by **Hanzhao Zhang** (experiment preparation and getting the system
ready for full runs), **Songtao Cheng** (hardware, and keeping everything running through the live
demo) and **Wei Ouyang** (who took it onto the CZI stage), with contributions from the whole AICell
Lab team.

### Built around safety

REEF pairs a capable AI agent with a safety-first system. Experiments stream to a live viewer, a
human stays in the loop, and unsafe actions are refused rather than risked, so the cells and the
instruments are protected even when a run hits the unexpected. (We keep the deeper technical
details under wraps while the work is unpublished.)

### Get involved

REEF is where AI agents, robotics and live cell biology meet. The code lives on
[GitHub](https://github.com/aicell-lab/reef-imaging), and if building labs that a scientist can
simply talk to sounds like your thing, we would be glad to [hear from you](/#recruiting).
