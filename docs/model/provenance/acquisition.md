---
title: Object Acquisition and Loan
up_href: "/model/provenance/"
up_label: "Provenance"
---

[TOC]

## Introduction

The majority of recorded provenance events are when the object changes ownership, and the various methods in which that happens.  In the descriptions below the terms 'seller' and 'buyer' are used to refer to the actor that is relinquishing ownership and the actor that is gaining ownership, even if there is no money or other goods or services changing hands. This is for clarity and conciseness of the descriptions, and not to imply that every transaction is a purchase.

## Object Acquisition

Acquisitions are used to describe the transfer of ownership of an object from one owner to the next. The first owner is typically the artist, who would then transfer it to the second owner, to the third owner and so on. The ownership chain can be expressed by repeating this same pattern with the buyer from one acquisition being the seller in the subsequent one.  If the previous owner (e.g. the seller if there is a value exchange) or the subsequent owner (e.g. the buyer) is not known for a particular acquisition, then the reference can be left out from the description.  
  
The acquistion is not necessarily a purchase, it could be a gift, an inheritance or any other method of gaining the right of ownership of an object.

The model encodes this information with an `Acquisition` part of the overall Provenance Event. The acquisition is the transfer of the right of ownership of an object (referenced in `transferred_title_of`) from the seller (in `transferred_title_from`) to the buyer (in `transferred_title_to`). 

Each object has its own Acquisition as part of the provenance event, so if a collector buys three paintings from a dealer, then there would be a single Provenance Event with three Acquisitions, all of which transfer the title of a single painting from the dealer to the collector.

```crom
top = vocab.ProvenanceEntry(label="Purchase of Sculpture")
buyer = Person(label="Buyer")
seller = Person(label="Seller")
acq = Acquisition(label="Acquisition of Sculpture from Seller")
top.part = acq
what = Sculpture(label="Sculpture", art=1)
acq.transferred_title_of = what
acq.transferred_title_from = seller
acq.transferred_title_to = buyer
```

### Multiple Owners

In the simple case of multiple simultaneous owners where either the division of the ownership is unknown or an even split, all of the owners can simply be listed with `transferred_title_from` (when the group is selling) or `transferred_title_to` (when the group is buying).  

If there is additional information known about the exact nature of the ownership division, then it is worth considering the more complex and more expressive section on [rights](rights.html) to describe this in more detail.

If there are multiple parties that have formally entered into a legal consortium or organization, and that consortium is the legal owner of the object, then the consortium should be modeled as a [`Group`](/model/actor/) with the parties as members, and be the sole owner of the object.

```crom
top = vocab.ProvenanceEntry(label="Purchase of Sculpture")
buyer = Person(label="Buyer")
buyer2 = Person(label="Buyer 2")
seller = Person(label="Seller")
acq = Acquisition(label="Acquisition of Sculpture from Seller by two Buyers")
top.part = acq
what = Sculpture(label="Sculpture", art=1)
acq.transferred_title_of = what
acq.transferred_title_from = seller
acq.transferred_title_to = buyer
acq.transferred_title_to = buyer2
```

### Agents

In some cases, it is known that an agent other than the buyer carried out the acquisition. This can be modeled by associating a different actor from the buyer (the person who title is transferred to) carrying out the activity. 

```crom
top = vocab.ProvenanceEntry(label="Purchase of Sculpture")
buyer = Person(label="Buyer")
seller = Person(label="Seller")
agent = Person(label="Agent for the Buyer")
acq = Acquisition(label="Acquisition of Sculpture from Seller")
top.part = acq
what = Sculpture(label="Sculpture", art=1)
acq.transferred_title_of = what
acq.transferred_title_from = seller
acq.transferred_title_to = buyer
acq.carried_out_by = agent
```

### Exchange of Objects

This pattern allows for the exchange of objects between two parties by simply adding a second Acquisition.

```crom
top = vocab.ProvenanceEntry(label="Exchange of Sculpture for Painting")
buyer = Person(label="Buyer")
seller = Person(label="Seller")
acq = Acquisition(label="Acquisition of Sculpture from Seller")
top.part = acq
what = Sculpture(label="Sculpture", art=1)
acq.transferred_title_of = what
acq.transferred_title_from = seller
acq.transferred_title_to = buyer
acq2 = Acquisition(label="Acquisition of Painting from Buyer")
top.part = acq2
what = Painting(label="Painting", art=1)
acq.transferred_title_of = what
acq.transferred_title_from = buyer
acq.transferred_title_to = seller
```


## Payments

A purchase is a common type of acquisition in which money is exchanged for the object.  The provenance event consists of the acquisition along with one or more related payments.  This typically involves a payment from the seller to the buyer for the agreed upon price, but might include further payments to or from others such as for shared ownership, payment of debts owed, or for services rendered as part of the overall activity.


The `Payment` activity has equivalent relationships for the actor that the money is transferred from (`paid_from`), the actor the money is transferred to (`paid_to`), and the amount of money paid (`paid_amount`).  The amount itself is a `MonetaryAmount` that has a value (`value`) and a currency (`currency`).  Each separable monetary amount is modeled as an individual instance of `Payment`, and thus if the buyer paid a commission to the agent who carried out the purchase, and paid for the object, then there would be two Payments, one from the buyer to the seller and one from the buyer to the agent. Commissions to auction houses or for consignments would use the same pattern.

!!! note "Diachronic Comparison of Monetary Amounts"
    The CIDOC-CRM SIG have clarified that the `MonetaryAmount` refers to the face value of the combination of value and currency. This means that any comparison between `MonetaryAmount` instances should also take into account the datetimes of resources that reference it, rather than standing alone. Further, it is still unclear if the same `MonetaryAmount` can be used for all occurences of value and currency, or whether there is something more unique than that.

```crom
top = vocab.ProvenanceEntry(label="Purchase of Sculpture")
seller = Actor(label="Seller")
buyer = Actor(label="Buyer")
paymt = Payment()
paymt.paid_from = buyer
paymt.paid_to = seller
amt = MonetaryAmount()
amt.value = 1000
amt.currency = vocab.instances['us dollars']
paymt.paid_amount = amt
top.part = paymt
```
 
### Payment for Services

Beyond simply paying the previous owner for the object, there are many other reasons why money might change hands that are relevant to describe for art history.

For example, it might be known how much commission went to an auction house or for the sale of objects by consignment, particularly if this comes from the stock books or records of the company. Artists might be paid a commission in advance for the production of an object, or agents might be paid a commission for finding and purchasing objects on behalf of the new owner.

__Example:__

The above payment might actually have been 900 dollars to the previous owner and 100 dollars to the auction house for its cut.

```crom
top = vocab.ProvenanceEntry(label="Purchase of Sculpture with Commission")
seller = Actor(label="Seller")
buyer = Actor(label="Buyer")
house = vocab.AuctionHouseOrg(label="Auction House")
pay1 = Payment()
pay1.paid_from = buyer
pay1.paid_to = seller
amt1 = MonetaryAmount()
amt1.value = 900
amt1.currency = vocab.instances['us dollars']
pay1.paid_amount = amt1
top.part = pay1
pay2 = vocab.CommissionPayment()
pay2.paid_from = buyer
pay2.paid_to = house
amt2 = MonetaryAmount()
amt2.value = 100
amt2.currency = vocab.instances['us dollars']
pay2.paid_amount = amt2
top.part = pay2
```

