---
title: "Objects: Physical Characteristics"
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction

There are several important physical features of artworks that it is important to capture, including the size, shapes, colors, and the materials that it is made of. The model allows for both being explicit in the data for these, as well as simply including a textual description.  The explicit form is preferred, however it is recognized that not all systems will be able to provide it. 

Beyond dimensions and materials, the model allows for the description of parts of objects, and parts of parts, using the base pattern.  These parts can be thought of as objects in their own right, and thus have titles ("Left Panel" of a triptych), descriptions, rights, images, dimensions, materials, and so forth.   

## Dimensions

The physical dimensions of an object, such as height, width, diameter or weight, are included in the `dimension` property, and consist of three primary pieces of information:  

* The numeric value in `value`.
* The type of dimension (e.g. height vs width) in `classified_as`, referencing an external vocabulary of dimension types.
* The `unit` used to align the value with the real world such as inches, pounds or seconds. The unit should also be given from a controlled vocabulary.

__Example:__

A painting that measures 16 inches wide by 20 inches tall.

```crom
top = Painting(art=1)
top._label = "Example 16x20 Painting"
w = Width(value=16)
w.unit = instances['inches']
top.dimension = w
h = Height(value=20)
h.unit = instances['inches']
top.dimension = h
```

### Dimension Statement

If the dimension text is not recorded in a way that is condusive to generating the full set, then it can be given as a `LinguisticObject`, classifed as dimensions by reference to _aat:300435430_, and the text provided in `content`. This is an example of the Statements base pattern.

__Example:__

The same 16 by 20 inch painting, described only in a human-readable text.

```crom
top = Painting(art=1)
top._label = "Example Painting"
dims = DimensionStatement()
dims.content = "The painting is approximately 16 inches wide, by 20 inches high"
top.referred_to_by = dims
```

### Measurements of Dimensions

In some contexts, it is also important to have more information about how the dimensions were measured. This could be useful, for example, to distinguish the time and method by which the measurement was taken, or to know who used which instrument in a conservation research setting to promote accuracy and reusability of results. 

In order to build upon the dimension model described above, the model adds an `AttributeAssignment` activity to the `Dimension` which is the measuring activity, following the [Assertion](/model/assertion/) pattern. The `Dimension` is `assigned_by` the `AttributeAssignment`, to the object which has the dimension.  In this particular case, as dimensions are specific to the object, and the `dimension` property is explicit in the model already, there is no need to link from the `AttributeAssignment` back to the object, or to give the property that is being assigned. It is permitted, but no new information is being added and hence it is not recommended.

__Example:__

A particular curator measured the painting to be 20 inches high.

```crom
top = Painting(label="Example Painting")
h = vocab.Height(value=20)
h.unit = vocab.instances['inches']
aa = model.AttributeAssignment(label="Measurement of Painting")
h.assigned_by = aa
who = model.Person(label="Curator")
aa.carried_out_by = who
top.dimension = h
```


### Colors

The main colors of an object can be determined and record in two very different ways - by capturing a very specific value for the wavelength of the light or composition of the color (in a Red/Green/Blue colorspace, for example), or categorizing the object into more broader, subjective color types ("pale green", "ochre"). The first approach might be done with instruments measuring the reflected light off the original, or via digital photography and computing the color from the resulting digital image.  The second approach is likely carried out by a curator in describing the object in a collection management system, hopefully using a controlled set of terms. As it is desirable to have only a single place to look for information, the model for color tries to capture both of these possibilities at once in as simple a way as possible, allowing either or both to happen for any given color.

Measurements record a `Dimension`, and thus we create an instance of the class to record the color, even if the measurement is a categorization. The dimension has a `value` and `unit`, just like the more obvious physical dimensions described above. For an RGB colorspace, the value must be converted into an integer from the more traditional three-part hexadecimal value, as values are always decimalized. This allows the true value to be recorded.  The dimension can also be `classified_as` a particular color family -- the object has a color which is a green color, for example. Either or both of these patterns can be used, and multiple dimensions using this pattern can be recorded without having to match up which categories map to which values. 

__Example:__

A green painting has a vivid (`00FF00`) green color, and is also categorized as being green (_aat:300128438_)

```crom
top = Painting(art=1)
top._label = "Example Green Painting"
c = vocab.Color()
c._label = "green"
c.classified_as = vocab.instances['color green']
c.value = 65280
c.unit = vocab.instances['rgb_colorspace']
top.dimension = c
```

