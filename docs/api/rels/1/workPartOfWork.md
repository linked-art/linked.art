---
title: "HAL Link: workPartOfWork"
---

## workPartOfWork

Return the works that are part of the work.

See the related [model documentation](/model/document/#structure)

### Example

From the record for The Lord of the Rings, the record for The Fellowship of the Ring would be in the response

### Details

* Class Given: Work
* Returns Class: Work
* Relationship: partOf

### SPARQL

```
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    $current crm:P106i_forms_part_of ?work .
  } UNION {
    ?work crm:P106_is_composed_of ?work .
  }
  ?work a crm:E33_Linguistic_Object .
  FILTER(isIRI(?work))
}
```
