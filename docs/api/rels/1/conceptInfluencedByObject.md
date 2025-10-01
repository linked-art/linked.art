---
title: "HAL Link: conceptInfluencedByObject"
---

## conceptInfluencedByObject

Return the concepts that were influenced by the object.

See the related [model documentation](/model/concept/#creation-and-influences)

### Example

From the record for the Night Watch, the concept of the Reception of the Night Watch in the 19th Century would be in the response


### Details

* Class Given: HumanMadeObject
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
  $current a crm:E22_Human-Made_Object .
}
```
