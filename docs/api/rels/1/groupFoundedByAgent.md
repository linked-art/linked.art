---
title: "HAL Link: groupFoundedByAgent"
---

## groupFoundedByAgent

Return the groups that were founded by the person or group.

See the related [model documentation](/model/actor/#birth-and-death-formation-and-dissolution)

### Example

From the record for Katherine Dreier, Man Ray or Marcel Duchamps, the group Societe Anonyme would be in the response

### Details

* Class Given: Agent
* Returns Class: Group
* Relationship: foundedBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?group
WHERE {
  {
    ?group crm:P95i_was_formed_by ?activity .
  } UNION {
    ?activity crm:P95_has_formed ?group .
  }
  {
    ?activity ccrm:P14_carried_out_by $current .
  } UNION {
    $current crm:P14i_performed ?activity .
  }
  {
    $current a crm:E21_Person .
  } UNION {
    $current a crm:E74_Group .
  }
}
```
