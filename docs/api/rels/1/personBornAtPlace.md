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

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?person
WHERE {
  {
    ?person crm:P98i_was_born ?birth .
  } UNION {
    ?birth crm:P98_brought_into_life ?person .
  }
  {
   ?birth crm:P7_took_place_at $current .
  } UNION {
   $current crm:P7i_witnessed ?birth .
  }
}
```
