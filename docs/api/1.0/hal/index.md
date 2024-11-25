---
title: "HAL Links"
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---

[TOC]

## Introduction

Linked Art includes non-semantic data within the Linked Data response using a standard called the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-11), or HAL. This allows the record to be self-documenting as to the versions of the model, API and any extensions in use, and to refer to other formats for the same information or related APIs.


## Hypertext Application Language

HAL defines a property called `_links`, which is a JSON object with named links in it. The links are expressed as JSON objects with an `href` property that contains the URI, plus some additional optional fields. This structure is embedded into the JSON-LD record but is not semantic. Thus, if the record is turned into an RDF graph and then re-serialized, this API level data will **not** be present in the graph or new serialization.

The simplest HAL block is merely a reference to the record itself, using the `self` key:

```
{
  "_links": {
    "self": "http://example.org/linked_art/objects/1234"
  }
}
```

The types of link can be extended by adding namespaced properties, allowing both the Linked Art API and local extensions to define relationships for clients to understand and follow. The namespaces are given in a block called `curies`, which is an array of links with an additional `name` property giving the prefix, and `templated` with a value of `true` to let the client know that it is a URL template rather than a complete URL. If expanded using the template given in the `curies` block, the links will resolve to a description of their semantics and use. The `_links` block might thus start like this, potentially with additional entries in `curies` for locally named and defined extensions:

```
{
  "_links": {
    "self": "http://example.org/linked_art/objects/1234"
    "curies": [
      {"name":"la","href":"https://linked.art/api/rels/1/{rel}","templated":true}
    ]
  }
}
```

## Versioning

There are three core properties defined by the Linked Art API to deal with API versioning.

The versioning properties are:

* `la:modelVersion` - the version of the linked art model used by the record, which might be different from the version of the API (required)
* `la:apiVersion` - the version of the linked art API used by the record (required)
* `la:localVersion` - the version of any extension or set of extensions used by the record (optional)

The URI given in the `href` field MUST refer to the human readable documentation for the particular version being referenced. The `name` field MUST be present and MUST have the following structure:

`v{major-version-integer}.{minor-version-integer}.{patch-version-string}`

Thus a client can take the name field, remove the leading "v" character and split the result on the '.' character to get the major, minor and patch versions. The major and minor versions MUST be integers, such that the client can turn them from strings to numbers and compare that 10 is greater than 2 (for example). The patch component is a string, MUST NOT contain the '.' character and MUST sort correctly as a string from lowest to highest such that "patch-10" comes after "patch-02".

This will allow clients to determine whether they can process the record. If the major version is higher than the client's supported major version number, then it is unlikely. If the major version number is equal to or lower than the clients supported version, then the client should be able to process the information. If the minor version number, relative to the major version, is higher than supported, then information might be lost, but minor versions are backwards compatible with all other minor versions within the corresponding major version. Patches do not introduce new or modified functionality and hence they are primarily for awareness.

The `_links` section might thus now look like the following:

```
{
  "_links": {
    "self": "http://example.org/linked_art/objects/1234"
    "curies": [
      {"name":"la","href":"https://linked.art/api/rels/1/{rel}","templated":true}
    ],
    "la:modelVersion": {"href":"https://linked.art/model/1.0/", "name": "v1.0"},
    "la:apiVersion": {"href":"https://linked.art/api/1.0/", "name": "v1.0"},
    "la:localVersion": {"href":"https://example.org/extension/maps/geo-210", "name": "v2.1.0-beta-01"},
  }
}
```

Note that, as a namespace, the curie template for the Linked Art relationships does not include a minor version number as minor versions must be backwards compatible with the major version. Future major versions will thus introduce a new set of links (though likely the same as the previous versions), and potentially also change the response format from following those links.


## Linking to Other Representations

There are two HAL links that can be used to refer to other parts of the API ecosystem. In particular, it is very valuable to link from the JSON-LD data to a web page that renders the data for humans, to other representations in different Linked Data formats, and to a IIIF Change Discovery API endpoint that would allow a remote system to harvest and stay synchronized with the overall dataset.

Linking from the JSON-LD record to a rendering of the data, as opposed to some external web collection page about the object, can be done with the `alternate` property. In order to convey the media type of the rendering is HTML, the link object MUST have the `type` property with the value `text/html`. The `alternate` property can also be used to refer to other representations of the data, such as a semantic representation in Turtle, or non-semantic representations such as CSV or XML. The `type` property MUST be present with the correct media type for the format.

A [IIIF Change Discovery endpoint](../discovery/) can similarly be referenced using the `collection` property.

Thus an extended `_links` section could look like:

```
{
  "_links": {
    "self": "http://example.org/linked_art/objects/1234"
    "curies": [
      {"name":"la","href":"https://linked.art/api/rels/1/{rel}","templated":true}
    ],

    "alternate": [
      {"href": "https://example.org/view/1234.html", "type": "text/html"},
      {"href": "https://example.org/linked_art/objects/1234.ttl", "type": "text/turtle"}
    ],
    "collection": {"href": "https://example.org/discovery/collection.json"},

    "la:modelVersion": {"href":"https://linked.art/model/1.0/", "name": "v1.0"},
    "la:apiVersion": {"href":"https://linked.art/api/1.0/", "name": "v1.0"},
    "la:localVersion": {"href":"https://example.org/extension/maps/geo-210", "name": "v2.1.0-beta-01"},

  }
}
```

## Linking to Searches

The main use for HAL links in Linked Art is to direct the consuming application to search results related to the current record. This is documented in the [search](../search/) API.
