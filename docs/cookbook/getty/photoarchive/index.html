---
title: "Getty Photo Archive Mapping"
---

{% include "toc.html" %}

## Introduction

A brief walk through of mapping a sample Photo Archive record from the Getty.

## Sample Record

```json
{
    "artist_name_1": "Rubens, Peter Paul", 
    "artist_dates_1": "1577-1640", 
    "artist_role_1": "Painter", 
    "brief_citation": "Vlieghe, CorpRub 8 (1972-73), no.144.", 
    "category": "PAINTINGS", 
    "collection_type": "Public", 
    "curr_owner_inst": "Galleria Nazionale d'Arte Antica, Palazzo Corsini", 
    "curr_regn_dist": "Lazio", 
    "curr_city": "Rome", 
    "curr_country": "Italy", 
    "curr_province": "Roma", 
    "date": "ca. 1604", 
    "dimension_units1": "cm",  
    "excollections_provenance": "Cardinal Neri Corsini (1685-1770); Purchased by the Italian government form Prince Tommaso Corsini (1884)", 
    "filing_category": "Religious, Devotional", 
    "gcpa_acc_no": "292221", 
    "height_1": "153", 
    "media_materials": "Oil on canvas", 
    "name_title": "St. Sebastian", 
    "national_school_1": "Flemish", 
    "photo_collection": "Erwin Panofsky Collection", 
    "photo_color": "Bl/Wh", 
    "photo_source": "Anderson", 
    "photo_src_ref": "1195", 
    "reference_number": "Inv. 388",
    "width_1": "118"
}
```

Which describes a photograph of a painting of St Sebastian being tended by angels.  You can see information about the painting at these sites:

