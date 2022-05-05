---
title: "Linked Art II: Background Resources"
---

[TOC]

This page provides additional background material for the [Linked Art questionnaire](../questionnaire/).

# Code Notebooks webinar presentations
The AHRC-funded Linked Art II project and Digital Scholarship at Oxford held a webinar on Tuesday 3 May 2022. In this webinar, Research Software Engineer Tanya Gray guided attendees through a practical exploration of transforming, reconciling, and visualising Linked Art, using real-world data from museums and galleries worldwide. These were be demonstrated using ‘code notebooks’ developed during the Linked Art II project and implemented in Jupyter. The notebooks provide step-by-step illustration and explanation, and can provide a foundation for further customisation.

The slides from the webinar are available:

- [Slides - introduction - Dr Kevin Page](../webinar/webinar-slides-intro-kp.pdf)
- [Slides - Linked Art code notebooks - Tanya Gray](../webinar/webinar-slides-tg.pdf)

# Linked Art workshop

Linked Art ran a 2 hour [workshop at the CIDOC 2020](https://linked.art/community/events/2020/cidoc/) conference providing a wealth of background motivation and detail, a recording of which can be found below.

The workshop included:
* An overview of the Linked Art initiative and community (00:00)
* A technical introduction to the Linked Art profile and overview of the core principles (from 00:14) (also available separately in the next section)
* The Van Gogh Worldwide project and its use of the Linked Art model (from 00:34)
Followed by audience Q&A
* A live encoding of data from the Rijksmuseum into Linked Art (from 01:35)

[![Watch the video](https://img.youtube.com/vi/afO7KEysda8/default.jpg)](https://youtu.be/afO7KEysda8)


Video length is 1 hour 53 minutes. 

# Linked Art Profile - overview

A short (20 minute) technical introduction to the Linked Art profile:

[![Watch the video](https://img.youtube.com/vi/lDbasKNtWM8/default.jpg)](https://youtu.be/lDbasKNtWM8)

Video length is 19 minutes.

# Linked Data

Linked Art is a targeted and focussed realisation of Linked Data. This video gives a quick 12 minute introduction to what Linked Data is.

[![Watch the video](https://img.youtube.com/vi/4x_xzT5eF5Q/default.jpg)](https://youtu.be/4x_xzT5eF5Q)

Video length is 12 minutes. 

# JSON-LD 

JSON-LD is serialisation format for Linked Data that is used to represent descriptions of artworks as Linked Art. This video gives a quick 13 minute introduction to JSON-LD:

[![Watch the video](https://img.youtube.com/vi/vioCbTo3C-4/default.jpg)](https://youtu.be/vioCbTo3C-4)



Video length is 13 minutes.

# Jupyter Notebook 

For those new to Jupyter Notebooks, we recommend you watch this short 7 minute introduction:

[![Watch the video](https://img.youtube.com/vi/jZ952vChhuI/default.jpg)](https://youtu.be/jZ952vChhuI)

Video length is 7 minutes. 

# Linked Art Jupyter Code Notebooks

For convenience, here is an annotated list of all the code notebooks from Section 2 of the questionnaire.

The different types of Jupyter notebooks:
* Transform - transformations using real-world collections data
* Reconcile - reconciliation of collections data with authoritative data on geographical place names
* Visualise - visualisation using Linked Art JSON-LD
  

|Notebook type | Notebook  | Download | nbviewer | Binder |
| -------- | ------------- | ------------- | ------- | ------ |
| Transform | Indianapolis Museum of Art  |  [download](https://github.com/tgra/Linked-Art/01-01-Transform-XML-IMA.ipynb) | [nbviewer](https://nbviewer.org/github/tgra/Linked-Art/blob/main/01-01-Transform-XML-IMA.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tgra/Linked-Art/HEAD?labpath=01-01-Transform-XML-IMA.ipynb)|
| Transform| Philadelphia Museum of Art | [download](https://github.com/tgra/Linked-Art/01-04-Transform-CSV-PMA.ipynb) | [nbviewer](https://nbviewer.org/github/tgra/Linked-Art/blob/main/01-04-Transform-CSV-PMA.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tgra/Linked-Art/HEAD?labpath=01-04-Transform-CSV-PMA.ipynb) |
| Transform| Cleveland Museum of Art | [download](https://github.com/tgra/Linked-Art/01-02-Transform-CSV-CMA.ipynb) | [nbviewer](https://nbviewer.org/github/tgra/Linked-Art/blob/main/01-02-Transform-CSV-CMA.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tgra/Linked-Art/HEAD?labpath=01-02-Transform-CSV-CMA.ipynb) |
| Transform| National Gallery of Art | [download](https://github.com/tgra/Linked-Art/01-03-Transform-CSV-NGA.ipynb) | [nbviewer](https://nbviewer.org/github/tgra/Linked-Art/blob/main/01-03-Transform-CSV-NGA.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tgra/Linked-Art/HEAD?labpath=01-03-Transform-CSV-NGA.ipynb) |
| Transform| Harvard Art Museum | [download](https://github.com/tgra/Linked-Art/01-05-Transform-JSON-Harvard-API.ipynb) | [nbviewer](https://nbviewer.org/github/tgra/Linked-Art/blob/main/01-05-Transform-JSON-Harvard-API.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tgra/Linked-Art/HEAD?labpath=01-05-Transform-JSON-Harvard-API.ipynb) |
| Reconcile| John Ruskin artworks - reconcile place names | [download](https://github.com/tgra/Linked-Art/02-01-Reconcile-John-Ruskin-Place-Names.ipynb) | [nbviewer](https://nbviewer.org/github/tgra/Linked-Art/blob/main/02-01-Reconcile-John-Ruskin-Place-Names.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tgra/Linked-Art/HEAD?labpath=02-01-Reconcile-John-Ruskin-Place-Names.ipynb) |
| Visualise | John Ruskin artworks - Timeline - Transform Data | [download](https://github.com/tgra/Linked-Art/02-01-Visualise-John-Ruskin-Transform-Data.ipynb)|[nbviewer](https://nbviewer.org/github/tgra/Linked-Art/blob/main/02-01-Visualise-John-Ruskin-Transform-Data.ipynb)|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tgra/Linked-Art/HEAD?labpath=02-01-Visualise-John-Ruskin-Transform-Data.ipynb)|
| Visualise | John Ruskin artworks - Timeline - Visualise with Google | [download](https://github.com/tgra/Linked-Art/02-02-Visualise-John-Ruskin-Google-Spreadsheet.ipynb)|[nbviewer](https://nbviewer.org/github/tgra/Linked-Art/blob/main/02-02-Visualise-John-Ruskin-Google-Spreadsheet.ipynb)|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tgra/Linked-Art/HEAD?labpath=02-02-Visualise-John-Ruskin-Google-Spreadsheet.ipynb)|
| Visualise | John Ruskin artworks - Timeline - Visualise locally | [download](https://github.com/tgra/Linked-Art/02-03-Visualise-John-Ruskin-Local.ipynb)|[nbviewer](https://nbviewer.org/github/tgra/Linked-Art/blob/main/02-03-Visualise-John-Ruskin-Local.ipynb)|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tgra/Linked-Art/HEAD?labpath=02-03-Visualise-John-Ruskin-Local.ipynb)|

