---
title: "Objects: Provenance"
up_href: "/model/object/"
up_label: "Objects"
---



## Introduction

Tracking the provenance of an object is described in detail in the [Provenance](/model/provenance) section of the model. This detail might not be available for all objects, and it is beneficial to have the current ownership, custody and location of objects available in the object record directly. 

Even if there are detailed records of the ownership history for an object, these are still likely limited to the basics of who owned it, when, and how they acquired it. The acquisition is also likely for the object by itself, and what was paid or exchanged for it is very infrequently able to be published. For this 99% case, the transfers of ownership can be listed in the object record instead of in separate provenance records, but can be linked to them if they do exist. This pattern does not extend to changes of custody or location.


## Current and Normal Owners, Custodians and Locations

### Ownership

The current owner of the object should be referenced with `transferred_title_to` in the most recent `Acquisition` that `transferred_title_of` the object. These transfers are described in detail in the [Acquistion](/model/provenance/acquisition) section.

To make the current owner easier to find from the object's description, the owner should also be referenced with `current_owner` from the object itself. There are further modeling details available about [People and Organizations](/model/actor) that might own objects.

__Example:__

The current owner of Spring is the Getty.

```crom
top = model.HumanMadeObject(ident="spring/6", label="Jeanne (Spring) by Manet")
top.current_owner = model.Group(ident="http://vocab.getty.edu/ulan/500115988", label="Getty Museum")
```

### Custody

Similarly, the current custodian of the object should be referenced with the `transferred_custody_to` in the most recent `TransferOfCustody`, in the same way as the current owner is referenced from the most recent `Acquisition`. There is an equivalent property to `current_owner` for custody, which is `current_custodian`.  This is described in more detail in the section on [custody](/model/provenance/custody).

If there is a department or person that is not the owner but is responsible for the object, then that actor is the `current_custodian`. Similarly, loans between organizations (either temporary or permanent) transfer custody rather than ownership.

__Example:__

The Night Watch is owned by the City of Amsterdam, and on permanent loan to the Rijksmuseum.

```crom
top = vocab.Painting(ident="nightwatch/14",label="Painting", art=1)
top.current_owner = model.Group(ident="amsterdam_govt", label="City of Amsterdam Governing Body")
top.current_custodian = model.Group(ident="http://vocab.getty.edu/ulan/500246547", label="Rijksmuseum")
```

#### Normal Custodian

When an object is temporarily loaned to another organization, for example for an exhibition, then the current owner does not change, but the current custodian will. It is useful in this circumstance to know who the usual or normal custodian of the object is when it's different from the current custodian. For example, if (and this is a big if given the size of the painting) the Night Watch was loaned to another organization, then the owner would remain the city, the current custodian would be the exhibiting organization, and the Rijksmuseum would remain the normal custodian. This uses a property called `current_permanent_custodian`.

__Example:__

The Night Watch is also (hypothetically) loaned to the Getty Museum.

```crom
top = vocab.Painting(ident="nightwatch/17",label="Painting", art=1)
top.current_owner = model.Group(ident="amsterdam_govt", label="City of Amsterdam Governing Body")
top.current_permanent_custodian = model.Group(ident="http://vocab.getty.edu/ulan/500246547", label="Rijksmuseum")
top.current_custodian = model.Group(ident="http://vocab.getty.edu/ulan/500115988", label="Getty Museum")
```


### Location

The current location of the object is given using the `current_location` property.  This can give a reference to a gallery or specific part of a facility, or be used for the general address of the organization where the object is currently held. There are further modeling details available about [Places](/model/place/).

__Example:__

The current location of the Spring is Gallery W204 (which is part of the West building, which is part of the Getty Center)

```crom
top = model.HumanMadeObject(ident="spring/7", label="Jeanne (Spring) by Manet")
top.current_location = model.Place(ident="W204", label="Gallery W204")
```

#### Normal Location

Similar to the current versus normal custodian, objects may also have a normal location compared to their current location. The object might not be where it normally is for conservation work, because it has been moved for an exhibition, or due to gallery rotations.  The model uses the same pattern with a `current_permanent_location` property.

__Example:__

Spring is (also hypothetically) currently in a different gallery for an exhibition.

```crom
top = model.HumanMadeObject(ident="spring/14", label="Jeanne (Spring) by Manet")
top.current_permanent_location = model.Place(ident="W204", label="Gallery W204")
top.current_location = model.Place(ident="E100", label="Exhibition Gallery 100")
```


## Simple Historical Ownership

The list of owners can be provided directly within the object record using the `changed_ownership_through` property.
This conveys a list of Acquisitions (not full Provenance events) in which the ownership of the object changed. The Acquisitions should be in the order in which they should be displayed. If there are full Provenance Activity records, then these can be referenced via the `part_of` property in the Acquisition.

Otherwise, all of the regular event properties and relationships are available for use.

__Example:__

Spring was transferred from Manet to Proust, and then later from the Durand-Ruel Gallery to Payne.
(The full set of transfers would be given in the real record)

```crom
top = model.HumanMadeObject(ident="spring/15", label="Jeanne (Spring) by Manet")

acq1 = model.Acquisition(label="Ownership of Spring to Proust")
acq1.transferred_title_from = model.Person(ident="manet", label="Manet")
acq1.transferred_title_to = model.Person(ident="proust", label="Proust")
ts1 = model.TimeSpan()
ts1.begin_of_the_begin = "1881-01-01T00:00:00Z"
ts1.end_of_the_end = "1883-12-31T23:59:59Z"
acq1.timespan = ts1
acq1.part_of = model.Activity(ident="manet_proust", label="Full Provenance Activity")
top.changed_ownership_through = acq1

acq2 = model.Acquisition(label="Ownership of Spring to Payne")
acq2.transferred_title_from = model.Person(ident="durand", label="Durand-Ruel Gallery")
acq2.transferred_title_to = model.Person(ident="payne", label="Oliver Payne")
ts2 = model.TimeSpan()
ts2.begin_of_the_begin = "1909-01-01T00:00:00Z"
ts2.end_of_the_end = "1909-12-31T23:59:59Z"
acq2.timespan = ts2
acq2.part_of = model.Activity(ident="durand_payne", label="Full Provenance Activity")
top.changed_ownership_through = acq2
```



