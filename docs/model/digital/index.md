---
title: "Digital Integration"
up_href: "/model"
up_label: "Model"
---

[TOC]

## Introduction

It is very unlikely that the descriptions provided in the Linked Art model are the only digital representations of the entities that they describe. There are also digital images, web pages, and other related content that should be referenced from the descriptions of the entities. The digital object may be also be the entity of interest, such as an eBook, net art, or a digital installation. This section describes how to describe and link digital resources in the Linked Art model.

Digital objects are generally treated in the same way as physical objects -- they are carriers of information, not the information itself. The information is described by a [work](/model/object/aboutness/) that is then digitally carried or shown by the digital object. This ensures that a digital facsimile and the physical object itself are both related to the same information. For example, a PDF (a `DigitalObject`) and a printed copy (a `HumanMadeObject`) of that PDF both carry exactly the same textual content (a `LinguisticObject`).


## Core Digital Object Properties

All Digital Objects share some basic characteristics, regardless of their particular nature.  The [basic patterns](/model/base/) of Name, Identifier, Classification, and Statement all apply in the regular way. Beyond the baseline, digital objects can have the following descriptive features:

* Access Point - The URLs where the actual file itself is available. The URL is given the `type` of `DigitalObject` for consistency, but the URL is the important aspect. For example, the access point for an image would be the URL from which you get the actual pixels, rather than a linked data description of the image.
* Format - The `format` of a digital object is its media type, often called a MIME type, given as a string.
* Standard - Many digital objects further conform to standard specifications, which can be referenced using the `conforms_to` property. This differs from `format`, as there may not be a media type for the specification, and from `classified_as` which is a broader classification (Image, rather than conforming to the standard for JPEG 2000)
* Dimensions - Digital dimensions follow the same pattern as [physical dimensions](/model/object/physical/#dimensions), but might use different types (file size) or the same (height, width for images) and different units (bytes, pixels).
* Creation - Digital Objects are created by `Creation` events rather than `Production` events, but otherwise have the same activity model.

This allows us to consistently and coherently model both physical and digital information carriers as core items of interest. In particular, a digital image file `digitally_shows` a `VisualItem`, or `digitally_carries` a `LinguisticObject`.

!!! note "Deletion / Erasure"
	It is currently not possible within the model to delete or erase a digital object. This will be added in a future minor version, and can be discussed in the [github issue](https://github.com/linked-art/linked.art/issues/524)


__Example:__

The Rijksmuseum published a digital publication on the web about their conservation efforts for The Night Watch.

```crom
top = vocab.WebPage(ident="operation_nw/1", label="Operation Night Watch Publication")
top.access_point = model.DigitalObject(ident="https://www.rijksmuseum.nl/en/stories/operation-night-watch")
top.format = "text/html"
top.conforms_to = model.InformationObject("http://w3.org/TR/html")
top.identified_by = model.Name(content="Operation Night Watch")
dim = model.Dimension(label="220 kb")
dim.unit = vocab.instances['kilobytes']
dim.value = 220
dim.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300265863", label="File Size")
top.dimension = dim
cre = model.Creation()
cre.carried_out_by = model.Group(ident="rijksmuseum", label="Rijksmuseum")
ts = model.TimeSpan()
ts.begin_of_the_begin = "2019-07-19T00:00:00Z"
ts.end_of_the_end = "2019-07-21T00:00:00Z"
cre.timespan = ts
top.created_by = cre
top.digitally_carries = model.LinguisticObject(ident="operation_nw_en", label="Operation Night Watch in English")
```

### Digital Surrogates

Some digital representations are intended to be faithful reproductions of a physical object.  Especially when digitizing two dimensional works, it is useful to distinguish between a digital image that depicts the object generally, but perhaps along with other objects, people and the surroundings, compared to a digital image which shows only the same visual content as the physical object. We can be more explicit that the physical object `shows` the same intellectual content that the digital image `digitally_shows`.

These images are sometimes called "Digital Surrogates", as they can stand in for the physical object. A digital surrogate might show more than just the object, such as a color strip and a ruler, however the main focus of the visual item must clearly be the object itself. The line between surrogate and depiction is left to the policies and practices of implementing organizations.

__Example:__

The same visual item is shown by both the physical painting, and the digitized image of the painting.

```crom
top = model.HumanMadeObject(ident="spring/8", label="Jeanne (Spring) by Manet")
top.identified_by = model.Name(content="Jeanne (Spring)")
top.shows = model.VisualItem(ident="spring", label="Visual Content of Spring")
```

```crom
top = model.DigitalObject(ident="spring/1", label="Jeanne (Spring) (Digital)")
top.identified_by = model.Name(content="Jeanne (Spring)")
top.digitally_shows = model.VisualItem(ident="spring", label="Visual Content of Spring")
```

## References to Digital Content

### Digital Images

Many of the entities that are described using Linked Art will have digital images that depict them. These images are useful for building compelling user interfaces for the data, and often take a prominent position in those interfaces. However these images are often not the main items of interest for the data, merely representations of the entities.

One image might show many different entities, of different types.  An image of an artist standing next to one of her paintings would show both the artist (a `Person`) and the painting (a `HumanMadeObject`).  Further, the same image might be shown by many digital copies and derivatives, each available at a different URL. The same image might also be shown by a physical object, either by printing a digital file or that the digital image is a digitization of the physical object. 

Note that this usage does not require a separate record to manage the digital object, instead the pattern is inverted with only a smaller set of properties available.

__Example:__

Rembrandt is depicted in a digital image hosted at wikimedia.

```crom
top = model.Person(ident="rembrandt/15", label="Rembrandt")
vi = model.VisualItem()
top.representation = vi
img = vocab.DigitalImage(label="Image of Rembrandt")
vi.digitally_shown_by = img
img.format = "image/jpeg"
img.access_point = model.DigitalObject("https://upload.wikimedia.org/wikipedia/commons/b/bd/Rembrandt_van_Rijn_-_Self-Portrait_-_Google_Art_Project.jpg")
```


### Web Pages

Another very common scenario is that there is a web page about the object, perhaps managed by a collections management system. For humans, this page is much more useful than the data intended for machines.  It can be referenced with the `subject_of` property, and points to a `DigitalObject` which is `classified_as` a web page, or _aat:300264578_.  As with digital images, the home page can have a `format` of "text/html" and other properties.

__Example:__

There is a home page for Jeanne in the Getty collections.

```crom
top = vocab.Painting(ident="spring/9", label="Jeanne (Spring) by Manet")
top.identified_by = model.Name(content="Jeanne (Spring)")
lo = model.LinguisticObject()
top.subject_of = lo
page = vocab.WebPage()
lo.digitally_carried_by = page
page.format = "text/html"
page.access_point = model.DigitalObject("https://www.getty.edu/art/collection/object/103QTZ")
```

### IIIF Manifests 

[IIIF](http://iiif.io/), the International Image Interoperability Framework, is an increasingly common way to make images and descriptions intended to be displayed to humans available. There are two primary alignments with the Digital Object model - Manifests from the IIIF Presentation API, and Images from the IIIF Image API.

The [IIIF Presentation API](http://iiif.io/api/presentation/) is considered to be a `DigitalObject` that is about the object, in the same way as the home page of the object in a collection information system. There is linguistic content within the manifest, that could be have one or more languages associated with it, and thus we have the same intermediary `LinguisticObject` as the value of the `subject_of` property. The `conformsTo` property should be used to refer to the context document for the API to ensure it can be recognized, including which version.

The specification that a Manifest conforms to is the Presentation API: [http://iiif.io/api/presentation/](http://iiif.io/api/presentation/)

And per that specification, the media type to be used in format follows the pattern: `application/ld+json;profile="http://iiif.io/api/presentation/3/context.json"`

__Example:__

Jeanne has a IIIF Presentation API Manifest.

```crom
top = vocab.Painting(ident="spring/10", label="Jeanne (Spring) by Manet")
top.identified_by = model.Name(content="Jeanne (Spring)")
lo = model.LinguisticObject()
top.subject_of = lo
mfst = model.DigitalObject()
mfst.access_point = model.DigitalObject(ident="https://media.getty.edu/iiif/manifest/db379bba-801c-4650-bc31-3ff2f712eb21")
mfst.conforms_to = model.InformationObject("http://iiif.io/api/presentation/")
mfst.format = "application/ld+json;profile='http://iiif.io/api/presentation/3/context.json'"
lo.digitally_carried_by = mfst
```

### IIIF Images

The [IIIF Image API](http://iiif.io/api/image/) is a `DigitalService` from which various derivatives of the image content can be requested. Similarly to the `access_point` property used in the previous sections, this service is referenced via the `digitally_available_via` property from the core `DigitalObject` that represents the digital image.  The same image might have both access points and image services.

The IIIF Image service should have a `conforms_to` property that refers to "http://iiif.io/api/image/" as the URI of an `InformationObject`, so that applications know what sort of service is being referred to. The `format` property refers to the image information document (info.json) which has the media type of `application/ld+json;profile="http://iiif.io/api/image/3/context.json"`

__Example:__

The image of Jeanne is also available via a IIIF Image API service.

```crom
top = vocab.Painting(ident="spring/11", label="Jeanne (Spring) by Manet")
top.identified_by = model.Name(content="Jeanne (Spring)")
img = model.VisualItem()
top.representation = img
do = vocab.DigitalImage()
img.digitally_shown_by = do
do.access_point = model.DigitalObject("https://media.getty.edu/iiif/image/8094f61e-e458-42bd-90cf-a0ed0dcc90b9/full/full/0/default.jpg")
svc = model.DigitalService()
svc.access_point = model.DigitalObject(ident="https://media.getty.edu/iiif/image/8094f61e-e458-42bd-90cf-a0ed0dcc90b9")
svc.conforms_to = model.InformationObject("http://iiif.io/api/image")
svc.format = "application/ld+json;profile='http://iiif.io/api/image/3/context.json'"
do.digitally_available_via = svc
```
