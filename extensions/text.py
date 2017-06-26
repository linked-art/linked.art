
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
    EndOfExistence, AttributeAssignment
from cromulent.vocab import Painting, InformationObject, Department, SupportPart, Type, \
	Auction, MuseumOrg, Place, Gallery, Activity, Actor, Group, MaterialStatement, \
	TimeSpan, ManMadeObject, MonetaryAmount, Curating, Inventorying, Provenance, \
	Attribution, Appraising, Dating, AuctionHouse, Auction, Bidding, AuctionCatalog, \
	LotNumber, Auctioneer, Bidding, AuctionLotSet, Theft, LocalNumber, AccessionNumber, \
	PrimaryAppellation, Sculpture, Description, Width, Height, DimensionStatement, \
	CreditStatement, RightsStatement, WebPage, PrimaryName, GivenName, FamilyName, \
	NamePrefix, NameSuffix, MiddleName, BiographyStatement, Nationality, Gender, \
	Exhibition, MuseumPlace, MultiExhibition, Naming, CollectionSet, StyleOfAttribution, \
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
			if resource in self.index and text.find("crom") < 0:
				# Gets called multiple times, no idea why
				# print text.find("crom")
				return text
			self.index[resource] = {}
			# Look for ``` crom ... ```
			# and replace with {% syntax json %} ... {% endsyntax %}
			hits = self.matcher.findall(text)
			for h in hits:
				eg = self.generate_example(h[1])
				text = text.replace(h[0], eg)
		return text

	def site_complete(self):
		#print "site complete... building example index"
		#print self.index
		pass

	def generate_example(self, egtext):

		try:
			exec(egtext) 
		except:
			return "EXECUTION FAIL\n\n" + egtext

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

		fp = js['id'][len(factory.base_url):] + ".ttl"	
		fh = open(os.path.join(factory.base_dir, fp), 'w')
		fh.write(out)
		fh.close()

		# Build index references
		# traverse(js, top.id)

		# And return the JSON plus links, to be substed by the top level filter
		raw = top.id + ".json"
		playground = "http://json-ld.org/playground/#startTab=tab-expanded&json-ld=%s" % raw
		turtle = top.id + ".ttl" 
		turtle_play = "http://cdn.rawgit.com/niklasl/ldtr/v0.2.2/demo/?edit=true&url=%s" % turtle 
		resp = """
```json
%s
```
[Raw](%s) | 
[Playground](%s) |
[Raw Turtle](%s) |
[Styled Turtle](%s)""" % (jsstr, raw, playground, turtle, turtle_play)	
		return resp


def traverse(what, eg):
	for (k,v) in what.items():
		if k == 'type':
			if type(v) == list:
				for t in v:
					try:
						class_hash[t][eg] = 1
					except:
						class_hash[t] = {eg:1}
			else:
				try:
					class_hash[v][eg] = 1
				except:
					class_hash[v] = {eg:1}
		elif k  == 'classified_as':
			if type(v) == list:
				for t in v:
					if type(t) == dict or isinstance(t, OrderedDict):
						t = t['id']					
					try:
						aat_hash[t][eg] = 1
					except:
						aat_hash[t] = {eg:1}
			else:
				if type(v) == dict or isinstance(v, OrderedDict):
					v = v['id']
				try:
					aat_hash[v][eg] = 1
				except:
					aat_hash[v] = {eg:1}
		elif k in ['@context', 'id']:
			if v.startswith('aat:'):
				try:
					aat_hash[v][eg] = 1
				except:
					aat_hash[v] = {eg:1}				
		else:		
			try:
				prop_hash[k][eg] = 1
			except:
				prop_hash[k] = {eg:1}
			# And now recurse
			if isinstance(v, OrderedDict):
				traverse(v, eg)
			elif type(v) == list:
				for x in v:
					traverse(x, eg)


# Global filters

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
