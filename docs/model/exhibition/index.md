---
title: "Exhibitions"
---

[TOC]

## Introduction

Exhibitions are very common activity that involves artwork owned by many different organizations being displayed together, often with additional contextual information linking the pieces together.  The exhibition is often presented at different venues over time, and might be part of a series such as the World's Fairs or annual exhibitions.

## Exhibition Concept

The model distinguishes between the concept of the exhibition and the activity that makes that concept real.  The concept is created by the people who originally think up the exhibition, long before any of the pieces are collected together.  The exhibition concept likely has some theme that results in a coherent set of objects being presented, which could be as complex as post-industrial life or as  simple as the life's work of a particular artist.

The concept is modeled as a `PropositionalObject`, and `classified_as` _aat:300417531_ to ensure that it's clearly tagged as an exhibition. It can have all of the affordances of any concept, such as names, identifiers, references, relationships and more.

```crom
top = vocab.ExhibitionIdea()
top._label = "Example Exhibition"
id1 = Identifier()
id1.content = "exh-2010-eg-a"
top.identified_by = id1
nm = Name()
nm.content = "Example Exhibition"
top.identified_by = nm
typ = instances['gender issues']
top.about = typ
cre = Creation()
cur = Person()
cur._label = "Curator"
cre.carried_out_by = cur
top.created_by = cre
ex = Exhibition()
ex._label = "Exhibition at Venue"
top.motivated = ex
```

## Exhibition Activity

There is an activity, as described in the section on [Provenance](/model/provenance/), which is the exhibiting of the objects.  In particular, the public exhibition takes place at a certain time given in `timespan`, at a certain place or places given in `took_place_at`, and was organized by some actor or actors, likely organizations, given in `carried_out_by`. It can be recognized as an exhibition using the classification of _aat:300054766_, "exhibitions".

```crom
top = Exhibition()
top._label = "Example Exhibition"
ts = TimeSpan()
ts.begin_of_the_begin = "2010-08-01"
ts.end_of_the_end = "2011-06-01"
top.timespan = ts
mus = MuseumPlace()
mus._label = "Example Museum's Location"
top.took_place_at = mus
mus2 = MuseumOrg()
mus2._label = "Example Museum"
top.carried_out_by = mus2
```

## Multiple Venues

Some exhibitions are shown at different locations over time, moving from one museum or exhibition hall to another.  In this case, each of the different locations is treated as an exhibition in its own right, and then a broader "travelling exhibition" _(aat:300054773)_ is created that these are part of.  Note that the travelling exhibition can have separate properties from its parts, such as a `label` to distinguish the joint nature and a broader `timespan` that covers all of the venues. There is no need to duplicate the organizations and locations in the travelling exhibition, these can be determined more easily by looking at the exhibitions that it consists of.

```crom
top = MultiExhibition()
top._label = "Example Travelling Exhibition at Two Museums"
ts = TimeSpan()
ts.begin_of_the_begin = "1980-10-01"
ts.end_of_the_end = "1981-08-14"
top.timespan = ts
exh = Exhibition()
exh._label = "Exhibition at Museum 1"
ts2 = TimeSpan()
ts2.begin_of_the_begin = "1980-10-01"
ts2.end_of_the_end = "1981-03-01"
exh.timespan = ts2
exh2 = Exhibition()
exh2._label = "Exhibition at Museum 2"
ts3 = TimeSpan()
ts3.begin_of_the_begin = "1981-03-14"
ts3.end_of_the_end = "1981-08-14"
exh2.timespan = ts3
top.part = exh
top.part = exh2
```

## Objects 

The collection of art objects on display at exhibitions can be listed from the Exhibition with the property `used_specific_object`. The model for the set of objects that make up the content of the exhibition is the same as the model for permanent collections -- the objects are collected together into an `Aggregation`, which is the object used by the Exhibition.  

For the travelling exhibitions described above, a different collection of objects should be referenced from each of the venues.  Objects are frequently added or removed for the venue, and each venue will likely have its own context specific information such as descriptions or labels.  The top level activity representing the overall exhibition does not have its own Aggregation in the travelling exhibition case.

```crom
top = Exhibition()
top._label = "Example Exhibition"
agg = model.Set()
obj = Painting(art=1)
obj._label = "Painting"
obj2 = Painting(art=1)
obj2._label = "Another Painting"
obj3 = Sculpture(art=1)
obj3._label = "Sculpture"
agg.member = obj
agg.member = obj2
agg.member = obj3
top.used_specific_object = agg
```

### Exhibition Provenance: Transfer of Custody

