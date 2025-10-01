---
title: "HAL Link: objectClassifiedAsConcept"
---

## objectClassifiedAsConcept

Return the objects that are classified as the concept.

See the related [model documentation](/model/base/#types-and-classifications)

### Example

From the record for Paintings, the record for Sunflowers would be in the response

### Details

* Class Given: Concept
* Returns Class: HumanMadeObject
* Relationship: classifiedAs

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?object
WHERE {
  {
    $current crm:P2_has_type ?concept .
  } UNION {
    ?concept crm:P2i_is_type_of $current .
  }
  $current a crm:E22_Human-Made_Object .
}
```
