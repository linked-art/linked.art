---
title: "HAL Link: workAboutOrRepresentsObject"
---

## workAboutOrRepresentsObject

Return the works that are about or represent the object.

See the related [model documentation](/model/object/aboutness/#subject)

### Example




### Details

* Class Given: HumanMadeObject
* Returns Class: Work
* Relationship: about / represents

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P129_is_about|crm:P138_represents $current .
  } UNION {
    $current crm:P129i_is_subject_of|crm:P138i_has_representation ?work .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
  $current a crm:E22_Human-Made_Object .
}
```
