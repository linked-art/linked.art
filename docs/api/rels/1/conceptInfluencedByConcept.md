---
title: "HAL Link: conceptInfluencedByConcept"
---

## conceptInfluencedByConcept

Return the concepts that are influenced by the concept.

See the related [model documentation](/model/concept/#creation-and-influences)

### Example

From the record for the concept of History, the record for History of France would be in the response

### Details

* Class Given: Concept
* Returns Class: Concept
* Relationship: influencedBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?concept
WHERE {
  {
    $current crm:P94i_was_created_by ?activity .
  } UNION {
    ?activity crm:P94_has_created ?concept .
  }
  {
    ?activity crm:P15_was_influenced_by $current .
  } UNION {
    $current crm:P15i_influenced ?activity .
  }
  $current a crm:E55_Type .
}
```
