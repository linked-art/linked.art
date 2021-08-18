---
title: CIDOC-CRM Class Analysis
up_href: "/model/profile/"
up_label: "Profile"
---

[TOC]

## Introduction

This is a brief analysis of the classes in the CIDOC-CRM ontology and their practical utility. The definition of "useful" is those classes which a reasonably comprehensive producer or consumer of a CIDOC-CRM based model should be expected to understand and would make functional differentiations on. Following this definition, there are several sets of classes that can be ignored, for various reasons.

## Classes to Ignore

### Abstract Classes

__Classes:__  E1, E2, E18, E19, E20, E24, E28, E63, E64, E70, E71, E72, E77, E90, E92

There are 16 classes which are not themselves directly used, however are the domain or range of useful relationships, or otherwise important distinctions within the class hierarchy. These classes likely need to stay in the ontology, but can be ignored for practical purposes.  Producers should never put them into their data, and consumers can likewise expect to never see them in data.  E63 and E64, the beginning and ending of existence respectively, are included in the set of abstract classes as their class-specific sub-classes are used instead. The issue that previously led to their use in data was resolved by splitting the event that caused the end of existence of a physical thing, from the actual Destruction of it, especially as the same event could destroy multiple objects. 

### Data Type Classes

__Classes:__ E59, E60, E61, E62, E94, E95

