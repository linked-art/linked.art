---
title: "HAL Link: agentMemberOfGroup"
---

## agentMemberOfGroup

Return the people or groups that are members of the group.

See the related [model documentation](/model/actor/#organization-membership)

### Example

From the record for Societe Anonyme, Katherine Dreier and Fortunato Depero would all be in the response


### Details

* Class Given: Group
* Returns Class: Agent
* Relationship: memberOf


### SPARQL
```
SELECT DISTINCT ?member WHERE {
   BIND (<%current%> AS ?group)
.   ?member crm:P107i_is_current_or_former_member_of ?group .
 }
```

