---
title: Object Curation
up_href: "/model/provenance/"
up_label: "Provenance"
---

[TOC]

## Introduction

While owned, the object is typically looked after and activities take place that affect it or try to preserve it. Whether these activities can be formally considered 'curation' is a very subjective and potentially controversial opinion, and we make no distinction between individual owners, art dealers, museums and galleries, or any other party that takes actions while owning an object. 

## Ownership 

Provenance activities exist in a larger context -- the ownership of the object by individuals, and the set of all owners.  Some events may only be linked to the owner, and hence be part of the ownership period with no further information available as to who carried them out or when they took place.

### Individual Owners

Between acquisitions, the object is owned and, presumably, looked after by its owner.  This activity of looking after the object _(aat:300054277)_ is modeled as a continuation of the ownership chain which is punctuated by the acquisition activities.
 
```
top = model.Phase()
top._label = "Ownership of the Painting"
start = Acquisition()
start._label = "Acquisition of Painting by Owner"
end = Acquisition()
end._label = "Owner gives Painting to someone else"
owner = Actor()
owner._label = "Owner"
what = Painting(art=1)
who = Person()
who._label = "Someone Else"
start.transferred_title_of = what
start.transferred_title_to = who
end.transferred_title_of = what
end.transferred_title_from = who
top.related_entity = who
top.phase_of = what
top.relationship = "current_owner"
top.initiated_by = start
top.terminated_by = end
```

#### Taking Inventory

One such activity is taking inventory _(aat:300077506)_ by the owner of all their objects, including the one being described. This is routinely carried out by art dealers, collectors or museums, in order to ensure that they still have custody of all of the objects that they believe they do.  This establishes the existence and presence of the object at a certain place and time, and is thus useful in tracking the object through history.

```
top = model.Phase()
top._label = "Ownership of the Painting"
inv = Inventorying()
inv._label = "Inventory Taking by Owner"
top.part = inv
```

### Lifetime of Object

The entire provenance of an object _(aat:300055863)_ is also an activity, that consists of all of all of the above events, from production through to destruction or the present day ownership.  All of the transfers of ownership and the resulting ownership periods are included, giving a single place to associate and thereby discover the events.

```
top = model.Phase()
what = Painting(art=1)
top._label = "Lifetime of Painting"
top.phase_of = what
prod = Production()
prod.produced = what
own1 = model.Phase()
own1._label = "Ownership by Artist"
c1 = Acquisition()
c1.transferred_title_of = what
own2 = model.Phase()
own2._label = "Ownership by first owner"
c2 = Purchase()
c2.transferred_title_of = what
own3 = model.Phase()
own3._label = "Ownership by second and final owner"
dest = Destruction()
dest.took_out_of_existence = what
top.part = prod
top.part = own1
top.part = c1
top.part = own2
top.part = c2
top.part = own3
top.part = dest
```
