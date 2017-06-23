
import re
from hyde.plugin import Plugin
import json, yaml

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

# And load up the AAT:Label mapping once
fh = file('extensions/aat_labels.json')
data = fh.read()
fh.close()
aat_labels = json.loads(data)

def exec_example(source):
	# {% filter exec_example -%}
	# ``` 
	# ...
	# ```
	# {%- endfilter %}
	print "CALLED EXEC EXAMPLE"
	try:
		lines = source.split('\n')
		if lines[0] != "```":
			return "START FAIL\n\n"+source
		if lines[-1] != "```":
			return "END FAIL\n\n" + source
		code = "\n".join(lines[1:-1])
		exec(code) 
	except:
		return "EXECUTION FAIL\n\n" + source
	# Now in scope should be a top resource
	factory.toFile(top, compact=False)
	js = factory.toString(top, compact=False)
	resp = """
```json
%s
```
""" % js
	return resp


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
