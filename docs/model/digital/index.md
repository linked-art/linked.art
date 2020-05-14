---
title: "Digital Integration"
up_href: "/model"
up_label: "Model"
---

[TOC]

## Introduction

It is very unlikely that the descriptions provided in this model are the only digital representations of the resources that they describe.  For building human readable representations, or just for linking to existing web pages, these other digital resources should be referenced.

## Image 

The most common scenario is if there are one or more images available of the object. This is described by using the `representation` property, which has a `VisualItem` as its value. The `id` of the image is the URI at which it is available, and additional properties to describe the image should also be given, such as a `label` and its media type (sometimes called a MIME type) in `format`. The digital image should be classified as such using _aat:300215302_.


```crom
top = Painting(art=1)
top._label = "Painting"
# img = DigitalImage("http://example.org/images/image.jpg")
# img._label = "Image of Painting"
# img.format = "image/jpeg"
# top.representation = img
```

## Home Page

Another very common scenario is that there is a web page about the object, perhaps managed by a collections management system. For humans, this page is much more useful than the data intended for machines.  It can be referenced with the `subject_of` property, and points to a `LinguisticObject` which is `classified_as` a web page, or _aat:300264578_.  As with digital images, the homepage should have a `format` of "text/html", the media type for HTML.

```crom
top = Painting(art=1)
top._label = "Painting"
page = WebPage("http://example.org/collection/1/painting")
page.classified_as = instances['primary']
page._label = "Homepage for Painting"
page.format = "text/html"
top.subject_of = page
```

## Other Pages

While the publishing organization might have a home page for their object as above, there are likely to be many other web pages about the object as well in different systems.  These pages follow the same model of being a `LinguisticObject`, but instead use the `referred_to_by` property for the link. 

```crom
top = Painting(art=1)
top._label = "Painting"
page = WebPage("http://example.org/journal/article")
page._label = "Webpage that discusses Painting, but is not its homepage"
page.format = "text/html"
top.referred_to_by = page
```

## IIIF 

[IIIF](http://iiif.io/), the International Image Interoperability Framework, is an increasingly common way to make images and descriptions intended to be displayed to humans available. There are two primary alignments with the CRM model, which mirror the above Image and Web Page patterns.

### IIIF Images

The [IIIF Image API](http://iiif.io/api/image/) in CRM can be considered a `VisualItem`, even though it is a service for obtaining them, and can thus be referenced with the same `representation` property. In order to know that the URI is an Image API endpoint, it should not have a `format` and instead have a `conforms_to` property with the value "http://iiif.io/api/image".  This follows the `protocol` pattern in IIIF Image Information documents.

```crom
top = Sculpture(art=1)
top._label = "Sculpture"
img = VisualItem("http://iiif.example.org/image/1")
img._label = "IIIF Image API for Sculpture"
img.conforms_to = BaseResource("http://iiif.io/api/image")
top.representation = img
```

### IIIF Manifests 

The [IIIF Presentation API](http://iiif.io/api/presentation/) in CRM can be considered an `InformationObject` that is about the object.  The property used to refer to it from the art object is `subject_of`.  It `conformsTo` the Presentation API URI, but can be given a `format` for JSON-LD that includes the context as a profile.

```crom
top = Painting(art=1)
top._label = "Painting"
mfst = InformationObject("http://iiif.example.org/presentation/1/manifest.json")
mfst.format = 'application/ld+json;profile="http://iiif.io/api/presentation/2/context.json"'
mfst.conforms_to = BaseResource("http://iiif.io/api/presentation")
top.subject_of = mfst
```
