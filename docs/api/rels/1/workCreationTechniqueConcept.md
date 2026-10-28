---
title: "HAL Link: workCreationTechniqueConcept"
---

## workCreationTechniqueConcept

Return the works whose creation has a technique of the concept.

See the related [model documentation]()

### Example

From the record for Sculpting, the record for the sculpture "Bather putting up her hair" would be in the response

### Details

* Class Given: Concept
* Returns Class: Work
* Relationship: creationTechnique

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P94i_was_created_by/(crm:P9_consists_of|crm:P9i_forms_part_of)*/sci:O13i_is_triggered_by $current .
  } UNION {
    $current crm:P7i_witnessed/(crm:P9i_forms_part_of|crm:P9_consists_of)*/sci:O13_triggers ?work .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
  $current a crm:E55_Type .
}
```
