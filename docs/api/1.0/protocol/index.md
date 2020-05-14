---
title: Linked Art API Protocol
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---

[TOC]

## Introduction

The purpose of an API is to provide an interface that can be used by application developers to interact with the data in a system which is, somehow, separate from the system they are implementing. In some contexts this separation might just be within a single codebase with different aspects being developed by different software engineers.  In the Linked Art API, this separation is much more concrete - the code of the consuming application is completely separate from the code of the publishing system, and we need a protocol to transport requests and responses over a network between the systems.

[Linked Open Usable Data](/loud/) acknowledges that this network interaction has costs, and the social separation between the various software engineers multiplies those costs. The protocol for transporting data from the publisher to the consuming application needs to be as minimal and well-understood as possible, in order to not further complicate implementations. For this reason, we prefer the strategy of a resource-centric interface (or "REST") to a service-oriented architecture.  We use the web as the core hypermedia platform, and thus use HTTP as the protocol for interaction.

Using the REST paradigm and the HTTP protocol follows our [design principles](../principles/). This document defines the specific details of how REST is interpreted in this context, and which features of HTTP should be taken into account by implementations.

## HTTP Implementation Details

### HTTPS and Protocol Versions

The encrypted form of HTTP, called HTTPS, is strongly recommended to publishing implementations. Even for completely open and reusable data, the security protects the privacy of users and allows implementation patterns in which the data is not completely open but instead requires some degree of authentication.  The URIs for the endpoints, and therefore the entities being described, would use the `https` protocol scheme.

For example, this documentation uses https, resulting in endpoints like:

> `https://linked.art/example/object/1.json`

There is a great advantage in terms of network interaction speed to support the latest version of the HTTP protocol, called `HTTP/2`. Supporting HTTP 2 allows many concurrent requests to take place, improving the time to complete page loads and avoiding the browser-imposed limit on the number of concurrent connections per site.  Web servers MUST support HTTP 1.1 and SHOULD support HTTP 2.

### Operations

The only operation supported by version 1.0 of the API is to retrieve representations from the endpoints. In HTTP terms, this means that only the `GET` method is directly used, and not `POST` (for creating resources), `PUT` (for updating resources), or `DELETE` (for deleting resources). 

However, there are two other operations that need to be taken into account.  The `OPTIONS` request must be supported by the server in order to allow interaction with the browser in javascript, in a process called CORS.  This is described below in its own section.  Secondly, there is the `HEAD` method which returns header information about the resource without the actual representation.  This is useful to support, but consuming clients MUST NOT rely on it.

Publishers MUST support GET and OPTIONS, and SHOULD support HEAD.


### HTTP Headers

In order to allow the URIs for the endpoints to coexist with other systems and representations, it is necessary to send a header on the request to the endpoint specifying the format that is desired.  This is often called "content negotiation", or sometimes just "conneg".  The media type of the desired format is sent in the `Accept` header, which (per the [json-ld](../json-ld/) documentation) is:

> `Accept: application/ld+json;profile="https://linked.art/ns/v1/linked-art.json"`

The server will then respond with the right format, and echo back the media type in the `Content-Type` header:

> `Content-Type: application/ld+json;profile="https://linked.art/ns/v1/linked-art.json"`

Servers MAY support other serializations as well as Linked Art JSON-LD at the same URIs, which would be requested by changing the media type given in the `Accept` header.

Linked Art does not specify a mechanism by which the set of other supported formats can be discovered.

### CORS

In order to allow browser-based applications to interact with the data, publishers MUST ensure that the Cross-Origin Resource Sharing, or [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS), headers are correctly set. In particular, the `Access-Control-Allow-Origin` header on the responses MUST be set to "*" on every response.

> `Access-Control-Allow-Origin: *`

Resources MUST also respond with this header in reaction to an `OPTIONS` request (called a preflight request) to allow the use of the data to take place across systems, and using very vanilla media types.


## URI Good Practices

There are no requirements for the URIs for any of the endpoints or instances for Linked Art, as the URIs never need to be manipulated to cause the service to behave differently.  By not requiring a particular pattern, we enable many different implementations including the reuse of existing URIs with a different format.

However it is acknowledged that there are some good practices for the construction of URIs, when there are no other considerations that must be taken into account. These fall into desirable features for the URI in general, and patterns within the structure of the URI itself.

### Desirable Features

__URIs should be as persistent as possible.__ Anything in the URI that might be required to change in the future should be avoided, including specific technology references, technology specific identifiers that cannot be maintained, institutional departments that might be renamed, and so forth.

__URIs should be short and readable, within reason.__ Shorter URIs are frequently preferred to longer ones, as they are more memorable and easier to copy or type out. Linked Art API URIs should thus be able to be short and readable ... within reason, given that they are almost certainly managed by automated systems through a database, and persistence is more important than readability.

__URIs should enable sensible data management and trivial implementations.__ As implementation should be possible by putting files on disk in a webserver, the URIs must be able to reflect this strategy without causing undue burdens.

__URIs must still be treated as if they were opaque strings.__ Regardless of the above features for the structure and components of a URI, they MUST still be treated as if they were completely opaque strings containing no useful information. The encoded patterns are there to facilitate software engineers understanding the API, not to facilitate software to interact with it.


### Preferred URI Structure

The preferred structure to meet the desiderata outlined above is

> scheme `://` hostname `/` _prefix_ `/` endpoint `/` identifier

where

* `scheme` is "https" if possible, or "http" if not
* `hostname` is the domain name for the institution that owns the resources described if possible, or manages the data if not
* `prefix` is an optional path component, that may include / characters, to allow the data to be published at any level of the website's hierarchy
* `endpoint` is a fixed path component per endpoint to collect all of the entries of a given type together 
* `identifier` is a unique identifier for the entry

Thus an example might be:

> `https://museum.org/data/object/opaque-identifier`


Preferred endpoint path names:

* `digital` - [Digital Objects](../endpoint/digital_object/)
* `event` - [Events](../endpoint/event/)
* `group` - [Groups](../endpoint/group/)
* `object` - [Physical Objects](../endpoint/physical_object/)
* `person` - [People](../endpoint/person/)
* `place` - [Places](../endpoint/place/)
* `provenance` - [Provenance Activities](../endpoint/provenance_activity/)
* `set` - [Collections and Sets](../endpoint/set/)
* `textual_work` - [Textual Works](../endpoint/textual_work/)
* `visual_work` - [Visual Works](../endpoint/visual_work/)

