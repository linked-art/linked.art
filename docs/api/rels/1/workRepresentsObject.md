---
title: "HAL Link: workRepresentsObject"
---

## workRepresentsObject

Return the visual works that represent or depict the object.

See the related [model documentation](/model/object/aboutness/#depiction)

### Example

From the record for the Night Watch, the record for a photograph of the Night Watch would be in the response

### Details

* Class Given: HumanMadeObject
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
  $current a crm:E21_Human-Made_Object .
  FILTER(isIRI(?work))
}
```
