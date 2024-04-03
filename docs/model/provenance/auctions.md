---
title: Auctions
up_href: "/model/provenance/"
up_label: "Provenance"
---

[TOC]

## Introduction

Auctions are a very common way for art objects to change ownership.  The description of the auction itself is valuable for historical context and to provide a sense of the changing value of the object. An auction is, generally speaking, any event in which there are one or more attemps to sell one or more objects, where the price is negotiated by a bidding process of would-be buyers offering progressively more money for the set of objects.

There are various regional and temporal variations on auctions, some of which are covered below, however the overall pattern remains the same.

There are established vocabulary entries for the different aspects of an auction:

* __Auction Activity:__ (_aat:300054751_) The overall auction, that might consist of multiple auction of lots.
* __Auction of Lot Activity:__ (_aat:300420001_) The auctioning of a single lot.
* __Auction House Organization:__ (_aat:300417515_) The organization that is responsible for the Auction.
* __Auction House Premises:__ (_aat:300005234_) The premises of the organization, often also called an Auction House.
* __Auction Lot:__ (_aat:300411307_) The set of objects being auctioned in an Auction of Lot.
* __Lot Number:__ (_aat:300404628_) The identifier assigned as the number of the Lot in the Auction.
* __Auction Catalog:__ (_aat:300026068_) A document typically produced by the Auction House Organization enumerating the objects in each lot as an advertisement for the event


## Auction

The auction is the overall event, and a typical auction has the features described here. The auction might occur over multiple days, during which many auction of lots (the sale of one or more objects) will take place. It is performed by an organization, known as an auction house, and for movable art objects takes place at the premises of the organization. The auction of lot is each a separate sale, described in the following section.

The auction is modeled as an `Activity`, and represents the overall event. It is `carried_out_by` the auction house (a `Group`), `took_place_at` the auction house premises (a `Place`), and has all of the regular properties of an `Activity`.
It is referenced by the auction of lot activities via their `part_of` property.

__Example:__

An auction event takes place on November 5th, 2014 at the New York premises of Christie's.

<!-- 
https://www.christies.com/en/auction/impressionist-modern-evening-sale-24477/
-->

```crom
top = vocab.AuctionEvent(ident="christies_24477/1", label="Impressionist Sale")
top.identified_by = vocab.PrimaryName(content="Impressionist & Modern Evening Sale")
top.took_place_at = vocab.AuctionHouse(ident="christies_nyc", label="Christie's, New York")
top.carried_out_by = vocab.AuctionHouseOrg(ident="christies", label="Christie's")
t = model.TimeSpan(label="Nov 5, 2014")
t.begin_of_the_begin = "2014-11-05T17:00:00Z"
t.end_of_the_end = "2014-11-05T23:59:59Z"
top.timespan = t
```

## Auction of Lot

The auction of a lot is an activity with an aim of obtaining the highest price for object or objects available in that lot. It is normally carried out by an auctioneer employed by the auction house organization. The price increases as people make bids, and the highest bidder is the winner of the auction. The details of the individual bids are not normally known, however whether there were bids but no sale is sometimes available. The auction of lot then causes the Provenance activity that describes the purchase, with the transfer of ownership, custody and payments.

The model uses an `Activity` for the auction of lot, which is `part_of` the Auction event.  It uses a `Set` of objects to link the objects for sale to the activity via the `used_specific_object` property. Any bidding information is `part` of the the Auction of Lot, and if the reserve price is met, then a provenance entry representing the purchase of the objects is `caused` by the Auction of Lot. It can also have all of the regular activity properties to refer to time and place.

__Example:__

Lot 16 was auctioned as part of the auction above.

```crom
top = vocab.Auction(ident="christies_24477_16/1", label="Auction of Lot 16")
top.identified_by = vocab.PrimaryName(content="Auction of Lot 16")
top.used_specific_object = model.Set(ident="24477_16_objects", label="Lot 16")
top.part_of = vocab.Activity(ident="christies_24477")
```

