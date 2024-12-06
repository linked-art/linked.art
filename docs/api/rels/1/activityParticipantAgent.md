---
title: "HAL Link: activityParticipantAgent"
---

## activityParticipantAgent

Return the activities in which the person or group participated but did not carry out directly.

See the related [model documentation]()

### Example

From the record for Tristan Tzara, the record for Cabaret Voltaire would be in the response. 


### Details

* Class Given: Agent
* Returns Class: Event, Activity
* Relationship: participant


### SPARQL
```
SELECT DISTINCT ?activity WHERE {
  ?activity crm:P11_had_participant <%current%>.  }
```

