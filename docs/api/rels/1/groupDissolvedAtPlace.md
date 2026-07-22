---
title: "HAL Link: groupDissolvedAtPlace"
---

## groupDissolvedAtPlace

Return the groups that were dissolved at the place.

See the related [model documentation](/model/actor/#birth-and-death-formation-and-dissolution)

### Example

From the record for New Haven Connecticut, the record for Société Anonyme would be in the response

### Details

* Class Given: Place
* Returns Class: Group
* Relationship: dissolvedAt

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?group
WHERE {
  {
    ?group crm:P99i_was_dissolved_by ?activity .
  } UNION {
    ?activity crm:P99_dissolved ?group .
  }
  {
    ?activity crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?activity .
  }
  $current a crm:E53_Place .
}
```