## Set of Objects 

The Lot is a set of objects grouped together for the purposes of the sale, and may potentially have come from different owners.  It is frequently assigned an identifying Lot Number by the auction house, and may have a title, description or other properties such as specific price information, discussed in more detail below.  The set has members which are the objects for sale. As with all other Sets, the membership information is given on the object using the `member_of` property, rather than on the Set directly.

__Example:__

Lot 16 consists of a single painting, Spring.

```crom
top = vocab.AuctionLotSet(ident="24477_16_objects/1", label="Set of Objects for Lot 16")
top.identified_by = vocab.PrimaryName(content="Lot 16: Le Printemps")
top.identified_by = vocab.LotNumber(content="16")
```

```crom
top = vocab.Painting(ident="spring/20", label="Spring")
top.identified_by = vocab.PrimaryName(content="Jeanne (Spring)")
top.member_of = model.Set(ident="24477_16_objects", label="Lot 16: Le Printemps")
```

### Pre-set Prices

In auctions, there are several types of monetary values that are useful and interesting to record.  There is a significant distinction between the starting price or reserve price for an auction and the regular purchase price of an object, in that even if the auction never takes place, these other prices are still known as they are set in advance.

There are three pre-set prices of interest:

  * __Starting Price:__  (_aat:300417242_) The price at which the auction will start.
  * __Reserve Price:__  (_aat:300417243_) The price that must be exceeded for the auction to result in a sale.
  * __Estimated Price:__  (_aat:300417244_) The price that the auction house estimates will be the final sale price.

These prices are associated with the Set of Objects that the Auction of Lot is intended to sell.  In this way, even if the auction never takes place, there is still the set of objects to associate the prices with.  In order to associate a monetary value with an object, it is treated as an observed dimension.

__Example:__

Lot 16 had an estimated price of $25,000,000:

```crom
top = vocab.AuctionLotSet(ident="24477_16_objects/2", label = "Set of Objects for Lot 16")
amnt = vocab.EstimatedPrice(value=25000000)
amnt.currency = vocab.instances['us dollars']
top.dimension = amnt
```

## Purchase of Lot 

The purchase of the lot is very similar to the purchase of any other object, however there is an explicit reference to the set of objects. The set is only a temporary grouping, put together only for the purpose of this particular auction and is not something which can be owned directly.  As such, each object has its own acquisition as part of the provenance event or its own record. Conversely, there is only a single payment for the entire lot.

__Example:__

The Getty acquired Lot 16 for $65,125,000.

```crom
top = vocab.ProvenanceEntry(ident="payneheirs_getty/2", label="Purchase of Lot 16")
top.used_specific_object = model.Set(label="Set of Objects for Lot 812")
top.part_of = model.Activity(ident="christies_24477_16", label="Auction of Lot 16")

seller = model.Group(ident="payne_heirs", label="Family of Oliver Payne")
buyer = model.Group(ident="getty", label="J. Paul Getty Museum")

acq = model.Acquisition(label="Acquisition of Spring")
top.part = acq
acq.transferred_title_of = model.HumanMadeObject(ident="spring", label="Spring")
acq.transferred_title_from = seller
acq.transferred_title_to = buyer
acq.carried_out_by = model.Person(ident="naumann", label="Otto Naumann")

pay = model.Payment(label="Payment for Lot 16")
ma = model.MonetaryAmount(value=65125000)
ma.currency = vocab.instances['us dollars']
pay.paid_amount = ma
pay.paid_from = buyer
pay.paid_to = seller
top.part = pay
```

<!--

Too Complex, Not Enough Data

### Known Bid Amounts

Sometimes we also know the monetary amounts that were unsuccessfully bid for the object, regardless of whether the auction eventually ended in a sale or not.  These bids are part of the overall bidding activity.

Bids are modeled as the creation of a proposition that the bidder (or the person that an agent is bidding on behalf of) will pay a certain amount of money for the object. In the example below, a known bid is $10,000 but it is not stated whether there was a sale concluded.

