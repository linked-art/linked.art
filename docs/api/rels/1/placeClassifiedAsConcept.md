---
title: "HAL Link: placeClassifiedAsConcept"
---

## placeClassifiedAsConcept

Return the places that are classified as the concept.

See the related [model documentation](/model/base/#types-and-classifications)

### Example

From the record for the concept of Cities, the record for Amsterdam would be in the response

### Details

* Class Given: Concept
* Returns Class: Place
* Relationship: classifiedAs

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?place
WHERE {
  {
    ?place crm:P2_has_type $current .
  } UNION {
    $current crm:P2i_is_type_of ?place .
  }
  ?place a crm:E53_Place .
}
```
