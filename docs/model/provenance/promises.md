---
title: Promised Activities
up_href: "/model/provenance/"
up_label: "Provenance"
---

[TOC]

## Introduction

Many acquisitions are first long term loans, with a promise that ownership of the object will also be transferred after some conditions have been met. These promises are also typically enforced via a legal contract.

There might also be other promised activities, with or without a contract, that are valuable to document if known. This could include the promise to produce an artwork in exchange for money, typically called a commission.

!!! note "Model Subject to Change"
	There is ongoing efforts to standardize how to describe social bonds between parties, activity plans that describe the conditions under which some activity would or did take place, and the management of ownership and other rights over time.  The model presented here concerning promise activities has reduced fidelity compared to these efforts, and when they have stabilized, the modeling may be revised to take into account those new facilities.

There is a necessary vocabulary term, given the lack of a more explicit class to model activity plans or social bonds, in order to distinguish a Promise from any other activity.

* __Promise:__ (_aat:300435599_) A promise that some future activity will be carried out.


## Promised Gift

A promise of a gift (or sale, or exchange) is an Activity which is carried out by the promising party.  It is a promise to some other actor to perform some further activity (the acquisition), however we lack the ontological machinery at the moment to make this explicit. Instead we can reference the promised party and the object being promised only via the more general properties of `participant` and `used_specific_object` respectively. 

Further details and clarification about the promise, including any description of the contract, should be given in a descriptive note on the promise activity.



__Example:__

The owner of a painting promises to give it to a museum after a period of time.

```crom
top = vocab.ProvenanceEntry()
promise = vocab.Promise(label="Promise of Gift")
own = model.Person(label="Owner")
mus = model.Group(label="Museum")
what = model.HumanMadeObject(label="Painting")
promise.referred_to_by = vocab.Description(content="Contractual gift over time from Owner to be completed in 2032")
promise.carried_out_by = own
promise.participant = mus
promise.used_specific_object = what
top.part = promise
```

## Commissions for Artwork

Another type of promise can occur even before the artwork is produced: a commission from a sponsor for the production of the work. This starts out with paired promises, where the artist promises to produce the work, and the commissioner promises to pay for it.  There might be some amount of money paid to the artist in advance, or other transfers of custody or ownership of objects, such as lending something to the artist to produce a copy of.  Given the potential for multiple exchanges of promises, money, and objects, the description of the commissioning activity fits cleanly into the broader Provenance Entry model.

The description of the production of the commissioned object is taken care of by the regular production pattern, as described in the [object](/model/object/) section. The subsequent transfer of title to the new owner, and the payment of any monies due to the artist is a second provenance entry following all of the regular patterns.

__Example__:

The commissioner of the art promises to pay $1000, with 10% of that up front, for a painting to be produced. This involves three steps: the exchange of promised activities, the production of the object, and then the exchange of the ownership of the produced painting for the remainder of the money.

```crom
top = vocab.ProvenanceEntry(label="Commission of Painting")
promise = vocab.Promise(label="Obligation to Pay Artist")  
fromwho = model.Person(label="Commissioner")
towho = model.Person(label="Artist")
promise.carried_out_by = fromwho
promise.participant = towho
promise.referred_to_by = vocab.Description(content="Promise to pay $1000 for a painting to be created by the artist, with 10% in advance")
top.part = promise
promprod = vocab.Promise(label="Obligation to Produce Painting")
promprod.carried_out_by = towho
promprod.participant = fromwho
promprod.referred_to_by = vocab.Description(content="Promise to paint a landscape for the commissioning party")
top.part = promprod
pay = model.Payment(label="Down Payment")
pay.paid_from = fromwho
pay.paid_to = towho
ma = model.MonetaryAmount(value=100)
ma.currency = vocab.instances['us dollars']
pay.paid_amount = ma
top.part = pay
```

The resulting production activity has a cause, which is the above Provenance Event.

```crom
top = vocab.Painting(label="Commissioned Landscape Painting")
top.referred_to_by = vocab.Description(content="A commissioned painting by Artist")
prod = model.Production()
prod.carried_out_by = model.Person(label="Artist")
prod.caused_by = vocab.ProvenanceEntry(label="Commission of Painting")
```

And finally the painting is delivered to the commissioning party from the artist in exchange for the remainder of the money.

```crom
top = vocab.ProvenanceEntry(label="Delivery of Painting")
artist = model.Person(label="Artist")
owner = model.Person(label="Commissioner")
what = model.HumanMadeObject(label="Painting")
acq = model.Acquisition()
acq.transferred_title_of = what
acq.transferred_title_from = artist
acq.transferred_title_to = owner
top.part = acq
pay = model.Payment(label="Payment")
pay.paid_from = owner
pay.paid_to = artist
ma = model.MonetaryAmount(value=900)
ma.currency = vocab.instances['us dollars']
pay.paid_amount = ma
top.part = pay
```


