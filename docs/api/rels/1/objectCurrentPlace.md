---
title: "HAL Link: objectCurrentPlace"
---

## objectCurrentPlace

Return the objects that are, as far as the system knows, currently at the place.

See the related [model documentation](/model/object/ownership/#location)

### Example

From the record for Getty's gallery W204, the record for Jeanne (Spring) would be in the response

### Details

* Class Given: Place
* Returns Class: HumanMadeObject
* Relationship: current

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P55_has_current_location $current .
  } UNION {
    $current crm:P55i_currently_holds ?object .
  }
  ?object a crm:E22_Human-Made_Object .
  $current a crm:E53_Place .
}
```
