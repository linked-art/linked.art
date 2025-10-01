---
title: "HAL Link: workClassifiedAsConcept"
---

## workClassifiedAsConcept

Return the works that are classified as the concept.

See the related [model documentation](/model/base/#types-and-classifications)

### Example

From the record for Impressionism, the record for the work of Van Gogh's "Irises" would be in the response

### Details

* Class Given: Concept
* Returns Class: Work
* Relationship: classifiedAs

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .
PREFIX la: <https://linked.art/ns/terms/> .

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P2_has_type $current .
  } UNION {
    $current crm:P2i_is_type_of ?work .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
}
```
