---
title: "HAL Link: objectProductionCausedByActivity"
---

## objectProductionCausedByActivity

Return the objects whose production was caused by the event or activity.

See the related [model documentation](/model/object/production/#cause-of-production)

### Example

From the record for a commission activity, the record for the object that was produced because of the commission would be in the response

### Details

* Class Given: Event,Activity
* Returns Class: HumanMadeObject
* Relationship: productionCausedBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .
PREFIX sci: <http://www.ics.forth.gr/isl/CRMsci/> .

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P108i_was_produced_by/(crm:P9_consists_of|crm:P9i_forms_part_of)*/sci:O13i_is_triggered_by $current .
  } UNION {
    $current sci:O13_triggers/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P108_has_produced ?object .
  }
}
```

