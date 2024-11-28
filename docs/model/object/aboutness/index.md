---
title: "Objects: Aboutness"
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

The features described in this section are information _about_ the object, and are mostly interpretive rather than absolute.  For example, any number of accurate descriptions of an object could be provided without invalidating the others, whereas only a single set of dimension measurements can be correct at a given time.

## Description

The main description of the object is provided in the same manner as other such texts; as the `content` of a `LinguisticObject` resource.  The recommended classification for descriptions is _(aat:300435416)_.  The description can include any content that describes the object, and is useful primarily for display to a human user. Note that the description of artworks are often about the image shown or the object's visual content, and less about the physicality of the object itself, however it is typically impossible to distinguish between them in current collection management systems. The visual content is described by a `VisualItem`, as explained below.

__Example:__

Spring by Manet has a description, explaining the object and its image.

```crom
top = model.HumanMadeObject(ident="spring/5", label="Jeanne (Spring) by Manet")
top.referred_to_by = vocab.Description(content="A chic young woman in a day dress with floral accents holds a parasol against a background of exuberant foliage.")
top.shows = model.VisualItem(ident="spring", label="Visual Content of Spring")
```

## Physical Object and Visual Work

Physical things are the carriers of intellectual works, either visual works or textual works. The same visual work can be carried by many physical things, such as multiple copies (editions) of a print or photograph. Multiple copies of a painting intentionally created to look the same would show the same visual work.  It can be thought of as the image or visual impression that the object gives when looking at it, regardless of the materiality of the object. The Mona Lisa as a Work is instantly recognizable on a t-shirt as "the Mona Lisa", even though the painting in the Louvre is clearly a very different physical item. Similarly the same physical item might carry multiple visual works, such as a painting with a sketch on the reverse.

Every human-made object with an intent to look a certain way is the carrier of a visual work, and could be a primarily two dimensional artwork such as a painting, a three dimensional artwork such as a statue, or a crafted three dimensional object such as armor, a plate, or a building.

This visual work is modeled as a `VisualItem` resource, associated with the `HumanMadeObject` instances via the `shows` property. The `VisualItem` then has various properties described below that are used to describe the different facets.

### Depiction

Many sorts of artwork depict things that can be pointed out in the artwork. These could be identifiable entities, such as a known Person or Object with a name or identifier, or unidentifiable (perhaps fictional) instances of a class of entity, such as a depiction of a battle but not any particular battle.  For example a portrait depicts the person sitting for it, or a sketch of a generic landscape depicts a place even if it's not a specific known location. The depiction pattern describes _what_ is in the artwork's image.

This is modeled using the `represents` property on the `VisualItem`, which refers to the entity that is being depicted.
 
__Example:__

The image of Manet's Spring represents (or depicts) Jeanne Demarsy, a French actress.

```crom
top = model.VisualItem(ident="spring/1", label="Visual Content of Spring")
top.represents = model.Person(ident="jeanne", label="Jeanne Demarsy")
```

### Depictions of Unidentified Instances

Still life paintings, photographs and many other artworks depict things which we can recognize by type or classification, but not as unique or individual entities in reality. A photograph of an unknown beach clearly depicts a beach, but in the same way that we do not create individual records for unidentified people, we do not need to create a Place for the beach.  Instead, we can use `represents_instance_of_type` as a shortcut directly to the classification of "beach". The same applies for people (depicts an instance of "child"), objects (depicts an instance of "bicycle"), and so forth.

__Example:__

The painting Spring also depicts a parasol which, of course, does not have its own identity.

```crom
top = model.VisualItem(ident="spring/5", label="Visual Content of Spring")
top.represents_instance_of_type = model.Type(ident="http://vocab.getty.edu/aat/300046218", label="Parasol")
```

### Subject

Subjects are the concepts or things that the artwork evokes, as opposed to an object (real or imaginary) that is depicted by the artwork.  For example, a portrait of a military commander in full regalia on a battlefield depicts the person and the place, but could be interpreted to have a subject of "war". A painting with an allusion to a piece of literature does not depict the literature, but instead evokes it as a subject. This could be thought of as what the artwork is _about_ rather than what can be seen, or as _why_ the content in the artwork is present.

The model for subjects is that the `VisualItem` is `about` the subject, which is a `Type` instance.

__Example:__

Manet's Spring is about the season spring.

```crom
top = model.VisualItem(ident="spring/2", label="Visual Content of Spring")
top.about = model.Type(ident="http://vocab.getty.edu/aat/300133097", label="Spring (season)")
```


### Style Classification

Styles are a categorization of the aesthetic qualities of the work being described, and can come from important features, techniques, locations, times or artistic movements.  Styles might include "geometric", "abstract", and "limited palette". It is considered that all styles are aesthetic rather than cultural, but the aesthetic style may be related to a particular culture. 

The distinction that all styles are aesthetic is somewhat controversial, but simplifies the model significantly at very little cost. A clear example is a perfect imitation of a Navajo dream-catcher made by a factory in China cannot be said to be culturally Navajo as an object, but the image of the object can be said to have an aesthetic that is related to the Navajo culture.

