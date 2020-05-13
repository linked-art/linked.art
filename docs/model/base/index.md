---
title: Baseline Patterns
up_href: "/model/"
up_label: "Model Overview"
---

[TOC]

It is useful to have some common baseline patterns to follow when using a very open ontology, like CIDOC-CRM.  From working with datasets from across many different museums, the following patterns have been agreed on as useful ways to think about our cultural data.

These patterns are presented below with examples of how they are used in practice, but these are not intended to be exhaustive.  The documentation for the different resource types will include more information about how they are used in different circumstances.

## Core Properties

There are a few core properties that every resource should have for it to be a useful part of the world of Linked Open Data:

* `@context` is a reference to the context mapping which determines how to interpret the JSON as Linked Open Data. It is not a property of the entity being described, but of the document. It must be present.
* `id` captures the URI that identifies the object.  Every resource must have exactly one id, and it must be an HTTP URI.
* `type` captures the class of the object, or `rdf:type` in RDF. Every resource must have exactly one class. This allows software to align the data model with an internal, object oriented class based implementation.
* `_label` captures a human readable label as a string, intended for developers or other people reading the data to understand what they are looking at.  Every resource should have exactly one label, and must not have more than one. It is just a string, and does not have a language associated with it -- if multiple languages are available for the content, then implementations can choose which is most likely to be valuable for a developer looking at the data.

__Example:__

The simplest possible object has a URI, a class and a label.

```crom
top = HumanMadeObject(label="Example Object")
```

## Types and Classifications

CIDOC-CRM is a framework that must be extended via additional vocabularies and ontologies to be useful.  The provided mechanism for doing this is the `classified_as` property, which refers to a term from a controlled vocabulary. This is in contrast to the `type` property described above, which is used for CIDOC-CRM defined classes, and a few extensions as needed. The `classified_as` property is thus a way to be more specific about the sort of entity, while maintaining the core information as the class using `type`. Controlled vocabulary entries should not be used with `type`, nor classes used with `classified_as`.

