---
title: "HAL Link: objectDestructionCausedByActivity"
---

## objectDestructionCausedByActivity

Return the objects whose destruction was caused by the event or activity.

See the related [model documentation](/model/object/production/#cause-of-destruction)

### Example

From the record for a fire that destroyed a museum, the record for an object destroyed in the fire would be in the response

### Details

* Class Given: Event,Activity
* Returns Class: HumanMadeObject
* Relationship: 

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P13i_was_destroyed_by $current .
  } UNION {
    $current crm:P13_destroyed ?object .
  }
  ?object a crm:E22_Human-Made_Object .
}
```
