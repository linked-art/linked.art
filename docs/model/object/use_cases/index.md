---
title: "Objects: Use Cases and Vocabulary"
up_href: "/model/object/"
up_label: "Objects"
---

[TOC]

## Introduction


## Types and Classifications

All objects that are considered to be works of art should be have the "works of art" classification: _aat:300133025_.  This will allow systems to distinguish between art objects and others that may be managed in the same dataset, but are not themselves art.  These non-art objects might include tools (pencils, paintbrushes, palette, chisel), documents (a copy of an auction catalog, a letter from the artist), or supporting objects (an aisel, case or shelf).


```crom
top = Sculpture(art=1)
top._label = "Sculpture of a Dragon"
```


### Vocabulary Entries

__Visual Works__

| AAT Term       | Label                | Usage Notes                   |
| -------------- | -------------------- | ----------------------------- |
 _aat:300133025_ | works of art         | Should be used for all objects considered as art, as well as entries from below, or other
 _aat:300014063_ | textiles             |
 _aat:300015342_ | mosaics              |
 _aat:300151343_ | ceramics             | 
 _aat:300033618_ | paintings            |  
 _aat:300033963_ | collages             |
 _aat:300033973_ | drawings             |
 _aat:300041273_ | prints               |
 _aat:300047090_ | sculpture            | 
 _aat:300047203_ | carvings             |
 _aat:300047896_ | installations        |
 _aat:300046300_ | photographs          |
 _aat:300127173_ | negatives            | 
 _aat:300028569_ | manuscripts          | 


__Objects__

| AAT Term       | Label                | Usage Notes                   |
| -------------- | -------------------- | ----------------------------- |
 _aat:300387350_ | exchange media       | For coins, stamps, tickets, coupons etc
 _aat:300037336_ | furnishings          | For furniture and furnishings
 _aat:300266639_ | clothing             | For anything that is worn on the body, made of cloth or metal or other
 _aat:300209273_ | costume accessories  | For jewelry and other worn or held accessories
 _aat:300036926_ | weapons              | 
 _aat:300197197_ | containers           | For boxes, baskets, vessels of all types
 _aat:300117130_ | fragments            | For small, separated pieces


## Names and Identifiers

### Names

The title of the object is given as its Name. Different types of name or title can be distinguished by associating appropriate vocabulary entries via `classified_as`.

There are currently none documented beyond the primary title.

### Identifiers

Objects can have many different types of identifier, following the basic pattern.

Use cases for identifiers of objects include:

* Accession numbers
* Local database numbers
* Stock numbers
 
```crom
top = Painting(art=1)
top._label = "Example Painting"
id1 = AccessionNumber()
id1._label = "Accession Number for Painting"
id1.content = "X198-093"
top.identified_by = id1
id2 = LocalNumber()
id2.content = "677"
id2._label = "Local Repository Number"
top.identified_by = id2
```

## Statements about an Object



| AAT Term       | Label                | Usage Notes                   |
| -------------- | -------------------- | ----------------------------- |
 _aat:300411780_ | description          | For general descriptions
 _aat:300010358_ | materials            | For materials/medium statements
 _aat:300026687_ | acknowledgments      | For acknowledgements and attributions
 _aat:300055547_ | legal concepts       | For rights statements
 _aat:300266036_ | dimensions           | For statements about size and shape
 _aat:300121294_ | editions             | For series or edition statements
 _aat:300055863_ | provenance           | For provenance statements
 _aat:300028702_ | inscriptions         | For transcribing inscriptions
 _aat:300028705_ | signatures           | For transcribing signatures
 _aat:300028744_ | markings             | For describing other markings
 _aat:300028749_ | watermarks           | For describing watermarks


## Parts



| AAT Term       | Label                | Usage Notes                   |
| -------------- | -------------------- | ----------------------------- |
 _aat:300190692_ | backs                |
 _aat:300190703_ | fronts               |
 _aat:300190710_ | tops                 |
 _aat:300190695_ | bottoms              |
 _aat:300190706_ | sides                |
 _aat:300014844_ | supports             | For the part that a drawing or painting is on
 _aat:300404391_ | frames               | 
 _aat:300131087_ | mounts               |
 _aat:300001656_ | bases                |

