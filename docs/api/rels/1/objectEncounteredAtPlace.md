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

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/> .

SELECT DISTINCT ?object
WHERE {
  {
    ?object sci:O19i_was_object_encountered_at ?encounter .
  } UNION {
    ?encounter sci:O19_encountered_object ?object .
  }
  {
    ?encounter crm:P9_consists_of*/crm:P7_took_place_at $current .
  } UNION {
    $current crm:P7i_witnessed/crm:P9i_forms_part_of* ?encounter .
  }
}
```

> [!WARNING]
> In CRMsci 3.0 `O19` is named:
> > O19 encountered object (was object encountered through)
> > -- <https://cidoc-crm.org/sites/default/files/CRMsci-v3.0i.i.i.pdf>

