---
title: Object Production and Destruction
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

This section covers the beginning and ending of objects' existence, along with the attribution of the artist to the production of the object.

## Base Production Activity

The first activity in an object's lifecycle is its creation, or `Production`.  The relationship to the object that was produced by the activity (`produced`) is added to the general activity model, along with the time, location and actors. This follows the base pattern for [activities](/model/base/#events-and-activities).

__Example:__

A painting is created by an artist, in their studio, in March 1780.

```crom
top = Painting(label="Painting", art=1)
prod = Production()
prod.carried_out_by = Actor(label="Artist")
prod.took_place_at = Place(label="Artist's Studio")
when = TimeSpan()
when.begin_of_the_begin = "1780-03-05T00:00:00Z"
when.end_of_the_end = "1780-03-06T00:00:00Z"
prod.timespan = when
top.produced_by = prod
```

## Techniques and Classifications

We distinguish between techniques used to create the artwork, and other classifications. Techniques have their own property (`technique` rather than `classified_as`) and can thus easily be distinguished from other classifications.

### Techniques

If there is a particular technique known to have been used in the creation of the object, this can be expressed using the `technique` property, referring to a controlled vocabulary term for the technique. This should be used to capture specific techniques or methods, and the base `classified_as` property used for more general classifications of the activity.

__Example:__

A glass sculpture is created using the glassblowing technique, which is identified by _aat:300053932_.

```crom
top = Sculpture(label="Glass Sculpture", art=1)
prod = Production()
prod.carried_out_by = Actor(label = "Glassblowing Artist")
prod.technique = instances['glassblowing']
top.produced_by = prod
```

### Classifications

Classifications for production events are less common than techniques, but still possible.  These classifications must not be techniques, but instead some assertion about the activity generally. This could include whether the activity was a minor contribution to the overall work, or whether the activity was performed legally or not. 

__Example:__

Grafitti artwork is created using the "spraypainting" technique, and could also be considered "vandalism", but vandalism is not a technique.

```crom
top = HumanMadeObject(label="Graffiti", art=1)
prod = Production(label="Production of Graffiti")
prod.technique = vocab.instances['spraypainting']
prod.classified_as = vocab.instances['vandalism']
top.produced_by = prod
```

## Multiple Artists

If there are multiple artists collaborating on the same piece of artwork, then we follow the partitioning pattern of creating separate parts of the main `Production` activity. Each of these components captures the details of one particular artist's role in the production of the object. This allows us to assert different properties for each artist's contribution, including different times, techniques, locations or influences.

For consistency, it is recommended that this pattern also be used for production activities when only one artist is known, such that it is easier to add further contributors to the work without restructuring the content. 

__Example:__

A sculpture that is then painted by another artist, would be produced by the overall activity, with two parts, one for each artist's activities.

```crom
top = Sculpture(label = "Painted Sculpture", art=1)
prod = Production()
top.produced_by = prod
act1 = Production()
act1.technique = instances['sculpting']
act1.carried_out_by = Actor(label="Sculptor")
prod.part = act1
act2 = Production()
act2.carried_out_by = Actor(label="Painter")
act2.technique = instances['painting']
prod.part = act2
```

## Objects Related to the Production

Other objects can play critical roles in the production of artwork, such as copying or being inspired by another artwork, or the use of the same source to create an artwork, either mechanically or manually, such as the negative used for printing a photograph.


### Inspiration or Copies

Some artworks are copies of, or clearly directly inspired by, others.  This relationship with another work can be captured with the `influenced_by` property of the `Production` activity. The copy could be from memory or with the copied object physically present, and it could be a faithful reproduction or merely recognizably similar. 

__Example:__


```crom
top = Painting(label="Copy of Painting of a Fish", art=1)
prod = Production()
top.produced_by = prod
copied = Painting(label="Painting of a Fish", art=1)
prod.influenced_by = copied
prod.carried_out_by = Person(label="Copyist")
```

