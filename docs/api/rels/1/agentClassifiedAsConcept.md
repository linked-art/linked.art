---
title: "HAL Link: agentClassifiedAsConcept"
---

## agentClassifiedAsConcept

Return the people or groups that are classified as the concept.

See the related [model documentation](/model/base/#types-and-classifications)

### Example

From the record for the concept of the Dutch nationality, the record for Rembrandt would be in the response

### Details

* Class Given: Concept
* Returns Class: Agent
* Relationship: classifiedAs

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?agent
WHERE {
  {
    ?agent crm:P2_has_type $current .
  } UNION {
    $current crm:P2i_is_type_of ?agent .
  }
}
```
