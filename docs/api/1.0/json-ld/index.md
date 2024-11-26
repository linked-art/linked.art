---
title: JSON-LD Serialization
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---



## Introduction

JSON-LD is a Linked Open Data serialization using the popular JSON (Javascript Object Notation) format that is convenient for both backend and browser based development.  It is specified by the [W3C](https://www.w3.org/TR/json-ld11/) as an official serialization. Continued development work happens in the JSON for Linking Data W3C [Community Group](https://www.w3.org/community/json-ld/).

The serialization for JSON-LD is friendly to developers through the use of context documents that specify the mapping between the key used in the json object and the RDF predicate used in the model.  This abstraction allows the developer to work with existing patterns and frameworks, while the data is still managed as a graph underneath.  This document describes the context used for CIDOC-CRM and other ontologies.

The context that provides the mapping of the terms used in the model is published as:
> `https://linked.art/ns/v1/linked-art.json`

## Media Type

The media type to use for representations in JSON-LD using the context is:

> `application/ld+json;profile="https://linked.art/ns/v1/linked-art.json"`

This would be the value of the `Content-Type` HTTP header on responses, and if there are other representations available via content negotiation, then it can be sent in requests in the `Accept` header.


## Core Requirements

There are several core requirements to keep in mind for JSON and JSON-LD representations:

* Terms are case sensitive.  `Type` (the class `crm:E55_Type`), and `type` (the property `rdf:type`) are different terms, separated only by the upper case of the initial letter. As described below, the JSON representation of the names of classes and properties is as consistent as possible.
* Properties cannot be repeated on a single object.  Instead, if there are multiple values for a property or multiple instances of a relationship, then the JSON will have an array as the value where each entry is considered to have that property. Linked Art does not use RDF's ordered lists (such as `rdf:List`) but instead relies on the order in the serialization.


## Other Serialization Formats

Other serialization formats of the underlying graph may also be available, such as [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/), [Turtle](https://www.w3.org/TR/turtle/), other standardized formats, or even non-standardized representations. These are not required in order to fully conform with the Linked Art API, and should not be assumed to exist. How to advertise and request these alternative serializations is documented in the [protocol](../protocol/) section.


## Examples

The examples throughout the documentation use the JSON-LD serialization.  Each has a link to the raw JSON-LD, and to load it into the invaluable JSON-LD playground where you can explore the details.  Instead of trying to describe all of the predicates and classes (for that just read the CIDOC-CRM specification), we present the models for the known use cases in an attempt to be more practical and results oriented.  We strive for usability and familiarity for developers, and the examples aim to present best practices at the same time as being easy to follow.

An example of the JSON-LD serialization for a painting, that is made of watercolor on a canvas support:

```crom
top = vocab.Painting(ident="auto int-per-segment", label="Example Painting", art=1)
top.made_of = vocab.instances['watercolor']
part = vocab.SupportPart(label="Canvas Support")
part.made_of = vocab.instances['canvas']
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
* Remove the prefix numbers (`Human-Made_Object` not `E22_Human-Made_Object`) as impossible to remember
* Remove dashes (`HumanMade_Object` not `Human-Made_Object`) as invalid in class names
* Use upper CamelCase for classes (`HumanMadeObject` not `HumanMade_Object`) as common practice
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
Property | Key
-------- | ---
P2 | `classified_as`
P5 | `subState`
P5i | `subState_of`
P7i | `location_of`
P9 | `part`
P9i | `part_of`
P12 | `involved`
P14i | `carried_out`
P20i | `specific_purpose_of`
P28 | `transferred_custody_from`
P29 | `transferred_custody_to`
P29i | `acquired_custody_through`
P32 | `technique`
P33 | `specific_technique`
P35i | `condition_identified_by`
P37 | `assigned_identifier`
P37i | `identifier_assigned_by`
P42 | `assigned_type`
P42i | `type_assigned_by`
P45 | `made_of`
P46 | `part`
P46i | `part_of`
P50 | `current_custodian`
P50i | `current_custodian_of`
P56 | `bears`
P65 | `shows`
P74 | `residence`
P86 | `part_of`
P86i | `part`
P89 | `part_of`
P89i | `part`
P100i | `died`
P101 | `general_use`
P106 | `part`
P106i | `part_of`
P107 | `member`
P107i | `member_of`
P127 | `part_of`
P127i | `part`
P132 | `volume_overlaps_with`
P133 | `distinct_from`
P135i | `type_created_by`
P139 | `alternative`
P140 | `assigned_to`
P148 | `conceptual_part`
P148i | `conceptually_part_of`
P151i | `participated_in_formation`
P164i | `timespan_of_presence`
P165 | `presence_of`
P165i | `incorporated_by`
P168 | `defined_by`
P172 | `spatially_contains`
P177 | `assigned_property`
P186i | `type_produced_by`
P190 | `content`
P195 | `presence_of_thing`
P195i | `thing_presence`
P196i | `thing_defined_by`
la:has_member | `member`
la:member_of | `member_of`
skos:closeMatch | `close_match`
skos:exactMatch | `exact_match`
dcterms:conformsTo | `conforms_to`
dcterms:relation | `related`
schema:genre | `style`
rdfs:seeAlso | `see_also`
rdfs:label | `_label`
sci:O13_triggers | `caused`
sci:O13i_is_triggered_by | `caused_by`
sci:O19_encountered_object | `encountered`
sci:O19i_was_object_encountered_at | `encountered_by`
