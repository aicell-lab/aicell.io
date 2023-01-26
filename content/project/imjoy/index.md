---
title: ImJoy - Web Data Analysis
summary: Supercharging scalability and interactivity
tags:
  - deep learning
  - AI
  - web image analysis
  - web browser
  - webassembly
date: '2023-01-01T00:00:00Z'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: ImJoy
  focal_point: Smart

links:
  - icon: globe
    icon_pack: fas
    name: Website
    url: https://imjoy.io
  - icon: twitter
    icon_pack: fab
    name: Follow
    url: https://twitter.com/ImJoyTeam
  - icon: paper
    icon_pack: fab
    name: Publication
    url: https://www.nature.com/articles/s41592-019-0627-0

url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: imjoy
---

Deep learning (DL) methods achieve breakthrough performances in analyzing biomedical data across countless tasks, including medical diagnostics, DNA sequence analysis, augmented microscopy and drug design. Combined with increasing data repositories in genomics, imaging and other fields, such successes underlay a growing demand to adapt DL methods to new datasets and questions1. However, the dissemination of DL approaches faces considerable hurdles. Most published DL studies2,3,4,5 require users to retrain models on their own data to obtain the best performance and/or avoid erroneous results. Although trained models are frequently available through web applications or ImageJ plugins, retraining is typically only possible via scripts or command lines, rather than graphical user interfaces (GUIs). In addition, the complexities of setting up the required hardware and software environments often constitute forbidding obstacles6. Furthermore, the large datasets and computational resources typical of current DL successes pose challenges to traditional desktop-oriented software that tightly couple GUI and computation. Cloud services can partly alleviate these difficulties, but raise privacy and confidentiality issues that can be prohibitive for medical data7. Meanwhile, deploying scientific software to mobile platforms can make them accessible to billions of people8, enabling large-scale biomedical research and citizen science. These opportunities and challenges call for new computational frameworks.

For more information, read our publication on [Nature Methods](https://www.nature.com/articles/s41592-019-0627-0).