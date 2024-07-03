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

### Primary Name

The main or primary name of the entity. Every record must have a name with the primary name classification so that user interfaces know which name to use. There may be multiple primary names for a single record, but each must have a unique language, or no language. See the [name documentation](/model/base/#names).

Example:

```crom
top = model.HumanMadeObject(ident="nightwatch/41", label="Night Watch by Rembrandt")
ttl = vocab.PrimaryName(content="The Night Watch")
ttl.language = vocab.instances['english']
top.identified_by = ttl
```

### Display Name

A name to use when displaying the node which has the associated name. For Statements, this is typically used by interfaces as the label for the statement. For TimeSpans or other structured data, it is used in place of the structured data.

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

A name to use when sorting the entity along with other entities in a list. This classification can be used on the same name as the primary name, or on a different form of the entity's name. Different languages can have different sort names, however each language must not have more than one.

```crom
top = model.Person(ident="rembrandt/41", label="Rembrandt")
top.identified_by = vocab.PrimaryName(content="Rembrandt van Rijn")
top.identified_by = vocab.SortName(content="van Rijn, Rembrandt Harmenszoon")
```

### Sort Value

An identifier to use for sorting the entity along with other entities in a list, instead of a linguistic form as described above. There must not be more than one sort value per entity. User interfaces should not render the sort value to the end user.

```crom
top = model.Person(ident="rembrandt/42", label="Rembrandt")
top.identified_by = vocab.SortValue(content="r0000011")
```

## Classification Types

### Statement

### Type of Work

### Style

### Color

### Shape

### Occupation

### Nationality


## Activity Types

### Exhibition Activity

### Provenance Activity

### Professional Activity

### Publication Activity

### Promise Activity


## Object Flags

### Collection Item

### Artwork

