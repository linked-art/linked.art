
import re
from hyde.plugin import Plugin
from hyde.site import Resource
import json, yaml
import os
import requests
import urllib

from rdflib import ConjunctiveGraph, URIRef
from pyld.jsonld import expand, to_rdf, JsonLdProcessor, set_document_loader

import cromulent
from cromulent import model, vocab
from cromulent.model import factory, BaseResource, Production, Acquisition, \
    Currency, Identifier, Person, TransferOfCustody, Identifier, VisualItem, \
    LinguisticObject, OrderedDict, Appellation, \
    AttributeAssignment, Formation, Material, MeasurementUnit, \
    ManMadeFeature, Dimension, PhysicalObject, Name, Move, Language, Transformation, \
    PropertyInterest, Payment, Creation, Destruction, \
    PropositionalObject, Language, Geometry, CoordinateSystem, Phase, Birth, Death
from cromulent.vocab import Painting, InformationObject, Department, SupportPart, Type, \
	Auction, MuseumOrg, Place, Gallery, Activity, Actor, Group, MaterialStatement, \
	TimeSpan, ManMadeObject, MonetaryAmount, Curating, Inventorying, Provenance, \
	AuctionHouse, Auction, Bidding, AuctionCatalog, \
	LotNumber, Auctioneer, Bidding, AuctionLotSet, Theft, LocalNumber, AccessionNumber, \
	Sculpture, Description, Width, Height, DimensionStatement, Photograph, Negative, \
	CreditStatement, RightsStatement, WebPage, PrimaryName, GivenName, FamilyName, \
	NamePrefix, NameSuffix, MiddleName, BiographyStatement, Nationality, Gender, \
	Exhibition, MuseumPlace, MultiExhibition, CollectionSet, \
	PhotographBW, PhotographColor, ProvenanceStatement, Purchase, FramePart, GivenName, \
	DigitalImage, instances, add_art_setter, add_attribute_assignment_check


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
PhysicalObject._uri_segment = "object"
Identifier._uri_segment = "identifier"
TransferOfCustody._uri_segment = "activity"
Move._uri_segment = "activity"
LinguisticObject._uri_segment = "text"
Appellation._uri_segment = "name"
Name._uri_segment = "name"
AttributeAssignment._uri_segment = "activity"
Dimension._uri_segment = "value"
PropertyInterest._uri_segment = "legal"
PropositionalObject._uri_segment = "concept"  # For Exhibition concept and bid
Destruction._uri_segment = "activity"
Phase._uri_segment = "activity"
Birth._uri_segment = "activity"
Death._uri_segment = "activity"

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
contextUrl = "%s://%s%s%sns/v1/linked-art.json" % (scheme, host, port, basedir)

factory.base_url = baseUrl
factory.base_dir = "content/%s" % egdir
factory.context_uri = contextUrl
# Ensure it's still int per segment
factory.auto_id_type = "int-per-segment"
add_art_setter()
add_attribute_assignment_check()
factory.id_type_label = True

# Try to load in the context only once
ctxt = factory.context_json['@context']

# Profile definition
fn = os.path.join(os.path.dirname(cromulent.__file__), 'data')
fn += "/crm-profile.json"
fh = open(fn)
d = fh.read()
fh.close()
linked_art_profile = json.loads(d)


docCache = {}
docCache[factory.context_uri] = {'contextUrl': None,
	'documentUrl': None,
	'document': {"@context": ctxt}}

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

