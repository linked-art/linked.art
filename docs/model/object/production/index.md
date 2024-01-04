---
title: Object Production and Destruction
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

This section covers the beginning and ending of objects' existence, along with the attribution of the artist to the production of the object.

## Base Production Activity

The first activity in an object's lifecycle is its creation, or `Production`.  The relationship from the object to the activity is `produced_by`, and the `Production` activity itself follows the general [base activity model](/model/base/#events-and-activities) with the description of time, location and agents.

__Example:__

Similar to the Production example in the basic patterns, "The Night Watch" was created by Rembrandt in Amsterdam in 1642.

```crom
top = model.HumanMadeObject(ident="nightwatch/5", label="Night Watch by Rembrandt")
prod = model.Production()
top.produced_by = prod
prod.carried_out_by = model.Person(ident="rembrandt", label="Rembrandt")
when = model.TimeSpan(label="1642")
when.begin_of_the_begin = "1642-01-01T00:00:00"
when.end_of_the_end = "1642-12-31T23:59:59"
prod.timespan = when
prod.took_place_at = model.Place(ident="amsterdam", label="Amsterdam")
```

## Techniques and Classifications

We distinguish between techniques used to create the artwork, and other classifications. Techniques have their own property (`technique` rather than `classified_as`) and can thus easily be distinguished from other classifications.

### Techniques

If there is a particular technique known to have been used in the creation of the object, this can be expressed using the `technique` property, referring to a controlled vocabulary term for the technique. This should be used to capture specific techniques or methods, and the base `classified_as` property used for more general classifications of the activity.  More general classifications are more common on individual roles, discussed below.
 
__Example:__

The sculpture "Bust of a Man" was created by the Studio of Francis Hardwood using the sculpting technique.

```crom
top = vocab.Sculpture(ident="bust/1", label="Bust of a Man")
prod = model.Production()
prod.carried_out_by = model.Group(ident="harwoodstudio", label="Studio of Francis Harwood")
prod.technique = vocab.instances['sculpting']
top.produced_by = prod
```

## Multiple Artists

If there are multiple artists collaborating on the same piece of artwork, then we follow the partitioning pattern of creating separate parts of the main `Production` activity. Each of these components captures the details of one particular artist's role in the production of the object. This allows us to assert different properties for each artist's contribution, including different times, techniques, locations or influences.

For consistency, it is recommended that this pattern also be used for production activities when only one artist is known, such that it is easier to add further contributors to the work without restructuring the content. For compatibility with other systems this is, however, not required.

__Example:__

A sculpture that is then painted by another artist, would be produced by the overall activity, with two parts, one for each artist's activities.

```crom
top = vocab.Sculpture(ident="auto int-per-segment", label = "Painted Sculpture", art=1)
prod = model.Production()
top.produced_by = prod
act1 = model.Production()
act1.technique = vocab.instances['sculpting']
act1.carried_out_by = model.Person(label="Sculptor")
prod.part = act1
act2 = model.Production()
act2.carried_out_by = model.Person(label="Painter")
act2.technique = vocab.instances['painting']
prod.part = act2
```

## Objects Related to the Production

Other objects can play critical roles in the production of artwork, such as copying or being inspired by another artwork, or the use of the same source to create an artwork, either mechanically or manually, such as the negative used for printing a photograph.


### Inspiration or Copies

Some artworks are copies of, or clearly directly inspired by, others.  This relationship with another work can be captured with the `influenced_by` property of the `Production` activity. The copy could be from memory or with the copied object physically present, and it could be a faithful reproduction or merely recognizably similar. 

__Example:__


```crom
top = vocab.Painting(ident="auto int-per-segment", label="Copy of Painting of a Fish", art=1)
prod = model.Production()
top.produced_by = prod
copied = vocab.Painting(label="Painting of a Fish", art=1)
prod.influenced_by = copied
prod.carried_out_by = model.Person(label="Copyist")
```

### Reproduction from an Identifiable Source

Many objects are created from a source, such as a photograph being printed from a negative, a print created from a woodcut, or a sculpture made from a cast.  The use of the particular source can be captured as part of the description of the `Production` of the object using the `used_specific_object` property.

