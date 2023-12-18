---
title: Linked Art / Schema.org Mapping
---


## Shared Properties

* /id --> /url
* /referred_to_by[classified_as/id=DESCRIPTION]/content --> /description
* /classified_as/id --> /additionalType
* /identified_by[type=Name][classified_as/id=PRIMARY_NAME]/content --> /name 
* /identified_by[type=Name]/content --> /alternateName
* /identified_by[type=Identifier]/content --> /identifier
* /equivalent/id --> /sameAs
* /representation/digitally_shown_by/access_point/id --> /image
* /subject_of/digitally_carried_by/access_point/id --> /mainEntityOfPage


## Person

* type = Person
* /born/timespan/begin_of_the_begin --> /birthDate
* /born/took_place_at/id --> /birthPlace
* /died/timespan/begin_of_the_begin --> /deathDate
* /died/took_place_at/id --> /deathPlace
* /contact_point[classified_as=EMAIL]/content --> /email
* /classified_as[classified_as=GENDER]/id --> /gender
* /classified_as[classified_as=OCCUPATION]/id --> /hasOccupation
* /classified_as[classified_as=NATIONALITY]/id --> /nationality
* /residence/id --> /homeLocation
* /member_of --> /memberOf


## Group

* type = Organization
* /contact_point[classified_as=EMAIL]/content --> /email
* /contact_point[classified_as=ADDRESS]/content --> /address
* /dissolved_by/timespan/begin_of_the_begin --> /dissolutionDate
* /formed_by/timespan/begin_of_the_begin --> /foundingDate
* /formed_by/took_place_at/id --> /foundingLocation
* /formed_by/carried_out_by/id --> /founder
* /residence/id --> /location
* /member_of --> /memberOf
* /member_of --> /parentOrganization (if known to be hierarchical, rather than some other membership)

## Place

* type = Place
* /part_of/id --> /containedInPlace
* /defined_by --> /geo ; or /latitude and /longitude if a point
* (If a particular image is known to be a map, use /hasMap not /image)

## Concepts

* Type = DefinedTerm, CreativeWork
* Additional Types: Language
* /broader --> /isPartOf
* /member_of --> /inDefinedTermSet

## Human Made Object

* type = VisualArtwork, ArchiveComponent 
* /classified_as/id --> /artform (painting, sculpture, etc)
* /referred_to_by[classified_as/id=DESCRIPTION]/content --> /abstract  (other classes use /description)
* /referred_to_by[classified_as/id=RIGHTS_STMT]/content --> /copyrightNotice
* /referred_to_by[classified_as/id=ACCESS_STMT]/content --> /conditionsOfAccess
* /referred_to_by[classified_as/id=CREDIT_STMT]/content --> /creditText
* /referred_to_by[classified_as/id=MATERIAL_STMT]/content --> /artMedium
* /produced_by/part*/carried_out_by --> /creator or /artist
* /produced_by/part*[classified_as=CONTRIBUTOR]/carried_out_by --> /contributor
* /produced_by/took_place_at (if a country) --> /countryOfOrigin
* /produced_by/timespan --> /dateCreated
* /produced_by/took_place_at --> /locationCreated
* /partOf --> /isPartOf
* /shows|carries --> /exampleOfWork
* /made_of --> /material
* /content --> /text
* /dimension[classified_as/id=HEIGHT]/value --> /height
* /dimension[classified_as/id=WIDTH]/value --> /width
* /dimension[classified_as/id=DEPTH]/value --> /depth
* /current_owner --> /holdingArchive
* /current_location --> /itemLocation

## Digital Object 

* /type = CreativeWork, DataSet
* /digitally_shows|digitally_carries --> /exampleOfWork
* /dimension[classified_as/id=HEIGHT]/value --> /height
* /dimension[classified_as/id=WIDTH]/value --> /width
* /dimension[classified_as/id=DEPTH]/value --> /depth
* /dimension --> /size
* /part_of --> /isPartOf
* /format --> /encodingFormat
* /conforms_to --> ??
* /access_point --> /distribution
* /created_by/part*/carried_out_by --> /creator
* /used_for[./classified_as/id=PUBLISHING]/carried_out_by --> /publisher

## Visual Item / Linguistic Object

* type = CreativeWork (for both Visual and Linguistic)
* /about --> /about
* /represents[./type=Place] --> /contentLocation
* /represents (for all) --> /mainEntity
* /language --> /inLanguage (to the Language concept)
* /classified_as (where the Concept is a genre) --> /genre 
* /created_by/part*/carried_out_by --> /author, /artist, or /creator
* /used_for[./classified_as/id=PUBLISHING]/carried_out_by --> /publisher
* /content --> /text
* /dimension --> /size
* /format --> /encodingFormat

## Event

* type = Event (ExhibitionEvent)
* /carried_out_by --> /organizer, /performer or /contributor
* /took_place_at --> /location
* /part_of --> /superEvent
* /timespan/begin_of_the_begin --> /startDate
* /timespan/end_of_the_end --> /endDate
* /used_specific_object --> /workFeatured
* /influenced_by --> /about (?)
* /caused_by --> ?

## Set

* type = ArchiveComponent (for Archives) or type = Collection (for other Sets)
* /member_of --> /isPartOf
* /created_by/part*/carried_out_by --> /author, /artist, or /creator
* /used_for[./classified_as/id=PUBLISHING]/carried_out_by --> /publisher
* /about --> /about
* /dimension --> /size


