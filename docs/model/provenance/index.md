---
title: Object Provenance
up_href: "/model/"
up_label: "Model Overview"
---

[TOC]

## Introduction

The general model for describing the provenance of an object is to track the events in which the object of interest is created or discovered, transferred between owners or custodians, until it is lost, destroyed or in its present location.  For example a painting's provenance starts when the artist paints it, and then there are events in which ownership of the painting is transferred from the artist to its first owner, and then on to subsequent owners. The details of those transfers are the primary data to be collected in the provenance part of the model.

In between the events there are periods of time in which the ownership does not change, but other interesting events may still occur, including change of custody, such as when the painting is loaned out for an [exhibition](../exhibition/) or [curation activities](curation.html), such as taking inventory, conservation or revaluation.

The provenance of an object is described as a series of activities, built on top of the basic patterns. For a single entry in the chain of provenance there are frequently multiple activities bundled together into a "Provenance Event" of interest.  These bundled activities could be the transfer of ownership, the transfer of custody, physically moving the object, a payment of money or the promise of some future action. This section documents the basic framework in which provenance events are described and subsequent sections will document specific use cases.

The chain of events starts with the production of the object by its creator, and ends only with its destruction. As there can only be one of each, they are focused on the object rather than on the activity and have a different pattern. This information is covered in the [Object](/model/object/production/) section of the model, as while the events are part of the lifecycle of the object, they are not modeled in the same way as other Provenance Events.

## Provenance Event

Provenance Events are wrapper activities which represent the context in which several more granular events occur, and represent the overall event that is tracked in the chain, rather than the specific legal and physical changes that affect one or more objects.  For example, an exchange of one object for another is a single provenance entry that involves the transfer of ownership of the two objects and thus that event would appear in both objects' timelines. It might also be accompanied by an additional payment of money, promise of an activity or other contributions. 

Provenance Events have all of the regular properties and relationships, as documented in the [baseline patterns](/model/base/). In particular, the relationships to actors, places and time reflect the overall event, and can be further specified in the separate parts if they are different and known.  

__Example:__

The Museum made a purchase in late April 2002 of a painting. The details about the painting and payment would be given using parts (the `Acquisition` and a `Payment` respectively, and described in more detail in subsequent sections).

```crom
top = vocab.ProvenanceEntry(label="Purchase of Painting")
top.identified_by = vocab.LocalNumber(value="acq-2002-0005")
museum = vocab.MuseumOrg(label="Museum")
top.carried_out_by = museum
ts = TimeSpan()
ts.begin_of_the_begin = "2002-04-19T00:00:00Z"
ts.end_of_the_end = "2002-04-26T00:00:00Z"
top.timespan = ts
acq = Acquisition(label="Acquisition of Painting from Seller")
pay = Payment(label="Payment of Price to Seller")
top.part = acq
top.part = pay
```


### Classifications

There are many different types of provenance activity that can be covered with this model, from simple purchases to exchange money for an object, or more complex endowments, promised gifts, bequeathments and so forth. These classifications should be added to the activity to clarify the particular event.

__Example:__

A benevolent donor gives two paintings to a museum.

```crom
top = vocab.ProvenanceEntry(label="Gift of two Paintings to Museum")
top.classified_as = Type(ident="http://vocab.getty.edu/aat/300417637")
acq = Acquisition(label="Acquisition of Painting 1")
acq2 = Acquisition(label="Acquisition of Painting 2")
top.part = acq
top.part = acq2
```

### Relative Times

When describing historical events, it may not be possible to give any useful timespan of when the activity occured, and only be able to relate it to happening before or after another event. This allows the activity to be ordered in a chain of events, without being explicit about any date range.

The provenance activity has two properties to cover this situation, `starts_after_the_end_of` and `ends_before_the_start_of`. The first relates to activities that occur before the current event (the start of the current event is after the end of the previous one) and the latter relates to activities that occur after the current one, by the same logic.


__Example:__


```crom
top = vocab.ProvenanceEntry(label="Undated Purchase of Painting")
top.starts_after_the_end_of = vocab.ProvenanceEntry(label="Previous Owner's Acquisition")
top.ends_before_the_start_of = vocab.ProvenanceEntry(label="Subsequent Owner's Acquisition")
```


## Parts

The Provenance Event likely includes some number of further, more specific aspects. These aspects are described in more detail in the following, linked sections.


### Acquisition and Payments

The majority of provenance events include the change of ownership of an object, or its acquisition.  Many of these acquisitions involve the payment of money, or the exchange of another object, for the transfer of ownership - a purchase rather than a gift.

These sorts of provenance events are documented in the [Acquisition](acquisition.html) section.

### Transfers of Custody

There are also provenance events that do not involve a transfer of legal ownership, only the transfer of custody or guardianship. Use cases for this include permanent loans, that might otherwise seem like ownership, and temporary loans, such as for exhibitions.  Theft or looting are both illegal transfers of custody, as the object should be restituted to its rightful owner, and the simple loss of an object is the transfer of custody to no entity in particular.

These sorts of provenance events are documented in the [Custody](custody.html) section.

### Acquisition of a Right

Some transfers of ownership are more complex than simply acquiring an object and involve the transfer of shares of ownership, possibly being traded amongst a network of owners over time. In this case, it is necessary to model the right of ownership, and how it is being divided and managed. Other scenarios where this pattern is important is when the "thing" being acquired is not a physical object, but an intellectual property right, such as the right to perform a work of theatre or other time-based media.

These sorts of provenance events are documented in the [Rights](rights.html) section.

### Rediscovery of an Object

Objects can be lost, sometimes for very long periods of time, and then encountered by a different culture or set of people than the ones that lost it. As this might happen several times in the history of an object, and there are ownership and custody implications of the rediscovery, encounters of these sorts are part of the provenance record of the object. Knowledge about previous encounters or the production of the object may not be known, meaning that it is possible that this is the first known entry in the provenance chain.

These sorts of provenance events are documented in the [Encountering an Object](encounters.html) section.

### Promise of Activity

A promise of an activity is also interesting to capture as part of a provenance event.  This includes situations where an object is on loan to an organization, but there is a promise that ownership will be given in the future according to some conditions.  Equally, a commision for an object involves a promise on the part of the artist to create an artwork, and may involve the lending of items to copy or be inspired by, and pre-payment of financial compensation. Finally, a bid at an auction is the promise to acquire the object (or objects) if it is the highest such bid.

Promises are documented in the [Promises](promises.html) section, and bids are auction specific uses of this, documented in the [Auctions](auctions.html) section.

### Movement of Object

Although not often explicitly documented, most provenance activities also involve the physical relocation of the acquired object. This is especially interesting for use with describing exhibitions, where the location is explicitly known over a period of time, or in cases where such movement is extraordinary in some way, such as the relocation of a building or other "immovable" piece of art.

These sorts of provenance events are documented in the [Movement](movement.html) section.


## Specific Uses

There are some common scenarios that can be described using Linked Art's Provenance modeling, with some additional vocabulary for precision:

* [Auctions](auctions.html)
* [Curatorial Activities during Ownership](curation.html)

