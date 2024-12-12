---
title: Object Acquisition and Loan
up_href: "/model/provenance/"
up_label: "Provenance"
---



## Introduction

The majority of recorded provenance events are when the object changes ownership, and the various methods in which that happens.  In the descriptions below the terms 'seller' and 'buyer' are used to refer to the actor that is relinquishing ownership and the actor that is gaining ownership, even if there is no money or other goods or services changing hands. This is for clarity and conciseness of the descriptions, and not to imply that every transaction is a purchase.

## Object Acquisition

Acquisitions are used to describe the transfer of ownership of an object from one owner to the next. The first owner is typically the artist, who would then transfer it to the second owner, to the third owner and so on. The ownership chain can be expressed by repeating this same pattern with the buyer from one acquisition being the seller in the subsequent one.  If the previous owner (e.g. the seller) or the subsequent owner (e.g. the buyer) is not known for a particular acquisition, then the reference can be left out from the description.
  
The acquistion is not necessarily a purchase, it could be a gift, an inheritance or any other method of gaining the right of ownership of an object.

The model encodes this information with an `Acquisition` part of the overall Provenance Event. The acquisition is the transfer of the right of ownership of an object (referenced in `transferred_title_of`) from the seller (in `transferred_title_from`) to the buyer (in `transferred_title_to`). 

Each object has its own Acquisition as part of the provenance event, so if a collector buys three paintings from a dealer, then there would be a single Provenance Event with three Acquisitions, all of which transfer the title of a single painting from the dealer to the collector.


__Example:__

Oliver Payne acquired Spring from the Durand-Ruel Gallery in New York in 1909

```crom
top = vocab.ProvenanceEntry(ident="durand_payne/1", label="Purchase of Spring by Payne")
top.identified_by = vocab.PrimaryName(content="Purchase of Spring by Payne from Durand-Ruel")

ts = model.TimeSpan()
ts.begin_of_the_begin = "1909-01-01T00:00:00Z"
ts.end_of_the_end = "1909-12-31T23:59:59Z"
top.timespan = ts

acq = model.Acquisition(label="Ownership of Spring to Payne")
top.part = acq
acq.transferred_title_of = model.HumanMadeObject(ident="spring", label="Spring")
acq.transferred_title_from = model.Person(ident="durand", label="Durand-Ruel Gallery")
acq.transferred_title_to = model.Person(ident="payne", label="Oliver Payne")
```

### Multiple Owners

In the simple case of multiple simultaneous owners where either the division of the ownership is unknown or an even split, all of the owners can simply be listed with `transferred_title_from` (when the group is selling) or `transferred_title_to` (when the group is buying).  

If there is additional information known about the exact nature of the ownership division, then it is worth considering the more complex and more expressive section on [rights](../rights) to describe this in more detail.

If there are multiple parties that have formally entered into a legal consortium or organization, and that consortium is the legal owner of the object, then the consortium should be modeled as a [`Group`](/model/actor/) with the parties as members, and be the sole owner of the object.

__Example:__

The Yale University Art Gallery and the Yale Center for British Art jointly purchased a painting by Kehinde Wiley in 2021 from an undisclosed seller.

```crom
top = vocab.ProvenanceEntry(ident="yuag_ycba_wiley/1", label="Purchase of Painting")
ts = model.TimeSpan()
ts.begin_of_the_begin = "2021-01-01T00:00:00Z"
ts.end_of_the_end = "2021-12-31T23:59:59Z"
top.timespan = ts
acq = model.Acquisition()
top.part = acq
acq.transferred_title_of = model.HumanMadeObject(ident="yiadom-boakye", label="Portrait of Lynette Yiadom-Boakye")
acq.transferred_title_to = model.Group(ident="yuag", label="Yale University Art Gallery")
acq.transferred_title_to = model.Group(ident="ycba", label="Yale Center for British Art")
```

### Agents

In some cases, it is known that an agent other than the buyer facilitated or carried out the acquisitionon the buyer's behalf. This can be modeled by associating a different person or group with the activity using `carried_out_by` as the relationship. Multiple agents can be listed in this way, but it is not possible to associate agents with the person or group they're working for -- the model does not have a notion of seller's agent as distinct from buyer's agent.

__Example:__

