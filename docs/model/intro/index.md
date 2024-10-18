---
title: "Introduction to the Model"
up_href: "/model/"
up_label: "Model Overview"
---

[TOC]

## Introduction

The intended audience for the data model documents is people interested in understanding how to model art historical information following the best practices of the museum domain, combined with the best practices of the linked data and web communities, or what to expect when consuming that information presented on the web.  This audience could be described as collections data managers, data engineers and software developers. 

Given this audience and intended use, the documentation is divided up by the primary entities that make up object descriptions and information systems, such as the artwork itself and the visual or textual content that it shows, the people and organizations that participate in activities (sometimes called "constituents" or "agents" in information systems), places and integration points with digital content. The descriptions are then oriented around progressively more complex use cases for those areas, such that it is hopefully easy to find the easy patterns and possible to find the less common or more complex ones.

There are always limitations to documentation, and not all use cases can be explicitly described.  This limitation currently includes the lack of search functionality across the documentation, but the [example index](/model/example_index) can serve as a useful browsing point for the terms in the models.

## Concrete Examples

The documentation uses the following real world objects for the majority of its examples, along with the related works, people, places, concepts, events and organizations:

* [Jeanne (Spring)](https://www.getty.edu/art/collection/object/103QTZ) by Manet, from the Getty Museum
* [The Night Watch](https://www.rijksmuseum.nl/en/collection/sk-c-5) by Rembrandt, from the Rijksmuseum
* [Bust of a Man](https://collections.britishart.yale.edu/catalog/tms:54430) by the Studio of Francis Harwood, from the Yale Center for British Art

The descriptions of the objects as examples are not intended to replace or compete with the organizations' own descriptions, and the URIs and identifiers generated for them should not be used apart from in the context of the Linked Art documentation. If you wish to cite the objects or their real descriptions, please see the links above for persistent identifiers and citation guides.

The Linked Art community is grateful to the owning organizations for letting us use their beautiful objects and images.
If the above objects do not cover the particular use case (for example the destruction of an object), then the documentation will link to a specific real world example in the appropriate section.

## Basic Terminology

We try to be consistent in our use of terminology in the description of the model, following these definitions:

* Object: A physical thing such as a painting, sculpture or laptop.
* Work: A conceptual thing, born of human creativity, that can be expressed in an Object. Works can be purely abstract (the "work" of an exhibition), based on language (the text of a book), or based on image (the visual content shown by a photograph). Future versions will investigate auditory works.
* Concept: A purely conceptual categorization, which is not itself a work. 
* Entity: Any of the above types.


## Reading the Examples

Every use case and section has an example that can be copied, in the target JSON-LD syntax.  The syntax has some syntax highlighting and indentation to assist with understanding that is not necessary for actual data. If you hover the mouse over a key (in green) in the examples, or a reference to a term in the documentation such as `identified_by`, then the expanded form of that term in RDF will be given in a callout window.

Below each example is an automatically generated diagram for the same content.  This automation means that some diagrams are less readable than others, but they have found to be more useful to include in general than to leave out. Work is ongoing to improve the styling and layout of the diagrams, and to include similar functionality to link to the expanded terms. The colors of the nodes in the examples are meaningful, and explained in the table below.

For each example there is also a set of links to other representations, including the raw JSON as a file (for example to use to test a client implementation), the JSON-LD presented in the JSON-LD playground, the linked data expressed as raw Turtle, and the same turtle in a syntax-highlighting environment.

| Color         | Description |
|---------------|-------------|
| Brown         | Physical things. Classes: `HumanMadeObject` |
| Green         | Places.  Classes: `Place` |
| Red/Pink      | Actors.  Classes: `Person`, `Group` |
| Orange        | Types and controlled vocabulary terms. Classes: `Type`, `Language`, `Currency`, `MeasurementUnit`, `Material` |
| Yellow        | Conceptual things, including image and text content, rights and sets. Classes: `PropositionalObject`, `VisualItem`, `LinguisticObject`, `Set`, `Right` |
| Pale Yellow   | Names and Identifiers. Classes: `Name`, `Identifier` |
| Blue          | Events and Activities. Classes include: `Event`, `Activity`, `Acquisition`, `Production`, `Creation`, and so on |
| Pale Blue     | Timespans. Classes: `TimeSpan` |
| Gray          | Dimensions and other data structures. Classes: `Dimension`, `MonetaryUnit` |
| Purple        | Digital Objects. Classes: `DigitalObject`, `DigitalService` |
| White         | The class itself, presented in a rectangle with square corners |
| Pale Gray     | Literal values, presented in a rectangle with slightly rounded corners |
