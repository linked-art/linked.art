---
title: "Linked Art API: Reference Structure"
up_href: "/api/1.0/shared/"
up_label: "Linked Art API 1.0 Shared Data Structures"
---


[TOC]

## Introduction

As with any hypermedia API, and especially those based on linked open data, the Linked Art API makes frequent use of references between resources. These references are designed to be recognizable as such, but still contain a minimum of information needed to understand what the reference is to.

It is very likely that more information about the referenced resource will be needed by the user interface, however it is impossible to know _a priori_ what that information is. Clients should be pro-active about aggressively following references and pre-caching the descriptions to enable a responsive user interface.

## Property Definitions

References can only have the three properties below, in order to make it clear that it is a reference to an external resource rather than one that is being embedded within the current JSON document.  The URI in `id` and the class in `type` MUST be the same as the referenced resource, once the URI has been dereferenced.  The label, however, MAY be different. 

[Types](../type/) are a special case of a reference to an external entry in a vocabulary system. As noted in the type documentation, they may also have meta-classifications to ensure that they can be processed, as dereferencing the type's URI might not result in a Linked Art formatted description.

Note that references inherently have the `_complete` property with a value of `false`. They can be detected as references as all other structures have mandatory fields beyond `id`, `type` and `_label`. The `_complete` property would thus be clutter in the most common scenario of shared constructions being fully included, and data for references not being included at all.

There are two additional properties that MAY be used on references to ensure that the records are as usable as possible. If the reference is to a record for an entity which has an equivalent in a well known system (such as a local concept that duplicates a concept in AAT), then the local record's URI can be given in `id` and the external URI given in `equivalent`. Similarly, if the language tag for a `Language` is known, then that is easier for most developers to use with existing translation and internationalization toolkits, and so can be given in `lang_code` as part of the reference.

### Properties of References

| Property Name     | Datatype      | Requirement | Description | 
|-------------------|---------------|-------------|-------------|
| `id`              | string        | Required    | The value MUST be a dereferenceable URI identifying the referenced resource |  
| `type`            | string        | Required    | The value MUST be the same as the `type` of the referenced resource |
| `_label`          | string        | Recommended | A human readable label for the referenced resource, intended for developers |
| `equivalent`      | array         | Optional    | An array of references to external resources which are equivalent to the referenced resource |
| `notation`        | array         | Optional    | An array of strings, each of which is a commonly used notation or identifier for the resource. This is typically used when the `type` of the reference is `Language` and gives the [language tag](https://www.w3.org/International/articles/language-tags/). |

There are too many incoming properties to try to list them all, as it amounts to the list of all properties for all classes.

## Example

A Painting, which has several references to other entities:

* It is `classified_as` a reference to a type, which is in turn `classified_as` a meta-type
* It is `referred_to_by` the textual content of a referenced article
* It is a `member_of` a referenced museum collection set
* It `shows` a particular referenced visual work
* It has a `current_owner` of a particular referenced person
* It has a `current_location` of a referenced gallery

```crom
top = vocab.Painting(ident="auto int-per-segment", label="Example Painting")
top.current_owner = model.Person(label="Owner")
top.current_location = model.Place(label="Gallery")
top.shows = model.VisualItem(label="Visual Work of Example Painting")
top.referred_to_by = model.LinguisticObject(label="Article about Painting")
top.member_of = model.Set(label="Museum Collection")
```
