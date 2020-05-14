---
title: "Actors: People and Organizations"
---

[TOC]

## Introduction

All activities are carried out by some actor, either a person (`Person`) or a group of people (`Group`) such as an organization or company.  The identity and description of these actors are very important to record in order to provide the human context for the activities, and their related places and objects. The creators, finders, owners, sellers and curators of objects are all relevant to understanding our cultural heritage.

As far as scope goes, the model does not consider that non-humans (such as software or animals) can perform activities, as activities require some notion of intent. Thus the [infamous monkey selfies from 2011](https://www.cnn.com/2018/04/24/us/monkey-selfie-peta-appeal/index.html) is not carried out by anyone, as the monkey cannot do it and the photographer did not intend for the selfies to be taken.

This model does not aim to capture all of the possible information about a Person or Group, or their relationships to other people, objects, places or activities. Instead it attempts to capture sufficient information to distinguish the actor from others, and to align the actor with other systems. 

## Types

There are two primary types of acting agent, `Person` and `Group`. `Person` is used for humans, and `Group` is used for any collective set of humans.  Groups typically are able to take action as a coherent whole, but in some cases this is overlooked for simplicity's sake.  For example, it is useful to be able to say that "The Museum" acquired a painting or "The Workshop" produced a sculpture, when in fact it was some subset of the members of the group that actually performed the activity but we do not know exactly who. 


`Person` and `Group` are sub-classes of the `Actor` class, which might be used when it is not certain whether the actor is a Person or a Group. For example, if a sale of an object is listed as being from an art dealer called "Smith", it is unclear whether it refers to a person via their family name, or to an organization named after its owner.  Equally, if there is no information about the actor currently available, but identity is desired such that it can later be reconciled or used because there is some other information known, then the use of `Actor` is likely needed in this case as well. This is only to be used when the nature of the actor is unknown to avoid asserting the existence of a Person when it might have been a Group, or vice versa.

__Example:__ 

Example Museum, a `Group`, acquires something from a J. Smith, a `Person`.

```crom
who = Person()
who._label = "J. Smith"
grp = MuseumOrg()
grp._label = "Example Museum Organization"
top = Acquisition()
top.transferred_title_from = who
top.transferred_title_to = grp
```

## Names

Names are described in detail in the [shared patterns section](/model/base.html#names). If there is a primary or main name to use, it should be `classified_as` _aat:300404670_.


__Example:__

A person named "J. Smith"

```crom
top = Person()
top._label = "J. Smith"
apl = PrimaryName()
apl.content = "J. Smith"
top.identified_by = apl
```

### Parts of Names

Personal names can often be broken down into parts, with different types.  The types are given using the `classified_as` property. The name parts are themselves `Name`s, and are included in the `part` set in the same way as other partitioning. The type of name is given using `classified_as`, in the regular fashion. Western name division vocabulary is given below, and other name part types should be suggested.

Recommended Vocabulary:

| Term        | Vocabulary        |
|-------------|-------------------|
| First Name  | _(aat:300404651)_ |
| Middle Name | _(aat:300404654)_ |
| Last Name   | _(aat:300404652)_ |
| Prefix      | _(aat:300404662)_ |
| Suffix      | _(aat:300404845)_ |


Example: A person named "Lady Joan A. Smith, Duchess of Wolverhampton"

```crom
top = Person()
top._label = "Lady Joan A. Smith, Duchess of Wolverhampton"
apl = PrimaryName()
apl.content = "Lady Joan A. Smith, Duchess of Wolverhampton"
top.identified_by = apl
given = GivenName()
given.content = "Joan"
fam = FamilyName()
fam.content = "Smith"
pref = NamePrefix()
pref.content = "Lady"
suff = NameSuffix()
suff.content = "Duchess of Wolverhampton"
mid = MiddleName()
mid.content = "A."
apl.part = pref
apl.part = given
apl.part = mid
apl.part = fam
apl.part = suff
```

## Identity

People and Organizations are often assigned identifiers that should be recorded and tracked in the same way as any other identity. These follow the same [basic pattern][/model/base.html#identifiers] as for other identifiers, with `identified_by` being used with an `Identifier` resource.

__Example:__

A local identifier for the person is "643".

```crom
top = Person()
top._label = "Xavier Y. Zeelander"
pid = LocalNumber()
pid.content = "643"
top.identified_by = pid
```

### Other Linked Data Identifiers

There may be other identifiers for the person available in external systems, such as [ULAN](http://vocab.getty.edu/ulan/) or any of a dozen others.  If all of the information needed about the person is available from that system, then it is recommended to simply use that identifier directly as the URI for the Person.  If there is a requirement to maintain separate information about the person, then the `exact_match` property should be used to align the two. This might happen when, for example, the local data has additional information about which documents refer to the person, or more detailed biographical information.


__Example:__

Van Gogh has the ULAN identity `http://vocab.getty.edu/ulan/500115588`

```crom
top = Person()
top._label = "Vincent Van Gogh"
ulan = BaseResource("http://vocab.getty.edu/ulan/500115588")
ulan._label = "Van Gogh, Vincent"
top.exact_match = ulan
```

## Addresses

People and Organizations often have addresses, physical or online, via which they can be contacted. This includes mailing addresses, email addresses and so forth.  These are referenced separately from Names and Identifiers, as many Actors might have the same contact point. The address is an identifier for a location or service, and is thus modeled as an Identifier. This means it does not have language information, unlike Names, but addresses are not inherently linguistic. 

This `Identifier` is then related to the actor via the `contact_point` property.  They can be `classified_as` different types, and use the `content` property to capture the address itself.

__Example:__

The person A. Bacchus has an email address, and can be contacted via mail at the museum they are employed by.

```crom
top = Person()
top._label = "A. Bacchus"
cp = vocab.EmailAddress()
cp.content = "a.person@example.org"
top.contact_point = cp
org = MuseumOrg()
org._label = "Example City Museum"
sa = vocab.StreetAddress()
sa.content = "1200 Museum Drive, Example City"
org.contact_point = sa
top.member_of = org
```

## Life Events

There are key events in a person or organization's lifespan that are often recorded as they contribute core information for determining the identity of the actor.  These include the birth or formation, death or dissolution, and the period in which they carried out the work they are known for.

### Birth and Death / Formation and Dissolution

Like the production of objects or the creation of texts, people and organizations also come into and out of existence through events.  These events can take place at certain Places, and happen at certain times.  

People are born in `Birth` events and die in `Death` events, related to the person by the `born` and `died` properties respectively. Groups are formed in `Formation` events, and dissolved in `Dissolution` events, referenced via the `formed_by` and `dissolved_by` properties. These classes are modeled not as Activities, but as Events that are not themselves carried out by anyone. They are the coming into existence instant of the person, not the conception of the couple, the labor of the mother, or potentially the killing by a murderer. These activities can be modeled as causes, as described below.

Birth and Death do not have any properties of their own that are used in the model, only those inherited from the event superclass, such as `timespan` and `took_place_at`.

!!! "note" "Inanimate Thing or Dead Person?"
    After death, people are still instances of `Person` which is a subclass of `Actor`, even though they can no longer carry out activities.  People in comas or otherwise completely incapacitated also cannot carry out activities, but are not temporarily non-Actors. The modeling that death is a transformation from an instance of Person to an instance of Thing adds complexity for the sake of purity, but does not add any actual value. Thus a burial activity (_aat:300263485_) buries a Person, not a Thing-that-used-to-be-a-Person. However if the skeleton is then dug up and exhibited, it is exhibited as a Thing. There is, therefore, a transition at some undetermined point.

Example:  The birth and death of Amanda B. Curtlett.

```crom
top = Person()
top._label = "Amanda B. Curtlett"
birth = Birth()
bts = TimeSpan()
bts.begin_of_the_begin = "1767-01-09"
bts.end_of_the_end = "1767-01-12"
birth.timespan = bts
death = Death()
dts = TimeSpan()
dts.begin_of_the_begin = "1824-08-21"
dts.end_of_the_end = "1824-08-21"
death.timespan = dts
dloc = Place()
dloc._label = "Death Place"
death.took_place_at = dloc
top.born = birth
top.died = death 
```

Example: The formation and dissolution of the ill-fated Example Organization

```crom
top = Group()
top._label = "Example Organization"
form = model.Formation()
form._label = "Formation of Example Organization"
top.formed_by = form
fts = TimeSpan()
fts.begin_of_the_begin = "1639-12-01T00:00:00"
fts.end_of_the_end = "1639-12-31T23:59:59"
form.timespan = fts
dis = model.Dissolution()
dis._label = "Dissolution of Example Organization"
top.dissolved_by = dis
dts = TimeSpan()
dts.begin_of_the_begin = "1790-06-12T00:00:00"
dts.end_of_the_end = "1790-06-12T23:59:59"
dis.timespan = dts
```

### Active Dates

It is often useful to know where and when the person or organization was active in their professional function. For example, an artist might have started painting when they were 20, stopped by 30, and only painted in Italy. This information can be used to help eliminate dubious attributions, for example.

The property for the Person or Group is `carried_out`, the inverse of the more familiar `carried_out_by` from Activities to Actors. The `Activity` resource should be `classified_as` _aat:300393177_, meaning the time when the actor is actively performing their primary professional function.  The other properties of activities can and should also be used.  

Example: Patrick Q. Robertson was active between 1910-01-01 and 1934-03-21

```crom
top = Person()
top._label = "Patrick Q. Robertson"
active = vocab.Active()
ats = TimeSpan()
ats.begin_of_the_begin = "1910-01-01"
ats.end_of_the_end = "1934-03-21"
active.timespan = ats
top.carried_out = active
```

## Descriptive Information

### Biography

Biographical descriptions follow the `LinguisticObject` [pattern](/model/base/index.html), with biography _(aat:300080102)_ as the classification.  In all other respects, it is a vanilla usage of a resource being `referred_to_by` a particular text.

Example: David E. Frederickson's very short example biography.

```crom
top = Person()
top._label = "David E. Frederickson"
bio = BiographyStatement()
bio.content = "David was born at a very early age."
top.referred_to_by = bio
```

### Nationality

Nationality is modeled as a Type that is associated with the Person, rather than as a Group as described in the CIDOC-CRM ontology document.  This is because all of the people, across all time, who have had a particular nationality, cannot take action as a single coherent entity.  As Group is a sub-class of Actor, it is not thought to be an appropriate class for this use. Without proliferating new classes (e.g. sets of people that are not actors), the traditional and perfectly consistent way to describe nationality is as a flag on the person, which is modeled as a Type.

The `Type` resource should have _aat:300379842_ as one of its classifications, such that a consuming application can find all of the nationality types from amongst the person's classifications. The nationality resource should either be from an established vocabulary of nationalities, or have an `exact_match` to an established vocabulary entry if additional local information is necessary to record, such as a particular name for that nationality.

Example: Jeremy K. Lintott is a British national.

```crom
top = Person()
top._label = "Jeremy K. Lintott"
natl = Nationality("http://vocab.getty.edu/aat/300111159")
natl._label = "British"
top.classified_as = natl
```

### Ethnicity

Ethnicity is separate from nationality, as it refers to a social group or culture as opposed to a political nation or state. The same argument as to why nationality is modeledthis is not a Group applies



### Gender

Gender is a hotly debated and politically charged topic. The intent of this section is not to take a stand on those debates, but instead to allow the representation of data in museum and other information management systems to be made accessible.

Gender is not specifically discussed in CRM, in fact it was even deleted from a previous version, and the current modeling decision is to echo the same `Aggregation` pattern as for nationality. This allows a plethora of gender diversity, and does not make any specific statements about biological versus assumed versus prefered gender roles.  A Person can be a member of multiple groups at the same time, allowing the association with multiple genders with this modeling decision.  Gender based groups should be `classified_as` _aat:300055147_ along with any specific classification known.

```crom
top = Person()
top._label = "Mabel N. Overton"
gender = Gender("http://vocab.getty.edu/aat/300189557")
gender._label = "feminine"
top.classified_as = gender
```

### Digital Integration

Images of the person can also be provided, in the same way as for [images of objects](/model/object/digital/) via the `representation` property. If IIIF resources, web pages or other digital content is available, the same patterns as for objects also apply.  Only the basic image case is shown below, the other scenarios can easily be determined from the referenced digital integration for objects.

FIXME

```crom
top = Person()
top._label = "Gertrude H. Ingram"
# img = DigitalImage("http://example.org/images/gertrude.jpg")
# img._label = "Image of G.H. Ingram"
# img.format = "image/jpeg"
# top.representation = img
```



## Organization Membership

As discussed above, Organizations can be seen as the actor when it comes to their roles in various events. For example, an auction is likely to be carried out by an organization, and they can own and curate objects.

The only significantly new aspect to organizational actors, compared to people, is that they can have members.  These members can be either sub-groups, such as a department within a museum, or individuals.

For example, a curator could be a `member_of` a department, which is in turn a member of the wider institution.  This is simply the inverse of `member` relationship described in the [base patterns](/model/base/#25-organizations).

```crom
top = Person()
top._label = "Sameen T. Underwood"
dept = Department()
dept._label = "Paintings Department"
mus = MuseumOrg()
mus._label = "Example Museum"
top.member_of = dept
dept.member_of = mus
```



