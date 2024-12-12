---
title: "HAL Link: workCreatedByAgent"
---

## workCreatedByAgent

Return the works that were created, in whole or in part, by the person or group.

See the related [model documentation](/model/document/#creation-and-publication)

### Example

From the record for André Chastel, the record for The Vatican Frescoes of Michelangelo would be in the response.


### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: createdBy


### SPARQL
```
SELECT DISTINCT ?work WHERE {
   BIND(<%current%> as ?who)
     ?work crm:P94i_was_created_by ?cre .
         ?cre crm:P9_consists_of*/crm:P14_carried_out_by ?who .
 }
```

