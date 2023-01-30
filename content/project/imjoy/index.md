---
title: ImJoy - Web Data Analysis
summary: A computational platform for supercharging scalability and interactivity
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


imjoy:
    config:
        show_window_title: true
        menu_container: "menu-container"
        menu_style: { float: 'right' }
    vizarr: |
        async function(source, window_id){
            let viewer;
            if(window_id){
                viewer = await api.createWindow({src: 'https://hms-dbmi.github.io/vizarr/', window_id, window_style: {height: '600px', 'border-style': 'solid'}})
            } else {
                viewer = await api.showDialog({src: 'https://hms-dbmi.github.io/vizarr/'});
            }
            viewer.add_image({source})
        }
    kaibu: |
        async function(url){
            const viewer = await api.showDialog({src: 'https://kaibu.org', fullscreen: true})
            await viewer.view_image(url);
            await viewer.add_shapes([], {name: 'annotation'});
        }
    startup: |
        async function(){
            
            imjoy.vizarr('https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr', 'vizarr-embeded-1')
        }
---

Deep learning (DL) methods achieve breakthrough performances in analyzing biomedical data across countless tasks, including medical diagnostics, DNA sequence analysis, augmented microscopy and drug design. Combined with increasing data repositories in genomics, imaging and other fields, such successes underlay a growing demand to adapt DL methods to new datasets and questions1. However, the dissemination of DL approaches faces considerable hurdles. Most published DL studies2,3,4,5 require users to retrain models on their own data to obtain the best performance and/or avoid erroneous results. Although trained models are frequently available through web applications or ImageJ plugins, retraining is typically only possible via scripts or command lines, rather than graphical user interfaces (GUIs). In addition, the complexities of setting up the required hardware and software environments often constitute forbidding obstacles6. Furthermore, the large datasets and computational resources typical of current DL successes pose challenges to traditional desktop-oriented software that tightly couple GUI and computation. Cloud services can partly alleviate these difficulties, but raise privacy and confidentiality issues that can be prohibitive for medical data7. Meanwhile, deploying scientific software to mobile platforms can make them accessible to billions of people8, enabling large-scale biomedical research and citizen science. These opportunities and challenges call for new computational frameworks.

For more information, read our publication on [Nature Methods](https://www.nature.com/articles/s41592-019-0627-0).



## Live Demos

This website contains ImJoy integration, you can find some example applications for image visualization below:

<div id="menu-container"></div>

### ITK/VTK Viewer
To visualize an image with ITK/VTK viewer, click <button onclick="api.showDialog({src: 'https://kitware.github.io/itk-vtk-viewer/app/', data: {image: 'https://images.proteinatlas.org/115/672_E2_1_blue_red_green.jpg'}})">here</button>

### Vizarr Example
Vizarr be embedded in the page directly:

<div id="vizarr-embeded-1"></div>

<br>
You can also view the image in a dialog by clicking <button onclick="imjoy.vizarr('https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr')">here</button>
