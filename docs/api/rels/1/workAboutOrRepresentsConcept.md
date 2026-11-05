---
title: "HAL Link: workAboutOrRepresentsConcept"
---

## workAboutOrRepresentsConcept

Return the works that are about or depict the concept.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for the concept of Law and Order, the record for the work of the Night Watch would be in the response

### Details

* Class Given: Concept
* Returns Class: Concept
* Relationship: about / represents

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

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
  $current a crm:E55_Type .
}
```
