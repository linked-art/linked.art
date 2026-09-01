---
title: "HAL Link: conceptMemberOfSet"
---

## conceptMemberOfSet

Return concepts which are members of the set.

See the related [model documentation](/model/collection/#features)

### Example

From the record for the AAT concept scheme (a Set), the record for AAT's Primary Name concept would be in the response

### Details

* Class Given: Set
* Returns Class: Concept
* Relationship: memberOf

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX la: <https://linked.art/ns/terms/>

SELECT DISTINCT ?concept
WHERE {
  {
    ?concept la:member_of $current .
  } UNION {
    $current la:has_member ?concept .
  }
  ?concept a crm:E55_Type .
}
```
