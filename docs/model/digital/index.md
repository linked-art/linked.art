---
title: "Digital Integration"
up_href: "/model"
up_label: "Model"
---

[TOC]

## Introduction

It is very unlikely that the descriptions provided in this model are the only digital representations of the entities that they describe.  For building human-readable views, or just for linking to existing web pages, these other digital resources should also be referenced.  This section describes how to link those digital resources, such as images and web pages, into the Linked Art descriptions of the entities.


## Digital Objects

All Digital Objects share some basic characteristics, regardless of their particular nature.  The [basic patterns](/model/base/) of Name, Identifier, Classification, and Statement all apply in the regular way. Beyond the baseline, digital objects can have the following descriptive features:

* Access Point - The URLs where the object is available. These may also treated as Digital Objects in their own right, but typically only the URL is given.
* Format - The `format` of a digital object is its media type, often called a MIME type, given as a string
* Standard - Many digital objects further conform to standard specifications, which can be referenced using the `conforms_to` property. This differs from `format`, as there may not be a media type for the specification, and from `classified_as` which is a broader classification (Image, rather than conforming to the standard for JPEG 2000)
* Dimensions - Digital dimensions follow the same pattern as [physical dimensions](/model/object/physical/#dimensions), but might use different types (file size) or the same (height, width for images) and different units (bytes, pixels).
* Creation - Digital Objects are created by `Creation` events rather than `Production` events, but otherwise have the same activity model.


__Example:__

A web page was created by a Museum Education department using the HTML format (and standard), is 100k in size, and is available on the museum website.

```crom
top = vocab.WebPage(ident="auto int-per-segment", label="Digital Object")
top.access_point = model.DigitalObject("https://www.eg.museum/edu/page1.html")
top.format = "text/html"
top.conforms_to = model.InformationObject("http://w3.org/TR/html")
top.identified_by = model.Name(content="Informative Web Page")
dim = model.Dimension(label="100 kb")
dim.unit = vocab.instances['kilobytes']
dim.value = 100
dim.classified_as = model.Type(ident="aat:300265863", label="File Size")
top.dimension = dim
cre = model.Creation()
cre.carried_out_by = model.Group(label="Museum Education Department")
ts = model.TimeSpan()
ts.begin_of_the_begin = "2007-01-20T13:53:00Z"
ts.end_of_the_end = "2007-01-20T13:54:00Z"
cre.timespan = ts
top.created_by = cre
```


## Digital Images

Many of the entities that are described using Linked Art will have digital images that depict them. These images are useful for building compelling user interfaces for the data, and often take a prominent position in those interfaces.

One image might show many different entities, of different types.  An image of an artist standing next to one of her paintings would show both the artist (a `Person`) and the painting (a `HumanMadeObject`).  Further, the same image might be shown by many digital copies and derivatives, each available at a different URL. The same image might also be shown by a physical object, either by printing a digital file or that the digital image is a digitization of the physical object. 

In order to accommodate these relationships, the model for digital objects echos the [physical object / visual work](/model/object/aboutness/) distinction. In particular, digital images `digitally_show` a `VisualItem`. The different entities in the model can then have a Visual Item as a `representation`, meaning that the visual item depicts the entity in its content. As the image might have many different URLs from which it is available, it has an `access_point` property that lists those URLs.

__Example:__

A Person (E.G. Person) is depicted in a digital image, and thus has a representation in the visual item which is digitally shown by the image.


```crom
top = model.Person(ident="auto int-per-segment", label="E.G. Person")
vi = model.VisualItem()
img = vocab.DigitalImage(label="Image of Person")
img.format = "image/jpeg"
img.access_point = model.DigitalObject("http://example.org/egperson/image.jpg")
top.representation = vi
vi.digitally_shown_by = img
```

### Digital Surrogates

Some digital representations are intended to be faithful reproductions of a physical object.  Especially when digitizing two dimensional works, it is useful to distinguish between a digital image that depicts the object but perhaps along with other objects, people and the surroundings, compared to a digital image which shows only the same visual content as the physical object. The basic digital model and image model are the same as above, however we can be more explicit that the same visual item that the physical object `shows` is also `digitally_shown_by` the digital image.  

These images are sometimes called "Digital Surrogates", as they can stand in for the physical object. A digital surrogate might show more than just the object, such as a color strip and a ruler, however the main focus of the visual item must clearly be the object itself. The line between surrogate and depiction is left to the policies and practices of the implementing organizations.

__Example:__

The same visual item is shown by both the physical painting, and the digitized image of the painting.

```crom
top = vocab.Painting(ident="auto int-per-segment", art=1)
top._label = "Painting"
vi = model.VisualItem()
img = vocab.DigitalImage()
img._label = "Digitized Image of Painting"
img.format = "image/jpeg"
img.access_point = model.DigitalObject("http://example.org/painting/image.jpg")
top.shows = vi
vi.digitally_shown_by = img
```


## Home Page

Another very common scenario is that there is a web page about the object, perhaps managed by a collections management system. For humans, this page is much more useful than the data intended for machines.  It can be referenced with the `subject_of` property, and points to a `DigitalObject` which is `classified_as` a web page, or _aat:300264578_.  As with digital images, the home page can have a `format` of "text/html" and other properties.

```crom
top = vocab.Painting(ident="auto int-per-segment", art=1)
top._label = "Painting"
page = vocab.WebPage()
page._label = "Homepage for Painting"
page.format = "text/html"
page.access_point = model.DigitalObject("http://example.org/collection/1/painting/index.html")
top.subject_of = page
```

## Other Pages

While the publishing organization might have a home page for their object as above, there are likely to be many other web pages about the object as well in different systems.  These pages follow the same model of being a `DigitalObject`, but instead use the `referred_to_by` property for the link in the same manner as other texts. 

```crom
top = vocab.Painting(ident="auto int-per-segment", art=1)
top._label = "Painting"
page = vocab.WebPage()
page._label = "Webpage that discusses Painting, but is not its homepage"
page.format = "text/html"
page.access_point = model.DigitalObject("http://example.org/journal/article")
top.referred_to_by = page
```

## IIIF 

[IIIF](http://iiif.io/), the International Image Interoperability Framework, is an increasingly common way to make images and descriptions intended to be displayed to humans available. There are two primary alignments with the Digital Object model.

### IIIF Images

The [IIIF Image API](http://iiif.io/api/image/) is a `DigitalService` from which various derivatives of the image content can be requested. Similarly to the `access_point` property used in the previous sections, this service is referenced via the `digitally_available_via` property from the core `DigitalObject` that represents the digital image.  The same image might have both access points and image services.

The IIIF Image service should have a `conforms_to` property that refers to "http://iiif.io/api/image" as the URI of an `InformationObject`, so that applications know what sort of service is being referred to.

__Example:__

A sculpture is digitized, and the image content made available through IIIF. 

```crom
top = vocab.Sculpture(ident="auto int-per-segment", label="Sculpture", art=1)
img = model.VisualItem(label="Visual content shown by sculpture")
top.shows = img
do = vocab.DigitalImage()
img.digitally_shown_by = do
do.access_point = model.DigitalObject("http://example.org/iiif/img/full/max/0/default.jpg")
svc = model.DigitalService()
svc.access_point = model.DigitalObject("http://example.org/iiif/img")
svc.conforms_to = model.InformationObject("http://iiif.io/api/image")
do.digitally_available_via = svc
```

### IIIF Manifests 

The [IIIF Presentation API](http://iiif.io/api/presentation/) is considered to be a `DigitalObject` that is about the object, in the same way as the home page of the object in a collection information system.  The property used to refer to it from the object is, thus, `subject_of`.  The `conformsTo` property should also be used with the Presentation API URI, and the Digital Object can also be given a `format` for JSON-LD.

```crom
top = vocab.Painting(ident="auto int-per-segment", label="Painting", art=1)
mfst = model.DigitalObject("http://iiif.example.org/presentation/1/manifest.json")
mfst.format = 'application/ld+json;profile="http://iiif.io/api/presentation/3/context.json"'
mfst.conforms_to = model.InformationObject("http://iiif.io/api/presentation")
top.subject_of = mfst
```
