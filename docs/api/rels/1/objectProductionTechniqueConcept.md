---
title: "HAL Link: objectProductionTechniqueConcept"
---

## objectProductionTechniqueConcept

Return the objects whose production has a technique of the concept.

See the related [model documentation](/model/object/production/#techniques-and-classifications)

### Example

From the record for Bronze Casting, the record for The Thinker would be in the response 

### Details

* Class Given: Concept
* Returns Class: HumanMadeObject
* Relationship: productionTechnique

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P108i_was_produced_by/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P32_used_general_technique $current .
  } UNION {
    $current crm:P32i_was_technique_of/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P108_has_produced ?object .
  }
}
```
