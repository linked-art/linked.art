---
title: "HAL Link: workCreatedByAgent"
---

## workCreatedByAgent

Return the works that were created, in whole or in part, by the person or group.

See the related [model documentation](/model/document/#creation-and-publication)

### Example

From the record for André Chastel, the record for The Vatican Frescoes of Michelangelo would be in the response.

### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: createdBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P94i_was_created_by/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P14_carried_out_by $current .
  } UNION {
    $current crm:P7i_witnessed/(crm:P9i_forms_part_of|crm:P9_consists_of)*/crm:P14i_performed ?work .
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
