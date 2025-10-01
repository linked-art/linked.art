---
title: "HAL Link: activityPartOfActivity"
---

## activityPartOfActivity

Return the periods, events or activities that were part of the period, event or activity.

See the related [model documentation](/model/base/#parts)

### Example

From the record for the Bronze Age, the record for the Middle Bronze Age would be in the response

### Details

* Class Given: Temporal
* Returns Class: Temporal
* Relationship: 

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?activity
WHERE {
  {
    ?activity crm:P9_consists_of $current .
  } UNION {
    $current crm:P9i_forms_part_of ?activity .
  }
}
```
