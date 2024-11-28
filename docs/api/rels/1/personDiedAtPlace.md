---
title: "HAL Link: personDiedAtPlace"
---

## personDiedAtPlace

Return the people who died at the place.

See the related [model documentation](/model/actor/#birth-and-death-formation-and-dissolution)

### Example

From the record for Amsterdam, the record for Rembrandt would be in the response


### Details

* Class Given: Place
* Returns Class: Person
* Relationship: diedAt


### SPARQL
```
SELECT DISTINCT ?person WHERE {
   BIND(<https://lux.collections.yale.edu/data/place/fff6ea51-e555-4b4e-92b1-8b378d0f913b> as ?where)
   ?person crm:P100i_died_in ?death .
    ?death crm:P7_took_place_at ?where .
 }
```

