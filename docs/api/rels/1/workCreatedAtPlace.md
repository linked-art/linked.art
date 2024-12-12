---
title: "HAL Link: workCreatedAtPlace"
---

## workCreatedAtPlace

Return the works that were created, in whole or in part, at the place.

See the related [model documentation](/model/document/#creation-and-publication)

### Example

From the record for Oxford UK, the Lord of the Rings and the Hobbit would be in the response


### Details

* Class Given: Place
* Returns Class: Work
* Relationship: createdAt


### SPARQL
```
SELECT DISTINCT ?work WHERE {
   BIND(<%current%> as ?where)
   ?work crm:P94i_was_created_by/crm:P9_consists_of*/crm:P7_took_place_at ?where .
  }
```

