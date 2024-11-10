---
title: Object Production and Destruction
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

This section covers the beginning and ending of objects' existence, along with the attribution of the artist to the production of the object.

## Base Production Activity

The first activity in an object's lifecycle is its creation, which is described using the `Production` class.  The relationship from the object to the activity is `produced_by`, and the `Production` activity itself follows the general [base activity model](/model/base/#events-and-activities) with the description of time, location and agents.

__Example:__
Similar to the Production example in the basic patterns, "The Night Watch" was created by Rembrandt in Amsterdam in 1642.

```crom
top = model.HumanMadeObject(ident="nightwatch/5", label="Night Watch by Rembrandt")
prod = model.Production()
top.produced_by = prod
prod.carried_out_by = model.Person(ident="rembrandt", label="Rembrandt")
when = model.TimeSpan(label="1642")
when.begin_of_the_begin = "1642-01-01T00:00:00Z"
when.end_of_the_end = "1642-12-31T23:59:59Z"
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

## Multiple Artists (with Different Roles)

If there are multiple artists collaborating on the same piece of artwork, then we follow the partitioning pattern of creating separate parts of the main `Production` activity. Each of these components captures the details of one particular artist's role in the production of the object. This allows us to assert different properties for each artist's contribution, including different times, techniques, roles, locations or influences.

For consistency, it is recommended that this pattern also be used for production activities when only one artist is known, such that it is easier to add further contributors to the work without restructuring the content. For compatibility with other systems this is, however, not required.

Note that these parts of productions can also have statements associated with them, describing the role in more detail beyond just the classification, technique or other structured data.

__Example:__

A [painted textile called "RÜN"](https://artgallery.yale.edu/collections/objects/153900), where the linen was hand-woven by Sarah Parke and then painted by Mark Barrow.


```crom
top = vocab.Painting(ident="run/1", label = "RUN")
prod = model.Production()
top.produced_by = prod
act1 = model.Production()
act1.technique = vocab.instances['painting']
act1.carried_out_by = model.Person(ident="barrow", label="Mark Barrow")
prod.part = act1
act2 = model.Production()
act2.technique = model.Type(ident="http://vocab.getty.edu/aat/300053643", label="hand weaving")
act2.carried_out_by = model.Person(ident="parke", label="Sarah Parke")
prod.part = act2
```

## Objects Related to the Production

Other objects can play critical roles in the production of artwork, such as copying or being inspired by another artwork, or the use of the same source to create an artwork, either mechanically or manually, such as the negative used for printing a photograph.


### Inspirations, Studies or Copies

Some artworks are copies of, or clearly directly inspired by, others.  This relationship with another work can be captured with the `influenced_by` property of the `Production` activity. The copy could be from memory or with the copied object physically present, and it could be a faithful reproduction or merely recognizably similar. This includes studies done for the final version of the work.

__Example:__

In 1964, Deane Keller created [a copy](https://artgallery.yale.edu/collections/objects/54339) of Daniel Huntington's [portrait of James Dwight Dana](https://artgallery.yale.edu/collections/objects/52687), from 1858. 

```crom
top = vocab.Painting(ident="kellerdana/1", label="Copy of Huntington Portrait")
prod = model.Production()
top.produced_by = prod
copied = model.HumanMadeObject(ident="huntingtondana", label="Huntington Portrait of Dana")
prod.influenced_by = copied
prod.carried_out_by = model.Person(ident="keller", label="Deane Keller")
```

### Reproduction from an Identifiable Source

Many objects are created from a source, such as a photograph being printed from a negative, a print created from a woodcut, or a sculpture made from a cast.  The use of the particular source can be captured as part of the description of the `Production` of the object using the `used_specific_object` property.

Note that all of the art objects created from the same source will show the same image, be it flat or three dimensional. The source also shows the same image, albiet likely somehow reversed. The image is modeled as a `VisualItem` that all of the physical objects show, allowing us to group the objects together. For more information about the work, see the section on [aboutness](../aboutness/).

Equipment or tools such as a particular camera or palette would also be modeled with the same property `used_specific_object`, however would not (of course) show the same visual item as the main work.

__Example:__

Copies of a photograph, taken by Alfred Stieglitz of Georgia O'Keeffe, are printed from the same negative at different times and now owned by different organizations: [Yale University Art Gallery](https://artgallery.yale.edu/collections/objects/198690), [National Gallery of Art](https://www.nga.gov/collection/art-object-page.60057.html), and the [Georgia O'Keeffe Museum](https://collections.okeeffemuseum.org/object/6627/)

```crom
top = vocab.Photograph(ident="okeeffe-gok/1", label = "GOK 1918, GOKM")
top.identified_by = vocab.AccessionNumber(content="2014.3.78")
prod = model.Production(label = "Printing of Photograph")
top.produced_by = prod
negative = model.HumanMadeObject(ident="okeeffe-negative", label = "Negative of GOK 1918")
prod.used_specific_object = negative
vi = model.VisualItem(ident="okeeffe", label="Visual Content of GOK 1918")
top.shows = vi
```

```crom
top = vocab.Photograph(ident="okeeffe-yuag/1", label = "GOK 1918, YUAG")
top.identified_by = vocab.AccessionNumber(content="2016.101.242")
prod = model.Production(label = "Printing of Photograph")
top.produced_by = prod
negative = model.HumanMadeObject(ident="okeeffe-negative", label = "Negative of GOK 1918")
prod.used_specific_object = negative
vi = model.VisualItem(ident="okeeffe", label="Visual Content of GOK 1918")
top.shows = vi
```

__Example:__

A [print](https://collections.britishart.yale.edu/catalog/tms:6141) at the Yale Center for British Art, Chaucer's Canterbury Pilgrims, made from a specific [copper plate](https://artgallery.yale.edu/collections/objects/11787) held at the Yale University Art Gallery.

```crom
top = vocab.Print(ident="ccp/1", label="Chaucer's Canterbury Pilgrims")
prod = model.Production(label="Printing from Plate")
top.produced_by = prod
prod.used_specific_object = model.HumanMadeObject(ident="ccp-plate", label="Plate for CCP")
```

```crom
top = model.HumanMadeObject(ident="ccp-plate/1", label="Plate for CCP")
top.made_of = vocab.instances['copper']
```

## Cause of Production

Artworks are frequently commissioned, where an artist agrees to create the artwork and the commissioner agrees to compenate the artist for his efforts. The modeling of the [commission](/model/provenance/promises/#commissions-for-artwork) is described in the Provenance section, as an exchange of promises, and potentially also Payments. The object can refer to this Activity in its Production with the `caused_by` property.

__Example:__

The production of the [Nuveen Painting](https://artgallery.yale.edu/collections/objects/290048) was caused by its commissioning.

```crom
top = model.HumanMadeObject(ident="nuveen/1", label="Nuveen Painting")
top.identified_by = vocab.PrimaryName(content="The Nuveen Painting")
prod = model.Production()
prod.carried_out_by = model.Person(ident="dine", label="Jim Dine")
prod.caused_by = model.Activity(ident="nuveen_commission", label="Commission")
top.produced_by = prod
```

## Unidentified or Unknown Artist

Many objects are created by an unknown or unidentified artist. While it is possible to have a different Person record with "Unidentified Artist" as the name, this quickly creates a huge number of identified people in the system with only a single reference to each. Instead, it is recommended to create a Group record to represent all unidentified artists, and then each object would have its Production `carried_out_by` the Group, meaning one (or more) people within that artificial set of people.

If some features of the artist is know, for example their nationality or the century in which they were active, these can be additional Groups with these properties.

__Example:__

The [Coppa Amatoria](https://artgallery.yale.edu/collections/objects/138452) was created by an unidentified artist or artists from Italy.

```crom
top = model.HumanMadeObject(ident="coppa/1", label="Coppa Amatoria")
top.identified_by = vocab.PrimaryName(content="Coppa Amatoria")
prod = model.Production()
prod.carried_out_by = model.Group(ident="unknown_italian", label="Unidentified Italian")
top.produced_by = prod
```


## Attribution Qualifiers

### Influenced By an Artist

If there is some connection between the production of the object and someone who was not the artist directly, but influenced the production, then the `influenced_by` property can be used to reference that person.  These are often expressed as "after", "in the style of", or "in the manner of" attributions -- they qualify the attribution by relating the production to someone (likely as embodied by their work, rather than through a personal connection) that directly influenced it.

__Example:__

The painting "Wash Day" was intentionally created in the manner of Winslow Homer.

```crom
top = vocab.Painting(ident="washday/1", label="Wash Day")
top.identified_by = vocab.PrimaryName(content="Wash Day")
prod = model.Production()
prod.influenced_by = model.Person(ident="whomer", label="Winslow Homer")
top.produced_by = prod
```

### Attribution of a Group Related to an Artist

Even if the artist's or artists' identity is not known exactly, the person or persons may be known to have been part of a group, such as the workshop of a more famous "master". In this case, the `Group` that represents the workshop can be the actor that carries out the `Production`: this does not mean that every member of the group participated, just that at least one of them did, in the same way that saying that a document was written by an organization does not imply all employees contributed to the text.

We can use the `influenced_by` property on the `Formation` (the creation) of the group to connect it to a known person -- the "master" of the workshop in the example use case. The "master" might not have participated in the group, or even been alive when it was formed, and hence does not necessarily form the group or is even a member of it. 

This approach can be used for workshops, studios, the set of pupils, followers, and so forth. It is not that the entire Group created the object, but that one or more of them did. 

__Example:__

The "Bust of a Man" object described above was created by the Studio of Francis Harwood, a Group. The example below is the record for the Group.
 
```crom
top = vocab.Studio(ident="harwoodstudio/1", label="Studio of Francis Harwood")
fm = model.Formation()
top.formed_by = fm
fm.influenced_by = model.Person(ident="http://vocab.getty.edu/ulan/500015886", label="Francis Harwood")
```

### Uncertain or Changing Attributions

A piece of information associated with historical artworks that can change as research and understanding improves is the identity of the artist that produced it. The actor that is referenced in `carried_out_by` is the current opinion, but previous attributions can still be recorded. The pattern used for this is described in more detail in the [assertions](/model/assertion/) section of the documentation.


## Production by Removal

It is also possible for an object to come into documentary existence when it is removed from a larger object.  The production of the part is simply part of the production of the whole, but until it is removed, it does not need a separate identity or existence.

This occurs reasonably frequently, for both valid and unscrupulous motivations.  In the work of conservation, it is often necessary to remove a tiny flake of an object to experiment with, before applying the method to the whole.  If there are unexpected side effects of the experiment, then the whole object is saved at the expense of an unnoticeable change. It is important to know that the sample was produced in the past and removed in the present, rather than it was created _de novo_ in the present.

A second scenario when this occurs is unfortunately common.  If an object, such as a medieval manuscript, can be sold for a higher profit by splitting it up into parts and selling each part individually, then unscrupulous sellers will do just that. Rather than sell an innocuous book of hours to a single buyer, instead each illumination can be sold individually and then the remaining text-bearing pages either dumped or sold over time at a greatly reduced price.  This dispersal of manuscripts still occurs today.

In order to model this, instead of a `Production`, the object is `removed_by` a `PartRemoval` activity.  That activity is just like all other activities, other than it has a `diminished` property that refers to the whole object from which the part was removed.  It is not normally useful to have a separate `Production` for the part, if the information about the source object it was removed from is known.


__Example:__

The collection item is a page from a gradual (manuscript) by the Master of the Libro dei Notai. [Source](https://artgallery.yale.edu/collections/objects/51500)

```crom
top = vocab.Page(ident="gradualpage/1", label="Page from a Gradual")
rm = model.PartRemoval()
whole = model.HumanMadeObject(ident="gradual", label="Gradual")
rm.diminished = whole
top.removed_by = rm
```

## Discovery versus Production

If the object enters into documented history by being found, rather than created, then instead of a `Production` entry, there is an `Encounter`. This would be appropriate for fossils, gemstones, or other natural history items, along with objects that were created but no information is available about that production or the "discovery" of the object is the first significant entry in the item's provenance. This pattern may only be used for the discovery of the object, rather than other sorts of encounters.

Encounters may also be recorded as separate events, as described in the [provenance section](../../provenance/encounters/). The separate event must be used for any encounter that is not a discovery.

Instead of `produced_by`, the property used is `encountered_by`, and the class of the activity is `Encounter`. All of the other patterns are the same, including where the encounter took place, who encountered it, when it occurred and so forth. The role pattern also applies, with the `part`s of the encounter also being `Encounter`s.

__Example:__

The fossil Torosaurus (VP.04072) was encountered in 1891 by John Bell Hatcher.

```crom
top = model.HumanMadeObject(ident="torosaurus/1", label="Torosaurus Gladius")
enc = model.Encounter()
enc.carried_out_by = model.Person(ident="hatcher", label="John Bell Hatcher")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1891-01-01T00:00:00Z"
ts.end_of_the_end = "1891-12-31T23:59:59Z"
enc.timespan = ts
top.encountered_by = enc
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
when.end_of_the_end = "1998-09-02T22:40:00Z"
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
when.end_of_the_end = "1998-09-02T22:40:00Z"
dest.timespan = when
act = model.Event(ident="sr111crash", label="Crash of Swiss Air 111")
dest.caused_by = act
```

