---
title: API Design Principles and Requirements
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---

[TOC]

The initial principles are derived from the [IIIF Design Patterns](https://iiif.io/api/annex/notes/design_patterns/), as a very successful approach to designing APIs in the cultural heritage domain.

# Design Principles

## 1. Scope design through shared, consistent use cases

The Linked Art APIs, like the model, are shaped by shared, documented, and well-understood use cases. Shared understanding promotes interoperability, and the specifications are more likely to be implemented if the results solve real, not speculative, problems. Assessment of use cases is a key factor in the process of determining which features should be included or prioritized in the APIs' representation of the model.

The intent of adopting this principle is to keep the resulting APIs as practical as possible and to solve real problems. Implementers will invest time in solutions that solve their problems, and not speculative or abstract ones. If the use case is shared by multiple organizations, then there is a need for interoperability.

## 2. Design for international use	

Internationalization of text is important in all aspects of the model and APIs. If content cannot be provided using the institution's native language, then that institution will seek a more appropriate specification. 

The intent of adopting this principle is to ensure there are no language-based barriers to adoption for the APIs.

## 3. As simple as possible, but no simpler

The APIs are designed to reduce the complexity to the lowest possible point at which the use cases that feed them can be met. They should make simple things easy and complex things possible. They should allow implementers to build up from a minimum viable product in stages and incrementally enable more complex use cases, rather than needing to implement complex and perhaps unnecessary patterns to even get started.

The intent of adopting this principle is to ensure the adoption of the specifications is as high as possible. Simplicity is often a trade-off between parties, and must take into account the generation and publishing of the data on the server side, and the consumption and processing of the data on the client side. 

## 4. Avoid dependency on specific technologies

The APIs should be able to be implemented without requiring any particular infrastructure of technology stack.  While the APIs must make choices for the sake of interoperability, these choices must be weighed as to how closely tied they are to specific products or environments. 

The intent of adopting this principle is to ensure that the specifications can be implemented in a variety of languages and styles. It results from the combination of the previous two patterns.


## 5. Use REST / Don’t break the web

The APIs should work with the web, rather than against it, in terms of interactions and web infrastructure such as authentication and caching. The API responses must be able to be trivially cached without complex invalidation algorithms, and easy to understand how to interact with via common network protocol interactions.

The intent of adopting this principle is to ensure that the specifications are cacheable and performant, at the same time as being easy to understand and implement.

## 6. Design for JSON-LD, while following LOD principles

The APIs are designed for JSON-LD as the primary serialization, as the easiest to understand serialization. This is described in more detail in the [JSON-LD Documentation](../json-ld/).

The intent of adopting this principle is to ensure that the representation of the Linked Data is as easy to use as possible without the need for a full RDF development suite. Developers must be able to treat the representation as plain JSON, with a predictable structure. This ease of understanding increases the likelihood of wide spread adoption.

## 7. Follow existing standards, best practices, when possible

While it is not always possible, the APIs (and model) should following existing standards and best practices. This is tempered by the need for ease of understanding, implementation and the timing of standards evolution and updates: exceptions are made when the cost of following the best practice would prove to be a significant barrier to understanding or implementation, and hence adoption. If a standard proves to be unusable for some reason, every attempt will be made to influence the evolution of that standard rather than competing with it.

The intent of adopting this principle is to ensure the continued understanding and technical integration of the APIs within the wider environment of web-based cultural heritage data. 

## 8. Define success, not failure (for extensibility)

The API should define the expected functionality and how to request it, rather than limiting the interpretation of the data. Any data structure outside of those defined by the APIs (and model) is able to be used by implementers, keeping in mind that future official API versions might make it inconsistent.

The intent of adopting this principle is to enable experimentation by implementers, thereby encouraging the early adoption and validation of new (minor) versions.

## 9. Don't fear the network

Any networked information requires the network for access.  While basic information must be available relatively quickly to ensure a good user experience for human users, the management of information and the ease of producing a data-publishing implementation must also be considered.  As demonstrated by the adoption of IIIF, the importance of having many possible publishing environments outweighs the complexity of having easy to implement consuming implementations.  The few consuming implementations need to be good, but good does not imply being able to be written in a weekend.  There are many more concerns to writing good client-side implementations than just network access.


# Requirements and Design Specifics

The following requirements are expressed to clarify the principles in practical, implementation-based terms.

## Trivial to Implement


__It must be possible to implement by just putting files on disk containing the data__

Implementation of the core APIs must not require a database or any other dynamic or interactive system.  The availability of such a system might (indeed certainly would) make the implementation better and easier to maintain, but must not be required.  

__It must be possible to hand create the data files__

The files on disk should not *require* code to create, even if this might make it significantly easier. Writing JSON in a text editor should be a methodology that works, even if it takes a lot of time. 

__The number of responses and the responses themselves should both be as small as possible, while remaining consistent__

While consistency and availability of the data to the processor is more important than the size of the response, if it is possible to keep responses small, then that is advantageous in terms of network interaction speed and human-writable files from the previous two requirements. 


## Consistency across Representations

__Each statement should only be in one response document, if possible__

If the same statement can be in multiple places, then they can become out of sync without a dynamic database to manage the API data.  This requirement is a consequence of the first requirement to not require a database. Performance issues might require specific exceptions to this, especially regarding the Names of resources to be presented to end users, but should be extremely limited to avoid inconsistency of data.


__If a resource has references from multiple other resources, then it needs to be in its own response__

This is derived from the previous requirements. If the same resource is described in multiple locations, then it clearly is not only in one response document.


__Inverse relations are a (special) case of the same information__

Inverse relationships are very common in the ontology, as almost every relationship is bidirectional. For example, if a Person produced an Object, then the Object was produced by the Person.  However only one of these assertions is necessary, as otherwise we run afoul of the requirement to have as little redundancy as possible in terms of information repetition.

Each relationship should be thus encoded only a single direction, however a separate API could retrieve the inverse relationships for a particular resource. There might also be performance oriented exceptions to this rule, in order to provide easy on-ramps into the data.

## Division of Information

__Partitioning, or other 1 to many relationships, should come from the many to the 1__

This requirement comes from keeping the responses manageable in terms of size.  If every page in a book is described with its own separate entity, as the pages were individually digitized and the image thus needs an entity that it depicts, then the book's representation would consist almost entirely of a list of links to the pages that it contains.  Instead, the page would refer to the book using a `part_of` relationship, and the book would have a separate API for inverses to discover the `part` relationships.


__The rules for which representation a statement appears in should be as computationally deterministic and as simple as possible__

This is to ensure that a system processing knowledge from a triplestore, rather than hand crafting the responses, can easily implement the API.


__If a resource does not require incoming references, and is 1:1 with its parent resource, it is embedded in its parent__

This notably includes the beginning and end of existence classes for all entities, as in the profile they only ever begin or end a single entity's existence. It also includes data constructs that are specific to the entity, such as Name, Identifier, Dimension, TimeSpan and MonetaryAmount.  This is to cut down the number of resources that need to be separately maintained at persistent URIs.


## URI Requirements

__If a resource does not need to be dereferenced separately then it does not need to have its own URI__

Nodes embedded in the graph, such as Name and Dimension, do not need to have their own URI.  They can be, in RDF terms, blank nodes.  If they needed to be referenced separately, then they would have their own endpoints and API documentation.  They are able to have their own URIs, but this must not be necessary.

__There are no requirements about the URI structure for the API endpoints__

We do not make any hard requirements about the structure of any URI that is dereferenced (or not dereferenced). This enables a broad set of implementations to be layered into existing sites, or to be implemented with whatever technology backend is available.  Any absolute requirements that can be depended on by a consuming implementation for the construction of those URIs breaks the "opaque URI" best practice, and reduces implementation possibilities.

Instead, there are best practices for URIs documented in the [protocol](../protocol/) section that may be adopted for convenience, but must not be assumed to be adopted by implementations.
