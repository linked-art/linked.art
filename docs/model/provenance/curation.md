---
title: Object Curation
up_href: "/model/provenance/"
up_label: "Provenance"
---

[TOC]

## Introduction

While owned, the object is typically looked after and activities take place that affect it or try to preserve it. Whether these activities can be formally considered 'curation' is a very subjective and potentially controversial opinion, and we make no distinction between individual owners, art dealers, museums and galleries, or any other party that takes actions while owning an object. 


## Taking Inventory

One such activity is taking inventory _(aat:300077506)_ by the owner of their objects. This is routinely carried out by art dealers, collectors or museums, in order to ensure that they still have custody of all of the objects that they believe they do.  This establishes the existence and presence of the object at a certain place and time, and is thus useful in tracking the object through history.

This is modeled as an `Encounter`. In this case, the actor knows where the object is and it is not a "discovery", and the Provenance Activity describes the activity of the owner recording that they have seen the object, and perhaps inspected or examined it.  The object itself does not change, nor its ownership or custody, but this is more that the knowledge of the state of the object is verified or updated.

```crom
top = vocab.ProvenanceEntry(ident="auto int-per-segment")
inv = vocab.Inventorying()
what = vocab.Painting(label="Painting")
who = vocab.MuseumOrg(label="Owning Museum")
inv.encountered = what
inv.carried_out_by = who
top.part = inv
```

## Object Ownership and Existence

There isn't a temporal entity in the model that represents the entire duration of ownership of an object by a Person or Group, nor a temporal entity that represents the entire existence of an object.  This is useful for the simple cases, when an object is acquired and sold individually, however quickly becomes complicated when multiple objects are involved in a single transaction.  Instead, the [relative temporal ordering properties](/model/provenance/) of `starts_after_the_end_of` and `ends_before_the_start_of` are recommended to chain Provenance Activities together, allowing a system to infer the periods between the events.

