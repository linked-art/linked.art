---
title: "HAL Link: conceptClassifiedAsConcept"
---

## conceptClassifiedAsConcept

Return the concepts that are classified as the concept.

See the related [model documentation](/model/concept/#partitioning-versus-classification)

### Example

From the record for the concept of Nationalities, the record for Dutch would be in the response

### Details

* Class Given: Concept
* Returns Class: Concept
* Relationship: classifiedAs

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?concept
WHERE {
  {
    $current crm:P2_has_type ?concept .
  } UNION {
    ?concept crm:P2i_is_type_of $current .
  }
}
```
