---
title: Linked Art Profile of CIDOC-CRM
---

## Introduction

With dozens of classes and hundreds of relationships, most of which are unnecessary, the CIDOC-CRM is a complex ontology. The linked.art profile aims to pare that back to its excellent core that can be used to build practical and interoperable solutions to real world problems.  Combined with the easy-to-use JSON-LD serialization, this profile is a functional and robust baseline to cover 90% of the use cases of 90% of the organizations, with only 10% of the complexity of the full CRM ontology with all of its approved extensions.

The core mission of the profile:

  * We are defining patterns and models that enable cultural heritage and memory institutions to easily publish their data for both event-based digital research projects and for use by non-domain-specific developers.
  * We use both shared models and shared software to accomplish our goal of reducing the complexity for publishers and consumers, while enabling researchers to access the full richness of the data.

It bears repeating that the profile's design is done...

  * iteratively (we will not get it right the first time)
  * responsively (we will change the model in response to feedback and concerns)
  * responsibly (we will consider changes and features carefully with respect to complexity and value)
  * collaboratively (we will engage with the community, projects and individuals early and often)

... including the following design principles.

## Design Principles

The creation and management of the profile is guided by these design principles, informed by those of the very successful [IIIF](http://iiif.io/api/annex/notes/design_patterns/) community, and the experiences of the [American Art Collaborative](http://review.americanartcollaborative.org/) and the [Pharos Consortium](http://pharosartresearch.org/).

### Scope Through Shared Use Cases and Real World Data

The specifications are shaped by shared, documented, and well-understood use cases. Shared understanding promotes interoperability, and the specifications are more likely to be implemented if the results solve real, not speculative, problems. Assessment of use cases is a key factor in the process of determining which features should be included or prioritized. Use cases where data exists in real systems are prioritized over ones where the data could exist.

The intent of adopting this pattern is to keep the resulting specifications practical and to solve real problems.  Implementers will invest time in solutions that solve their problems, and not speculative or abstract ones.  If the use case is shared by multiple organizations, then there is a need for interoperability. 

Implications:

  * If there isn't a concrete use case with real world data, then there is no need for the class or property. 
  * Engagement with the community is essential to collect, understand and analyze use cases.


### Select Solutions That Are as Simple as Possible and No Simpler

The specifications should be designed to reduce the complexity to the lowest possible point at which the use cases that feed them can be met.  They should make simple things easy and complex things possible.  They should allow implementers to build up from a minimum viable product in stages and incrementally enable more complex use cases. The human cost of understanding a system with hundreds of classes and relationships is extremely high, and increases the likelihood that different approaches will be taken, thereby reducing interoperability.

The intent of adopting this pattern is to ensure the adoption of the specifications is as high as possible. Simplicity is often a trade-off between parties, and must take into account the generation and publishing of the data on the server side, and the consumption and processing of the data on the client side.

Implications:

  * Classes or properties that do not provide a functional and concrete advantage are unnecessary.
  * Reuse of existing classes/properties is greatly preferred to new ones - the cost of adding new features is high.
  * Extensions, the definition of new classes and properties, beyond the core CRM ontology are to be avoided if possible without an exceptional reason. This includes existing CRM extensions and new ones.
  * Multiple Instantiation (an instance with multiple classes) is to be avoided as more complex to implement than Multiple Inheritance (a class with multiple parents). This leads to a very small number of new classes being defined where absolutely necessary.

### Intelligently Manage Addition of Complexity

The specifications should encourage easy implementations that publish data according to the core model. They should not require costly or complicated libraries or tooling to get started, nor computationally expensive runtime processing. A useful implementation should require only a way to host files that are accessible via a web server.

The intent of adopting this pattern is to support simple and quick implementations as a way to encourage adoption, and ensure the on-ramp is as quick and painless as possible.

Implications:

  * "Expansions" are an important pattern, where the primary, basic information uses a simple pattern, and more complex data does not interfere with that but instead expands upon it. For example, the Production is `carried_out_by` the Artist in all cases, whereas previous attributions expand upon this by using `AttributeAssignment` to assert them, rather than also requiring `AttributeAssignment` for the current attribution.  In the future the current Artist might be relegated to the previous attribution pattern and replaced.  For systems that only care about the current belief, the simple pattern is easy to use. For those that want more information, it is also available.
  * The importance of reuse of common patterns is reinforced, as additional complexity that seems familiar is better than a completely new pattern.


### Avoid Dependency on Specific Technologies

The specifications should avoid placing undue value on one technology or format over another, unless there is a clear benefit and the choice does not pose a significant barrier to entry.  While the specifications must make choices for the sake of interoperability, these choices must be weighed as to how closely tied they are to specific products or formats. 

The intent of adopting this pattern is to ensure that the specifications can be implemented in a variety of languages and styles.  It results from the combination of the previous two patterns.

Implications:

  * Consumption and analysis using specific graph-based technologies such as SPARQL is an important, but secondary, consideration to the design.  

### Follow Linked Data Principles and Best Practices

The specifications conform to [Linked Data](https://en.wikipedia.org/wiki/Linked_data), relevant [web architecture](web architecture) standards and best practices for [JSON-LD](http://json-ld.org/spec/latest/json-ld-api-best-practices/), [LOD](https://www.w3.org/TR/ld-bp/) and [Data on the Web](https://www.w3.org/TR/dwbp/), as defined by the W3C and IETF. From the previous point, they should not require an RDF based development stack to implement, but it must be possible to implement using one.  It should be possible to transform representations back and forth between triples and the [JSON-LD](/model/jsonld/) serialization without loss, but not necessarily without the use of custom code.

The intent of adopting this pattern is to ensure that the data published can be part of the Web, not just on the Web. The design of the specifications should be informed by existing and ongoing work, but evaluated as to the appropriateness of the application to the art domain.

Implications:

  * Features of CIDOC-CRM that conflict with core Linked Data principles are to be avoided, such as .1 properties on properties, and defining data types as classes.


### Design for JSON-LD First

The specifications are designed for JSON-LD as the primary serialization. This is comprised of publishing and maintaining a JSON-LD context document, and providing JSON-LD Frames. Further design principles for JSON-LD are [documented with the context](/model/jsonld/#context-design).

The intent of adopting this pattern is to ensure that the representation of the Linked Data is as easy to use as possible without the need for a full RDF development suite.  Developers must be able to treat the representation as plain JSON, with a predictable structure.  This ease of understanding increases the likelihood of wide spread adoption.

Implications:

  * The terms used in JSON-LD and the ontology are often radically different. 
  * The use of rdf:List for managing order is endorsed, though complicated by requiring extensions

### Define Success, Not Failure

The specifications define the functionality that can be expected to work and how to request it, and do not limit the interpretation of requests that are beyond the scope or current definition of the specification.  Any pattern outside of those defined is able to be used by implementers, keeping in mind that future official extensions might make it inconsistent.  

The intent of adopting this pattern is to enable experimentation by implementers, thereby encouraging the early adoption and validation of new (minor) versions.

Implications:

  * There are no errors beyond those defined by the underlying specifications, only unsupported patterns. 


## Analysis

Some (iterative, ongoing) analysis of the CIDOC-CRM ontology that both contributes to and is derived from the work on the profile:

* [Class Analysis](class_analysis.html)
* Relationship Analysis to come.


## Additional Terms

The analysis performed above, in conjunction with the use cases and data for what is required, result in the creation of some additional ontological modeling.

* [Linked Art Ontology](ontologies/linkedart.xml) of additional terms
* [Other Ontologies](ontologies/linkedart_crm_enhancements.xml) mapped into the CRM universe

And for completeness, the base CIDOC-CRM ontology used plus property inverses:

* [CIDOC-CRM 6.2.7](ontologies/cidoc.xml)
