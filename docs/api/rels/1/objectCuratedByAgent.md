---
title: "HAL Link: objectCuratedByAgent"
---

## objectCuratedByAgent

Return the objects that are curated, looked after, or otherwise are in the custody of the person or group.

See the related [model documentation](/model/object/ownership/#custody)

### Example

From the record for the Paintings Department of the Rijksmuseum, the record for The Night Watch would be in the response.

### Details

* Class Given: Agent
* Returns Class: HumanMadeObject
* Relationship: curatedBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?object
WHERE {
  {
    ?object la:member_of ?set .
  } UNION {
    ?set la:has_member ?object .
  }
  {
    ?object crm:P50_has_current_keeper $current .
  } UNION {
    $current crm:P50i_is_current_keeper_of ?object .
  }
  {
    ?set crm:P16i_was_used_for ?activity .
  } UNION {
    ?activity crm:P16_used_specific_object ?set .
  }
  {
    ?activity crm:P14_was_carried_out_by $current .
  } UNION {
    $current crm:P14i_performed ?activity .
  }
  ?object a crm:E22_Human-Made_Object .
}
```
