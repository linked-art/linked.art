---
title: Linked Art API 1.0
---

## Status of this Document

**This version:** 0.9

**Latest Stable Version:** TBA

Versions before 1.0 are considered to be **unstable**. This means that any changes may be made at any time, without concern for compatibility. Version 0.9 is reserved for implementation feedback, and is considered as a release candidate for 1.0. Version 1.0 is expected by the end of calendar year 2024 (delayed due to COVID and other related circumstances).

The Linked Art API is published and maintained by the [Editorial Board](../../community/index.md#editorial-board) under the [CC BY 4.0 license](http://creativecommons.org/licenses/by/4.0/).

## Introduction

The model, or application profile, defines the aspects of the conceptual model, ontologies and vocabulary terms that are used by Linked Art. It is not defined with respect to any specific technical method of interaction, for retrieving, updating, harvesting, searching or browsing, allowing many different possible implementations.

This section of the website documents the web-based API, or Application Programming Interface, by which applications can interact with the data from a conforming publisher. This API has been designed with several design principles in mind to ensure that it is as usable as possible for software developers. The documentation is divided into several sections, separating protocol interactions over HTTP from format decisions about the structure of the JSON returned and the links between different JSON endpoints. The endpoints are split up by the core entities of the model, with shared constructs such as Names and Identifiers being described separately.

## The Linked Art APIs

  * Fundamentals
    * [Design Principles](principles/) - The underlying principles guiding decisions for the design of the API
    * [JSON-LD Considerations](json-ld/) - Core JSON and JSON-LD details
    * [Protocol](protocol/) - Making API requests over the web via HTTP(S)
  * APIs
    * Core Descriptive APIs
       * [Entity Descriptions](endpoint/) - The objects, people, places and other entities described in Linked Art, as JSON-LD
       * [Shared Constructs](shared/) - Patterns that are shared between descriptions
       * [Versioning](hal/) - Declaring API versions
       * [JSON Schema](schema_docs/) - JSON Schemas with documentation for the APIs
       * [Class Reference](classes) - Which ontology class is which end point?
    * Hypermedia and Search
       * [Hypermedia](hal/) - API specific affordances to convey the version of the document, and links to search endpoints
       * [Web Integration](ecosystem/) - Functional APIs to promote discovery, harvesting and other cross-system interactions    


## API Versioning

We follow the notion of [Semantic Versioning](https://semver.org/spec/v2.0.0.html), with a structure of _Major.Minor.Patch_ in the version numbers.  All minor releases are backwards compatible with their major version, but may add new features or clarify technical aspects that were not well defined. Patch releases are only for documentation changes that do not affect functionality, and will be made in-place without a change to the documentation's URI. Major releases are reserved for backwards incompatible changes, and will be made sparingly.

