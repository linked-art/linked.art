
import re
from hyde.plugin import Plugin
import json, yaml
import os

from rdflib import ConjunctiveGraph, URIRef
from pyld.jsonld import expand, to_rdf, JsonLdProcessor, set_document_loader

import cromulent
from cromulent.model import factory, BaseResource, Production, Acquisition, Purchase, \
    Currency, Identifier, Person, TransferOfCustody, Identifier, VisualItem, \
    LinguisticObject, Right, OrderedDict, Appellation, BeginningOfExistence, \
    EndOfExistence, AttributeAssignment, Formation
from cromulent.vocab import Painting, InformationObject, Department, SupportPart, Type, \
	Auction, MuseumOrg, Place, Gallery, Activity, Actor, Group, MaterialStatement, \
	TimeSpan, ManMadeObject, MonetaryAmount, Curating, Inventorying, Provenance, \
	Attribution, Appraising, Dating, AuctionHouse, Auction, Bidding, AuctionCatalog, \
	LotNumber, Auctioneer, Bidding, AuctionLotSet, Theft, LocalNumber, AccessionNumber, \
	PrimaryAppellation, Sculpture, Description, Width, Height, DimensionStatement, \
	CreditStatement, RightsStatement, WebPage, PrimaryName, GivenName, FamilyName, \
	NamePrefix, NameSuffix, MiddleName, BiographyStatement, Nationality, Gender, \
	Exhibition, MuseumPlace, MultiExhibition, Naming, CollectionSet, StyleOfAttribution, \
	PhotographBW, PhotographColor, ProvenanceStatement, \
	materialTypes, dimensionUnits, add_art_setter
from cromulent.extra import PhysicalObject, Payment, EoEActivity, add_rdf_value, \
	add_schema_properties

ManMadeObject._uri_segment = "object"
Activity._uri_segment = "activity"
Place._uri_segment = "place"
InformationObject._uri_segment = "info"
Group._uri_segment = "group"
Actor._uri_segment = "actor"
Person._uri_segment = "person"
TimeSpan._uri_segment = "time"
Production._uri_segment = "activity"
Acquisition._uri_segment = "activity"
Purchase._uri_segment = "activity"
Payment._uri_segment = "activity"
MonetaryAmount._uri_segment = "money"
Currency._uri_segment = "money"
EoEActivity._uri_segment = "activity"
PhysicalObject._uri_segment = "object"
Identifier._uri_segment = "identifier"
TransferOfCustody._uri_segment = "activity"
LinguisticObject._uri_segment = "text"
Appellation._uri_segment = "name"
BeginningOfExistence._uri_segment = "event"
EndOfExistence._uri_segment = "event"
AttributeAssignment._uri_segment = "activity"

fh = file('site.yaml')
siteData = fh.read()
fh.close()
site = yaml.load(siteData)

scheme = site['var']['scheme']
port = site['var'].get('port', '')
host = site['var']['hostname']
if port:
	port = ":%s" % port

basedir = site['base_url']
egdir = site['var']['exampleDir']
baseUrl = "%s://%s%s%s%s/" % (scheme, host, port, basedir, egdir)
contextUrl = "%s://%s%s%sns/context/1/full.jsonld" % (scheme, host, port, basedir)

factory.base_url = baseUrl
factory.base_dir = "content/%s" % egdir
factory.context_uri = contextUrl
# Ensure it's still int per segment
factory.auto_id_type = "int-per-segment"
add_rdf_value()
add_schema_properties()
add_art_setter()

# Try to load in the context only once
fh = file('content/ns/context/1/full.jsonld')
data = fh.read()
fh.close()
ctxt = json.loads(data)['@context']

docCache = {}
docCache[factory.context_uri] = {'contextUrl': None,
	'documentUrl': None,
	'document': ctxt}

def fetch(url):
    fh = urllib.urlopen(url)
    data = fh.read()
    fh.close()
    return data    

def load_document_and_cache(url):
    if docCache.has_key(url):
        return docCache[url]

    doc = {
        'contextUrl': None,
        'documentUrl': None,
        'document': ''
    }
    data = fetch(url)
    doc['document'] = data;
    docCache[url] = doc
    return doc

set_document_loader(load_document_and_cache)

# And load up the AAT:Label mapping once
fh = file('extensions/aat_labels.json')
data = fh.read()
fh.close()
aat_labels = json.loads(data)

