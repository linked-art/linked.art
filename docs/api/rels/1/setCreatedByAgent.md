---
title: "HAL Link: setCreatedByAgent"
---

## setCreatedByAgent

Return the sets or collections that were created, in whole or in part, by the person or group.

See the related [model documentation](/model/collection/#features)

### Example

From the record for O.C. Marsh, the record for his archive would be in the response


### Details

* Class Given: Agent
* Returns Class: Set
* Relationship: createdBy


### SPARQL
```
SELECT DISTINCT ?set WHERE {
   ?set crm:P94i_was_created_by ?creation .
    ?creation crm:P15_was_influenced_by <%current%>. }
```

