---
title: "HAL Link: objectPartOfObject"
---

## objectPartOfObject

Return the objects that are part of the object.

See the related [model documentation](/model/object/physical/#parts)

### Example

From the record for the Night Watch, the record for the frame of the Night Watch would be in the response

### Details

* Class Given: HumanMadeObject
* Returns Class: HumanMadeObject
* Relationship: objectPartOfObject

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P46i_forms_part_of $current .
  } UNION {
    $current crm:P46_is_composed_of ?object .
  }
  ?object a crm:E22_Human-Made_Object .
}
```
