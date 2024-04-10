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

The Night Watch is 379.5 cm high, by 453.5 cm wide.

```crom
top = vocab.Painting(ident="nightwatch/6", label="Night Watch by Rembrandt")
w = vocab.Width(value=453.5)
w.unit = vocab.instances['cm']
top.dimension = w
h = vocab.Height(value=379.5)
h.unit = vocab.instances['cm']
top.dimension = h
```

### Dimension Statement

If the dimension text is not recorded in a way that is condusive to generating the full set, then it can be given as a `LinguisticObject`, classifed as dimensions by reference to _aat:300435430_, and the text provided in `content`. This is an example of the Statements base pattern.

__Example:__

The dimensions, including weight, of the Night Watch, described in a human-readable text.

```crom
top = vocab.Painting(ident="nightwatch/7", label="Night Watch by Rembrandt")
dims = vocab.DimensionStatement()
dims.content = "height 379.5 cm × width 453.5 cm × weight 337 kg"
top.referred_to_by = dims
```

### Dimension Display Labels

Another method is to have the dimensions in the data include a human readable label for the value that the dimension is representing.  This allows clients to present the data in a particular style, rather than having to generate the text from the dimension value, unit and type.

This same approach can be used on many data structures and is merely being called out here to compare with the machine oriented view of just the data structure, and the human oriented view of just the full description as a statement.

__Example:__

The Night Watch once more, described with human readable labels on each dimension.

```crom
top = vocab.Painting(ident="nightwatch/8", label="Night Watch by Rembrandt")
w = vocab.Width(value=453.5)
w.unit = vocab.instances['cm']
top.dimension = w
h = vocab.Height(value=379.5)
h.unit = vocab.instances['cm']
top.dimension = h
w.identified_by = vocab.DisplayName(value="453.5 cm wide")
h.identified_by = vocab.DisplayName(value="379.5 cm high")
```


### Measurements of Dimensions

In some contexts, it is also important to have more information about how the dimensions were measured. This could be useful, for example, to distinguish the time and method by which the measurement was taken, or to know who used which instrument in a conservation research setting to promote accuracy and reusability of results. 

In order to build upon the dimension model described above, the model adds an `AttributeAssignment` activity to the `Dimension` which is the measuring activity, following the [Assertion](/model/assertion/) pattern. The `Dimension` is `assigned_by` the `AttributeAssignment`, to the object which has the dimension.  In this particular case, as dimensions are specific to the object, and the `dimension` property is explicit in the model already, there is no need to link from the `AttributeAssignment` back to the object, or to give the property that is being assigned. It is permitted, but no new information is being added and hence it is not recommended.

__Example:__

The measurement of the Night Watch was carried out by the "Operation Night Watch" team, during "[Operation Night Watch](https://www.rijksmuseum.nl/en/stories/operation-night-watch)" 

```crom
top = vocab.Painting(ident="nightwatch/9", label="Night Watch by Rembrandt")
h = vocab.Height(value=379.5)
h.unit = vocab.instances['cm']
top.dimension = h
aa = model.AttributeAssignment(label="Measurement of the Night Watch")
h.assigned_by = aa
aa.carried_out_by = model.Group(ident="nightwatchteam", label="Operation Night Watch Team")
aa.part_of = model.Activity(ident="operationnightwatch", label="Operation Night Watch")
```

### Measurement of Object Features

It is common to measure parts of a particular object, such as the base of a statue or the image bearing part of a painting, or the object in a particular state, such as the height of the chest with the lid open rather than with the lid closed. If there is a record for the part, separate from the full object, then the dimension can be associated with that part of the object directly, but it is inconvenient to make separate records for all of the possible aspects that could be measured, and impossible to manage state in this way.

If there isn't a requirement to have multiple dimensions connected, and there isn't an interoperability or searchability requirement to be able to distinguish them computationally, then a display Name or a Statement is likely sufficient to explain to a human reader what was being measured.

If this is a requirement, then instead we add the `technique` property on the `AttributeAssignment` discussed in the previous section as a way to reference the method in which the measurement was taken. The technique would represent, for example, "measuring the base" or "measuring while open". The same technique would be added to each of the measurements for the particular feature -- the height, width, and depth of the statue's base would all have the "measuring the base" technique as a way to connect them together.

