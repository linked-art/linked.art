---
title: "HAL Link: groupFormedAtPlace"
---

## groupFormedAtPlace

Return the groups that were formed at the place.

See the related [model documentation](/model/actor/#birth-and-death-formation-and-dissolution)

### Example

From the record for Los Altos California, the record for Apple Computers would be in the response


### Details

* Class Given: Place
* Returns Class: Group
* Relationship: formedAt


### SPARQL
```
SELECT DISTINCT ?group WHERE {
   BIND(<https://lux.collections.yale.edu/data/place/9889853b-2bf1-4d52-83eb-629158f96067> as ?where)
   ?group crm:P95i_was_formed_by ?formation .
    ?formation crm:P7_took_place_at ?where .
 }
```

