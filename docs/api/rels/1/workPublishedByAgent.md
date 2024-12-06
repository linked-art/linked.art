---
title: "HAL Link: workPublishedByAgent"
---

## workPublishedByAgent

Return the works that are published by the person or group.

See the related [model documentation](/model/document/#creation-and-publication)

### Example

From the record for Bloomsbury Publishing, the record for Alias Grace would be in the response.


### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: publishedBy


### SPARQL
```
SELECT DISTINCT ?work WHERE {
    BIND(<%current%> AS ?who)
     ?work crm:P16i_was_used_for ?pub .
    ?pub crm:P14_carried_out_by ?who .
 } 
```