/// note | Missing Vocabulary
These techniques are unlikely to exist in shared vocabularies, and implementers are thus very likely to have to create their own based on local practice.
///

__Example:__

Spring has "Framed [Outer Dim]" and "Unframed" dimensions. The "Unframed" height and width are 74 and 51.5cm.

```crom
top = vocab.Painting(ident="spring/29", label="Spring")
h = vocab.Height(value=74)
h.unit = vocab.instances['cm']
top.dimension = h
aa = model.AttributeAssignment(label="Unframed Measuring")
aa.technique = model.Type('measuring_unframed', label="Unframed Measuring")
h.assigned_by = aa
w = vocab.Width(value=51.5)
w.unit = vocab.instances['cm']
top.dimension = w
aa2 = model.AttributeAssignment(label="Unframed Measuring")
aa2.technique = model.Type('measuring_unframed', label="Unframed Measuring")
w.assigned_by = aa2
```


### Colors

The main colors of an object can be determined and record in two very different ways - by capturing a very specific value for the wavelength of the light or composition of the color (in a Red/Green/Blue colorspace, for example), or categorizing the object into more broader, subjective color types ("pale green", "ochre"). The first approach might be done with instruments measuring the reflected light off the original, or via digital photography and computing the color from the resulting digital image.  The second approach is likely carried out by a curator in describing the object in a collection management system, hopefully using a controlled set of terms. As it is desirable to have only a single place to look for information, the model for color tries to capture both of these possibilities at once in as simple a way as possible, allowing either or both to happen for any given color.

Measurements record a `Dimension`, and thus we create an instance of the class to record the color, even if the measurement is a categorization. The dimension has a `value` and `unit`, just like the more obvious physical dimensions described above. For an RGB colorspace, the value must be converted into an integer from the more traditional three-part hexadecimal value, as values are always decimalized. This allows the true value to be recorded.  The dimension can also be `classified_as` a particular color family -- the object has a color which is a green color, for example. Either or both of these patterns can be used, and multiple dimensions using this pattern can be recorded without having to match up which categories map to which values. The traditional hex string for the color can be given as the `content` of an Identifier for the dimension. 

__Example:__

The Night Watch is primarily a brown color (`B35A1F`), which is categorized as being brown (_aat:300127490_)

```crom
top = vocab.Painting(ident="nightwatch/10", label="Night Watch by Rembrandt")
c = vocab.Color(label="brown")
c.identified_by = model.Identifier(content="#B35A1F")
c.classified_as = vocab.instances['color brown']
c.value = 11754015.0
c.unit = vocab.instances['rgb_colorspace']
top.dimension = c
```

!!! note "Implementation Note"

	In order to generate an integer value from a hexadecimal value is typically very easy in most programming languages. In Python, for example, it is simply `int("B35A1F", 16)`. The reverse is also true, with the equivalent being `hex(11754015)`. As such, the unobvious value of `11754015` is not wonderful from a data-readability perspective, but the implementation is very straightforward and thus the consistency with all other dimensions is deemed to provide more usability than having a special case of `value` that takes a string instead of an integer. The string can be carried as an Identifier on the Dimension instance.


## Shapes

While some combinations of dimensions can give a sense of the shape of the object, it is also often useful to be more explicit.  For example, a shield-shaped painting (perhaps due to being painted on an actual shield) would likely still only have height and width given. Without the additional information of the shape, it might be concluded that the painting is rectangular. Similarly, a circular object could be mistaken as a square, as the height and width would be the same in either case.

Shapes are given as classifications on the object via the `classified_as` property.  The classification is then further classified as being a shape, with the term _aat:300056273_, in the same way that being a painting is further classified as being the type of work.

__Example:__

The Night Watch is a landscape format painting, as it is wider than it is high.

```crom
top = vocab.Painting(ident="nightwatch/11", label="Night Watch by Rembrandt")
top.classified_as = vocab.instances['oblong']
```

## Materials

