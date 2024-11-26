---
title: "HAL Link: workPublishedAtPlace"
---

## workPublishedAtPlace

Return the works that were published at the place.

See the related [model documentation](/model/document/#creation-and-publication)

### Example

From the record for Los Angeles, the Getty Exhibition catalog for Pacific Standard Time would be in the response


### Details

* Class Given: Place
* Returns Class: Work
* Relationship: publishedAt


### SPARQL
```
SELECT DISTINCT ?work WHERE {
     BIND(<%current%> as ?where)
     ?activity ^crm:P16i_was_used_for ?work ;         crm:P2_has_type <http://vocab.getty.edu/aat/300054686> ;         crm:P9_consists_of*/crm:P7_took_place_at ?where .
 } 
```

