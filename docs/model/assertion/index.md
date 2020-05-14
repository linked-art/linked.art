---
title: Previously-Held or Context-Specific Assertions
---

[TOC]

## Introduction

It is useful for research to have access to historical information, such as which artist was previously believed to be the creator of a work, or previous valuations of an object.  The majority of use cases, however, are to get the current information.  The assignment of attributes model allows for this additional information to be associated, without making every property a list of historical values.

This pattern is also used for context-specific assertions, such as when an object is given a label or description for the purposes of an exhibition or other event.  This exhibition label does not replace the owning museum's title, but is useful for historical comparison and research purposes.

## Assignment of Attributes

The `AttributeAssignment` class is an `Activity`, carried out by curators or researchers rather than by artists, that assigns information to resources in the model. This can be used to assign any property or relationship on any resource that can be the subject of such a property.  The general Activity properties of `carried_out_by`, `timespan` and `took_place_at` are also available for when and where the assignment happened, and who made it.  The `timespan` is the moment when the assignment took place, rather than the length of time that the assignment was held to be true by some audience.

The value of the assignment is given using `assigned`, and it can be any resource or value. The resource that the value is assigned to is given using the `assigned_to` property, and the relationship between them is given using `assigned_property`. Thus an `AttributeAssignment` can assign an `Actor` to a `Production` with the `carried_out_by` relationship, or a `Name` to an `Actor` with the `identified_by` relationship.  

The example below demonstrates associating a previous title with an object.

```crom
obj = Painting(art=1)
obj._label = "Current Painting Title"
top = AttributeAssignment()
top.assigned_property = "identified_by"
name = Name()
name.content = "Previous Painting Title"
top.assigned = name
top.assigned_to = obj
who = Person()
who._label = "Painting Curator"
top.carried_out_by = who
ts = TimeSpan()
ts.begin_of_the_begin = "1804-05-19"
ts.end_of_the_end = "1804-05-19"
top.timespan = ts
```

### "Style Of" Attribution

There is a common special case of wanting to assign not an individual (e.g. Rembrandt) or a group with specific identity (Workshop of Rembrandt) to the production of an object, but simply to say that it was produced as if it had been produced by some other actor.  This is traditionally recorded as being "in the style of" a known artist. It is not correct to say that Rembrandt carried out the production, but a search for objects attributed (loosely speaking) to Rembrandt should discover this object.  The assessment of "style of" attribution is a judgement decision that might be changed later as new evidence of the actual creator comes to light.

The approach taken for this case is to use an `AttributeAssignment` that associates a Production activity that is `influenced_by` the artist and `classified_as` being in the "style of" (_aat:300404285_).  This prevent systems from mistakenly infering that the actor `carried_out` the production, but is consistent with the overall pattern.

This would also apply to cases where there is a "workshop of", "studio of", "circle of" and similar attributions in which there is doubt that there really was such a group, and thus there is reluctance to give that hypothetical group an identity.  Instead of using the "style of" aat concept, it would use "workshop of" (_aat:300404274_), or other [attribution qualifiers](http://www.getty.edu/vow/AATHierarchy?find=&logic=AND&note=&page=1&subjectid=300404264) from AAT.

```crom
top = AttributeAssignment()
top.assigned_property = "produced_by"
obj = Painting(art=1)
obj._label = "Example Painting"
who = Person()
who._label = "Well Known Artist"
prod = Production()
prod.influenced_by = who
prod.classified_as = instances['style of']
top.assigned = prod
top.assigned_to = obj
by = Person()
by._label = "Painting Curator"
top.carried_out_by = by
```

## Context Specific Assertions

The basic pattern for making an assertion within some context is to reuse the `AttributeAssignment` activity, and have it be part of some larger activity.  A good example of this is the assignment of a particular title to a work during an [Exhibition](/model/exhibition/#exhibition-specific-labels). This could equally be part of the larger cataloging activity of an organization, an art dealer taking inventory, or similar.

There are two relationships to note with this pattern.  The first is that the broader activity has a `part` which is the `AttributeAssignment`.  This gives some basic temporal context for the assignment. There is also in many cases a set of objects or other resources that provide additional context. In the Exhibition case, the set of objects and their labels in the exhibit is `involved` in the provision of the `Name` of the individual object.



```crom
top = Exhibition()
top._label = "Example Exhibition"
agg = model.Set()
top.used_specific_object = agg
obj = Painting(art=1)
obj._label = "Real Painting Name"
agg.member = obj
aa = AttributeAssignment()
aa.assigned_property = "identified_by"
name = Name()
name.content = "Exhibition Specific Name"
aa.assigned = name
aa.assigned_to = obj
curator = Person()
curator._label = "A. Curator"
aa.carried_out_by = curator
aa.involved = agg
top.part = aa
```

## Inferred Data

Some assertions, or even entire resources, are computationally inferred from other data rather than being evidenced in primary source literature or history. It is useful to tag these resources as such, so that they can be treated appropriately when it comes to research making use of them: if the underlying data has errors, these errors will have been propogated to this resource.

The way that this can be signalled in the data is to add the "computer-generated" concept _aat:300202389_ to the resource in the `classified_as` field.  

```crom
top = Activity()
top._label = "Inferred Activity"
top.classified_as = instances['computer generated']
a = Actor()
a._label = "Performer of inferred activity"
top.carried_out_by = a
```
