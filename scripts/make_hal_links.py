import json

#   {
#        "category": "agent",
#        "given": ["Person", "Group"],
#        "returns": ["HumanMadeObject"],
#        "where": "producedBy",
#        "name": "objectProducedByAgent",
#        "docs": "/model/object/production/#base-production-activity",
#        "description": "Returns the instances of HumanMadeObject produced by the given Person or Group",
#        "example": "Given Rembrandt, would return at the Night Watch painting"
#    }


fh = open("hal_links.json")
data = fh.read()
fh.close()
links = json.loads(data)

cats = ["all", "object", "work", "agent", "place", "concept", "event"]
per_cat = {}
for c in cats:
    per_cat[c] = []

## Write individual files, and an index

indiv_tmpl = """---
title: "Linked Art HAL Link: {name}"
---

## {name}

{description}

### Example {example}


* Class Given: {given}
* Returns Class: {returns}
* Relationship: {where}

"""

for l in links:
    fh = open(f"../docs/api/rels/1/{l['name']}.md", "w")
    fh.write(indiv_tmpl.format(**l))
    fh.close()
