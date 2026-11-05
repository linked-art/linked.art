---
title: "HAL Link: agentBornOrFormedAtPlace"
---

## agentBornOrFormedAtPlace

Return the people or groups who were born or formed at the place.

See the related [model documentation](/model/actor/#birth-and-death-formation-and-dissolution)

### Example

From the record for Harlem, New York, the record for Ayize Jama-Everett would be in the response

### Details

* Class Given: Place
* Returns Class: Agent
* Relationship: born / formed

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?agent
WHERE {
  {
    ?agent crm:P98i_was_born|crm:P95i_was_formed_by ?activity .
  } UNION {
    ?activity crm:P98_brought_into_life|crm:P95_has_formed ?agent .
  }
  {
    ?activity crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?activity .
  }
}
```
