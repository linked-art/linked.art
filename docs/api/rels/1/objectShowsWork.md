---
title: "HAL Link: objectShowsWork"
---

## objectShowsWork

Return the objects that show the visual work.

See the related [model documentation](/model/object/aboutness/#physical-object-and-visual-work)

### Example

From the record for the image of the Night Watch, the record for the painting would be in the response

### Details

* Class Given: VisualItem
* Returns Class: HumanMadeObject
* Relationship: shows

### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?object
WHERE {
  {
    ?object crm:P65_shows_visual_item $current .
  } UNION {
    $current crm:P65i_is_shown_by ?object .
  }
}
```
