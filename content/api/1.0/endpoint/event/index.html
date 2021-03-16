---
title: "Linked Art API: Event"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 Endpoints"
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

{% include "toc.html" %}

## Introduction

The Event API is a method of getting access to descriptions of periods of time, events or activities that are not directly associated with other entities, nor are provenance activities or exhibitions, but are still noteworthy occurences somehow related to artwork.  Examples might include a fire that burnt down a museum, thereby causing the destruction of many works of art, a project that researched aspects of works of art, or a named period during which objects were created. Although these are different classes, they are so similar in this usage that they are grouped together into a single endpoint from the perspective of the API. The Event API is of average complexity with many familiar properties and patterns of other endpoints, plus the event and activity properties familiar from embedded events.  

## Property Definitions

Dereferencing an entity via the Event endpoint would result in a JSON-LD document containing a single JSON object with the following properties.

### Properties of Events

| Property Name     | Datatype      | Requirement | Description | 
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | Required    | The value MUST be the URI of the [Linked Art context](../../json-ld/) as a string, `"https://linked.art/ns/v1/linked-art.json"` or an array in which the URI is the last entry to allow for [extensions](../../json-ld/extensions.html) | 
| `id`              | string        | Required    | The value MUST be the HTTP(S) URI at which the event's representation can be [dereferenced](../../protocol/) |  
| `type`            | string        | Required    | The class for the event, which MUST be the value `"Period"`, `"Event"` or `"Activity"` |
| `_label`          | string        | Recommended | A human readable label for the event, intended for developers |
| `classified_as`   | array         | Recommended | An array of json objects, each of which is a classification of the event and MUST follow the requirements for [Type](../../shared/type/) |
| `identified_by`   | array         | Recommended | An array of json objects, each of which is a name/title of the event and MUST follow the requirements for [Name](../../shared/name/), or an identifier for the event and MUST follow the requirements for [Identifier](../../shared/identifier/) |
| `referred_to_by`  | array         | Optional    | An array of json objects, each of which is a human readable statement about the event and MUST follow the requirements for [Statement](../../shared/statement/) |
| `equivalent`      | array         | Optional    | An array of json objects, each of which is a [reference](../../shared/reference) to an external identity and description of the current event |
| `representation`  | array         | Optional    | An array of json objects, each of which is a reference to a [Visual Work](../visual_work) that represents the current event, and MUST follow the requirements for a [reference](../../shared/reference/) |
| `member_of`       | array         | Optional    | An array of json objects, each of which is a Set that the current event is a member of and MUST follow the requirements for a [reference](../../shared/reference/) to a Set |
| `subject_of`      | array         | Optional    | An array of json objects, each of which is a reference to a [Textual Work](../textual_work/), the content of which focuses on the current event, and MUST follow the requirements for a [reference](../../shared/reference/) |
| `attributed_by`   | array         | Optional    | An array of json objects, each of which is a [Relationship Assignment](../../shared/assignment/) that relates the current event to another entity |
| `part_of` | array | Optional | An array of json objects, each of which is a [reference](../../shared/reference/) to another Event that the current event is a part of. |
| `timespan`        | json object   | Recommended | A json object recording when the event occured, which MUST follow the requirements for [timespans](../timespan/)|
| `took_place_at`   | array         | Optional    | An array of json objects, each of which is a [reference](../../shared/reference/) to a [Place](../place/) where the event occured |
| `caused_by`       | array         | Optional    | An array of json objects, each of which is a [reference](../../shared/reference/) to another Event that caused this event to occur. **Only usable when the `type` is `"Event"` or `"Activity"`** |
| `influenced_by`   | array         | Optional    | An array of json objects, each of which is a [reference](../../shared/reference/) to an entity that influenced the event in some noticable fashion.  **Only usable when the `type` is `"Activity"`** | 
| `carried_out_by`  | array         | Optional    | An array of json objects, each of which is a [reference](../../shared/reference/) to a [Person](../person/) or [Group](../group/) that carried out the activity. **Only usable when the `type` is `"Activity"`** |
| `used_specific_object` | array    | Optional    | An array of json objects, each of which is a [reference](../../shared/reference)] to an entity that was instrumental in the carrying out of the activity. **Only usable when the `type` is `"Activity"`** |


### Property Diagram

> ![diagram](event_properties.png){:.diagram_img width="600px"}

### JSON Schema

See the [schema documentation](../../schema_docs/event.html) and the [schema itself](../../schema/event.json)


### Incoming Properties

Event instances are typically found as the object of the following properties, other than the self-referential properties above.  This list is not exhaustive, but is intended to cover the likely cases where other endpoints refer to events.

| Property Name              | Source Endpoint | Description |
|----------------------------|-----------------|-------------|
| `part_of`                  | All             | Any other event or activity in any of the end points can be `part_of` a broader period, event or activity. This implies that the spatial and temporal constraints of the broader event apply also to the referencing event. |


## Example

The JSON for an Event describing an auction in 1820 could be as below.

* It has the Linked Art context document reference in `@context`
* It self-documents its URI in `id`
* It has a `type` of "Activity" (as it is carried out by some Group, thus it is not an Event or Period)
* It has a `_label` with the value "Foster Auction of March 1820" for people reading the JSON
* It is `classified_as` an "Auction Event", which has an `id` of "aat:300054751"
* It is `identified_by` ...
    * ... a `Name`, with the content "Edward Foster Auction of March 1820"
    * ... and an `Identifier`, with the content "Br1908", which is `classified_as` an Owner-Assigned number ("aat:300404621")
* It is `referred_to_by` a statement which ...
    * ... has `content` of "Besides paintings, this sale ..."
    * ... is `classified_as` a Description ("aat:300411780")
* It has a `timespan` which ...
    * ... has a display title, with the `content` "1820 Mar 09"
    * ... has a `begin_of_the_begin` with the value "1820-03-09T00:00:00Z"  (the earliest possible time on March 9th)
    * ... has an `end_of_the_end` with the value "1820-03-09T23:59:59Z" (the latest possible time on March 9th)
* It `took_place_at` London
* It was `carried_out_by` the Group "Edward Foster & Son"
* It `used_specific_object` of a Set, encompassing all of the auction lots
* It is `equivalent` to another description of the same event at example.auction
* It is the `subject_of` the text of a Sales Catalog


```crom
top = vocab.AuctionEvent(ident="auto int-per-segment", label="Foster Auction of March 1820")
top.identified_by = model.Name(content="Edward Foster Auction of March 1820")
top.identified_by = vocab.LocalNumber(content="Br1908")
top.carried_out_by = model.Group(ident="http://vocab.getty.edu/ulan/500451765", label="Edward Foster & Son")
top.took_place_at = model.Place(ident="http://vocab.getty.edu/tgn/7011781", label="London")
top.referred_to_by = vocab.Description(content="Besides paintings, this sale included a few lots with musical instruments and watches. The owners were a number of dealers who regularly consigned their wares to this auctioneer, despite the fact that the title page names \"A Gentleman\" as the owner.")
top.equivalent = model.Activity(ident="http://example.auction/past/foster/1820/03/1")
top.subject_of = model.LinguisticObject(ident="http://example.org/catalog/Br1908", label="Sales Catalog of Br-1908")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1820-03-09T00:00:00Z"
ts.end_of_the_end = "1820-03-09T23:59:59Z"
ts.identified_by = vocab.DisplayName(content="1820 Mar 09")
top.timespan = ts
top.used_specific_object = model.Set(ident="http://example.org/sets/Br1908", label="All Auction Lots of Br1908")
```
