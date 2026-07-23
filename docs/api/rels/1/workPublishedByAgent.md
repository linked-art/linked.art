---
title: "HAL Link: workPublishedByAgent"
---

## workPublishedByAgent

Return the works that are published by the person or group.

See the related [model documentation](/model/document/#creation-and-publication)

### Example

From the record for Bloomsbury Publishing, the record for Alias Grace would be in the response.


### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: publishedBy


### SPARQL
```
SELECT DISTINCT ?work WHERE {
    BIND(<%current%> AS ?who)
     ?work crm:P16i_was_used_for ?pub .
    ?pub crm:P14_carried_out_by ?who .
 } 
```


```
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P16i_was_used_for/(crm:P9_consists_of|crm:P9i_forms_part_of)* ?activity .
  } UNION {
    ?activity (crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P16_used_specific_object ?work .
  }
  {
    ?activity crm:P2_has_type <http://vocab.getty.edu/aat/300054686> .
  } UNION {
    <http://vocab.getty.edu/aat/300054686> crm:P2i_is_type_of ?activity .
  }
  {
    ?activity crm:P14_carried_out_by $current .
  } UNION {
    $current crm:P14i_performed ?activity .
  }
  ?work a crm:E33_Linguistic_Object .
  FILTER(isIRI(?work))
}
```
