---
title: "HAL Link: workRepresentsAgent"
---

## workRepresentsAgent

Return the visual works that represent or depict the person or group.

See the related [model documentation](/model/object/aboutness/#depiction)

### Example

From the record for Sarah Hope Harvey Trumbull, the record for Sarah Trumbull with a Spaniel would be in the response.


### Details

* Class Given: Agent
* Returns Class: Work
* Relationship: represents


### SPARQL
```
SELECT DISTINCT ?work WHERE {
    BIND (<%current%> AS ?who)
    ?work crm:P138_represents ?who .
 } 
```

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P138_represents $current .
  } UNION {
    $current crm:P138i_has_representation ?work .
  }
  {
    $current a crm:E21_Person .
  } UNION {
    $current a crm:E76_Group .
  }
  {
    ?work a crm:E33_Linguistic_Object .
  } UNION {
    ?work a crm:E36_Visual_Item .
  }
  FILTER(isIRI(?work))
}
```