All of the art objects created from the same source show the same image, be it flat or three dimensional. The source also shows the same image, albiet likely somehow reversed. The image is modeled as a `VisualItem` that all of the physical objects, including the source object, show. This allows us to group the objects together based on their provenance.

__Example:__

A photograph is printed using a Negative. Both the positive and the negative show the same visual content, as would any other prints of the photograph.


```crom
top = vocab.Photograph(ident="auto int-per-segment",label = "Photograph")
prod = model.Production(label = "Printing of Photograph")
top.produced_by = prod
negative = vocab.Negative(label = "Negative of Photograph")
prod.used_specific_object = negative
vi = model.VisualItem(label="Visual Content of Photographs and Negative")
top.shows = vi
negative.shows = vi
```

## Attributions

### Attribution of a Group

Even if the artist's or artists' identity is not known exactly, the person or persons may be known to have been part of a group, such as the workshop of a more famous "master". In this case, the `Group` that represents the workshop can be the actor that carries out the `Production`: this does not mean that every member of the group participated, just that at least one of them did, in the same way that saying that a document was written by an organization does not imply all employees contributed to the text.

We can use the `influenced_by` property on the `Formation` (the creation) of the group to connect it to a known person -- the "master" of the workshop in the example use case. The "master" might not have participated in the group, or even been alive when it was formed, and hence does not necessarily form the group or is even a member of it. 

__Example:__

A painting is from the workshop of an artist named Franckz.
 
```crom
top = vocab.Painting(ident="auto int-per-segment", label = "Painting from the workshop of Franckz", art=1)
prod = model.Production()
top.produced_by = prod
grp = model.Group(label = "Workshop of Franckz")
prod.carried_out_by = grp
f = model.Formation()
grp.formed_by = f
f.influenced_by = model.Person(label = "Franckz")
```

### Uncertain or Changing Attributions

A piece of information associated with historical artworks that can change as research and understanding improves is the identity of the artist that produced it. The actor that is referenced in `carried_out_by` is the current opinion, but previous attributions can still be recorded. 

In order to clearly separate the previous thinking from current, the model explicitly includes the act of assigning the previous artist as an `AttributeAssignment`. The assignment activity assigns the previous artist's role as part of the main Production, but has an "obsolete" classification to indicate that it is no longer believed to be correct. A "possibly" classification would indicate that the attribution of the artist is uncertain.

The Attribute Assignment pattern is described in more detail in the [assertions](/model/assertion/) section of the documentation.

__Example:__

It was previously thought that J. Artist produced the painting, by Paintings Curator in 1923, but that is no longer held to be correct.

```crom
top = vocab.Painting(ident="auto int-per-segment",label="Painting", art=1)
prod = model.Production()
top.produced_by = prod
aa = vocab.ObsoleteAssignment()
who = model.Person(label="J. Artist")
prod2 = model.Production()
prod2.carried_out_by = who
prod.assigned_by = aa
aa.assigned = prod2
aa.assigned_property = "part_of"
aa.carried_out_by = model.Person(label = "Paintings Curator")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1923-07-20"
ts.end_of_the_end = "1923-07-21"
aa.timespan = ts
```

## Production by Removal

It is also possible for an object to come into documentary existence when it is removed from a larger object.  The production of the part is simply part of the production of the whole, but until it is removed, it does not need a separate identity or existence.

This occurs reasonably frequently, for both valid and unscrupulous motivations.  In the work of conservation, it is often necessary to remove a tiny flake of an object to experiment with, before applying the method to the whole.  If there are unexpected side effects of the experiment, then the whole object is saved at the expense of an unnoticeable change. It is important to know that the sample was produced in the past and removed in the present, rather than it was created de novo in the present.

A second scenario when this occurs is unfortunately common.  If an object, such as a medieval manuscript, can be sold for more by splitting it up into parts and selling each part individually, then unscrupulous sellers will do just that. Rather than sell an innocuous book of hours to a single buyer, instead each illumination can be sold individually and then the remaining text-bearing pages either dumped or sold over time at a greatly reduced price.  This dispersal of manuscripts still occurs today.


