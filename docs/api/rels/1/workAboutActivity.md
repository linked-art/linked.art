---
title: "HAL Link: workAboutActivity"
---

## workAboutActivity

Return the works that are about or have a subject of the period, event or activity.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for the Bronze Age, the record for a work about the Bronze Age would be in the response

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
    $current crm:P129_is_about ?work .
  } UNION {
    ?work crm:P129i_is_subject_of $current .
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
