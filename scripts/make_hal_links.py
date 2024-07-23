import json

# https://docs.google.com/spreadsheets/d/185364qXkgnPRwI-ht-D1L9I-fACHfX-0zufiIwnLBNk/edit?pli=1&gid=0#gid=0


# Columns: Category Name    Returns Relationship    Given   Docs Link   Description SPARQL  Example


fh = open("hal_links.tsv")
data = fh.readlines()
fh.close()
data = data[1:]  # skip headers

cols = ["category", "name", "returns", "relationship", "given", "docs", "description", "sparql", "example"]

cats = ["object", "work", "agent", "place", "concept", "activity", "set"]
per_cat = {}
for c in cats:
    per_cat[c] = []

## Write individual files, and an index

indiv_tmpl = """---
title: "HAL Link: {name}"
---

## {name}

{description}

### Example

{example}

### Details

* Class Given: {given}
* Returns Class: {returns}
* Relationship: {relationship}


### SPARQL
```
{sparql}
```

"""

for row in data:
    l = row.split("\t")
    if l[0]:
        d = dict(zip(cols, l))
        d["sparql"] = d["sparql"].replace(" .", " .\n").replace(" {", " {\n").replace(")", ")\n").replace("} }", "}\n}")

        fh = open(f"../docs/api/rels/1/{d['name']}.md", "w")
        fh.write(indiv_tmpl.format(**d))
        fh.close()
        per_cat[d["category"]].append(d)


index = [
    """---
title: Linked Art HAL Links
---

## HAL Links

"""
]

for c in cats:
    ls = per_cat[c]
    ls.sort(key=lambda x: x["name"])
    index.append(f"### {c.title()}")
    index.append("")
    for l in ls:
        index.append("  * [{name}]({name}): {description}")

    index.append("")

index_str = "\n".join(index)
fh = open("../docs/api/rels/1/index.md", "w")
fh.write(index_str)
fh.close()
