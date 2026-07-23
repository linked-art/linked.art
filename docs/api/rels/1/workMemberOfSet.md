---
title: "HAL Link: workMemberOfSet"
---

## workMemberOfSet

Return works which are members of the set.

See the related [model documentation](/model/collection/#features)

### Example

From the record for the set of works which describe the Night Watch, the record for Bikker's "The Night Watch" would be in the response

### Details

* Class Given: Set
* Returns Class: Work
* Relationship: memberOf

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX la: <https://linked.art/ns/terms/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work la:member_of $current .
  } UNION {
    $current la:has_member ?work .
  }
  ?work a crm:E33_Linguistic_Object .
  FILTER(isIRI(?work))
}
```

> Require metatype for "Type of Work"?
