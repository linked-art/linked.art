---
title: Transfer of Rights
up_href: "/model/provenance/"
up_label: "Provenance"
---

[TOC]

## Introduction

Ownership is often more complicated than a single individual acquiring an object and immediately having both physical possession and the legal right of ownership.  This section deals with the description of more complex scenarios that require explicitly describing the right that is held by a particular actor, such as for asymmetric shared ownership of an object. Other scenarios in which a right is being transferred or created rather than the more specific case of the entire right of ownership are also covered here, such as the intellectual property right to perform a work of time-based media or theatre.


## Rights and their Acquisition

The model for acquiring an object (by purchase, gift or other means) incorporates the specific right of ownership into the properties of the `Acquisition` resource.  The acquisition transfers the title of the object between parties, but that "title" could be expanded to a more completely modeled `Right`.  For some scenarios where we have more information about the interactions and legal status, we need to explicitly model these rights.

Rights are conceptual things that apply to their real world subjects. They are not relative to time, but can be established and invalidated by various activities or events.  The simplest case would be that as part of the provenance event where an object is acquired, there is also the establishment of the right of ownership of that object by the new owner and the invalidation of the right of ownership of the previous owner.

While it is possible and valid to have both the `Acquisition` and the `Right` in a single provenance entry, it is redundant as the acquisition model is simpler and more concise without losing any information. The sections below introduce scenarios in which information would be lost without the explicit modeling of the Right.

In order to connect the `Right` to the provenance activity, we introduce a new `Activity` subclass called `RightAcquistion`.  It has two new properties: `establishes` links the `Right` that was established by this activity, and `invalidates` can optionally link to the `Right` that was rendered invalid by the activity.  

Instances of `Right` have two properties: `possessed_by` refers to the actor (`Group` or `Person`) that has the right described, and `applies_to` refers to the thing over which the right pertains.

```crom
top = vocab.ProvenanceEntry()
# Omit some classifications for readability
what = model.HumanMadeObject(label="Painting")
who = model.Group(label="Museum")
xfer = Acquisition()
xfer.transferred_title_of = what
xfer.transferred_title_to = who
top.part = xfer
rxfer = model.RightAcquisition()
right = vocab.OwnershipRight(label="Right of Ownership for Painting")
rxfer.establishes = right
right.possessed_by = who
right.applies_to = what
top.part = rxfer
```


## Multiple Owners with Different Stakes

A change in ownership might involve more than two parties, resulting in a state where multiple actors together own some share of the object.  Examples of this situation include when art dealers share the costs of purchasing an object and then share the proceeds of sale in the same proportions, when a donor gives part of the value of an object to an institution, or when a marriage is dissolved and the value of the object is split between the individuals.

The base acquisition model allows for ownership to be transferred to multiple actors, but it is impossible to then determine the share of the value that was owned by each party and the implicit assumption should be that all parties owned equal shares. In order to allow for the description of different proportions of the object to be owned by different actors, we need partition the `Right` into shares to be divided. These components are themselves `Right`s that are possessed by the respective parties.

In the same way as describing the physical extent of a physical object, we can use a `Dimension` to describe the logical extent of the ownership. At any given time the total shares of an object should, of course, add up to the entire object.  If this is not true, then it might signify either that the accounting is wrong (more than 100% of the object is claimed as being owned), theft (multiple claims of ownership at the same time, some of which are illegal), or just that it is now unknown what happened.

```crom
top = vocab.ProvenanceEntry(label="Purchase of Painting by Two Dealers")
d1 = Group(label="Dealer 1")
d2 = Group(label="Dealer 2")
what = Painting(label="Painting")
unit = MeasurementUnit(ident="http://qudt.org/1.1/vocab/unit/Percent", label="Percent")
right = vocab.OwnershipRight(label="Total Right of Ownership")

rxfer = model.RightAcquisition()
top.part = rxfer
rxfer.establishes = right
right.applies_to = what

r1 = vocab.OwnershipRight(label="30% Ownership by Dealer 1")
r1.possessed_by = d1
dim1 = Dimension()
dim1.value = 30
dim1.unit = unit
r1.dimension = dim1
right.part = r1

r2 = vocab.OwnershipRight(label="70% Ownership by Dealer 2")
r2.possessed_by = d2
dim1 = Dimension()
dim1.value = 70
dim1.unit = unit
r2.dimension = dim1
right.part = r2
```


### Transfer of Shares

Once the share of an object has been established, that right can be traded as part of future provenance entries.  

In order to maintain consistency with the original establishment of the division of ownership, the difference between the initial state and the new state is not described, but instead the new state is described directly. If a 10% share is acquired from another owner, the 10% is not traded requiring the system to calculate the new total proportions, but instead the new total proportions are described. 

If only existing owners are part of the entry, then there is no need to establish a new Right that is the new total ownership, it is simply a new division of the existing total. Ownership Rights are brought into existence by `Acquisition` events - the set of people who possess the right is fixed, and is the same set of actors as those referenced by `title_transferred_to`. Thus any new Acquisition by a new partial owner requires a new Ownership Right, as described above.


```crom
top = vocab.ProvenanceEntry(label="Trading Shares of Painting between Two Dealers")
d1 = Group(label="Dealer 1")
d2 = Group(label="Dealer 2")
what = Painting(label="Painting")
unit = MeasurementUnit(ident="http://qudt.org/1.1/vocab/unit/Percent", label="Percent")

rx1 = model.RightAcquisition()
top.part = rx1
r1 = vocab.OwnershipRight(label="40% Ownership by Dealer 1")
r1.possessed_by = d1
r1.applies_to = what
dim1 = Dimension()
dim1.value = 40
dim1.unit = unit
r1.dimension = dim1
rx1.establishes = r1
rx1.invalidates = vocab.OwnershipRight(label="30% Ownership by Dealer 1")

rx2 = model.RightAcquisition()
top.part= rx2
r2 = vocab.OwnershipRight(label="60% Ownership by Dealer 2")
r2.possessed_by = d2
dim1 = Dimension()
dim1.value = 70
dim1.unit = unit
r2.dimension = dim1
rx2.establishes = r2
rx2.invalidates = vocab.OwnershipRight(label="70% Ownership by Dealer 2")
```

## Intellectual Property Rights

Other sorts of rights associated with art that can be acquired include the intellectual property rights, such as copyright for a text or image, separate from any physical carrier, or the right to perform some piece of time-based media such as a projected installation.  The manipulation of these rights also uses the `RightAcquisition` pattern.

Many copyrights for images are owned by collective organizations rather than individuals, and these organizations can acquire and exchange those copyrights completely independently of any physical carrier of the image.

__Example:__

A copyright management organization, the Paintings Copyright Association, acquired the copyright for a particular painting in 2014.


```crom
top = vocab.ProvenanceEntry(label="Copyright acquisition by PCA")
pca = model.Group(label="Paintings Copyright Association")
what = vocab.Painting(label="Painting", art=1)
xfer = model.RightAcquisition()
top.part = xfer
right = vocab.CopyrightRight()
xfer.establishes = right
right.possessed_by = pca
right.applies_to = what
```
