---
title: "HAL Link: agentActiveAtPlace"
---

## agentActiveAtPlace

Return the people or groups who were active at the place.

See the related [model documentation](/model/actor/#active-dates)

### Example

From the record for Harlem, New York, the record for A.Philip Randolph would be in the response

### Details

* Class Given: Place
* Returns Class: Agent
* Relationship: activeAt

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?agent
WHERE {
  {
    $current crm:P7i_witnessed ?activity .
  } UNION {
    ?activity crm:P7_took_place_at $current .
  }
  {
    ?activity crm:P14_carried_out_by ?agent .
  } UNION {
    ?agent crm:P14i_perfomed ?activity .
  }
}
```
