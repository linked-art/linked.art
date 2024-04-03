---
title: "Objects: Rights Information"
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

The rights information about both the physical objects and their digital representations is important to capture.  For general, textual statements about rights information the model uses the LinguisticObject pattern that should now be familiar.  For more specific rights that can be identified individually, such as copyright, and optionally who holds those rights, there is the ability to assert them in a machine readable way.

## Credit / Attribution Statement

It is important to be able to give a credit or attribution statement that should be displayed along with the object. For example, a painting that has been donated might have the requirement to state who the donor was. This is modeled using the statement pattern as a `LinguisticObject`, that is `classified_as` _aat:300026687_ - the term for "acknowledgements". The text is given in the `content` property.

__Example:__

The Night Watch is on loan to the Rijksmuseum from the City of Amsterdam.

```crom
top = vocab.Painting(ident="nightwatch/15", label="Night Watch by Rembrandt")
top.referred_to_by = vocab.CreditStatement(content="On loan from the City of Amsterdam")
```

## Rights Statement

For general statements about rights or licenses, the information can be provided in the same way as for a credit or attribution.  The difference is that it is `classified_as` _aat:300435434_ - the term for license or legal statements.
Such rights statements might be associated with the physical object or with the visual work, but likely should be associated with the work (the image that has or had copyright, rather than the bits of matter that carry it).


__Example:__

The visual content of the Night Watch is in the Public Domain.

```crom
top = model.VisualItem(ident="nightwatch/1", label="Visual Content of Night Watch")
top.referred_to_by = vocab.RightsStatement(content="Public Domain")
```

## Rights Assertions

More detailed information is, however, often available and it is useful to be explicit. These patterns associate a `Right` that the object is `subject_to`, and then give more detail about the nature of that right, such as what sort of right, and who holds it.

### RightsStatements.org Assertions

There is a recent effort to standardize rights statements, described at [rightsstatements.org](http://rightsstatements.org/).  Twelve basic rights statements were identified and given URIs to identify them.  If any of these statements apply, it is useful to use these URIs to ensure that client systems can process them the in the same way. These assertions are modeled as individual Rights, which are then `classified_as` the Rights Statement URI or a Creative Commons URI.

These rights must be associated with the Work, rather than the Object, if they are about the copyright or other use of the image rather than the physical object. Asserting that you can reuse "The Night Watch" does not give you any physical rights over the object in the Rijksmuseum, it gives you usage rights over the visual content.

__Example:__

The visual content of the Night Watch is in the Public Domain.

```crom
top = model.VisualItem(ident="nightwatch/2", label="Visual Content of Night Watch")
r = model.Right(label="Night Watch's Public Domain status")
t = model.Type(ident="https://creativecommons.org/publicdomain/zero/1.0/", label="Public Domain")
r.identified_by = model.Name(content="Public Domain")
r.classified_as = t
top.subject_to = r
```
