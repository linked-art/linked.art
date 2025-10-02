---
title: "HAL Link: workAboutOrRepresentsAgent"
---

## workAboutOrRepresentsAgent

Return the works that are either about or depict the person or group.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for John Trumbull, the visual items and texts that depict him (such as a bibliographic record and a self-portrait) would be in the response

### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: about / represents

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
    $current a crm:E21_Person .
  } UNION {
    $current a crm:E76_Group .
  }
}
```
