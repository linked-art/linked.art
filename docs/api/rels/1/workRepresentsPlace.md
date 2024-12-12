---
title: "HAL Link: workRepresentsPlace"
---

## workRepresentsPlace

Return the visual works that represent or depict the place.

See the related [model documentation](/model/object/aboutness/#depiction)

### Example

From the record for Paris France, the record for Pissarro's "Boulevard Montmartre at Night" would be in the response


### Details

* Class Given: Place
* Returns Class: Work
* Relationship: represents


### SPARQL
```
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> SELECT DISTINCT ?work WHERE {
   BIND(<%current%>as ?where)
   ?work crm:P138_represents ?where .
  }
```