class IndexingPlugin(Plugin):

	def __init__(self, site):
		super(IndexingPlugin, self).__init__(site)
		self.index = {}		
		self.matcher = re.compile("^(```\s*crom\s*$(.+?)^```)$", re.M | re.U | re.S)

	def begin_site(self):
		self.index = {}
		self.aat_hash = {}
		self.prop_hash = {}
		self.class_hash = {}		

	def begin_text_resource(self, resource, text):
		if resource.relative_path.endswith('.html'):

			# It gets called three times, only the last one
			# actually does anything
			# No Idea why

			try:
				self.index[resource.relative_path] += 1
			except:
				self.index[resource.relative_path] = 1

			if self.index[resource.relative_path] != 3:
				return text

			# Look for ```crom ... ```
			hits = self.matcher.findall(text)
			for h in hits:
				try:
					eg = self.generate_example(h[1], resource)
				except Exception, e:
					print ">>> In %s" % resource.relative_path
					print "Caught Exception: %s" % e
					print "Failed to execute example:\n%s" % h[1]
					raise
				text = text.replace(h[0], eg)
		return text

	def site_complete(self):
		# Just write the document in markdown
		top = """---
extends: base.j2
default_block: content
title: Index of Classes, Properties, Authorities
---

{% include "toc.html" %}

"""
		lines = [top]

		lines.append("## Class Index")
		its = self.class_hash.items()
		its.sort()
		for (k,v) in its:
			lines.append("* __%s__" % k)
			lv= []
			for (k2,v2) in v.items():
				n = k2.replace('https://linked.art/example/', '')
				lv.append("[%s](/%s)" % (n, v2.relative_path + "#" + n.replace('/', '_')))			
			vstr = ' | '.join(lv)
			lines.append("    * %s" % vstr)

		lines.append("\n## Property Index")
		its = self.prop_hash.items()
		its.sort()
		for (k,v) in its:
			lines.append("* __%s__" % k)
			lv= []
			for (k2,v2) in v.items():
				n = k2.replace('https://linked.art/example/', '')
				lv.append("[%s](/%s)" % (n, v2.relative_path + "#" + n.replace('/', '_')))			
			vstr = ' | '.join(lv)
			lines.append("    * %s" % vstr)

		lines.append("\n## AAT Index")
		its = self.aat_hash.items()
		its.sort()		
		for (k,v) in its:
			if not k.startswith('aat:'):
				continue
			lines.append("* __%s__ (%s)" % (k, aat_labels.get(k, "???")))
			lv= []
			for (k2,v2) in v.items():
				n = k2.replace('https://linked.art/example/', '')				
				lv.append("[%s](/%s)" % (n, v2.relative_path + "#" + n.replace('/', '_')))
			vstr = ' | '.join(lv)
			lines.append("    * %s" % vstr)

		out = '\n'.join(lines)
		fh = file('content/model/example_index.html', 'w')
		fh.write(out)
		fh.close()


	def generate_example(self, egtext, resource):
		# Yes really... 
		exec(egtext) 

		# Now in scope should be a top resource
		factory.toFile(top, compact=False)
		jsstr = factory.toString(top, compact=False)
		js = factory.toJSON(top)

		# Generate all our serializations
		nq = to_rdf(js, {"format": "application/nquads"})
		g = ConjunctiveGraph()
		for ns in ['crm', 'dc', 'schema', 'dcterms', 'skos', 'foaf', 'pi']:
			g.bind(ns, ctxt[ns])
		g.parse(data=nq, format="nt")
		out = g.serialize(format="turtle")

		fp = js['id'][len(factory.base_url):]
		fp2 = fp + ".ttl"	
		fh = open(os.path.join(factory.base_dir, fp2), 'w')
		fh.write(out)
		fh.close()

		# Build index references
		self.traverse(js, top.id, resource)

		# And return the JSON plus links, to be substed by the top level filter
		raw = top.id + ".json"
		playground = "http://json-ld.org/playground/#startTab=tab-expanded&json-ld=%s" % raw
		turtle = top.id + ".ttl" 
		turtle_play = "http://cdn.rawgit.com/niklasl/ldtr/v0.2.2/demo/?edit=true&url=%s" % turtle 
		egid = fp.replace('/', '_')
		resp = """
<a id="%s"/>
```json
%s
```
[Raw](%s) | 
[Playground](%s) |
[Raw Turtle](%s) |
[Styled Turtle](%s)""" % (egid, jsstr, raw, playground, turtle, turtle_play)	
		return resp

	def traverse(self, what, top, res):
		for (k,v) in what.items():
			if k == 'type':
				which = "class_hash"
				nv = v
			elif k == 'classified_as':
				which = "aat_hash"
				nv = v
			elif k == 'id':
				if v.startswith('aat:'):
					which = "aat_hash"
					nv = v
				else:
					continue
			elif k == '@context':
				continue
			else:
				which = "prop_hash"			
				nv = k

			h = getattr(self, which)
			if type(nv) == list:
				for t in nv:
					if type(t) == dict or isinstance(t, OrderedDict):
						t = t['id']	
					try:
						h[t][top] = res
					except:
						h[t] = {top: res}
			else:	
				if type(nv) == dict or isinstance(nv, OrderedDict):
					nv = nv['id']
				try:
					h[nv][top] = res
				except:
					h[nv] = {top: res}

			# And now recurse
			if which == "prop_hash":
				if isinstance(v, OrderedDict):
					self.traverse(v, top, res)
				elif type(v) == list:
					for x in v:
						self.traverse(x, top, res)



### Global filters

def regex_replace(source, regex, replace):
	try:
		repl = re.compile(regex)
	except:
		print "ERROR: Failing regex: %s" % regex
		return source
	return repl.sub(replace, source)

def regex_replace_fn(source, regex, fnname):
	try:
		repl = re.compile(regex)
	except:
		print "ERROR: Failing regex: %s" % regex
		return source
	try:
		fn = globals()[fnname]
	except:
		print "ERROR: No such function '%s'" % fnname
	return repl.sub(fn, source)

def aatlabel(source):
	full = source.group(0)
	data = source.group(1)
	label = aat_labels.get(full, "")
	label = label.replace('"', '')
	return '<a href="http://vocab.getty.edu/aat/%s" data-ot="%s" data-ot-title="AAT Term" data-ot-fixed="true" class="aat">aat:%s</a>' % (data, label, data)


def ctxtrepl(source):
	full = source.group(0)
	data = source.group(1)
	if ctxt.has_key(data):
		if type(ctxt[data]) == dict:
			crm = ctxt[data]['@id']
		else:
			crm = ctxt[data]
		return '<abbr data-ot="%s" data-ot-title="Linked Data Term" data-ot-fixed="true">%s</abbr>' % (crm, full)
	else:
		return full
