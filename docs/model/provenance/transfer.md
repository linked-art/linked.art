---
title: Unknown Transfers
up_href: "/model/provenance/"
up_label: "Provenance"
---

[TOC]

## Introduction

Especially when working from incomplete documentary evidence, it is frequently difficult to determine exactly what sort of exchange took place in the past. The object might have been sold or otherwise changed ownership, or it might have been only on loan. While this could theoretically be handled by a transfer of an indeterminate [property right](rights), this would be very complex and give the impression of more information being available than is actually the case. Instead, we add a new class called `Transfer` which allows the indeterminate transfer of an object between two parties without claiming whether it is ownership, custody or something else entirely.


## Transfer

The class for indeterminate transfers is `Transfer`, and has three properties beyond the core activity properties:

* **transferred**: references the object or objects being transferred
* **transferred_from**: references the people or groups from whom the object(s) are being transferred
* **transferred_to**: references the people or groups to which the object(s) are being transferred

This mirrors the other classes such as `Acquisition`, `TransferOfCustody`, and `Move`.


__Example:__

A painting is transferred between two people, however it is not clear whether it was permanent or merely a loan.

```crom
top = vocab.ProvenanceEntry(ident="transfer/1", label="Transfer of Painting")
xfer = model.Transfer()
xfer.transferred = model.HumanMadeObject(ident="example", label="Example Painting")
xfer.transferred_from = model.Person(ident="person1", label="Person 1")
xfer.transferred_to = model.Person(ident="person2", label="Person 2")
top.part = xfer
```