In 2014, the family heirs of Oliver Payne sold Spring (by auction at Christie's) to Otto Naumann, acting for the J. Paul Getty Museum.

```crom
top = vocab.ProvenanceEntry(ident="payneheirs_getty/1", label="Purchase of Spring for Getty")
ts = model.TimeSpan()
ts.begin_of_the_begin = "2014-11-05T00:00:00Z"
ts.end_of_the_end = "2014-11-05T23:59:59Z"
acq = model.Acquisition(label="Acquisition of Spring")
top.part = acq
acq.transferred_title_of = model.HumanMadeObject(ident="spring", label="Spring")
acq.transferred_title_from = model.Group(ident="payne_heirs", label="Family of Oliver Payne")
acq.transferred_title_to = model.Group(ident="getty", label="J. Paul Getty Museum")
acq.carried_out_by = model.Person(ident="naumann", label="Otto Naumann")
```

### Exchange of Objects

This pattern allows for the exchange of objects between two parties by simply adding a second Acquisition with buyer and seller reversed.

__Example:__

In 1962, the Yale University Art Gallery exchanged "Nude Woman" by Beckmann for "Personnages dans un parc" by Masson.

```crom
top = vocab.ProvenanceEntry(ident="yuag_stora/1", label="Exchange of Objects")
yuag = model.Group(ident="yuag", label="Yale University Art Gallery")
feigen = model.Group(ident="feigen", label="Richard Feigen Gallery")
acq = model.Acquisition(label="Acquisition of Personnages")
top.part = acq
acq.transferred_title_of = model.HumanMadeObject(ident="masson_personnages", label="Personnages dans un parc")
acq.transferred_title_from = feigen
acq.transferred_title_to = yuag
acq2 = model.Acquisition(label="Acquisition of Nude")
top.part = acq2
acq.transferred_title_of = model.HumanMadeObject(ident="beckmann_nude", label="Nude Woman by Beckmann")
acq.transferred_title_from = yuag
acq.transferred_title_to = feigen
```


## Payments

A purchase is a common type of acquisition in which money is exchanged for the object.  The provenance event consists of the acquisition along with one or more related payments.  This typically involves a payment from the seller to the buyer for the agreed upon price, but might include further payments to or from others such as for shared ownership, payment of debts owed, or for services rendered as part of the overall activity.

The `Payment` activity has equivalent relationships for the actor that the money is transferred from (`paid_from`), the actor the money is transferred to (`paid_to`), and the amount of money paid (`paid_amount`).  The amount itself is a `MonetaryAmount` that has a value (`value`) and a currency (`currency`).  Each separable monetary amount is modeled as an individual instance of `Payment`, and thus if the buyer paid a commission to the agent who carried out the purchase, and paid for the object, then there would be two Payments, one from the buyer to the seller and one from the buyer to the agent. Commissions to auction houses or for consignments would use the same pattern.

!!! note "Diachronic Comparison of Monetary Amounts"
    The underlying ontology has specified that the `MonetaryAmount` refers to the face value of the combination of value and currency. This means that any comparison between `MonetaryAmount` instances should also take into account the datetimes of resources that reference it, rather than standing alone. It is unclear if the same `MonetaryAmount` can be used for all occurences of value and currency, or whether it is something more unique than that, and to be safe the model assumes that one instance will only be used in a single `Payment`.

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
 
### Payment for Services

Beyond simply paying the previous owner for the object, there are many other reasons why money might change hands that are relevant to describe. For example, it might be known how much commission went to an auction house or for the sale of objects by consignment, particularly if this comes from the stock books or records of the company. Artists might be paid a commission in advance for the production of an object, or agents might be paid a commission for finding and purchasing objects on behalf of the new owner. This is often not recorded in detail, however the pattern is provided for situations when it is known.

__Example:__

A sculpture is purchased with $900 going to the seller, and $100 going to the auction house.

```crom
top = vocab.ProvenanceEntry(ident="fixme/1", label="Purchase of Sculpture with Commission")
seller = model.Person(label="Seller")
buyer = model.Person(label="Buyer")
house = vocab.AuctionHouseOrg(label="Auction House")
pay1 = model.Payment()
pay1.paid_from = buyer
pay1.paid_to = seller
amt1 = model.MonetaryAmount()
amt1.value = 900
amt1.currency = vocab.instances['us dollars']
pay1.paid_amount = amt1
top.part = pay1
pay2 = vocab.CommissionPayment()
pay2.paid_from = buyer
pay2.paid_to = house
amt2 = model.MonetaryAmount()
amt2.value = 100
amt2.currency = vocab.instances['us dollars']
pay2.paid_amount = amt2
top.part = pay2
```

