---
title: "HAL Link: objectEncounteredByAgent"
---

## objectEncounteredByAgent

Return the objects that were discovered or encountered by the person or group.

See the related [model documentation](/model/object/production/#discovery-versus-production)

### Example

From the record for O.C. Marsh, the record for the Torosaurus holotype would be in the response

### Details

* Class Given: Agent
* Returns Class: HumanMadeObject
* Relationship: encounteredBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?object
WHERE {
  {
    ?object sci:O19i_was_object_encountered_at ?encounter .
  } UNION {
    ?encounter sci:O19_encountered_object ?object .
  }
  {
    ?encounter (crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P14_carried_out_by $current .
  } UNION {
    $current crm:P14i_performed/(crm:P9_consists_of|crm:P9i_forms_part_of)* ?encounter .
  }
}
```
