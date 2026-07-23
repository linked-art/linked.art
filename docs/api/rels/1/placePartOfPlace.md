---
title: "HAL Link: placePartOfPlace"
---

## placePartOfPlace

Return the places which are part of the place.

See the related [model documentation](/model/place/#core-information)

### Example

From the record for Île-de-France, the record for Paris would be in the response

### Details

* Class Given: Place
* Returns Class: Place
* Relationship: partOf

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?place
WHERE {
  {
    ?place crm:P89_falls_within $current .
  } UNION {
    $current crm:P89i_contains ?place .
  }
  ?place a crm:E53_Place .
}
```
