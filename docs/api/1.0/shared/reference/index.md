---
title: "Linked Art API: Reference Structure"
up_href: "/api/1.0/shared/"
up_label: "Linked Art API 1.0 Shared Data Structures"
---

<style>
th, td {
  padding: 5px 5px;
  text-align: left;
  border: 1px solid #D0D0D0; }
th { background: #F0F0F0; }
th:first-child, td:first-child { padding-left: 3px; }
th:last-child, td:last-child { padding-right: 3px; }
</style>

[TOC]

## Introduction

As with any hypermedia API, and especially those based on linked open data, the Linked Art API makes frequent use of references between resources. These references are designed to be recognizable as such, but still contain a minimum of information needed to understand what the reference is to.

It is very likely that more information about the referenced resource will be needed by the user interface, however it is impossible to know _a priori_ what that information is. Clients should be pro-active about aggressively following references and pre-caching the descriptions to enable a responsive user interface.

## Property Definitions

References can only have the three properties below, in order to make it clear that it is a reference to an external resource rather than one that is being embedded within the current JSON document.  The URI in `id` and the class in `type` MUST be the same as the referenced resource, once the URI has been dereferenced.  The label, however, MAY be different. 

[Types](../type/) are a special case of a reference to an external entry in a vocabulary system. As noted in the type documentation, they may also have meta-classifications to ensure that they can be processed, as dereferencing the type's URI might not result in a Linked Art formatted description.

### Properties of References

| Property Name     | Datatype      | Requirement | Description | 
|-------------------|---------------|-------------|-------------|
| `id`              | string        | Required    | The value MUST be a dereferenceable URI identifying the referenced resource |  
| `type`            | string        | Required    | The value MUST be the same as the `type` of the referenced resource |
| `_label`          | string        | Recommended | A human readable label for the referenced resource, intended for developers |

There are too many incoming properties to try to list them all, as it amounts to the list of all properties for all classes.

## Example

A human-made object ...

* ... is `classified_as` a reference to a type, which is in turn `classified_as` a meta-type
* ... is `referred_to_by` the textual content of a referenced article
* ... is a `member_of` a referenced museum collection set
* ... `shows` a particular referenced visual work
* ... has a `current_owner` of a particular referenced person
* ... and has a `current_location` of a referenced gallery.

```crom
top = vocab.Painting(label="Example Painting")
top.current_owner = model.Person(label="Owner")
top.current_location = model.Place(label="Gallery")
top.shows = model.VisualItem(label="Visual Work of Example Painting")
top.referred_to_by = model.LinguisticObject(label="Article about Painting")
top.member_of = model.Set(label="Museum Collection")
```
