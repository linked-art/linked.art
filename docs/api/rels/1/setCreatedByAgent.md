---
title: "HAL Link: setCreatedByAgent"
---

## setCreatedByAgent

Return the sets or collections that were created, in whole or in part, by the person or group.

See the related [model documentation](/model/collection/#features)

### Example

From the record for O.C. Marsh, the record for his archive would be in the response


### Details

* Class Given: Agent
* Returns Class: Set
* Relationship: createdBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX la: <https://linked.art/ns/terms/>

SELECT DISTINCT ?set
WHERE {
  {
    ?set crm:P94i_was_created_by ?activity .
  } UNION {
    ?activity crm:P94_has_created ?set .
  }
  {
    ?activity crm:P15_was_influenced_by $current .
  } UNION {
    $current crm:P15i_influenced ?activity .
  }
  {
    $current a crm:E22_Person .
  } UNION {
    $current a crm:E76_Group .
  }
  ?set a la:Set .
}
```
