---
title: "HAL Link: groupFormedAtPlace"
---

## groupFormedAtPlace

Return the groups that were formed at the place.

See the related [model documentation](/model/actor/#birth-and-death-formation-and-dissolution)

### Example

From the record for Los Altos California, the record for Apple Computers would be in the response

### Details

* Class Given: Place
* Returns Class: Group
* Relationship: formedAt

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?group
WHERE {
  {
    ?group crm:P95i_was_formed_by ?activity .
  } UNION {
    ?activity crm:P95_has_formed ?group .
  }
  {
    ?activity crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?activity .
  }
  $current a crm:E53_Place .
}
```
