---
title: "Objects: Provenance"
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

Tracking the provenance of an object is described in detail in the [Provenance](/model/provenance) section of the model. This section describes how to link the object's description into those events and entities.

## Ownership

The current owner of the object should be referenced with `transferred_title_to` in the most recent `Acquisition` that `transferred_title_of` the object. These transfers are described in detail in the [Acquistion](/model/provenance/acquisition.html) section.

To make the current owner easier to find from the object's description, the owner should also be referenced with `current_owner` from the object itself. There are further modeling details available about [People and Orgaizations](/model/actor) that might own objects.

__Example:__

The current owner of the painting is a Museum.

```crom
top = Painting(label="Painting", art=1)
top.current_owner = vocab.MuseumOrg(label="Museum")
```

## Custody

Similarly, the current custodian of the object should be referenced with the `transferred_custody_to` in the most recent `TransferOfCustody`, in the same way as the current owner is referenced from the most recent `Acquisition`. There is an equivalent property to `current_owner` for custody, which is `current_custodian`.  This is described in more detail in the section on [custody](/model/provenance/custody.html).

Note that objects are owned by legal entities, such as people or organizations. If there is a department or person that is not the owner but is responsible for the object, then that actor is the `current_custodian`.

```crom
top = Painting(label="Painting", art=1)
top.current_owner = vocab.MuseumOrg(label="Museum")
top.current_custodian = vocab.Department(label="Paintings Department")
```

## Location

The current location of the object is given using the `current_location` property.  This can give a reference to a gallery or specific part of a facility, or be used for the general address of the organization where the object is currently held. There are further modeling details available about [Places](/model/place/).


__Example:__

The current location of the painting is Gallery W6.

```crom
top = Painting(art=1)
top._label = "Painting"
where = Place()
where._label = "Gallery W6"
top.current_location = where
```
