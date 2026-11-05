---
title: "HAL Link: workAboutOrRepresentsActivity"
---

## workAboutOrRepresentsActivity

Return the works that are about or represent the period, event or activity.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for the activity of the Battle of Bunker Hill, the records for the text of an article about it and the image of Trumbull's painting would both be in the response

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
    ?work crm:P129_is_about|crm:P138_represents $current .
  } UNION {
    $current crm:P129i_is_subject_of|crm:P138i_has_representation ?work .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
  {
    $current a crm:E4_Period .
  } UNION {
    $current a crm:E5_Event .
  } UNION {
    $current a crm:E7_Activity .
  }
}
```
