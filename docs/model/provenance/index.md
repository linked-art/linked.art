---
title: Object Provenance
up_href: "/model/"
up_label: "Model Overview"
---



## Introduction

The general model for describing the provenance of an object is to track the events in which the object of interest is created or discovered, transferred between owners or custodians, until it is lost, destroyed or in its present location.  For example a painting's provenance starts when the artist paints it, and then there are events in which ownership of the painting is transferred from the artist to its first owner, and then on to subsequent owners. The details of those transfers are the primary data to be collected in the provenance part of the model.

In between the events there are periods of time in which the ownership does not change, but other interesting events may still occur, including change of custody, such as when the painting is loaned out for an [exhibition](../exhibition/) or [curation activities](curation), such as taking inventory, conservation or revaluation that establish the object's location and ownership at a point in time.

The provenance of an object is described as a series of activities, built on top of the basic patterns. For a single entry in the chain of provenance there are frequently multiple activities bundled together into a "Provenance Event" of interest.  These bundled activities could be the transfer of ownership, the transfer of custody, physically moving the object, a payment of money or the promise of some future action. This section documents the basic framework in which provenance events are described and subsequent sections will document specific use cases.

The chain of events starts with the production of the object by its creator, and ends only with its destruction. As there can only be one of each, they are focused on the object rather than on the activity and have a different pattern. This information is covered in the [Object](/model/object/production/) section of the model, as while the events are part of the lifecycle of the object, they are not modeled in the same way as other Provenance Events.

## Provenance Event

Provenance Events are wrapper activities which represent the context in which several more granular events occur, and represent the overall event that is tracked in the chain, rather than the specific legal and physical changes that affect one or more objects.  For example, an exchange of one object for another is a single provenance entry that involves the transfer of ownership of the two objects and thus that event would appear in both objects' timelines. It might also be accompanied by an additional payment of money, promise of an activity or other contributions. 

Provenance Events have all of the regular properties and relationships, as documented in the [baseline patterns](/model/base/). In particular, the relationships to actors, places and time reflect the overall event, and can be further specified in the separate parts if they are different and known.  

__Example:__

Édouard Manet sold his painting, Jeanne, to Antonin Proust in 1883 for 3,000 francs.

```crom
top = vocab.ProvenanceEntry(ident="manet_proust/1", label="Purchase of Spring by Proust")
top.identified_by = vocab.PrimaryName(content="Purchase of Spring by Proust from Manet")

ts = model.TimeSpan()
ts.begin_of_the_begin = "1881-01-01T00:00:00Z"
ts.end_of_the_end = "1883-12-31T23:59:59Z"
top.timespan = ts

acq = model.Acquisition(label="Ownership of Spring to Proust")
top.part = acq
acq.transferred_title_of = model.HumanMadeObject(ident="spring", label="Spring")
acq.transferred_title_from = model.Person(ident="manet", label="Manet")
acq.transferred_title_to = model.Person(ident="proust", label="Proust")

pay = model.Payment(label="3000 Francs to Manet")
pay.paid_from = model.Person(ident="proust", label="Proust")
pay.paid_to = model.Person(ident="manet", label="Manet")
amnt = model.MonetaryAmount()
amnt.currency = vocab.instances['fr francs']
amnt.value = 3000
pay.paid_amount = amnt
top.part = pay
```


### Classifications

There are many different types of provenance activity that can be covered with this model, from simple purchases to exchange money for an object, or more complex endowments, promised gifts, bequeathments and so forth. These classifications should be added to the activity to clarify the particular event.

__Example:__

Xu Ziwei gave her painting "Landscape" to Yale University Art Gallery in 1999

```crom
top = vocab.ProvenanceEntry(ident="ziwei_yuag/1", label="Gift of Landscape to YUAG")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300417637")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1999-01-01T00:00:00Z"
ts.end_of_the_end = "1999-12-31T23:59:59Z"
top.timespan = ts
acq = model.Acquisition(label="Acquisition of Painting 1")
acq.transferred_title_of = model.HumanMadeObject(ident="ziwei_landscape", label="Landscape")
acq.transferred_title_to = model.Group(ident="yuag", label="Yale University Art Gallery")
acq.transferred_title_from = model.Person(ident="ziwei", label="Xu Ziwei")
top.part = acq
```

### Relative Times

