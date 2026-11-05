---
title: "HAL Link: workPublishedAtPlace"
---

## workPublishedAtPlace

Return the works that were published at the place.

See the related [model documentation](/model/document/#creation-and-publication)

### Example

From the record for Los Angeles, the Getty Exhibition catalog for Pacific Standard Time would be in the response

### Details

* Class Given: Place
* Returns Class: Work
* Relationship: publishedAt

### SPARQL

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
    ?activity crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed ?activity .
  }
  ?work a crm:E33_Linguistic_Object .
  FILTER(isIRI(?work))
}
```
