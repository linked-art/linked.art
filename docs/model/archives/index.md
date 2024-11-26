---
title: Archives
up_href: "/model/"
up_label: "Model Overview"
---



## Introduction

Linked Art includes a simple model for describing archives and archival material. This model makes use of [Sets](/model/collection/) as a way to group together objects (either physical or digital) into a hierarchy. The archival items themselves are typically [HumanMadeObjects](/model/object/) which can be described in detail, but often are only very briefly described, if at all in archival practice. The only new functionality added to support archival description is the link between a Set and the physical container in which the members of the conceptual set are held.


## Archival Hierarchy

Archival tradition typically does not distinguish between the intellectual arrangement and the physical containment of an archive, however in Linked Art and CIDOC-CRM these are two very separate parts of the model. Linked Art treats the archival hierarchy as conceptual -- it is a product of the mind, not a feature of the physical world. This can be thought of in the following way: if one were to remove a letter from an archival folder, it is not removed from the "archive", it is removed from its current container. One might, temporarily, add it to another folder that happened to be part of a second archive ... perhaps to carry them to a reader together. This would, similarly, not add it to the second archive.

With this in mind, the archives can be described as a hierarchy of `Set`s, where the Set that represents the sub-series is a `member_of` the Set that represents the series, which is a `member_of` the sub-fonds, and so on. There is no limit to the depth of the hierarchy, and given the graph-based nature of Linked Art, this makes it possible for the same object to be part of two archives at the same time.

The items, if described, are `HumanMadeObject`s which are also `member_of` the `Set`s, and follow the regular physical [object](/model/object/) model. 
 
Note that the ordering of the members within the archival group can be given in [the same way](/model/collection/#order-of-members) as ordering for any other Set.


__Example:__

A letter between Alfred Stieglitz and Bertha Obermeyer, dated 1920 is part of the "Stieglitz Family Letters" sub-series, which is part of "Series I: Alfred Stieglitz Correspondence" (which is part of the "Alfred Stieglitz / Georgia O'Keeffe Archive" at Yale University)

The letter ...

```crom
top = model.HumanMadeObject(ident="letter/1", label="Obermeyer 1920")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300026879", label="Letter")
top.identified_by = vocab.PrimaryName(content="Obermeyer, Bertha (1920)")
top.member_of = model.Set(ident="archive_sfl", label="Stieglitz Family Letters")
```

is a member of the sub-series ...

```crom
top = vocab.ArchiveSubGroupSet(ident="archive_sfl/1", label="Stieglitz Family Letters")
top.identified_by = vocab.PrimaryName(content="Stieglitz Family Letters")
top.member_of = model.Set(ident="archive_asc", label="Alfred Stiegliz Correspondence")
```

which is a member of the series ...

```crom
top = vocab.ArchiveGroupSet(ident="archive_asc/1", label="Alfred Stiegliz Correspondence")
top.identified_by = vocab.PrimaryName(content="Alfred Stiegliz Correspondence")
```

(and so on)

### Alignment between Conceptual and Physical Hierarchies

At one or more points in the archival hierarchy it is useful to align between the conceptual arrangement and the physical storage of the objects. This is done with the `members_contained_by` property on the archival Set resource, referencing a `HumanMadeObject` which physically contains or holds the objects, such as a box, folder or shelf. The physical objects, if described individually, can also be part of this physical hierarchy using the `held_or_supported_by` property.


__Example:__

The Stieglitz Family Letters set has its members in Box 55.

```crom
top = vocab.ArchiveSubGroupSet(ident="archive_sfl/2", label="Stieglitz Family Letters")
top.identified_by = vocab.PrimaryName(content="Stieglitz Family Letters")
top.members_contained_by = model.HumanMadeObject(ident="box55", label="Archival Box 55")
```

And the letter is within the box.

```crom
top = model.HumanMadeObject(ident="letter/3", label="Obermeyer 1920")
top.identified_by = vocab.PrimaryName(content="Obermeyer, Bertha (1920)")
top.held_or_supported_by = model.HumanMadeObject(ident="box55", label="Archival Box 55")
top.member_of = model.Set(ident="archive_sfl", label="Stieglitz Family Letters")
```

## Collective Description

It is possible to describe the shared features of members of Sets using the `members_exemplified_by` property on Set instances.  This is described in more detail in the [collections](/model/collection/) page. This is especially useful for establishing the range of dates of creation of objects, the language of their contents, their types and so forth for the members of the archival collection.

Otherwise, much of the description of archives is done in plain text, which follows the [statement](/model/base/) pattern.




