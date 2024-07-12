---
title: Required Vocabulary Terms
up_href: "/model/vocab/"
up_label: "Vocabulary Terms"
---

[TOC]

## Introduction

These terms are required to be used in order to facilitate even the most basic understanding of the data. If a term is listed here then you MUST NOT use a different term for the same concept, as systems are expecting these terms. This is not to say that you MUST always have the terms in every record, you might not know (for example) the shape of an object, but if you do know it, then you must use the agreed upon URI for the concept of "shape".

## Summary

For brevity in the table, the AAT URI is compacted with a namespace, however the full URI **MUST** be used in the data. For example, the URI for Primary Name is `http://vocab.getty.edu/aat/300404670`

| Name                  | URI           | Classifies | Description |
|-----------------------|---------------|------------|-------------|
| Primary Name          | aat:300404670 | Name       | The primary name of the entity |
| Display Name          | aat:300404669 | Name       | The name to use for displaying the node |
| Sort Name             | aat:300451544 | Name       | The name to use when sorting this entity with others |
| Sort Value            | aat:300456575 | Identifier | The identifier to use when sorting this entity with others |
| Statement             | aat:300418049 | Type       | A type of statement |
| Type of Work          | aat:300435443 | Type       | A type of works |
| Style                 | aat:300015646 | Type       | A style |
| Shape                 | aat:300056273 | Type       | A shape |
| Occupation            | aat:300263369 | Type       | An occupation |
| Nationality           | aat:300379842 | Type       | A nationality |
| Color                 | aat:300080438 | Dimension  | A color |
| Exhibition Activity   | aat:300054766 | Activity   | An exhibition | 
| Provenance Activity   | aat:300055863 | Activity   | A provenance activity | 
| Professional Activity | aat:300393177 | Activity   | A professional activity |
| Publication Activity  | aat:300054686 | Activity   | A publishing activity |
| Promise Activity      | aat:300435599 | Activity   | A promise |
| Collection Item       | aat:300404024 | Any        | The entity is part of a cultural heritage collection |
| Artwork               | aat:300133025 | Any        | The entity is an artwork |


See below for details about each

## Name Types

There are four required vocabulary entries for Names and Identifiers to be able to distinguish them from others. Each has particular requirements for use by the client or search system.

### Primary Name

