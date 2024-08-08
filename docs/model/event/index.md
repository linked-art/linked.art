---
title: "Temporal Context: Periods, Events and Activities"
---

[TOC]

## Introduction

Most of the events and activities and other temporal aspects that we care about are directly related to the objects, people, and other entities. These would include the activity that brings the entity into existence (productions, creations, births and formations), takes them out of existence (destructions, erasures, dissolutions) or otherwise significantly affects their appearance in the cultural record (when there were encountered, their publication, a person's professional activities). There are two broad classes of activity which have their own specific models -- the [provenance](../provenance/) or ownership history of the object, and [exhibitions](../exhibition/).

There are also periods of time, events and activities carried out by people which provide additional context to the objects, but are not directly tied to them. These sorts of temporal entity would include periods of time (the cretaceous period, the bronze age, the 17th century), events that occur but are not intentionally carried out by people (the eruption of Vesuvius, the fire of London, the COVID 19 pandemic), and activities carried out by people (the first Linked Art face to face meeting, the landing on the moon, Scott's journey to Antarctica). This part of the model concerns these latter types, as they are separate from the objects and works in the same way that people, places and concepts are.

## Types

There are three types of temporal entity, as described above:

* **Period**: A period of time, likely somewhat arbitrarily defined, such as an "age" or century.
* **Event**: An event which occurs and then is finished, and typically changes the state of the world in some way.
* **Activity**: An event that was intentionally or willfully carried out by humans, singularly or in a group.

These types or classes are recorded in `type` in the model.

__Example:__ 

The 19th Century is a period that spans from 1800 through the end of 1899.

```crom
top = model.Period(ident="19c/1", label="19th Century")
top.identified_by = vocab.PrimaryName(content="19th Century")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1800-01-01T00:00:00Z"
ts.end_of_the_end = "1899-12-31T23:59:59Z"
top.timespan = ts
```

## Common Features

All of the common features of entities are available for events, including those defined specifically for events or activities such as being caused by another event described below in more detail, being carried out by a person or group, and so forth.


## Causes

Events and Activities can be caused by a preceding event or activity, for example the destruction of Pompeii was caused by the eruption of Vesuvius. The eruption of Vesuvius would then be an Event, referenced from the Destruction event for the (physical) city of Pompeii using the `caused_by` property. The eruption is also depicted in many paintings, and is the subject of many books. As such, it must have its own record, so that the objects, works and events can refer to the same entity.

__Example:__

Vesuvius erupts on August 24th, 79 CE.

```crom
top = model.Event(ident="vesuvius/1", label="Eruption of Vesuvius")
top.identified_by = vocab.PrimaryName(content="Eruption of Vesuvius")
top.took_place_at = model.Place(ident="vesuvius_it", label="Mount Vesuvius")
ts = model.TimeSpan()
ts.begin_of_the_begin = "0079-08-24T12:00:00Z"
ts.end_of_the_end = "0079-08-26T23:59:59Z"
top.timespan = ts
``` 

And is the cause of the destruction of the city of Pompeii.

```crom
top = model.HumanMadeObject(ident="pompeii_buildings/1", label="Buildings making up the city of Pompeii")
top.identified_by = vocab.PrimaryName(content="City of Pompeii")
dest = model.Destruction()
dest.caused_by = model.Event(ident="vesuvius")
top.destroyed_by = dest
```

## During vs Part Of

There are two relationships that describe how events are related to each other in terms of partitioning or inclusion, `part_of` and `during`. Each has a particular usage that should be adhered to carefully, otherwise searches and user interfaces will become very confusing and convoluted. 

Firstly, if one event is a strict part of another, and if you listed all of the parts, then the entire whole would be completed described, then the correct property to use is `part_of`.  For example, the Bronze Age consists of the Early Bronze Age, the Middle Bronze Age and the Late Bronze Age. Each of those might be further subdivided into a hierarchy of periods.

Conversely, if we know that an artifact was created during the bronze age, we would not list that along side its parts. The relationship is one of inclusion, rather than strict partitioning, and often either a stand-in for an unknown and more explicit timespan, or a method to categorize or group the activities or events that occur during the broader context.  For example the Production activity for the artifact occured `during` the Bronze Age period, but is not one of the constituent parts like those listed above.

__Example:__

The Early Roman Empire period, from 31 BCE through 193 CE, is part of the Roman Empire period.

```crom
top = model.Period(ident="early_roman/1", label="Early Roman Empire (31 BCE - 193 CE)")
top.identified_by = vocab.PrimaryName(content="Early Roman Empire")
top.part_of = model.Period(ident="roman", label="Roman Empire")
```

And Vesuvius erupted during this period.

```crom
top = model.Event(ident="vesuvius/2", label="Eruption of Vesuvius")
top.identified_by = vocab.PrimaryName(content="Eruption of Vesuvius")
top.during = model.Period(ident="early_roman", label="Early Roman Empire")
```

## Relative Times

`before`

`after`

