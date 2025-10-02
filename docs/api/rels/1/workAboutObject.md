---
title: "HAL Link: workAboutObject"
---

## workAboutObject

Return the works that are about or have a subject of the object.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for the Night Watch, the record for Bikker's "The Night Watch" would be in the response

### Details

* Class Given: HumanMadeObject
* Returns Class: Work
* Relationship: about

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P129_is_about $current .
  } UNION {
    $current crm:P129i_is_subject_of ?work .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
  $current a crm:E22_Human-Made_Object .
}
```
