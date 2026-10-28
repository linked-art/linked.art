---
title: "HAL Link: objectProducedByAgent"
---

## objectProducedByAgent

Return the objects that were produced, in whole or in part, by the person or group.

See the related [model documentation](/model/object/production/#base-production-activity)

### Example

From the record for Rembrandt, the record for The Night Watch would be in the response

### Details

* Class Given: Agent
* Returns Class: HumanMadeObject
* Relationship: producedBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P108i_was_produced_by/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P14_carried_out_by $current .
  } UNION {
    $current crm:P14i_performed/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P108_has_produced ?object .
  }
}
```