In order to model this, instead of a `Production`, the object is `removed_by` a `PartRemoval` activity.  That activity is just like all other activities, other than it has a `diminished` property that refers to the whole object from which the part was removed.  The removed object can have a `Production` event, but it should be a part of the `Production` of the whole.  As it is unlikely that there is any new information about the removed part, this is not normally useful.


__Example:__

A conservator removes a paint sample from a painting.

```crom
top = model.HumanMadeObject(ident="auto int-per-segment",label="Paint sample")
rm = model.PartRemoval()
rm.carried_out_by = model.Person(label="Conservator")
whole = vocab.Painting(label="Painting")
rm.diminished = whole
top.removed_by = rm
```

__Example:__

A seller removes a page of a manuscript for individual sale.

```crom
top = vocab.Page(ident="auto int-per-segment",label="Page of Manuscript")
rm = model.PartRemoval()
rm.carried_out_by = model.Person(label="Unscrupulous Seller")
whole = vocab.Manuscript(label="Manuscript")
rm.diminished = whole
top.removed_by = rm
```

## Destruction

The end of the provenance chain of an object is when it is known to have been destroyed.  Loss of the object leaves the chain open ended as it might be recovered in the future, however if the object is destroyed then there is no coming back. Objects should, thus, only be recorded as destroyed if they are known to be so.

The model uses a `Destruction` class that represents the going out of existence of the object. A destruction only applies to a single object, and thus every object has their own destruction, even if that destruction was caused by the same wider event or activity.  This means that the Destruction is not `carried_out_by` an actor, but instead (as in the following section) another activity causes the destruction.

__Example:__

The painting "Le Peintre" by Picasso was destroyed (in a plane crash) on September 2nd, 1998 at about 10:30pm. [Source](https://en.wikipedia.org/wiki/Swissair_Flight_111)

```crom
top = vocab.Painting(ident="lepeintre/1", label="Le Peintre by Picasso")
dest = model.Destruction(label="Destruction of Le Peintre")
top.destroyed_by = dest
when = model.TimeSpan()
when.begin_of_the_begin = "1998-09-02T22:20:00Z"
when.end_of_the_end = "1998-09-02T022:40:00Z"
dest.timespan = when
```

### Cause of Destruction

As discussed above, the same event or activity could be the cause of the destruction of many individual objects. A museum burning down or otherwise being destroyed would destroy many objects, including the building itself. On a smaller scale, an individual destruction could be caused by a particular activity of an individual. 

In order to distinguish between the destruction itself and its cause, we use the `caused_by` relationship between the Destruction and the Activity or Event that caused it. The event should be described and classified as any other event in the model.

__Example:__

Le Peintre was destroyed because of the plane crashing. (Which also would have caused the destruction of the plane, the death of the crew, passengers and many other consequences)

```crom
top = vocab.Painting(ident="lepeintre/2", label="Le Peintre by Picasso")
dest = model.Destruction(label="Destruction of Le Peintre")
top.destroyed_by = dest
when = model.TimeSpan()
when.begin_of_the_begin = "1998-09-02T22:20:00Z"
when.end_of_the_end = "1998-09-02T022:40:00Z"
dest.timespan = when
act = model.Event(ident="sr111crash", label="Crash of Swiss Air 111")
dest.caused_by = act
```


## Other Specific Activities

If there are other activities that are specific to the particular object and do not have any identity of their own beyond the object, then that activity can be described with a relationship from the object to the activity, rather than from the activity to the object. In these cases the description of the activity will end up embedded completely within the object's record, in the same way that the publication of a work is embedded within the work's record.  In the more general case, when the activity has its own identity (such as an auction or conservation work on the object) then the event will instead refer to the object and the object must not refer to the event. The relationship for this situation is `used_for` between the object and the activity.


__Example:__

A knife was created and used for a specific ritual, about which we know nothing else.

```
top = model.HumanMadeObject(ident="auto int-per-segment", label="Ritual Knife")
top.identified_by = vocab.PrimaryName(content="Ritual Knife")
ritual = model.Activity()
ritual.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300065284")
top.used_for = ritual
```
