---
title: Linked Art Cook Book
---

## Introduction

In order to provide examples of how to apply the [data model](/model/), this section is a community contributed cookbook of recipes for putting the different ingredients together to produce the desired results.  Each contributing organization has their own section, in which they can provide as many different recipes as they have time for.  The recipes are checked on submission for appropriateness and correctness.

## Recipes
<!-- 
  Build from folder structure /cookbook/{organization}/{recipe}/
  Each folder must have a meta.yaml with a title property
-->

{# RPP - commented out as resource not avail in mkdocs 
{% for folder in resource.node.child_nodes %}
  * {{ folder.meta.title }}
  {% for recipe in folder.child_nodes %}
    * [{{ recipe.meta.title }}]({{ recipe.full_url }}/)
  {% endfor %}
{% endfor %}
#}

