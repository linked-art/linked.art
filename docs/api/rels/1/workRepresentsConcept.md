---
title: "HAL Link: workRepresentsConcept"
---

## workRepresentsConcept

Return the visual works that represent or depict the concept, or an instance of the concept

See the related [model documentation](/model/object/aboutness/#depiction)

### Example

From the record for the concept of Dogs, the record for the work of the Night Watch would be in the response (as the image depicts an unidentified dog)

### Details

* Class Given: Concept
* Returns Class: Work
* Relationship: represents

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P138_represents|crm:P199_represents_instance_of_type $current .
  } UNION {
    $current crm:P138i_has_representation|crm:P199i_has_instance_represented_by ?work .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
  $current a crm:E55_Type .
  FILTER(isIRI(?work))
}
```
