---
title: Linked Art / Schema.org Mapping
---

This mapping is from Linked Art into Schema.org.

## Shared Properties

| Linked Art | Schema.org |
|---|---|
| `/id` | `/url` |
| `/referred_to_by[classified_as/id=DESCRIPTION]/content` | `/description` |
| `/classified_as/id` | `/additionalType` |
| `/identified_by[type=Name][classified_as/id=PRIMARY_NAME]/content` | `/name` |
| `/identified_by[type=Name]/content` | `/alternateName` |
| `/identified_by[type=Identifier]/content` | `/identifier` |
| `/equivalent/id` | `/sameAs` |
| `/representation/digitally_shown_by/access_point/id` | `/image` |
| `/subject_of/digitally_carried_by/access_point/id` | `/mainEntityOfPage` |


## Person

**Schema.org type:** `Person`

| Linked Art | Schema.org |
|---|---|
| `/born/timespan/begin_of_the_begin` | `/birthDate` |
| `/born/took_place_at/id` | `/birthPlace` |
| `/died/timespan/begin_of_the_begin` | `/deathDate` |
| `/died/took_place_at/id` | `/deathPlace` |
| `/contact_point[classified_as=EMAIL]/content` | `/email` |
| `/classified_as[classified_as=GENDER]/id` | `/gender` |
| `/classified_as[classified_as=OCCUPATION]/id` | `/hasOccupation` |
| `/classified_as[classified_as=NATIONALITY]/id` | `/nationality` |
| `/residence/id` | `/homeLocation` |
| `/member_of` | `/memberOf` |


## Group

**Schema.org type:** `Organization`

| Linked Art | Schema.org |
|---|---|
| `/contact_point[classified_as=EMAIL]/content` | `/email` |
| `/contact_point[classified_as=ADDRESS]/content` | `/address` |
| `/dissolved_by/timespan/begin_of_the_begin` | `/dissolutionDate` |
| `/formed_by/timespan/begin_of_the_begin` | `/foundingDate` |
| `/formed_by/took_place_at/id` | `/foundingLocation` |
| `/formed_by/carried_out_by/id` | `/founder` |
| `/residence/id` | `/location` |
| `/member_of` | `/memberOf` |
| `/member_of` | `/parentOrganization` _(if known to be hierarchical, rather than some other membership)_ |


## Place

**Schema.org type:** `Place`

| Linked Art | Schema.org |
|---|---|
| `/part_of/id` | `/containedInPlace` |
| `/defined_by` | `/geo` — or `/latitude` and `/longitude` if a point |

> **Note:** If a particular image is known to be a map, use `/hasMap` rather than `/image`.


## Concepts

**Schema.org types:** `DefinedTerm` AND `CreativeWork`; additional type: `Language`

| Linked Art | Schema.org |
|---|---|
| `/broader` | `/isPartOf` |
| `/member_of` | `/inDefinedTermSet` |


## Human Made Object

**Schema.org type:** `VisualArtwork` OR `ArchiveComponent`

| Linked Art | Schema.org |
|---|---|
| `/classified_as/id` | `/artform` _(painting, sculpture, etc.)_ |
| `/referred_to_by[classified_as/id=DESCRIPTION]/content` | `/abstract` _(other classes use `/description`)_ |
| `/referred_to_by[classified_as/id=RIGHTS_STMT]/content` | `/copyrightNotice` |
| `/referred_to_by[classified_as/id=ACCESS_STMT]/content` | `/conditionsOfAccess` |
| `/referred_to_by[classified_as/id=CREDIT_STMT]/content` | `/creditText` |
| `/referred_to_by[classified_as/id=MATERIAL_STMT]/content` | `/artMedium` |
| `/produced_by/part*/carried_out_by` | `/creator` or `/artist` |
| `/produced_by/part*[classified_as=CONTRIBUTOR]/carried_out_by` | `/contributor` |
| `/produced_by/took_place_at` _(if a country)_ | `/countryOfOrigin` |
| `/produced_by/timespan` | `/dateCreated` |
| `/produced_by/took_place_at` | `/locationCreated` |
| `/partOf` | `/isPartOf` |
| `/shows` or `/carries` | `/exampleOfWork` |
| `/made_of` | `/material` |
| `/content` | `/text` |
| `/dimension[classified_as/id=HEIGHT]/value` | `/height` |
| `/dimension[classified_as/id=WIDTH]/value` | `/width` |
| `/dimension[classified_as/id=DEPTH]/value` | `/depth` |
| `/current_owner` | `/holdingArchive` |
| `/current_location` | `/itemLocation` |


## Digital Object

**Schema.org types:** `CreativeWork` AND `DataSet`

| Linked Art | Schema.org |
|---|---|
| `/digitally_shows` or `/digitally_carries` | `/exampleOfWork` |
| `/dimension[classified_as/id=HEIGHT]/value` | `/height` |
| `/dimension[classified_as/id=WIDTH]/value` | `/width` |
| `/dimension[classified_as/id=DEPTH]/value` | `/depth` |
| `/dimension` | `/size` |
| `/part_of` | `/isPartOf` |
| `/format` | `/encodingFormat` |
| `/access_point` | `/distribution` |
| `/created_by/part*/carried_out_by` | `/creator` |
| `/used_for[classified_as/id=PUBLISHING]/carried_out_by` | `/publisher` |


## Visual Item / Linguistic Object

**Schema.org type:** `CreativeWork` _(for both Visual and Linguistic)_

| Linked Art | Schema.org |
|---|---|
| `/about` | `/about` |
| `/represents[type=Place]` | `/contentLocation` |
| `/represents` _(for all)_ | `/mainEntity` |
| `/language` | `/inLanguage` _(to the Language concept)_ |
| `/classified_as` _(where the Concept is a genre)_ | `/genre` |
| `/created_by/part*/carried_out_by` | `/author`, `/artist`, or `/creator` |
| `/used_for[classified_as/id=PUBLISHING]/carried_out_by` | `/publisher` |
| `/content` | `/text` |
| `/dimension` | `/size` |
| `/format` | `/encodingFormat` |


## Event

**Schema.org type:** `Event` _(ExhibitionEvent)_

| Linked Art | Schema.org |
|---|---|
| `/carried_out_by` | `/organizer`, `/performer`, or `/contributor` |
| `/took_place_at` | `/location` |
| `/part_of` | `/superEvent` |
| `/timespan/begin_of_the_begin` | `/startDate` |
| `/timespan/end_of_the_end` | `/endDate` |
| `/used_specific_object` | `/workFeatured` |
| `/influenced_by` | `/about` _(?)_ |


## Set

**Schema.org type:** `ArchiveComponent` _(for Archives)_ OR `Collection` _(for other Sets)_

| Linked Art | Schema.org |
|---|---|
| `/member_of` | `/isPartOf` |
| `/created_by/part*/carried_out_by` | `/author`, `/artist`, or `/creator` |
| `/used_for[classified_as/id=PUBLISHING]/carried_out_by` | `/publisher` |
| `/about` | `/about` |
| `/dimension` | `/size` |
