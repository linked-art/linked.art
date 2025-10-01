---
title: "HAL Link: activityUsedWork"
---

## activityUsedWork

Return the activities that used the work.

See the related [model documentation]()

### Example




### Details

* Class Given: Work
* Returns Class: Activity
* Relationship: used

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?activity
WHERE {
  {
    ?activity crm:P15_was_influenced_by $current .
  } UNION {
    $current crm:P15i_influenced ?activity .
  }
}
```
