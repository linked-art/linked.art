---
title: JSON-LD Serialization
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---

[TOC]

## Introduction

JSON-LD is a Linked Open Data serialization using the popular JSON (Javascript Object Notation) format that is convenient for both backend and browser based development.  It is specified by the [W3C](https://www.w3.org/TR/json-ld11/) as an official serialization. Continued development work happens in the JSON for Linking Data W3C [Community Group](https://www.w3.org/community/json-ld/).

The serialization for JSON-LD is friendly to developers through the use of context documents that specify the mapping between the key used in the json object and the RDF predicate used in the model.  This abstraction allows the developer to work with existing patterns and frameworks, while the data is still managed as a graph underneath.  This document describes the context used for CIDOC-CRM and other ontologies.

The context that provides the mapping of the terms used in the model is published as:
> `{{ site.config.var.scheme }}://{{site.config.var.hostname}}{{site.config.base_url}}ns/v1/linked-art.json`

## Media Type

The media type to use for representations in JSON-LD using the context is:

> `application/ld+json;profile="{{ site.config.var.scheme }}://{{site.config.var.hostname}}{{site.config.base_url}}ns/v1/linked-art.json"`

This would be the value of the `Content-Type` HTTP header on responses, and if there are other representations available via content negotiation, then it can be sent in requests in the `Accept` header.


## Other Serialization Formats

Other serialization formats of the underlying graph may also be available, such as [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/), [Turtle](https://www.w3.org/TR/turtle/), other standardized formats, or even non-standardized representations. These are not required in order to fully conform with the Linked Art API, and should not be assumed to exist. How to request these alternative serializations is documented in the [protocol](../protocol/) section.


## Examples

The examples throughout the documentation use the JSON-LD serialization.  Each has a link to the raw JSON-LD, and to load it into the invaluable JSON-LD playground where you can explore the details.  Instead of trying to describe all of the predicates and classes (for that just read the CIDOC-CRM specification), we present the models for the known use cases in an attempt to be more practical and results oriented.  We strive for usability and familiarity for developers, and the examples aim to present best practices at the same time as being easy to follow.

An example of the JSON-LD serialization for a painting, that is made of watercolor on a canvas support:

```crom
top = Painting(art=1)
top._label = "Example Painting"
top.made_of = instances['watercolor']
part = SupportPart(top.id + "/part/1")
part._label = "Canvas Support"
part.made_of = instances['canvas']
top.part = part
```

## Context Design

The important part of the JSON-LD serialization is the shared context document.  This context has some design constraints that it is useful to understand before looking at the data model and mapping from the ontology.  In particular:

* The resulting JSON must be __valid__ Linked Open Data and valid JSON-LD. The nested object structure in the JSON is a result of the graph of resources. 
* The resulting JSON must be __understandable__ by developers who are unfamiliar with both the model and RDF in general. If the target technical audience was developers who had the full suite of RDF tools at their disposal, then Turtle and SPARQL would likely be preferable.  The serialization instead tries to make the content as accessible as the model will allow, to the broadest possible audience.
* The resulting JSON must be __usable__ regardless of programming language or application environment to ensure the widest possible adoption and value. The context is designed to allow as many of conveniences as possible to be used, and to maximize the situations in which it can be used.  Consistency is a core feature of usability, and as such the context tries to be as consistent as possible.

There are some challenges overlaid on these principles from the CIDOC-CRM ontology.

* The use of numbers in the class and properties runs counter to the understandable and usable principles.
* The use of - in the names of some classes and properties reduces usability, as it is not allowed as the name of a property in most programming languages.
* The use of the same name for a property, minus its number, is not possible in JSON-LD as the keys must map uniquely to a predicate.
* The use of underscores in class or property names is not common in Javascript or in RDF ontologies, which tend to prefer CamelCase.
* The same conceptual relationship between resources has different instantiations in the ontology, introducing unnecessary inconsistency. For example, the core partitioning relationships are class-specific rather than being a more obvious `part` relationship for everything. 

The context tries to manage all of these issues in a practical and programmatically accesible way from the ontology definition.

## Context

The following process is used to create the JSON-LD keys from the CIDOC-CRM ontology:

* Remove `@` symbols (`id` not `@id`) as a JSON-LD best practice
* Remove namespaces from classes and properties (`E22_Man-Made_Object` not `crm:E22_Man-Made_Object`) as unnecessary with the context mapping
* Remove the prefix numbers (`Man-Made_Object` not `E22_Man-Made_Object`) as impossible to remember
* Remove dashes (`ManMade_Object` not `Man-Made_Object`) as invalid in class names
* Use upper CamelCase for classes (`ManMadeObject` not `ManMade_Object`) as common practice
* Use lower snake_case for properties (`is_identified_by`) as generating camelCase is difficult automatically for such a broad set of terms
* Remove `is_`, `was_`, `has_` and `had_` from the beginning of properties, as being inconsistently applied in the ontology and hard to remember (`identified_by` not `is_identified_by` ; compare the `created` and `destroyed` properties, which are not of the form `was_created` in the ontology)
* Rename properties with collisions, from furthest down the hierarchy first, with a first effort of adding the range's class to the predicate name, but preferring a human understandable term 
* Rename properties that are inconsistently named, when those properties are used
* Provide a single context with all of the terms, to facilitate ease of extensions using core terminology
* Include prefixes for commonly used ontologies (`skos`, `schema`, `rdf`) and vocabularies (`aat`, `tgn`, `geonames`)

The context implements the notion that if a property can ever have multiple values, then it must always be an array. In JSON-LD this is done with `@container: @set` on such properties, and you'll see many instances of this in the examples where a property has an array with a single object inside it.

The context is designed for JSON-LD 1.1, and uses the feature known as "scoped contexts": sub-contexts that are defined per class or per relationship that apply only within that term.  This is used to map all of the the various partitioning relationships to `part` and `part_of`, regardless of the type of resource being partitioned.  This feature makes the JSON much easier to read and write, without losing the semantic precision of the separate underlying terms.

Name collisions and naming inconsistencies in the ontology have been resolved as follows:

> 
{% include "_include/prop_key_map.md" %}
