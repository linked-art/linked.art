---
title: "HAL Link: workAboutConcept"
---

## workAboutConcept

Return the works that are about the concept.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for the concept of Democracy, the record for Diamond's work "In Search of Democracy" would be in the response

### Details

* Class Given: Concept
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
  $current a crm:E55_Type .
}
```
