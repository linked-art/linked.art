---
title: Basic Patterns
up_href: "/model/"
up_label: "Model Overview"
---

[TOC]
 
It is useful to have some common, basic patterns to follow when using a very open model and ontology. The following patterns have been agreed on as useful ways to think about our cultural data, through working with objects, entities and collections from across many different museums and organizations. They are foundational to all of Linked Art, and used extensively both to describe the core entities of interest (objects, works, people, places and so on) as well as within the descriptions (for example to give a label to a description, or a classification to a span of time).

These patterns are presented below with examples of how they are used in practice, but these are not intended to be exhaustive.  The documentation for the different entity types will include more information about how they are used in different circumstances.

## Core Properties

There are a few core properties that every resource must have for it to be a useful part of the world of Linked Art and Linked Open Usable Data ([LOUD](../../loud/)):

* `@context` is a reference to the context mapping which determines how to interpret the JSON as LOUD. It is not a property of the entity being described, but of the document. It must be present.
* `id` captures the URI that identifies the entity.  Every core entity must have exactly one URI.
* `type` captures the class of the entity, or `rdf:type` in RDF. Every entity must have exactly one class. This allows software to align the data model with an internal, object oriented class based implementation. Classes determine which properties or relationships may be associated with the entity.
* `_label` captures a human readable label as a string, intended for developers or other people reading the data to understand what they are looking at.  Every entity should have exactly one label, and must not have more than one. It is just a string, and does not have a language associated with it -- if multiple languages are available for the content, then implementations can choose which is most likely to be valuable for a developer looking at the data.

The classes used for the core entities we describe are summarized as below, with links to the full documentation about them:

>
| Class             | Documentation                | Description   |
|-------------------|------------------------------|---------------|
| `HumanMadeObject` | [Objects](../object/)        | Physical things you can touch, e.g. a painting |
| `DigitalObject`   | [Digital](../digital/)       | Digital things that exist only in computers, e.g. a web page |
| `Person`          | [Agents](../actor/)          | A human person, e.g. Rembrandt |
| `Group`           | [Agents](../actor/)          | A group of people, capable of collective action, e.g. a museum department |
| `Place`           | [Places](../place/)          | A place, typically somewhere on earth that could have coordinates, e.g. Paris |
| `VisualItem`      | [Visual Work](../object/aboutness/) | Conceptual image/visual content shown by a physical or digital object, e.g. the image we know as "The Mona Lisa", as opposed to the physical painting |
| `LinguisticObject`| [Documents](../document/)    | Textual content carried by a physical or digital object, e.g. the text of The Lord of the Rings |
| `PropositionalObject`| [Exhibitions](../exhibition/) | An entirely abstract work that is neither linguistic nor visual, e.g. the notion of an exhibition or piece of performance art |
| `Type`            | [Concepts](../concept/)      | A category, concept, or similar, e.g. centimeters or sculpting |
| `Set`             | [Collection](../collection/) | A set or collection of some number of other entities, e.g. a museum collection |
| `Activity`        | [Provenance](../provenance/), [Exhibitions](../exhibition/) | An activity carried out by people or groups, e.g. an exhibition or the transfer of ownership of an object between parties |


__Example:__

The simplest possible object description of "Spring" has a URI, a class and a label.

```crom
top = model.HumanMadeObject(ident="spring/1", label="Jeanne (Spring) by Manet")
```

## Types and Classifications

CIDOC-CRM, our underlying ontology, is a framework that must be extended via additional vocabularies and ontologies to be useful.  The provided mechanism for doing this is the `classified_as` property, which refers to a term from a controlled vocabulary. This is in contrast to the `type` property described above, which is used for a limited number of core, ontological classes. The `classified_as` property is thus a way to be more specific about the sort of entity, while maintaining the core information as the class using `type`. Controlled vocabulary entries should not be used with `type`, nor classes used with `classified_as`. 

