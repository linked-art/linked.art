---
title: Previously-Held or Context-Specific Assertions
---

[TOC]

## Introduction

It is useful for research to have access to historical information, such as which artist was previously believed to be the creator of a work, or previous valuations of an object.  The majority of use cases, however, are to get the current information.  The assignment of attributes model allows for this additional information to be associated, without making every property a list of historical values.

This pattern is also used for context-specific assertions, such as when an object is given a label or description for the purposes of an exhibition or other event.  This exhibition label does not replace the owning museum's title, but is useful for historical comparison and research purposes.

The use of context specific assertions or other attribute assignments should be kept to a minimum if possible. The data structure is significantly more complex than other patterns, which reduces the likelihood of implementation and increases the difficult of search queries. This pattern should only be used if there is no other way to express the knowledge, and it is important to capture with all of the details.

## Assignment of Attributes

The `AttributeAssignment` class is an `Activity`, carried out by curators or researchers rather than by artists or collectors, that assigns information to resources in the model. This can be used to assign any property or relationship on any resource that can be the _subject_ of such a property.  The general Activity properties of `carried_out_by`, `timespan` and `took_place_at` are available for when and where the assignment happened, and who made it.  The `timespan` is the moment when the assignment took place, rather than the length of time that the assignment was held to be true by some audience.

This pattern is useful when you do not want to assert the relationship directly, such as for a name that was previously given to the object but is no longer actively used. Or an attribution of an artist that is possibly true, but might only be an informed guess.

The value of the assignment is given using `assigned`, and it can be any resource or value. The resource that the value is assigned to is given using the `attributed_by` property on that resource, and the relationship between them is given using `assigned_property`. Thus an `AttributeAssignment` can assign an `Actor` to a `Production` with the `carried_out_by` relationship, or a `Name` to an `Actor` with the `identified_by` relationship.  In terms of the relationship that the `AttributeAssignment` expresses, the resource with the `attributed_by` property is the subject of the relationship, the relationship itself is given in `assigned_property`, and the object of the relationship is given in `assigned`, thereby making up a regular 'triple' of subject, predicate, object.

__Example:__

Manet called his painting "Le Printemps", "Spring" in French.

```crom
top = vocab.Painting(ident="spring/21", label="Spring")
aa = model.AttributeAssignment()
aa.assigned_property = "identified_by"
name = model.Name()
name.content = "Le Printemps"
aa.assigned = name
top.attributed_by = aa
aa.carried_out_by = model.Person(ident="manet", label="Manet")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1881-01-01T00:00:00Z"
ts.end_of_the_end = "1881-12-31T23:59:59Z"
aa.timespan = ts
```

### Assigned Value as Resource

In other situations the assigned value is the appropriate resource with which to associate the `AttributeAssignment`. In this case we flip the `AttributeAssignment` around and use `assigned_by` on the value of the assignment (the object of the relationship), and do not specify the subject of the relationship as it's the resource which refers to the value. For example, it is very useful to be able to assert which organization created and assigned an identifier to an object of a given type in order to disambiguate that organization's identifier from another organization's identifier of the same type, such as accession numbers.  Another use case is giving further information about a particular `Dimension` associated with the object, such as who measured it, when, with which instrument, and so on.

In this case, the subject of the relationship is the resource which refers to the value, the predicate is that relationship, and the object is the resource with the `assigned_by` property which refers to the AttributeAssignment.

__Example:__

The Kehinde Wiley painting "Portrait of Lynette Yiadom-Boakye, Jacob Morland of Capplethwaite" is jointly owned by the Yale University Art Gallery and the Yale Center for British Art. Both organizations have assigned their own accession numbers to the painting, and both are correct simultaneously.

```crom
top = vocab.Painting(ident="yiadom-boakye/1", label="Portrait of Lynette Yiadom-Boakye")
acc1 = vocab.AccessionNumber(value="2021.25.1")
acc2 = vocab.AccessionNumber(value="B2021.5")
aa1 = model.AttributeAssignment()
aa1.carried_out_by = vocab.MuseumOrg(ident="yuag", label="Yale University Art Gallery")
aa2 = model.AttributeAssignment()
aa2.carried_out_by = vocab.MuseumOrg(ident="ycba", label="Yale Center for British Art")
acc1.assigned_by = aa1
acc2.assigned_by = aa2
top.identified_by = acc1
top.identified_by = acc2
```

## Uncertain or Former Assignments

Similar to the approach taken in the first example above, it is possible to use `attributed_by` on a `Production` node to make either uncertain or previously held to be true claims about it. The assignment then creates another `Production` to encapsulate the information that isn't certain, or was formerly held to be correct, including the artist(s) but also potentially other links such as the place of production, the date, or other influences.

__Example:__ 

The watercolor painting "Forum Romanum" was possibly produced by Salomon Corrodi

```crom
top = vocab.Painting(ident="forum/1", label="Forum Romanum")
top.identified_by = vocab.PrimaryName(content="Forum Romanum")
prod = model.Production()
top.produced_by = prod
aa = model.AttributeAssignment()
aa.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300404272", label="Possibly By")
part = model.Production()
aa.assigned = part
part.carried_out_by = model.Person(ident="corrodi", label="Salomon Corrodi")
aa.assigned_property = "part"
prod.attributed_by = aa
```

## Unknown Relationships

Another use of `AttributeAssignment` is to capture relationships between entities when the nature of that relationship is unknown. This will often appear in human-oriented user interfaces with a label like "Related Place" or "Related Subject". The use of AttributeAssignment in this way should be as a last resort for when there isn't any way to be more specific that just "there is a relationship". A scenario in which this might be useful and justified is to explicitly connect "related" objects in a collection, where the related-ness is via some computed similarity measure. Equally, the underlying data format might not be explicit as to the relationship between the entities, and the attribute assignment pattern is as close as can be expressed.

__Example:__

The Night Watch is related to another object in the Rijksmuseum collection "Nachtwacht", but the relationship is not captured specifically.

```crom
top = vocab.Painting(ident="nightwatch/17", label="The Night Watch")
top.identified_by = vocab.PrimaryName(content="The Night Watch")
aa = model.AttributeAssignment()
top.attributed_by = aa
aa.assigned = model.HumanMadeObject(ident="rppob-28-106", label="Nachtwacht")
```
