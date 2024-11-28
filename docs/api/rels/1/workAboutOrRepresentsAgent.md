---
title: "HAL Link: workAboutOrRepresentsAgent"
---

## workAboutOrRepresentsAgent

Return the works that are either about or depict the person or group.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for John Trumbull, the visual items and texts that depict him (such as a bibliographic record and a self-portrait) would be in the response


### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: about / represents


### SPARQL
```
SELECT DISTINCT ?work WHERE {
   {
     ?work crm:P138_represents <https://lux.collections.yale.edu/data/person/c225d5e4-8767-4a25-802b-af054d5e8f52> .
   }   UNION   {
     ?work crm:P129_is_about <https://lux.collections.yale.edu/data/person/c225d5e4-8767-4a25-802b-af054d5e8f52> .
   }
}
```

