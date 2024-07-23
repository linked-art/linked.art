---
title: "HAL Link: objectCuratedByAgent"
---

## objectCuratedByAgent

Return the objects that are curated, looked after, or otherwise are in the custody of the person or group.

See the related [model documentation](/model/object/ownership/#custody)

### Example

From the record for the Paintings Department of the Rijksmuseum, the record for The Night Watch would be in the response.


### Details

* Class Given: Agent
* Returns Class: HumanMadeObject
* Relationship: curatedBy


### SPARQL
```
SELECT DISTINCT ?object WHERE {
   BIND(<%current%> as ?who)
   {
     ?object a crm:E22_Human-Made_Object ; la:member_of ?coll .
     ?coll crm:P16i_was_used_for ?curating .
     ?curating crm:P14_carried_out_by ?who .
    } UNION {
     ?object crm:P50_has_current_keeper ?who .
   }
}
```

