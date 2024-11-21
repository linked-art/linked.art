---
title: "Exhibitions"
---

[TOC]

## Introduction

Exhibitions are a very common activity that involves artwork owned by different organizations being displayed together, often with additional contextual information linking the pieces together.  The exhibition is often presented at different venues over time, and might be part of a series such as the World Fairs or annual exhibitions.

The model divides exhibitions across two separate entities: the activity of exhibiting the objects that occured at a place and point in time, and the conceptual notion of the exhibition. This separation is important as activities are not `about` anything, and for exhibitions that were planned but cancelled (perhaps due to a war, a pandemic, or just loss of financing) the conceptual exhibition allows the description of the idea without asserting that it actually occured.


## Exhibition Activity

There is an activity which is the exhibiting of the objects.  In particular, the exhibition occurs at a certain time given in `timespan`, at a certain place or places given in `took_place_at`, and was organized by some actor or actors, likely organizations, given in `carried_out_by`. It can be recognized as an exhibition using the classification of _aat:300054766_, "exhibitions". Exhibitions link to the set of objects exhibited with the `used_specific_object` property to a [Set](/model/collection/)

Note that exhibitions as activities do not have a theme or subject, instead the activity is `influenced_by` an abstract work -- the idea of the Exhibition, described in the next section.

__Example:__

Manet and Modern Beauty at the Getty, October 2019 to January 2020, was carried out by the Getty Museum in Los Angeles, and influenced by the idea behind the exhibition.

```crom
top = vocab.Exhibition(ident="exha/1", label="Manet and Modern Beauty (Getty)")
top.identified_by = vocab.PrimaryName(content="Manet and Modern Beauty")
top.referred_to_by = vocab.Description(content="The great painter of modern Paris Edouard Manet famously shocked contemporary audiences with his provocative pictures. The first exhibition ever to explore the last years of his short life, Manet and Modern Beauty highlights a less familiar and more intimate side of this celebrated artist's work.")
ts = model.TimeSpan()
ts.begin_of_the_begin = "2019-10-08T00:00:00Z"
ts.end_of_the_end = "2020-01-12T23:59:59Z"
top.timespan = ts
top.carried_out_by = vocab.MuseumOrg(ident="http://vocab.getty.edu/ulan/500115988", label="Getty Museum")
top.took_place_at = vocab.City(ident="http://vocab.getty.edu/tgn/7023900", label="Los Angeles")
top.used_specific_object = model.Set(ident="exhset", label="Exhibition objects")
top.influenced_by = model.PropositionalObject(ident="exhidea", label="Idea for Manet and Modern Beauty")
```


## Exhibition Concept

The model distinguishes between the concept of the exhibition and the activity that makes that concept real.  The concept is created by the people who originally think up the exhibition, long before any of the pieces are collected together.  The exhibition concept likely has some theme that results in a coherent set of objects being presented, which could be as complex as post-industrial life or as simple as the life's work of a particular artist.

The concept is modeled as a `PropositionalObject`, and `classified_as` _aat:300417531_ to ensure that it's clearly tagged as an exhibition and separate from the activity. It can have all of basic patterns, such as names, identifiers, references, as well as rights and subjects.

__Example:__

The idea for the Manet and Modern Beauty exhibition is about Manet and Beauty.

```crom
top = vocab.ExhibitionIdea(ident="exhidea/1", label="Idea for Manet and Modern Beauty")
top.identified_by = vocab.PrimaryName(content="Manet and Modern Beauty")
top.about = model.Type(ident="http://vocab.getty.edu/aat/300055821", label="Beauty")
top.about = model.Person(ident="http://vocab.getty.edu/ulan/500010363", label="Manet")
cre = model.Creation()
cre.carried_out_by = model.Person(ident="allan", label="Scott Allan")
cre.carried_out_by = model.Person(ident="beeny", label="Emily Beeny")
cre.carried_out_by = model.Person(ident="groom", label="Gloria Groom")
top.created_by = cre

```

### Known Artist without Known Objects

A frequently encountered situation is that we know about a historical exhibition and which artist or artists had works that were exhibited, but do not know any of the individual works. As the artist was likely not present at the exhibition, nor was involved in planning or otherwise executing it, they cannot be a participant in the activity, nor in the conceptualization of the activity. Equally, we might know of an exhibition that was planned around an artist, but it may never have actually occured.  Finally, we may wish to link an artist to the exhibition regardless of whether we know the objects or not.

The link to the artist is thus on the Exhibition Concept, rather than related to the activity. If the exhibition is about the artist specifically, then the concept can be `about` the artist. If the artist is just known to have had works used in the exhibition, then its `Creation` should be `influenced_by` the artist. It can also, of course, be both.

__Example:__

The conceptualization of the "Manet and Modern Beauty" exhibition was influenced by the Manet and his work.

