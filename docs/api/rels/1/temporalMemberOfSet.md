---
title: "HAL Link: temporalMemberOfSet"
---

## temporalMemberOfSet

Return periods, events and activities which are members of the set.

See the related [model documentation](/model/collection/#features)

### Example

From the record for the set of Linked Art face to face meetings, the record for the second face to face meeting in Oxford would be in the response

### Details

* Class Given: Set
* Returns Class: Temporal
* Relationship: memberOf

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .
PREFIX la: <https://linked.art/ns/terms/> .

SELECT DISTINCT ?temporal
WHERE {
  {
    ?temporal la:member_of $current .
  } UNION {
    $current la:has_member ?temporal .
  }
  {
    ?temporal a crm:E4_Period .
  } UNION {
    ?temporal a crm:E5_Event .
  } UNION {
    ?temporal a crm:E7_Activity .
  }
  $current a la:Set .
}
```
