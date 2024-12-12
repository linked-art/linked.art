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
```
SELECT DISTINCT ?objects WHERE {
  ?objects crm:P108i_was_produced_by ?production .
  ?production crm:P15_was_influenced_by <%current%>.  }
```