```crom
top = vocab.ExhibitionIdea(ident="exhidea/2", label="Idea for Manet and Modern Beauty")
top.identified_by = vocab.PrimaryName(content="Manet and Modern Beauty")
cre = model.Creation()
top.created_by = cre
cre.influenced_by = model.Person(ident="http://vocab.getty.edu/ulan/500010363", label="Manet")
```


## Multiple Venues

Some exhibitions are shown at different locations over time, moving from one museum or exhibition hall to another.  In this case, each of the different locations is treated as an exhibition activity in its own right, and then a broader "travelling exhibition" _(aat:300054773)_ is created that these are part of.  Note that the travelling exhibition can have separate properties from its parts, such as a `label` to distinguish the joint nature and a broader `timespan` that covers all of the venues. There is no need to duplicate the organizations and locations in the travelling exhibition, these can be determined more easily by looking at the exhibitions that it consists of.

__Example:__

The Art Institute of Chicago exhibited Manet and Modern Beauty in Chicago with a specific set of objects, and is part of the larger multi-venue exhibition.

```crom
top = vocab.Exhibition(ident="exhb/1", label="Manet and Modern Beauty (AIC)")
top.identified_by = vocab.PrimaryName(content="Manet and Modern Beauty")
ts = model.TimeSpan()
ts.begin_of_the_begin = "2019-05-26T00:00:00Z"
ts.end_of_the_end = "2019-09-08T23:59:59Z"
top.timespan = ts
top.carried_out_by = vocab.MuseumOrg(ident="http://vocab.getty.edu/ulan/500304669", label="Art Institute")
top.took_place_at = vocab.City(ident="http://vocab.getty.edu/tgn/7013596", label="Chicago")
top.used_specific_object = model.Set(ident="exhset", label="Exhibition objects")
top.influenced_by = model.PropositionalObject(ident="exhidea", label="Idea for Manet and Modern Beauty")
top.part_of = model.Activity(ident="exhab", label="Manet and Modern Beauty")
```

The larger multi-venue exhibition activity.

```crom
top = vocab.MultiExhibition(ident="exhab/1", label="Manet and Modern Beauty")
top.identified_by = vocab.PrimaryName(content="Manet and Modern Beauty")
ts = model.TimeSpan()
ts.begin_of_the_begin = "2019-05-26T00:00:00Z"
ts.end_of_the_end = "2020-01-12T23:59:59Z"
top.timespan = ts
top.influenced_by = model.PropositionalObject(ident="exhidea", label="Idea for Manet and Modern Beauty")
```

## Objects 

The collection of art objects on display at exhibitions can be listed from the Exhibition with the property `used_specific_object`. The model for the set of objects that make up the content of the exhibition is the same as the model for permanent collections -- the objects are collected together into a `Set`, which is used by the Exhibition.  

For travelling exhibitions described above, a different collection of objects should be referenced from each of the venues if those sets are substantially different.  Objects are typically added or removed, and each venue will likely have its own context specific information such as descriptions or labels.  The top level activity representing the overall exhibition does not have its own Set in the travelling exhibition scenario.

__Example:__

The objects in Manet and Modern Beauty ...

```crom
top = model.Set(ident="exhset/1", label="Exhibition objects")
top.identified_by = vocab.PrimaryName(content="Objects in Manet and Modern Beauty")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300378926", label="Exhibition Collection")
top.referred_to_by = vocab.Description(content="Objects in the exhibition Manet and Modern Beauty at the Art Institute of Chicago and the Getty Museum")
cre = model.Creation()
ts = model.TimeSpan()
ts.begin_of_the_begin = "2019-05-01T00:00:00Z"
ts.end_of_the_end = "2019-05-01T23:59:59Z"
cre.timespan = ts
top.created_by = cre
```

... include Jeanne, by Manet.

```crom
top = vocab.Painting(ident="spring/12", label="Jeanne (Spring) by Manet")
top.identified_by = model.Name(content="Jeanne (Spring)")
top.member_of = model.Set(ident="exhset")
```

## Integration with Other Parts of the Model

### Provenance Events for Exhibitions

As objects used for exhibitions frequently come from many different organizations, it is useful and interesting to track the custody of the object as well as the ownership.  This event is modeled in the same way as other [Custody](/model/provenance/custody/) changes.  

For each exhibition, the custody of the object is transferred from the previous custodian to the next. In the simple case of a single venue for the exhibition, the first transfer is likely to be from the owner to the organization responsible for the exhibition, and then at the end of the exhibition, the custody is transferred back again.  In a more complex scenario with multiple venues, each organization hosting the exhibition will likely transfer custody to the next in the sequence.  

However, when the object being exhibited at the location is owned by the same organization, there is no transfer of custody. The equivalent activity is likely to be simply moving the object from its regular location to the exhibition space. This is described in the same way as other [Movement](/model/provenance/movement/) events.

The provenance activities can be linked to the Exhibition by asserting that they are `part_of` the Exhibition activity.


### Exhibition Specific Titles

The curators for exhibitions sometimes assign new titles or names for objects. This is an instance of the [Context Specific Assertions](/model/assertion/#context-specific-assertions) pattern.


