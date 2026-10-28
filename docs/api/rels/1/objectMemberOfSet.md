---
title: "HAL Link: objectMemberOfSet"
---

## objectMemberOfSet

Return objects which are members of the set.

See the related [model documentation](/model/collection/#features)

### Example

From the record for the Rijksmuseum's highlight objects, the record for the Night Watch would be in the response

### Details

* Class Given: Set
* Returns Class: HumanMadeObject
* Relationship: memberOf

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX la: <https://linked.art/ns/terms/>

SELECT DISTINCT ?object
WHERE {
  {
    ?object la:member_of $current .
  } UNION {
    $current la:has_member ?object .
  }
  $current a crm:E22_Human-Made_Object .
}
```
