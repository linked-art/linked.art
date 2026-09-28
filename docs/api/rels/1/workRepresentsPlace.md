---
title: "HAL Link: workRepresentsPlace"
---

## workRepresentsPlace

Return the visual works that represent or depict the place.

See the related [model documentation](/model/object/aboutness/#depiction)

### Example

From the record for Paris France, the record for Pissarro's "Boulevard Montmartre at Night" would be in the response

### Details

* Class Given: Place
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
  $current a crm:E53_Place .
  FILTER(isIRI(?work))
}
```
