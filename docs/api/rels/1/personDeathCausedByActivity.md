---
title: "HAL Link: personDeathCausedByActivity"
---

## personDeathCausedByActivity

Return the people whose death was caused by the event or activity.

See the related [model documentation]()

### Example

From the record for the Bubonic Plague, the record for a person who died of the plague would be in the response

### Details

* Class Given: Event,Activity
* Returns Class: Person
* Relationship: 

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?person
WHERE {
  {
    ?person crm:P100i_died_in ?death .
  } UNION {
    ?death crm:P100_was_death_of ?person .
  }
  {
    ?death sci:O13i_is_triggered_by $current .
  } UNION {
    $current sci:O13_triggered ?death .
  }
}
```