The URI for Primary Name is: [http://vocab.getty.edu/aat/300404670](http://vocab.getty.edu/aat/300404670)

The main or primary name of the entity. Every record must have a name with the primary name classification so that user interfaces know which name to use. There may be multiple primary names for a single record, but each must have a unique language, or no language. See the [name documentation](/model/base/#names).

Example:

```crom
top = model.HumanMadeObject(ident="nightwatch/41", label="Night Watch by Rembrandt")
ttl = vocab.PrimaryName(content="The Night Watch")
ttl.language = vocab.instances['english']
top.identified_by = ttl
```

### Display Name

The URI for Display Name is: [http://vocab.getty.edu/aat/300404669](http://vocab.getty.edu/aat/300404669)

A name to use when displaying the node which has the associated name. For Statements, this is typically used by interfaces as the label for the statement. For [TimeSpans](/model/base/#time-span-details) or other structured data, it is used in place of the structured data.

Example 1:

```crom
top = model.HumanMadeObject(ident="nightwatch/42", label="Night Watch by Rembrandt")
lo = vocab.MaterialStatement(content="Oil on Canvas")
lo.identified_by = vocab.DisplayName(content="Materials")
top.referred_to_by = lo
```

Example 2:

```crom
top = model.HumanMadeObject(ident="nightwatch/43", label="Night Watch by Rembrandt")
prod = model.Production()
top.produced_by = prod
ts = model.TimeSpan()
ts.begin_of_the_begin = "1642-01-01T00:00:00Z"
ts.end_of_the_end = "1842-12-31T23:59:59Z"
ts.identified_by = vocab.DisplayName("1642")
prod.timespan = ts 
```

### Sort Name

The URI for Sort Name is: [http://vocab.getty.edu/aat/300451544](http://vocab.getty.edu/aat/300451544)

A name to use when sorting the entity along with other entities in a list. This classification can be used on the same name as the primary name, or on a different form of the entity's name. Different languages can have different sort names, however each language must not have more than one.

```crom
top = model.Person(ident="rembrandt/41", label="Rembrandt")
top.identified_by = vocab.PrimaryName(content="Rembrandt van Rijn")
top.identified_by = vocab.SortName(content="van Rijn, Rembrandt Harmenszoon")
```

### Sort Value

The URI for Sort Name is: [http://vocab.getty.edu/aat/300456575](http://vocab.getty.edu/aat/300456575)

A non-linguistic identifier to use for sorting the entity along with other entities in a list, instead of a linguistic form as described above. There must not be more than one sort value per entity. User interfaces should not render the sort value to the end user.

```crom
top = model.Person(ident="rembrandt/42", label="Rembrandt")
top.identified_by = vocab.SortValue(content="r0000011")
```

## Classification Types

There are six classifications that stand as categories when it is otherwise difficult to distinguish between very similar constructs in the same property. These are described in the [types of types section](/model/base/#types-of-types), and sometimes referred to as "meta-types". A related required term is that for color, however it classifies a Dimension rather than another Type.

### Statement

The URI for the Statement type is: [http://vocab.getty.edu/aat/300418049](http://vocab.getty.edu/aat/300418049)

There are many types of [Statements](model/base/#statements-about-an-entity), and it is impossible to enumerate all of those different types in a way that could be implemented successfully and usably. Instead, the type of the statement (e.g. materials statement) is given a meta-type of "brief text" so that they can be recognized as the type of statement.

```crom
top = model.HumanMadeObject(ident="nightwatch/44", label="Night Watch by Rembrandt")
top.referred_to_by = vocab.MaterialStatement(content="Oil on Canvas")
```

### Type of Work

The URI for Type of Work is: [http://vocab.getty.edu/aat/300435443](http://vocab.getty.edu/aat/300435443)

There are many [types of works](/model/base/#types-and-classifications) (painting, statue, print, ...) and it is equally impossible for any system to know all of them a priori. Instead the type of work of an object is classified with the Type of Work meta-type so it can be recognized.

```crom
top = vocab.Painting(ident="nightwatch/45", label="Night Watch by Rembrandt")
```

### Style

The URI for Style is: [http://vocab.getty.edu/aat/300015646](http://vocab.getty.edu/aat/300015646)

Similarly, there are many [styles](/model/object/aboutness/#style-classification) and we use aat:300015646 to distinguish a style concept from other categorizations of the work.

```crom
top = model.VisualItem(ident="nightwatch/40", label="Appearance of Night Watch")
top.classified_as = vocab.instances['baroque style']
```

### Shape

The URI for Shape is: [http://vocab.getty.edu/aat/300056273](http://vocab.getty.edu/aat/300056273)

There are, similarly, many [shapes](/model/object/physical/#shapes) and we need to distinguish shape from other classifications.

```crom
top = model.HumanMadeObject(ident="nightwatch/48", label="Night Watch by Rembrandt")
top.classified_as = vocab.instances['rectangular']
```

### Nationality

The URI for Nationality is: [http://vocab.getty.edu/aat/300379842](http://vocab.getty.edu/aat/300379842)

In the same way as for objects and works, people also have a variety of types of classification associated with them. A common one is [nationality](/model/actor/#nationality).

```crom
top = model.Person(ident="rembrandt/44", label="Rembrandt")
top.classified_as = vocab.instances['dutch nationality']
```

### Occupation

The URI for Occupation is: [http://vocab.getty.edu/aat/300263369](http://vocab.getty.edu/aat/300263369)

People can also be categorized by their occupation.

```crom
top = model.Person(ident="rembrandt/43", label="Rembrandt")
top.classified_as = vocab.instances['artist occupation']
```

### Color

The URI for Color is: [http://vocab.getty.edu/aat/300080438](http://vocab.getty.edu/aat/300080438)

As [colors](/model/object/physical/#colors) can be measured precisely as well as being treated as a category, the classification sits on the Dimension. The dimension might end up not having a value and unit, only a second classification for what sort of color it is (in this case, brown), but the required terminology is to use aat:300080438 on the Dimension.

```crom
top = model.HumanMadeObject(ident="nightwatch/47", label="Night Watch by Rembrandt")
c = vocab.Color(label="brown")
c.value = 11754015.0
c.unit = vocab.instances['rgb_colorspace']
top.dimension = c
```

## Activity Types

There are several classifications for Activity that are important to use, as they they define core cultural heritage organization practices.

### Exhibition Activity

The URI for Exhibition is: [http://vocab.getty.edu/aat/300054766](http://vocab.getty.edu/aat/300054766)

Exhibitions are [documented in their own section](/model/exhibition/), but do not have a class of their own in the ontology. As such we need to give them a required classification so they can be recognized.

```crom
top = vocab.Exhibition(ident="exha/40", label="Manet and Modern Beauty (Getty)")
```

### Provenance Activity

The URI for Provenance entries is: [http://vocab.getty.edu/aat/300055863](http://vocab.getty.edu/aat/300055863)

Provenance activities also have their own [section](/model/provenance/) of the documentation, and do not have a class in the ontology. This classification is for the top level activity which groups together the other parts.

```crom
top = vocab.ProvenanceEntry(ident="manet_proust/40", label="Purchase of Spring by Proust")
```

### Publication Activity

The URI for Publication activities is: [http://vocab.getty.edu/aat/300054686](http://vocab.getty.edu/aat/300054686)

Works, especially texts such as books, are [published](/model/document/#creation-and-publication) in an activity. These activities are embedded in the record for the work, but are no less important to be able to distinguish.

```crom
top = vocab.LinguisticObject(ident="koot_nightwatch/40", label="Content of Koot's Night Watch")
pub = vocab.Publishing(label="MI's Publishing")
pub.carried_out_by = model.Group(ident="meulenhoff", label="Meulenhoff International")
top.used_for = pub
```

### Professional Activity

The URI for Professional Activities is: [http://vocab.getty.edu/aat/300393177](http://vocab.getty.edu/aat/300393177)

```crom
top = model.Person(ident="rembrandt/44", label="Rembrandt")
top.carried_out = vocab.Active()
```

### Promise Activity

The URI for Promises is: [http://vocab.getty.edu/aat/300435599](http://vocab.getty.edu/aat/300435599)

Albeit a small part of the detailed provenance, there isn't a class for [promises](/model/provenance/promises/) in the ontology, and thus we have to require terminology to fill the role. 

```crom
top = vocab.ProvenanceEntry(ident="coffin_promise/1", label="Promised Gift of Coffin")
promise = vocab.Promise(label="Promise of Gift")
top.part = promise
```

## Object Flags

### Collection Item

### Artwork

