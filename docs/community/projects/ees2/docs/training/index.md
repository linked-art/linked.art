---
title: ""
---
[Back to EES2 Project page](https://linked.art/community/projects/ees2/)

# Train the Trainer

## A Tutorial for Using Linked Art with Quire

### Overview
The Enriching Exhibition Stories project held sessions at the Digital Humanities at Oxford Summer School (DHOxSS) from August 12-16, 2024, at St Anne’s College, Oxford. The workshops, titled “Enriching Exhibition Stories with Quire” (Parts 1 and 2), provided participants with a comprehensive introduction to Quire, an open-source software developed by Getty for creating rich, exhibition-centric digital narratives, as well as practical training on effectively using the software.

The project team demonstrated how to use Quire for crafting digital stories based on the Ashmolean Museum’s acclaimed 2023 exhibition *Labyrinth: Knossos, Myth & Reality*. Participants were trained to use the Linked Art extension, which was developed by the Enriching Exhibition Stories project, and engaged in hands-on exercises to design and implement their own projects with this extension.

We are providing the materials created for these sessions here, free-to-use and open-source. These materials can serve as training aids for anyone interested in using Quire and the Linked Art extension, supporting researchers, educators, and cultural heritage professionals in their digital storytelling.

Explore the links below to access the training materials.

### Resources
- **Introductory Slides** ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/training/training-slides.pdf)|[pptx](https://github.com/oerc-csi/la-quire/raw/main/docs/training/training-slides.pptx))
- **Installation instructions for Quire and Linked Art Extension**
    - [Download the Extension](https://linked.art/community/projects/ees2/docs/quire/)
    - MacOS ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/training/installation-instructions-macOS.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/training/installation-instructions-macOS.docx))
    - Windows ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/training/installation-instructions-windows.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/training/installation-instructions-windows.docx))
- **Exercise Sheet** ([PDF](https://github.com/oerc-csi/la-quire/raw/main/docs/training/exercise-sheet.pdf)|[docx](https://github.com/oerc-csi/la-quire/raw/main/docs/training/exercise-sheet.docx))
- **Quire Template for Exercises** ([Zip](https://github.com/oerc-csi/la-quire/raw/main/docs/training/quire-template.zip))
    - Run `npm install` in the template folder to install dependencies
- **Exercise Sheet Walk-Through Video** ([.mp4](https://github.com/oerc-csi/la-quire/raw/main/docs/training/training_video.mp4))
<script src="https://www.youtube.com/iframe_api"></script>

<div id="player"></div>

<ul>
    <li><a href="javascript:void(0);" onclick="seekToTime(0)">00:00 - Exercise 1: Download and preview the Quire project Template</a></li>
    <li><a href="javascript:void(0);" onclick="seekToTime(110)">01:50 - Exercise 2: Give your project a title and add your name</a></li>
    <li><a href="javascript:void(0);" onclick="seekToTime(240)">04:00 - Exercise 3: Write a brief introduction</a></li>
    <li><a href="javascript:void(0);" onclick="seekToTime(309)">05:09 - Exercise 4: Add a figure from a Linked Art resource</a></li>
    <li><a href="javascript:void(0);" onclick="seekToTime(505)">08:25 - Exercise 5: Add an object from a Linked Art resource</a></li>
    <li><a href="javascript:void(0);" onclick="seekToTime(668)">11:08 - Exercise 6: Add a figure to an existing object</a></li>
</ul>

<script>
    var player;
    function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
            height: '315',
            width: '560',
            videoId: 'y0z8u-r9UCY',
            events: {
                'onReady': onPlayerReady
            }
        });
    }

    function onPlayerReady(event) {
    }

    function seekToTime(seconds) {
        if (player) {
            player.seekTo(seconds, true);
        }
    }
</script>