def fetch_aat_label(what):
	url = what.replace("aat:", "http://vocab.getty.edu/aat/")
	url += ".jsonld"
	try:
		resp = requests.get(url)
		aatjs = json.loads(resp.text)
	except:
		return ""
	prefs = aatjs[0]["http://www.w3.org/2004/02/skos/core#prefLabel"]
	label = ""
	for p in prefs:
		if p['@language'] in ['en', 'en-us']:
			label = p['@value']
			aat_labels[what] = label
			break
	return label

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
		self.aat_label_len = len(aat_labels)

	def begin_text_resource(self, resource, text):
		if resource.relative_path.endswith('.html'):

			# It gets called three times locally, only the last one
			# actually does anything
			# Weirder, it only gets called twice on netlify

			try:
				self.index[resource.relative_path] += 1
			except:
				self.index[resource.relative_path] = 1

			if self.index[resource.relative_path] != 2:
				return text

			# Look for ```crom ... ```
			hits = self.matcher.findall(text)
			for h in hits:
				try:
					eg = self.generate_example(h[1], resource)
				except Exception as e:
					print(">>> In %s" % resource.relative_path)
					print("Caught Exception: %s" % e)
					print("Failed to execute example:\n%s" % h[1])
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
			lines.append("* __`%s`__" % k)
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
			lines.append("* __`%s`__" % k)
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
			lines.append("* __%s__: _%s_" % (k, aat_labels.get(k) or fetch_aat_label(k)))
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
		# Annoyingly we need to generate this file separately

		# Check if we should re-cache aat_labels
		if len(aat_labels) > self.aat_label_len:
			outjs = json.dumps(aat_labels)
			fh = file('extensions/aat_labels.json', 'w')
			fh.write(outjs)
			fh.close()			

	def generate_example(self, egtext, resource):
		# Yes really... 
		exec(egtext) 

		# Now in scope should be a top resource
		factory.pipe_scoped_contexts = False
		factory.toFile(top, compact=False)

		factory.pipe_scoped_contexts = True
		jsstr = factory.toString(top, compact=False, collapse=80)
		factory.pipe_scoped_contexts = False

		js = factory.toJSON(top)
		# Generate all our serializations
		nq = to_rdf(js, {"format": "application/nquads"})
		g = ConjunctiveGraph()
		for ns in ['crm', 'dc', 'schema', 'dcterms', 'skos', 'la']:
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
		rawq = urllib.quote(raw).replace('/', "%2F")
		playground = "http://json-ld.org/playground-dev/#startTab=tab-expanded&copyContext=true&json-ld=%s" % rawq
		turtle = top.id + ".ttl" 
		turtle_play = "http://cdn.rawgit.com/niklasl/ldtr/v0.2.2/demo/?edit=true&url=%s" % turtle 
		egid = fp.replace('/', '_')
		resp = """
<a id="%s"></a>
```json
%s
```
[JSON-LD (Raw)](%s) | 
[JSON-LD (Playground)](%s) |
[Turtle (Raw)](%s) |
[Turtle (Styled)](%s)""" % (egid, jsstr, raw, playground, turtle, turtle_play)	
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
						if isinstance(x, OrderedDict):
							self.traverse(x, top, res)

### Global filters

def regex_replace(source, regex, replace):
	try:
		repl = re.compile(regex)
	except:
		print("ERROR: Failing regex: %s" % regex)
		return source
	return repl.sub(replace, source)

def regex_replace_fn(source, regex, fnname):
	try:
		repl = re.compile(regex)
	except:
		print("ERROR: Failing regex: %s" % regex)
		return source
	try:
		fn = globals()[fnname]
	except:
		print("ERROR: No such function '%s'" % fnname)
	return repl.sub(fn, source)

def aatlabel(source):
	full = source.group(0)
	data = source.group(1)
	label = aat_labels.get(full) or fetch_aat_label(full)
	label = label.replace('"', '')
	return '<a href="http://vocab.getty.edu/aat/%s" data-ot="%s" data-ot-title="AAT Term" data-ot-fixed="true" class="aat">aat:%s</a>' % (data, label, data)

def ctxtrepl(source):
	full = source.group(0)
	data = source.group(1)

	pidx = data.find("|")
	if pidx > -1:
		# Hack to include it in the serialization
		ttl = "Core Linked Data Term"
		col = ""
		crm = data[pidx+1:]
		full = full.replace("|%s" % crm, '')
	elif ctxt.has_key(data):
		# So it's CRM or added extension
		# get the full from 
		defn = ctxt[data]
		if not type(defn) == dict:
			# type --> @type
			crm = defn
			ttl = "Core Linked Data Term"
			col = ""
		else:
			crm = ctxt[data]['@id']
			term = crm.replace('crm:', '')
			if term in linked_art_profile:
				okay = linked_art_profile[term]
				if okay == 0 or (type(okay) == list and okay[0] == 0):
					ttl = "Extension Linked Data Term"
					col = 'style="color: orange"'				
				else:
					ttl = "Core Linked Data Term"
					col = ""
			else:
				return full
	else:
		return full

	val = '<abbr %s data-ot="%s" data-ot-title="%s" data-ot-fixed="true">%s</abbr>' % (col, crm, ttl, full)
	return val


