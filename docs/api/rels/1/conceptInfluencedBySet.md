---
title: "HAL Link: conceptInfluencedBySet"
---

## conceptInfluencedBySet

Return concepts which were influenced by the set.

See the related [model documentation](/model/concept/#creation-and-influences)

### Example




### Details

* Class Given: Set
* Returns Class: Concept
* Relationship: influencedBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX la: <https://linked.art/ns/terms/>

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
  $current a la:Set .
}
```
