---
title: "HAL Link: workAboutOrRepresentsPlace"
---

## workAboutOrRepresentsPlace

Return works that are about or depict the place.

See the related [model documentation](/model/object/aboutness/#subject)

### Example

From the record for Paris, the records for the image carried by a painting of Notre Dame and the text of a book about the city would be in the response

### Details

* Class Given: Place
* Returns Class: Work
* Relationship: about / represents


### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

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
  $current a crm:E53_Place .
}
```