* [Owning Museum](http://www.barberinicorsini.org/opera/san-sebastiano-curato-dagli-angeli/)
* [Dutch Institute for Art History](https://rkd.nl/en/explore/images/120267) 

The current, aging, online record built from the information above looks like:

![Star Record Screenshot](rubens_starweb.png){: width="650px"}

## Overview

The model for the photo archive is divided into two main parts: the description of the photograph and its provenance, and the description of the artwork depicted in the photograph.  Both are treated as valuable objects in their own right.

### The Photograph

The photograph in the archive does not have many properties in this record. Most are about the object depicted in the photograph.

In particular:

 * `gcpa_acc_no`: the Getty Accession number
 * `photo_color`: whether the photograph is black and white, or color
 * `photo_collection`: the original photographer or collector's collection
 * `photo_source`: who the Getty acquired the photograph from
 * `photo_src_ref`: the source's reference number for the photograph

Other records also have:

 * `photo_date`: the date the photograph was taken
 * `photo_coll_ref`: the reference number in the original collection
 * `shelf_number`: the (older) shelf-based reference number the photograph
 * `acquisition_date`: the date the photograph was acquired
 * `photo_notes`: freetext notes about the photograph 

The mapping approach is:

 * The photograph itself is an [object](model/object)
 * The `gcpa_acc_no`, `photo_src_ref` and `photo_coll_ref` values are [identifiers](/model/object/identity), with collection specific contexts
 * The transaction between the `photo_source` and the Getty is modeled according to the [provenance](/model/provenance) model
 * The `photo_date` provides the timespan for the creation of the photograph (we do not distinguish between the act of photographing and printing of the physical photograph)
 * The `photo_notes` information is a note associated with the object, modeled in the same way as other [descriptive texts](/model/base/index.html#base_stmt).
 * The photograph then shows an image, which represents the art object, as described under [depiction](/model/aboutness/#depiction)

This results in the model:

![Photograph Model](photo_model.png){: width="800px"}


### The Depicted Object

The rest of the information is about the object depicted.

 * The `artist*` fields, `national_school` and `date` provide the [creation information](/model/provenance/#object-creation) and information about the [artist](/model/actor/).
 * `name_title` is the [title](/model/object/identity/#titles) of the object
 * The `current*` fields, `reference_number` and `collection_type` are the last known location and owner of the object, described using the provenance model
 * `height`, `width` and `dimension_units` plus `media_materials` are the [physical characteristics](/model/object/physical/) of the object
 * `category` is object type, and `filing_category` is the [subject](/model/object/aboutness/#subject).
 * `excollections_provenance` is further known provenance information

## Mapping in Detail

### The Photograph

We create a `ManMadeObject` to represent the photograph, by checking the `photo_color` property to see whether it should be black and white _(aat:300128359)_, color _(aat:300128347)_ or if not present, then just a photograph _(aat:300046300)_.
We construct a label for the photograph based on this type and the name of the object depicted.

```crom
top = PhotographBW()
top._label = "Black and White Photograph of 'St. Sebastian'"
```

We create an Identifier for the Accession Number, and type it as  _(aat:300312355)_. This is referenced from the photograph with the `identified_by` property.

```crom
top = AccessionNumber()
top.content = "292221"
```

A second `Identifier` for Anderson's identifier is created. This identifier is associated with the source collection.  We also create an Acquisition activity, by which the photograph is acquired by The Getty. This is not shown in the example below, but is shown in the full description of the photograph.

```crom

top = PhotographBW()
top._label = "Black and White Photograph of 'St. Sebastian'"
srccoll = CollectionSet()
srccoll._label = "Collection of Anderson"
who = Actor()
who._label = "Anderson"
cre = Creation()
cre.carried_out_by = who
srccoll.created_by = cre
top.member_of = srccoll
idr = Identifier()
idr.content = "1195" 
#proxy = Proxy()
#proxy.proxyFor = top
#proxy.proxyIn = srccoll
#proxy.identified_by = idr
```

We create the original collection, despite only having a label for it. 

The above needs work, as the Anderson Collection does not *currently* aggregate the photograph. See [Issue 147](https://github.com/linked-art/linked.art/issues/147).
{: .warning}

Plus we link the, as of yet unconfigured, Painting resource to it via a `VisualItem`.

```crom
top = PhotographBW()
top._label = "Black and White Photograph of 'St. Sebastian'"
coll = CollectionSet()
coll._label = "Erwin Panofsky Collection"
top.member_of = coll
vi = VisualItem()
vi._label = "Image on Photograph"
art = Painting(art=1)
vi.represents = art
top.shows = vi
```

We can thus fill in the data about the photograph to our model:

![Photograph Data following Model](photo_data.png){: width="800px"}


### The Art Object

We can fill out a lot of details about the object itself.  In particular, it has a Title (which we also associate with the object directly as a label), height and width dimensions in centimetres, and a parseable materials statement.  We record both the statement as a `LinguisticObject`, as well as breaking the information out into machine readable material and part resources.

```crom
top = Painting(art=1)
top._label = "St. Sebastian"
apl = Name()
apl.content = "St. Sebastian"
top.identified_by = apl
h = Height()
h._label = "Height"
h.value = 153
h.unit = instances['cm']
w = Width()
w._label = "Width"
w.value = 118
w.unit = instances['cm']
top.dimension = h
top.dimension = w
mats = MaterialStatement()
mats.content = "Oil on canvas"
top.referred_to_by = mats
top.made_of = instances['oil']
part = SupportPart()
part._label = "Canvas Support"
part.made_of = instances['canvas']
top.part = part
```

Now we can tackle the creation of the painting.  The activity is a `Production`, which was carried out by the artist at a particular point in time.  We know the artist's name and their birth and death dates, and an approximate date for the activity.

```crom
top = Production()
artist = Person()
artist._label = "Rubens, Peter Paul"
birth = Birth()
bt = TimeSpan()
bt._label = "1577"
bd = "1577-01-01T00:00:00Z"
bt.begin_of_the_begin = bd
be = "1578-01-01T00:00:00Z"
bt.end_of_the_end = be
birth.timespan = bt
death = Death()
dt = TimeSpan()
dt._label = "1640"
dd = "1640-01-01T00:00:00Z"
dt.begin_of_the_begin = dd 
de = "1641-01-01T00:00:00Z"
dt.end_of_the_end = de
death.timespan = dt
artist.born = birth
artist.died = death
top.carried_out_by = artist
ts = TimeSpan()
ts._label = "ca. 1604"
ts.begin_of_the_begin = "1603-01-01T00:00:00Z" 
ts.end_of_the_end = "1606-01-01T00:00:00Z"
top.timespan = ts 
```

Due to research by the photo archive catalogers, we know a relatively recent (if not necessarily absolutely current) owner, location and identifier for the object. The owner and identifer follow the same pattern as for the identifiers of the photograph.

```crom
top = Painting(art=1)
top._label = "St. Sebastian"
coll = CollectionSet()
coll.classified_as = instances['public collection']
own = Group()
own._label = "Galleria Nazionale d'Arte Antica, Palazzo Corsini"
cre = Creation()
cre.carried_out_by = own
coll.created_by = cre
top.member_of = coll
#proxy = Proxy()
#proxy.proxyFor = top
#proxy.proxyIn = coll
#idr = Identifier()
#idr.content = "Inv. 388"
#proxy.identified_by = idr
```

And its current location is very well described in the data, so we map all of it in this example.  However, this is not a recommended pattern and instead a gazetter or vocabulary such as TGN or Geonames should be used instead.  Only places that do not have existing identities should have new identities created.  Instead, the city of Rome should be identified as `tgn:7000874-place` and then the TGN hierarchy used for the province, region, and country.

```crom
itl = Place()
itl._label = "Italy"
laz = Place()
laz._label = "Lazio"
rom = Place()
rom._label = "Roma"
top = Place()
top._label = "Rome"
top.part_of = rom
rom.part_of = laz
laz.part_of = itl
```

And a few additional features for the provenance statement, a brief citation and a category:

```crom
top = Painting(art=1)
top._label = "St. Sebastian"
ps = ProvenanceStatement()
ps.content = "Cardinal Neri Corsini (1685-1770); Purchased by the Italian government form Prince Tommaso Corsini (1884)"
top.referred_to_by = ps
bc = LinguisticObject()
bc._label = "Vlieghe, CorpRub 8 (1972-73), no.144."
top.referred_to_by = bc
io = InformationObject()
t = Type() # NB Explicitly no id to generate local identifier
t._label = "Religious, Devotional"
io.about = t
top.carries = io
```

Putting all of the above together gives us a full description of the artwork depicted in the photograph.
