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

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?agent
WHERE {
  {
    ?agent crm:P107i_is_current_or_former_member_of $current .
  } UNION {
    $current crm:P107_has_current_or_former_member ?agent .
  }
}
```