While any external vocabulary of terms can be used, the [Getty's Art and Architecture Thesaurus](http://vocab.getty.edu/aat/) is used whenever possible for consistency and that it is already widespread in the museum domain. The set of terms that have been identified as useful are listed in the [community best-practices](/community/best-practices/vocabularies/) for recommendations, and within the documentation of the model when a particular choice is essential for interoperability.

Use cases for this pattern are in almost every example, but include:

 * The object being an art object
 * The type of an art object being a painting
 * The type of a description being a materials statement
 * The type of an identifier being an accession number
 * The type of an organization being a museum
 * The type of a place being a gallery

__Example:__

The type of the object (an instance of the class `HumanMadeObject`) is a painting _(aat:300033618)_, and an artwork _(aat:300133025)_:

```crom
top = model.HumanMadeObject(label="Simple Example Painting")
top.classified_as = Type(ident="http://vocab.getty.edu/aat/300033618", label="Painting")
top.classified_as = Type(ident="http://vocab.getty.edu/aat/300133025", label="Work of Art")
```

### Types of Types

A common pattern is to not only classify main entities, but also to classify the types themselves in order to know what sort of type it is, without recognizing all of them individually.
This is important when the set of first degree types is not easily enumerable, such as classifications for the type of object or work. If the set of vocabulary terms that can normally be used without further extension can be established, then this pattern is not used. This is also not needed when the relationship from the entity to the first degree type clarifies this, such as the `motivation` or `about` properties. 

Use cases for this pattern include:

* The classification is the type of object or work of the physical thing (e.g. Painting)
* The classification is the type of text of the statement (e.g. Dimensions Statement)
* The classification is the nationality of the person (e.g. Swiss)


__Example:__

The physical thing is classified as being a Painting, and the concept "Painting" is for classifying the type of object (as opposed to any other sort of classification).

```crom
top = Painting(label="Example Painting", art=1)
```


## Names and Identifiers for a Resource

### Names

As the `_label` property is intended as internal documentation for the data, it is strongly recommended that every resource that should be rendered to an end user also have at least one specific name. The name could be for an object, a person, a group, an event or anything else.  This pattern uses the `identified_by` property, with a `Name` resource.  The value of the name is given in the `content` property of the `Name`. 

It is somewhat unintuitive to think of a name as identifying the resource it is associated with, as names are typically not unique.  However, as the name itself __is__ uniquely identified rather than just an anonymous string, they are no longer a shared label and instead the particular instance of a name is uniquely associated with the resource. With this formulation, the name instance does uniquely identify the resource.  

If there is more than one name given, then there should be one that is `classified_as` the primary name for use. This is done by adding the Primary Name _(aat:300404670)_ term to it. There should be exactly one primary title given per language.

Names are also part of human communication, and can have the Linguistic features of the model associated with them, such as having a particular language, or having translations.

__Example:__

The primary name for the painting is "Pasture and Sheep", which is in English.

```crom
top = Painting(art=1)
top._label = "Painting: Pasture and Sheep"
ttl = PrimaryName()
ttl.content = "Pasture and Sheep"
ttl.language = instances['english']
top.identified_by = ttl
```

### Identifiers

Many resources of interest are also given external identifiers, such as accession numbers for objects, ORCIDs for people or groups, lot numbers for auctions, and so forth.  Identifiers are represented in a very similar way to names, but instead use the `Identifier` class. Identifiers will normally have a classification determining which sort of identifier it is, to distinguish between internal repository system assigned numbers from museum assigned accession numbers, for example.

As `Identifier`s and `Name`s use the same `identified_by` property, the JSON will frequently have mixed classes in the array. Unlike `Name`s, `Identifier`s are not part of human language and thus cannot have translations or a language associated with them.

__Example:__

The accession number identifier for the painting is "P1998-27".

```crom
top = Painting(art=1)
top._label = "Pasture and Sheep"
id1 = AccessionNumber()
id1.content = "P1998-27"
top.identified_by = id1
ttl = PrimaryName()
ttl.content = "Pasture and Sheep"
top.identified_by = ttl
```

## Statements about a Resource

In many cases, current data does not support the level of specificity that the full ontology allows, or the information is simply best expressed in human-readable form.  For example, instead of a completely modeled set of parts with materials, many museum collection management systems allow only a single human-readable string for the "medium" or "materials statement".  The same is true in many other situations, including rights or allowable usage statements, dimensions, edition statements and so forth.  Any time that there is a description of the resource, with or without qualification as to the type of description, then this pattern can be used to record the descriptive text.

The pattern makes use of the `LinguisticObject` class that is used to identify a particular piece of textual content.  These Linguistic Objects are then refered to by any other resource.  They maintain the statement's text in the `content` property, and the language of the statement (if known) in the `language` property.

Use cases for this pattern include:

* General description of the resource
* Materials statement for an object
* Attribution statement for an image
* Biography for a person
* Dimensions statement for a part of an object

__Example:__

Having only a textual description of the materials in English, the content `"Oil on Canvas"` is recorded as referring to the painting as a "materials" _(aat:300435429)_ statement:

```crom
top = Painting(art=1)
top._label = "Painting on Canvas"
lo = MaterialStatement(top.id + "/statement/1")
lo.content = "Oil on Canvas"
lo.language = instances['english']
top.referred_to_by = lo
```

## Parts

Describing the hierarchy of parts of resources is a core pattern for having increasingly granular or specific descriptions. The advantage of partitioning is that more specific information can be provided about each part, as a thing separate from the whole. This pattern covers the spectrum of different classes used in the model, from physical and textual, to temporal or geographic.  Parts are given using the properties `part` (from the whole to the part) or `part_of` (from the part to the whole).

Use cases for this pattern include:

 * Delineating physical components or aspects of an object, such as the frame being part of the painting, or the recto side being part of the page.
 * Separating a long period or event into smaller sections, such as battles within a war, or the activities of different people during the production of an object.
 * Separating geographical locations into smaller subdivisions, such as that the neighborhood is part of the city, which is in turn part of the state.
 * Partitioning a text into segments, such as that the paragraph is part of a chapter, which is in turn part of the entire book


__Example:__

The canvas support is part of the overall watercolor painting.

```crom
top = Painting(art=1)
top._label = "Example Painting"
top.made_of = instances['watercolor']
part = SupportPart(top.id + "/part/1")
part._label = "Canvas Support"
part.made_of = instances['canvas']
top.part = part
```

### Membership

Membership in a set is treated slightly differently. A set can have no members and still be a set, whereas if you destroy the last part of an object, it no longer exists. For example, a department of an organization (a Group) might not have any members due to the retirement of the last member, but there is a still an identifiable, ongoing group that would hopefully gain members when new hires are made.  Membership is given using the `member` or `member_of` property, instead of the corresponding `part` and `part_of`.

Use cases for the membership pattern include:

* A curator is a member of the paintings department of the museum.
* A painting is part of the collection of a the museum.
* An identifier is part of the set of identifiers that collectively make up the accession numbers assigned to paintings by the museum.

__Example:__

The curator is a member of the paintings department.

```crom
top = vocab.Department()
top._label = "Paintings Department"
who = Person()
who._label = "Curator"
top.member = who
```

## Events and Activities

Patterns are not only within a single entity, but also in the way that we manage relationships between entities.  While many systems link straight from one an object to its creator, for example, CIDOC-CRM and thus Linked Art instead uses an intermediate entity that represents the activity of the artist in creating the object. This enables us to associate time, place, actors, techniques, other objects and more with the creation activity, rather than needing many individual relationships.

The key participants in those different types of events are:

  * the [Object](../object/) being acted upon,
  * the [Actors](../actor/) (people or organizations) that perform the activity,
  * the [Locations](../place) at which the activity occurs,
  * and the Time at which it occurs.

The general pattern is to create a resource for the `Activity` or `Event`, and associate the participants with that resource. The relationships for time (`timespan`) and place (`took_place_at`) are relevant to `Event`s that happen without the direct cause being a human action, and the relationship for the actor (`carried_out_by`) is added to those for human activities.  The relationship to the `Object` is dependent on the type of `Event` or `Activity`, which are discussed in more detail in the specific sections.

There are both subclasses of `Activity`, such as `Acquisition`, `Production` and `AttributeAssignment`, and classifications associated with them to be more specific, either as a `technique` like glassblowing _(aat:300053932)_, or via `classified_as` for more general terms like gift giving _(aat:aat:300404212)_ to clarify the sort of `Acquisition`.

The pattern uses the terms and structure given in this completely artificial example:

```crom
top = Activity()
who = Actor()
who._label = "Who"
when = TimeSpan()
when._label = "When"
when.begin_of_the_begin = "earliest-start-datetime"
when.end_of_the_end = "latest-end-datetime"
where = Place()
where._label = "Where"
top.carried_out_by = who
top.took_place_at = where
top.timespan = when
```

### Time Span Details

The minimal timespan model is given above, with just the `begin_of_the_begin` and an `end_of_the_end` properties to record the beginning of the span, and the end of the span.  The end of the span is not included in the span, and thus if the `end_of_the_end` is `"1500-01-01T00:00:00Z"`, then the 1500 is not included, and the last mathematical moment of the last day of December 1499 is the very end. 

It is very useful to have a `Name` for the `TimeSpan` that gives a human readable version of the machine readable timestamps and durations. This uses the pattern given above for naming things, and might be displayed to user directly, whereas the other properties could be used for matching a time-based search.

There are other properties for `TimeSpan` instances that are useful when the exact span of time is not certain.

* `end_of_the_begin`: This property is another datetime that gives the latest possible datetime for the beginning of the span.
* `begin_of_the_end`: This property is yet another datetime that gives the earliest possible datetime for the end of the span. 
* `duration`: This property refers to a `Dimension`, that describes the amount of time that the activity or event took, within the span of time.  As the property defines the type of dimension, the `Dimension` instance does not need to be `classified_as` any particular `Type` ... it is always a duration.


__Example:__ 

An auction that occured during April 1763 over a period of three consecutive days.


```crom
top = vocab.AuctionEvent(label="Auction")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1763-04-01T00:00:00Z"
ts.end_of_the_begin = "1763-04-28T00:00:00Z"
ts.begin_of_the_end = "1763-04-04T00:00:00Z"
ts.end_of_the_end = "1763-05-01T00:00:00Z"
dim = model.Dimension(value=3)
dim.value = 3
dim.unit = vocab.instances['days']
ts.duration = dim
n = model.Name()
n.content = "Three days within April 1763"
ts.identified_by = n
top.timespan = ts 
```

