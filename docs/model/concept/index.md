---
title: "Concepts"
---



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
top.equivalent = model.Type(ident="http://vocab.getty.edu/aat/300033618", label="painting (visual works)")
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

When it comes to concepts, it is easy to confuse the distinction between the concept being a part of a broader concept, and being classified as a type of concept. The broader concept is a concept that the narrower concept is part of, along with other. The broader concept is a more general concept than the narrower one. For example visual works is a more general concept than the concept of paintings, animals is a more general concept than mammals, European is a more general concept than Dutch.

Conversely a second concept that classifies the first would be one that categorizes it but doesn't encompass it directly. For example, type of work is the category for the concept of painting, taxonomic rank would be a category for mammals, and nationality would be a category for Dutch.

Concepts can, and should, have both broader terms and classifications, as demonstrated in the above examples.

__Example:__

The concept of painting is a type of work, and has a broader concept of visual artworks.

```crom
top = model.Type(ident="painting/3", label="Local Copy of Painting")
top.equivalent = model.Type(ident="http://vocab.getty.edu/aat/300033618", label="painting (visual works)")
top.broader = model.Type(ident="http://vocab.getty.edu/aat/300191086", label="visual works")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300435443", label="type of work")
```

## Concept Schemes and Sets

Another way to group concepts is within a concept scheme (such as AAT), or within a set of concepts that have been collected together for some purpose. The set of concepts might be to collect together concepts that have a certain usage but aren't within a single hierarchical structure, such as types of statement, object or work. Concepts can be in multiple sets at once, and those sets can also be arranged hierarchically.  This grouping is a third, completely orthogonal way to arrange concepts beyond partitioning and classifying.

__Example:__

The concept of painting is in the Local Concept Scheme.

```crom
top = model.Type(ident="painting/4", label="Local Copy of Painting")
top.member_of = model.Set(ident="conceptScheme", label="Local Concept Scheme")
```

## Creation and Influences

Some concepts are the coordination or compilation of other concepts or entities. For example the concept "history of France" could be thought of as being the concept "history" as it relates to the place "France". Or the concept "history of France, 20th century" would be the same with an additional related period of time.

As these related entities are not necessarily also concepts, they cannot be part of the narrower/broader hierarchy -- the "history of france" concept cannot have a broader relationship to France, because France is an instance of `Place`, not of `Type`.

In order to manage these sorts of relationships, we use the `influenced_by` property of the `Creation` of the concept, which can refer to any entity.

__Example:__

The concept "history of France" is influenced by the concept of "history" and the place "France".

```crom
top = model.Type(ident='historyFrance/1', label="History of France")
cre = model.Creation()
top.created_by = cre
cre.influenced_by = model.Type(ident="history", label="History")
cre.influenced_by = model.Place(ident="france", label="France")
```

## Alignment with SKOS

This model is heavily influenced by and highly compatible with [SKOS](https://www.w3.org/TR/skos-primer/) the Simple Knowledge Organization System specification from the W3C. Concepts in Linked Art could easily be skos:Concepts, with different types of name (called labels in skos), descriptions/notes, narrower and broader concepts and other relationships. Coordinated concepts are managed through the creation influences pattern. Concept Schemes in SKOS are modeled as Sets in Linked Art. 

As such, any skos described concept should be able to be transformed to Linked Art with minimal difficulty.