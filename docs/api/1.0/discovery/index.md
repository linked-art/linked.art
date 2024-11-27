---
title: "Linked Art Discovery API"
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---

[TOC]

## Introduction

Linked Art data does not exist in a vacuum, nor does it try to define all possible interactions with cultural heritage data. Instead, our scope is to define the semantic description of cultural heritage items, and the important surrounding contextual information such as people, places, concepts and events. This section documents how to reference Linked Art records from other APIs and web-based systems.


## Data Visibility from HTML

In order to ensure that search engines such as Google get as much information as possible, there is a mapping from Linked Art into the [Schema.Org](https://schema.org/) structure. Schema.Org can be embedded within web pages as JSON-LD or other formats enabling search engines to process the data as data, rather than only via the human-intended HTML. The [mapping](/cookbook/mappings/schema/) is not part of the versioned APIs as it will be updated as the underlying schema and its usage changes, which is not in our control.

For visibility of the data to clients that might be given a web page, rather than the URI of the JSON-LD record, it is also important to give them a link to the data. This is done via [Link Headers](https://www.rfc-editor.org/rfc/rfc8288.html) in the HTTP response (for non-browser clients), and within the HTML `head` element (for browser-based clients). This will allow the client to go from the HTML view for human users directly to the more machine understandable JSON-LD records for processing.

In the HTTP response of the web page for the object, the header to link to the JSON-LD record would look like this:

```
Link: <https://example.com/data/object/1>;
        rel="describedby";
        type="application/ld+json;profile='https://linked.art/ns/v1/linked-art.json'"
```

And in the `head` element of the HTML:

```XML
<head>
  <link rel="describedby" href="https://example.com/data/object/1" 
        type="application/ld+json;profile='https://linked.art/ns/v1/linked-art.json'"/>
</head>
```

The `link` element in `head` MUST be present, and the HTTP header SHOULD be present if possible. The page MUST have only one such link to a linked art record to avoid confusion about which one should be used.

Note that this follows the [FAIR Signposting Profile](https://signposting.org/FAIR/) so any implementation of Linked Art that follows the above, will also conform to that specification.


## Harvesting

In order to produce cross-collection and cross-institutional aggregating services or applications, it is necessary to be able to find all of the records in an efficient manner and stay synchronized with any changes to those records.  This is the purpose of the [IIIF Change Discovery API](https://iiif.io/api/discovery/). 

In order to make the Linked Art record types available, a short context document ([https://linked.art/ns/v1/record-types.json](https://linked.art/ns/v1/record-types.json)) can be used as an extension, as described in the IIIF API's section on Linked Data Contexts and [Extensions](https://iiif.io/api/discovery/1.0/#342-extensions).

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

