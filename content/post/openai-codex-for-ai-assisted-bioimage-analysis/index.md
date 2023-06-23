---
title: "AI-assisted BioImage Analysis with GPT models"
summary: "Using of OpenAI's GPT models for generating Python code from natural language to assist with bioimage analysis, providing an intuitive interface for non-programmers, while also highlighting the need for running generated code in a secure environment due to potential inaccuracies and security concerns."
date: '2020-01-17T00:00:00Z'
lastmod: '2020-01-17T00:00:00Z'
draft: false
featured: true
image:
  caption: "Image credit: Wei Ouyang"
  focal_point: Smart
  placement: 10
  preview_only: false
authors:
  - Wei Ouyang
tags:
  - Generative AI
  - GPT
  - ChatGPT
  - LLM
categories:
  - post
---
# AI-assisted BioImage Analysis with OpenAI GPT models

*Originally Posted on [image.sc](https://forum.image.sc/t/ai-assisted-bioimage-analysis-with-openai-codex/), on 17th Jan 2022*

Deep learning has already revolutionized the way we do image analysis, now it comes the latest AI models for natural language processing which will change the way we interact with bioimage analysis software. 

Here is an Open AI codex demo showing how one can generate Python code from English for bioimage analysis including cellpose segmentation, feature extraction and plotting!

Watch the video here: 
<iframe width="560" height="315" src="https://www.youtube.com/embed/pkOp_oUybsc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This type of code generation technology is ideally suited for users without programming skills, and provides a solution for building simple interface for complex scientific software. It enables us to build next generation software that are powerful, flexible, but with only very simple speech or text prompt interface. 

It can completely change how software tools are delivered to the users. Since the codex model can read developer document and generate code based on the documentation, developers can focus on making reusable library and forget about the GUI part. For each bioimage anlysis task, we can provide a prompt (a chunk of text with hint on how to perform a certain task) and user can then use English or other natural language to send instruction to perform the analysis task. During the code generation, reusable UI components such as jupyter widgets, imjoy plugins or napari can be used to provide rich interaction. 

![Software UI and Codex|690x365](featured.jpeg)

The key difference compared to conventional software design is that the code are generated on the fly, and it effectively makes the user (without programming skills) a developer and makes the software more generalizable for more applications. In addition, the generated software can be reused and published, for example, one can easily generate napari or ImJoy plugins with codex model. 

However, as of now, the Codex model remains a black box and we do not have an actual way of controlling the code generation process besides the prompt and instructions. As a result, the generated code are not always correct and safe to run on the user's computer (e.g. it might accidentally remove all the data). Therefore, it is safer to run it in a sandbox environment, e.g. in the browser or docker containers. 

On the other hand, ImJoy is ideally suited for working with AI generated code because every ImJoy plugin runs in its own sandbox environment and it is easy enough to contain AI generate code that might go wrong seriously. Within the #ImJoy team, we are currently developing a new interface based on Codex code generation. The new interface will be accessible from a web browser and connected to a cloud infrastructure that allows multi-model serving, data management and serverless app hosting. 

Meanwhile, we are happy to hear your thoughts about this new direction!