---
title: "HAL Link: workRepresentsWork"
---

## workRepresentsWork

Return the works that represent or depict the work.

See the related [model documentation](/model/object/aboutness/#depiction)

### Example




### Details

* Class Given: Work
* Returns Class: Work
* Relationship: represents

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P138_represents $current .
  } UNION {
    $current crm:P138i_has_representation ?work .
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
  FILTER(isIRI(?work))
}
```
