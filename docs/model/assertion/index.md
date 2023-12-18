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

The example below demonstrates associating a previous title with an object.

```crom
top = vocab.Painting(ident="auto int-per-segment",art=1)
top._label = "Current Painting Title"
aa = model.AttributeAssignment()
aa.assigned_property = "identified_by"
name = model.Name()
name.content = "Previous Painting Title"
aa.assigned = name
top.attributed_by = aa
who = model.Person()
who._label = "Painting Curator"
aa.carried_out_by = who
ts = model.TimeSpan()
ts.begin_of_the_begin = "1804-05-19"
ts.end_of_the_end = "1804-05-19"
aa.timespan = ts
```

### Assigned Value as Resource

In other situations the assigned value is the appropriate resource with which to associate the `AttributeAssignment`. In this case we flip the `AttributeAssignment` around and use `assigned_by` on the value of the assignment (the object of the relationship), and do not specify the subject of the relationship as it's the resource which refers to the value. For example, it is very useful to be able to assert which organization created and assigned an identifier to an object of a given type in order to disambiguate that organization's identifier from another organization's identifier of the same type, such as accession numbers.  Another use case is giving further information about a particular `Dimension` associated with the object, such as who measured it, when, with which instrument, and so on.

In this case, the subject of the relationship is the resource which refers to the value, the predicate is that relationship, and the object is the resource with the `assigned_by` property which refers to the AttributeAssignment.

```crom
top = vocab.Painting(ident="auto int-per-segment", label="Example Painting", art=1)
acc1 = vocab.AccessionNumber(value="1925.0034")
acc2 = vocab.AccessionNumber(value="B-1254.6")
aa1 = model.AttributeAssignment()
aa1.carried_out_by = vocab.MuseumOrg(label="First Owning Museum")
aa2 = model.AttributeAssignment()
aa2.carried_out_by = vocab.MuseumOrg(label="Another Owning Museum")
acc1.assigned_by = aa1
acc2.assigned_by = aa2
top.identified_by = aa1
top.identified_by = aa2
```

### "Style Of" Attribution

There is a common special case of wanting to assign not an individual (e.g. Rembrandt) or a group with specific identity (Workshop of Rembrandt) to the production of an object, but simply to say that it was produced as if it had been produced by some other actor.  This is traditionally recorded as being "in the style of" or "in the manner of" a known artist. It is not correct to say that Rembrandt carried out the production, but a search for objects attributed (loosely speaking) to Rembrandt should discover this object. The assessment of "style of" attribution is a judgement decision that might be changed later as new evidence of the actual creator comes to light.

The approach taken for this case is to use an `AttributeAssignment` that associates a Production activity that is `influenced_by` the artist and `classified_as` being in the "style of" (_aat:300404285_).  This prevent systems from mistakenly infering that the actor `carried_out` the production, but is consistent with the overall pattern.

This would also apply to cases where there is a "circle of" or "follower of" and similar attributions in which there is doubt that there was an actual coherent group, and thus there is reluctance to give that hypothetical group an identity.  Instead of using the "style of" AAT concept, it would use another [attribution qualifiers](http://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300404264).

```crom
top = vocab.Painting(ident="auto int-per-segment",art=1)
top._label = "Example Painting"
aa = model.AttributeAssignment()
aa.assigned_property = "produced_by"
who = model.Person()
who._label = "Well Known Artist"
prod = model.Production()
prod.influenced_by = who
prod.classified_as = vocab.instances['style of']
aa.assigned = prod
top.assigned_by = aa
by = model.Person()
by._label = "Painting Curator"
aa.carried_out_by = by
```

## Context Specific Assertions

The basic pattern for making an assertion within some context is to reuse the `AttributeAssignment` activity, and have it be part of some larger activity.  A good example of this is the assignment of a particular title to a work during an [Exhibition](/model/exhibition/#exhibition-specific-labels). This could equally be part of the larger cataloging activity of an organization, an art dealer taking inventory, or any number of other contexts.

There are two relationships to note with this pattern.  The first is that the broader activity has a `part` which is the `AttributeAssignment`.  This gives some basic temporal context for the assignment. There is also in many cases a set of objects or other resources that provide additional context. In the Exhibition case, the set of objects and their labels in the exhibit is `involved` in the provision of the `Name` of the individual object.


```crom
top = vocab.Exhibition(ident="auto int-per-segment")
top._label = "Example Exhibition"
agg = model.Set()
top.used_specific_object = agg
obj = vocab.Painting(art=1)
obj._label = "Real Painting Name"
agg.member = obj
aa = model.AttributeAssignment()
aa.assigned_property = "identified_by"
name = model.Name()
name.content = "Exhibition Specific Name"
aa.assigned = name
aa.assigned_to = obj
curator = model.Person()
curator._label = "A. Curator"
aa.carried_out_by = curator
aa.involved = agg
top.part = aa
```

## Inferred Data

Some assertions, or even entire resources, are computationally inferred from other data rather than being evidenced in primary source literature or history. It is useful to tag these resources as such, so that they can be treated appropriately when it comes to research making use of them: if the underlying data has errors, these errors will have been propogated to this resource.

The way that this can be signalled in the data is to add the "computer-generated" concept _aat:300202389_ to the resource in the `classified_as` field.  

```crom
top = model.Activity(ident="auto int-per-segment")
top._label = "Inferred Activity"
top.classified_as = vocab.instances['computer generated']
a = model.Actor()
a._label = "Performer of inferred activity"
top.carried_out_by = a
```
