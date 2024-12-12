---
title: "HAL Link: workAboutAgent"
---

## workAboutAgent

Return the works that are about or have a subject of the person or group.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for Abraham Lincoln, the record for We are Lincoln Men : Abraham Lincoln and his Friends would be in the response.


### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: about


### SPARQL
```
SELECT DISTINCT ?work WHERE {
    BIND(<%current%> AS ?who)
    ?work crm:P129_is_about ?who .
 } 
```

