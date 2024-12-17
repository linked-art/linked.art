---
title: "Linked Art Schema: Person"
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---



     <h1>Person</h1><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">_crm:E21\_Person_
A human.
See: [API](https://linked.art/api/1.0/endpoint/person/) | [Model](https://linked.art/model/actor/)</span> <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordion@context">
    <div class="card">
        <div class="card-header" id="heading@context">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#@context"
                        aria-expanded="" aria-controls="@context" onclick="setAnchor('#@context')"><span class="property-name">@context</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="@context"
             class="collapse property-definition-div" aria-labelledby="heading@context"
             data-parent="#accordion@context">
            <div class="card-body pl-5">

    <h4>JSON-LD Context</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Either an array of contexts, or a string containing the Linked Art context URI</span>

    <div class="any-of-value" id="@context_anyOf"><h2 class="handle">
  <label>Any of</label>
</h2><ul class="nav nav-tabs" id="tabs@context_anyOf_anyOf" role="tablist"><li class="nav-item">
            <a class="nav-link active anyOf-option"
               id="@context_anyOf_i0" data-toggle="tab" href="#tab-pane_@context_anyOf_i0" role="tab"
               onclick="setAnchor('#@context_anyOf_i0')"
            >Linked Art</a>
        </li><li class="nav-item">
            <a class="nav-link anyOf-option"
               id="@context_anyOf_i1" data-toggle="tab" href="#tab-pane_@context_anyOf_i1" role="tab"
               onclick="setAnchor('#@context_anyOf_i1')"
            >Linked Art with Extensions</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_@context_anyOf_i0" role="tabpanel">
            

    <h4>Linked Art</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="@context_anyOf_i0_const">Specific value: <code>"https://linked.art/ns/v1/linked-art.json"</code></span>
        

        
        

        
        </div><div class="tab-pane fade card-body "
             id="tab-pane_@context_anyOf_i1" role="tabpanel">
            

    <h4>Linked Art with Extensions</h4><span class="badge badge-dark value-type">Type: array</span><br/>

        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Tuple Validation</h4>
    
    <h5>Item at 1 must be:</h5>
    <div class="card">
        <div class="card-body items-definition" id="@context_anyOf_i1_items_i0">
            

    <span class="badge badge-dark value-type">Type: string</span><span class="badge badge-info value-type">Format: uri</span><br/>

        

        
        

        
        </div>
    </div>
    
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionid">
    <div class="card">
        <div class="card-header" id="headingid">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#id"
                        aria-expanded="" aria-controls="id" onclick="setAnchor('#id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="id"
             class="collapse property-definition-div" aria-labelledby="headingid"
             data-parent="#accordionid">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span>

    
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiontype">
    <div class="card">
        <div class="card-header" id="headingtype">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#type"
                        aria-expanded="" aria-controls="type" onclick="setAnchor('#type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="type"
             class="collapse property-definition-div" aria-labelledby="headingtype"
             data-parent="#accordiontype">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabstype_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="type_allOf_i0" data-toggle="tab" href="#tab-pane_type_allOf_i0" role="tab"
               onclick="setAnchor('#type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="type_allOf_i1" data-toggle="tab" href="#tab-pane_type_allOf_i1" role="tab"
               onclick="setAnchor('#type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="type_allOf_i1_const">Specific value: <code>"Person"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionlabel">
    <div class="card">
        <div class="card-header" id="headinglabel">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#label"
                        aria-expanded="" aria-controls="label" onclick="setAnchor('#label')"><span class="property-name">_label</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="label"
             class="collapse property-definition-div" aria-labelledby="headinglabel"
             data-parent="#accordionlabel">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="label_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Georgia O&#39;Keeffe&quot;</span>
</pre></div>
</div><div id="label_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Blue by Georgia O&#39;Keeffe&quot;</span>
</pre></div>
</div><div id="label_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;New Haven, CT&quot;</span>
</pre></div>
</div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by"
                        aria-expanded="" aria-controls="identified_by" onclick="setAnchor('#identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="identified_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by"
             data-parent="#accordionidentified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items">
            

    <span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A Name or an Identifier</span>

    <div class="any-of-value" id="identified_by_items_anyOf"><h2 class="handle">
  <label>Any of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_anyOf" role="tablist"><li class="nav-item">
            <a class="nav-link active anyOf-option"
               id="identified_by_items_anyOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0')"
            >crm:E33_E41_Linguistic_Appellation</a>
        </li><li class="nav-item">
            <a class="nav-link anyOf-option"
               id="identified_by_items_anyOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1')"
            >crm:E42_Identifier</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i0" role="tabpanel">
            

    <h4>crm:E33_E41_Linguistic_Appellation</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A name of an entity
See: [API](https://linked.art/api/1.0/shared/name/) | [Model](https://linked.art/model/base/#names)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="identified_by_items_anyOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">    </span><span class="s2">&quot;type&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;Name&quot;</span><span class="p">,</span>
<span class="w">    </span><span class="s2">&quot;content&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;Georgia O&#39;Keeffe&quot;</span>
<span class="p">}</span>
</pre></div>
</div><button class="btn btn-light example-show collapsed" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_ex2" aria-controls="identified_by_items_anyOf_i0_ex2"></button><div id="identified_by_items_anyOf_i0_ex2" class="collapse jumbotron examples"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">    </span><span class="s2">&quot;type&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;Name&quot;</span><span class="p">,</span>
<span class="w">    </span><span class="s2">&quot;content&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;Blue&quot;</span><span class="p">,</span>
<span class="w">    </span><span class="s2">&quot;classified_as&quot;</span><span class="o">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="s2">&quot;id&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;http://vocab.getty.edu/aat/300404670&quot;</span><span class="p">,</span>
<span class="w">            </span><span class="s2">&quot;type&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;Type&quot;</span><span class="p">,</span>
<span class="w">            </span><span class="s2">&quot;_label&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;Primary Name&quot;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">],</span>
<span class="w">    </span><span class="s2">&quot;language&quot;</span><span class="o">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">            </span><span class="s2">&quot;id&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;http://vocab.getty.edu/aat/300388277&quot;</span><span class="p">,</span>
<span class="w">            </span><span class="s2">&quot;type&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;Language&quot;</span><span class="p">,</span>
<span class="w">            </span><span class="s2">&quot;_label&quot;</span><span class="o">:</span><span class="w"> </span><span class="s2">&quot;English&quot;</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">]</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0__label" onclick="setAnchor('#identified_by_items_anyOf_i0__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0__label"
             data-parent="#accordionidentified_by_items_anyOf_i0__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_type" onclick="setAnchor('#identified_by_items_anyOf_i0_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_type"
             data-parent="#accordionidentified_by_items_anyOf_i0_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i0_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i0_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i0_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i0_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i0_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i0_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i0_type_allOf_i1_const">Specific value: <code>"Name"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_identified_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_identified_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_identified_by" onclick="setAnchor('#identified_by_items_anyOf_i0_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_identified_by"
             data-parent="#accordionidentified_by_items_anyOf_i0_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i0_referred_to_by_items">
            

    <h4>crm:E33_Linguistic_Object</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An embedded, relatively short piece of textual content
See: [API](https://linked.art/api/1.0/shared/statement/) | [Model](https://linked.art/model/base/#statements-about-a-resource)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items__label" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items__label"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_type" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_type"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i0_referred_to_by_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i0_referred_to_by_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i0_referred_to_by_items_type_allOf_i1_const">Specific value: <code>"LinguisticObject"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_identified_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_identified_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_identified_by" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_identified_by"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_referred_to_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_referred_to_by" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_referred_to_by"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items">
            

    <h4>crm:E55_Type</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A concept or 'Type' in the taxonomic sense
See: [API](https://linked.art/api/1.0/shared/type/) | [Model](https://linked.art/model/base/#types-and-classifications)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_id" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_id"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items__label" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items__label"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_type_allOf_i1_const">Specific value: <code>"Type"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_identified_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_identified_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_identified_by" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_identified_by"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_classified_as">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_classified_as"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_classified_as" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_classified_as"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items">
            

    <h4>*</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to another primary entity
See: [API](https://linked.art/api/1.0/shared/reference/) | [Model]()</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1')"
            >Requirement 2</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1" role="tabpanel">
            

    <span class="badge badge-dark value-type">Type: enum (of string)</span><br/>
<div class="enum-value" id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1_enum">
            <h4>Must be one of:</h4>
            <ul class="list-group"><li class="list-group-item enum-item">"HumanMadeObject"</li><li class="list-group-item enum-item">"Person"</li><li class="list-group-item enum-item">"Group"</li><li class="list-group-item enum-item">"VisualItem"</li><li class="list-group-item enum-item">"LinguisticObject"</li><li class="list-group-item enum-item">"Set"</li><li class="list-group-item enum-item">"Place"</li><li class="list-group-item enum-item">"DigitalObject"</li><li class="list-group-item enum-item">"Type"</li><li class="list-group-item enum-item">"Event"</li><li class="list-group-item enum-item">"Activity"</li><li class="list-group-item enum-item">"Period"</li><li class="list-group-item enum-item">"Language"</li><li class="list-group-item enum-item">"Material"</li><li class="list-group-item enum-item">"Currency"</li><li class="list-group-item enum-item">"MeasurementUnit"</li><li class="list-group-item enum-item">"PropositionalObject"</li></ul>
            </div>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_content">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_content">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_content"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_content" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_content')"><span class="property-name">content</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_content"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_content"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_content">
            <div class="card-body pl-5">

    <h4>crm:P190_has_symbolic_content</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The string representation of a `Name`, `Identifier`, `Statement` or other text</span>

    
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_language">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_language">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_language"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_language" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_language')"><span class="property-name">language</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_language"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_language"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_language">
            <div class="card-body pl-5">

    <h4>crm:P72_has_language</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more `Language` entities in which the `content` of this text is written</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i0_referred_to_by_items_language_items">
            

    <h4>crm:E56_Language</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Language`</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_language_items_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_language_items_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_language_items_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_language_items_id" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_language_items_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_language_items_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_language_items_id"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_language_items_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_language_items_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_language_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_language_items_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_language_items_type" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_language_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_language_items_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_language_items_type"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_language_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_i1')"
            >Requirement 2</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_i1" role="tabpanel">
            

    <span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i0_referred_to_by_items_language_items_type_allOf_i1_const">Specific value: <code>"Language"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_language_items__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_language_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_language_items__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_language_items__label" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_language_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_language_items__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_language_items__label"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_language_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_language_items_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_language_items_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_language_items_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_language_items_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_language_items_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_language_items_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_language_items_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_language_items_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_format">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_format">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_format"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_format" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_format')"><span class="property-name">format</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_format"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_format"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_format">
            <div class="card-body pl-5">

    <h4>dc:format</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The media type of the content of the embedded text, e.g. text/plain</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="identified_by_items_anyOf_i0_referred_to_by_items_format_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;text/html&quot;</span>
</pre></div>
</div><div id="identified_by_items_anyOf_i0_referred_to_by_items_format_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;image/jpeg&quot;</span>
</pre></div>
</div>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_classified_as">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_classified_as"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_classified_as" onclick="setAnchor('#identified_by_items_anyOf_i0_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_classified_as"
             data-parent="#accordionidentified_by_items_anyOf_i0_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_content">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_content">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_content"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_content" onclick="setAnchor('#identified_by_items_anyOf_i0_content')"><span class="property-name">content</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_content"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_content"
             data-parent="#accordionidentified_by_items_anyOf_i0_content">
            <div class="card-body pl-5">

    <h4>crm:P190_has_symbolic_content</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The string representation of a `Name`, `Identifier`, `Statement` or other text</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_content" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_content')" class="ref-link">Same definition as content</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_language">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_language">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_language"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_language" onclick="setAnchor('#identified_by_items_anyOf_i0_language')"><span class="property-name">language</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_language"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_language"
             data-parent="#accordionidentified_by_items_anyOf_i0_language">
            <div class="card-body pl-5">

    <h4>crm:P72_has_language</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more `Language` entities in which the `content` of this text is written</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_language" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_language')" class="ref-link">Same definition as language</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_part">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_part">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_part"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_part" onclick="setAnchor('#identified_by_items_anyOf_i0_part')"><span class="property-name">part</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_part"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_part"
             data-parent="#accordionidentified_by_items_anyOf_i0_part">
            <div class="card-body pl-5">

    <span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A list of one or more `Name` structures, which are parts of this `Name`</span>
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i0_part_items">
            

    <h4>crm:E33_E41_Linguistic_Appellation</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A name of an entity
See: [API](https://linked.art/api/1.0/shared/name/) | [Model](https://linked.art/model/base/#names)</span><a href="#identified_by_items_anyOf_i0" onclick="anchorLink('identified_by_items_anyOf_i0')" class="ref-link">Same definition as crm:E33_E41_Linguistic_Appellation</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1" role="tabpanel">
            

    <h4>crm:E42_Identifier</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An identifier for an entity
See: [API](https://linked.art/api/1.0/shared/identifier/) | [Model](https://linked.art/model/base/#identifiers)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1__label" onclick="setAnchor('#identified_by_items_anyOf_i1__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1__label"
             data-parent="#accordionidentified_by_items_anyOf_i1__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_type" onclick="setAnchor('#identified_by_items_anyOf_i1_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_type_allOf_i1_const">Specific value: <code>"Identifier"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_identified_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_identified_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_identified_by" onclick="setAnchor('#identified_by_items_anyOf_i1_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_identified_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_referred_to_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_referred_to_by" onclick="setAnchor('#identified_by_items_anyOf_i1_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_referred_to_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_classified_as">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_classified_as"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_classified_as" onclick="setAnchor('#identified_by_items_anyOf_i1_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_classified_as"
             data-parent="#accordionidentified_by_items_anyOf_i1_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_content">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_content">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_content"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_content" onclick="setAnchor('#identified_by_items_anyOf_i1_content')"><span class="property-name">content</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_content"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_content"
             data-parent="#accordionidentified_by_items_anyOf_i1_content">
            <div class="card-body pl-5">

    <h4>crm:P190_has_symbolic_content</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The string representation of a `Name`, `Identifier`, `Statement` or other text</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_content" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_content')" class="ref-link">Same definition as content</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_part">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_part">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_part"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_part" onclick="setAnchor('#identified_by_items_anyOf_i1_part')"><span class="property-name">part</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_part"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_part"
             data-parent="#accordionidentified_by_items_anyOf_i1_part">
            <div class="card-body pl-5">

    <span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A list of one or more `Identifier` structures, which are parts of this `Identifier`</span>
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_part_items">
            

    <h4>crm:E42_Identifier</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An identifier for an entity
See: [API](https://linked.art/api/1.0/shared/identifier/) | [Model](https://linked.art/model/base/#identifiers)</span><a href="#identified_by_items_anyOf_i1" onclick="anchorLink('identified_by_items_anyOf_i1')" class="ref-link">Same definition as crm:E42_Identifier</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by')"><span class="property-name">assigned_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by">
            <div class="card-body pl-5">

    <span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">The activity through which this `Identifier` was assigned to the entity</span>
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items">
            

    <h4>crm:E13_Attribute_Assignment</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An activity which involves the assignment of some value to some entity, often with an explicit relationship between value and entity</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_type_allOf_i1_const">Specific value: <code>"AttributeAssignment"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_identified_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_identified_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_identified_by" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_identified_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_classified_as">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_classified_as"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_classified_as" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_classified_as"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_referred_to_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_referred_to_by" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_referred_to_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_took_place_at"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_took_place_at" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_took_place_at')"><span class="property-name">took_place_at</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at">
            <div class="card-body pl-5">

    <h4>crm:P7_took_place_at</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Place` at which this event occured</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items">
            

    <h4>crm:E53_Place</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Place` entity
See: [Schema](place.html)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_id" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_id"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_type_allOf_i1_const">Specific value: <code>"Place"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_took_place_at_items_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan')"><span class="property-name">timespan</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan">
            <div class="card-body pl-5">

    <h4>crm:P4_has_time-span</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A `TimeSpan` which describes the date-time range during which this event occured</span>

    

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_timespan_type_allOf_i1_const">Specific value: <code>"TimeSpan"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_identified_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_identified_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_identified_by" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_identified_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_classified_as">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_classified_as"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_classified_as" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_classified_as"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_begin">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_begin">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_begin"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_begin" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_begin')"><span class="property-name">begin_of_the_begin</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_begin"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_begin"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_begin">
            <div class="card-body pl-5">

    <h4>crm:P82a_begin_of_the_begin</h4><span class="badge badge-dark value-type">Type: string</span><span class="badge badge-info value-type">Format: date-time</span><br/>
<span class="description">The earliest possible date-time at which the timespan could have started</span>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_begin">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_begin">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_begin"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_begin" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_begin')"><span class="property-name">end_of_the_begin</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_begin"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_begin"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_begin">
            <div class="card-body pl-5">

    <h4>crm:P81a_end_of_the_begin</h4><span class="badge badge-dark value-type">Type: string</span><span class="badge badge-info value-type">Format: date-time</span><br/>
<span class="description">The latest possible date-time at which the timespan could have started</span>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_end">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_end">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_end"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_end" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_end')"><span class="property-name">begin_of_the_end</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_end"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_end"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_begin_of_the_end">
            <div class="card-body pl-5">

    <h4>crm:P81b_begin_of_the_end</h4><span class="badge badge-dark value-type">Type: string</span><span class="badge badge-info value-type">Format: date-time</span><br/>
<span class="description">The earliest possible date-time at which the timespan could have ended</span>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_end">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_end">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_end"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_end" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_end')"><span class="property-name">end_of_the_end</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_end"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_end"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_end_of_the_end">
            <div class="card-body pl-5">

    <h4>crm:P82b_end_of_the_end</h4><span class="badge badge-dark value-type">Type: string</span><span class="badge badge-info value-type">Format: date-time</span><br/>
<span class="description">The latest possible date-time at which the timespan could have ended</span>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration')"><span class="property-name">duration</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration">
            <div class="card-body pl-5">

    <h4>crm:P191_had_duration</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A `Dimension` that describes the duration of the timespan within any given date-times</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_type_allOf_i1_const">Specific value: <code>"Dimension"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_identified_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_identified_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_identified_by" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_identified_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_classified_as">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_classified_as"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_classified_as" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_classified_as"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value')"><span class="property-name">value</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value">
            <div class="card-body pl-5">

    <h4>crm:P90_has_value</h4><span class="badge badge-dark value-type">Type: number</span><br/>
<span class="description">The numeric value of a `Dimension` or `MonetaryAmount`</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="mf">10</span>
</pre></div>
</div><div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="mf">0.5</span>
</pre></div>
</div><div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_value_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="mf">42.75</span>
</pre></div>
</div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_lower_value_limit">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_lower_value_limit">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_lower_value_limit"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_lower_value_limit" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_lower_value_limit')"><span class="property-name">lower_value_limit</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_lower_value_limit"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_lower_value_limit"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_lower_value_limit">
            <div class="card-body pl-5">

    <h4>crm:P90a_has_lower_value_limit</h4><span class="badge badge-dark value-type">Type: number</span><br/>
<span class="description">The lowest possible value for the `Dimension` or `MonetaryAmount`</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Example:</div>
<br/><div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_lower_value_limit_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="mf">5</span>
</pre></div>
</div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_upper_value_limit">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_upper_value_limit">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_upper_value_limit"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_upper_value_limit" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_upper_value_limit')"><span class="property-name">upper_value_limit</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_upper_value_limit"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_upper_value_limit"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_upper_value_limit">
            <div class="card-body pl-5">

    <h4>crm:P90a_has_upper_value_limit</h4><span class="badge badge-dark value-type">Type: number</span><br/>
<span class="description">The highest possible value for the `Dimension` or `MonetaryAmount`</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Example:</div>
<br/><div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_upper_value_limit_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="mf">100</span>
</pre></div>
</div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit')"><span class="property-name">unit</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit">
            <div class="card-body pl-5">

    <h4>crm:P91_has_unit</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to the MeasurementUnit for this dimension</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_id" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_id"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_i1')"
            >Requirement 2</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_i1" role="tabpanel">
            

    <span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_type_allOf_i1_const">Specific value: <code>"MeasurementUnit"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_unit_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_assigned_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_assigned_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_assigned_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_assigned_by" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_assigned_by')"><span class="property-name">assigned_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_assigned_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_assigned_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_timespan_duration_assigned_by">
            <div class="card-body pl-5">

    <h4>crm:P141i_was_assigned_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">The Measurement(s) that led to the assigning of this dimension</span>
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_timespan_duration_assigned_by_items">
            

    <h4>crm:E13_Attribute_Assignment</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An activity which involves the assignment of some value to some entity, often with an explicit relationship between value and entity</span><a href="#identified_by_items_anyOf_i1_assigned_by_items" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items')" class="ref-link">Same definition as crm:E13_Attribute_Assignment</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
            </div>
        </div>
    </div>
</div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_caused_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_caused_by" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by')"><span class="property-name">caused_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_caused_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by">
            <div class="card-body pl-5">

    <h4>sci:O13i_is_triggered_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">Another event which caused this event to occur</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items">
            

    <span class="badge badge-dark value-type">Type: object</span><br/>


    <div class="any-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf"><h2 class="handle">
  <label>Any of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_anyOf" role="tablist"><li class="nav-item">
            <a class="nav-link active anyOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0')"
            >crm:E6_Event</a>
        </li><li class="nav-item">
            <a class="nav-link anyOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1')"
            >crm:E7_Activity</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0" role="tabpanel">
            

    <h4>crm:E6_Event</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to an `Event`
See: [Schema](event.html)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_id" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_id"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_i1')"
            >Requirement 2</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_i1" role="tabpanel">
            

    <span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_type_allOf_i1_const">Specific value: <code>"Event"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1" role="tabpanel">
            

    <h4>crm:E7_Activity</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to an `Activity`
See: [Schema](event.html)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_id" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_id"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_i1')"
            >Requirement 2</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_i1" role="tabpanel">
            

    <span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_type_allOf_i1_const">Specific value: <code>"Activity"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div></div></div>
        

        
        

        
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by')"><span class="property-name">carried_out_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by">
            <div class="card-body pl-5">

    <h4>crm:P14_carried_out_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to a Person or Group which carried out this activity</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items">
            

    <span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A Reference to a Person or Group</span>

    <div class="any-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf"><h2 class="handle">
  <label>Any of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_anyOf" role="tablist"><li class="nav-item">
            <a class="nav-link active anyOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0')"
            >E21_Person</a>
        </li><li class="nav-item">
            <a class="nav-link anyOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1')"
            >crm:E74_Group</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0" role="tabpanel">
            

    <h4>E21_Person</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Person`
See: [Schema](person.html)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_id" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_id"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_type_allOf_i1_const">Specific value: <code>"Person"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1" role="tabpanel">
            

    <h4>crm:E74_Group</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Group`
See: [Schema](group.html)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_id" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_id"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_i0')"
            >rdf:type</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_i0" role="tabpanel">
            

    <h4>rdf:type</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span><a href="#type_allOf_i0" onclick="anchorLink('type_allOf_i0')" class="ref-link">Same definition as rdf:type</a>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_type_allOf_i1_const">Specific value: <code>"Group"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div></div></div>
        

        
        

        
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object')"><span class="property-name">used_specific_object</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object">
            <div class="card-body pl-5">

    <h4>crm:P16_used_specific_object</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An object or set of things which was used to carry out this activity</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items">
            

    <span class="badge badge-dark value-type">Type: object</span><br/>


    <div class="any-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf"><h2 class="handle">
  <label>Any of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_anyOf" role="tablist"><li class="nav-item">
            <a class="nav-link active anyOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0')"
            >crm:E22_Human-Made_Object</a>
        </li><li class="nav-item">
            <a class="nav-link anyOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1')"
            >la:Set</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0" role="tabpanel">
            

    <h4>crm:E22_Human-Made_Object</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `HumanMadeObject`
See: [Schema](object.html)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_id" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_id"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_type_allOf_i1_const">Specific value: <code>"HumanMadeObject"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i0_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1" role="tabpanel">
            

    <h4>la:Set</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Set`
See: [Schema](set.html)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_id" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_id"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_i1')"
            >Requirement 2</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_i1" role="tabpanel">
            

    <span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_type_allOf_i1_const">Specific value: <code>"Set"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_used_specific_object_items_anyOf_i1_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div></div></div>
        

        
        

        
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_influenced_by">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_influenced_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_influenced_by"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_influenced_by" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_influenced_by')"><span class="property-name">influenced_by</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_influenced_by"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_influenced_by"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_influenced_by">
            <div class="card-body pl-5">

    <h4>crm:P15_was_influenced_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An entity that influenced the activity in some way</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_influenced_by_items">
            

    <h4>*</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to another primary entity
See: [API](https://linked.art/api/1.0/shared/reference/) | [Model]()</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items')" class="ref-link">Same definition as *</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_technique">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_technique">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_technique"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_technique" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_technique')"><span class="property-name">technique</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_technique"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_technique"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_technique">
            <div class="card-body pl-5">

    <h4>crm:P32_used_general_technique</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A general technique that was employed to carry out this activity</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_technique_items">
            

    <h4>crm:E55_Type</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A concept or 'Type' in the taxonomic sense
See: [API](https://linked.art/api/1.0/shared/type/) | [Model](https://linked.art/model/base/#types-and-classifications)</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items')" class="ref-link">Same definition as crm:E55_Type</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_during">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_during">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_during"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_during" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_during')"><span class="property-name">during</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_during"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_during"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_during">
            <div class="card-body pl-5">

    <h4>crm:P10_falls_within</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to a Period that the current temporal entity occurs during</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_during_items">
            

    <h4>crm:E4_Period</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Period`
See: [Schema](event.html)</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_during_items_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_during_items_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_during_items_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_during_items_id" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_during_items_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_during_items_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_during_items_id"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_during_items_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_during_items_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_during_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_during_items_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_during_items_type" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_during_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_during_items_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_during_items_type"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_during_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_i1')"
            >Requirement 2</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_i1" role="tabpanel">
            

    <span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="identified_by_items_anyOf_i1_assigned_by_items_during_items_type_allOf_i1_const">Specific value: <code>"Period"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_during_items__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_during_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_during_items__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_during_items__label" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_during_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_during_items__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_during_items__label"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_during_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_during_items_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_during_items_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_during_items_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_during_items_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_during_items_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_during_items_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_during_items_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_during_items_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_after">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_after">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_after"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_after" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_after')"><span class="property-name">after</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_after"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_after"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_after">
            <div class="card-body pl-5">

    <h4>crm:P183i_starts_after_the_end_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A Period, Event or Activity that the current Period, Event or Activity is after. (e.g. the referenced temporal entity is before the current one)</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_after_items">
            

    <span class="badge badge-dark value-type">Type: object</span><br/>


    <div class="any-of-value" id="identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf"><h2 class="handle">
  <label>Any of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_anyOf" role="tablist"><li class="nav-item">
            <a class="nav-link active anyOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i0')"
            >crm:E4_Period</a>
        </li><li class="nav-item">
            <a class="nav-link anyOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i1')"
            >crm:E6_Event</a>
        </li><li class="nav-item">
            <a class="nav-link anyOf-option"
               id="identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i2" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i2" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i2')"
            >crm:E7_Activity</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i0" role="tabpanel">
            

    <h4>crm:E4_Period</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Period`
See: [Schema](event.html)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_during_items" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_during_items')" class="ref-link">Same definition as crm:E4_Period</a>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i1" role="tabpanel">
            

    <h4>crm:E6_Event</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to an `Event`
See: [Schema](event.html)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i0')" class="ref-link">Same definition as crm:E6_Event</a>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i1_assigned_by_items_after_items_anyOf_i2" role="tabpanel">
            

    <h4>crm:E7_Activity</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to an `Activity`
See: [Schema](event.html)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_caused_by_items_anyOf_i1')" class="ref-link">Same definition as crm:E7_Activity</a>
        </div></div></div>
        

        
        

        
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_before">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_before">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_before"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_before" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_before')"><span class="property-name">before</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_before"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_before"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_before">
            <div class="card-body pl-5">

    <h4>crm:P183_ends_before_the_start_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A Period, Event or Activity that the current Period, Event or Activity is before. (e.g. the referenced temporal entity is after the current one)</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i1_assigned_by_items_before_items">
            

    <span class="badge badge-dark value-type">Type: object</span><br/>
<a href="#identified_by_items_anyOf_i1_assigned_by_items_after_items" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_after_items')" class="ref-link">Same definition as identified_by_items_anyOf_i1_assigned_by_items_after_items</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_part_of">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_part_of">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_part_of"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_part_of" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_part_of')"><span class="property-name">part_of</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_part_of"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_part_of"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_part_of">
            <div class="card-body pl-5">

    <span class="badge badge-dark value-type">Type: object</span><br/>
<a href="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_caused_by_items')" class="ref-link">Same definition as identified_by_items_anyOf_i1_assigned_by_items_caused_by_items</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_assigned">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_assigned">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_assigned"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_assigned" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_assigned')"><span class="property-name">assigned</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_assigned"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_assigned"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_assigned">
            <div class="card-body pl-5">

    <h4>*</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Attribute Assignments can assign any entity, structure or value</span>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i1_assigned_by_items_assigned_property">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i1_assigned_by_items_assigned_property">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i1_assigned_by_items_assigned_property"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i1_assigned_by_items_assigned_property" onclick="setAnchor('#identified_by_items_anyOf_i1_assigned_by_items_assigned_property')"><span class="property-name">assigned_property</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i1_assigned_by_items_assigned_property"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i1_assigned_by_items_assigned_property"
             data-parent="#accordionidentified_by_items_anyOf_i1_assigned_by_items_assigned_property">
            <div class="card-body pl-5">

    <h4>crm:P177_assigned_property_type</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The relationship from the attributed entity to the assigned entity, given as a string which resolves to a relationship in the context definition</span>
        

        
        

        
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
        </div></div></div>
        

        
        

        
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionclassified_as">
    <div class="card">
        <div class="card-header" id="headingclassified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#classified_as"
                        aria-expanded="" aria-controls="classified_as" onclick="setAnchor('#classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="classified_as"
             class="collapse property-definition-div" aria-labelledby="headingclassified_as"
             data-parent="#accordionclassified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionreferred_to_by">
    <div class="card">
        <div class="card-header" id="headingreferred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#referred_to_by"
                        aria-expanded="" aria-controls="referred_to_by" onclick="setAnchor('#referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingreferred_to_by"
             data-parent="#accordionreferred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionequivalent">
    <div class="card">
        <div class="card-header" id="headingequivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#equivalent"
                        aria-expanded="" aria-controls="equivalent" onclick="setAnchor('#equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="equivalent"
             class="collapse property-definition-div" aria-labelledby="headingequivalent"
             data-parent="#accordionequivalent">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="equivalent_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsequivalent_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="equivalent_allOf_i0" data-toggle="tab" href="#tab-pane_equivalent_allOf_i0" role="tab"
               onclick="setAnchor('#equivalent_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="equivalent_allOf_i1" data-toggle="tab" href="#tab-pane_equivalent_allOf_i1" role="tab"
               onclick="setAnchor('#equivalent_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_equivalent_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items">
            

    <h4>*</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to another primary entity
See: [API](https://linked.art/api/1.0/shared/reference/) | [Model]()</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1')"
            >Requirement 2</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1" role="tabpanel">
            

    <span class="badge badge-dark value-type">Type: enum (of string)</span><br/>
<div class="enum-value" id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_type_allOf_i1_enum">
            <h4>Must be one of:</h4>
            <ul class="list-group"><li class="list-group-item enum-item">"HumanMadeObject"</li><li class="list-group-item enum-item">"Person"</li><li class="list-group-item enum-item">"Group"</li><li class="list-group-item enum-item">"VisualItem"</li><li class="list-group-item enum-item">"LinguisticObject"</li><li class="list-group-item enum-item">"Set"</li><li class="list-group-item enum-item">"Place"</li><li class="list-group-item enum-item">"DigitalObject"</li><li class="list-group-item enum-item">"Type"</li><li class="list-group-item enum-item">"Event"</li><li class="list-group-item enum-item">"Activity"</li><li class="list-group-item enum-item">"Period"</li><li class="list-group-item enum-item">"Language"</li><li class="list-group-item enum-item">"Material"</li><li class="list-group-item enum-item">"Currency"</li><li class="list-group-item enum-item">"MeasurementUnit"</li><li class="list-group-item enum-item">"PropositionalObject"</li></ul>
            </div>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent">
    <div class="card">
        <div class="card-header" id="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent"
                        aria-expanded="" aria-controls="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent" onclick="setAnchor('#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent"
             data-parent="#accordionidentified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent_items_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_equivalent_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">List of `Person` entities</span>
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="equivalent_allOf_i1_items">
            

    <h4>E21_Person</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Person`
See: [Schema](person.html)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i0')" class="ref-link">Same definition as E21_Person</a>
        </div>
    </div>
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation">
    <div class="card">
        <div class="card-header" id="headingrepresentation">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation"
                        aria-expanded="" aria-controls="representation" onclick="setAnchor('#representation')"><span class="property-name">representation</span></button>
            </h2>
        </div>

        <div id="representation"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation"
             data-parent="#accordionrepresentation">
            <div class="card-body pl-5">

    <h4>crm:P138i_has_representation</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded link through a VisualItem to a Digital Object</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="representation_items">
            

    <h4>crm:E36_Visual_Item</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An embedded Visual Item, such as the content of a digital image</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionrepresentation_items_type">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_type"
                        aria-expanded="" aria-controls="representation_items_type" onclick="setAnchor('#representation_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="representation_items_type"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_type"
             data-parent="#accordionrepresentation_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="representation_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsrepresentation_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="representation_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_representation_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#representation_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="representation_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_representation_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#representation_items_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_representation_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_representation_items_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="representation_items_type_allOf_i1_const">Specific value: <code>"VisualItem"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items__label">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items__label"
                        aria-expanded="" aria-controls="representation_items__label" onclick="setAnchor('#representation_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="representation_items__label"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items__label"
             data-parent="#accordionrepresentation_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_identified_by">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_identified_by"
                        aria-expanded="" aria-controls="representation_items_identified_by" onclick="setAnchor('#representation_items_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="representation_items_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_identified_by"
             data-parent="#accordionrepresentation_items_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_classified_as">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_classified_as"
                        aria-expanded="" aria-controls="representation_items_classified_as" onclick="setAnchor('#representation_items_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="representation_items_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_classified_as"
             data-parent="#accordionrepresentation_items_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_referred_to_by"
                        aria-expanded="" aria-controls="representation_items_referred_to_by" onclick="setAnchor('#representation_items_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="representation_items_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_referred_to_by"
             data-parent="#accordionrepresentation_items_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by" onclick="setAnchor('#representation_items_digitally_shown_by')"><span class="property-name">digitally_shown_by</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by"
             data-parent="#accordionrepresentation_items_digitally_shown_by">
            <div class="card-body pl-5">

    <h4>la:digitally_shown_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A digital object that shows the current visual item</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="representation_items_digitally_shown_by_items">
            

    <h4>dig:D1_Digital_Object</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An embedded Digital Object, such as a home page reference</span>

    
        

        
        

        
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_type">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_type"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_type" onclick="setAnchor('#representation_items_digitally_shown_by_items_type')"><span class="property-name">type</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_type"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_type"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="representation_items_digitally_shown_by_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsrepresentation_items_digitally_shown_by_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="representation_items_digitally_shown_by_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_representation_items_digitally_shown_by_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#representation_items_digitally_shown_by_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="representation_items_digitally_shown_by_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_representation_items_digitally_shown_by_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#representation_items_digitally_shown_by_items_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_representation_items_digitally_shown_by_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_representation_items_digitally_shown_by_items_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="representation_items_digitally_shown_by_items_type_allOf_i1_const">Specific value: <code>"DigitalObject"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items__label">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items__label"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items__label" onclick="setAnchor('#representation_items_digitally_shown_by_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items__label"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items__label"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_identified_by">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_identified_by"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_identified_by" onclick="setAnchor('#representation_items_digitally_shown_by_items_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_identified_by"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_classified_as">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_classified_as"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_classified_as" onclick="setAnchor('#representation_items_digitally_shown_by_items_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_classified_as"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_referred_to_by"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_referred_to_by" onclick="setAnchor('#representation_items_digitally_shown_by_items_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_referred_to_by"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_access_point">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_access_point">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_access_point"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_access_point" onclick="setAnchor('#representation_items_digitally_shown_by_items_access_point')"><span class="property-name">access_point</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_access_point"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_access_point"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_access_point">
            <div class="card-body pl-5">

    <h4>la:access_point</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A URL from which the digital object is able to be retrieved</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="representation_items_digitally_shown_by_items_access_point_items">
            

    <h4>dig:D1_Digital_Object
See: [Schema](digital.html)</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `DigitalObject`</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_access_point_items_id">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_access_point_items_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_access_point_items_id"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_access_point_items_id" onclick="setAnchor('#representation_items_digitally_shown_by_items_access_point_items_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_access_point_items_id"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_access_point_items_id"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_access_point_items_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_access_point_items_type">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_access_point_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_access_point_items_type"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_access_point_items_type" onclick="setAnchor('#representation_items_digitally_shown_by_items_access_point_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_access_point_items_type"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_access_point_items_type"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_access_point_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="representation_items_digitally_shown_by_items_access_point_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsrepresentation_items_digitally_shown_by_items_access_point_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="representation_items_digitally_shown_by_items_access_point_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_representation_items_digitally_shown_by_items_access_point_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#representation_items_digitally_shown_by_items_access_point_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="representation_items_digitally_shown_by_items_access_point_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_representation_items_digitally_shown_by_items_access_point_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#representation_items_digitally_shown_by_items_access_point_items_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_representation_items_digitally_shown_by_items_access_point_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_representation_items_digitally_shown_by_items_access_point_items_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="representation_items_digitally_shown_by_items_access_point_items_type_allOf_i1_const">Specific value: <code>"DigitalObject"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_access_point_items__label">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_access_point_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_access_point_items__label"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_access_point_items__label" onclick="setAnchor('#representation_items_digitally_shown_by_items_access_point_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_access_point_items__label"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_access_point_items__label"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_access_point_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_access_point_items_equivalent">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_access_point_items_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_access_point_items_equivalent"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_access_point_items_equivalent" onclick="setAnchor('#representation_items_digitally_shown_by_items_access_point_items_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_access_point_items_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_access_point_items_equivalent"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_access_point_items_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_format">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_format">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_format"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_format" onclick="setAnchor('#representation_items_digitally_shown_by_items_format')"><span class="property-name">format</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_format"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_format"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_format">
            <div class="card-body pl-5">

    <h4>dc:format</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The media type of the content of the embedded text, e.g. text/plain</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_format" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_format')" class="ref-link">Same definition as format</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_conforms_to">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_conforms_to">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_conforms_to"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_conforms_to" onclick="setAnchor('#representation_items_digitally_shown_by_items_conforms_to')"><span class="property-name">conforms_to</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_conforms_to"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_conforms_to"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_conforms_to">
            <div class="card-body pl-5">

    <h4>dcterms:conformsTo</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A standard or specification that this entity conforms to or embodies</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="representation_items_digitally_shown_by_items_conforms_to_items">
            

    <h4>crm:E73_Information_Object</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to an `InformationObject`</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_conforms_to_items_id">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_conforms_to_items_id">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_conforms_to_items_id"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_conforms_to_items_id" onclick="setAnchor('#representation_items_digitally_shown_by_items_conforms_to_items_id')"><span class="property-name">id</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_conforms_to_items_id"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_conforms_to_items_id"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_conforms_to_items_id">
            <div class="card-body pl-5">

    <h4>the subject uri</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The URI of the entity</span><a href="#id" onclick="anchorLink('id')" class="ref-link">Same definition as id</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_conforms_to_items_type">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_conforms_to_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_conforms_to_items_type"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_conforms_to_items_type" onclick="setAnchor('#representation_items_digitally_shown_by_items_conforms_to_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_conforms_to_items_type"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_conforms_to_items_type"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_conforms_to_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="representation_items_digitally_shown_by_items_conforms_to_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsrepresentation_items_digitally_shown_by_items_conforms_to_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="representation_items_digitally_shown_by_items_conforms_to_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_representation_items_digitally_shown_by_items_conforms_to_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#representation_items_digitally_shown_by_items_conforms_to_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="representation_items_digitally_shown_by_items_conforms_to_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_representation_items_digitally_shown_by_items_conforms_to_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#representation_items_digitally_shown_by_items_conforms_to_items_type_allOf_i1')"
            >Requirement 2</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_representation_items_digitally_shown_by_items_conforms_to_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_representation_items_digitally_shown_by_items_conforms_to_items_type_allOf_i1" role="tabpanel">
            

    <span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="representation_items_digitally_shown_by_items_conforms_to_items_type_allOf_i1_const">Specific value: <code>"InformationObject"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_conforms_to_items__label">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_conforms_to_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_conforms_to_items__label"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_conforms_to_items__label" onclick="setAnchor('#representation_items_digitally_shown_by_items_conforms_to_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_conforms_to_items__label"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_conforms_to_items__label"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_conforms_to_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionrepresentation_items_digitally_shown_by_items_conforms_to_items_equivalent">
    <div class="card">
        <div class="card-header" id="headingrepresentation_items_digitally_shown_by_items_conforms_to_items_equivalent">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#representation_items_digitally_shown_by_items_conforms_to_items_equivalent"
                        aria-expanded="" aria-controls="representation_items_digitally_shown_by_items_conforms_to_items_equivalent" onclick="setAnchor('#representation_items_digitally_shown_by_items_conforms_to_items_equivalent')"><span class="property-name">equivalent</span></button>
            </h2>
        </div>

        <div id="representation_items_digitally_shown_by_items_conforms_to_items_equivalent"
             class="collapse property-definition-div" aria-labelledby="headingrepresentation_items_digitally_shown_by_items_conforms_to_items_equivalent"
             data-parent="#accordionrepresentation_items_digitally_shown_by_items_conforms_to_items_equivalent">
            <div class="card-body pl-5">

    <h4>la:equivalent</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more other identities for this entity, such as in external vocabularies or systems</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as_items_equivalent')" class="ref-link">Same definition as equivalent</a>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionmember_of">
    <div class="card">
        <div class="card-header" id="headingmember_of">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#member_of"
                        aria-expanded="" aria-controls="member_of" onclick="setAnchor('#member_of')"><span class="property-name">member_of</span></button>
            </h2>
        </div>

        <div id="member_of"
             class="collapse property-definition-div" aria-labelledby="headingmember_of"
             data-parent="#accordionmember_of">
            <div class="card-body pl-5">

    <h4>crm:P107i_is_current_or_former_member_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more `Group` entities of which this entity is a member</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="member_of_items">
            

    <h4>crm:E74_Group</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Group`
See: [Schema](group.html)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_carried_out_by_items_anyOf_i1')" class="ref-link">Same definition as crm:E74_Group</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionsubject_of">
    <div class="card">
        <div class="card-header" id="headingsubject_of">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#subject_of"
                        aria-expanded="" aria-controls="subject_of" onclick="setAnchor('#subject_of')"><span class="property-name">subject_of</span></button>
            </h2>
        </div>

        <div id="subject_of"
             class="collapse property-definition-div" aria-labelledby="headingsubject_of"
             data-parent="#accordionsubject_of">
            <div class="card-body pl-5">

    <h4>crm:P129i_is_subject_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">One or more human-readable web pages or other digital objects where the focus of the content is this entity</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="subject_of_items">
            

    <h4>crm:E33_Linguistic_Object</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An embedded Linguistic Object, such as the content of a web page</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordionsubject_of_items_type">
    <div class="card">
        <div class="card-header" id="headingsubject_of_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#subject_of_items_type"
                        aria-expanded="" aria-controls="subject_of_items_type" onclick="setAnchor('#subject_of_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="subject_of_items_type"
             class="collapse property-definition-div" aria-labelledby="headingsubject_of_items_type"
             data-parent="#accordionsubject_of_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="subject_of_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabssubject_of_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="subject_of_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_subject_of_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#subject_of_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="subject_of_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_subject_of_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#subject_of_items_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_subject_of_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_subject_of_items_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="subject_of_items_type_allOf_i1_const">Specific value: <code>"LinguisticObject"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionsubject_of_items__label">
    <div class="card">
        <div class="card-header" id="headingsubject_of_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#subject_of_items__label"
                        aria-expanded="" aria-controls="subject_of_items__label" onclick="setAnchor('#subject_of_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="subject_of_items__label"
             class="collapse property-definition-div" aria-labelledby="headingsubject_of_items__label"
             data-parent="#accordionsubject_of_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionsubject_of_items_identified_by">
    <div class="card">
        <div class="card-header" id="headingsubject_of_items_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#subject_of_items_identified_by"
                        aria-expanded="" aria-controls="subject_of_items_identified_by" onclick="setAnchor('#subject_of_items_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="subject_of_items_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingsubject_of_items_identified_by"
             data-parent="#accordionsubject_of_items_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionsubject_of_items_classified_as">
    <div class="card">
        <div class="card-header" id="headingsubject_of_items_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#subject_of_items_classified_as"
                        aria-expanded="" aria-controls="subject_of_items_classified_as" onclick="setAnchor('#subject_of_items_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="subject_of_items_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingsubject_of_items_classified_as"
             data-parent="#accordionsubject_of_items_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionsubject_of_items_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingsubject_of_items_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#subject_of_items_referred_to_by"
                        aria-expanded="" aria-controls="subject_of_items_referred_to_by" onclick="setAnchor('#subject_of_items_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="subject_of_items_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingsubject_of_items_referred_to_by"
             data-parent="#accordionsubject_of_items_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionsubject_of_items_language">
    <div class="card">
        <div class="card-header" id="headingsubject_of_items_language">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#subject_of_items_language"
                        aria-expanded="" aria-controls="subject_of_items_language" onclick="setAnchor('#subject_of_items_language')"><span class="property-name">language</span></button>
            </h2>
        </div>

        <div id="subject_of_items_language"
             class="collapse property-definition-div" aria-labelledby="headingsubject_of_items_language"
             data-parent="#accordionsubject_of_items_language">
            <div class="card-body pl-5">

    <h4>crm:P72_has_language</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to one or more `Language` entities in which the `content` of this text is written</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_language" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_language')" class="ref-link">Same definition as language</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionsubject_of_items_digitally_carried_by">
    <div class="card">
        <div class="card-header" id="headingsubject_of_items_digitally_carried_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#subject_of_items_digitally_carried_by"
                        aria-expanded="" aria-controls="subject_of_items_digitally_carried_by" onclick="setAnchor('#subject_of_items_digitally_carried_by')"><span class="property-name">digitally_carried_by</span></button>
            </h2>
        </div>

        <div id="subject_of_items_digitally_carried_by"
             class="collapse property-definition-div" aria-labelledby="headingsubject_of_items_digitally_carried_by"
             data-parent="#accordionsubject_of_items_digitally_carried_by">
            <div class="card-body pl-5">

    <h4>la:digitally_carried_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A digital object that carries the current linguistic object</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="subject_of_items_digitally_carried_by_items">
            

    <h4>dig:D1_Digital_Object</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An embedded Digital Object, such as a home page reference</span><a href="#representation_items_digitally_shown_by_items" onclick="anchorLink('representation_items_digitally_shown_by_items')" class="ref-link">Same definition as dig:D1_Digital_Object</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionattributed_by">
    <div class="card">
        <div class="card-header" id="headingattributed_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#attributed_by"
                        aria-expanded="" aria-controls="attributed_by" onclick="setAnchor('#attributed_by')"><span class="property-name">attributed_by</span></button>
            </h2>
        </div>

        <div id="attributed_by"
             class="collapse property-definition-div" aria-labelledby="headingattributed_by"
             data-parent="#accordionattributed_by">
            <div class="card-body pl-5">

    <h4>crm:P140i_was_attributed_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">One or more AttributeAssignments that relate some other entity to this one</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="attributed_by_items">
            

    <h4>crm:E13_Attribute_Assignment</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An activity which involves the assignment of some value to some entity, often with an explicit relationship between value and entity</span><a href="#identified_by_items_anyOf_i1_assigned_by_items" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items')" class="ref-link">Same definition as crm:E13_Attribute_Assignment</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out">
    <div class="card">
        <div class="card-header" id="headingcarried_out">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out"
                        aria-expanded="" aria-controls="carried_out" onclick="setAnchor('#carried_out')"><span class="property-name">carried_out</span></button>
            </h2>
        </div>

        <div id="carried_out"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out"
             data-parent="#accordioncarried_out">
            <div class="card-body pl-5">

    <h4>crm:P14i_performed</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">One or more activities which this entity carried out or performed</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="carried_out_items">
            

    <h4>crm:E7_Activity</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An activity carried out by some person or group</span>

     <span class="badge badge-info no-additional">No Additional Properties</span>
        

        
        

        
<div class="accordion" id="accordioncarried_out_items_type">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_type"
                        aria-expanded="" aria-controls="carried_out_items_type" onclick="setAnchor('#carried_out_items_type')"><span class="property-name">type</span> <span class="badge badge-warning required-property">Required</span></button>
            </h2>
        </div>

        <div id="carried_out_items_type"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_type"
             data-parent="#accordioncarried_out_items_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="carried_out_items_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabscarried_out_items_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="carried_out_items_type_allOf_i0" data-toggle="tab" href="#tab-pane_carried_out_items_type_allOf_i0" role="tab"
               onclick="setAnchor('#carried_out_items_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="carried_out_items_type_allOf_i1" data-toggle="tab" href="#tab-pane_carried_out_items_type_allOf_i1" role="tab"
               onclick="setAnchor('#carried_out_items_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_carried_out_items_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_carried_out_items_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="carried_out_items_type_allOf_i1_const">Specific value: <code>"Activity"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items__label">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items__label"
                        aria-expanded="" aria-controls="carried_out_items__label" onclick="setAnchor('#carried_out_items__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="carried_out_items__label"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items__label"
             data-parent="#accordioncarried_out_items__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_identified_by">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_identified_by"
                        aria-expanded="" aria-controls="carried_out_items_identified_by" onclick="setAnchor('#carried_out_items_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="carried_out_items_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_identified_by"
             data-parent="#accordioncarried_out_items_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_classified_as">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_classified_as"
                        aria-expanded="" aria-controls="carried_out_items_classified_as" onclick="setAnchor('#carried_out_items_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="carried_out_items_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_classified_as"
             data-parent="#accordioncarried_out_items_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_referred_to_by"
                        aria-expanded="" aria-controls="carried_out_items_referred_to_by" onclick="setAnchor('#carried_out_items_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="carried_out_items_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_referred_to_by"
             data-parent="#accordioncarried_out_items_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_took_place_at">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_took_place_at">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_took_place_at"
                        aria-expanded="" aria-controls="carried_out_items_took_place_at" onclick="setAnchor('#carried_out_items_took_place_at')"><span class="property-name">took_place_at</span></button>
            </h2>
        </div>

        <div id="carried_out_items_took_place_at"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_took_place_at"
             data-parent="#accordioncarried_out_items_took_place_at">
            <div class="card-body pl-5">

    <h4>crm:P7_took_place_at</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Place` at which this event occured</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_took_place_at" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_took_place_at')" class="ref-link">Same definition as took_place_at</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_timespan">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_timespan">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_timespan"
                        aria-expanded="" aria-controls="carried_out_items_timespan" onclick="setAnchor('#carried_out_items_timespan')"><span class="property-name">timespan</span></button>
            </h2>
        </div>

        <div id="carried_out_items_timespan"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_timespan"
             data-parent="#accordioncarried_out_items_timespan">
            <div class="card-body pl-5">

    <h4>crm:P4_has_time-span</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A `TimeSpan` which describes the date-time range during which this event occured</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_timespan" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_timespan')" class="ref-link">Same definition as timespan</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_caused_by">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_caused_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_caused_by"
                        aria-expanded="" aria-controls="carried_out_items_caused_by" onclick="setAnchor('#carried_out_items_caused_by')"><span class="property-name">caused_by</span></button>
            </h2>
        </div>

        <div id="carried_out_items_caused_by"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_caused_by"
             data-parent="#accordioncarried_out_items_caused_by">
            <div class="card-body pl-5">

    <h4>sci:O13i_is_triggered_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">Another event which caused this event to occur</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_caused_by" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_caused_by')" class="ref-link">Same definition as caused_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_carried_out_by">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_carried_out_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_carried_out_by"
                        aria-expanded="" aria-controls="carried_out_items_carried_out_by" onclick="setAnchor('#carried_out_items_carried_out_by')"><span class="property-name">carried_out_by</span></button>
            </h2>
        </div>

        <div id="carried_out_items_carried_out_by"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_carried_out_by"
             data-parent="#accordioncarried_out_items_carried_out_by">
            <div class="card-body pl-5">

    <h4>crm:P14_carried_out_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to a Person or Group which carried out this activity</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_carried_out_by" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_carried_out_by')" class="ref-link">Same definition as carried_out_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_used_specific_object">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_used_specific_object">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_used_specific_object"
                        aria-expanded="" aria-controls="carried_out_items_used_specific_object" onclick="setAnchor('#carried_out_items_used_specific_object')"><span class="property-name">used_specific_object</span></button>
            </h2>
        </div>

        <div id="carried_out_items_used_specific_object"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_used_specific_object"
             data-parent="#accordioncarried_out_items_used_specific_object">
            <div class="card-body pl-5">

    <h4>crm:P16_used_specific_object</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An object or set of things which was used to carry out this activity</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_used_specific_object" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_used_specific_object')" class="ref-link">Same definition as used_specific_object</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_influenced_by">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_influenced_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_influenced_by"
                        aria-expanded="" aria-controls="carried_out_items_influenced_by" onclick="setAnchor('#carried_out_items_influenced_by')"><span class="property-name">influenced_by</span></button>
            </h2>
        </div>

        <div id="carried_out_items_influenced_by"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_influenced_by"
             data-parent="#accordioncarried_out_items_influenced_by">
            <div class="card-body pl-5">

    <h4>crm:P15_was_influenced_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An entity that influenced the activity in some way</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_influenced_by" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_influenced_by')" class="ref-link">Same definition as influenced_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_technique">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_technique">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_technique"
                        aria-expanded="" aria-controls="carried_out_items_technique" onclick="setAnchor('#carried_out_items_technique')"><span class="property-name">technique</span></button>
            </h2>
        </div>

        <div id="carried_out_items_technique"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_technique"
             data-parent="#accordioncarried_out_items_technique">
            <div class="card-body pl-5">

    <h4>crm:P32_used_general_technique</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A general technique that was employed to carry out this activity</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_technique" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_technique')" class="ref-link">Same definition as technique</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_during">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_during">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_during"
                        aria-expanded="" aria-controls="carried_out_items_during" onclick="setAnchor('#carried_out_items_during')"><span class="property-name">during</span></button>
            </h2>
        </div>

        <div id="carried_out_items_during"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_during"
             data-parent="#accordioncarried_out_items_during">
            <div class="card-body pl-5">

    <h4>crm:P10_falls_within</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to a Period that the current temporal entity occurs during</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_during" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_during')" class="ref-link">Same definition as during</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_after">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_after">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_after"
                        aria-expanded="" aria-controls="carried_out_items_after" onclick="setAnchor('#carried_out_items_after')"><span class="property-name">after</span></button>
            </h2>
        </div>

        <div id="carried_out_items_after"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_after"
             data-parent="#accordioncarried_out_items_after">
            <div class="card-body pl-5">

    <h4>crm:P183i_starts_after_the_end_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A Period, Event or Activity that the current Period, Event or Activity is after. (e.g. the referenced temporal entity is before the current one)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_after" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_after')" class="ref-link">Same definition as after</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_before">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_before">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_before"
                        aria-expanded="" aria-controls="carried_out_items_before" onclick="setAnchor('#carried_out_items_before')"><span class="property-name">before</span></button>
            </h2>
        </div>

        <div id="carried_out_items_before"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_before"
             data-parent="#accordioncarried_out_items_before">
            <div class="card-body pl-5">

    <h4>crm:P183_ends_before_the_start_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A Period, Event or Activity that the current Period, Event or Activity is before. (e.g. the referenced temporal entity is after the current one)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_before" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_before')" class="ref-link">Same definition as before</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncarried_out_items_part_of">
    <div class="card">
        <div class="card-header" id="headingcarried_out_items_part_of">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#carried_out_items_part_of"
                        aria-expanded="" aria-controls="carried_out_items_part_of" onclick="setAnchor('#carried_out_items_part_of')"><span class="property-name">part_of</span></button>
            </h2>
        </div>

        <div id="carried_out_items_part_of"
             class="collapse property-definition-div" aria-labelledby="headingcarried_out_items_part_of"
             data-parent="#accordioncarried_out_items_part_of">
            <div class="card-body pl-5">

    <span class="badge badge-dark value-type">Type: object</span><br/>
<a href="#identified_by_items_anyOf_i1_assigned_by_items_caused_by_items" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_caused_by_items')" class="ref-link">Same definition as identified_by_items_anyOf_i1_assigned_by_items_caused_by_items</a>
            </div>
        </div>
    </div>
</div>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionparticipated_in">
    <div class="card">
        <div class="card-header" id="headingparticipated_in">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#participated_in"
                        aria-expanded="" aria-controls="participated_in" onclick="setAnchor('#participated_in')"><span class="property-name">participated_in</span></button>
            </h2>
        </div>

        <div id="participated_in"
             class="collapse property-definition-div" aria-labelledby="headingparticipated_in"
             data-parent="#accordionparticipated_in">
            <div class="card-body pl-5">

    <h4>crm:P11i_participated_in</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">One or more activities which this entity participated in, but did not carry out directly</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="participated_in_items">
            

    <h4>crm:E7_Activity</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An activity carried out by some person or group</span><a href="#carried_out_items" onclick="anchorLink('carried_out_items')" class="ref-link">Same definition as crm:E7_Activity</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordioncontact_point">
    <div class="card">
        <div class="card-header" id="headingcontact_point">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#contact_point"
                        aria-expanded="" aria-controls="contact_point" onclick="setAnchor('#contact_point')"><span class="property-name">contact_point</span></button>
            </h2>
        </div>

        <div id="contact_point"
             class="collapse property-definition-div" aria-labelledby="headingcontact_point"
             data-parent="#accordioncontact_point">
            <div class="card-body pl-5">

    <h4>crm:P76_has_contact_point</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An identifier which can be used as a contact point or address for the entity, such as an email address</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="contact_point_items">
            

    <h4>crm:E42_Identifier</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">An identifier for an entity
See: [API](https://linked.art/api/1.0/shared/identifier/) | [Model](https://linked.art/model/base/#identifiers)</span><a href="#identified_by_items_anyOf_i1" onclick="anchorLink('identified_by_items_anyOf_i1')" class="ref-link">Same definition as crm:E42_Identifier</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionresidence">
    <div class="card">
        <div class="card-header" id="headingresidence">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#residence"
                        aria-expanded="" aria-controls="residence" onclick="setAnchor('#residence')"><span class="property-name">residence</span></button>
            </h2>
        </div>

        <div id="residence"
             class="collapse property-definition-div" aria-labelledby="headingresidence"
             data-parent="#accordionresidence">
            <div class="card-body pl-5">

    <h4>crm:P74_has_current_or_former_residence</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Place` where this entity has resided or done business</span>

    
        

        
        

         <span class="badge badge-info no-additional">No Additional Items</span><h4>Each item of this array must be:</h4>
    <div class="card">
        <div class="card-body items-definition" id="residence_items">
            

    <h4>crm:E53_Place</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">Reference to a `Place` entity
See: [Schema](place.html)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_took_place_at_items')" class="ref-link">Same definition as crm:E53_Place</a>
        </div>
    </div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn">
    <div class="card">
        <div class="card-header" id="headingborn">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born"
                        aria-expanded="" aria-controls="born" onclick="setAnchor('#born')"><span class="property-name">born</span></button>
            </h2>
        </div>

        <div id="born"
             class="collapse property-definition-div" aria-labelledby="headingborn"
             data-parent="#accordionborn">
            <div class="card-body pl-5">

    <h4>crm:P98i_was_born</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">The event in which this Person was born</span>

    
        

        
        

        
<div class="accordion" id="accordionborn_type">
    <div class="card">
        <div class="card-header" id="headingborn_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_type"
                        aria-expanded="" aria-controls="born_type" onclick="setAnchor('#born_type')"><span class="property-name">type</span></button>
            </h2>
        </div>

        <div id="born_type"
             class="collapse property-definition-div" aria-labelledby="headingborn_type"
             data-parent="#accordionborn_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="born_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsborn_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="born_type_allOf_i0" data-toggle="tab" href="#tab-pane_born_type_allOf_i0" role="tab"
               onclick="setAnchor('#born_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="born_type_allOf_i1" data-toggle="tab" href="#tab-pane_born_type_allOf_i1" role="tab"
               onclick="setAnchor('#born_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_born_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_born_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="born_type_allOf_i1_const">Specific value: <code>"Birth"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn__label">
    <div class="card">
        <div class="card-header" id="headingborn__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born__label"
                        aria-expanded="" aria-controls="born__label" onclick="setAnchor('#born__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="born__label"
             class="collapse property-definition-div" aria-labelledby="headingborn__label"
             data-parent="#accordionborn__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn_identified_by">
    <div class="card">
        <div class="card-header" id="headingborn_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_identified_by"
                        aria-expanded="" aria-controls="born_identified_by" onclick="setAnchor('#born_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="born_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingborn_identified_by"
             data-parent="#accordionborn_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn_classified_as">
    <div class="card">
        <div class="card-header" id="headingborn_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_classified_as"
                        aria-expanded="" aria-controls="born_classified_as" onclick="setAnchor('#born_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="born_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingborn_classified_as"
             data-parent="#accordionborn_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingborn_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_referred_to_by"
                        aria-expanded="" aria-controls="born_referred_to_by" onclick="setAnchor('#born_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="born_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingborn_referred_to_by"
             data-parent="#accordionborn_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn_took_place_at">
    <div class="card">
        <div class="card-header" id="headingborn_took_place_at">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_took_place_at"
                        aria-expanded="" aria-controls="born_took_place_at" onclick="setAnchor('#born_took_place_at')"><span class="property-name">took_place_at</span></button>
            </h2>
        </div>

        <div id="born_took_place_at"
             class="collapse property-definition-div" aria-labelledby="headingborn_took_place_at"
             data-parent="#accordionborn_took_place_at">
            <div class="card-body pl-5">

    <h4>crm:P7_took_place_at</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Place` at which this event occured</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_took_place_at" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_took_place_at')" class="ref-link">Same definition as took_place_at</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn_timespan">
    <div class="card">
        <div class="card-header" id="headingborn_timespan">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_timespan"
                        aria-expanded="" aria-controls="born_timespan" onclick="setAnchor('#born_timespan')"><span class="property-name">timespan</span></button>
            </h2>
        </div>

        <div id="born_timespan"
             class="collapse property-definition-div" aria-labelledby="headingborn_timespan"
             data-parent="#accordionborn_timespan">
            <div class="card-body pl-5">

    <h4>crm:P4_has_time-span</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A `TimeSpan` which describes the date-time range during which this event occured</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_timespan" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_timespan')" class="ref-link">Same definition as timespan</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn_during">
    <div class="card">
        <div class="card-header" id="headingborn_during">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_during"
                        aria-expanded="" aria-controls="born_during" onclick="setAnchor('#born_during')"><span class="property-name">during</span></button>
            </h2>
        </div>

        <div id="born_during"
             class="collapse property-definition-div" aria-labelledby="headingborn_during"
             data-parent="#accordionborn_during">
            <div class="card-body pl-5">

    <h4>crm:P10_falls_within</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to a Period that the current temporal entity occurs during</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_during" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_during')" class="ref-link">Same definition as during</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn_after">
    <div class="card">
        <div class="card-header" id="headingborn_after">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_after"
                        aria-expanded="" aria-controls="born_after" onclick="setAnchor('#born_after')"><span class="property-name">after</span></button>
            </h2>
        </div>

        <div id="born_after"
             class="collapse property-definition-div" aria-labelledby="headingborn_after"
             data-parent="#accordionborn_after">
            <div class="card-body pl-5">

    <h4>crm:P183i_starts_after_the_end_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A Period, Event or Activity that the current Period, Event or Activity is after. (e.g. the referenced temporal entity is before the current one)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_after" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_after')" class="ref-link">Same definition as after</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn_before">
    <div class="card">
        <div class="card-header" id="headingborn_before">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_before"
                        aria-expanded="" aria-controls="born_before" onclick="setAnchor('#born_before')"><span class="property-name">before</span></button>
            </h2>
        </div>

        <div id="born_before"
             class="collapse property-definition-div" aria-labelledby="headingborn_before"
             data-parent="#accordionborn_before">
            <div class="card-body pl-5">

    <h4>crm:P183_ends_before_the_start_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A Period, Event or Activity that the current Period, Event or Activity is before. (e.g. the referenced temporal entity is after the current one)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_before" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_before')" class="ref-link">Same definition as before</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordionborn_caused_by">
    <div class="card">
        <div class="card-header" id="headingborn_caused_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#born_caused_by"
                        aria-expanded="" aria-controls="born_caused_by" onclick="setAnchor('#born_caused_by')"><span class="property-name">caused_by</span></button>
            </h2>
        </div>

        <div id="born_caused_by"
             class="collapse property-definition-div" aria-labelledby="headingborn_caused_by"
             data-parent="#accordionborn_caused_by">
            <div class="card-body pl-5">

    <h4>sci:O13i_is_triggered_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">Another event which caused this event to occur</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_caused_by" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_caused_by')" class="ref-link">Same definition as caused_by</a>
            </div>
        </div>
    </div>
</div>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied">
    <div class="card">
        <div class="card-header" id="headingdied">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died"
                        aria-expanded="" aria-controls="died" onclick="setAnchor('#died')"><span class="property-name">died</span></button>
            </h2>
        </div>

        <div id="died"
             class="collapse property-definition-div" aria-labelledby="headingdied"
             data-parent="#accordiondied">
            <div class="card-body pl-5">

    <h4>crm:P100i_died_in</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">The event in which this Person died</span>

    
        

        
        

        
<div class="accordion" id="accordiondied_type">
    <div class="card">
        <div class="card-header" id="headingdied_type">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_type"
                        aria-expanded="" aria-controls="died_type" onclick="setAnchor('#died_type')"><span class="property-name">type</span></button>
            </h2>
        </div>

        <div id="died_type"
             class="collapse property-definition-div" aria-labelledby="headingdied_type"
             data-parent="#accordiondied_type">
            <div class="card-body pl-5">

    <br/>
<div class="all-of-value" id="died_type_allOf"><h2 class="handle">
  <label>All of</label>
</h2><ul class="nav nav-tabs" id="tabsdied_type_allOf_allOf" role="tablist"><li class="nav-item">
            <a class="nav-link active allOf-option"
               id="died_type_allOf_i0" data-toggle="tab" href="#tab-pane_died_type_allOf_i0" role="tab"
               onclick="setAnchor('#died_type_allOf_i0')"
            >General</a>
        </li><li class="nav-item">
            <a class="nav-link allOf-option"
               id="died_type_allOf_i1" data-toggle="tab" href="#tab-pane_died_type_allOf_i1" role="tab"
               onclick="setAnchor('#died_type_allOf_i1')"
            >Specific</a>
        </li></ul>
<div class="tab-content card"><div class="tab-pane fade card-body active show"
             id="tab-pane_died_type_allOf_i0" role="tabpanel">
            

    <h4>General</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">The class of the entity</span>

    
        

        
        

        <br/>
<div class="badge badge-secondary">Examples:</div>
<br/><div id="type_allOf_i0_ex1" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Person&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex2" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Place&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex3" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;Type&quot;</span>
</pre></div>
</div><div id="type_allOf_i0_ex4" class="jumbotron examples"><div class="highlight"><pre><span></span><span class="s2">&quot;HumanMadeObject&quot;</span>
</pre></div>
</div>
        </div><div class="tab-pane fade card-body "
             id="tab-pane_died_type_allOf_i1" role="tabpanel">
            

    <h4>Specific</h4><span class="badge badge-dark value-type">Type: const</span><br/>
<span class="const-value" id="died_type_allOf_i1_const">Specific value: <code>"Death"</code></span>
        

        
        

        
        </div></div></div>
        

        
        

        
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied__label">
    <div class="card">
        <div class="card-header" id="headingdied__label">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died__label"
                        aria-expanded="" aria-controls="died__label" onclick="setAnchor('#died__label')"><span class="property-name">_label</span></button>
            </h2>
        </div>

        <div id="died__label"
             class="collapse property-definition-div" aria-labelledby="headingdied__label"
             data-parent="#accordiondied__label">
            <div class="card-body pl-5">

    <h4>rdfs:label</h4><span class="badge badge-dark value-type">Type: string</span><br/>
<span class="description">A human readable name or label for the entity, intended for developers</span><a href="#label" onclick="anchorLink('label')" class="ref-link">Same definition as _label</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied_identified_by">
    <div class="card">
        <div class="card-header" id="headingdied_identified_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_identified_by"
                        aria-expanded="" aria-controls="died_identified_by" onclick="setAnchor('#died_identified_by')"><span class="property-name">identified_by</span></button>
            </h2>
        </div>

        <div id="died_identified_by"
             class="collapse property-definition-div" aria-labelledby="headingdied_identified_by"
             data-parent="#accordiondied_identified_by">
            <div class="card-body pl-5">

    <h4>crm:P1_is_identified_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Name` or `Identifier` that identifies the entity</span><a href="#identified_by" onclick="anchorLink('identified_by')" class="ref-link">Same definition as identified_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied_classified_as">
    <div class="card">
        <div class="card-header" id="headingdied_classified_as">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_classified_as"
                        aria-expanded="" aria-controls="died_classified_as" onclick="setAnchor('#died_classified_as')"><span class="property-name">classified_as</span></button>
            </h2>
        </div>

        <div id="died_classified_as"
             class="collapse property-definition-div" aria-labelledby="headingdied_classified_as"
             data-parent="#accordiondied_classified_as">
            <div class="card-body pl-5">

    <h4>crm:P2_has_type</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Type` which classifies this entity beyond the class given in the `type` property</span><a href="#identified_by_items_anyOf_i0_referred_to_by_items_classified_as" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by_items_classified_as')" class="ref-link">Same definition as classified_as</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied_referred_to_by">
    <div class="card">
        <div class="card-header" id="headingdied_referred_to_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_referred_to_by"
                        aria-expanded="" aria-controls="died_referred_to_by" onclick="setAnchor('#died_referred_to_by')"><span class="property-name">referred_to_by</span></button>
            </h2>
        </div>

        <div id="died_referred_to_by"
             class="collapse property-definition-div" aria-labelledby="headingdied_referred_to_by"
             data-parent="#accordiondied_referred_to_by">
            <div class="card-body pl-5">

    <h4>crm:P67i_is_referred_to_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">An embedded statement about this entity, or a reference to a text that refers to the entity</span><a href="#identified_by_items_anyOf_i0_referred_to_by" onclick="anchorLink('identified_by_items_anyOf_i0_referred_to_by')" class="ref-link">Same definition as referred_to_by</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied_took_place_at">
    <div class="card">
        <div class="card-header" id="headingdied_took_place_at">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_took_place_at"
                        aria-expanded="" aria-controls="died_took_place_at" onclick="setAnchor('#died_took_place_at')"><span class="property-name">took_place_at</span></button>
            </h2>
        </div>

        <div id="died_took_place_at"
             class="collapse property-definition-div" aria-labelledby="headingdied_took_place_at"
             data-parent="#accordiondied_took_place_at">
            <div class="card-body pl-5">

    <h4>crm:P7_took_place_at</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A `Place` at which this event occured</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_took_place_at" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_took_place_at')" class="ref-link">Same definition as took_place_at</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied_timespan">
    <div class="card">
        <div class="card-header" id="headingdied_timespan">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_timespan"
                        aria-expanded="" aria-controls="died_timespan" onclick="setAnchor('#died_timespan')"><span class="property-name">timespan</span></button>
            </h2>
        </div>

        <div id="died_timespan"
             class="collapse property-definition-div" aria-labelledby="headingdied_timespan"
             data-parent="#accordiondied_timespan">
            <div class="card-body pl-5">

    <h4>crm:P4_has_time-span</h4><span class="badge badge-dark value-type">Type: object</span><br/>
<span class="description">A `TimeSpan` which describes the date-time range during which this event occured</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_timespan" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_timespan')" class="ref-link">Same definition as timespan</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied_during">
    <div class="card">
        <div class="card-header" id="headingdied_during">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_during"
                        aria-expanded="" aria-controls="died_during" onclick="setAnchor('#died_during')"><span class="property-name">during</span></button>
            </h2>
        </div>

        <div id="died_during"
             class="collapse property-definition-div" aria-labelledby="headingdied_during"
             data-parent="#accordiondied_during">
            <div class="card-body pl-5">

    <h4>crm:P10_falls_within</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A reference to a Period that the current temporal entity occurs during</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_during" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_during')" class="ref-link">Same definition as during</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied_after">
    <div class="card">
        <div class="card-header" id="headingdied_after">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_after"
                        aria-expanded="" aria-controls="died_after" onclick="setAnchor('#died_after')"><span class="property-name">after</span></button>
            </h2>
        </div>

        <div id="died_after"
             class="collapse property-definition-div" aria-labelledby="headingdied_after"
             data-parent="#accordiondied_after">
            <div class="card-body pl-5">

    <h4>crm:P183i_starts_after_the_end_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A Period, Event or Activity that the current Period, Event or Activity is after. (e.g. the referenced temporal entity is before the current one)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_after" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_after')" class="ref-link">Same definition as after</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied_before">
    <div class="card">
        <div class="card-header" id="headingdied_before">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_before"
                        aria-expanded="" aria-controls="died_before" onclick="setAnchor('#died_before')"><span class="property-name">before</span></button>
            </h2>
        </div>

        <div id="died_before"
             class="collapse property-definition-div" aria-labelledby="headingdied_before"
             data-parent="#accordiondied_before">
            <div class="card-body pl-5">

    <h4>crm:P183_ends_before_the_start_of</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">A Period, Event or Activity that the current Period, Event or Activity is before. (e.g. the referenced temporal entity is after the current one)</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_before" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_before')" class="ref-link">Same definition as before</a>
            </div>
        </div>
    </div>
</div>
<div class="accordion" id="accordiondied_caused_by">
    <div class="card">
        <div class="card-header" id="headingdied_caused_by">
            <h2 class="mb-0">
                <button class="btn btn-link property-name-button" type="button" data-toggle="collapse" data-target="#died_caused_by"
                        aria-expanded="" aria-controls="died_caused_by" onclick="setAnchor('#died_caused_by')"><span class="property-name">caused_by</span></button>
            </h2>
        </div>

        <div id="died_caused_by"
             class="collapse property-definition-div" aria-labelledby="headingdied_caused_by"
             data-parent="#accordiondied_caused_by">
            <div class="card-body pl-5">

    <h4>sci:O13i_is_triggered_by</h4><span class="badge badge-dark value-type">Type: array</span><br/>
<span class="description">Another event which caused this event to occur</span><a href="#identified_by_items_anyOf_i1_assigned_by_items_caused_by" onclick="anchorLink('identified_by_items_anyOf_i1_assigned_by_items_caused_by')" class="ref-link">Same definition as caused_by</a>
            </div>
        </div>
    </div>
</div>
            </div>
        </div>
    </div>
</div>

    <footer>
        <p class="generated-by-footer">Generated using <a href="https://github.com/coveooss/json-schema-for-humans">json-schema-for-humans</a> on 2024-12-17 at 15:54:05 -0500</p>
    </footer>