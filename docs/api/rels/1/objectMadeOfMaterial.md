---
title: "HAL Link: objectMadeOfMaterial"
---

## objectMadeOfMaterial

Return the objects which are made of the material.

See the related [model documentation](/model/object/physical/#materials)

### Example

From the record for Canvas, the record for The Night Watch would be in the response

### Details

* Class Given: Material
* Returns Class: HumanMadeObject
* Relationship: madeOf

### SPARQL

```
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P45_consists_of $current .
  } UNION {
    $current crm:P45i_is_incorporated_in ?object .
  }
  $current a crm:57_Material .
}
```
