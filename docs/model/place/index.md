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

There is a city called Los Angeles, in California.

```crom
top = vocab.City(label="Los Angeles, CA")
top.identified_by = Name(content="Los Angeles")
top.referred_to_by = vocab.Description(content="Los Angeles is a city in California, USA.")
top.part_of = vocab.Province(label="California")
```


## Geospatial Location

One of the expected user interface requirements for places is the ability to plot them on a map.  In order to do this, or to calculate the geospatial overlap of places, it is useful to have a geometry that describes the place's boundaries in the real world. This could be very detailed, a simple bounding box within which the place fits, or a point close to the center of the area.

This is handled simply by associating a [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) string with the place using the `defined_by` property. A simple user interface for generating WKT representations is available from the [Wicket Project](https://arthur-e.github.io/Wicket/sandbox-gmaps3.html).


__Example:__

A polygon that (approximately) defines the country New Zealand.

```crom
top = vocab.Nation(label="New Zealand")
top.defined_by = "POLYGON((165.74 -33.55, -179.96 -33.55, -179.96 -47.8, 165.74 -47.8, 165.74 -33.55))"
```

### Geospatial Approximation

All recorded locations are approximate to some degree. It may be desirable to capture this approximation separately from the actual place, especially when that approximation is very uncertain. Especially if the place is the exact location of several events, and perhaps an address or other information is known, but not the exact geospatial coordinates.  

Secondly, as a place is defined by exactly one definition, but there might be multiple approximations such as a polygon as well as the central point, the real place that an activity occured at can be related to multiple approximate places to capture these different approximations.


__Example:__

Many art sales take place in auction houses over time, and while the city might be known, the exact address within the city might not be and it would be wrong to collect all of the art sales within the entire city together.

```crom
top = model.Place(label="True Auction House Location")
p2 = model.Place(label="Auction House Location Approximation")
p2.defined_by = "POINT(-0.0032937526703165 51.515107154846)"
top.approximated_by = p2
```


## Buildings and "Immovable" Objects

It is easy to confuse places with the constructions that exist at the place. While rare, there are situations when buildings are moved between locations. The building, just like a painting, is thus modeled as an object that has a current location in space. Activities take place in the place, rather than in the object.  The granularity of the place compared to the building may be different due to underlying data management.

This applies to any other "immovable" object as well, such as large stellae through pyramids, ruins, or any other constructed object that might otherwise be "permanently" at a particular location.


__Example:__

The [Frank Lloyd Wright House](https://crystalbridges.org/frank-lloyd-wright/) was originally built in New Jersey, and subsequently moved to its current location in Arkansas.

```crom
top = vocab.Building(label="Frank Lloyd Wright House")
top.current_location = Place(label="Current Location in Arkansas at Crystal Bridges");
```