Objects are created using different materials, such as canvas or marble.  These are recorded using the `made_of` property on the object directly. The materials are the type of material, rather than the specific bits of matter and therefore refer to entries in external vocabularies.  When possible, it is good to use this model, and combined with the parts model described in the next section, allows for a comprehensive set of information about which parts are which sizes, shapes, colors, and made of which materials.

Note that the type-of-type pattern is not needed for materials, like it is for shape, as they have their own `Material` class that is used to distinguish them. Note also that materials should be specifically the material of the artwork, rather than the tool used to apply the material. For example, the material should be graphite, not pencil, as pencils can be used as materials to create (very small) sculptures.


__Example:__

The Night Watch is made of oil paint and canvas.

```crom
top = vocab.Painting(ident="nightwatch/12", label="Night Watch by Rembrandt")
top.made_of = vocab.instances['oil']
top.made_of = vocab.instances['canvas']
```

### Materials Statement 

Similarly to dimensions statements, it is possible to describe the materials using a `LinguisticObject` classified as being about the materials of the object via _aat:300435429_.

__Example:__

The Night Watch is "oil on canvas".

```crom
top = vocab.Painting(ident="nightwatch/13", label="Night Watch by Rembrandt")
top.referred_to_by = vocab.MaterialStatement(content="Oil on Canvas")
```

## Parts

As described in the [basic patterns](/model/base/), one of the main modeling paradigms used is to separate parts of resources from the whole. Physical objects are particularly amenable to this, and allows reuse of the rest of the model as needed.  The parts do not need to be physically separable without destroying the object, but do need to be objectively definable in terms of the matter that makes it up.  For example, the arm of a sculpture could have dimensions and materials, but while an arch-shaped space in a rock formation might have dimensions, it could not be removed, nor is it made of anything, and thus it is not a part.

Physical parts are linked to the whole using the `part_of` property, and use the same `HumanMadeObject` class. The `classified_as` property can be used to be more specific as to the sort of part, in this case the support for the painting, which is in turn made of canvas. The type of part is then further classified as _aat:300241583_ to ensure that it can be distinguished as a part-type, rather than an object-type.

The model does not have a separate parts statement to describe this in a human-readable way, as this is traditionally done using the materials statement as demonstrated above.

__Example:__

The support part of the Night Watch is made of canvas, and part of the Night Watch.

```crom
top = vocab.SupportPart(ident="nightwatch/support", label="Support of Night Watch")
top.made_of = vocab.instances['canvas']
top.part_of = model.HumanMadeObject(ident="nightwatch", label="Night Watch by Rembrandt")
```

### Sides of an Object

While some artworks can be treated as two dimensional, as the only part of interest is the front of a flat surface such as a painting, drawing or photograph, there are many other objects where it is desirable to record information separately about the front and back, or any number of other sides.

This pattern allows separate identities for the recto and verso of a page, the obverse and reverse of a coin, in the same manner as the frame or canvas of a painting.  The use of the classification _aat:300133025_ (artwork) is important to distinguish between objects that should be treated as the complete artwork, and objects that are either parts of it, or those that it is part of.

__Example:__


On the back of Manet's "Spring" is an inscription "11505F".

```crom
top = vocab.BackPart(ident="spring/back", label="Back of Spring by Manet")
top.part_of = model.HumanMadeObject(ident="spring", label="Jeanne (Spring) by Manet")
top.referred_to_by = vocab.InscriptionStatement(content="11505F")
```

### Number of Parts

Some objects have a much higher number of parts than others, and it would be impractical to describe them all independently. For example, a chess set might consist of 33 parts (the board, the 16 white pieces, the 16 black pieces), whereas a vase that has been shattered might consist of hundreds of fragments. It is possible, using the `dimension` pattern described above, to record the number of parts of an object regardless of whether they are described individually or not.

__Example:__

"Vessel with miniature chess set" by Michael Mode consists of 36 parts (the 32 pieces, the board, a lid, and two other parts)

```crom
top = model.HumanMadeObject(ident="chess/1", label="Miniature Chess")
top.identified_by = vocab.PrimaryName(content="Vessel with miniature chess set")
dim = model.Dimension()
dim.value = 36
dim.unit = model.MeasurementUnit(ident="http://vocab.getty.edu/aat/300241583", label="Components")
dim.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300404433", label="Count")
top.dimension = dim
```
