---
title: "HAL Link: workCreatedAtPlace"
---

## workCreatedAtPlace

Return the works that were created, in whole or in part, at the place.

See the related [model documentation](/model/document/#creation-and-publication)

### Example

From the record for Oxford UK, the Lord of the Rings and the Hobbit would be in the response

### Details

* Class Given: Place
* Returns Class: Work
* Relationship: createdAt

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P94i_was_created_by/crm:P9_consists_of*/crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed/crm:P9i_forms_part_of*/crm:P94_has_created ?work .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
  $current a crm:E53_Place .
}
```