As objects used for exhibitions frequently come from many different organizations, it is useful and interesting to track the custody of the object as well as the ownership.  This `TransferOfCustody` event is modeled in the same way as other [Provenance](/model/provenance/) changes.  

For each exhibition, the custody of the object is transferred from the previous custodian to the next. In the simple case of a single venue for the exhibition, the first transfer is likely to be from the owner to the organization responsible for the exhibition, and then at the end of the exhibition, the custody is transferred back again.  In a more complex scenario with multiple venues, each organization hosting the exhibition will likely transfer custody to the next in the sequence.  Unlike regular provenance transfers, these happen for a specific purpose ... the exhibition.  This is added to the model with the `specific_purpose` property.

```crom
top = TransferOfCustody()
top._label = "Custody Transfer of Painting for Exhibition"
exh = Exhibition()
exh._label = "Example Exhibition"
obj = Painting(art=1)
obj._label = "Painting"
mus = MuseumOrg()
mus._label = "Exhibiting Museum"
owner = MuseumOrg()
owner._label = "Owning Museum"
top.transferred_custody_of = obj
top.transferred_custody_to = mus
top.transferred_custody_from = owner
top.specific_purpose = exh
agg = model.Set()
agg.member = obj
exh.used_specific_object = agg
exh.carried_out_by = mus
obj.current_owner = owner
```

### Exhibition Provenance: Internal Moves

Conversely to the previous section, when the object being exhibited at the location is owned by the same organization, there is no transfer of custody. The equivalent activity is likely to be simply moving the object from its regular location to the exhibition space.  If the exhibition location is not known, then there is no need to provide the `moved_to` and `moved_from` relationships for the `Move` activity.

```crom
top = Move()
top._label = "Move of object for exhibition"
exh = Exhibition()
exh._label = "Example Exhibition"
obj = Painting(art=1)
obj._label = "Example Painting"
mus = MuseumOrg()
mus._label = "Exhibiting Museum"
agg = model.Set()
agg._label = "Set of Exhibited Objects"
top.moved = obj
top.specific_purpose = exh
obj.current_owner = mus
agg.member = obj
exh.used_specific_object = agg
exh.carried_out_by = mus
top.carried_out_by = mus
```


### Exhibition Specific Labels

The curators for exhibitions sometimes assign new labels or names for objects, for example to ensure that they follow an established pattern for the exhibition, rather than following that of the owning organization or person, if any.  This activity of assigning a title to the object is part of the exhibition via the `part` property, and assigns a new `Name` to the object. This separation of the name from the object via the `AttributeAssignment` ensures that the `Name` does not directly end up in the set of titles for the object without further intervention.  As with any activity, the assignment can also be `carried_out_by` an actor, and have a timespan for when it was assigned.  This is an instance of the [Context Specific Assertions](/model/assertion/#context-specific-assertions) pattern.

```crom
top = Exhibition()
top._label = "Example Exhibition"
agg = model.Set()
top.used_specific_object = agg
obj = Painting(art=1)
obj._label = "Real Painting Name"
agg.member = obj
aa = AttributeAssignment()
aa.assigned_property = "identified_by"
name = Name()
name.content = "Exhibition Specific Name"
aa.assigned = name
aa.assigned_to = obj
curator = Person()
curator._label = "A. Curator"
aa.carried_out_by = curator
aa.involved = agg
top.part = aa
```

### Depiction of the Object at the Exhibition

There are often photographs of the object as displayed in the exhibition. These are representations of the object regardless, and hence can be associated directly with the object rather than via an `AttributeAssignment`. The description of the image therefore follows the same pattern as other [digital representations of the object](/model/object/digital/), but like the label example above, it occurred as part of the exhibition.

The same pattern of having the creation of the image as part of the exhibition activity does not suffice, as the image could be a digital reproduction of physical photograph, created much later than the exhibition.  Secondly, the creation of the photograph was very likely not carried out as part of carrying out the exhibition by the museum, it could easily have been taken by a visitor. 

Instead, we associate the image with a `Proxy` resource that stands for the object in the context of the Aggregation of objects used by the Exhibition ... the image is a representation of the object in that context.

FIXME

```crom
top = Exhibition()
top._label = "Example Exhibition"
obj = Painting(art=1)
obj._label = "Painting"
agg = model.Set()
agg.member = obj
top.used_specific_object = agg
#img = DigitalImage("http://example.org/images/object-at-exhibition.jpg")
#obj.representation = img
#proxy = Proxy()
#proxy.proxyFor = obj
#proxy.proxyIn = agg
# proxy.representation = img
#img.represents = proxy
```

