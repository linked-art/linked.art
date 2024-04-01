---
title: "Places"
---

[TOC]

## Introduction

Places are one of the foundational classes in the model.  Events and activities occur at both a time and a place, objects of all sizes have locations, and people and organizations have associated locations where they reside or are otherwise associated with. Places are extents in space, independent of time or what may or may not be present in that space. For built works such as architecture and works that are fixed in location due to their media (a cave drawing for example), Place is a defining characteristic.

Places also form a core integration point with Geographical Information Systems (GIS) and map based user interfaces. By aligning with these other systems, we enable better usability and interactivity with our data. 

## Core Information

All of the core information for resources is available for Place, including identifiers, classifications, labels, names, statements and so forth.

It is recommended that external gazeteer systems be used for recording the spatial hierarchy of Places, however it is still useful to be able to position historical locations within their larger geospatial context.  This uses the same partitioning pattern as all other classes in the model.

__Example:__

There is a city called Amsterdam in the Netherlands.

```crom
top = vocab.City(ident="amsterdam/1", label="Amsterdam")
top.identified_by = model.Name(content="Amsterdam")
top.referred_to_by = vocab.Description(content="Amsterdam is a city in the Netherlands")
top.part_of = vocab.Nation(ident="netherlands", label="Netherlands")
```

## Geospatial Location

One of the expected user interface requirements for places is the ability to plot them on a map.  In order to do this, or to calculate the geospatial overlap of places, it is useful to have a geometry that describes the place's boundaries in the real world. This could be very detailed, a simple bounding box within which the place fits, or a point close to the center of the area.

This is handled simply by associating a [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) string with the place using the `defined_by` property. A simple user interface for generating WKT representations is available from the [Wicket Project](https://arthur-e.github.io/Wicket/sandbox-gmaps3.html).


__Example:__

A polygon that (approximately) defines the country of New Zealand.

```crom
top = vocab.Nation(ident="new_zealand/1", label="New Zealand")
top.defined_by = "POLYGON((165.74 -33.55, -179.96 -33.55, -179.96 -47.8, 165.74 -47.8, 165.74 -33.55))"
```

### Geospatial Approximation

All recorded locations are approximate to some degree. It may be desirable to capture the exact location separately from a broader area that is known, especially when that approximation is very uncertain. If the place is the exact location of several events, and a name for the place is available but not exact geospatial coordinates or a full address, then this pattern is especially valuable. This is managed using the `part_of` construction -- the specific place is somewhere within the broader area.
 
__Example:__

Many art sales take place in auction houses over time, and while the city might be known, the exact address within the city might not be and it could be misleading to collect all of the art sales within the entire city together.

```crom
top = model.Place(ident="amsterdam_auction_house/1", label="Christie's AMS")
top.identified_by = model.Name(content="Christie's Amsterdam Location")
p2 = model.Place(ident="amsterdam", label="Amsterdam")
top.part_of = p2
```


## Buildings and "Immovable" Objects

It is easy to confuse places with the constructions that exist at the place. While rare, there are situations when buildings are moved between locations. The building, just like a painting, is thus modeled as an object that has a current location in space. Activities take place in the place, rather than in the object.  The granularity of the place compared to the building may be different due to underlying data management.

This applies to any other "immovable" object as well, such as large stellae through pyramids, ruins, or any other constructed object that might otherwise be "permanently" at a particular location.


__Example:__

The [Frank Lloyd Wright House](https://crystalbridges.org/frank-lloyd-wright/) was originally built in New Jersey, and subsequently moved to its current location in Arkansas.

```crom
top = vocab.Building(ident="flw_house/1", label="Frank Lloyd Wright House")
top.identified_by = model.Name("Frank Lloyd Wright House")
top.current_location = model.Place(ident="crystal_bridges", label="Crystal Bridges")
```
