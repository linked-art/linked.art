---
title: "HAL Link: setCreationCausedByActivity"
---

## setCreationCausedByActivity

Return the sets whose creation was caused by the event or activity.

See the related [model documentation]()

### Example




### Details

* Class Given: Event,Activity
* Returns Class: Set
* Relationship: 


### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .
PREFIX la: <https://linked.art/ns/terms/> .
PREFIX sci: <http://www.ics.forth.gr/isl/CRMsci/> .

SELECT DISTINCT ?object
WHERE {
  {
    ?set crm:P94i_was_created_by/(crm:P9_consists_of|crm:P9i_forms_part_of)*/sci:O13i_is_triggered_by ?activity .
  } UNION {
    ?activity sci:O13_triggers/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P94_has_created ?set .
  }
  ?set a la:Set .
}
```
