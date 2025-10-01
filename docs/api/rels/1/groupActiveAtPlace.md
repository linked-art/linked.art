---
title: "HAL Link: groupActiveAtPlace"
---

## groupActiveAtPlace

Return the groups who were active at the place.

See the related [model documentation](/model/actor/#active-dates)

### Example

From the record for Paris France, the record for Goupil & Cie would be in the response

### Details

* Class Given: Place
* Returns Class: Group
* Relationship: activeAt

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?group
WHERE {
  {
    ?group crm:P14i_performed ?activity .
  } UNION {
    ?activity crm:P14_carried_out_by ?group .
  }
  {
    ?activity crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?activity .
  }
  $current a crm:E53_Place .
}
```
