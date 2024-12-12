---
title: "Indianapolis Museum of Art (IMA) Collection Mapping"
---



## Introduction

An example mapping of IMA Collection Metadata to Linked.Art

## Datasource

[https://github.com/IMAmuseum/ima-collection](https://github.com/IMAmuseum/ima-collection)

A collection of JSON files, each representing a single work of art.

## Sample Record 

Data file 
<https://github.com/IMAmuseum/ima-collection/blob/master/json/objects/0038000/0038020.json>

[Local copy of data file](turner.json) 

Collection Record 
<http://collection.imamuseum.org/artwork/65338/>

Google Street view of the location
<https://goo.gl/maps/UFpRnKGEbbTxqFEQ6>

Google Street view map of the location
<iframe src="https://www.google.com/maps/embed?pb=!4v1632740826449!6m8!1m7!1sBg_zt3s8vqCMxzfKmFB90g!2m2!1d51.75387499815886!2d-1.256444565026974!3f141.21006648184127!4f1.9911108742760746!5f0.7820865974627469" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>


```json
{
    "accession_number": "80.825.86", 
    "| Actor	 	|s": [
        {
            "ULAN": {
                "Name": "Joseph Mallord William Turner", 
                "UlanIdNo": "500026846"
            }, 
            "after_follower": null, 
            "birth_date": "1775", 
            "collaboration": null, 
            "death_date": "1851", 
            "display_name": "Joseph Mallord William Turner", 
            "first": "Joseph", 
            "fullname": "Joseph M. Turner", 
            "irn": 626263, 
            "last": "Turner", 
            "middle": "Mallord William", 
            "nationality": null, 
            "organization": null, 
            "party_type": "Ulan", 
            "role": "Artist"
        }, 
        {
            "ULAN": {
                "Name": "Basire, James II", 
                "UlanIdNo": null
            }, 
            "after_follower": null, 
            "birth_date": "1769", 
            "collaboration": null, 
            "death_date": "1822", 
            "display_name": "Basire, James II", 
            "first": null, 
            "fullname": "Basire, James II", 
            "irn": 1790, 
            "last": "Basire, James II", 
            "middle": null, 
            "nationality": null, 
            "organization": null, 
            "party_type": "ULAN", 
            "role": "Engraver"
        }
    ], 
    "creation_date": "1806", 
    "credit_line": "Bequest of Kurt F. Pantzer", 
    "cultures": [], 
    "dimensions": null, 
    "dynasty": null, 
    "images": [], 
    "irn": 38020, 
    "materials": "engraving", 
    "on_view": false, 
    "period": null, 
    "printers": [], 
    "publishers": [], 
    "rights": null, 
    "title": "View of Exeter College from the Turl"
}
```


## Data Dictionary

* Load JSON data file into [Open Refine](https://openrefine.org/) to review fields in tabulated format
* Prepare data dictionary, if one is not available, with description for each field

|  Entity    |  Field name          |  Description                   | 
| :---      | :---------------      | :-------------                |
|  Artwork	| irn	                | Artwork IMA id                   |
|  Artwork	| title	                | Artwork title |
|  Artwork	| period	            | Artwork period|
|  Artwork	| rights	            | Artwork rights|
|  Artwork	| dynasty	            | Artwork dynasty|
|  Artwork	| on_view	            | Artwork - is it on view?|
|  Artwork	| materials	            | Artwork - materials used|
|  Artwork	| dimensions	        | Artwork - dimensions|
|  Artwork	| credit_line	        | Credit line|
|  Artwork	| creation_date	        | Artwork creation date|
|  Artwork	| accession_number	    | Artwork IMA accession number|
| Actor	    |	 irn	            | IMA ID |
| Actor	 	|	last	            | last name|
| Actor	 	|	role	            | Role in relation to the Artwork   |
| Actor	 	|	first	            | first name|
| Actor	 	|	middle	            | middle name|
| Actor	 	|	fullname	        | full name|
| Actor	 	|	birth_date	        | birth date|
| Actor	 	|	death_date	        | death date|
| Actor	 	|	party_type	||
| Actor	 	|	nationality	        | nationality|
| Actor	 	|	display_name	    | display name|
| Actor	 	|	organization	    | organization|
| Actor	 	|	collaboration       | 	|
| Actor	 	|	after_follower      | 	|
| Actor	 	|	ULAN - Name	        | ULAN name|
| Actor	 	|	UlanIdNo	        | ULAN Identifier|


## IMA Model 

The model for the artwork is divided into two main parts:
* the description of the artwork
* description of actors and their role in relation to the artwork

### The Artwork
```json
{
    "accession_number": "80.825.86", 
    "creation_date": "1806", 
    "credit_line": "Bequest of Kurt F. Pantzer", 
    "cultures": [], 
    "dimensions": null, 
    "dynasty": null, 
    "images": [], 
    "irn": 38020, 
    "materials": "engraving", 
    "on_view": false, 
    "period": null, 
    "printers": [], 
    "publishers": [], 
    "rights": null, 
    "title": "View of Exeter College from the Turl"
}
```

The artwork is described as an instance of an engraving.

The minimum JSON-LD representation for the engraving is as follows: 

```json
{
    "@context": "https://linked.art/ns/v1/linked-art.json", 
    "id": "http://imamuseum.org/mercury/load-artwork/38020", 
    "type": "HumanMadeObject", 
    "_label": "View of Exeter College from the Turl"
}

```

The `_label` is a human readable label, intended for developers and other people reading the data. The value has been taken from the record's `title` field.

The `materials` field has the value 'engraving' that we can use to classify the artwork as being a type of engraving. Using the recommended[Getty's Art and Architecture Thesaurus (AAT)](https://www.getty.edu/research/tools/vocabularies/aat/), the term `engraving` is matched with a term in the AAT that describes engravings that are a type of prints, with an identifier <http://vocab.getty.edu/page/aat/300041340>. 

The type of the object (an instance of the class HumanMadeObject) is an engraving [http://vocab.getty.edu/page/aat/300041340](aat:300033618), and an artwork [http://vocab.getty.edu/aat/300133025](aat:300133025), represented in JSON-LD as:

```json
{
  "@context": "https://linked.art/ns/v1/linked-art.json", 
    "id": "http://imamuseum.org/mercury/load-artwork/38020", 
    "type": "HumanMadeObject", 
    "_label": "View of Exeter College from the Turl"
  "classified_as": [
    {
      "id": "http://vocab.getty.edu/page/aat/300041340",
      "type": "Type",
      "_label": "Engraving"
    },
    {
      "id": "http://vocab.getty.edu/aat/300133025",
      "type": "Type",
      "_label": "Work of Art"
    }
  ]
}
```

Refer to <https://linked.art/model/base/> for further information.

The Linked Art model supports classification of types of types, e.g. classification of an engraving as being a type of work:

```json
{
  "@context": "https://linked.art/ns/v1/linked-art.json", 
    "id": "http://imamuseum.org/mercury/load-artwork/38020", 
    "type": "HumanMadeObject", 
    "_label": "View of Exeter College from the Turl"
  "classified_as": [
    {
      "id": "http://vocab.getty.edu/page/aat/300041340",
      "type": "Type",
      "_label": "Engraving",
      "classified_as": [
        {
          "id": "http://vocab.getty.edu/aat/300435443",
          "type": "Type",
          "_label": "Type of Work"
        }
      ]
    },
    {
      "id": "http://vocab.getty.edu/aat/300133025",
      "type": "Type",
      "_label": "Work of Art"
    }
  ]
}

```


#### Names 

The Linked Art model recommends every resource should be rendered with at least one specific name. In this example, the title value will be used for the name of the artwork.

```json
{
  "@context": "https://linked.art/ns/v1/linked-art.json", 
    "id": "http://imamuseum.org/mercury/load-artwork/38020", 
    "type": "HumanMadeObject", 
    "_label": "View of Exeter College from the Turl"
  

"identified_by": [
    {
      "type": "Name",
      "classified_as": [
        {
          "id": "http://vocab.getty.edu/aat/300404670",
          "type": "Type",
          "_label": "Primary Name"
        }
      ],
      "content": "View of Exeter College from the Turl",
      "language": [
        {
          "id": "http://vocab.getty.edu/aat/300388277",
          "type": "Language",
          "_label": "English"
        }
      ]
    }
  ]
}
```

### Identifiers
The engraving has identifiers associated with it:
* accession_number - a unique number assigned by IMA as a means of identifying the artwork
* irn - IMA local identifier

```json

 "@context": "https://linked.art/ns/v1/linked-art.json", 
    "id": "http://imamuseum.org/mercury/load-artwork/38020", 
    "type": "HumanMadeObject", 
    "_label": "View of Exeter College from the Turl"
  

"identified_by": [
    {
      "type": "Identifier",
      "classified_as": [
        {
          "id": "http://vocab.getty.edu/aat/300312355",
          "type": "Type",
          "_label": "IMA Accession Number"
        }
      ],
      "content": "80.825.86"
    },
    38020
    {
      "type": "Identifier",
      "classified_as": [
        {
          "id": "http://vocab.getty.edu/aat/300312355",
          "type": "Type",
          "_label": "IMA irn"
        }
      ],
      "content": "38020"
    }
  ]
}


```


### Statements about the Artwork

Where human-readable strings are provided in the metadata that cannot be linked to specific ontology terms, they are modelled as a `LinguisticObject` in Linked Art. The `credit_line` field is an example of a human-readable strings in the IMA record:
* credit_line

```json

```json

 {
"@context": "https://linked.art/ns/v1/linked-art.json", 
"id": "http://imamuseum.org/mercury/load-artwork/38020", 
"type": "HumanMadeObject", 
"_label": "View of Exeter College from the Turl",

"referred_to_by": [
{
  "type": "LinguisticObject",
  "classified_as": [
    {
      "id": "http://vocab.getty.edu/aat/300435429",
      "type": "Type",
      "_label": "Material Statement",
      "classified_as": [
        {
          "id": "http://vocab.getty.edu/page/aat/300435418",
          "type": "Type",
          "_label": "Credit line"
        }
      ]
    }
  ],
  "content": "Kurt F. Panzer",
  "language": [
    {
      "id": "http://vocab.getty.edu/aat/300388277",
      "type": "Language",
      "_label": "English"
    }
  ]
}
]
}


```

### Production of the Artwork

The creation_date field refers to a creation event, that can be modelled as a Production activity <https://linked.art/model/object/production>.

The date is represented using two properties, `begin_of_the_begin` and `end_of_the_end`. As only the year is provided, the begin date is represented as 00:00:00 1 Jan 1806, and the end date is 23:59:59 31 Dec 1806.

```json
{
"@context": "https://linked.art/ns/v1/linked-art.json", 
"id": "http://imamuseum.org/mercury/load-artwork/38020", 
"type": "HumanMadeObject", 
"_label": "View of Exeter College from the Turl",
    "created_by": {
        "type": "Production",
        "timespan": {
          "type": "TimeSpan", 
          "begin_of_the_begin": "1806-01-01T00:00:00Z", 
          "end_of_the_end": "1806-12-31T23:59:59Z"
        },
        "carried_out_by": [
            {
                "id": "http://vocab.getty.edu/ulan/500026846",
                "type": "Person",
                "_label": "Joseph Mallord William Turner"
            }
        ]
    }

}

```



### Depiction 

<https://linked.art/model/object/aboutness/#depiction>

The engraving shows a place, identified in the `title` field as 'View of Exeter College from the Turl', that can be described according to a Linked Art model [depiction](https://linked.art/model/object/aboutness/#depiction). With additional information, this location can be identified as being located in Oxford. 

```json

{
    "@context": "https://linked.art/ns/v1/linked-art.json", 
    "id": "http://imamuseum.org/mercury/load-artwork/38020", 
    "type": "HumanMadeObject", 
    "_label": "View of Exeter College from the Turl",

    "shows": [
    {
      "type": "VisualItem",
      "represents": [
        {
        "id": "http://vocab.getty.edu/page/tgn/7011931",
        "type": "Place",
        "_label": "Oxford",
        "classified_as": [
            {
            "id": "http://vocab.getty.edu/aat/300008389",
            "type": "Type",
            "_label": "City"
            }
        ],
        "identified_by": [
            {
            "type": "Name",
            "content": "Oxford"
            }
        ],
        }
      ]
    }
  ]

}


```

The mapping approach is:
* The engraving is an object
* The `irn` and `accession_number` values are [identifiers](https://linked.art/model/base/#identifiers) with collection-specific contexts
* The `credit_line` indicates a bequest activity involving the engraving and a person whose name is "Kurt F. Panzer"
* The `creation_date` provides the year that the engraving was [created](https://linked.art/model/object/production/#base-production-activity)
* The `title` provides the [title or name](https://linked.art/model/base/#names) for the engraving
* The engraving shows a place, identified in the `title`field as Exeter College, that can be described according to a Linked Art model [depiction](https://linked.art/model/object/aboutness/#depiction) 
* The `credit_line` information is a note associated with the object, modelled in the same way as other descriptive texts.
* The `materials` and `dimension` fields describe the [physical characteristics](https://linked.art/model/object/physical/) of the artwork
* The `rights` field provides [rights information](https://linked.art/model/object/rights/) about the artwork
* The `printers` and `publishers` fields indicate that some records contain details of printers and publishers that are associated with artworks. This example, does not contain that information, however.
* The `on_view` field refers to whether the artwork is currently on display, and is out of scope for the Linked Art data model
* The engraving has`period`, `dynasty` and `cultures` properties, although these are not populated in the example record

### Actors in relation to Artwork


```json
{
    "| Actor	 	|s": [
        {
            "ULAN": {
                "Name": "Joseph Mallord William Turner", 
                "UlanIdNo": "500026846"
            }, 
            "after_follower": null, 
            "birth_date": "1775", 
            "collaboration": null, 
            "death_date": "1851", 
            "display_name": "Joseph Mallord William Turner", 
            "first": "Joseph", 
            "fullname": "Joseph M. Turner", 
            "irn": 626263, 
            "last": "Turner", 
            "middle": "Mallord William", 
            "nationality": null, 
            "organization": null, 
            "party_type": "Ulan", 
            "role": "Artist"
        }, 
        {
            "ULAN": {
                "Name": "Basire, James II", 
                "UlanIdNo": null
            }, 
            "after_follower": null, 
            "birth_date": "1769", 
            "collaboration": null, 
            "death_date": "1822", 
            "display_name": "Basire, James II", 
            "first": null, 
            "fullname": "Basire, James II", 
            "irn": 1790, 
            "last": "Basire, James II", 
            "middle": null, 
            "nationality": null, 
            "organization": null, 
            "party_type": "ULAN", 
            "role": "Engraver"
        }
    ]
}
```


The mapping approach is:
* `UlanIdNo` ULAN name authority id for actor
* `Name`  ULAN name authority text label for actor
* `after_follower`
* `birth_date` and `death_date` birth and death dates for person
* `full_name`, `display_name`, `first`, `last` and `middle` represent name of person
* `nationality` person's nationality 
* `organization` - name of actor if an organisation instead of a person?
* `party_type`
* `role` - role of person/organisation in relation to the artwork



