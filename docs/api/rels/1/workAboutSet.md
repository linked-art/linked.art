---
title: "HAL Link: workAboutSet"
---

## workAboutSet

Return works which are about the set.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for the set for the Archives of O. C. Marsh, a text of an article about the archives would be in the response

### Details

* Class Given: Set
* Returns Class: Work
* Relationship: about

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .
PREFIX la: <https://linked.art/ns/terms/> .

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P129_is_about $current .
  } UNION {
    $current crm:P129i_is_subject_of ?work .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
  $current a la:Set .
}
```
