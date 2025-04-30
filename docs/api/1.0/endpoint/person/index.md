---
title: "Linked Art API: Person"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 Endpoints"
---




## Introduction

The Person API is a method of getting access to descriptions of people, living or dead.  This would include artists and collectors, but also museum staff such as curators or conservators that perform their professional activities on or using artwork. The Person model is of average complexity, with many familiar properties and patterns, plus a few more specific fields.  This results in an average complexity API that can result in reasonably long JSON responses if all of the fields have values. 

For more information about the usage of Person data, please see the [Person model](/model/actor/) description.


## Property Definitions

Dereferencing an entity via the Person endpoint would result in a JSON-LD document containing a single JSON object with the following properties.

### Properties of People

| Property Name     | Datatype      | Requirement | Description | 
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | Required    | The value MUST be the URI of the [Linked Art context](../../json-ld/) as a string, `"https://linked.art/ns/v1/linked-art.json"` or an array in which the URI is the last entry to allow for [extensions](../../json-ld/extensions) | 
| `id`              | string        | Required    | The value MUST be the HTTP(S) URI at which the person's representation can be [dereferenced](../../protocol/) |  
| `type`            | string        | Required    | The class for the person, which MUST be the value `"Person"` |
| `_label`          | string        | Recommended | A human readable label for the person, intended for developers |
| `classified_as`   | array         | Recommended | An array of json objects, each of which is a classification of the person and MUST follow the requirements for [Type](../../shared/type/) |
| `identified_by`   | array         | Recommended | An array of json objects, each of which is a name of the person and MUST follow the requirements for [Name](../../shared/name/), or an identifier for the person and MUST follow the requirements for [Identifier](../../shared/identifier/) |
| `referred_to_by`  | array         | Optional    | An array of json objects, each of which is a human readable statement about the person and MUST follow the requirements for [Statement](../../shared/statement/) |
| `equivalent`      | array         | Optional    | An array of json objects, each of which is a [reference](../../shared/reference) to an external identity and description of the current Person |
| `representation`  | array         | Optional    | An array of json objects, each of which is a reference to a [Visual Work](../visual_work) that represents the current Person, and MUST follow the requirements for a [reference](../../shared/reference/) |
| `member_of`       | array         | Optional    | An array of json objects, each of which is a Group that the current Person is a member of and MUST follow the requirements for a [reference](../../shared/reference/) to a **[Group](../group/)** |
| `subject_of`      | array         | Optional    | An array of json objects, each of which is a reference to a [Textual Work](../textual_work/), the content of which focuses on the current Person, and MUST follow the requirements for a [reference](../../shared/reference) |
| `attributed_by`   | array         | Optional    | An array of json objects, each of which is a [Relationship Assignment](../../shared/assignment/) that relates the current Person to another entity |
| `contact_point` | array | Optional | An array of json objects, each of which is an address at which the person is reachable and MUST follow the requirements for an [Identifier](../../shared/identifier) |
| `residence` | array | Optional | A place that the person was associated with, and MUST follow the requirements for a [reference](../../shared/reference/) to a [Place](../place/) |
| `carried_out` | array | Optional | An array of json objects, each of which represents professional activities of the person and follows the requirements for [Activities](../../shared/activity) |
| `participated_in` | array | Optional | An array of json objects, each of which represents an activity or event in which the person participated, but was not responsible, and follows the requirements for [Activities](../../shared/activity) |
| `born` | json object | Optional | A json object representing the birth of the person, which follows the requirements for a [Birth](../../shared/activity) | 
| `died` | json object | Optional | A json object representing the death of the person, which follows the requirements for a [Death](../../shared/activity) |

### Property Diagram

> ![diagram](person_properties.png){:.diagram_img width="600px"}

### JSON Schema

See the [schema documentation](../../schema_docs/person) and the [schema itself](../../schema/person.json)


### Incoming Properties

Person instances are typically found as the object of the following properties, other than the self-referential properties above.  This list is not exhaustive, but is intended to cover the likely cases where other endpoints refer to people.

