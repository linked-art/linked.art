---
title: Loans, Thefts, Losses and other Changes of Custody
up_href: "/model/provenance/"
up_label: "Provenance"
---

[TOC]

## Introduction

When there is a change of who has physical possession of an object, but not who the legal owner of it is, that constitutes a change of custody rather than a change of ownership.  This pattern includes use cases such as lending an object to another party for some amount of time, the theft of an object (as the legal owner does not change), and losing track of the location of an object. 


## Loans

The model makes a distinction between the [transfer of legal ownership](acquisition.html) and the transfer of custody of an object (e.g. by losing the object or loaning it out for an exhibition). If the possession of the object is temporary, such that the object would be given back to the real owner at the end of that possession without what might be considered a sale or exchange, then it is a transfer of custody.  Note that the provenance activity here does not represent the entire duration of the change in custody, only the transfer of it.  Just like acquisitions, there would be a second provenance activity that would transfer the custody back to the original custodian or on to some other party.

Long term loans or even "permanent" loans are just open ended pairs of activities -- the object has had its custody transferred, and the object has not been returned yet.

In the model, these transfers of custody use a different class, `TransferOfCustody` instead of `Acquisition`. The properties that capture the parties and object involved are also different, although equivalent, to those of `Acquisition`: `transferred_custody_of` the object, `transferred_custody_from` the previous custodian, and `transferred_custody_to` the new custodian.

__Example:__

A sculpture is lent from one person to another, and then later returned.

```crom
top = vocab.ProvenanceEntry(label="Lending a Sculpture to Recipient")
loan = vocab.Loan()
top.part = loan
loan.transferred_custody_of = Sculpture(label="Sculpture", art=1)
loan.transferred_custody_from = Person(label="Lender")
loan.transferred_custody_to = Person(label="Recipient")
```

Which would typically be followed by a later return with the same form:

```crom
top = vocab.ProvenanceEntry(label="Return of the Sculpture to Lender")
loan = vocab.ReturnOfLoan(label="Return")
top.part = loan
loan.transferred_custody_of = Sculpture(label="Sculpture", art=1)
loan.transferred_custody_from = Person(label="Recipient")
loan.transferred_custody_to = Person(label="Lender")
```

## Institutional Ownership, Departmental Custody

Objects are owned by legal entities, such as museum organizations or individual people. However there may be more information about which department is responsible within a museum for the curation of the object. This is the division between acquisitions (the legal ownership of the object) and custody (the responsibility for looking after the object). If the department is known, then it should be either part of the Provenance Event in which the object is acquired, or a separate provenance event if the object was not accessioned by a department and later came under their care, or was transferred between departments. In these latter cases, the ownership does not change, only the custody of the object.

The department becomes the `current_keeper` of the object, whereas the institution is the `current_owner`, as described in the [object section](/model/object/ownership/). The transfer model is otherwise identical to other transfers of custody.

__Example:__

An object is acquired by the museum and the custody of the painting is transferred to a particular department.

```crom
top = vocab.ProvenanceEntry(label="Purchase of Painting")
buyer = vocab.MuseumOrg(label="Museum")
seller = Person(label="Seller")
dept = vocab.Department(label="Paintings Department of Museum")
what = vocab.Painting(label="Painting", art=1)
acq = Acquisition(label="Acquisition of Painting")
top.part = acq
acq.transferred_title_of = what
acq.transferred_title_from = seller
acq.transferred_title_to = buyer
cust = TransferOfCustody(label="Custody by Department")
top.part = cust
cust.transferred_custody_of = what
cust.transferred_custody_from = seller
cust.transferred_custody_to = dept
```

## Loss

The loss of an object is the transfer of custody away from its current owner, without stating a recipient.  In the future, if the object is discovered, the recipient might be able to be filled in.  If the object is then returned to the owner, there would be the reverse transfer of custody from the party that found it.  It might be that the owner simply loses track of it, and although it is still in their possession, they are not aware of it ... it has no custodian, but it has not moved and the owner still owns it.


```crom
top = vocab.ProvenanceEntry(label="Loss of Painting")
xfer = vocab.Loss()
xfer.transferred_custody_of = Painting(label="Lost Painting", art=1)
xfer.transferred_custody_from = Person(label="Owner")
when = TimeSpan(label="Time noticed as Lost")
when.begin_of_the_begin = "1790-12-04T00:00:00Z"
when.end_of_the_end = "1790-12-05T00:00:00Z"
xfer.timespan = when
top.part = xfer
```

## Theft

The theft of an object is also the (illegal) transfer of custody of the object, rather than a transfer of ownership. If  the stolen object were recovered, then it would be restored to its owner. Stolen, or looted as a special case of theft, objects and their repatriation are an interesting and important part of the provenance of a work and frequently contested.

A single theft event might involve stealing multiple objects, in the same way that the purchase of an auction lot might involve the acquisition of multiple objects for a combined payment. 

```crom
top = vocab.ProvenanceEntry(label="Theft of Two Paintings")
own = Person(label="Owner")
thf = Person(label="Thief")
xfer = vocab.Theft()
xfer.transferred_custody_of = Painting(label="Stolen Painting", art=1)
xfer.transferred_custody_from = own
xfer.transferred_custody_to = thf
xfer2 = vocab.Theft()
xfer2.transferred_custody_of = Painting(label="Stolen Painting 2" , art=1)
xfer2.transferred_custody_from = own
xfer2.transferred_custody_to = thf
top.part = xfer
top.part = xfer2
```

### Sale of Stolen or Looted Objects

If a stolen object is sold, then that purchase is actually just a transfer of custody in exchange for money (or other payment). Typically, of course, the nature of that transaction is not discovered until long after the fact. This can then have many effects on the provenance record for the object as suddenly many acquisitions would be retroactively changed to being transfers of custody. This updating of the historical record is necessary without going to great lengths to model the belief that an acquisition is legal for the vast majority of cases when it is, indeed, legal in order to allow that belief to be incorrect for the few times when it is not.

```crom
top = vocab.ProvenanceEntry(label="Unknowing Purchase of Stolen Painting")
thf = Person(label="Thief")
mus = vocab.MuseumOrg(label="Museum")
what = Painting(label="Stolen Painting", art=1)
xfer = vocab.SaleOfStolenGoods(label="Obtaining Painting")
top.part = xfer
xfer.transferred_custody_of = what
xfer.transferred_custody_from = thf
xfer.transferred_custody_to = mus
pay = Payment()
pay.paid_from = mus
pay.paid_to = thf
amnt = MonetaryAmount(label="Payment to Thief")
amnt.value = 10000
amnt.currency = vocab.instances['gb pounds']
pay.paid_amount = amnt
top.part = pay
```

## Exhibitions

Exhibitions are a common way that the custody of an object changes, while the ownership remains the same.  Exhibitions are described in more detail [here](/model/exhibition/).
