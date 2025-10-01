---
title: "HAL Link: placeMemberOfSet"
---

## placeMemberOfSet

Return places which are members of the set.

See the related [model documentation](/model/collection/#features)

### Example

From the record for the set of places in which Van Gogh lived, the record for Arles would be in the response

### Details

* Class Given: Set
* Returns Class: Place
* Relationship: memberOf

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .
PREFIX la: <https://linked.art/ns/terms/> .

SELECT DISTINCT ?place
WHERE {
  {
    ?place la:member_of $current .
  } UNION {
    $current la:has_member ?place .
  }
  $current a crm:E53_Place .
}
```
