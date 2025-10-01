---
title: "HAL Link: conceptInfluencedByAgent"
---

## conceptInfluencedByAgent

Return the concepts that were influenced by the person or group.

See the related [model documentation](/model/concept/#creation-and-influences)

### Example

From the record for Rembrandt, the record for the concept 'Rembrandt -- Aesthetics' would be in the response

### Details

* Class Given: Agent
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
  {
    $current a crm:E21_Person .
  } UNION {
    $current a crm:E74_Group .
  }
}
```
