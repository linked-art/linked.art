---
title: "HAL Link: activityTookPlaceAtPlace"
---

## activityTookPlaceAtPlace

Return the activities that took place at the place.

See the related [model documentation](/model/base/#events-and-activities)

### Example

From the record for New Haven, the record for the exhibition activity Life, Liberty and the Pursuit of Happiness would be in the response

### Details

* Class Given: Place
* Returns Class: Event, Activity
* Relationship: tookPlaceAt

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?activity
WHERE {
  {
    ?activity crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?activity .
  }
}
```
