---
title: "Concepts"
---

[TOC]

## Introduction

Concepts are an important aspect of Linked Art, and encompass "units of thought" from classifications of objects or other entities, to languages, materials and beyond. For the most part, Linked Art leverages the Getty's Art and Architecture Thesaurus (AAT) for concepts rather than defining our own, however the model only [requires](/model/vocab/required/) the use of AAT terms in a very limited number of situations.

When it is useful or necessary to define a new concept, or to redefine an existing one in order to add new information, then we need to have a model and corresponding data for those concepts rather than just a URI. This page describes how we model concepts in Linked Art.

## Concept Classes 

There are five core classes for concepts:

* `Type` is the catch-all, general concept class. The following classes are sub-classes of it.
* `Currency` is a financial currency. Instances of it are used as the value of the `currency` property for monetary amounts. This is typically only needed for detailed [provenance](/model/provenance/acquisitions/) information.
* `Language` is a language understood natively by humans, including via speech, writing or gesture. Instances of it are used as the value of the `language` property on Linguistic Objects.
* `Material` is a physical material type, such as wood, gold or oil paint. Instances of it are used as the value of the `made_of` property on Human-Made Objects.
* `MeasurementUnit` is a unit that clarifies how to understand the value of a dimension, such as seconds, meters or kilograms. Instances of it are used as the value of the `unit` property on Dimensions.

All of the types are used in the regular `type` property, but care should be taken to use the right class whenever possible rather than always falling back to `Type`.

__Example:__

A minimal record for a concept of a Painting.

```crom
top = model.Type(ident="painting/1", label="Painting")
```

## Importance of Equivalents

If new information is to be added to an existing concept, or it is needed as a record in a local system without changes, then including references with the `equivalent` property to existing identifiers for the new record for the concept is very important for semantic interoperability. This is described also in the [basic patterns](/model/base/#equivalent-data-uris) and in the [record reference](/api/1.0/shared/reference/) API pattern but bears repeating here.

This applies both in the new concept record, as in the example below, but also in any reference from another record to that record.

__Example 1:__

A local record that sets a different primary name, but is equivalent to the AAT concept.

```crom
top = model.Type(ident="painting/2", label="Local Copy of Painting")
top.identified_by = vocab.PrimaryName(content="Painting")
top.equivalent = model.Type(ident="http://vocab.getty.edu/aat/300033618", label="painting (visual art)")
```

__Example 2:__

The Night Watch is a painting, using the local record with an equivalent of the AAT concept.

```crom
top = model.HumanMadeObject(ident="nightwatch/52", label="Night Watch by Rembrandt")
ptg = model.Type(ident="painting", label="Local Copy of Painting")
ptg.equivalent = model.Type(ident="http://vocab.getty.edu/aat/300033618", label="painting (visual art)")
top.classified_as = ptg
```


## Partitioning versus Classification





## Concept Schemes

## Creation and Influences

