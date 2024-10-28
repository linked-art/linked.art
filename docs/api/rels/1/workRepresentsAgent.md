---
title: "HAL Link: workRepresentsAgent"
---

## workRepresentsAgent

Return the visual works that represent or depict the person or group.

See the related [model documentation](/model/object/aboutness/#depiction)

### Example

From the record for Sarah Hope Harvey Trumbull, the record for Sarah Trumbull with a Spaniel would be in the response.


### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: represents


### SPARQL
```
SELECT DISTINCT ?work WHERE {
    BIND (<https://lux.collections.yale.edu/data/person/b81ac68b-ab31-474e-ad1d-2ee95b1d26c1> AS ?who)
    ?work crm:P138_represents ?who .
 } 
```