!!! note "Implementation Note"

	In order to generate an integer value from a hexadecimal value is typically very easy in most programming languages. In Python, for example, it is simply `int(hex_value, 16)`. The reverse is also true, with the equivalent being `hex(int_value)`. As such, the unobvious value of `65280` is not wonderful from a data-readability perspective, but the implementation is very straightforward and thus the consistency is deemed to provide more usability than having a special case of `value` that takes a string instead of an integer.


## Shapes

While some combinations of dimensions can give a sense of the shape of the object, it is also often useful to be more explicit.  For example, a shield-shaped painting (perhaps due to being painted on an actual shield) would likely still only have height and width given. Without the additional information of the shape, it might be concluded that the painting is rectangular. Similarly, a circular object could be mistaken as a square, as the height and width would be the same in either case.

Shapes are given as classifications on the object via the `classified_as` property.  The classification is then further classified as being a shape, with the term _aat:300056273_, in the same way that being a painting is further classified as being the type of work.

__Example:__

An oval-shaped painting.

```crom
top = Painting(art=1)
top.classified_as = instances['oval']
top._label = "Example Oval Painting"
```

## Materials

Objects are created using different materials, such as canvas or marble.  These are recorded using the `made_of` property on the object directly. The materials are the type of material, rather than the specific bits of matter and therefore refer to entries in external vocabularies.  When possible, it is good to use this model, and combined with the parts model described in the next section, allows for a comprehensive set of information about which parts are which sizes, shapes, colors, and made of which materials.

Note that the type-of-type pattern is not needed for materials, like it is for shape, as they have their own `Material` class that is used to distinguish them.

__Example:__

A statue made of marble.

```crom
top = Sculpture(art=1)
top._label = "Example Marble Sculpture"
top.made_of = instances['marble']
```

### Materials Statement 

Similarly to dimensions statements, it is possible to describe the materials using a `LinguisticObject` classified as being about the materials of the object via _aat:300435429_.

__Example:__

A multi-media painting, with a description of the materials in human-readable text only.

```crom
top = Painting(art=1)
top._label = "Example Multi-Media Painting"
mats = MaterialStatement()
mats.content = "Oil, French Watercolors on Paper, Graphite and Ink on Canvas, with an Oak frame"
top.referred_to_by = mats
```

## Parts

As described in the [baseline patterns](/model/base/), one of the main modeling paradigms used is to separate parts of resources from the whole. Physical objects are particularly amenable to this, and allows reuse of the rest of the model as needed.  The parts do not need to be physically separable without destroying the object, but do need to be objectively definable in terms of the matter that makes it up.  For example, the arm of a sculpture could have dimensions and materials, but while an arch-shaped space in a rock formation might have dimensions, it could not be removed, nor is it made of anything, and thus it is not a part.

Physical parts are given using the `part` property, and use the same `HumanMadeObject` class, as per the full object. The `classified_as` property can be used to be more specific as to the sort of part, in this case the support for the painting, which is in turn made of canvas. The type of part is then further classified as _aat:300241583_ to ensure that it can be distinguished as a part-type, rather than an object-type.

The model does not have a separate parts statement to describe this in a human-readable way, as this is traditionally done using the materials statement as demonstrated above.

__Example:__

A watercolor painting, that has a part which is the support and is made of canvas.

```crom
top = Painting(art=1)
top._label = "Example Painting"
top.made_of = instances['watercolor']
part = SupportPart(top.id + "/part/1")
part._label = "Canvas Support"
part.made_of = instances['canvas']
top.part = part
```

### Sides of an Object

While some artworks can be treated as two dimensional, as the only part of interest is the front of a flat surface such as a painting, drawing or photograph, there are many other objects where it is desirable to record information separately about the front and back, or any number of other sides.

 This pattern allows separate identities for the recto and verso of a page, the obverse and reverse of a coin, in the same manner as the frame or canvas of a painting.  The use of the classification _aat:300133025_ (artwork) is important to distinguish between objects that should be treated as the complete artwork, and objects that are either parts of it, or those that it is part of.

__Example:__

A photograph that depicts the Example Painting, where the image is on the front part, and there is an inscription on the back that reads "Photograph of Example Painting, taken 1932".
The use of the classification of being an artwork applies only to the front of the photograph, and not the back.


```crom
top = vocab.PhotographColor()
top._label = "Photograph of Example Artwork"

recto = vocab.FrontPart(art=1)
recto._label = "Front of Photograph"
verso = vocab.BackPart()
verso._label = "Back of Photograph"
top.part = recto
top.part = verso

what = Painting(art=1)
what._label = "Example Painting"
vi = VisualItem()
vi.represents = what
recto.shows = vi

txt = LinguisticObject()
txt.content = "Photograph of Example Painting, taken 1932"
verso.carries = txt
```
