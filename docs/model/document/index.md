---
title: Texts and Documents
---

[TOC]

## Introduction

This section documents the model for documents that contain text, including artworks such as medieval manuscripts, archival material such as letters, ledgers or diaries, scholarly communication such as journals, articles and monographs, digital objects such as web pages, or any other sort of written communication.

The intent is not to be an all-encompassing model that would be suitable for a graph based library management system, archival finding aids, or catalog of any digital resource, but instead to provide sufficient description that the object is identified, understandable and able to be referenced within other more specific systems and ontologies.  This model is intended to be enough to use for the basic use cases of referencing texts that are related to artwork, regardless of whether they are held in a library, archive, museum, or on the internet.

Notably, it does not attempt to reproduce the formalisms of [FRBR](https://www.ifla.org/node/2016), as manifested by [FRBRoo](https://www.ifla.org/publications/node/11240) or [BibFrame](http://www.loc.gov/bibframe/docs/index.html), or other conceptual hierarchies, but instead provide as simple as possible a model to accomplish core bibliographic reference tasks. 

## Physical Objects, Conceptual Texts

The first distinction that is needed is between the physical carrier of the text, and the text itself.  Like the `VisualItem` pattern for the [artwork's visual content shown by objects](/model/object/aboutness/#depiction), the `LinguisticObject` that represents the text of a work can be `carried` by many `HumanMadeObject`s.  In this way, all of the copies of a particular book carry the same information content, that only needs to be described once and can act as a single connection point.

Like other LinguisticObjects, it can have a `value` for the actual text of the work, classifications, languages and so forth.

```crom
top = vocab.Book(ident="auto int-per-segment")
top._label = "Physical Book"
li = model.LinguisticObject()
li._label = "Textual content of the Book"
li.content = "Once upon a time, ..."
li.language = instances['english']
top.carries = li
```

## Core Features

The same core features of all other resources are also applicable to the `LinguisticObject`s used to represent texts.  They must have an `id` and `type`, they should have a `label`, they should have a `classified_as` relationship to a `Type` that further describes the sort of object, and so forth. They may also have a `language` property, that references a Language resource.

The title of a text is captured using the `Name` pattern, and assigned identifiers using the `Identifier` pattern, referenced with the `identified_by` relationship.

```crom
top = vocab.ArticleText(ident="auto int-per-segment",)
top._label = "Example Article"
top.language = instances['english']
title = model.Name()
title.content = "Title of Article"
id = model.Identifier()
id._label = "DOI of Article"
id.content = "10.1000/1011"
top.identified_by = title
top.identified_by = id
```


## Creation and Publication

The production of the physical carriers of texts uses the same model as for other physical objects, and may be of interest for manuscripts, very early printed works (incunabula), letters or other similar documents, however the factory details for a specific modern book are likely of much less importance to capture.

There are two primary text-specific activities that are captured -- the creation of the text, being the conceptual `LinguisticObject` and its publication.  The text is created by a `Creation` activity of the author, but then there is a publishing `Activity` (_aat:300054686_) carried out by the publishing organization, for the same resource. 

```crom
top = vocab.ArticleText(ident="auto int-per-segment")
top._label = "Example Journal Article"
cre = model.Creation()
cre._label = "Creation of the Article Content"
author = model.Person()
author._label = "Author"
cre.carried_out_by = author
top.created_by = cre
pub = vocab.Publishing()
publr = model.Group()
publr._label = "Publishing House"
pub.carried_out_by = publr
top.used_for = pub
```

## Structure

The textual structure can be modeled with the partitioning of `LinguisticObject`s via the `part_of` property, in the same way that the parts of a physical object can be partitioned.  Thus the content of an Article can be part of the containing Issue, which is part of a Volume, which is part of the Journal or other periodical.  Similarly Chapters can be part of a Book or Proceedings, particular entries within a catalog, and so forth. 

```crom
top = vocab.MonographText(ident="auto int-per-segment")
top._label = "Example Monograph Text"
chap = vocab.ChapterText()
chap._label = "Chapter 1"
chap2 = vocab.ChapterText()
chap2._label = "Chapter 2"
top.part = chap
top.part = chap2
```

## Pages

Textual content is typically presented on pages or folios. As there might be many physical copies with the same structure, it is common to describe the pagination of the content as it applies to the content in general, rather than the many physical objects that carry that content.  Pagination (_aat:300200294_) or Foliation (_aat:300200662_) statements are the most common way to represent this, as simple descriptive fields following the core statement pattern. For uncomplicated, machine readable pagination values, it is possible create a pair of start and end Dimensions.

### Pagination Statement

The easiest way to describe the page range of a particular section of a larger collection is with a pagination statement.  The disadvantage of the approach is that it is not computationally available for processing.

```crom
top = vocab.ArticleText(ident="auto int-per-segment")
top._label = "Example 10 page Article"
pag = vocab.PaginationStatement()
pag.content = "125-135"
top.referred_to_by = pag
```


## Abstracts

While the full text of the `LinguisticObject` may be either too long to provide, or protected by publication and access restrictions, it is common for an abstract to be published and circulated openly.  This abstract might be provided by some other actor than the author of the content, such as via an abstracting and indexing service.  In this case, the Abstract would have its own separate `Creation` activity from that of the abstracted content.

```crom
top = vocab.Abstract(ident="auto int-per-segment")
top._label = "Abstract of Example Article"
top.content = "This is the abstract of the example article, which is excellent."
art = vocab.ArticleText()
art._label = "Example Article"
top.refers_to = art
cre = model.Creation()
abstr = model.Person()
abstr._label = "Example Abstracter"
cre.carried_out_by = abstr
top.created_by = cre
```

## References to other Resources

Textual content can `refer_to` other resources in the overall model. These references might be just that the content discusses the resource, such as a mention of a particular painting.  Equally, the reference might be that the content was used as the evidence for the resource, such as a Materials Statement being the evidence for the Materials in the model that the painting is asserted to be `made_of`. 

```crom
top = vocab.ArticleText(ident="auto int-per-segment")
top._label = "Article about Example Painting"
what = vocab.Painting(art=1)
what._label = "Example Painting"
top.refers_to = what
```

## Translations

One Linguistic Object, be it captured in the model as a Statement or as the full text content carried by a physical object, can be the translation of another. For example an article can be the translation of an original article in a different language. This is represented using the `translation_of` relationship.

```crom
top = vocab.ArticleText(ident="auto int-per-segment")
top._label = "The Birth of Artistic Conception in China"
top.language = instances['english']
orig = vocab.ArticleText()
orig._label =  "Zhongguo yishu yijing zhi dansheng"
orig.language = instances['chinese']
top.translation_of = orig