While any external vocabulary of terms can be used, the [Getty's Art and Architecture Thesaurus](http://vocab.getty.edu/aat/) is used whenever possible for consistency and that it is already widespread in the museum domain. The set of terms that have been identified as useful are listed in the [community best-practices](/community/best-practices/vocabularies/) for recommendations, and within the documentation of the model when a particular choice is essential for interoperability.

Use cases for this pattern are in almost every example, but include:

 * The object being an art object
 * The type of an art object being a painting
 * The type of a description being a materials statement
 * The type of an identifier being an accession number
 * The type of an organization being a museum
 * The type of a place being a gallery

__Example:__

The classification of "Spring" (an instance of the class `HumanMadeObject`) is a painting _(aat:300033618)_, and an artwork _(aat:300133025)_:

```crom
top = model.HumanMadeObject(ident="spring/2", label="Jeanne (Spring) by Manet", art=1)
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300033618",label="Painting")
```

The classification of "Paris" (an instance of the class `Place`) is a city _(aat:00008389)_: 

```crom
top = vocab.City(ident="paris/1", label="Paris")
```


### Types of Types

A common pattern is to not only classify main entities, but also to classify the types themselves in order to know what sort of type it is, without recognizing all of them individually.
This is important when the set of first degree types is not easily enumerable, such as classifications for the type of object or work. If the set of vocabulary terms that can normally be used without further extension can be established, then this pattern is not used. This is also not needed when the relationship from the entity to the first degree type clarifies this, such as the `motivation` or `about` properties. 

Use cases for this pattern include:

* The classification is the type of object or work of the physical thing (e.g. Painting)
* The classification is the type of text of the statement (e.g. Dimensions Statement)
* The classification is the nationality of the person (e.g. Swiss)


__Example:__

The object is classified as being a Painting, and the concept "Painting" is for classifying the type of object (as opposed to any other sort of classification).

```crom
top = vocab.Painting(ident="spring/3", label="Jeanne (Spring) by Manet", art=1)
```

Rembrandt (a person) has a nationality of Dutch:

```crom
top = model.Person(ident="rembrandt/1", label="Rembrandt")
top.classified_as = vocab.instances['dutch']
```


## Names and Identifiers for a Resource

### Names

As the `_label` property is intended as internal documentation for the data, it is strongly recommended that every entity that should be rendered to an end user also have at least one specific name. The name could be for an object, a person, a group, an event or anything else.  This pattern uses the `identified_by` property, with a `Name` construct.  The value of the name is given in the `content` property of the `Name`. 

It is somewhat unintuitive to think of a name as identifying the resource it is associated with, as names are typically not unique.  However, as the name has its own class (Name) and __could__ have an `id`, it is not just an anonymous string and thus no longer a shared label. Instead each name is the particular instance of a name which is uniquely associated with its entity. With this formulation, the name instance __does__ uniquely identify the entity.  

If there is more than one name given, then there should be one that is `classified_as` the primary name for use. This is done by adding the Primary Name _(aat:300404670)_ term to it. There should be exactly one primary name given per language. Names are also part of human communication, and can have the Linguistic features of the model associated with them, such as having a particular language.


__Example:__

The primary name for "The Night Watch" is "The Night Watch" in English, and "De Nachtwacht" in Dutch:

```crom
top = model.HumanMadeObject(ident="nightwatch/1", label="Night Watch by Rembrandt")
ttl = vocab.PrimaryName(content="The Night Watch")
ttl.language = vocab.instances['english']
top.identified_by = ttl
ttl2 = vocab.PrimaryName(content="De Nachtwacht")
ttl2.language = vocab.instances['dutch']
top.identified_by = ttl2
```

### Identifiers

Many entities are also given external identifiers, such as accession numbers for objects, ORCIDs for people or groups, lot numbers for auctions, and so forth.  Identifiers are represented in a very similar way to names, but instead use the `Identifier` class. Identifiers will normally have a classification determining which sort of identifier it is, to distinguish between internal repository system assigned numbers from museum assigned accession numbers, for example.

As `Identifier`s and `Name`s use the same `identified_by` property, the JSON will frequently have mixed classes in the array. Unlike `Name`s, `Identifier`s are not part of human language and thus cannot have a language associated with them.

__Example:__

The accession number identifier for "The Night Watch" is "SK-C-5":

```crom
top = model.HumanMadeObject(ident="nightwatch/2", label="Night Watch by Rembrandt")
top.identified_by = vocab.AccessionNumber(content="SK-C-5")
top.identified_by = vocab.PrimaryName(content="The Night Watch")
```

### Equivalent Data URIs

Identifiers for the same entity within the web of linked data are treated differently from string identifiers such as accession numbers or ISBNs. In order to allow systems to follow the link and potentially process the information that they discover there, we use a new property `equivalent` to link out to other organizations' data about the same entity.  For example, Rembrandt has a description in the Getty's [ULAN](http://vocab.getty.edu/ulan/500011051) vocabulary, in [Wikidata](http://www.wikidata.org/entity/Q5598), in the Library of Congress [Name Authority File](http://id.loc.gov/authorities/names/n79142935), and in OCLC's [Virtual International Authority File](http://viaf.org/viaf/64013650), amongst many others. The URI given must identify the entity itself, rather than about page the entity. For example, in ULAN there is also the website version [http://vocab.getty.edu/page/ulan/500011051](http://vocab.getty.edu/page/ulan/500011051) which must not be used with equivalent.

__Example:__

The Night Watch has an external URI that also identifies the same physical object in [wikidata](https://www.wikidata.org/wiki/Q219831):

```crom
top = model.HumanMadeObject(ident="nightwatch/3", label="Night Watch by Rembrandt")
top.equivalent = model.HumanMadeObject(ident="https://www.wikidata.org/entity/Q219831", label="Night Watch")
```


## Statements about an Entity

In many cases, current data does not support the level of specificity that the full ontology allows, or the information is simply best expressed in a human-readable form.  For example, instead of a completely modeled set of parts with materials, many museum collection management systems allow only a single human-readable string for the "medium" or "materials statement".  The same is true in many other situations, including rights or allowable usage statements, dimensions, edition statements and so forth.  Any time that there is a description of the entity, with or without qualification as to the type of description, then this pattern can be used to record the descriptive text.

The pattern makes use of the `LinguisticObject` class that is used to identify a particular piece of textual content.  These Linguistic Objects are then refered to by any other resource.  They maintain the statement's text in the `content` property, and the language of the statement (if known) in the `language` property.

Use cases for this pattern include:

* General description of the resource
* Materials statement for an object
* Attribution statement for an image
* Biography for a person
* Dimensions statement for a part of an object

Note that both Names and Statements can have their own Names (e.g. "Former Title", "Supplied Description") and their own Statements (such as the source of the name or statement), however best practice is to only use these sparingly.

__Example:__

Having only a textual description of the materials in English, the content `"Oil on Canvas"` is recorded as referring to the painting as a "materials" _(aat:300435429)_ statement:

```crom
top = model.HumanMadeObject(ident="nightwatch/4", label="Night Watch by Rembrandt")
lo = vocab.MaterialStatement(content="Oil on Canvas")
lo.language = vocab.instances['english']
top.referred_to_by = lo
```

## Events and Activities

Patterns are not only within a single entity, but also in the way that we manage relationships between entities.  While many systems link straight from one an object to its creator, for example, Linked Art instead uses an intermediate entity that represents the activity of the artist in creating the object. This enables us to associate time, place, actors, techniques, other objects and more with the creation activity, rather than needing many individual relationships.

The key participants in those different types of events are:

  * the [Object](../object/) being acted upon,
  * the [Actors](../actor/) (people or organizations) that perform the activity,
  * the [Locations](../place) at which the activity occurs,
  * and the Time at which it occurs.

The general pattern is to create a construct internal to the record for the event (with the class `Event`) or activity (with the class `Activity` or a more specific class), and associate the participants with that construct. The relationships for time (`timespan`) and place (`took_place_at`) are relevant to `Event`s that happen without the direct cause being a human action, and the relationship for the actor (`carried_out_by`) is added to those for human activities.  The relationship to the object is dependent on the type of event or activity, which are discussed in more detail in the specific sections.

There are both subclasses, such as `Birth`, `Production` and `Creation`, and classifications associated with them to be more specific, such as glassblowing _(aat:300053932)_ to clarify the type or technique of the activity. There are three common categories of activity which are used across the different entity types: their beginning of existence, their end of existence, and core activities that they either performed (for people or groups) or were required for (for objects and works). The table below summaries the beginning and ending of existence classes per main entity class. Note that conceptual entities cannot have an end of existence, and Places have neither.

| Class             | Beginning    | Ending        |
|-------------------|--------------|---------------|
| `HumanMadeObject` | `Production` | `Destruction` |
| `DigitalObject`   | `Creation`   | `Erasure`     |
| `LinguisticObject`| `Creation`   | None          |
| `VisualItem`      | `Creation`   | None          |
| `PropositionalObject`| `Creation`| None          |
| `Type`            | `Creation`   | None          |
| `Set`             | `Creation`   | None          |
| `Person`          | `Birth`      | `Death`       |
| `Group`           | `Formation`  | `Dissolution` |


__Example:__

"Spring" was produced in a Production activity carried out by Manet in 1881, somewhere in France.

```crom
top = model.HumanMadeObject(ident="spring/4", label="Jeanne (Spring) by Manet")
prod = model.Production()
top.produced_by = prod
prod.carried_out_by = model.Person(ident="manet", label="Manet")
when = model.TimeSpan(label="1881")
when.begin_of_the_begin = "1881-01-01T00:00:00"
when.end_of_the_end = "1881-12-31T23:59:59"
prod.timespan = when
prod.took_place_at = model.Place(ident="france", label="France")
```

### Time Span Details

The minimal timespan model is given above, with just the `begin_of_the_begin` and an `end_of_the_end` properties to record the beginning of the span, and the end of the span.  The end of the span **is** included in the span, and thus if the `end_of_the_end` is `"1500-01-01T00:00:00Z"`, then the 1500 **is** included, and thus the timestamp should be "1499-12-31T23:59:59Z" for the last moment of the 1400s and not any of 1500. 

The datestamps must be fully qualified with year, month, day, hour, minute and second. If a timezone is not supplied it should be assumed to be "Z" (GMT) to ensure comparisons work correctly.

It is very useful to have a `Name` for the `TimeSpan` that gives a human readable version of the machine readable timestamps and durations. This uses the pattern given above for naming things, and might be displayed to user directly, whereas the other properties could be used for matching a time-based search.

There are other properties for `TimeSpan` instances that are useful when the exact span of time is not certain.

* `end_of_the_begin`: This property is another datetime that gives the latest possible datetime for the beginning of the span.
* `begin_of_the_end`: This property is yet another datetime that gives the earliest possible datetime for the end of the span. 
* `duration`: This property refers to a `Dimension`, that describes the amount of time that the activity or event took, within the span of time.  As the property defines the type of dimension, the `Dimension` instance does not need to be `classified_as` any particular `Type` ... it is always a duration.

__Example:__ 

The Christie's auction of the Stowe House took place over 40 days in August and September, 1848 ([Source](https://www.countrylife.co.uk/luxury/art-and-antiques/5-sales-which-made-christies-no-2-the-stowe-sale-144150)).


```crom
top = vocab.AuctionEvent(ident="stowe/1", label="Auction of Stowe House")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1848-08-01T00:00:00Z"
ts.end_of_the_begin = "1848-08-20T23:59:59Z"
ts.begin_of_the_end = "1848-09-09T00:00:00Z"
ts.end_of_the_end = "1848-09-30T23:59:59Z"
dim = model.Dimension(value=40)
dim.value = 3
dim.unit = vocab.instances['days']
ts.duration = dim
n = model.Name()
n.content = "40 days in August and September, 1848"
ts.identified_by = n
top.timespan = ts 
```


## Parts

Describing the hierarchy of parts of resources is a core pattern for having increasingly granular or specific descriptions. The advantage of partitioning is that more specific information can be provided about each part, as a thing separate from the whole. This pattern covers the spectrum of different classes used in the model, from physical and textual, to temporal or geographic.  Parts are given using the properties `part_of`, from the part to the whole.

Use cases for this pattern include:

 * Delineating physical components or aspects of an object, such as the frame being part of the painting, or the recto side being part of the page.
 * Separating a long period or event into smaller sections, such as battles within a war, or the activities of different people during the production of an object.
 * Separating geographical locations into smaller subdivisions, such as that the neighborhood is part of the city, which is in turn part of the state.
 * Partitioning a text into segments, such as that the paragraph is part of a chapter, which is in turn part of the entire book

Note that these parts are separate records from the main entity, and the main entity does not refer to its parts. Instead the API defines a method to retrieve [all of the parts](/api/1.0/hal/#referring-records-links) of the main entity, or other incoming references.

__Example:__

The canvas support is part of the overall painting of Spring.

```crom
top = vocab.SupportPart(ident="spring/support", label="Support of Spring")
top.referred_to_by = vocab.MaterialStatement(content="Canvas")
top.part_of = model.HumanMadeObject(ident="spring", label="Jeanne (Spring) by Manet")
```

### Membership

Membership in a set is treated slightly differently. A set can have no members and still be a set, whereas if you destroy the last part of an object, it no longer exists. For example, a department of an organization (a Group) might not have any members due to the retirement of the last member, but there is a still an identifiable, ongoing group that would hopefully gain members when new hires are made.  Membership is given using the `member_of` property, instead of the corresponding `part_of`.

Use cases for the membership pattern include:

* A curator is a member of the paintings department of the museum.
* A painting is part of the collection of a the museum.
* An identifier is part of the set of identifiers that collectively make up the accession numbers assigned to paintings by the museum.

__Example:__

Rembrandt was a member of the Guild of St Luke.

```crom
top = model.Person(ident="rembrandt/2", label="Rembrandt")
grp = model.Group(ident="stluke", label="Guild of St Luke")
top.member_of = grp
```

### Partitioning of Internal Constructs

It is sometimes necessary to partition an activity that is embedded within another record, such as the `Production` of an object or `Creation` of a work, in order to be more specific about individual roles or aspects. In this case, as there isn't another record to refer to with `part_of`, the parts are included within the record using `part`. This allows information to be associated with either the individual parts of the activity, or the whole activity.

__Example:__

A video (modeled as a Work that contains language, or a `LinguisticObject`) about Rembrandt's Night Watch was directed by Peter Greenaway and Produced by Femke Wolting.

```crom
top = model.LinguisticObject(ident="rembrandtjaccuse/1", label="Rembrandt's J'accuse")
cre = model.Creation()
top.created_by = cre
ts = model.TimeSpan(label="2008")
ts.begin_of_the_begin = "2008-01-01T00:00:00"
ts.end_of_the_end = "2008-12-31T23:59:59"
cre.timespan = ts
pg = model.Creation()
cre.part = pg
pg.carried_out_by = model.Person(ident="greenaway", label="Peter Greenaway")
pg.classified_as = model.Type(ident="https://vocab.getty.edu/aat/300025654", label="Director")
fw = model.Creation()
cre.part = fw
fw.carried_out_by = model.Person(ident="wolting", label="Femke Wolting")
fw.classified_as = model.Type(ident="https://vocab.getty.edu/aat/300197742", label="Producer")
```
