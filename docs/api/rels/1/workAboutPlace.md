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
   BIND(<https://lux.collections.yale.edu/data/place/8e117529-3872-494c-ab5f-8d7800be2c64> as ?where)
   ?work crm:P129_is_about ?where .
  }
```

