---
title: "Linked Art API Ecosystem"
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---

[TOC]

## Introduction

Linked Art data does not exist in a vacuum, nor does it try to define all possible interactions with cultural heritage data. Instead, our scope is to define the semantic description of cultural heritage items, and the important surrounding contextual information such as people, places, concepts and events. This section documents the broader ecosystem, and how to make use of the other standards and specifications in conjunction with Linked Art records.


## Presenting Content

While Linked Art metadata records can easily be rendered via an attractive interface for humans to engage with, the display of full text, image, audio, video, 3d and any other content resources is left to external specifications and tools. In particular, the functionality of the IIIF Image and Presentation APIs are recommended.

The hooks to those resources are given using the [Digital Integration](/model/digital) patterns.

* [IIIF Image API](https://iiif.io/api/image/)
* [IIIF Presentation API](https://iiif.io/api/presentation/)


## Data Visibility from HTML

In order to ensure that search engines such as Google get as much information as possible, there is a mapping from Linked Art into the [Schema.Org](https://schema.org/) structure. Schema.Org can be embedded within web pages as JSON-LD or other formats enabling search engines to process the data as data, rather than only via the human-intended HTML. The [mapping](/cookbook/mappings/schema.org/) is not part of the versioned APIs as it will be updated as the underlying schema and its usage changes, which is not in our control.

For visibility of the data to clients that might be given a web page, rather than the URI of the JSON-LD record, it is also important to give them a link to the data. This is done via [Link Headers](https://www.rfc-editor.org/rfc/rfc8288.html) in the HTTP response (for non-browser clients), and within the HTML `head` element (for browser-based clients).

In the HTTP response of the web page for the object, the header to link to the JSON-LD record would look like this:

```
Link: <https://example.com/data/object/1>;
        rel="alternate";
        type="application/ld+json;profile='https://linked.art/ns/v1/linked-art.json'"
```

And in the `head` element of the HTML:

```XML
<head>
  <link rel="alternate" href="https://example.com/data/object/1" 
        type="application/ld+json;profile='https://linked.art/ns/v1/linked-art.json'"/>
</head>
```

The `link` element in `head` MUST be present, and the HTTP header SHOULD be present if possible.


## Harvesting

In order to produce cross-collection and cross-institutional aggregating services or applications, it is necessary to be able to find all of the records in an efficient manner and stay synchronized with any changes to those records.  This is the purpose of the [IIIF Change Discovery API](https://iiif.io/api/discovery/). 

In order to make the Linked Art record types available, a short context document ([https://linked.art/ns/v1/record-types.json](https://linked.art/ns/v1/record-types.json)) can be used as an extension, as described in the API's section on Linked Data Contexts and [Extensions](https://iiif.io/api/discovery/1.0/#342-extensions).

Thus the contexts in the response would be:

```json
{
  "@context": [
    "https://linked.art/ns/v1/record-types.json",
    "http://iiif.io/api/discovery/1/context.json"
  ]
}
```

This would allow change entries such as the following to be present in the stream, rather than being limited to the IIIF values for `type`.

```json
{
  "type": "Update",
  "object": {
    "id": "https://example.org/api/object/1",
    "type": "HumanMadeObject"
  }
}
```

Otherwise, the functionality and syntax is exactly as described by the IIIF specification.

## Search

The Linked Art API does not specify a query syntax for searching, but we do define a response format. This is the format expected as a response from the links in the [HAL](../hal/) links section, but can also be used for responses from arbitrary search URIs as well.  It is a basic paged list syntax and based on the [IIIF Change Discovery API](https://iiif.io/api/discovery/) and [IIIF Content Search API](https://iiif.io/api/search/) formats, which in turn use the W3C's [Activity Streams](https://www.w3.org/TR/activitystreams-core/) format.

It is documented [here](search.html).

For more complex search cases, implmenters are advised to look at [GraphQL](https://graphql.org/) which queries by example, and [SPARQL](https://www.w3.org/TR/sparql11-query/) which is the standard for RDF graph based queries.
