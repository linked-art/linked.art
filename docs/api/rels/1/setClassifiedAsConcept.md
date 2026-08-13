---
title: "HAL Link: setClassifiedAsConcept"
---

## setClassifiedAsConcept

Return the sets that are classified as the concept.

See the related [model documentation](/model/base/#types-and-classifications)

### Example

From the record for the concept of Auction Lots, the record for Lot 14 would be in the response


### Details

* Class Given: Concept
* Returns Class: Set
* Relationship: classifiedAs


### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX la: <https://linked.art/ns/terms/>

SELECT DISTINCT ?set
WHERE {
  {
    ?set crm:P2_has_type $current .
  } UNION {
    $current crm:P2i_is_type_of ?set .
  }
  ?set a la:Set .
}
```