```crom
top = vocab.Auction(ident="auto int-per-segment", label="Auction of Lot J-1823-5")
bidset = model.Activity(label="Bids on Lot J-1823-5")
top.part = bidset
bid = vocab.Bidding(label="Bid of 10000 dollars")
bidset.part = bid
who = model.Person(label="Example Bidder")
bid.carried_out_by = who
bidprop = model.PropositionalObject()
bid.created = bidprop
amnt = model.MonetaryAmount()
amnt.value = 10000
amnt.currency = vocab.instances["us dollars"]
bidprop.refers_to = amnt
```

-->

## Auction Catalog

Much of the information we have about historical auctions comes from Auction Catalogs.  These documents thus provide the primary source of evidence, and can be linked to the descriptions of the activities.  These follow the same model as other [documents](/model/document/).

```crom
top = vocab.AuctionCatalogText(ident="catalog_24477", label="Auction Catalog")
top.identified_by = vocab.PrimaryName(content="Impressionist & Modern Evening Sale Catalog")
top.about = model.Activity(ident="christies_24477", label="Impressionist Sale")
```


## Other Results

Not every auction of lot results in a purchase, and not every lot that is advertised in an auction catalog is actually presented for sale. Objects can be withdrawn, reserve prices might not be met, the winner might not be able to pay, or the owner might bid on their own objects to determine or drive up their value. These scenarios are discussed in this section as to how they can be described using the model.

### Lot Withdrawn

It is possible that an auction lot is withdrawn from the auction before the auction of lot occurs. The auction catalog will record the objects in the lot, and is valuable for the historical record to know that they were offered for sale and then withdrawn. 

In this case, there should be a catalog entry and the auction lot set that the entry describes, but no corresponding auction of lot activity, as it did not take place. The date can be calculated from the dates of the auction event, to position the objects in time.  In some cases, where the auctioned objects are all from a single person or organization, this would also establish evidence of ownership at that time.

### Object Withdrawn from Lot

It can also be that a single object is withdrawn from a Lot with multiple objects, which is otherwise sold. In this case, the withdrawn object is returned to the owner as part of the provenance event that is caused by the auction of the lot which still takes place. That return has a specific purpose that can distinguish withdrawn objects from objects that are returned for other reasons below.

### Reserve Not Met

Another scenario is when the auction of lot does take place, but there is no purchase because a reserve price was not met.  This is often referred to as being "Bought In", or sometimes "Passed".

In this case the auction of lot activity does occur, but there may or may not have been any bidding. It does result in a provenance entry, as for the auction house organization to be able to auction it, they must have had some degree of custody of the object.  There may also be a commission paid from the owner to the auction house for running the auction, even though it was ultimately unsuccessful.  The return of the object to the owner would be a Transfer of Custody in the same way as returning a painting to the owner after an exhibition.

### Bought by Owner

In some cases the owner of the object actively bids on their own items, either directly or via an agent, and ends up bidding the highest amount, and thereby winning the lot. This is different to the bought in case, as in that case the reserve was not met, and in this case it was. This was sometimes done intentionally to determine what the market would bear for an object, or to drive up the price of related objects by providing a precedent.

As the owner cannot sell the object to themselves, this does not result in a __change__ of ownership. In the same way as when the reserve is not met, there is a change of custody from the owner to the auction house and back again, and might involve paying commission to the auction house for the "sale". Conversely, in this case we do know that there was bidding as there was a "sale", even if there was not a transfer of ownership.  

### Winner Unable to Pay

And in other cases, someone successfully wins the auction other than the owner, but is unable to pay.  In this case there was a bid, the promise to pay a given amount, but no subsequent fulfillment of the promise with a payment. Again, this results in the transfer of custody of the object from the auction house back to the owner. The bid amount can be recorded as described in the bidding section.

It is not often to know that this has occured, unless the information is coming either directly from the auction house or from the owner.  This might happen when an art dealer auctions an object, and then records the return of the object in their stock management system.



