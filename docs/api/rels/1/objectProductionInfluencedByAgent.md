---
title: "HAL Link: objectProductionInfluencedByAgent"
---

## objectProductionInfluencedByAgent

Return the objects whose production was influenced by the person or group.

See the related [model documentation](/model/object/production/#inspirations-studies-or-copies)

### Example

From the record for Albert Bierstadt, the prints of his works (which were not necessarily created by him) would be in the response

### Details

* Class Given: Agent
* Returns Class: HumanMadeObject
* Relationship: productionInfluencedBy

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX sci: <http://www.ics.forth.gr/isl/CRMsci/>

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P108i_was_produced_by/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P15_was_influenced_by $current .
  } UNION {
    $current crm:P15i_influenced/(crm:P9_consists_of|crm:P9i_forms_part_of)*/crm:P108_has_produced ?object .
  }
  {
    $current a crm:E21_Person .
  } UNION {
    $current a crm:E74_Group .
  }
}
```
