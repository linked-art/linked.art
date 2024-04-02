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
	There are ongoing efforts within CIDOC to standardize how to describe social bonds between parties, activity plans that describe the conditions under which some activity would or did take place, and the management of ownership and other rights over time.  The model presented here concerning promise activities has reduced fidelity compared to these efforts, and when they have stabilized, the modeling may be revised to take them into account.

There is a necessary vocabulary term, given the lack of a more explicit class to model activity plans or social bonds, in order to distinguish a Promise from any other activity.

* __Promise:__ (_aat:300435599_) A promise that some future activity will be carried out.


## Promised Gift

A promise of a gift (or sale, or exchange) is an Activity which is carried out by the promising party.  It is a promise to some other actor to perform some further activity (the giving or sale of the object), however we lack the ontological machinery at the moment to make this explicit. Instead we can reference the promised party and the object being promised only via the more general properties of `participant` and `used_specific_object` respectively. 

Further details and clarification about the promise, including any description of the contract, should be given in a descriptive note on the promise activity.

__Example:__

Thomas Jaffe has promised to give the 19th Century Indo-Pacific Coffin to Yale University Art Gallery.

```crom
top = vocab.ProvenanceEntry(ident="coffin_promise/1", label="Promised Gift of Coffin")
promise = vocab.Promise(label="Promise of Gift")
own = model.Person(ident="jaffe", label="Thomas Jaffe")
mus = model.Group(ident="yuag", label="Yale University Art Gallery")
what = model.HumanMadeObject(ident="coffin", label="Coffin")
promise.referred_to_by = vocab.Description(content="Promised gift of Thomas Jaffe, B.A. 1971")
promise.carried_out_by = own
promise.participant = mus
promise.used_specific_object = what
top.part = promise
```

## Commissions for Artwork

Another type of promise can occur even before the artwork is produced: a commission from a sponsor for the production of the work. This starts out with paired promises, where the artist promises to produce the work, and the commissioner promises to pay for it.  There might be some amount of money paid to the artist in advance, or other transfers of custody or ownership of objects, such as lending something to the artist to produce a copy of.  Given the potential for multiple exchanges of promises, money, and objects, the description of the commissioning activity fits cleanly into the broader Provenance Entry model.

The description of the production of the commissioned object is taken care of by the regular production pattern, as described in the [object](/model/object/) section. The subsequent transfer of title to the new owner, and the payment of any monies due to the artist is a second provenance entry following all of the regular patterns.

__Example:__

The "Nuveen Painting" by Jim Dine was commissioned by Richard Franke in 1985.

```crom
top = vocab.ProvenanceEntry(ident="nuveen_commission/1", label="Commission of Painting")
promise = vocab.Promise(label="Obligation to Pay Artist")  
fromwho = model.Person(ident="franke", label="Richard Franke")
towho = model.Person(ident="dine", label="Jim Dine")
promise.carried_out_by = fromwho
promise.participant = towho
promise.referred_to_by = vocab.Description(content="Promise to pay for a painting to be created by the artist")
top.part = promise
promprod = vocab.Promise(label="Obligation to Produce Painting")
promprod.carried_out_by = towho
promprod.participant = fromwho
promprod.referred_to_by = vocab.Description(content="Promise to produce a painting for the commissioning party")
top.part = promprod
```

The resulting production activity has a cause, which is the above Provenance Event.

```crom
top = vocab.Painting(ident="nuveen/1", label="Nuveen Painting")
top.identified_by = vocab.PrimaryName(content="The Nuveen Painting")
prod = model.Production()
prod.carried_out_by = model.Person(ident="dine", label="Jim Dine")
prod.caused_by = model.Activity(ident="nuveen_commission", label="Commission of Painting")
```
