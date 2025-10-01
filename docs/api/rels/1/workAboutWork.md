---
title: "HAL Link: workAboutWork"
---

## workAboutWork

Return the works that are about or have a subject of the work.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for The Lord of the Rings, the record for an article about Tolkien's work would be in the response

### Details

* Class Given: Work
* Returns Class: Work
* Relationship: about

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

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
  {
    $current a crm:E33_Linguistic_Object .
  } UNION {
    $current a crm:E36_Visual_Item .
  }
}
```
