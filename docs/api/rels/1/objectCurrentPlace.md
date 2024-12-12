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
```
SELECT DISTINCT ?object WHERE {
     BIND(<%current%> as ?where)
     ?object a crm:E22_Human-Made_Object ;         crm:P55_has_current_location ?where }
```

