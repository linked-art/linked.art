---
title: "HAL Link: groupDissolvedAtPlace"
---

## groupDissolvedAtPlace

Return the groups that were dissolved at the place.

See the related [model documentation](/model/actor/#birth-and-death-formation-and-dissolution)

### Example

From the record for New Haven Connecticut, the record for Société Anonyme would be in the response


### Details

* Class Given: Place
* Returns Class: Group
* Relationship: dissolvedAt


### SPARQL
```
SELECT DISTINCT ?group WHERE {
   BIND(<%current%>as ?where)
   ?group crm:P99i_was_dissolved_by ?dissolution .
    ?dissolution crm:P7_took_place_at ?where .
 }
```

