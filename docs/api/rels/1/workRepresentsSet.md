---
title: "HAL Link: workRepresentsSet"
---

## workRepresentsSet

Return visual works which represent or depict the set.

See the related [model documentation](/model/object/aboutness/#depiction)

### Example

From the record for the set for the Archives of O. C. Marsh, an image that depicts the archive would be in the response

### Details

* Class Given: Set
* Returns Class: Work
* Relationship: represents

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX la: <https://linked.art/ns/terms/>

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
  $current a la:Set .
  FILTER(isIRI(?work))
}
```
