---
title: Optional Vocabulary Terms
up_href: "/model/vocab/"
up_label: "Vocabulary Terms"
---

## Introduction

These terms are listed to be used in order to facilitate interoperability between datasets where possible, and make it easier to find them when doing data mappings. They are in the list because someone has found them to be useful, rather than that they are recommended for general use. If you don't have a reason to use a different term, then please use these. If you do have a reason to use a different term, that's totally okay. 

Also, if you would like to suggest additions that you think would be interesting, for example new terms that mitigate a bias resulting from the somewhat ad hoc process of compiling the lists here, please [reach out](https://linked.art/community/)!


## Types

### Name Types

See the [name documentation](/model/base/#names).

| Name                | URI           | Description |
|---------------------|---------------|-------------|
| Translated Title    | aat:300417194 | The Name is a translation of another name |
| Sub-title           | aat:300312006 | The Name is part of a larger title, and is the sub-title |
| Alias               | aat:300404664 | The Name is an alias or nickname, likely for a person |
| Pseudonym           | aat:300404657 | The Name is a pseudonym, pen-name or other adopted name |



### Identifier Types

See the [identifier documentation](/model/base/#identifiers).

| Name                | URI           | Description |
|---------------------|---------------|-------------|
| Auction Lot Number  | aat:300404628 | The identifier, typically a number, for an auction lot. The same identifier might be repeated across different auctions |
| ISBN                | aat:300417443 | An International Standard Book Number |
| ISSN                | aat:300417430 | An International Standard Serial Number (for journals) |
| DOI                 | aat:300417432 | A Digital Object Identifier |
| Stock Number        | aat:300412177 | An identifier based on the stock managed by a commercial organization |


### Contact Identifier Types

See the [contact point documentation](/model/actor/#addresses)

| Name                | URI           | Description |
|---------------------|---------------|-------------|
| Email Address       | aat:300435686 | An email address, as a string rather than a mailto: URI |
| Street Address      | aat:300386983 | A street address |
| Telephone Number    | aat:300435688 | A telephone number |
| Fax Number          | aat:300435689 | A fax number |


### Statement Types

See the [statement documentation](/model/base/#statements-about-an-entity)

| Name                   | URI           | Description |
|------------------------|---------------|-------------|
| Biography (Statement)  | aat:300435422 | A description of the life of a person|
| Condition Statement    | aat:300435425 | The physical condition of an object |
| Context Statement      | aat:300435428 | Context of any sort relevant to the resource it is associated with|
| Culture Statement      | aat:300435431 | The culture from which the object or work is drawn, or that the person or group is part of |
| Edition Statement      | aat:300435435 | The edition or number of a work or object |
| Foliation Statement    | aat:300435441 | The foliation statement of an object with folios, such as "i-ix, f1r-f256v" |
| Language Statement     | aat:300435433 | A statement declaring the language or languages of a text |
| Pagination Statement   | aat:300435440 | Similar to a foliation statement, a description of the page count for the object |
| Period Statement       | aat:300435432 | A statement about the period of time from which the object, work or other entity originates |
| Significance Statement | aat:300435427 | A statement as to the significance of the object or work |
| Valuation Statement    | aat:300435426 | A statement as to the value of the object or work |


### Document Types

See the [textual document documentation](/model/document/)

| Name               | URI           | Description |
|--------------------|---------------|-------------|
| Annotation         | aat:300026100 | |
| Article            | aat:300048715 | |
| Auction Catalog    | aat:300026068 | |
| Catalog Raisonne   | aat:300026061 | |
| Chapter            | aat:300311699 | |
| Data               | aat:300438434 | |
| Exhibition Catalog | aat:300026096 | |
| Issue              | aat:300312349 | |
| Journal            | aat:300215390 | |
| Monograph          | aat:300060417 | |
| Patent             | aat:300027832 | |
| Proceedings        | aat:300027316 | |
| Text of a Page     | aat:300194222 | |
| Thesis             | aat:300028028 | |
| Volume             | aat:300265632 | |


### Place Types

See the [place documentation](/model/place/)

| Name                | URI           | Description |
|---------------------|---------------|-------------|
| City Block          | aat:300008077 | |
| Township            | aat:300000792 | |
| Storage place       | aat:300150151 | |
| Ocean               | aat:300008687 | |
| Sea                 | aat:300008694 | |
| Bay                 | aat:300132316 | |


### Group Types

See the person and [group documentation](/model/actor/)

| Name                | URI           | Description |
|---------------------|---------------|-------------|
| Atelier (of)        | aat:300404277 | |
| Circle (of)         | aat:300404283 | |
| Followers (of)      | aat:300404282 | |
| Pupils (of)         | aat:300404279 | |
| School (of)         | aat:300404284 | |
| Studio (of)         | aat:300404275 | |
| Workshop (of)       | aat:300404274 | |



### Object Types

See the [object documentation](/model/object/) and base [classification documentation](/model/base/#types-and-classifications)

| Name                  | URI           | Description |
|-----------------------|---------------|-------------|
| Box                   | aat:300045643 | |
| Building              | aat:300004792 | |
| Embroidery            | aat:300264024 | |
| Enamel                | aat:300178264 | |
| Envelope              | aat:300197601 | |
| Folder                | aat:300197602 | |
| Implement             | aat:300024841 | |
| Lithograph            | aat:300041379 | |
| Musical Instrument    | aat:300041620 | |
| Photo Album           | aat:300026695 | |
| Photo Book            | aat:300265728 | |
| Photographic Negative | aat:300127173 | |
| Sample                | aat:300028875 | |
| Vessel                | aat:300193015 | | 

### Parts of Objects Types

See the [partitioning documentation](/model/base/#parts)

| Name                | URI           | Description |
|---------------------|---------------|-------------|
| Back                | aat:300190692 | |
| Base                | aat:300001656 | |
| Bottom              | aat:300190695 | |
| Front               | aat:300190703 | |
| Mount               | aat:300131087 | |
| Panel               | aat:300014657 | |
| Side                | aat:300190706 | |
| Support             | aat:300014844 | |
| Top                 | aat:300190710 | |


### Dimension Types

See the [dimensions documentation](/model/object/physical/#dimensions)

| Name                | URI           | Description |
|---------------------|---------------|-------------|
| Diameter            | aat:300055624 | |
| Length              | aat:300055645 | |
| Thickness           | aat:300055646 | |


<!--

## Instances

### Materials

| Name                | URI           | Description |
|---------------------|---------------|-------------|



### Occupations

| Name                | URI           | Description |
|---------------------|---------------|-------------|


### Nationalities

| Name                | URI           | Description |
|---------------------|---------------|-------------|

### Genders

| Name                | URI           | Description |
|---------------------|---------------|-------------|

### Languages

| Name                | URI           | Description |
|---------------------|---------------|-------------|

### Currencies

| Name                | URI           | Description |
|---------------------|---------------|-------------|

### Measurement Units

| Name                | URI           | Description |
|---------------------|---------------|-------------|

-->