| Property Name              | Source Endpoint | Description |
|----------------------------|-----------------|-------------|
| `carried_out_by`           | All             | An activity that the Person carried out |
| `current_owner`            | [Object](../physical_object/) | An object owned by the Person |
| `current_custodian`        | [Object](../physical_object/) | An object in the custody of the Person |
| `current_permanent_custodian` | [Object](../physical_object/) | An object that is normally in the custody of the Group |
| `represents`               | [Visual Work](../visual_work/)     | Image content which represents the Person (the inverse of `representation`) |
| `about`                    | [Textual Work](../textual_work/)    | Textual content that is about the Person |
| `transferred_custody_to`   | [Provenance](../provenance_activity/)      | The activity of transferring custody of an object to the Person |
| `transferred_custody_from` | [Provenance](../provenance_activity/)      | The activity of transferring custody of an object away from the Person |
| `transferred_title_to`     | [Provenance](../provenance_activity/)      | The activity of transferring ownership of an object to the Person |
| `transferred_title_from`   | [Provenance](../provenance_activity/)      | The activity of transferring ownership of an object away from the Person |
| `paid_to`                  | [Provenance](../provenance_activity/)      | The activity of paying money to the Person from someone else |
| `paid_from`                | [Provenance](../provenance_activity/)      | The activity of paying money from the Person to someone else |


## Example


The JSON for a Person entry for the artist Rembrandt could be as below.

* It has the Linked Art context reference in `@context`
* It self-documents its URI in `id`
* It has a `type` of "Person"
* It has a `_label` with the value "Rembrandt" for humans reading the JSON
* It has a `classified_as` property with entries for ...
    * ... Male, which is in turn `classified_as` a Gender
    * ... Dutch, which is in turn `classified_as` a Nationality
* It has an `identified_by` property, with a `Name` for his full name of "Rembrandt Harmenszoon van Rijn"
* It has a `referred_to_by` for a statement, `classified_as` a Biography
* It has a `born` property for his birth, with a `timespan` and a location in `took_place_at`.
* It has a `died` property for his death, with a `timespan` and a location in `took_place_at`.
* It has a `carried_out` for his professional activity, again with `timespan` and `took_place_at` properties, but also `classified_as` being professional activities
* It has an `equivalent` to his ULAN identity
* It has a `residence` with a reference to the Place where he lived
* It has a `contact_point` for his former street address 

```crom
top = model.Person(ident="auto int-per-segment", label="Rembrandt")
n = model.Name(content="Rembrandt Harmenszoon van Rijn")
top.identified_by = n
b = model.Birth(label="Birth of Rembrandt")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1606-07-15T00:00:00Z"
ts.end_of_the_end = "1606-07-16T00:00:00Z"
b.timespan = ts
p1 = model.Place(ident="auto int-per-segment", label="Leiden")
b.took_place_at = p1
top.born = b

d = model.Death(label="Death of Rembrandt")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1669-10-04T00:00:00Z"
ts.end_of_the_end = "1669-10-05T00:00:00Z"
d.timespan = ts
p2 = model.Place(ident="auto int-per-segment", label="Amsterdam")
d.took_place_at = p2
top.died = d

top.referred_to_by = vocab.BiographyStatement(
	content="Rembrandt was a Dutch draughtsman, painter and printmaker.")

top.classified_as = vocab.instances['male']
top.classified_as = vocab.instances['dutch nationality']

act = vocab.Active(label="Active Dates")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1631-01-01T00:00:00Z"
ts.end_of_the_end = "1669-10-05T00:00:00Z"
act.timespan = ts
act.took_place_at = p2
top.carried_out = act

top.residence = model.Place(label="Nieuwe Doelenstraat")
top.contact_point = vocab.StreetAddress(content="Jodenbreestraat 4, 1011NK Amsterdam")
top.equivalent = model.Person(ident="http://vocab.getty.edu/ulan/500011051", label="Rembrandt")


```
