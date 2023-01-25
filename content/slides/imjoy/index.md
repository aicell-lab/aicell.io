---
title: Slides
summary: ImJoy
authors: []
tags: []
categories: []
date: '2021-02-05T00:00:00Z'
slides:
  # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: black
  # Choose a code highlighting style (if highlighting enabled in `params.toml`)
  #   Light style: github. Dark style: dracula (default).
  highlight_style: dracula
---

## ImJoy: Supercharging Interactivity and Scalability for BioImage Analysis

Wei Ouyang 

KTH | SciLifeLab, Stockholm

---
## Challenges in AI for bioimaging

* **Usability**: User friendly GUI
* **Flexibility**: Flexible for different data types
* **Interactivity**: Respond to GUI on laptop/mobile
* **Scalability**: Remote storage and compute resources
* **Privacy**: Edge computing

---
## Progressive Web App

* Rich and interactive UI libraries
* Computation in the browser (+cloud)
* Offline support

---
<!-- .slide: data-background="white" -->
### ImJoy https://imjoy.io
Data science tools in the browser

<img src="https://docs.google.com/drawings/d/e/2PACX-1vSBsdhDBrp4L2zWfL_9YOUHCS2zQ51HtjplGa-l_a1hMpNjbqENzmXrcSmYs6yed_NACNZSRH-7qsph/pub?w=1248&amp;h=573">
---
# Key concepts
 * Sandboxed plugins connected via Remote Procedure calls
 * Workflow composition via asynchronous programming
 * Open Integration with existing software/website

---

### 👐Open Integration with Web Apps

Customize annotation workflow with Kaibu

```js
// load the web app via its URL
viewer = await api.createWindow({src: "https://kaibu.org/#/app"})
// call api functions directly via RPC
// add an image layer
await viewer.view_image("https://images.proteinatlas.org/61448/1319_C10_2_blue_red_green.jpg")
// add an annotation layer
await viewer.add_shapes([], {name:"annotation"})
```

---

### 🔥Demo: Visualization with Vizarr

Made by Trevor Manz et. al.
<iframe width="100%" height="500px" src="https://hms-dbmi.github.io/vizarr/?source=https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr"  frameborder="0" allowfullscreen></iframe>


---

## 🚀A rapid growing list of plugins
 * [ImageJ.JS](https://ij.imjoy.io)
 * [File Manager](https://imjoy-team.github.io/elFinder/)
 * [Vizarr](https://github.com/hms-dbmi/vizarr) for visualizing zarr images
 * [ITK/VTK Viewer](https://kitware.github.io/itk-vtk-viewer/docs/) for 3D visualizing
 * [ImJoy Slides](https://slides.imjoy.io)
 * [ImJoy Chart Editor](https://chart.imjoy.io)

---
### Works with Jupyter/Binder and Colab

<img style="height:70%;object-fit:contain;background-color: white;"  src="https://raw.githubusercontent.com/imjoy-team/imjoy-demo-assets/main/image125.gif">

---
## Conclusions
 * ImJoy is built for scalability and interactivity
 * ImJoy plugins are sandbox services connected via RPC

---
### Acknowledgements
Work carried out at Cell Profiling group @ SciLifeLab headed by Emma Lundberg

---

# 🙏Thank You!
