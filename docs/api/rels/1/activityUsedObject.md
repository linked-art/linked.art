---
title: "HAL Link: activityUsedObject"
---

## activityUsedObject

Return the activities that used the object.

See the related [model documentation]()

### Example

From the record for the Night Watch, the record for the conservation work on the painting would be in the response

### Details

* Class Given: HumanMadeObject
* Returns Class: Activity
* Relationship: used

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?activity
WHERE {
  {
    ?activity crm:P31_has_modified $current .
  } UNION {
    $current crm:P31i_was_modified_by ?activity .
  }
}
```
