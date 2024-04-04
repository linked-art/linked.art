---
title: Linked Art / CDWA Mapping
---


## Introduction

[Categories for the Description of Works of Art](https://www.getty.edu/research/publications/electronic_publications/cdwa/index.html) (CDWA) is a Getty publication describing a set of guidelines for cataloging art and architecture. 

## Mapping

Remarks, citations, and page are repeated everywhere in CDWA, but the same pattern applies as from 1.5 and 1.6.

Similarly, there are earliest and latest dates called out explicitly for every date field, which again is as per 4.2.1.


### 1. OBJECT/WORK 

* 1.1. Catalog Level --> No mapping, this is meta-meta-data 
* 1.2. Object/Work Type --> `classified_as` on the Object, with metatype of Type of Object
* 1.3. Object/Work Type Date --> Could be handled with an Attribute Assignment, but this is mostly a Phase
* 1.4. Components/Parts --> `part_of` from the component/part to the parent
* 1.4.1 Components Quantity --> A `Dimension` for the number of parts
* 1.4.2 Components Type --> `classified_as` on a part
* 1.5. Remarks --> Statement pattern
* 1.6. Citations --> `about` on the citing LinguisticObject, or a Statement

### 2. CLASSIFICATION 

* 2.1. Classification Term --> `classified_as`

### 3. TITLES OR NAMES 

* 3.1. Title Text --> `identified_by[type=Name]/content`
* 3.2. Title Type --> `identified_by[type=Name]/classified_as`
* 3.3. Preference --> Are the same as 3.2
* 3.4. Title Language --> `identified_by[type=Name]/language`
* 3.5. Title Date --> Attribute Assignment of the title to associate a date with the naming

### 4. CREATION 

* 4.1. Creator Description --> The exact string could be in a Statement, but really this is `produced_by/carried_out_by`
* 4.1.1. Creator Extent --> `technique` or `classified_as` on the `Production`
* 4.1.2. Qualifier --> Depends. Either `influenced_by`, assigning a `Group`, or an `AttributeAssignment`
* 4.1.3. Creator Identity --> `produced_by/carried_out_by/id`
* 4.1.4. Creator Role --> Same as extent
* 4.1.5. Creator Statement --> A Statement on the Production
* 4.2. Creation Date --> `produced_by/timespan`
* 4.2.1. Earliest Date --> `produced_by/timespan/begin_of_the_begin`
* 4.2.2. Latest Date  --> `produced_by/timespan/end_of_the_end`
* 4.2.3. Date Qualifier --> Associated with the part of the production that has the technique/classified_as (per extent)
* 4.3. Creation Place/Original Location --> `produced_by/took_place_at`
* 4.3.1. Place Qualifier --> as per extent
* 4.4. Object/Work Culture --> `classified_as`
* 4.5. Commissioner --> See Provenance section on Promises
* 4.6. Creation Numbers --> `identified_by[type=Identifier]/content`
* 4.6.1. Number Type --> `identified_by[type=Identifier]/classified_as`

### 5. STYLES/PERIODS/GROUPS/MOVEMENTS

* 5.1. Styles/Periods Description --> `classified_as` on the Work, or link to the period/place/group from the Production if more specific knowledge is available
* 5.2. Styles/Periods Indexing Terms --> as above
* 5.2.1. Term Qualifier --> as above

### 6. MEASUREMENTS 

* 6.1. Dimensions Description --> Statement in `referred_to_by`
* 6.2. Dimensions Type --> `dimension/classified_as`
* 6.3. Dimensions Value --> `dimension/value`
* 6.4. Dimensions Unit --> `dimension/unit`
* 6.5. Dimensions Extent --> Add an attribute assignment to the dimension, and then give it a `technique`
* 6.6. Scale Type --> Not mapped
* 6.7. Dimensions Qualifier --> these are how the dimension is taken, so classified_as on an attribute assignment
* 6.8. Dimensions Date --> timespan on the attribute assignment
* 6.9. Shape --> `classified_as` on the object
* 6.10. Format/Size --> format for digital objects is `format`; `classified_as` for others

### 7. MATERIALS/TECHNIQUES 

* 7.1. Materials/Techniques Description --> Statement in `referred_to_by`
* 7.2. Materials/Techniques Flag --> unnecessary, they're different `classified_as` on the statement
* 7.3. Materials/Techniques Extent --> This would require parts to be explicitly defined
* 7.4. Materials/Techniques Role --> Also wold need a part
* 7.5. Materials/Techniques Name --> `material` or `technique` then to the Material/Type and identified_by
* 7.6. Material Color --> Dimension for specific colors, classified_as for general colors
* 7.7. Material Source Place --> this isn't possible
* 7.8. Watermarks --> Statement in `referred_to_by`
* 7.8.1. Watermark Identification --> This would need a Feature which was the watermark
* 7.8.2. Watermark Date --> Ditto
* 7.9. Performance Actions --> Performance Art is not yet modeled (but would be its own activity)

### 8. INSCRIPTIONS/MARKS

* 8.1. Inscription Transcription or Description --> Statement in `referred_to_by`
* 8.2. Inscription Type --> if a statement, and differentiation is needed, then different `classified_as` on the statement. Otherwise needs a separate LinguisticObject record, and then `classified_as` on that
* 8.3. Inscription Author --> Needs a separate LinguisticObject that is carried by the the object, then regular `created_by`
* 8.4. Inscription Location --> took_place_at on the LinguisticObject's creation
* 8.5. Inscription Language --> `language` on the LinguisticObject
* 8.6. Typeface/ Letterform --> Not Mapped
* 8.7. Mark Identification --> Not mappped, but could be classified_as on a VisualItem of the mark
* 8.8. Inscription Date --> `timespan` on the Creation of the LinguisticObject

### 9. STATE

* 9.1. State Description --> Statement
* 9.2. State Identification --> `classified_as`
* 9.3. Known States --> Not mapped


### 10. EDITION

10.1. Edition Description --> Statement
10.2. Edition Number or Name --> Not mapped -- we don't have "Edition" as an entity to associate information with
10.3. Impression Number --> Not mapped
10.4. Edition Size --> Not mapped


### 11. FACTURE

* 11.1. Facture Description --> Statement


### 12. ORIENTATION/ARRANGEMENT

* 12.1. Orientation/Arrangement Description --> Statement
* 12.2. Orientation Indexing Terms --> Not mapped


### 13. PHYSICAL DESCRIPTION

* 13.1. Physical Appearance --> Statement
* 13.2. Physical Description Indexing Terms --> classified_as, or not mapped


### 14. CONDITION/EXAMINATION HISTORY

* 14.1. Condition/Examination Description --> Statement
* 14.2. Examination Type --> AttributeAssignment of the statement, classified_as
* 14.3. Examination Agent --> carried_out_by
* 14.4. Examination Date --> timespan
* 14.5. Examination Place --> took_place_at


### 15. CONSERVATION/TREATMENT HISTORY

* 15.1. Conservation/Treatment Description --> Statement
* 15.2. Treatment Type --> Modification of the object, classified_as
* 15.3. Treatment Agent --> carried_out_by
* 15.4. Treatment Date --> timespan
* 15.5. Treatment Place --> took_place_at


### 16. SUBJECT MATTER 

* 16.1. Subject Display --> Statement
* 16.2. General Subject Terms --> `about` on the Work (generally)
* 16.2.1. General Subject Type --> different properties: `classified_as` vs `about` vs `represents`
* 16.2.2. General Subject Extent --> associate with a part record if needed
* 16.2. Specific Subject Terms --> the same as above
* 16.3.1. Specific Subject Type --> ditto
* 16.3.2. Specific Subject Extent --> ditto
* 16.4. Outside Iconography Term --> as above
* 16.4.1. Outside Iconography Code --> identifier on the Type
* 16.4.1. Outside Iconography Source --> equivalent?
* 16.5. Subject Interpretive History --> Statement

### 17. CONTEXT

* 17.1. Historical/Cultural Events --> a Period/Event/Activity record for the event
* 17.1.1. Event Type --> Event's `classified_as`
* 17.1.2. Event Identification --> `identified_by`
* 17.1.3. Event Date --> `timespan`
* 17.1.4. Event Place --> `took_place_at`
* 17.1.5. Event Agent --> `carried_out_by` or `participated_in`
* 17.1.5.1. Agent Role --> `classified_as` on a part of the event carried out by agent
* 17.1.6. Contextual Cost or Value --> Not mapped, but we have MonetaryAmount construct
* 17.2. Architectural Context --> Not mapped. Could be where removed from, could be encounter. 
* 17.2.1. Building/Site Context --> Ditto
* 17.2.2. Part/Placement Context --> Ditto
* 17.2.3. Architectural Context Date --> Ditto
* 17.3. Archeological Context --> `encountered_by` 
* 17.3.1. Discovery/Excavation Place --> Encounter's `took_place_at`
* 17.3.2. Excavation Site Sector --> Place's `identified_by`
* 17.3.3. Excavator --> Encounter's `carried_out_by`
* 17.3.4. Discovery/Excavation Date --> Encounter's `timespan`
* 17.4. Historical Location Context --> Not mapped
* 17.4.1. Historical Location Place --> Not mapped
* 17.4.2. Historical Location Date --> Not mapped


### 18. DESCRIPTIVE NOTE

* 18.1. Descriptive Note Text --> All of these are Statements
* 18.1.1. Abstract Description
* 18.1.2. Pagination Description
* 18.1.3. Foliation Description
* 18.1.4. Extent Description
* 18.1.5. Arrangement Description

### 19. CRITICAL RESPONSES

* 19.1. Critical Comment --> Linguistic Object about the entity
* 19.2. Comment Document Type
* 19.3. Comment Author
* 19.4. Comment Date
* 19.5. Comment Circumstances


### 20. RELATED WORKS

* 20.1. Related Work Label/Identification --> Different mappings for different relationships. Can fall back to Attribute Assignment if needed.
* 20.1.1. Work Relationship Type
* 20.1.2. Work Relationship Date
* 20.2. Work Broader Context
* 20.2.1. Historical Flag
* 20.2.2. Broader Context Date
* 20.2.3. Hierarchical Relationship Type
* 20.3. Relationship Number

### 21. CURRENT LOCATION 

* 21.1. Current Location Description --> access Statement
* 21.2. Current Repository / Geographic Location  --> `current_location` or `current_owner` 
* 21.2.1 Current Flag --> Not mapped, infer from attribute assignment for former values
* 21.2.2 Location Type --> `classified_as` on Place or Group
* 21.2.3 Repository Numbers --> indirect through location to organization, then `identified_by`, or through `current_owner`
* 21.2.3.1. Number Type --> `classified_as` on the Identifier
* 21.2.4. Gallery/Shelf Location --> `current_location`
* 21.2.5. Coordinates --> `defined_by` on the Place
* 21.2.6. Credit Line --> Statement
* 21.3. Object/Work Label/Identification --> its URI, or a Statement for description


### 22. COPYRIGHT/RESTRICTIONS

* 22.1. Copyright Statement --> Statement
* 22.2. Copyright Holder Name --> Could create a Right (per Provenance) and associate it with the holder of the right, but basically this isn't mapped
* 22.3. Copyright Place --> ditto
* 22.4. Copyright Date --> ditto


### 23. OWNERSHIP/COLLECTING HISTORY

* 23.1. Provenance Description --> Statement
* 23.1.1. Acquisition Description --> `Acquisition` in a Provenance Entry or Object
* 23.2. Transfer Mode --> `classified_as` on the Acquisition 
* 23.3. Cost or Value --> `Payment` or a valuation, as below
* 23.3.1. Valuation --> `dimension` of a Monetary Amount (perhaps with an Attribute Assignment for details)
* 23.3.1.1. Valuation Amount --> `value` on the Monetary Amount
* 23.3.1.2. Currency Unit --> `currency`
* 23.4. Legal Status --> Rights statement
* 23.5. Owner/Agent --> `current_owner`, or who the ownership was transferred to or from by an Acquisition. Agent is in `carried_out_by`
* 23.5.1. Owner/Agent Role --> `classified_as` or via the relationship
* 23.6. Ownership Place --> Not mapped
* 23.7. Ownership Date --> the difference between acquisitions
* 23.8. Owner's Numbers --> `identified_by` with an Attribute Assignment
* 23.8.1. Number Type --> `classified_as` on the Identifier
* 23.9. Owner's Credit Line --> Statement

### 24. EXHIBITION/LOAN HISTORY

* 24.1. Exhibition/Loan Description --> Statement
* 24.2. Exhibition Title or Name --> Create an Exhibition with `identified_by`
* 24.3. Exhibition Type --> `classified_as`
* 24.4. Exhibition Curator --> `carried_out_by` or `created_by/carried_out_by` on the abstract work
* 24.5. Exhibition Organizer --> `carried_out_by`
* 24.6. Exhibition Sponsor --> Not mapped
* 24.7. Exhibition Venue --> `took_place_at`
* 24.7.1. Venue Name/Place --> `identified_by[type=Name]` on the place
* 24.7.2. Venue Date --> timespan on the Exhibition
* 24.8. Exhibition Object Number --> Attribute Assignment
* 24.8.1. Number Type --> classified_as on the identifier assigned
* 24.9. Exhibition Object/Work Label/Identification --> URI or Statement


### 25. CATALOGING HISTORY

* 25.1. Cataloging Institution --> We don't record meta-meta-data, intentionally not mapped.
* 25.2. Cataloger Name
* 25.3. Cataloger Action
* 25.4. Area of Record Affected
* 25.5. Cataloging Date
* 25.7. Object/Work Record ID
* 25.8. Cataloging Language

### 26. RELATED VISUAL DOCUMENTATION

* 26.1. Image References --> `representation` to the image work, then digitally_* carried_by to the digital image itself
* 26.1.1. Image to Work Relationship Type --> `classified_as` on the VisualItem of * the Image
* 26.2. Image Label/Identification --> URI or Statement or Name
* 26.2.1. Image Catalog Level --> Not mapped
* 26.2.2. Image Type --> `classified_as` likely on the visual item, not the digital object
* 26.2.3. Image Title/Name --> `identified_by`
* 26.2.3.1 Image Title Type --> `classified_as` on the Name
* 26.2.4. Image Measurements --> `dimension`
* 26.2.4.1. Dimensions Type --> Dimension's `classified_as`
* 26.2.4.2. Dimensions Value --> Dimension's `value`
* 26.2.4.3. Dimensions Unit --> Dimension's `unit`
* 26.2.5. Image Format --> `format`, `conforms_to` or `classified_as` on the DO
* 26.2.6. Image Date --> `created_by/timespan`
* 26.2.7. Image Color --> `classified_as`
* 26.2.8. Works Depicted --> `represents` referring to the object
* 26.2.9. Image View Description --> Statement
* 26.2.9.1. View Type --> `classified_as`
* 26.2.9.2. View Subject --> `represents` per depicting
* 26.2.9.2.1. View Subject Indexing Terms --> Still `represents`
* 26.2.9.3. View Date --> If this is the date of the subject matter, then it would be that the image's VI is `about` a Period with a timespan?
* 26.2.10. Image Maker/Agent --> `created_by/carried_out_by`
* 26.2.10.1. Image Maker Role --> `created_by/part/classified_as`
* 26.2.10.2. Image Maker Extent --> Either same as role, or make a new entity that is part of the Image
* 26.2.11. Image Repository --> `current_owner` or `current_location` of the Physical Object that shows the Visual Item. 
* 26.2.11.1. Image Repository Numbers --> `identified_by` on owner / location
* 26.2.11.1.1. Number Type --> `classified_as` on the Identifier
* 26.2.12. Image Copyright/Restrictions --> Statement
* 26.2.12.1. Image Copyright Holder --> See Rights
* 26.2.12.1.1. Image Copyright Holder's Numbers --> identified_by with a Attribute Assignment
* 26.2.12.1.1.1. Number Type --> classified_as
* 26.2.12.2. Image Copyright Date --> See Rights
* 26.2.13. Image Source --> Not mapped, if different from Repository.
* 26.2.13.1. Image Source Number --> ditto
* 26.2.13.1.1. Number Type --> ditto
* 26.2.14. Related Image --> Same as for related objects
* 26.2.14.1. Image Relationship Type
* 26.2.14.2. Image Relationship Number
* 26.2.14.3. Image Relationship Date
* 26.2.15. Image Broader Context --> Hierarchy looks like Sets of images
* 26.2.18. Image Authority Record ID --> URI or `identified_by`

### 27. RELATED TEXTUAL REFERENCES 

* 27.1. Citations for Sources --> Statement
* 27.1.1. Page --> Pagination statement on a Linguistic Object
* 27.1.2. Work Cited or Illustrated --> `about` on the LO
* 27.1.3. Cited Object/Work Number --> Identifier on the cited object
* 27.1.3.1. Number Type --> classified_as on that Identifier
* 27.2. Source Brief Citation --> Statement
* 27.2.1. Source Type --> classified_as on a LO
* 27.2.2. Source Full Citation --> Longer Statement, or the LO itself 
* 27.2.2.1. Source Title --> identified_by on LO
* 27.2.2.2. Source Broader Title --> ditto
* 27.2.2.3. Source Author --> created_by/carried_out_by
* 27.2.2.4. Source Editor/Compiler --> created_by/carried_out_by with a classified_as for editor, compiler, etc
* 27.2.2.5. Source Publication Place --> used_for/took_place_at
* 27.2.2.6. Source Publisher --> used_for/carried_out_by
* 27.2.2.7. Source Publication Year --> used_for/timespan
* 27.2.2.8. Source Edition Statement --> used_for/referred_to_by
* 27.2.4. Citations Authority Record ID --> URI/identifier of the LO

### 28. PERSON/CORPORATE BODY AUTHORITY 

* 28.1. Person Authority Record Type --> `type`
* 28.2. Person/Corporate Body Name  --> `identified_by`
* 28.2.1. Preference --> `classified_as` on Name
* 28.2.2. Name Type --> `classified_as` on Name
* 28.2.3. Name Qualifier --> Could be a Statement on the Name
* 28.2.4. Name Language --> `language`
* 28.2.5. Historical Flag --> Attribute Assignment or classified_as for former
* 28.2.6. Display Name Flag --> `classified_as`
* 28.2.7. Other Name Flags --> still in `classified_as`
* 28.2.8. Name Source --> textual citation can go in a Statement, otherwise referred_to_by to a Linguistic Object
* 28.2.8.1. Page --> in the citation statement only
* 28.2.9. Name Date --> Not mapped. This is a Phase.
* 28.3. Display Biography --> Statement
* 28.4. Birth Date --> born/timespan
* 28.5. Death Date  --> died/timespan
* 28.6. Birth Place --> born/took_place_at
* 28.7. Death Place --> died/took_place_at
* 28.8. Person Nationality/Culture/Race  --> classified_as
* 28.8.1. Preference --> not mapped
* 28.8.2. Nationality/Culture Type --> classified_as/classified_as 
* 28.9. Gender --> classified_as
* 28.10. Life Roles --> if just a role, then put in classified_as ...
* 28.10.1. Preference --> not mapped 
* 28.10.2. Role Date --> ... if professional activity, put in carried_out_by with dates
* 28.11. Person/Corporate Body Event --> carried_out_by or participated_in
* 28.11.1. Event Date --> timespan
* 28.11.2. Event Place --> took_place_at
* 28.12. Related Person/Corporate Body --> Attribute Assignment of relationship
* 28.12.1. Person Relationship Type --> classified_as
* 28.12.2. Person Relationship Date --> Not mapped, this is also a Phase
* 28.13. Person/Corporate Body Broader Context --> member_of
* 28.13.1. Broader Context Date --> Not mapped, but could be modeled with Joining / Leaving
* 28.14. Person/Corporate Body Label/Identification --> Name or Identifier
* 28.15. Person/Corporate Body Descriptive Note --> Statement
* 28.18. Person Authority Record ID --> URI or Identifier

### 29. PLACE/LOCATION AUTHORITY 

* 29.1. Place/Location Authority Record Type --> `type` (always Place) 
* 29.2. Place Name --> Same as Name of Person
* 29.3. Geographic Coordinates --> `defined_by`
* 29.4. Place Types --> classified_as
* 29.4.1. Preference --> Not mapped
* 29.4.2. Place Type Date --> Not mapped
* 29.5. Related Places --> Attribute Assignment if necessary
* 29.5.1. Place Relationship Type
* 29.5.2. Place Relationship Date
* 29.6. Place Broader Context --> part_of
* 29.6.1. Broader Context Date --> Not mapped
* 29.7. Place/Location Label/Identification --> Name or Identifier
* 29.8. Place/Location Descriptive Note --> Statement
* 29.11. Place Authority Record ID --> URI or Identifier

### 30. GENERIC CONCEPT AUTHORITY 
* 30.1. Concept Authority Record Type --> `type`
* 30.2. Concept Term --> identified_by
* 30.2.1. Preference --> classified_as on the Name
* 30.2.2. Term Type --> classified_as on the Name
* 30.2.3. Term Qualifier --> Statement on the Name
* 30.2.4. Concept Language --> language
* 30.2.5. Historical Flag --> classified_as or attribute assignment
* 30.2.6. Display Term --> classified_as
* 30.2.7. Other Name Flags --> still classified_as
* 30.2.8. Term Source --> statement or referred_to_by
* 30.3. Related Generic Concepts --> Attribute Assignment
* 30.3.1. Concept Relationship Type --> not mapped
* 30.3.2. Concept Relationship Date --> not mapped
* 30.4. Concept Broader Context --> broader 
* 30.4.1. Broader Context Date --> Not mapped
* 30.5. Generic Concept Label/Identification --> identified_by
* 30.6. Concept Scope Note --> Statement
* 30.9. Concept Authority Record ID --> URI or Identifier

### 31. SUBJECT AUTHORITY 

Is the same as 30 -- no distinctions are made between Generic Concepts and Subjects
