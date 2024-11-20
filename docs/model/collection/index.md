---
title: "Collections and Sets"
---

[TOC]

## Introduction

There are many use cases for grouping entities together, often of the same class but sometimes of varying types.  These use cases are exemplified in the sections below, and range from the set of objects in an auction lot, to dealer inventories and museum collections, exhibitions, a set of related concepts, or the set of people that share a common feature such as gender or nationality.

In order to cover all of the use cases with a consistent pattern, we introduce a new `Set` class from outside of CIDOC-CRM. This avoids issues with sets of entities with different types, and the semantics of the identity of objects and collections. If an equivalent class were to be added into the core CIDOC-CRM ontology in the future, a new major version of the specification would likely change to use it.


## Features

Sets are conceptual groupings, rather than physical ones.  The set of objects in a virtual exhibition or simply the set of a person's favorite objects never change their physical state by being part of the Set or not. One might have a set of destroyed objects which would be extremely strange if the Set was a physical aggregation of things which no longer existed. Sets are, thus, created by a `Creation`, not by a `Production`, and cannot be destroyed. A set may have zero members at any given point in time without going out of existence.

Like any core entity, instances of `Set` must have an `id` and `type`, are likely to have additional classifications, and can have identifiers and names. They can have statements made about them, and most importantly can have member entities.  

Entities that are members of the set are included via the `member_of` from the member entity with a value of the URI of the `Set`. Members may, in theory, be of any class, however the Linked Art API limits to only core entity types. This means that the publisher of the information about the member needs to include the `member_of` property to the `Set` instance. This is not a problem in the situation where both are managed in the same environment, nor a challenge conceptually in the model (there is the inverse `member` property), however the API does not allow for sets to refer to their members following the same design principles that groups do not refer to their members, nor objects to their parts. It also means that the members must be one of the main classes in the specification that can stand alone as [records](/api/1.0/endpoint/), such as a `HumanMadeObject` or an `Activity`, and not classes that are only used within records such as `Production` or `Name`, as there is no way to find the encapusating record.

__Example:__

The set of objects in an exhibition.

```crom
top = model.Set(ident="exhset/1", label="Exhibition objects")
top.identified_by = vocab.PrimaryName(content="Objects in Manet and Modern Beauty")
top.referred_to_by = vocab.Description(content="Objects in the exhibition Manet and Modern Beauty at the Art Institute of Chicago and the Getty Museum")
cre = model.Creation()
ts = model.TimeSpan()
ts.begin_of_the_begin = "2019-05-01"
ts.end_of_the_end = "2019-05-01"
cre.timespan = ts
top.created_by = cre
```

An object in that set.

```crom
top = vocab.Painting(ident="spring/13", label="Jeanne (Spring) by Manet")
top.identified_by = model.Name(content="Jeanne (Spring)")
top.member_of = model.Set(ident="exhset")
```

### Order of Members

In order to ensure that the members are ordered correctly, a sort value can be added as an Identifier on the member. This value should sort correctly with respect to the other members of the set, with the alphanumerically lowest identifier value being presented first and then in ascending order from there. This identifier may have an `AttributeAssignment` associated with it that is `influenced_by` the Set in which the sort value should be applied. This allows the same entity to be a member of multiple ordered sets at the same time.

__Example:__

