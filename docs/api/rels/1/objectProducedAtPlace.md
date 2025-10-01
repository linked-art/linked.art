---
title: "HAL Link: objectProducedAtPlace"
---

## objectProducedAtPlace

Return the objects that were produced, in whole or in part, at the place.

See the related [model documentation](/model/object/production/#base-production-activity)

### Example

From the record for Amsterdam, the record for The Night Watch would be in the response

### Details

* Class Given: Place
* Returns Class: HumanMadeObject
* Relationship: producedAt

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P108i_was_produced_by/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P108_has_produced ?object .
  }
  ?object a crm:E22_Human-Made_Object .
}
```
