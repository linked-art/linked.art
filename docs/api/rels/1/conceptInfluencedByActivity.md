---
title: "HAL Link: conceptInfluencedByActivity"
---

## conceptInfluencedByActivity

Return the concepts that were influenced by the period, event or activity.

See the related [model documentation](/model/concept/#creation-and-influences)

### Example

From the record for the 15th Century (a Period), the record for the History of France in the 15th Century would be in the response

### Details

* Class Given: Temporal
* Returns Class: Concept
* Relationship: 

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
}
```
