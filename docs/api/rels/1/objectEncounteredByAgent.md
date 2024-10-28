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
```
SELECT DISTINCT ?object WHERE {
   BIND(<%current%> as ?who)
   ?object a crm:E22_Human-Made_Object ; sci:O19i_was_object_encountered_at ?enc .
   ?enc crm:P9_consists_of*/crm:P14_carried_out_by ?who .
  }
```