The classes in the CRM that model data types (String, Number, etc) can be ignored, and indeed are ignored in the recent RDF ontologies.  Instead the appropriate XSD types should be used in their place:

  * _E59 Primitive Value_ - rdf:Literal
  * _E60 Number_ - xsd:integer / xsd:float as appropriate
  * _E61 Time Primitive_ - xsd:dateTime
  * _E62 String_ - xsd:string
  * _E94 Space Primitive_ - Use appropriate external vocabulary or format, such as [WKT](http://docs.opengeospatial.org/is/12-063r5/12-063r5.html)
  * _E95 Spacetime Primitive_ - Use appropriate external vocabulary or format

### Overly Specific Classes

There are many classes that fail the CRM's own test of individual importance. These can be broken down into clusters.  The solution for all of these classes is instead to use _P2 has type_ to refer to an external vocabulary, if needed at all.

__Attribution Reification Classes:__ E14, E15, E16, E17

All of the subclasses of _E13 Attribute Assignment_ can be dispensed with, and replaced with references to external vocabularies from an instance of E13.  This would be more consistent with other assignments that must use E13 directly, such as attribution of an artist to a production event, the valuation of an object assigning a Monetary Amount to an object, the naming of an object assigning an Appellation and so on. 

__Appellation Classes:__ E35, E41, (E44, E45, E46, E47, E48, E49, E50, E51, E75, E82)

All of the subclasses of _E41 Appellation_ can be dispensed, other than E42 Identifier. For the most part there is also no need to associate specific vocabulary terms to replace them. The name of a Place does not need to be an _E44 Place Appellation_, as this carries no additional information beyond the class of the subject of the relationship. This also prevents the modeling collision between Names (E44 and similar) and Identifiers (E42) for resources as it would be questionable which of the two classes to use.  It should be noted that Identifiers are not Linguistic Objects, even if they are derived from some formal identifier scheme. This argument was agreed upon by the maintenance body for the ontology, leading to the official deprecation of E44, E45, E46, E47, E48, E49, E50, E51, E75 and E82!  

E41 Appellation is also added to the list of classes to ignore, as it is not also a Linguistic Object.  The number of Appellations which are not Linguistic is infinitesimal compared to the set of Linguistic Appellations, and hence we use only the `Name` mapping of `E33_E41_Linguistic_Appellation` that inherits both Appellation and Linguistic Object. This class should be used in place of E35 Title for consistency.

__Entity Specialization Classes:__ E27, E31, E32, E40, E83, E84, E96, E99 

These classes (_E27 Site, E31 Document, E32 Authority Document, E40 Legal Body, E84 Information Carrier, E96 Purchase, E99 Product Type_) have no useful distinguishing features beyond what could easily be conveyed with a Type on their respective parent classes.  Authority Documents and concepts should instead use the W3C's SKOS ontology rather than attempting to model knowledge organization using CRM. Information Carriers are only distinguished from Man Made Objects by the unknowable intent of the designer. Likewise, the distinction between E73 and E31 is that instances of E31 is that subset of E73s that make propositions about reality ... which is not a very useful or tractable distinction.  While Purchase does have a property (had_sales_price), it is quickly insufficient for any non-trivial transaction or description common in the art market, including multiple buyers or sellers, commissions, part payment/part exchange, reserve prices, and so on. Given the need for a Payment class, and the use of dimension to relate other prices, Purchase becomes unnecessary. E83 is added to the overly specific set of classes, as there's nothing to distinguish the creation of a Type from the creation of any other conceptual resource. The additional properties might be useful in a vocabulary management system, however that is not the purpose of this profile (nor of CRM generally, one might argue, compared to SKOS or other more appropriate ontologies).

__Visual Concept Classes:__ E34, E37, (E38)

There is a significant overlap between the classes _E34 Inscription_, _E36 Visual Item_, _E37 Mark_ and _E38 Image_. The simplest approach is to use only E36 for visual or image content, and instead of E34, instead use _E33 Linguistic Object_ to capture inscriptions.  _E38 Image_, while a more appealing class name, has no additional features or meaning beyond that of E36, and was officially deprecated from the ontology for this reason. Similarly, E37 has no differences with E36. The use of E33 for inscriptions is more consistent with other modeling of textual information, assuming that the inscription really contains linguistic content.  For the situations where it is uncertain if an inscription is linguistic, then E36 is preferred. Note that E37 "does not intend to describe ... an individual physical embodiment", which is modeled instead as a Man-Made Object.

__Curated Holding Classes:__ E78, E87

The _E78 Curated Holding_ class, formerly called Collection, is the subject of much debate as to the requirements for which sets of objects can be considered collections (curated holdings) and which are sets of objects that are not curated. In order to have a consistent approach, in the absence of a separate class to represent sets, the preferred class for all such aggregations is `Aggregation`.  Collections can be typed as such using the well established P2_has_type relationship to an appropriate vocabulary.  This also obviates the need for E87, as an overly specific subclass of Activity.  `Aggregation` is preferred over E19 Physical Object for consistency with sets of other types of resource, and that a Collection which was never brought together stretches the limits of the definition.  It also makes it very hard to distinguish between an object with physical parts (Painting with a Frame) and a Collection with members (Paintings Collection with a Painting).

__Condition Classes:__ E3

Not only is there no current use case for _E3 Condition State_, it is too complex to use in any practical way, and lacks important additional structure in the ontology to make it worth the effort.  For example, there is no way to create an identity for "Box with lid open" versus "Box with lid closed" for the purposes of associating measurements or photographs.  

__Incomprehensible Classes:__ E93

_E93 Presence_ is simply incomprehensible. As such, it has no known use cases and is impossible to know whether it is useful or not. It is telling that there are no examples given in the documentation.

The definition is:

> This class comprises instances of E92 Spacetime Volume, whose arbitrary temporal extent has been chosen in order to determine the spatial extent of a phenomenon over the chosen time-span. 

It has been explained as the "wormhole" through space and time that an entity occupies. With complete knowledge of a universe, this might be interesting to calculate relative positions in time and space ... however we lack the supercomputing power and panopticon sensors needed to do this. 


## Useful Classes

The remaining classes are actively used in mappings for the known datasets.

  * _E4 Period:_  Activities such as Productions will often only fall within a named Period
  * _E5 Event:_ Events can be depicted by Artworks
  * _E6 Destruction:_ The event of the destruction of an Object
  * _E7 Activity:_ Activities of Actors and their interactions with objects is a core feature
  * _E8 Acquisition:_ Needed for Provenance
  * _E10 Transfer of Custody:_ Needed for Exhibitions
  * _E11 Modification:_ A significant change to an object, that did not destroy it, is worthy of description
  * _E12 Production:_ The beginning of existence of a physical thing.
  * _E13 Attribute Assignment:_ Used for recording previously believed values
  * _E21 Person:_ Individual people
  * _E22 Human-Made Object:_ Objects
  * _E33 Linguistic Object:_ Statements
  * _E33 E41 Linguistic Appellation:_ The class for Names, recently added to the ontology
  * _E36 Visual Item:_ Used for images and image content
  * _E39 Actor:_ Used when it is unclear if the actor is an individual or a group 
  * _E42 Identifier:_ Identifiers of things
  * _E52 Time-Span:_ Collects the beginning and ending of time spans
  * _E53 Place:_ Locations
  * _E54 Dimension:_ Dimensions of objects 
  * _E55 Type:_ References to external vocabularies, such as AAT
  * _E56 Language:_ Used when the text of a E33 is not available, but the language is known. When the value is available, it should use the RDF language tags instead.
  * _E57 Material:_ The type of Material that makes up an object
  * _E58 Measurement Unit:_ The unit of measurement for a dimension value, such as inches
  * _E65 Creation:_ Similar to Production, an Activity that creates non-physical things
  * _E66 Formation:_
  * _E67 Birth:_
  * _E68 Dissolution:_
  * _E69 Death:_
  * _E73 Information Object:_ Concepts, Schemes, Texts  
  * _E74 Group:_ Married Couples, Organizations, Workshops, etc. that can take actions as a single entity
  * _E79 Part Addition:_ Similar to Modification, adding parts can substantially change an object
  * _E80 Part Removal:_ And the inverse, the removal of a Part is also important for denoting samples used for conservation research
  * _E85 Joining:_ Primarily used for recording the time of getting married
  * _E86 Leaving:_ Primarily used for recording the dissolution of a marriage
  * _E89 Propositional Object:_ Used very sparingly, when there is no symbolic representation that makes sense for a proposition about reality, such as the promise to pay expressed by bidding on an object at an auction, indicated only by the bidder raising their hand.
  * _E97 Monetary Amount:_ Recording an amount of money for a price or payment
  * _E98 Currency:_ The currency of the monetary amount
  

## Optional Classes

After analysis of the datasets available from multiple consortia and large individual organizations, the data available does not currently require using these classes. This is not to say that they will not be useful in the future, just that they are not used by any currently known instance. In particular:

  * _E9 Move_ requires information that is not often tracked - the explicit activities used to move objects between locations - to be useful. In a dedicated inventory management system it could be valuable to track shipping objects between venues or moving between galleries, but this is unlikely to be made available as public Linked Open Data.
  * _E26 Physical Feature_ is useful for describing non-man-made non-objects such as arches or caves, however none of the datasets needed this and E22 is a reasonable approximation.
  * _E29 Design or Procedure_ might be useful in a conservation-specific specific system, if carefully described procedures are being explicitly modeled and activities that follow them recorded. 
  * _E81 Transformation_ might be useful in some situations where one object is transformed into another as part of the artistic process. We typically lack the knowledge of the object prior to the documented form, however.

## Appropriated Classes

_E30 Right_

The definition of E30 Right in CIDOC-CRM doesn't fit any actual need that has been encountered to date. The rationale is below, but the summary is that E30 is conceptual and is not contextualized by space or time, however the legal status of objects changes all the time. This is covered in more, excruciating, detail in the note below.

Given that the class is not useful as currently defined, the approach has been taken to attempt to fix that usage within the context of Linked Art, and then submit the necessary changes with evidence from the community back to the ontology maintenance agency for consideration of a revised model. This has been discussed within the SIG, and is thus expected rather than subversive.

!!! note "The Problem of Rights"

    The basic problem with E30 Right is that it is a Conceptual Object, and Conceptual Objects cannot be destroyed.  While there is any carrier of the object, including the CIDOC-CRM description of it or even within someone's memory, then the concept still exists somewhere.  As it cannot be written down without persisting it, it cannot be destroyed and instead it can simply pass out of all knowledge.  This means that the existence of the Right is not the same as the validity of the Right: the concept of slavery in America still exists, but it is no longer legally valid. There are no terms within the CRM to express the effective dates, and the CRM-SIG clarified that the right's effectiveness would be a different sort of resource.  In particular that an E30 Right "is the formulation of the right, the terms", and not whether the right had any legal standing in any jurisdiction at any point in time.

    It also means that for every combination of Right+Object+Actor, there are many instances, all of which exist at the same time. The Right of Ownership of the Mona Lisa has at least one instance per Actor that ever actually owned it, and given the conceptual nature of E30, there could be many Rights for Actors that never actually owned it.

    There is also no way to distinguish jurisdiction or legal code under which the right would exist, if it was ever in force. The discussion of the SIG was inconclusive as to whether a Right can be conceived by anyone, or only by Actors with the potential to make them legally enforcable even if they never do so. In other words, if I conceive of the terms of a Right of ownership, that applies to the Mona Lisa, and is possessed by myself ... is that an E30 Right, or is it just a Conceptual Object that quacks like a Right. If I cannot conceive Rights into existence, the requirements for agents that can conceive them are unknown, especially given that they're not governed by legal jurisdictions nor time. 

    Finally, E72 Legal Object is not the parent of Conceptual Object but instead of Symbolic Object. This means that Rights cannot be applied to ideas, yet patents can provide legal protection for those ideas. Thus even if all of the above were solved, Rights would still not cover the correct set of classes without multiple instantiation.

    In summary, CIDOC-CRM lacks the expressiveness to state what is required and the current definition of E30 Right is insufficiently clear for use as currently documented in the standard. If you're still not convinced, you can read [the email thread that starts here](http://lists.ics.forth.gr/pipermail/crm-sig/2017-August/003045.html) (if you dare).


## Useful Additional Classes

__Payment__

There is currently no way to describe the Activity of transferring MonetaryAmounts between actors, a Payment.  The transfer classes (Acquisition, Transfer of Custody, Move) are very specific as to their semantics and the sorts of things that can be transferred. Thus, a new class is required, `Payment`, with three relationships of `paid_from`, `paid_to` and `paid_amount`.  A better solution would be a low level transfer class that could be used to transfer right of custody, right of ownership, the object itself, and monetary amounts, from one actor to another.

