
import json
import yaml
import os

from rdflib import ConjunctiveGraph, URIRef
from pyld import jsonld
from pyld.jsonld import expand, to_rdf, JsonLdProcessor
import requests

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

fh = file('../site.yaml')
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
factory.base_dir = "../content/%s" % egdir
factory.context_uri = contextUrl
# Ensure it's still int per segment
factory.auto_id_type = "int-per-segment"
add_rdf_value()
add_schema_properties()
add_art_setter()

id_uri_hash = {}

page_hash = {"base": "model/base/index.html",
	"prov": "model/provenance/index.html",
	"provprod": "model/provenance/production.html",
	"provcur": "model/provenance/curation.html",
	"provacq": "model/provenance/acquisition.html",
	"auction": "model/provenance/auctions/index.html",
	"objid": "model/object/identity/index.html",
	"objabout": "model/object/aboutness/index.html",
	"objphys": "model/object/physical/index.html",
	"objrights": "model/object/rights/index.html",
	"objdig": "model/object/digital/index.html",
	"objprov": "model/object/provenance/index.html",
	"actor": "model/actor/index.html",
	"exh": "model/exhibition/index.html",
	"assert": "model/assertion/index.html"
	}

### First make the override table

lines = ["Property | Key", "-------- | ---"]
fn = os.path.join(cromulent.__path__[0], 'data', 'overrides.json')
fh = file(fn)
data = fh.read()
fh.close()
overs = json.loads(data)
its = overs.items()

def sorter(x):
	x = x[0]
	if x[-1] == "i":
		return int(x[1:-1]) + 0.5
	else:
		return int(x[1:])

its.sort(key=sorter)
for (k,v) in its:
	lines.append("%s | %s" % (k, v))

table = '\n'.join(lines)
fh = file('../content/_include/prop_key_map.md', 'w')
fh.write(table)
fh.close()

### Now make all the examples

### This one doesn't seem to be in the docs
# Prov - Sale of Stolen Object

act = TransferOfCustody()
act.label = "Sale of Stolen Object"
what = Painting(art=1)
what.label = "Example Stolen Painting"
act.transferred_custody_of = what
thief = Person()
thief.label = "Thief"
act.transferred_custody_from = thief
buyer = Person()
buyer.label = "Recipient"
act.transferred_custody_to = buyer
pay = Payment()
pay.paid_from = buyer
pay.paid_to = thief
amt = MonetaryAmount()
amt.value = 1000
curr = Currency()
curr.label = "dollars"
amt.currency = curr
pay.paid_amount = amt
act.consists_of = pay
id_uri_hash['provacq_theft_sale'] = act


# Joint Ownership


print ">>> Built examples "

# ------ Build out the examples -------

prop_hash = {}
class_hash = {}
aat_hash = {}

# Set up JSON-LD to TTL environment

docCache = {}

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

jsonld.set_document_loader(load_document_and_cache)

fh = file('../content/ns/context/1/full.jsonld')
ctxtdata = fh.read()
fh.close()
ctxtjs = json.loads(ctxtdata)
docCache[factory.context_uri] = {'contextUrl': None,
	'documentUrl': None,
	'document': ctxtdata}

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

ym = []
for (k,what) in sorted(id_uri_hash.items()):
	factory.toFile(what, compact=False)
	ym.append("%s: %s" % (k, what.id.replace(baseUrl, '')))
	# Now walk the json of the objects and build an index
	js = factory.toJSON(what)
	traverse(js, k)	
	# Now turn JSON-LD into TTL
	nq = to_rdf(js, {"format": "application/nquads"})
	g = ConjunctiveGraph()
	for ns in ['crm', 'dc', 'schema', 'dcterms', 'skos', 'foaf', 'pi']:
		g.bind(ns, ctxtjs['@context'][ns])
	g.parse(data=nq, format="nt")
	out = g.serialize(format="turtle")

	fp = js['id'][len(factory.base_url):] + ".ttl"	
	fh = open(os.path.join(factory.base_dir, fp), 'w')
	fh.write(out)
	fh.close()

def sorter(x):
	y = id_uri_hash[x].id
	return int(y[y.rfind('/')+1:])


# Consider using label of the top resource as label in index?
for d in [class_hash, prop_hash, aat_hash]:
	for (k,v) in d.items():
		n = []
		nks = v.keys()
		nks.sort(key=sorter)
		for nk in nks:
			what = id_uri_hash[nk]
			pg = page_hash[nk[:nk.find("_")]]
			n.append([pg, str(what.id.replace(baseUrl, '')), nk])
		d[k] = n

# Now build an index yaml structure, and iter through in the template
# Need to map page to the example id, and in page build <a name="eg"/> to #link to

idx = {'class_idx': sorted([list(x) for x in class_hash.items()]),
	'prop_idx': sorted([list(x) for x in prop_hash.items()]),
	'auth_idx': sorted([list(x) for x in aat_hash.items()])}

top = """---
extends: base.j2
default_block: content
title: Index of Classes, Properties, Authorities

"""
fh = file('../content/model/example_index.html', 'w')
fh.write(top)
fh.write(yaml.dump(idx))
fh.write('\n---\n\n{% include "_include/index_renderer.html" %}\n')
fh.close()

top = """extends: base.j2
default_block: content
level: top

example:
"""
fh = file('../content/model/meta.yaml', 'w')
fh.write(top)
for y in ym:
	fh.write("    %s.json\n" % y)
fh.close()


### And update aat_labels.json dict if needed

fh = file('../extensions/aat_labels.json')
data = fh.read()
fh.close()
aat_labels = json.loads(data)

write_aat_json = False
for k in aat_hash.keys():
	if not k in aat_labels and k.startswith('aat:'):
		# go fetch it as JSONLD
		url = k.replace("aat:", "http://vocab.getty.edu/aat/")
		url += ".jsonld"
		resp = requests.get(url)
		aatjs = json.loads(resp.text)
		prefs = aatjs[0]["http://www.w3.org/2004/02/skos/core#prefLabel"]
		for p in prefs:
			if p['@language'] in ['en', 'en-us']:
				label = p['@value']
				print "%s == %s" % (k, label)
				aat_labels[k] = label
				write_aat_json = True
				break

if write_aat_json:
	outjs = json.dumps(aat_labels)
	fh = file('../extensions/aat_labels.json', 'w')
	fh.write(outjs)
	fh.close()

print ">>> Wrote Indexes"
