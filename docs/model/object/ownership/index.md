---
title: "Objects: Provenance"
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

Tracking the provenance of an object is described in detail in the [Provenance](/model/provenance) section of the model. This section describes how to link the object's description into those events and entities.

## Ownership

The current owner of the object should be referenced with `transferred_title_to` in the most recent `Acquisition` that `transferred_title_of` the object. These transfers are described in detail in the [Acquistion](/model/provenance/acquisition) section.

To make the current owner easier to find from the object's description, the owner should also be referenced with `current_owner` from the object itself. There are further modeling details available about [People and Organizations](/model/actor) that might own objects.

__Example:__

The current owner of Spring is the Getty.

```crom
top = model.HumanMadeObject(ident="spring/6", label="Jeanne (Spring) by Manet")
top.current_owner = model.Group(ident="https://vocab.getty.edu/ulan/500115988", label="Getty Museum")
```

## Custody

Similarly, the current custodian of the object should be referenced with the `transferred_custody_to` in the most recent `TransferOfCustody`, in the same way as the current owner is referenced from the most recent `Acquisition`. There is an equivalent property to `current_owner` for custody, which is `current_custodian`.  This is described in more detail in the section on [custody](/model/provenance/custody).

If there is a department or person that is not the owner but is responsible for the object, then that actor is the `current_custodian`. Similarly, loans between organizations (either temporary or permanent) transfer custody rather than ownership.

__Example:__

The Night Watch is owned by the City of Amsterdam, and on permanent loan to the Rijksmuseum.

```crom
top = vocab.Painting(ident="nightwatch/1",label="Painting", art=1)
top.current_owner = model.Group(ident="amsterdam_govt", label="City of Amsterdam Governing Body")
top.current_custodian = model.Group(ident="http://vocab.getty.edu/ulan/500246547", label="Rijksmuseum")
```

## Location

The current location of the object is given using the `current_location` property.  This can give a reference to a gallery or specific part of a facility, or be used for the general address of the organization where the object is currently held. There are further modeling details available about [Places](/model/place/).


__Example:__

The current location of the Spring is Gallery W204 (which is part of the West building, which is part of the Getty Center)

```crom
top = model.HumanMadeObject(ident="spring/7", label="Jeanne (Spring) by Manet")
top.current_location = model.Place(ident="W204", label="Gallery W204")
```
