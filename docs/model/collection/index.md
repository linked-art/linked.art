---
title: "Collections and Sets"
---

[TOC]

## Introduction

There are many use cases for grouping resources together, often of the same class but sometimes of varying types.  These use cases are exemplified in the sections below, and range from the set of objects in an auction lot, to dealer inventories and museum collections, exhibitions, a set of related concepts, or the set of people that share a common feature such as gender or nationality.

In order to cover all of the use cases with a consistent pattern, we adopt the `Aggregation` class from outside of CIDOC-CRM.  This also gives us access to a convenient pattern for context-specific information, via the `Proxy` class. This avoids issues with sets of resources with different types, and the semantics of the identity of objects and collections.

## Aggregations

### Core Features

Aggregations are conceptual groupings, rather than physical ones.  The set of objects in a virtual exhibition or simply the set of a person's favorite objects never change their physical state by being part of the Aggregation or not.  Aggregations are thus created by a `Creation`, not by a `Production`.

Like any resource, Aggregations must have an `id` and `type`, are likely to have additional classifications, and can have Identifiers and Names. They can have statements made about them, and have member resources.  These member resources are included via the `aggregates` property rather than `part`, as the inverse relationship would be ambiguous in some situations.  

```crom
top = CollectionSet()
top._label = "Example Collection"
p = Painting()
p._label = "Example Painting"
top.member = p
desc = Description()
desc.content = "This is a lovely little collection"
top.referred_to_by = desc
n = Name()
n.content = "Example Collection"
top.identified_by = n
cre = Creation()
ts = TimeSpan()
ts.begin_of_the_begin = "1954-01-01"
ts.end_of_the_end = "1955-01-01"
cre.timespan = ts
top.created_by = cre
```


### Collections of Objects

Aggregations can be used to record the set of objects that make up a curated collection. This not necessarily the set of objects that the institution owns, as there could be objects which are looked after but owned by some other organization or individual, nor the set of objects that the institution has custody over, as objects being loaned to other organizations for exhibitions are still part of the conceptual collection of objects. The details of the relationship between the object and the institution are recorded on the object, and the Aggregation simply records which objects are thought of as being part of the collection.  Objects can be thought of as being part of multiple collections at the same time -- the private owner's personal collection and the museum's public collection.  So while the majority of objects are both owned by and in the custody of the organization, this is not certain and should not be inferred. The Aggregation is created by the organization or person that abstractly manages the collected objects.

This pattern can be used for any type of organization that manages objects, from museums and archives to individuals and art dealers.

```crom
top = CollectionSet()
top._label = "Collection of Example Museum"
p = Painting()
p._label = "Example Painting"
top.member = p
cre = Creation()
inst = vocab.MuseumOrg()
inst._label = "Example Museum"
cre.carried_out_by = inst
top.created_by = cre
```

#### Departmental Collections

Institutions are often split up into departments, each of which will manage a part of the overall collection. These parts of the collection are managed as separate Aggregations, rather than a tree structure of Aggregations of Aggregations.  It is useful to be able to describe the properties of the object in each of the contexts, and allow a separate structure of inventory management from organizational chart. The department might also conceive of further sets of their objects, without any direct correspondence and likely with the same object being part of more than one set at the same time.

```crom
top = CollectionSet()
top._label = "Collection of Example Museum's Paintings Department"
p = Painting()
p._label = "Example Painting"
top.member = p
cre = Creation()
inst = vocab.MuseumOrg()
inst._label = "Example Museum"
dept = vocab.Department()
dept._label = "Paintings Department"
dept.member_of = inst
cre.carried_out_by = dept
top.created_by = cre
```

### Uses Described Elsewhere

The [nationality](/model/actor/#nationality) and [gender](/model/actor/#gender) are two uses of Aggregations where the aggregated resources are people rather than objects.  These are conceptual sets of people, where the set does not have the capacity to carry out activities as a single whole, unlike an organization.  A person can be part of multiple such Aggregations at the same time, such as non-binary gendered people and dual-nationality citizens.

The set of objects in an [auction lot](/model/provenance/auctions.html#set-of-objects) are also modeled as an Aggregation. These are not curated, and not necessarily ever brought together physically, but are being put up for auction as a single entity.  Similarly, the set of objects used in an [exhibition](/model/exhibition/#objects) is also modeled as an Aggregation.

### Collection Specific Information

Information about a resource that is specific to the context of the Aggregation that they are part of, such as the accession number of an object for that particular collection, can be described using the AttributeAssignment and Proxy patterns described in the page about [assertions](/model/assertion/#context-specific-assertions).  In particular, relationships may be associated with the Proxy for a resource in an Aggregation which are then interpreted as being about the resource within that context.


## Collections over Time

Collections are not static over time but instead change as objects are acquired and sold, stolen or given to new owners. Recording these states results in some complexity, as we still want to be able to refer to objects in a previous context, rather than just their current context. It is useful, for example, to record the accession or stock number of an object in previous collections or as assigned by dealerships and auction houses.  For collections that never change once finished, this isn't a problem.  The object can be considered to always be part of the auction lot.  However for museum or dealer collections, it is important to distinguish between the objects that are currently part of that collection and the objects that have ever been part of the collection. 

The solution that has been adopted is to have two different types of aggregation for the same collection, one is a snapshot at a particular time and normally the current time, and the other is atemporal and records all of the objects that have ever been part of the collection. The atemporal Aggregation is the focus, as along with the full provenance of the objects, it can be used to generate the snapshot at any given point in time.

Much of the time only one is needed at all.  The current set of people with a particular nationality is unimportant, only that a particular person was of that nationality when they were alive. The nationality aggregation is thus always atemporal and snapshots are impossible to generate.  Conversely, there is no need for an atemporal auction lot, as the set of objects never changes.


### Adding and Removing Resources

Objects are rarely added and removed from collections without further contextual information, there is almost always some larger activity that results in the change.  The ownership of the object is transferred to the organization which prompts it to be accessioned into the collection, and subsequently an accession number Identifier as assigned to it.

There are two activities, Adding and Removing.  They reference the Proxy, rather than having relationships to the object and the collection, in order to ensure that information associated with the Proxy can be tied to the activity.


### Snapshots

