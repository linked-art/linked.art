---
title: "Introduction to the Model"
up_href: "/model/"
up_label: "Model Overview"
---

[TOC]

## Introduction

The intended audience for the data model documents is people interested in understanding how to model art historical information following the best practices of the museum domain, combined with the best practices of the linked data and web communities, or what to expect when consuming that information presented on the web.  This audience could be described as collections data managers, data engineers and software developers. 

Given this audience and intended use, the documentation is divided up by the primary entities that make up object descriptions and information systems, such as the artwork itself and the visual or textual content that it shows, the people and organizations that participate in activities (sometimes called "constituents" in information systems), places and integration points with digital content. The descriptions are then oriented around progressively more complex use cases for those areas, such that it is hopefully easy to find the easy patterns and possible to find the less common or more complex ones.

There are always limitations to documentation, and not all use cases can be explicitly described.  This limitation currently includes the lack of search functionality across the documentation, but the [example index](/model/example_index.html) can serve as a useful browsing point for the terms in the models.


## Reading the Examples

Every use case and section has an example that can be copied, in the target JSON-LD syntax.  The syntax has some syntax highlighting and indentation to assist with understanding that is not necessary for actual data. If you hover the mouse over a key (in green) in the examples, or a reference to a term in the documentation such as `identified_by`, then the expanded form of that term will be given in a callout window.

Below each example is an automatically generated diagram for the same content.  This automation means that some diagrams are less readable than others, but they have found to be more useful to include in general than to leave out. Work is ongoing to improve the styling and layout of the diagrams, and to include similar functionality to link to the expanded terms. The colors of the nodes in the examples are meaningful, and explained in the table below.

For each example there is also a set of links to other representations, including the raw JSON as a file (for example to use to test a client implementation), the JSON-LD presented in the JSON-LD playground, the linked data expressed as raw Turtle, and the same turtle in a syntax-highlighting environment.

| Color         | Description |
| ------------- | ----------- |
| Brown         | Physical things. Classes: `HumanMadeObject` |
| Green         | Places.  Classes: `Place` |
| Red/Pink      | Actors.  Classes: `Actor`, `Person`, `Group` |
| Orange        | Types and controlled vocabulary terms. Classes: `Type`, `Language`, `Currency`, `MeasurementUnit`, `Material` |
| Yellow        | Conceptual things, including image and text content, rights and sets. Classes: `InformationObject`, `VisualItem`, `LinguisticObject`, `Set`, `Right` |
| Pale Yellow   | Names and Identifiers. Classes: `Name`, `Identifier` |
| Blue          | Events and Activities. Classes include: `Event`, `Activity`, `Acquisition`, `Production`, `Creation`, and so on |
| Pale Blue     | Timespans. Classes: `TimeSpan` |
| Gray          | Dimensions and other data structures. Classes: `Dimension`, `MonetaryUnit` |
| Purple        | Digital Objects. Classes: `DigitalObject` |
| White         | The class itself, presented in a rectangle with square corners |
| Pale Gray     | Literal values, presented in a rectangle with slightly rounded corners |
