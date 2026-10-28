---
title: "HAL Link: conceptCreationCausedByActivity"
---

## conceptCreationCausedByActivity

Return the concepts whose creation was caused by the event or activity.

See the related [model documentation]()

### Example




### Details

* Class Given: Event,Activity
* Returns Class: Concept
* Relationship: 

### SPARQL

```
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?concept
WHERE {
  {
    $current crm:P94i_was_created_by ?activity .
  } UNION {
    ?activity crm:P94_has_created $current .
  }
}
```