The style is associated with the object using the `classified_as` property, and must be a reference to an appropriate vocabulary. It is associated with the `VisualItem` that is shown by the object, to reinforce that it is the way the object looks that determines the style, not the physicality of its production.  The style could be thought of as _how_ the content is presented.  In order to distinguish styles from other classifications, the style itself has a `classified_as` of _aat:300015646_.

__Example:__

Manet's Spring is in an impressionist style.

```crom
top = model.VisualItem(ident="spring/3", label="Visual Content of Spring")
top.classified_as = vocab.instances['style impressionism']
```

### Other Classifications

Other classifications can also be assigned to the object's content. If it is possible to say that "the artistic content of this object is an X", then X can be included in the set of classifications using the `classified_as` property on the `VisualItem`.  This could include classifications such as "Landscape", "Genre", "Portrait" or "Allusion", compared to classifications that are derived from the physical nature of the object such as a "Painting", "Photograph" or "Sculpture" which are associated with the object.  

__Example:__

Spring's visual appearance is classified as a Portrait.

```crom
top = model.VisualItem(ident="spring/4", label="Visual Content of Spring")
top.classified_as = vocab.instances['content portrait']
```

## Textual and Visual Works

While the primary use case for Linked Art is visual works, there is also a universal need to be able to describe textual works: works containing content in a human readable language. Some works are solely textual (which we call linguistic), and some are solely visual. A single object might carry more than one visual work, and/or more than one textual work. There can also be single works that have both visual and textual components, but cannot be separated. For example, a poster with specific layout, fonts, colors and other stylistic choices cannot truly separate the linguistic from the visual.

### Inscriptions and Signatures

The most common textual content that is carried by primarily image based works is an inscription or a signature.  The easiest way to represent this information is to provide a Statement on the object that conveys a description and content of the inscription or signature.

It is possible to convey detailed, structured information about important inscriptions by following the model described in the following sections. This would treat the inscription as its own identifiable entity with a `LinguisticObject` record. That entity can have a `Creation`, a `Language`, and be `carried_by` either the full physical object or a part of it. In the case of signatures that are part of the image, then the signature's `LinguisticObject` can be `part_of` the `VisualItem`. While it is infrequent that this level of detailed description is either available or necessary, it is feasible to convey.

__Example:__

The Night Watch has a signature statement:

```crom
top = model.HumanMadeObject(ident="nightwatch/18")
top.referred_to_by = vocab.SignatureStatement(content="signature and date: ‘Rembrandt f 1642’")
```

### Objects Carrying Textual Works

The description of textual works are covered in detail in the [Document](../../document/) section of the model. 


### Single Object, Multiple Works

A single object might carry both significant textual content and separate visual works. For example an exhibition catalog carries its text and, via its illustrations, the visual content of the objects that were exhibited. In this case we could simply list each of the works.

__Example:__

A copy of the [exhibition catalog](https://lccn.loc.gov/80013795) for the "Post-Impressionism: Cross-Currents in European and American Painting 1880-1906", at which Manet's "Spring" (from the Getty) and Cezanne's "Houses in Provence" (from the [National Gallery](https://www.nga.gov/collection/art-object-page.54129.html)) were exhibited, shows both works and carries its own text.

```crom
top = vocab.ExhibitionCatalog(ident="catalog/1", label="Copy of Exhibition Catalog")
top.carries = model.LinguisticObject(ident="catalogtext", label="Exhibition Catalog Text")
top.shows = model.VisualItem(ident="spring", label="Visual Content of Spring")
top.shows = model.VisualItem(ident="houses", label="Visual Content of Houses in Provence")
```


### Single Object, Single Textual and Visual Work

However, in the poster or magazine cover case, there is only a single work that has both important visual and textual attributes. In this case we do not want to give the impression that they are separate and instead use the partitioning pattern.

__Example:__

"Harper's January" at the [Yale University Art Gallery](https://artgallery.yale.edu/collections/objects/11254) is a print by Edward Penfield that has both significant text and visual content. As there is visual content which is not text, but all text is necessarily visual, the textual content is `part_of` the visual content.

```crom
top = vocab.Print(ident="harpers/1", label="Poster Item")
vi = model.VisualItem(ident="harpers", label="Visual Content of Harpers")
top.shows = vi
```

```crom
top = model.VisualItem(ident="harpers/1", label="Visual Content of Harpers")
top.represents = model.Type(ident="http://vocab.getty.edu/aat/300025943", label="Woman")
top.referred_to_by = vocab.Description(content="The text and image are primarily red and black")
```

```crom
top = model.LinguisticObject(ident="harpers/1", label="Textual component of Harpers")
top.content = "Harper's. January contains Roden's corner. A Novel by Henry Seton Merriman [...]"
top.part_of = model.VisualItem(ident="harpers", label="Visual Content of Harpers")
```

## Related Objects

A list of related objects is often known for any given object, however the reason for the relation is not recorded. These objects might be physically similar, they may have been created by the same artist, they might have been exhibited together or they might just be both highlights of the current institution and share no observable features. In this circumstance, the best that can be done is to record that there is some relationship without any specificity as to the details.  If there are more details known about the relationship then more specific patterns should be used instead.

The model uses an `AttributeAssignment` activity to relate the two objects together. This allows additional information to be associated with the activity, such as a label, name or classification if known. The pattern is fully documented in the [assertion](../../assertion/) section of the documentation.




