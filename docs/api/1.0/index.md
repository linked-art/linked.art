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


## Linked Art APIs

### Core Entity Description API

The core Linked Art API is to provide records describing the entities following the model serialized as JSON-LD according to the Linked Art context document. The response also has a non-semantic block that follows the Hypertext Application Language (or HAL) specification to provide links to versions, searches, and other related information.

* [Entity Description Endpoints](endpoint/) - Retrieving the objects, works, people, places and other entities as JSON-LD
    * [Shared Data Structures](shared/) - Shared patterns that are used by multiple descriptions
    * [JSON Schema](schema_docs/) - JSON Schema definitions, with documentation, for the API
* [Hypertext Application Language](hal/) - Versioning, cross-format links, and other HAL links


### Search API

Linked Art defines a format for responses to search requests, but does not define a query language for defining the search at the present time. The intended use of the standardized response is that the queries can be referenced via HAL links from within the records, and the consuming application will receive a consistent format when following the link. Individual implementations might use [SPARQL](https://www.w3.org/TR/sparql11-query/), [GraphQL](https://graphql.org/) , Cypher, the Elasticsearch DSL, the Solr query language or some other syntax that can be embedded in a URL without the application needing to know how to construct it.

* [Search API](search/) - The response format for Linked Art searches, and how to link to them using HAL
* [Search Links](../rels/1/) - The list of named searches for HAL links


### Data Discovery APIs

In an environment where the intent is that data is openly available for use and reuse, it is important to be able to harvest the data to a local system for processing and indexing. Subsequently it is important to be able to remain synchronized with the data, knowing when records are created, changed or deleted. It is also useful for applications to know where the data is that was used in producing a web interface for in-browser applications.

* [Discovery APIs](discovery/) - Making records available for easy harvesting and discover from HTML


## API Design Fundamentals

* [Design Principles](principles/) - The underlying principles guiding decisions for the design of the API
* [JSON-LD Considerations](json-ld/) - Core JSON and JSON-LD details
* [Protocol](protocol/) - Making API requests over the web via HTTP(S)


### API Versioning

We follow the notion of [Semantic Versioning](https://semver.org/spec/v2.0.0.html), with a structure of _Major.Minor.Patch_ in the version numbers.  All minor releases are backwards compatible with their major version, but may add new features or clarify technical aspects that were not well defined. Patch releases are only for documentation changes that do not affect functionality, and will be made in-place without a change to the documentation's URI. Major releases are reserved for backwards incompatible changes, and will be made sparingly.

