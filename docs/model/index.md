---
title: Linked Art Data Model
---

## Status of this Document

**This version:** 1.0.0

**Latest Stable Version:** 1.0.0

The Linked Art Data Model is published and maintained by the [Editorial Board](../community/index.md#editorial-board) under the [CC BY 4.0 license](http://creativecommons.org/licenses/by/4.0/).

## Introduction

The Linked Art Data Model is an application profile that can be used to describe cultural heritage resources, with a focus on artworks and museum-oriented activities. It defines common patterns and terms to ensure that the resulting data can be easily [used](/loud/) and is based on real-world data and use cases.

Development of the model for version 1.0 has finished, and the documentation is being tidied for an official release shortly. All of the decisions have been made and documented, all that remains is checking for consistency and accuracy. This does not mean that work stops however -- the community will continue to improve the model over time, and has identified issues to discuss for future versions. 

## The Linked Art Model

* Introduction
    * [How To Read](intro/) the model documentation, and model versioning
    * [Basic Patterns](base/) used throughout the model
* Artworks and other Physical Objects
    * [Objects](object/) 
    * [Digital Content](digital/) about or depicting the objects
    * [Collections](collection/) of objects, and other sets
    * [Provenance](provenance/) of objects
    * [Exhibitions](exhibition/) of objects
    * [Conservation](conservation/) of objects
* Related People, Places, Concepts and Events
    * [People and Organizations](actor/)
    * [Places](place/)
    * [Concepts](concept/)
    * [Events](event/)
    * [Vocabulary Terms Used](vocab/)
* Cultural Context
    * [Textual Documents](document/) 
    * [Archival Hierarchies](archives/)
    * [Specific Assertions](assertion/)


## Development of the Model

### Model Background

Following the existing standards and best practices of the community, our starting point consists of the following background standards:

* [CIDOC-CRM](https://www.cidoc-crm.org/) as the core conceptual model, giving an event-based paradigm.
    * We use a streamlined [subset](profile/) of [CIDOC-CRM 7.1.3](https://www.cidoc-crm.org/Version/version-7.1.3) to ensure consistency and comprehension.
* The [Getty Vocabularies](http://vocab.getty.edu/) as core sources of identity for domain-specific terminology
    * Terminology is divided into three lists: [required](vocab/required/), [recommended](vocab/recommended/) and [optional](vocab/optional/) based on whether systems will be interoperable if different choices were made.
* The concrete expression of the profile and access to data is fully covered in the [API](/api/) documentation.
    * The core serialization format is [JSON-LD 1.1](https://w3.org/TR/json-ld11)


### Scope and Process

#### Development Process

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

#### Scope Limitations

* Interoperability
    * The goal of the work is interoperability between systems, not to provide a comprehensive data model to describe everything that a single institution might know. This implies that management and production of the data is out of scope as a system specific concern. Similarly, the exact models used within those systems are not our concern. These would otherwise violate the technology independency principle. Open access is not a requirement, but the intent to publish beyond system boundaries is.
* Complete Bibliographic and Archival Description
    * The thorough description of bibliographic and archival resources in Linked Data is the subject of several ongoing discussions in the Library and Archives domains. Linked Art provides an on-ramp to those domains by defining the basic descriptions using our shared patterns, but does not attempt to be complete in these domains.
* Data Provenance 
    * Recording the individual events in which the data itself is created, modified and managed is out of scope of this work. The global Linked Open Data community has various approaches to this problem, with varying degrees of complexity and accuracy. Given the relative infancy of the work in the Art domain, we feel that adding this is an unnecessary burden at this stage at any level below the entire dataset. 
* Quantification of Uncertainty and Belief
    * Similarly, the degree of certainty or beliefs about the data being expressed is valuable and of interest to researchers, but requires a significantly more complex environment. This would also prove an unsustainable burden, and is impractical to use even if it were provided.
