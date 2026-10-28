---
title: "HAL Link: workRepresentsActivity"
---

## workRepresentsActivity

Return the works that are represent or depict the period, event or activity.

See the related [model documentation](/model/object/aboutness/#depiction)

### Example

From the record for the activity of the Battle of Bunker Hill, the record for the image created by Trumbull of the painting of the same name would be in the response

### Details

* Class Given: Temporal
* Returns Class: Work
* Relationship: 

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
    $current a crm:E4_Period .
  } UNION {
    $current a crm:E5_Event .
  } UNION {
    $current a crm:E7_Activity .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
  FILTER(isIRI(?work))
}
```
