---
title: "HAL Link: objectCarriesWork"
---

## objectCarriesWork

Return the objects that carry the linguistic work.

See the related [model documentation](/model/document/#physical-objects-conceptual-texts)

### Example

From the record for the Lord of the Rings, the record for the copy in the British Library would be in the response

### Details

* Class Given: LinguisticObject
* Returns Class: HumanMadeObject
* Relationship: carries

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?object
WHERE {
  {
    $current crm:P128_carries ?textualWork .
  } UNION {
    ?textualWork crm:P128i_is_carried_by $current .
  }
  ?textualWork a crm:E33_Linguistic_Object .
  $current a crm:E22_Human-Made_Object .
}
```
