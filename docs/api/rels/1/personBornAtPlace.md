---
title: "HAL Link: personBornAtPlace"
---

## personBornAtPlace

Return the people who were born at the place.

See the related [model documentation](/model/actor/#birth-and-death-formation-and-dissolution)

### Example

From the record for Leiden, the record for Rembrandt would be in the response


### Details

* Class Given: Place
* Returns Class: Person
* Relationship: bornAt


### SPARQL
```
SELECT DISTINCT ?agent WHERE {
   BIND(<%current%>as ?where)
   ?agent crm:P98i_was_born ?birth .
    ?birth crm:P7_took_place_at ?where .
 }
```

