---
title: "HAL Link: activityCarriedOutByAgent"
---

## activityCarriedOutByAgent

Return the activities that were carried out by the person or group.

See the related [model documentation](/model/base/#events-and-activities /model/exhibition/#exhibition-activity)

### Example

From the record for the National Gallery of Art, the record for the Manet exhibition activity would be in the response

### Details

* Class Given: Agent
* Returns Class: Activity
* Relationship: carriedOutBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?activity
WHERE {
  {
    ?activity crm:P14_carried_out_by $current .
  } UNION {
    $current crm:P14i_performed ?activity .
  }
}
```
