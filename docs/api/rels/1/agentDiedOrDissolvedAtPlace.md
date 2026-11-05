---
title: "HAL Link: agentDiedOrDissolvedAtPlace"
---

## agentDiedOrDissolvedAtPlace

Return the people or groups who died or were dissolved at the place.

See the related [model documentation](/model/actor/#birth-and-death-formation-and-dissolution)

### Example

From the record for Harlem, New York, the record for Howard Johnson-1941-2021 would be in the response

### Details

* Class Given: Place
* Returns Class: Agent
* Relationship: died / dissolved

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?agent
WHERE {
  {
    ?agent crm:P100i_died_in|crm:P95i_was_formed_by ?activity .
  } UNION {
    ?activity crm:P100_was_death_of|crm:P99_dissolved ?agent .
  }
  {
    ?activity crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?activity .
  }
}
```
