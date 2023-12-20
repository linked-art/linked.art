---
title: "Linked Art Search Response Format"
up_href: "/api/1.0/ecosystem/"
up_label: "Linked Art API 1.0 Ecosystem"
---

[TOC]

## Introduction

The format described below is not new, and is used in a variety of places within the cultural heritage API ecosystem. It is based upon the Collections model from [Activity Streams 2.0](https://www.w3.org/TR/activitystreams-core/#collections) and is used in specifications such as the [IIIF Change Discovery API](https://iiif.io/api/discovery/1.0/), the [IIIF Content Search API](https://iiif.io/api/search/2.0/), the [W3C's Web Annotation Model](https://www.w3.org/TR/annotation-model/#collections), and beyond. It is a very straight forward paging model where the server rather than the client gets to define the page size.

This documentation will not go into great detail about the format and focus on the core functionality needed for implementation. If excruciating detail is desirable, then reading the above links will provide that experience.

The format has two main responses: the overall Collection of items or results, which consists of one or more pages that enumerate the included items. The [HAL](../hal/) links from records will refer to the first page of the collection, rather than to the collection directly. The collection is then embedded within each page, meaning that it never has to be dereferenced separately. 


## Result Pages

Result pages have a very simple structure with the following properties:

* `@context` - This MUST be present, with the value `"https://linked.art/ns/v1/search.json"
* `id` - This MUST be present, with the value being the URI of the page
* `type` - This MUST be present, with the value being the string `"OrderedCollectionPage"`
* `partOf` - This MUST be present, with the value being a JSON object for the Collection, described in the next section.
* `next` - This MUST be present unless it is the last page. The value is a JSON object with exactly two properties: `id` being the id of the next page in the collection, and `type` with the value `"OrderedCollectionPage"`.
* `prev` - This MUST be present unless it is the first page. The value is a JSON object with exactly two properties: `id` being the id of the previous page in the collection, and `type` with the value `"OrderedCollectionPage"`.
* `startIndex` - This SHOULD be present, with the value being the 0-based index of the first entry in the `orderedItems` list within the overall collection.
* `orderedItems` - This MUST be present, with the value being an array of items. Each item is a JSON object with exactly two properties: `id` and `type` from the included Linked Art record.

An example page would thus be:

```
{
	"@context": "https://linked.art/ns/v1/search.json",
	"id": "https://example.org/api/objectHasPartObject/1234/2",
	"type": "OrderedCollectionPage",
	"partOf": { ... },
	"next": {
		"id":"https://example.org/api/objectHasPartObject/1234/3",
		"type": "OrderedCollectionPage"
	},
	"prev": {
		"id":"https://example.org/api/objectHasPartObject/1234/1",
		"type": "OrderedCollectionPage"
	},
	"startIndex": 20,
	"orderedItems": [
		{
			"id":"https://example.org/data/object/1234-21",
			"type": "HumanMadeObject"
		},
		{
			"id":"https://example.org/data/object/1234-22",
			"type": "HumanMadeObject"
		}
	]
}

```

## Collections

The Collection represents the overall search results (or other set of items). In Linked Art, it is embedded within each page, but MAY also be available separately.

Collections have the following properties:

* `@context` - If the collection is being requested separately then this MUST be present, with the value `"https://linked.art/ns/v1/search.json"`. It MUST NOT be present when embedded.
* `id` - This MUST be present, with the value being the URI of the collection.
* `type` - This MUST be present, with the value being the string `"OrderedCollection"`
* `first` - This MUST be present. The value is a JSON object with exactly two properties: `id` being the id of the first page of the collection, and `type` with the value `"OrderedCollectionPage"`.
* `last` - This MUST be present. The value is a JSON object with exactly two properties: `id` being the id of the last page in the collection, and `type` with the value `"OrderedCollectionPage"`.
* `totalItems` - This SHOULD be present, with the value being the count of entries in the entire collection.
* `label` - This MAY be present. If present, the value is a JSON object with the keys being the two letter code for a language, and the values being an array of strings, where each string is a name or label for the collection in that language.
* `summary` - This MAY be present. If present, the value is a JSON object with the keys being the two letter code for a language, and the values being an array of strings, where each string is a description or summary of the collection in that language.


```
{
	"@context": "https://linked.art/ns/v1/search.json",
	"id": "https://example.org/api/objectHasPartObject/1234/2",
	"type": "OrderedCollectionPage",
	"partOf": { 
		"id": "https://example.org/api/objectHasPartObject/1234/",
		"type": "OrderedCollection",
		"first": {
			"id": "https://example.org/api/objectHasPartObject/1234/1",
			"type": "OrderedCollectionPage"
		},
		"last": {
			"id": "https://example.org/api/objectHasPartObject/1234/10",
			"type": "OrderedCollectionPage"
		},
		"totalItems": 195,
		"label": {
			"en": ["Parts of Manuscript 1234"]
		},
		"summary": {
			"en": ["Manuscript 1234 has 195 pages, each described separately"]
		}
	}
}
```

