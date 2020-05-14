---
title: Object Location and Movement
up_href: "/model/provenance/"
up_label: "Provenance"
---

[TOC]

## Introduction

The [current location](/model/object/ownership/) of an object is determined by the most recent time that it was moved. In an environment where every activity was recorded, it would not be necessary to record the location as this could be calculated for any given point in time based on the activities which resulted in the object being moved. Such an information environment is important for some sectors (such as couriers and shipping companies) that specialize in object tracking, however is not something which most cultural heritage information systems track to this degree of granularity.

There are several scenarios in which it is, however, useful to track the movement of an object, in the same way as tracking custody or ownership.  These include:


* Putting an object on display, or taking it off display and putting it back in storage. This would inform when objects were visible to the public.
* Putting an object on display as part of an exhibition, when the object is owned by the exhibiting organization and hence there is no transfer of custody between organizations.
* Moving an object between storage facilities, conservation studios or galleries.

If the institution is subdivided into departments, these moves may also coincide with the transfer of custody between departments. For example, if the paintings department and the conservation department are separate entities, then not only is the painting moved from the gallery to the conservation studio, it might also have its custody transferred to the conservation department.


## Moving an Object

The model for moving an object is very similar to that of an Acquisition, Transfer of Custody or Payment.  There is an activity, which can be `carried_out_by` an actor and all of the other basic activity features, that `moved` the object between two locations, from the place given in `moved_from` and to the place given in `moved_to`.

```crom
top = vocab.ProvenanceEntry(label="Exhibiting a Painting")
what = vocab.Painting(label="Example Painting")
storage = vocab.StoragePlace(label="Storage Venue")
display = vocab.Gallery(label="Gallery")
exh = vocab.Exhibition()
top.motivated_by = exh
mv = model.Move()
mv.moved = what
mv.moved_from = storage
mv.moved_to = display
top.part = mv
```
