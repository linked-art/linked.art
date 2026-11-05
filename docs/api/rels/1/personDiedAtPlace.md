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

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?person
WHERE {
  {
    ?person crm:P100i_died_in ?death .
  } UNION {
    ?death crm:P100_was_death_of ?person .
  }
  {
    ?death crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?death .
  }
}
```
