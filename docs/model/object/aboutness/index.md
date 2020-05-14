---
title: "Objects: Aboutness"
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

The features described in this section are information _about_ the object, and are mostly interpretive rather than absolute.  For example, any number of accurate descriptions of an object could be provided without invalidating the others, whereas only a single set of dimension measurements can be correct at a given time.

## Description

The main description of the object is provided in the same manner as other such texts; as the `content` of a `LinguisticObject` resource.  The classification for descriptions is _(aat:300411780)_.  The description can include any content that describes the object, and is useful primarily for display to a human user.

__Example:__

A painting the has the description "The Example Painting is a great example of exampleness".

```crom
top = Painting(art=1)
top._label = "Example Painting"
desc = Description()
desc.content = "The Example Painting is a great example of exampleness."
top.referred_to_by = desc
```

## Physical Object and Visual Work

Physical things are the carriers of intellectual works, be they visual works or textual works. The same visual work can be carried by many physical things, such as multiple copies (editions) of a print or photograph. Even multiple copies of a painting created manually to look the same would show the same visual work.  It can be thought of as the image or impression that the object gives when looking at it. 

Every human-made object with an intent to look a certain way is the carrier of a visual work, be that a two dimensional artwork such as a painting, a three dimensional artwork such as a statue, or a crafted three dimensional object such as armor, a plate, or a building.

This visual work is modeled as a `VisualItem` resource, associated with the `HumanMadeObject` instances via the `shows` property. The `VisualItem` then has various properties described below that are used to describe the different facets.

### Depiction

Many sorts of artwork depict things that can be pointed out in the artwork. These could be identifiable entities, such as a known Person or Object with a name or identifier, or unidentifiable (perhaps fictional) instances of a class of entity, such as a depiction of a battle but not any particular battle.  For example a portrait depicts the person sitting for it, or a sketch of a generic landscape depicts a place even if it's not a particular, known location. The depiction pattern describes _what_ is in the artwork's image.

This is modeled using the `represents` property on the `VisualItem`, which refers to the entity that is being depicted.
 
__Example:__

A self portrait is both produced by the artist and has visual content that represents the artist.

```crom
top = Painting(art=1)
top._label = "Self Portrait"
who = Actor()
who._label = "Artist"
vi = VisualItem()
top.shows = vi
vi.represents = who 
prd = Production()
prd.carried_out_by = who
top.produced_by = prd
```

### Subject

Subjects are the concepts or things that the artwork evokes, as opposed to an object (real or imaginary) that is depicted by the artwork.  For example, a portrait of a military commander in full regalia on a battlefield depicts the person and the place, but could be interpreted to have a subject of "war". A painting with an allusion to a piece of literature does not depict the literature, but instead evokes it as a subject. This could be thought of as what the artwork is _about_ rather than what can be seen, or as _why_ the content in the artwork is present.

The model for subject is that the `VisualObject` is `about` the subject, which is a `Type` instance.

__Example:__

A visual content of a portrait of Lord Nelson has the conceptual subject of "war". It would also represent Lord Nelson, following the example above, however this is not included in the example.

```crom
top = Painting(art=1)
top._label = "Portrait of Lord Nelson"
vi = VisualItem()
top.shows = vi
vi.about = instances['war']
```


### Style Classification

Styles are a categorization of the aesthetic qualities of the work being described, and can come from important features, techniques, locations, times or artistic movements.  Styles might include "geometric", "abstract", and "limited palette". It is considered that all styles are aesthetic rather than cultural, but the aesthetic style may be related to a particular culture. 

The distinction that all styles are aesthetic is somewhat controversial, but simplifies the model significantly at very little cost. A clear example is a perfect imitation of a Navajo dream-catcher made by a factory in China cannot be said to be culturally Navajo as an object, but the image of the object can be said to have an aesthetic that is related to the Navajo culture.

The style is associated with the object using the `classified_as` property, and must be a reference to an appropriate vocabulary. It is associated with the `VisualItem` that is shown by the object, to reinforce that it is the way the object looks that determines the style, not the physicality of its production.  The `style` property could be thought of as _how_ the content is presented.  In order to distinguish styles from other classifications, the style itself has a `classified_as` of _aat:300015646_.

__Example:__

An impressionist painting is classified as impressionism, which is classified as being a type of style.

```crom
top = Painting(art=1)
top._label = "Example Impressionist Painting"
vi = VisualItem()
top.shows = vi
vi.classified_as = instances['style impressionism']
```

### Other Classifications

Other classifications can also be assigned to the object's content. If it is possible to say that "the artistic content of this object is an X", then X can be included in the set of classifications using the `classified_as` property on the `VisualItem`.  This could include classifications such as "Landscape" or "Allusion", compared to classifications that are derived from the physical nature of the object such as a "Painting", "Photograph" or "Sculpture" which are associated with the object.  

```crom
top = Painting(art=1)
top._label = "Example Allusion Painting"
vi = VisualItem()
top.shows = vi
vi.classified_as = instances['allusion']
```

## Related Objects

A list of related objects is often known for any given object, however the reason for the relation is not recorded. These objects might be physically similar, they may have been created by the same artist, they might have been exhibited together or they might just be both highlights of the current institution and share no observable features. In this circumstance, the best that can be done is to record that there is some relationship without any specificity as to the details.  If there are more details known about the relationship then more specific patterns should be used instead.

The model uses an `AttributeAssignment` activity to relate the two objects together. This allows additional information to be associated with the activity, such as a label, name or classification if known.  The relationship has a direction, slightly paradoxically from the entity which has an `attributed_by` property to the `AttributeAssignment`, to the entity which is `assigned`. The property can be given using `assigned_property`, with the value being the name of the property.


__Example:__

Example Painting is related, in some unknown way, to Yet Another Example Painting. Perhaps the relationship is that they are both examples.

```crom
top = Painting(art=1, label="Example Painting")
p2 = Painting(art=1, label="Yet Another Example Painting")
aa = AttributeAssignment()
aa.assigned = p2
top.attributed_by = aa
```
