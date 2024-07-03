---
title: Vocabulary Terms in Linked Art 
up_href: "/model/"
up_label: "Model Overview"
---

[TOC]

## Introduction

As the Linked Art model is very broad in terms of its classes and properties, we rely heavily on the use of vocabulary terms to be more specific about individual entities. There isn't a difference at the ontology level between a book or a painting or a bridge, they're all instances of the class `HumanMadeObject`. This makes it easy to be interoperable at the ontological level, however in order to compare data across institutions or datasets, there must also be interoperability at the vocabulary level to avoid thinking that the bridge should be counted in the same way as the painting.

Any entity in the model can have one or more classifications associated with it using the `classified_as` property, as discussed in the [Types and Classifications](/model/base/#types-and-classifications) section. Consistency in the use of URIs for those classifications will make the data easier to use for everyone. The vocabulary has been divided into three different sets, based on how important it is to reuse the terms.

The reference to the vocabulary entry can be either directly in the `id` of the reference, or as an embedded `equivalent` to an intermediary. For the purposes of conformance and utility, the following are both equally acceptable.

Vocabulary in `id`:

```crom
top = model.HumanMadeObject(ident="spring/30", label="Jeanne (Spring) by Manet")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300033618",label="Painting")
```

Vocabulary in `equivalent`:

```crom
top = model.HumanMadeObject(ident="spring/31", label="Jeanne (Spring) by Manet")
typ = model.Type(ident="https://linked.art/vocab/terms/painting", label="Painting")
eq = model.Type(ident="http://vocab.getty.edu/aat/300033618",label="Painting")
typ.equivalent = eq
top.classified_as = typ 
```

## Updates to the Vocabulary Lists

The required list will only be updated with a new major version of Linked Art, at which point terms can be added, removed or changed to different URIs. This is because an implementation which was conformant to a particular minor version would become non-conformant if it did not happen to use a particular required term that was added in the update. This would thus be a breaking change, and require a major version rather than a minor version.

The recommended list can be updated with a new minor version, as not following the list does not break compatability with previous minor versions. This includes adding, removing and changing the URIs for entries in the list.

The optional list, as merely informational, is not semantically versioned and thus can be updated at any time.

The community should propose additions to the lists via [github](https://github.com/linked-art/linked.art/issues) issues.


## Terms by Requirement Class

* [Required Terms](required/) -- you **must** use these terms to be considered to have implemented Linked Art
* [Recommended Terms](recommended/) -- you **should** use these terms unless you have a specific reason not to
* [Optional Terns](optional/) -- you **may** use these terms, but should feel no compulsion to if there's a reason not to
