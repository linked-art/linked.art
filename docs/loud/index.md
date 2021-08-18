---
title: "LOUD: Linked Open Usable Data"
---

## Introduction

[Linked Open Data](http://5stardata.info/en/), with its five stars of excellence, changed the way that we publish data on the web. It gave us a short and very practical checklist that we could use to go from thinking about semantics to publishing actual data. It promotes openness, standards, and linking between systems as necessary for reuse. 

But it comes exclusively from a publishing perspective, and does not make any recommendations about how to publish data in a way that is usable by potential consumers. In the intervening time, the web community has recognized that we need 5 more stars, or design principles, to promote data consumption. If our data isn't used, then no value is gained from the resources that were invested in its creation, publication, maintenance and improvement.  If we want our data to be used, then it needs to be **usable**: Linked Open Usable Data.

## Usability

According to wikipedia,

> ... *usability* is the degree to which [a thing] can be used by specified consumers to achieve [their] quantified objectives with effectiveness, efficiency, and satisfaction in a quantified context of use.

Meaning that usability is dependent upon the audience. The audience for data is developers, and the user interface for developers is the API by which they get access to the data. The API for LOD is via HTTP, which is well understood, but also dependent on the ontology.  Ontologies are designed primarily for semantic or theoretical correctness, which is the least practical concern. We need to balance the trade-offs between completeness and precision of expression and the usability of the resulting data constructs.

JSON-LD allows for some mapping of ontological constructs into JSON, the lingua-franca of modern developers and is a cornerstone technology of LOUD.  Five design principles are the baseline for usability.


## Design Principles of LOUD

### A. The right **A**bstraction for the audience

Developers do not need the same level of access to data as ontologists, in the same way that a driver does not need the same level of access to the inner workings of their car as a mechanic. Use cases and requirements should drive the interoperability layer between systems, not ontological purity.

### B. Few **B**arriers to entry

It should be easy to get started with the data and build something. If it takes a long time to understand the model, ontology, sparql query syntax and so forth, then developers will look for easier targets.  Conversely, if it is easy to start and incrementally improve, then more people will use the data.

### C. **C**omprehensible by introspection

The data should be understandable to a large degree simply by looking at it, rather than requiring the developer to read the ontology and vocabularies. Using JSON-LD lets us to talk to the developer in their language, which they already understand.

### D. **D**ocumentation with working examples

You can never intuit all of the rules for the data. Documentation clarifies the patterns that the developer can expect to encounter, such that they can implement robustly. Example use cases allow contextualization for when the pattern will be encountered, and working examples let you drop the data into the system to see if it implements that pattern correctly.

### E. Few **E**xceptions, instead many consistent patterns

Every exception that you have in an API (and hence ontology) is another rule that the developer needs to learn in order to use the system. Every exception is jarring, and requires additional code to manage. While not everything is homogenous, a set of patterns that manage exceptions well is better than many custom fields.


## Examples of systems following the LOUD principles

* [IIIF](https://iiif.io/) and especially the [Presentation API, version 3.0](https://iiif.io/api/presentation/3.0/)
* [Web Annotation](http://www.w3.org/TR/annotation-model)
* And of course ... Linked Art.

## Further Resources

Videos:

Watch Rob's LOUD keynote at Europeana Tech in 2018:

<iframe width="560" height="315" src="https://www.youtube.com/embed/r4afi8mGVAY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Or check out some relevant slidedecks:

<iframe src="//www.slideshare.net/slideshow/embed_code/key/BMdlmZ7ewadpGr" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/azaroth42/the-importance-of-being-loud" title="The Importance of being LOUD" target="_blank">The Importance of being LOUD</a> </strong> from <strong><a href="https://www.slideshare.net/azaroth42" target="_blank">Robert Sanderson</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/bopQK4FdYcUDpp" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/azaroth42/standards-and-communities-connected-people-consistent-data-usable-applications" title="Standards and Communities: Connected People, Consistent Data, Usable Applications" target="_blank">Standards and Communities: Connected People, Consistent Data, Usable Applications</a> </strong> from <strong><a href="https://www.slideshare.net/azaroth42" target="_blank">Robert Sanderson</a></strong> </div>

<iframe src="//www.slideshare.net/slideshow/embed_code/key/uo5ilgP1YF9uPV" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/azaroth42/illusions-of-grandeur-trust-and-belief-in-cultural-heritage-linked-open-data" title="Illusions of Grandeur: Trust and Belief in Cultural Heritage Linked Open Data" target="_blank">Illusions of Grandeur: Trust and Belief in Cultural Heritage Linked Open Data</a> </strong> from <strong><a href="https://www.slideshare.net/azaroth42" target="_blank">Robert Sanderson</a></strong> </div> 


