---
title: "HAL Link: agentResidentAtPlace"
---

## agentResidentAtPlace

Return the people or groups who are or were resident at the place.

See the related [model documentation](/model/actor/#residence-as-a-place)

### Example

From the record for Brooklyn, New York the record for E.V. Day would be in the response

### Details

* Class Given: Place
* Returns Class: Agent
* Relationship: residenceAt

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?agent
WHERE {
  {
    ?agent crm:P74_has_current_or_former_residence $current .
  } UNION {
    $current crm:P74i_is_current_or_former_residence_of ?agent .
  }
}
```
