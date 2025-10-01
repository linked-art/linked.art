---
title: "HAL Link: activityClassifiedAsConcept"
---

## activityClassifiedAsConcept

Return the activities that are classified as the concept.

See the related [model documentation](/model/base/#types-and-classifications)

### Example

From the record for the concept of Exhibitions, the record for "Manet and Modern Beauty" would be in the response

### Details

* Class Given: Concept
* Returns Class: Temporal
* Relationship: classifiedAs

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?activity
WHERE {
  {
    ?activity crm:P2_has_type $current .
  } UNION {
    $current crm:P2i_is_type_of ?activity .
  }
}
```
