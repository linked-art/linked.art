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
```
SELECT DISTINCT ?object WHERE {
   BIND(<%current%> as ?who)
   ?object a crm:E22_Human-Made_Object ; crm:P108i_was_produced_by ?prod .
   ?prod crm:P9_consists_of*/crm:P14_carried_out_by ?who .
  }
```

