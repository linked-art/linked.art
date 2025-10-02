---
title: "HAL Link: workAboutOrRepresentsSet"
---

## workAboutOrRepresentsSet

Return the works which are about or represent the set.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for the set for the Archives of O. C. Marsh, the records for an article about the archive and an image of the archive would be in the response

### Details

* Class Given: Set
* Returns Class: Work
* Relationship: about / represents

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX la: <https://linked.art/ns/terms/>

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
  $current a la:Set .
}
```