When describing historical events, it may not be possible to give any useful timespan of when the activity occured, and only be able to relate it to happening before or after another event. This allows the activity to be ordered in a chain of events, without being explicit about any date range.

The provenance activity has two properties to cover this situation, `after` (this event starts after the end of the referenced event) and `before` (this event ends before the start of the referenced event). The first relates to activities that occur before the current event (the start of the current event is after the end of the previous one) and the latter relates to activities that occur after the current one, by the same logic.


__Example:__

Jean-Baptise Faure owned Spring after Proust (but not necessarily directly from Proust), before transferring it to the Galerie Durand-Ruel (Paris) in 1907.

```crom
top = vocab.ProvenanceEntry(ident="unknown_faure/1", label="Unknown Acquisition of Spring by Faure")
top.after = vocab.ProvenanceEntry(ident="manet_proust")
top.before = vocab.ProvenanceEntry(label="foure_durand")
```


## Parts

The Provenance Event likely includes some number of further, more specific aspects. These aspects are described in more detail in the following, linked sections.


### Acquisition and Payments

The majority of provenance events include the change of ownership of an object, or its acquisition.  Many of these acquisitions involve the payment of money, or the exchange of another object, for the transfer of ownership - a purchase rather than a gift.

These sorts of provenance events are documented in the [Acquisition](acquisition) section.

### Transfers of Custody

There are also provenance events that do not involve a transfer of legal ownership, only the transfer of custody or guardianship. Use cases for this include permanent loans, that might otherwise seem like ownership, and temporary loans, such as for exhibitions.  Theft or looting are both illegal transfers of custody, as the object should be restituted to its rightful owner, and the simple loss of an object is the transfer of custody to no entity in particular.

These sorts of provenance events are documented in the [Custody](custody) section.

### Rediscovery of an Object

Objects can be lost, sometimes for very long periods of time, and then encountered by a different culture or set of people than the ones that lost it. As this might happen several times in the history of an object, and there are ownership and custody implications of the rediscovery, encounters of these sorts are part of the provenance record of the object. Knowledge about previous encounters or the production of the object may not be known, meaning that it is possible that this is the first known entry in the provenance chain.

These sorts of provenance events are documented in the [Encountering an Object](encounters) section.

### Acquisition of a Right

Some transfers of ownership are more complex than simply acquiring an object and involve the transfer of shares of ownership, possibly being traded amongst a network of owners over time. In this case, it is necessary to model the right of ownership, and how it is being divided and managed. Other scenarios where this pattern is important is when the "thing" being acquired is not a physical object, but an intellectual property right, such as the right to perform a work of theatre or other time-based media.

Note that this section is complicated, and likely only valuable to specialized databases of provenance. Feedback is welcome to improve its usability and accuracy in representing the transfer of non-physical ownership.

These sorts of provenance events are documented in the [Rights](rights) section.

### Promise of Activity

A promise of an activity is also interesting to capture as part of a provenance event.  This includes situations where an object is on loan to an organization, but there is a promise that ownership will be given in the future according to some conditions.  Equally, a commision for an object involves a promise on the part of the artist to create an artwork, and may involve the lending of items to copy or be inspired by, and pre-payment of financial compensation. Finally, a bid at an auction is the promise to acquire the object (or objects) if it is the highest such bid.

Promises are documented in the [Promises](promises) section, and bids are auction specific uses of this, documented in the [Auctions](auctions) section.

### Movement of Object

Although not often explicitly documented, most provenance activities also involve the physical relocation of the acquired object. This is especially interesting for use with describing exhibitions, where the location is explicitly known over a period of time, or in cases where such movement is extraordinary in some way, such as the relocation of a building or other "immovable" piece of art.

These sorts of provenance events are documented in the [Movement](movement) section.

### Unknown Type of Transfer

When working from incomplete documentary evidence it is frequently difficult to determine exactly what sort of exchange took place in the past. For example, an archive or letter might say that the object "went to the museum", which would be insufficient to distinguish between a transfer of ownership, a transfer of custody, or merely physical movement of the object. While every effort should be made to be precise in provenance document whenever possible, it is also important to capture uncertain activities.

These sorts of provenance events are document in the [Transfer](transfer) section.


## Specific Uses

There are some common scenarios that can be described using Linked Art's Provenance modeling, with some additional vocabulary for precision:

* [Auctions](auctions)