### Reproduction from an Identifiable Source

Many objects are created from a source, such as a photograph being printed from a negative, a print created from a woodcut, or a sculpture made from a cast.  The use of the particular source can be captured as part of the description of the `Production` of the object using the `used_specific_object` property.

All of the art objects created from the same source show the same image, be it flat or three dimensional. The source also shows the same image, albiet likely somehow reversed. The image is modeled as a `VisualItem` that all of the physical objects, including the source object, show. This allows us to group the objects together based on their provenance.

__Example:__

A photograph is printed using a Negative. Both the positive and the negative show the same visual content, as would any other prints of the photograph.


```crom
top = Photograph(label = "Photograph")
prod = Production(label = "Printing of Photograph")
top.produced_by = prod
negative = Negative(label = "Negative of Photograph")
prod.used_specific_object = negative
vi = VisualItem(label="Visual Content of Photographs and Negative")
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
top = Painting(label = "Painting from the workshop of Franckz", art=1)
prod = Production()
top.produced_by = prod
grp = Group(label = "Workshop of Franckz")
prod.carried_out_by = grp
f = Formation()
grp.formed_by = f
f.influenced_by = Person(label = "Franckz")
```

### Uncertain or Changing Attributions

A piece of information associated with historical artworks that can change as research and understanding improves is the identity of the artist that produced it. The actor that is referenced in `carried_out_by` is the current opinion, but previous attributions can still be recorded. 

In order to clearly separate the previous thinking from current, the model explicitly includes the act of assigning the previous artist as an `AttributeAssignment`. The assignment activity assigns the previous artist's role as part of the main Production, but has an "obsolete" classification to indicate that it is no longer believed to be correct. A "possibly" classification would indicate that the attribution of the artist is uncertain.

The Attribute Assignment pattern is described in more detail in the [assertions](/model/assertion/) section of the documentation.

__Example:__

It was previously thought that J. Artist produced the painting, by Paintings Curator in 1923, but that is no longer held to be correct.

```crom
top = Painting(label="Painting", art=1)
prod = Production()
top.produced_by = prod
aa = vocab.ObsoleteAssignment()
who = Person(label="J. Artist")
prod2 = Production()
prod2.carried_out_by = who
prod.assigned_by = aa
aa.assigned = prod2
aa.assigned_property = "part_of"
aa.carried_out_by = Person(label = "Paintings Curator")
ts = TimeSpan()
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

A seller removes a page of a manuscript for individual sale.

```crom
top = vocab.Page(label="Page of Manuscript")
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

The Painting was destroyed in 1823.

```crom
top = Painting(label="Example Destroyed Painting", art=1)
dest = Destruction(label="Destruction of Painting")
top.destroyed_by = dest
when = TimeSpan()
when.begin_of_the_begin = "1823-03-01T00:00:00Z"
when.end_of_the_end = "1823-03-31T00:00:00Z"
dest.timespan = when
```


### Cause of Destruction

As discussed above, the same event or activity could be the cause of the destruction of many individual objects. A museum burning down or otherwise being destroyed would destroy many objects, including the building itself. On a smaller scale, an individual destruction could be caused by a particular activity of an individual. 

In order to distinguish between the destruction itself and its cause, we use the `caused_by` relationship between the Destruction and the Activity or Event that caused it. The event should be described and classified as any other event in the model.

__Example:__

The Painting was destroyed in 1823, due to being burnt by someone.

```crom
top = Painting(label="Example Destroyed Painting", art=1)
dest = Destruction(label="Destruction of Painting")
top.destroyed_by = dest
when = TimeSpan()
when.begin_of_the_begin = "1823-03-01T00:00:00Z"
when.end_of_the_end = "1823-03-31T00:00:00Z"
dest.timespan = when
act = Activity(label="Burning of the Painting")
act.carried_out_by = Person(label="Painting Burner")
dest.caused_by = act
```

