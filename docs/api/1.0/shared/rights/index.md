---
title: "Linked Art API: Rights Structure"
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

The Rights construct is used to express machine comparable, but not necessarily actionable, rights assertions about intellectual works. The URI for the class of Right is conveyed in `classified_as`.

See the model documentation for [rights](/model/object/rights/#rights-assertions).

## Property Definitions

The rights data structure has the following properties.

### Properties of Rights

| Property Name     | Datatype      | Requirement | Description | 
|-------------------|---------------|-------------|-------------|
| `id`              | string        | Optional    | If present, the value MUST be a URI identifying the right description, from which a representation of it can be retrieved | 
| `type`            | string        | Required    | The class for the right, which MUST be the value `"Right"` |
| `_label`          | string        | Recommended | A human readable label, intended for developers |
| `_complete`       | boolean       | Optional    | Non-Semantic. If there is an `id` property with a URI, and there is more information about the identifier available from the representation at that URI, then `_complete` MUST be present with a value of `false` to inform the consuming application that it might want to retrieve it |
| `identified_by`   | array         | Recommended | An array of json objects, each of which is a name for the right, and MUST follow the requirements for [Name](../name/) |
| `classified_as`   | array         | Recommended | An array of json objects, each of which is a further classification of the right and MUST follow the requirements for [Type](../type/) |
| `referred_to_by`  | array         | Optional    | An array of json objects, each of which is an embedded [statement](../statement/) about the right. |


### Property Diagram

> ![diagram](right_properties.png){:.diagram_img width="600px"}

### Incoming Properties

Right instances are typically found as the object of the following properties.

| Property Name   | Source Endpoint   | Description |
|-----------------|-------------------|-------------|
| `subject_to`     | [Textual Work](../../endpoint/textual_work/), [Visual Work](../../endpoint/visual_work), [Abstract Work](../../endpoint/abstract_work), [Statement](../statement/) | Intellectual things, primarily works, can have rights associated with them using the `subject_to` property |


## Example


```crom
top = model.LinguisticObject()

```
