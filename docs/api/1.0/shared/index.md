---
title: "Linked Art API: Shared Data Structures"
---

[TOC]

## Introduction

These data structures are shared between many endpoints, within the main response. 

## Data Structures

* [Activities](activity/) - Creations, Publications, Births/Deaths and other activities which are embedded in the main entity's record
* [Digital Links](digital/) - Links to other digital content such as web pages and images
* [Dimensions](dimension/) - Dimensions of the resource with a given unit and type (e.g. 20 inches wide)
* [Identifiers](identifier/) - Identifiers for the resource (e.g. Accession Number of 1997-1234)
* [Monetary Amounts](money/) - Monetary amounts in a given currency (e.g. 10000 US Dollars)
* [Names](name/) - Names in a human language that have been given to the resource (e.g. Mona Lisa in English)
* [Rights](right/) - Structured rights assertions for licenses or property rights
* [References](reference/) - References to another entity in the system (e.g. the reference from a painting to the artist's information)
* [Statements](statement/) - Human readable texts that describe the resource (e.g. a Materials statement)
* [TimeSpans](timespan/) - Spans of time, with fuzziness at each end (e.g. 1950 to 1955)
* [Types / Concepts](type/) - References to types that further clarify the entity (e.g. Painting rather than Object)
* [Relationships](assignment/) - Relationship assignments between entities (e.g. related works, family relations)


## Contexts and URIs

Note that data structures embedded within the records available from endpoints do not have their own `@context` entries, as they use the context document from the main record. If the data structure is shared separately using the linked art format, then it MUST have the `@context` reference added.

If there is an embedded structure (rather than a reference to another record) that has its own URI given in `id` at which data can be retrieved, and there is more information there about the entity, then the structure in the linked art record MUST have a property called `_complete` with the value of `false`. This will enable consumers of the data to know that it could be valuable to retrieve the data from the URI given in the `id` field. Otherwise, the expectation is that the URI in `id` is informational only.


```crom
top = model.HumanMadeObject(ident="auto int-per-segment")
n = vocab.PrimaryName(ident="auto int-per-segment", content="Hacha")
n.language = vocab.instances['spanish']
n._complete = False
top.identified_by = n
```
