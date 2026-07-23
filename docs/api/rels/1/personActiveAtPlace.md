---
title: "HAL Link: personActiveAtPlace"
---

## personActiveAtPlace

Return the people who were active at the place.

See the related [model documentation](/model/actor/#active-dates)

### Example

From the record for Arles France, the record for Vincent Van Gogh would be in the response

### Details

* Class Given: Place
* Returns Class: Person
* Relationship: activeAt

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?person
WHERE {
  {
    ?person crm:P14i_performed/(crm:P9_consists_of|crm:P9i_forms_part_of)* ?activity .
  } UNION {
    ?activity (crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P14_carried_out_by ?person .
  }
  {
    ?activity crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?activity .
  }
  ?person a crm:E21_Person .
}
```
