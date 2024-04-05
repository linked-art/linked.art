---
title: Conservation Activity
up_href: "/model/"
up_label: "Model Overview"
---

[TOC]

## Introduction

This section accommodates information about activities typically undertaken as part of the care and conservation of objects. In particular, there are condition assessments, conservation activities, and conservation projects which encapsulate the previous two.
Condition assessments are when a curator or conservator assesses the state of an object, and the extent to which conservation intervention is needed. Conservation activities are physical modifications of the object to improve its condition.

Other sections of the Linked.Art model also relate to conservation:

* [Statements](/model/base/#statements-about-an-entity) can be about the object's state or conservation related activities
* Sampling as an activity is described under [Production by removal](/model/object/production/#production-by-removal).
* Hazardous material can be under [Materials](/model/object/physical/#materials) by adding a classification to the Material itself.


## Condition Assessment

Condition Assessment describes an activity during which an object is examined and its preservation condition or types of damage are identified. The condition type is assigned as classification to the object. 

__Example:__

The Rijksmuseum checked the condition of The Night Watch, at the beginning of the project "Operation Night Watch"

```crom
top = vocab.Painting(ident="nightwatch/25", label="The Night Watch")
aa = model.AttributeAssignment(label="Condition Assessment of Night Watch")
top.attributed_by = aa
ts = model.TimeSpan()
ts.begin_of_the_begin = "2019-05-01T00:00:00Z"
ts.end_of_the_end = "2019-09-30T23:59:59Z"
aa.timespan = ts
actor = model.Group(ident="rijksmuseum", label="Rijksmuseum")
aa.carried_out_by = actor
aa.identified_by = model.Name(content="Thorough Condition Assessment")
aa.assigned_property = "classified_as"
aa.referred_to_by = vocab.Description(content = "Very fine cracks throughout the painted surface")
aa.assigned = model.Type(ident="http://vocab.getty.edu/aat/300387447", label="Microcracks")
aa.part_of = model.Activity(ident="operation_nightwatch", label="Operation Night Watch")
```

## Conservation Activities

Conservation Activities refers to the activities undertaken on an object before exhibition or with the objective to prevent the object from deteriorating. 

__Example:__

Minor conservation improvements were made to The Night Watch.

```crom
top = vocab.Painting(ident="nightwatch/26", label="The Night Watch")
mod = model.Modification(label="Conservation of Night Watch")
top.modified_by = mod
ts = model.TimeSpan()
ts.begin_of_the_begin = "2020-01-01T00:00:00Z"
ts.end_of_the_end = "2021-12-31T23:59:59Z"
mod.timespan = ts
mod.carried_out_by = model.Group(ident="rijksmuseum", label="Rijksmuseum")
mod.referred_to_by = vocab.Description(content="Minor conservation work in response to earlier survey")
mod.technique = model.Type(ident="http://vocab.getty.edu/aat/300053027", label="Cleaning")
mod.part_of = model.Activity(ident="operation_nightwatch", label="Operation Night Watch")
```


## Conservation Project

Conservation Projects are wrapper activities which represent the context of more granular events, and represent the overall event that is tracked in the chain, rather than the specific legal and physical changes that affect one or more objects. For example, a condition check of a collection which involves checking multiple objects, or conservation activity which starts with a condition check and continues with interventive conservation work. 

Conservation Projects have all of the regular properties and relationships, as documented in the [baseline patterns](/model/base/). In particular, the relationships to actors, places and time reflect the overall event.  

__Example:__

Operation Night Watch is a conservation and research project about The Night Watch

```crom
top = vocab.Conserving(ident="operation_nightwatch/1", label="Conservation Project")
top.identified_by = vocab.PrimaryName(content="Operation Night Watch")
top.carried_out_by = model.Group(ident="rijksmuseum", label="Rijksmuseum")
top.carried_out_by = model.Group(ident="akzonobel", label="AkzoNobel")
ts = model.TimeSpan()
ts.begin_of_the_begin = "2019-01-01T00:00:00Z"
ts.end_of_the_end = "2023-12-31T23:59:59Z"
top.timespan = ts
top.referred_to_by = vocab.Description(content="Operation Night Watch is the biggest and most wide-ranging ever study of Rembrandt’s most famous painting.")
```
