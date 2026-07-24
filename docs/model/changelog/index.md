---
title: Linked Art Data Model Change Log
---


## Data Model Change Log

This is the log of changes per version of the Linked Art Data Model to make it easier to track and understand how the model has evolved over time. It is organized incrementally by version, and assumes that Version 1.0 is the first version.

## Version 1.x Series

Version 1.0 was released in February 2025.

### Version 1.1 

Version 1.1 was released on _____ and includes the following changes.

#### New Features

* Performing Arts model. 


#### Clarifications

* Updated the language about "event" and "activity" to be more consistent, especially in the Provenance section.
* Clarified that references, other than Concept References, cannot have `classified_as`, as implied by the example.


#### Typos

* Fixed typo in base model documentation in the Stowe Auction example
* Fixed missing middle name example in actor example
* Fixed note styling for Inanimate Thing or Dead Person callout in actor model
* Removed `classified_as` entry from the reference API example as confusing
* Added missing `id` fields for references in Person examples
* Fixed array vs string for `notation` in Language API documentation 

#### Vocabulary Changes

* Added missed "Part Type" vocabulary term to required vocabulary entries. An oversight in 1.0
