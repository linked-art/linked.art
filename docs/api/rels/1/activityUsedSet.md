---
title: "HAL Link: activityUsedSet"
---

## activityUsedSet

Return activities which used the set.

See the related [model documentation](/model/exhibition/#exhibition-activity)

### Example

From the record for the set of objects shown in an exhibition, the record for the exhibition's activity would be in the response

### Details

* Class Given: Set
* Returns Class: Activity
* Relationship: used

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?activity
WHERE {
  {
    ?activity crm:P16_used_specific_object $current .
  } UNION {
    $current crm:P16i_was_used_for ?activity .
  }
}
```
