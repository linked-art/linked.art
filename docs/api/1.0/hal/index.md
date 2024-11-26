---
title: "HAL Links"
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---



## Introduction

Following from the [principle](../principles/) that each relationship should be in only one record, there needs to be a solution that allows clients to determine that the relationship exists from the referenced record rather than the record with the relationship. For example, the object record records who was responsible for creating it and thus the artist record does not have the list of objects created by that person. However, it is clearly important to be able to determine which objects were created by the artist. The solution to this is to have a well-defined search interaction, which could be calculated in advance rather than dynamically, available to list the inverses of each relationship between records. Further, in order to not define a search query grammar, which would be difficult to implement, we use a link embedded within the record to allow the client to simply retrieve the results rather than generate a query itself. This uses a standard called the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-11), or HAL.


## Hypertext Application Language

HAL defines a property called `_links`, which is a JSON object with named links in it. The links are expressed as JSON objects with an `href` property that contains the URI, plus some additional optional fields. This structure is embedded into the JSON-LD record but is not, itself, semantic. Thus, if the record is turned into an RDF graph and then re-serialized, this API level data will not be present in the graph or new serialization.

The simplest HAL block is merely a reference to the record itself:

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

Before turning to the set of possible inverse links, there are three core properties defined by the Linked Art API to deal with API versioning.

The versioning properties are:

* `la:modelVersion` - the version of the linked art model used by the record, which might be different from the version of the API (required)
* `la:apiVersion` - the version of the linked art API used by the record (required)
* `la:localVersion` - the version of any extension or set of extensions used by the record (optional)

The URI given in the `href` field MUST refer to the human readable documentation for the particular version being referenced. The `name` field MUST be present and MUST have the following structure:

`v{major-version-integer}.{minor-version-integer}.{patch-version-string}`

Thus a client can take the name field, remove the leading "v" character and split the result on the '.' character to get the major, minor and patch versions. The major and minor versions MUST be integers, such that the client can turn them from strings to numbers and compare that 10 is greater than 2 (for example). The patch component is a string, and MUST NOT contain the '.' character and MUST sort correctly as a string such that "patch-10" comes after "patch-02".

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


## Referring Records Links

The links to the lists of referring records can now be added to the `_links` block.

The links are named in camelCase according to the current record's type, the relationship that it has to the entities in the response, and then the expected type of those entities. For example, the set of works that are about the current object would be `object` plus `SubjectOf` (being the inverse of `about`) plus `Work`. This convention helps to ensure that there will not be collisions with naming in future versions.

Going to the name of the link, generated by expanding the name with the template in the `curies` section, in the browser will display documentation about that particular link. For example, see [objectHasPartObject](https://linked.art/api/rels/1/objectHasPartObject). The full set of possible links is described at the [URI](/api/rels/1/) given in the `curies` block. 

If there are no other records that participate in the relationship (for example the person did not create any objects, or the object does not have any parts), then the link SHOULD NOT be present in the `_links` list. This will prevent clients from making unnecessary requests to retrieve information that does not exist.

The URI given in `href` has no structural requirements. It can be a search with query parameters, a direct translation of the link name and the identifier for the object, or anything else. The only requirement is that it produce the correct response format when retrieved.

The response format is a profile of [Activity Streams](https://www.w3.org/TR/activitystreams-core/), as used in the [IIIF Search API](https://iiif.io/api/search/2.0/) and other standards. It is described in more detail under the [Ecosystem](../ecosystem/) documentation. The links MUST refer to the first page of the collection, rather than to the collection itself, to prevent unnecessary retrievals.

A complete HAL `_links` block might thus look like:

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

    "la:objectHasPartObject": {"href": "https://example.org/api/objectHasPartObject/1234/1"},
    "la:objectSubjectOfWork": {"href": "https://example.org/api/objectSubjectOfWork/1234/1"}
  }
}
```

## Other HAL Links

There are two further HAL links that enable the overall [ecosystem](../ecosystem/) to flourish. In particular, it is very valuable to link from the JSON-LD data to a web page that renders the data for humans and also to a IIIF Change Discovery API endpoint that would allow a remote system to harvest and stay synchronized with the overall dataset.

Linking from the JSON-LD record to a rendering of the data, as opposed to some external web collection page about the object, can be done with the `alternate` property. In order to convey the media type of the page (very likely to be HTML), this can be added as the `type` property in the link object.

The Change Discovery endpoint can similarly be referenced using the `collection` property.

Thus an extended `_links` section could look like:

```
{
  "_links": {
    "self": "http://example.org/linked_art/objects/1234"
    "curies": [
      {"name":"la","href":"https://linked.art/api/rels/1/{rel}","templated":true}
    ],
    "alternate": {"href": "https://example.org/collection/1234", "type": "text/html"},
    "collection": {"href": "https://example.org/api/discovery/collection.json"},

    "la:modelVersion": {"href":"https://linked.art/model/1.0/", "name": "v1.0"},
    "la:apiVersion": {"href":"https://linked.art/api/1.0/", "name": "v1.0"},
    "la:localVersion": {"href":"https://example.org/extension/maps/geo-210", "name": "v2.1.0-beta-01"},

    "la:objectHasPartObject": {"href": "https://example.org/api/objectHasPartObject/1234"},
    "la:objectSubjectOfWork": {"href": "https://example.org/api/objectSubjectOfWork/1234"}
  }
}
```



