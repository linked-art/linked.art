---
title: "HAL Link: workCreatedByAgent"
---

## workCreatedByAgent

Return the works that were created, in whole or in part, by the person or group.

See the related [model documentation](/model/document/#creation-and-publication)

### Example




### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: createdBy


### SPARQL
```
SELECT DISTINCT ?work WHERE {
   BIND(<https://lux.collections.yale.edu/data/person/5bc822aa-1312-4ae5-8f24-1709f7ebda17> as ?who)
     ?work crm:P94i_was_created_by ?cre .
         ?cre crm:P9_consists_of*/crm:P14_carried_out_by ?who .
 }
```

