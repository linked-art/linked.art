---
title: Linked Art Data Model
---

## Introduction

The Linked Art Data Model is an application profile that can be used to describe cultural heritage resources, with a focus on artworks and museum-oriented activities. It defines common patterns and terms to ensure that the resulting data can be easily [used](/loud/) and is based on real-world data and use cases.

The model is currently under very active development in the community and the documentation is shifting to keep up with the current decisions. While the basic patterns have been fleshed out thoroughly, as we investigate more use cases, the model should be expected to change to reflect these new discussions. The documentation is not always up to date with the discussions, and sometimes there are bugs in the rendering. Please bear with us while we do our best to ensure that the result is as considered, accurate and usable as possible.

## Model Fundamentals

Following the existing standards and best practices of the community, our starting point consists of:

* [CIDOC-CRM](http://www.cidoc-crm.org/) as the core conceptual model, giving an event-based paradigm.
    * We use a streamlined [profile](profile/) of CIDOC-CRM to ensure consistency and comprehension.
    * We also use the RDF implementation of CIDOC-CRM, given our choice of web and linked data as an integration platform.
* The [Getty Vocabularies](http://vocab.getty.edu/) as core sources of identity for domain-specific terminology
    * Core terminology is part of the application profile documentation directly, when interoperability between systems relies on the selection.
    * Other best practices are discussed in the [vocabularies best practice](/community/best-practices/vocabularies/) section.
* The concrete expression of the profile and access to data is fully covered in the [API](/api/) documentation.
    * The core serialization format is [JSON-LD 1.1](https://w3.org/TR/json-ld11)
    * The access mechanism is designed to be as simple as possible to publish and consume, following basic REST and web patterns.

These are then expanded on in order to fulfill shared use cases and common requirements, as they become known.

## Model Components

The model can be treated as interlinking components that describe aspects of the events of interest. 

* [Introduction](intro/) on how to read the documentation
* [Basic Patterns](base/) shared across the model
* [Object](object/) descriptions
* [People and Organizations](actor/)
* [Places](place/)
* [Digital Integration](digital/)
* [Provenance](provenance/) of Objects
* [Collections](collection/) and Sets
* [Exhibitions](exhibition/) of Objects
* [Primary Sources](document/) of information
* [Assertion](assertion/) level metadata
* [Dataset](dataset/) level metadata

An index of all of the classes, properties and identities used:

* [Index of Examples](example_index.html)

## Scope and Process

### Development Process

The desired target model for Linked Open Data in the Art domain is one with the following properties:

* Captures as much of the information that we know about the resources as possible
* Can be productively used via easy to implement [services](/api/)
* Provides interoperability with other related data sets
* Solves actual challenges, which are documented as use cases

Successful models are developed:

* iteratively (we will not get it right the first time)
* responsively (we will change the model in response to feedback and concerns)
* responsibly (we will consider changes and features carefully with respect to complexity and value)
* collaboratively (we will engage with the community, projects and individuals early and often)

For more information about how you can participate in Linked Art, please see the [Community](/community/) section of the website.

### Scope Limitations

* Interoperability
    * The goal of the work is interoperability between systems, not to provide a comprehensive data model to describe everything that a single institution might know. This implies that management and production of the data is out of scope as a system specific concern. Similarly, the exact models used within those systems are not our concern. These would otherwise violate the technology independency principle. Open access is not a requirement, but the intent to publish beyond system boundaries is.
* Complex Bibliography
    * The thorough description of bibliographic resources in Linked Data is the subject of several ongoing discussions in the Library domain. We feel that the Art and Museum community should adopt whatever solution is devised by the experts in that field for complex bibliographic description, if necessary beyond the model described for documents generally.
* Data Provenance 
    * Recording the individual events in which the data itself is created, modified and managed is out of scope of this work. The global Linked Open Data community has various approaches to this problem, with varying degrees of complexity and accuracy. Given the relative infancy of the work in the Art domain, we feel that adding this is an unnecessary burden at this stage at any level below the entire dataset. 
* Quantification of Uncertainty
    * Similarly, the degree of certainty about the data being expressed is valuable and of interest to researchers, but requires a significantly more complex environment. This would also prove an unsustainable burden, and is impractical to use even if it were provided.