The Obermeyer letter described in the [archives use case](/model/archives/#archival-hierarchy) should sort as "000001" within the Stieglitz Family Letters set.

```crom
top = model.HumanMadeObject(ident="letter/2", label="Obermeyer 1920")
top.identified_by = vocab.PrimaryName(content="Obermeyer, Bertha (1920)")
sv = vocab.SortValue(content="000001")
aa = model.AttributeAssignment()
aa.influenced_by = model.Set(ident="archive_sfl", label="Stieglitz Family Letters")
sv.assigned_by = aa
top.identified_by = sv
top.member_of = model.Set(ident="archive_sfl", label="Stieglitz Family Letters")
```

### Prototypical Members

The information about any particular member of a set might not be available, however general information might be known about the entities that are members of the set. For example, objects in a particular set might have been created by the same person, be classified as the same type, or have had the same owner. Works might be written in the same language, be about the same subject, and so on. As any entity can be a member of a set, this gives a lot of freedom to describe the sorts of things that have been grouped together. This is frequently true for Archives, but can also be valuable for making the rationale for the set be more apparent, such as that the objects curated by a Paintings department are (generally) paintings.

The description of prototype member is embedded within the set as the value of the `members_exemplified_by` property. 

This is not the 'highlight' members of the set, such as the famous pieces in a collection of objects. For that, use the [Related Objects](/model/assertions/) pattern. Using this approach does not imply that *every* member of the set has all of the features of the prototypical member, however care should be taken to not include information that is not generally true.

__Example:__

The objects exhibited were typically (but not exclusively) paintings by Manet.

```crom
top = model.Set(ident="exhset/2", label="Exhibition objects")
hmo = vocab.Painting()
prod = model.Production()
prod.carried_out_by = model.Person(ident="http://vocab.getty.edu/ulan/500010363", label="Manet")
hmo.produced_by = prod
top.members_exemplified_by = hmo
```

## Collections of Objects

Sets can be used to describe the set of objects that make up a curated collection. This is not necessarily the same as the set of objects that the institution owns, as there could be objects which are looked after but owned by some other organization or individual, nor the set of objects that the institution currently has custody over, as objects being loaned to other organizations for exhibitions are still part of the conceptual collection of objects. The details of the relationship between the object and the institution are recorded on the object, and the Set provides identity for the collection itself, independently of the member objects.  Objects can be part of multiple collections at the same time -- the private owner's personal collection and the museum's public collection.  So while the majority of objects are both owned by and in the custody of the organization, this is not certain and should not be inferred.

Institutions are often split up into departments, each of which will manage a part of the overall collection. These parts of the collection are managed as separate Sets, rather than somewhow within a single Set. The departmental collections may be members of the institutional collection in the same way that the department is a `member_of` the organization. It is useful to be able to describe the properties of the object in each of the contexts, and allow a separate structure of inventory management from organizational chart. The department might also conceive of further sets of their objects, without any direct correspondence and likely with the same object being part of more than one set at the same time.

__Example:__

The full collection of the Rijksmuseum.

```crom
top = vocab.CollectionSet(ident="rijks_objects/1", label="Collection of the Rijksmuseum")
top.identified_by = vocab.PrimaryName(content="Collection of the Rijksmuseum")
```

The paintings of the Rijksmuseum, as curated by the Paintings department.

```crom
top = vocab.CollectionSet(ident="rijks_paintings/1", label="Paintings of the Rijksmuseum")
top.identified_by = vocab.PrimaryName(content="Paintings of the Rijksmuseum")
top.member_of = model.Set(ident="rijks_objects", label="Collection of the Rijksmuseum")
cur = vocab.Curating()
cur.carried_out_by = model.Group("rijks_paintings_dept", label="Paintings Department")
top.used_for = cur
```

The Night Watch is a member of the paintings set.

```crom
top = vocab.Painting(ident="nightwatch/16", label="Night Watch by Rembrandt")
top.identified_by = vocab.PrimaryName(content="The Night Watch")
top.member_of = model.Set(ident="rijks_paintings", label="Paintings of the Rijksmuseum")
```


## Other Use Cases

### Sets of People

A Group is a Set of other `Group`s and `Person`s which can take action. This means that the features of Sets are also available for use with Groups, such as `members_exemplified_by`. This allows us to be specific about prototypical members of large groups, such as nationalities or "unidentified" people.

/// warning
That Set is a new super-class of Group is only true when using the Linked Art ontology and not true in the CIDOC-CRM base ontology, as Linked Art introduces the notion of the Set.
///


__Example:__

The prototypical member of the "14th Century Italians" group was a person born between 1300 and 1400 in Italy.

```crom
top = model.Group(ident="14thc_italian/1", label="14th c italians")
top.identified_by = model.PrimaryName(content="Unidentified 14th Century Italian")
p = model.Person()
b = model.Birth()
ts = model.TimeSpan()
ts.begin_of_the_begin = "1300-01-01T00:00:00Z"
ts.end_of_the_end = "1399-12-31T00:00:00Z"
b.timespan = ts
b.took_place_at = model.Place(ident="https://vocab.getty.edu/tgn/1000080", label="Italy")
p.born = b
top.members_exemplified_by = p
```

### Archives

Set is used extensively in the model for [Archives](/model/archives/).

### Auction Lots

The set of objects in an [auction lot](/model/provenance/auctions.html#set-of-objects) are also modeled as a Set. These are not curated in the same way as a museum collection, are not necessarily ever brought together physically, and may not even be physical but instead digital objects, but are being put up for auction as a single entity.  Similarly, the set of objects used in an [exhibition](/model/exhibition/#objects) is also modeled as a Set.

### Collection Specific Information

Information about an entity that is specific to the context of the set that they are part of, such as the accession number of an object for that particular collection, can be described using the `AttributeAssignment` patterns described in the page about [assertions](/model/assertion/#context-specific-assertions) in the same way as the sort value within the set described above.

