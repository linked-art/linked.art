---
title: Texts and Documents
---

[TOC]

## Introduction

This section documents the model for documents that contain text, including artworks such as medieval manuscripts, archival material such as letters, ledgers or diaries, scholarly communication such as journals, articles and monographs, digital objects such as web pages, or any other sort of written communication.

The intent is not to be an all-encompassing model that would be suitable for a graph based library management system, archival finding aids, or catalog of any digital resource, but instead to provide sufficient description that the object is identified, understandable and able to be referenced within other more specific systems and ontologies.  This model is intended to be enough to use for the basic use cases of referencing texts that are related to artworks, regardless of whether they are held in a library, archive, museum, or on the internet.

Notably, it does not attempt to reproduce the formalisms of [FRBR](https://www.ifla.org/node/2016), as manifested by [FRBRoo](https://www.ifla.org/publications/node/11240) or [BibFrame](http://www.loc.gov/bibframe/docs/index.html), or other complex conceptual hierarchies, but instead provide as simple as possible a model to accomplish core bibliographic reference tasks. 

## Physical Objects, Conceptual Texts

The first distinction that is needed is between the physical or digital carrier of the text, and the text itself.  Like the `VisualItem` pattern for the [artwork's visual content shown by objects](/model/object/aboutness/#depiction), the `LinguisticObject` that represents the text of a work can be `carried` by many `HumanMadeObject`s.  In this way, all of the copies of a particular book carry the same information content, that only needs to be described once and can act as a single connection point.

Like other `LinguisticObject`s, it can have a `content` property for the actual text of the work, classifications, languages and so forth.

__Example:__

Yale University Library holds a copy of Koot's book about The Night Watch.

```crom
top = vocab.Book(ident="yul_10801219/1", label="Yale's copy of Koot's Night Watch")
top.identified_by = vocab.PrimaryName(content="Rembrandt's Night Watch. A Fascinating Story")
top.identified_by = vocab.SystemNumber(content="mfhd:10801219")
top.referred_to_by = vocab.PhysicalStatement(content="92 p. with illus.")
li = model.LinguisticObject(ident="koot_nightwatch", label="Content of Koot's Night Watch")
top.carries = li
```

## Core Features

The same core features of all other resources are also applicable to the `LinguisticObject`s used to represent texts.  They must have an `id` and `type`, they should have a `label`, they should have a `classified_as` relationship to a `Type` that further describes the sort of object, and so forth. They may also have a `language` property, that references a `Language` instance.

The title of a text is captured using the `Name` pattern, and assigned identifiers using the `Identifier` pattern, both with the `identified_by` relationship.

__Example:__

The textual content of Koot's work.

```crom
top = vocab.MonographText(ident="koot_nightwatch/1", label="Content of Koot's Night Watch")
top.identified_by = vocab.PrimaryName(content="Rembrandt's Night Watch. A Fascinating Story")
top.identified_by = vocab.SystemNumber(content="75441784")
top.language = vocab.instances['english']
```

## Creation and Publication

The production of the physical carriers of texts uses the same model as for other physical objects, and may be of interest for manuscripts, very early printed works (incunabula), letters or other similar documents, however the factory details for a specific modern book are likely of much less importance to capture.

There are two primary text-specific activities that are captured -- the creation of the text and its publication.  The text is created by a `Creation` activity of the author, but then there is a publishing `Activity` (_aat:300054686_) carried out by the publishing organization, for the same resource. 

__Example:__

The authorship and publication of the text.

```crom
top = vocab.MonographText(ident="koot_nightwatch/2", label="Content of Koot's Night Watch")
cre = model.Creation(label="Koot's writing of the work")
cre.carried_out_by = model.Person(ident="koot", label="Ton Koot")
top.created_by = cre
pub = vocab.Publishing(label="MI's Publishing")
pub.carried_out_by = model.Group(ident="meulenhoff", label="Meulenhoff International")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1969-01-01T00:00:00Z"
ts.end_of_the_end = "1969-12-31T23:59:59Z"
pub.timespan = ts
top.used_for = pub
```

## Structure

The textual structure can be modeled with the partitioning of `LinguisticObject`s via the `part_of` property, in the same way that the parts of a physical object can be partitioned.  Thus the content of an Article can be part of the containing Issue, which is part of a Volume, which is part of the Journal or other periodical.  Similarly Chapters can be part of a Book or Proceedings, particular entries within a catalog, and so forth. 

Note that unless it is important to create a separate record (for example the chapter is written by a different author, or there are other significant details), then it is also possible to add the description of the structure as a note, using the Statement pattern.

__Example:__

```crom
top = vocab.ChapterText(ident="koot_nightwatch_ch1/1", label="Chapter 1 of Koot")
top.identified_by = vocab.PrimaryName(content="Introduction")
top.part_of = model.LinguisticObject(ident="koot_nightwatch", label="Koot's Night Watch")
```

## Pages

Textual content is typically presented on pages or folios. As there might be many physical copies with the same structure, it is common to describe the pagination of the content as it applies to the content in general, rather than the many physical objects that carry that content. This is justifiable, not only for convenience, but also because the text is divided up across those pages. Pagination (_aat:300200294_) or Foliation (_aat:300200662_) statements are the most common way to represent this, as simple descriptive fields following the core statement pattern. 

The structured way is to have a Dimension associated with the object or work that gives the count of pages. This follows the regular pattern for counting parts. The easiest way to describe the page range of a particular section of a larger collection is with a pagination statement.  The disadvantage of the approach is that it is not computationally available for processing.

__Example:__

The introduction chapter to Koot's book is 10 pages long.

```crom
top = vocab.ChapterText(ident="koot_nightwatch_ch1/2", label="Chapter 1 of Koot")
top.identified_by = vocab.PrimaryName(content="Introduction")
top.referred_to_by = vocab.PaginationStatement(content="5 - 10")
dim = model.Dimension(label="10 pages")
dim.value = 10
dim.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300404433", label="Count Of")
dim.unit = model.MeasurementUnit(ident="http://vocab.getty.edu/aat/300194222", label="Pages")
top.dimension = dim
```

## References to other Entities

Textual content can be `about` other resources in the overall model. 

__Example:__

Koot's book is about The Night Watch.

```crom
top = vocab.MonographText(ident="koot_nightwatch/3", label="Content of Koot's Night Watch")
top.about = model.HumanMadeObject(ident="nightwatch", label="The Night Watch")
```

