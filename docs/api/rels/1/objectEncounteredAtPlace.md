---
title: "HAL Link: objectEncounteredAtPlace"
---

## objectEncounteredAtPlace

Return the objects that were encountered at the place.

See the related [model documentation](/model/object/production/#discovery-versus-production)

### Example

From the record for the Burgess Shale, the record for Anomalocaris Canadiensis would be in the response


### Details

* Class Given: Place
* Returns Class: HumanMadeObject
* Relationship: encounteredAt


### SPARQL
```
SELECT DISTINCT ?object WHERE {
     BIND(<%current%> as ?where)
     ?object a crm:E22_Human-Made_Object ;         sci:O19i_was_object_found_by/crm:P9_consists_of*/crm:P7_took_place_at ?where .
  }
```

