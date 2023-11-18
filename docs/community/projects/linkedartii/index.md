---
title: "Linked Art II: Developing Community, Practice, and Scholarship"
---

<img src="/community/projects/researchnetwork/ox_brand1_rev_rect.gif" alt="University of Oxford" height="67" />       <img src="/community/projects/researchnetwork/UKRI_AHR_Council-Logo_Horiz-RGB.png" alt="AHRC" height="75" /> 


*Linked Art II: Developing Community, Practice, and Scholarship* (project reference AH/T013117/1) was a project funded by the UK [Arts and Humanities Research Council](https://ahrc.ukri.org/) (AHRC) through their programme for *UK-US Collaboration for Digital Scholarship in Cultural Institutions*.

## Project Participants

- **Principal Investigator**: [Dr. Kevin Page](https://eng.ox.ac.uk/people/kevin-page/), [University of Oxford e-Research Centre](https://www.oerc.ox.ac.uk/)
- **Co-Investigator**: Rob Sanderson, [J. Paul Getty Trust](https://www.getty.edu/)
- **Research Software Engineer**: Tanya Gray, [Digital Scholarship at Oxford](https://digitalscholarship.web.ox.ac.uk/)
- **Project Partners**:
    - [American Numismatic Society](http://numismatics.org/)
    - [National Gallery of Art](https://www.nga.gov/) (US)
    - [The National Gallery](https://www.nationalgallery.org.uk/) (UK)
    - [Newfields](https://discovernewfields.org/)
    - [Philadelphia Museum of Art](https://www.philamuseum.org/)
    - [Smithsonian Institution](https://www.si.edu/)
    - [Victoria and Albert Museum](https://www.vam.ac.uk/)
    - [Yale Center for British Art](https://britishart.yale.edu/)

Please address enquiries about the project to Dr. Page in the first instance.

# Linked Art II Project Activities and Outcomes

## Community Modelling Workshops

Due to the project start in February 2020 coinciding with the COVID-19 pandemic, the planned Community Outreach Workshops were translated into fortnightly 1-hour online Zoom sessions which ran between June and November 2020. Practitioners from project partners (listed above) brought their data ‘exemplars’ to the sessions which were ‘live modelled’ as Linked Art.

This offering of online ‘exemplar mapping’ sessions has continued on demand in Linked Art teleconferences ([get involved](https://linked.art/community/#get-involved)). This approach informed the online workshop activity at the CIDOC 2020 conference (see below).

## Transformation Notebooks and Exemplars using Jupyter 
To establish good practice in the transformation of existing collections data into Linked Art, and building upon the project’s earlier community modelling activity, the project then developed a suite of ‘code notebooks’.

Created by the project’s Research Software Engineer, Tanya Gray, the code notebooks embed modifiable software (written in Python) within explanatory description and documentation, which users can iteratively work through step-by-step (using a notebook environment called Jupyter). By completing a notebook, users both create Linked Art compatible data, and gain a better understanding of the practices involved in creating this data.

The suite of notebooks is fully documented and includes exemplars for transformation, reconciliation, and visualisation, which are freely available for use and adaptation at: [https://tgra.github.io/Linked-Art/](https://tgra.github.io/Linked-Art/)


## Code Notebook training sessions
The code notebooks were used in two training sessions for the cultural heritage community.

The first was held as the online webinar ‘[Linked Art in Practice using Jupyter Code Notebooks - Connecting Cultural Heritage Collections Data](https://linked.art/community/projects/linkedartii/webinar/)’. In this webinar, the Linked Art II project guided over 50 international attendees through a practical exploration of transforming, reconciling, and visualising Linked Art, using real-world data from museums and galleries worldwide. These were demonstrated using the ‘code notebooks’ developed during the Linked Art II project and implemented in Jupyter. The notebooks provide step-by-step illustration and explanation, and can provide a foundation for further customisation.

In a second training session, the project team ran an in-person tutorial at the [Digital Humanities at Oxford Summer School 2022](https://digitalscholarship.web.ox.ac.uk/digital-humanities-oxford-summer-school). After an introduction to the principles and standards behind Linked Art, a hands-on practical session guided attendees through the notebooks, learning how to use the software workflows for creating and manipulating Linked Art data developed in the project.

This video playlist accompanies the documentation and shows the notebooks in action:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?list=PLo9oxak5HtogWrzIc99LmCgyifDjd6CQr" title="Linked Art II code notebooks demonstration" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Linked Art Questionnaire
In the first half of 2022 the project ran a [community questionnaire](https://linked.art/community/projects/linkedartii/questionnaire/) seeking views on the use and adoption of Linked Art, and capturing the opportunities and challenges members of the community might foresee. The questionnaire was widely promoted and open to all those who create, support, or do research using art collections data.

In addition to sections on the broader implications of Linked Art adoption, the questionnaire included a section gathering feedback about the code notebooked (described above), which respondents were encouraged to try out; and a final section requesting proposals for specific exemplars in which Linked Art could be applied.

Once the questionnaire was closed the project team analysed questionnaire responses and long-listed exemplar proposals broadly consistent and representative with trends across the community. The project team then consulted with a shortlist of respondents who had suggested exemplars.  Finally, two exemplars were selected for development during the final stages of the project, in collaboration with their proposers; these are described below.

## Co-created Exemplar: Enabling Participatory Data Perspectives for Image Archives through a Linked Art Workflow
Collaborating with Julien A. Raemy from the Swiss [Participatory Knowledge Practices in Analogue and Digital Image Archives](https://about.participatory-archives.ch) (PIA), the project developed a reconfigurable Python-based workflow to transform photographic collections (specifically the Family Kreis and Ernst Brunner collections) into Linked Open Usable Data, as a foundation for varied participatory interfaces supporting scholarship. The resultant workflow further developed and refined the principles and practice established in the code notebooks (described above), applying them within the specific context and needs of PIA.

This exemplar was published and presented at the Digital Humanities 2023 conference in Graz, Austria. Further information can be found at:
- [https://doi.org/10.5281/zenodo.7878358](https://doi.org/10.5281/zenodo.7878358) (Poster)
- [https://doi.org/10.5451/unibas-ep95099](https://doi.org/10.5451/unibas-ep95099) (Extend abstract in the Book of Abstracts)

## Co-created Exemplar: New York Alternative Spaces Exhibitions Browser

The project’s second community-generated exemplar was a collaboration with Jonathan Lill, Head of Metadata and Systems at The Museum of Modern Art (MoMA) Library, Archives, and Research Collections (ALRC) in New York.

We identified a general need for an ‘exhibition browser’ which can present data (encoded using Linked Art) about art exhibitions in a sustainable way with few resources, for example by very small institutions or informal or transient organisations.

We decided to explore and prototype these ideas for an ‘exhibition browser’ through its application to a dataset curated by Jonathan which documents the alternative exhibition spaces of New York, data which has no institutional owner or support for maintenance. The idea was to create software which would make  the information about these exhibitions more easily accessible and explorable by a wider audience, published on the web in a form which is simple to host and maintain (e.g. on a platform such as github).

We designed the Exhibition Browser tool:

1. To ingest an exhibition dataset as Linked Art, or in a semi-structured format (e.g. CSV from a spreadsheet) which could be converted to Linked Art using variants of our existing Jupyter notebooks;
2. Allow the ‘curator’ to investigate the ‘shape’ of the data -- the relative quantities and density of links between different aspects of the data (e.g. artists, venues, exhibition dates) -- to inform decisions about how to prioritise lists, views, and navigational links between them. This enables a general viewer of the resultant Exhibition Browser (e.g. member of the public) to benefit from the expertise of the curator when first exploring an exhibition dataset, while retaining the freedom to explore all the data once they are familiar with it. This pre-publication data investigation stage is realised as a separate tool extending and enhancing the project’s Jupyter notebook approach through the Mercury platform. Here the curator is assisted in identifying patterns and quantifications, which are then used to create configuration files used to structure the published Exhibition Browser.
3. Use these configuration files to generate a standalone website for the exhibition dataset, including outwards links to other web resources where available. This Exhibition Browser can be exported as a ‘static’ website, which does not need a database or complex content management system, and can be easily hosted using the simplest of website providers. Unlike insitutally hosted online gallery interfaces, the Exhibition Browser tool does not assume a dynamically updated and maintained dataset. It is assumed the curator will regenerate a new version of the Exhibition Browser for publishing as and when this is required.
4. The Exhibition Browser was additionally extended to incorporate visualisations of the data, summarising the information on some pages in an even more readily accessible form.

In this video a published Exhibition Browser website for the ‘alternative spaces’ dataset is demonstrated by Tanya Gray:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/93pVD9LQ_9k" title="Linked Art II Exhibition Browser: Alternative Spaces" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> 


This video shows the preceeding analysis step for the same dataset:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/RgkRf6dbTy8" title="Linked Art II Exhibition Browser: Alternative Spaces data analysis" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The ‘hosted’ version of the resultant Exhibition Browser for the ‘alternative spaces’ dataset (as seen in the above videos) can be found at [https://tgra.github.io/Linked-Art-Exhibition-Browser-MoMA](https://tgra.github.io/Linked-Art-Exhibition-Browser-MoMA)

The technical and implementation details of the Exhibition Browser tool are documented in the exemplar’s github repository: [https://github.com/tgra/Linked-Art-Exhibition-Browser](https://github.com/tgra/Linked-Art-Exhibition-Browser) 

Code for the data analysis stage tooling (step 2, above) can be found in this repository: [https://github.com/tgra/Linked-Art-Exhibition-Browser-Data-Analysis](https://github.com/tgra/Linked-Art-Exhibition-Browser-Data-Analysis)


## Additional Project Dissemination

The project also supported dissemination activities including an [introductory workshop demonstrating live modelling of Linked Art, and a panel at the online CIDOC 2020 conference](https://linked.art/community/events/2020/cidoc); and a [panel on Linked Art at the online Digital Humanities 2020 conference](https://hcommons.org/deposits/item/hc:32009/).


## Project Abstract

*Linked Art II: Developing Community, Practice, and Scholarship* brings together University researchers with experts from some of the leading art museums in the UK and US. The project will engage with scholars and practitioners to highlight the opportunities afforded by connected collections as data, and establish where new digital methods and tools are needed to enable novel research. Linked Art II will engage with cultural institutions to examine how structured data can contribute towards digital challenges, including improving the accessibility of collections, and increasing the range and diversity of institutions and material available to the public.

The foundation of the project is the development and application of Linked Data to cultural heritage collections, with an emphasis on works of art and their provenance. Linked Data will provide a platform for multi-modal digital scholarship across these rich collections; Linked Art II will continue a partnership setting an international agenda to realise this platform through a common data model, building capacity for future collaborative implementations and research investigations.

In the first phase of this work, a research network was formed to bring together experts who are collaborating on the design of the common data model. The Linked Art II project continues this work, but also seeks to trial and test the model through a series of feasibility studies and proof of concept implementations.

These 'exemplars' will be developed in collaboration with project partners and the wider Linked Art community; two exemplars will be selected via an open call for collaboration. The project will publish documentation and explanation of the exemplars on the Linked Art website so that others can understand and learn about the practicalities of Linked Art adoption.

The project is led by the University of Oxford and the J. Paul Getty Trust, with project partners from the UK and US including: the American Numismatic Society, the National Gallery (London), the National Gallery of Art (Washington D.C.), Newfields, the Philadelphia Museum of Art, the Smithsonian Institution, the University of the Arts London, the Victoria & Albert Museum, and the Yale Center for British Art.

The project will advocate Linked Art adoption amongst the cultural heritage community in the UK and US through a series of outreach workshops, disseminating discussion points and conclusions from the network in easily understood and readily available forms, and enabling the wider sector to benefit from the transformative step-change offered by Linked Art as it evolves. 

## About the AHRC

The Arts and Humanities Research Council (AHRC) funds world-class, independent researchers in a wide range of subjects: history, archaeology, digital content, philosophy, languages, design, heritage, area studies, the creative and performing arts, and much more. This financial year the AHRC will spend approximately £98 million to fund research and postgraduate training, in collaboration with a number of partners. The quality and range of research supported by this investment of public funds not only provides social and cultural benefits and contributes to the economic success of the UK but also to the culture and welfare of societies around the globe.

Visit the AHRC website at: [ahrc.ukri.org](https://ahrc.ukri.org), on Twitter at [@ahrcpress](https://twitter.com/ahrcpress), and on Facebook search for the [Arts and Humanities Research Council](https://www.facebook.com/artsandhumanitiesresearchcouncil), or Instagram at [@ahrcpress](https://www.instagram.com/ahrcpress/).

