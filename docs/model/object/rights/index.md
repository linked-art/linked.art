---
title: "Objects: Rights Information"
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

The rights information about both the physical objects and their digital representations is important to capture.  For general, textual statements about rights information the model uses the LinguisticObject pattern that should be familiar.  For more specific rights that can be identified individually, such as copyright, and optionally who holds those rights, there is the ability to assert them in a machine readable way.

## Credit / Attribution Statement

It is important to be able to give a credit or attribution statement that should be displayed along with the object. For example, a painting that has been donated might have the requirement to state who the donor was. This is modeled using the statement pattern as a `LinguisticObject`, that is `classified_as` _aat:300026687_ - the term for "acknowledgements". The text is given in the `content` property.

__Example:__

The painting was a donation of a Ms J. Smith.

```crom
top = Painting(art=1)
top._label = "Example Painting"
crdt = CreditStatement()
crdt.content = "Donation of Ms J. Smith; Example Organization"
top.referred_to_by = crdt
```

## Rights Statement

For general statements about rights that have not been aligned with any other controlled vocabularies such as [rightsstatements.org](http://rightsstatements.org/), the information can be provided in the same way as for a credit or attribution.  The difference is that it is `classified_as` _aat:300435434_ - the term for license or legal statements.

__Example:__

An assertion that the copyright status of an object has not been assessed, and is thus unknown.

```crom
top = Painting(art=1)
top._label = "Example Painting"
crdt = RightsStatement()
crdt.content = "Copyright of this object has not yet been assessed"
top.referred_to_by = crdt
```

## Rights Assertions

More detailed information is, however, often available and it is useful to be explicit. These patterns associate a `Right` that the object is `subject_to`, and then give more detail about the nature of that right, such as what sort of right, and who holds it.

### RightsStatements.org Assertions

There is a recent effort to standardize rights statements, described at [rightsstatements.org](http://rightsstatements.org/).  Twelve basic rights statements were identified and given URIs to identify them.  If any of these statements apply, it is useful to use these URIs to ensure that client systems can process them the in the same way.

These assertions are modeled as individual Rights, which are then `classified_as` the rights statement URI. A label, via`_label`, can also be given to provide clarity for developers looking at the data in the same way as `Type` objects.

__Example:__

The painting has no known copyright.

```crom
top = Painting(art=1)
top._label = "Painting"
r = model.Right()
t = model.Type(ident="http://rightsstatements.org/vocab/NKC/1.0/")
t._label = "No known copyright"
r.classified_as = t
top.subject_to = r
```
