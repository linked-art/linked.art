---
title: "HAL Link: objectOwnedByAgent"
---

## objectOwnedByAgent

Return the objects that are owned by the person or group.

### Example

From the record for the Rijksmuseum, the record for The Night Watch would be in the response.


### Details

* Class Given: Agent
* Returns Class: HumanMadeObject
* Relationship: ownedBy


### SPARQL
```
SELECT DISTINCT ?object WHERE {
   BIND(<%current%> as ?who)
   ?object a crm:E22_Human-Made_Object ; crm:P52_has_current_owner ?who .
 }
```

