---
title: "HAL Link: workLanguageLanguage"
---

## workLanguageLanguage

Return the works that are written or in the language.

See the related [model documentation](/model/document/#core-features)

### Example

From the record for English, the record for the Lord of the Rings would be in the response


### Details

* Class Given: Language
* Returns Class: LinguisticObject
* Relationship: language


### SPARQL

```sparql
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT DISTINCT ?work
WHERE {
  {
    ?work crm:P72_has_language $language .
  } UNION {
    $current crm:P72i_is_language_of ?work .
  }
  ?work a crm:E33_Linguistic_Object .
  FILTER(isIRI(?work))
}
```
