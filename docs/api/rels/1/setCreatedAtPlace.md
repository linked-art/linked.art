---
title: "HAL Link: setCreatedAtPlace"
---

## setCreatedAtPlace

Return the sets which were created at the place.

See the related [model documentation](/model/collection/#features)

### Example

From the record for New Haven, the record for the set representing the Archives of O. C. Marsh would be in the response

### Details

* Class Given: Place
* Returns Class: Set
* Relationship: createdAt

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
    ?activity crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?activity .
  }
  ?set a la:Set .
}
```


