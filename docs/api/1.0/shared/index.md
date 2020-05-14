---
title: "Linked Art API: Shared Data Structures"
up_href: "/api/1.0/"
up_label: "Linked Art API"
---

[TOC]

## Introduction

These data structures are shared between many endpoints, within the main response. 

## Data Structures

* [Dimensions](dimension/) - Dimensions of the resource with a given unit and type (e.g. 20 inches wide)
* [Identifiers](identifier/) - Identifiers for the resource (e.g. Accession Number of 1997-1234)
* [Monetary Amounts](money/) - Monetary amounts in a given currency (e.g. 10000 US Dollars)
* [Names](name/) - Names in a human language that have been given to the resource (e.g. Mona Lisa in English)
* [Statements](statement/) - Human readable texts that describe the resource (e.g. a Materials statement)
* [TimeSpans](timespan/) - Spans of time, with fuzziness at each end (e.g. 1950 to 1955)
* [Types / Concepts](type/) - References to types that further clarify the entity (e.g. Painting rather than Object)
* [Entity References](reference/) - References to another entity in the system (e.g. the reference from a painting to the artist's information)

## Notes

Note that data structures, as they are embedded within the formats available from endpoints, do not have `@context` entries.  The examples for the data structures have `id` properties with identifying URIs, but these are not required.
