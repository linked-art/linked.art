---
title: "HAL Link: workAboutPlace"
---

## workAboutPlace

Return the works that are about or have a subject of the place.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for Paris France, the record for Victor Hugo's work "Paris" would be in the response 


### Details

* Class Given: Place
* Returns Class: Work
* Relationship: about


### SPARQL
```
SELECT DISTINCT ?work WHERE {
   BIND(<%current%>as ?where)
   ?work crm:P129_is_about ?where .
  }
```

