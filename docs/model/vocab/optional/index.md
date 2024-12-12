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
| Annotation         | aat:300026100 | A note or comment added to text, diagrams, or data, which can vary in length and format. |
| Article            | aat:300048715 | A nonfictional prose forming an independent part of a publication. |
| Auction Catalog    | aat:300026068 | A catalog listing items to be sold at an auction, often including descriptions and estimates. |
| Catalogue raisonné   | aat:300026061 | A comprehensive, annotated listing of all the known artworks by an artist. |
| Chapter            | aat:300311699 | A main division of a book, typically with a number or title. |
| Data               | aat:300438434 | Factual information used as a basis for reasoning, discussion, or calculation. |
| Exhibition Catalog | aat:300026096 | A publication accompanying an exhibition, detailing the works displayed. |
| Issue              | aat:300312349 | A single edition of a periodical released at a particular time. |
| Journal            | aat:300215390 | A periodical publication containing scholarly articles on a specific subject. |
| Monograph          | aat:300060417 | A detailed written study on a single specialized subject or aspect of it. |
| Patent             | aat:300027832 | An official document granting exclusive rights to an invention or process. |
| Proceedings        | aat:300027316 | A published record of a conference, including papers and discussions. |
| Text of a Page     | aat:300194222 | The written or printed words found on a single page. |
| Thesis             | aat:300028028 | A dissertation presenting original research, submitted for an academic degree. |
| Volume             | aat:300265632 | A book forming part of a work or series, often numbered. |



### Place Types

See the [place documentation](/model/place/)


| Name                | URI           | Description |
|---------------------|---------------|-------------|
| City Block          | aat:300008077 | A rectangular area in a city enclosed by streets, containing buildings. |
| Township            | aat:300000792 | A subdivision of a county with some self-government. |
| Storage place       | aat:300150151 | A location designated for storing objects or materials. |
| Ocean               | aat:300008687 | A vast body of salt water covering a major part of the Earth's surface. |
| Sea                 | aat:300008694 | A large body of salt water, smaller than an ocean, partially enclosed by land. |
| Bay                 | aat:300132316 | A broad inlet of the sea where the land curves inward. |



### Group Types

See the person and [group documentation](/model/actor/)


| Name                | URI           | Description |
|---------------------|---------------|-------------|
| Atelier (of)        | aat:300404277 | A workshop or studio of an artist, including assistants and apprentices. |
| Circle (of)         | aat:300404283 | A group of artists influenced by a particular master, often without direct contact. |
| Followers (of)      | aat:300404282 | Artists who adopt the style of a master or movement. |
| Pupils (of)         | aat:300404279 | Students under the guidance of a specific teacher or master. |
| School (of)         | aat:300404284 | Artists sharing common styles or philosophies, often linked to a location or period. |
| Studio (of)         | aat:300404275 | The workplace of an artist or professional, sometimes including collaborators. |
| Workshop (of)       | aat:300404274 | A place where an artist or craftsperson and their team produce works collectively. |



### Object Types

See the [object documentation](/model/object/) and base [classification documentation](/model/base/#types-and-classifications)


| Name                  | URI           | Description |
|-----------------------|---------------|-------------|
| Box                   | aat:300045643 | A container with a flat base and sides, typically square or rectangular. |
| Building              | aat:300004792 | A structure with walls and a roof, such as a house or factory. |
| Embroidery            | aat:300264024 | Decorative needlework stitched on fabric. |
| Enamel                | aat:300178264 | A glossy coating fused onto metal, glass, or ceramics for protection or decoration. |
| Envelope              | aat:300197601 | A flat paper container with a sealable flap, used for enclosing documents. |
| Folder                | aat:300197602 | A cover or holder for storing loose papers. |
| Implement             | aat:300024841 | A tool or instrument used in performing an action or task. |
| Lithograph            | aat:300041379 | A print made by lithography, using a flat stone or metal plate. |
| Musical Instrument    | aat:300041620 | A device created or adapted to make musical sounds. |
| Photo Album           | aat:300026695 | A book with blank pages for mounting and displaying photographs. |
| Photo Book            | aat:300265728 | A book composed primarily of photographs, often centered around a theme or artist. |
| Photographic Negative | aat:300127173 | An image with inverted colors and tones, used to produce positive photographs. |
| Sample                | aat:300028875 | A small part or quantity intended to show what the whole is like. |
| Vessel                | aat:300193015 | A hollow container, especially for holding liquids. |


### Parts of Objects Types

See the [partitioning documentation](/model/base/#parts)


| Name                | URI           | Description |
|---------------------|---------------|-------------|
| Back                | aat:300190692 | The rear part or side of an object, opposite the front. |
| Base                | aat:300001656 | The bottom support of an object; foundation. |
| Bottom              | aat:300190695 | The lowest part or point of something. |
| Front               | aat:300190703 | The foremost part or side of an object. |
| Mount               | aat:300131087 | A backing or support on which something is mounted for display or study. |
| Panel               | aat:300014657 | A flat or curved component, often rectangular, forming part of a surface. |
| Side                | aat:300190706 | A position to the left or right of an object or central point. |
| Support             | aat:300014844 | The material or structure upon which a work of art is executed. |
| Top                 | aat:300190710 | The highest or uppermost part of something. |



### Dimension Types

See the [dimensions documentation](/model/object/physical/#dimensions)

| Name       | URI           | Description |
|------------|---------------|-------------|
| Diameter   | aat:300055624 | A straight line passing through the center of a circle or sphere. |
| Length     | aat:300055645 | The measurement of something from end to end. |
| Thickness  | aat:300055646 | The distance between the two opposite surfaces of an object; depth. |


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


