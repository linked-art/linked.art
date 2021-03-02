import re
from hyde.plugin import Plugin
from hyde.site import Resource
import json, yaml
import os
import requests
import urllib
import uuid
import sys

from rdflib import ConjunctiveGraph, URIRef
from pyld.jsonld import expand, to_rdf, JsonLdProcessor, set_document_loader

import cromulent
from cromulent import model, vocab
from cromulent.model import factory, OrderedDict
from cromulent.vocab import instances

model.HumanMadeObject._uri_segment = "object"
model.Activity._uri_segment = "activity"
model.Place._uri_segment = "place"
model.InformationObject._uri_segment = "info"
model.Group._uri_segment = "group"
model.Actor._uri_segment = "actor"
model.Person._uri_segment = "person"
model.TimeSpan._uri_segment = "time"
model.Production._uri_segment = "activity"
model.Acquisition._uri_segment = "activity"
model.Purchase._uri_segment = "activity"
model.Payment._uri_segment = "activity"
model.MonetaryAmount._uri_segment = "money"
model.Currency._uri_segment = "money"
model.PhysicalObject._uri_segment = "object"
model.Identifier._uri_segment = "identifier"
model.TransferOfCustody._uri_segment = "activity"
model.Move._uri_segment = "activity"
model.LinguisticObject._uri_segment = "text"
model.Appellation._uri_segment = "name"
model.Name._uri_segment = "name"
model.AttributeAssignment._uri_segment = "activity"
model.Dimension._uri_segment = "value"
model.PropositionalObject._uri_segment = "concept"  # For Exhibition concept and bid
model.Destruction._uri_segment = "activity"
model.Birth._uri_segment = "activity"
model.Death._uri_segment = "activity"
model.DigitalObject._uri_segment = "digital"
model.DigitalService._uri_segment = "digital"
model.Type._uri_segment = "concept"

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

# The vast majority of nodes should be blank nodes
# only the top node needs an id
# So use ident="auto int-per-segment" on top
factory.auto_assign_id = False
factory.auto_id_type = "int-per-segment"

vocab.add_art_setter()
vocab.add_attribute_assignment_check()
vocab.conceptual_only_parts()
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
		self.example_list = []
		self.class_styles = {
			"HumanMadeObject": "object",
			"Place": "place",
			"Actor": "actor",
			"Person": "actor",
			"Group": "actor",
			"Type": "type",
			"MeasurementUnit": "type",
			"Currency": "type",
			"Material": "type",
			"Language": "type",
			"Name": "name",
			"Identifier": "name",
			"Dimension": "dims",
			"MonetaryAmount": "dims",			
			"LinguisticObject": "infoobj",
			"VisualItem": "infoobj",
			"InformationObject": "infoobj",
			"Set": "infoobj",
			"PropositionalObject": "infoobj",
			"Right": "infoobj",
			"PropertyInterest": "infoobj",
			"TimeSpan": "timespan",
			"Activity": "event",
			"Event": "event",
			"Birth": "event",
			"Death": "event",
			"Production": "event",
			"Destruction": "event",
			"Creation": "event",
			"Formation": "event",
			"Dissolution": "event",
			"Acquisition": "event",
			"TransferOfCustody": "event",
			"Move": "event",
			"Payment": "event",
			"AttributeAssignment": "event",
			"Phase": "event",
			"RightAcquisition": "event",
			"PartRemoval": "event",
			"PartAddition": "event",
			"Encounter": "event",
			"DigitalObject": "digital",
			"DigitalService": "digital",
			"Addition": "event",
			"Removal": "event"
		}

	def begin_site(self):
		self.index = {}
		self.aat_hash = {}
		self.prop_hash = {}
		self.class_hash = {}		
		self.aat_label_len = len(aat_labels)

	def uri_to_label(self, uri):
		if uri.startswith('http://vocab.getty.edu/'):
			uri = uri.replace('http://vocab.getty.edu/', '')
			uri = uri.replace('/', '&colon;')
		elif uri.startswith('https://linked.art/example/'):
			uri = uri.replace('https://linked.art/example/', '')
			uri = uri.replace('/', '')
		elif uri.startswith('http://qudt.org/1.1/vocab/unit/'):
			uri = uri.replace('http://qudt.org/1.1/vocab/unit/', 'qudt:')
		else:
			print("Unhandled URI: %s" % uri)
		return uri

	def walk(self, js, curr_int, id_map, mermaid):
		if isinstance(js, dict):
			# Resource
			if 'id' in js:
				curr = js['id']
				lbl = self.uri_to_label(curr)
			else:
				curr = str(uuid.uuid4())
				lbl = " _ "
			if curr in id_map:
				currid = id_map[curr]
			else:
				currid = "O%s" % curr_int
				curr_int += 1
				id_map[curr] = currid
			line = "%s(%s)" % (currid, lbl)
			if not line in mermaid:
				mermaid.append(line)
			t = js.get('type', '')
			if t:
				style = self.class_styles.get(t, '')
				if style:
					line = "class %s %s;" % (currid, style)
					if not line in mermaid:
						mermaid.append("class %s %s;" % (currid, style))
				else:
					print("No style for class %s" % t)
				line = "%s-- type -->%s_0[%s]" % (currid, currid, t)
				if not line in mermaid:
					mermaid.append(line) 			
					mermaid.append("class %s_0 classstyle;" % currid)

			n = 0
			for k,v in js.items():
				n += 1
				if k in ["@context", "id", "type"]:
					continue
				elif isinstance(v, list):
					for vi in v:
						if isinstance(vi, dict):
							(rng, curr_int, id_map) = self.walk(vi, curr_int, id_map, mermaid)
							mermaid.append("%s-- %s -->%s" % (currid, k, rng))				
						else:
							print("Iterating a list and found %r" % vi)
				elif isinstance(v, dict):
					(rng, curr_int, id_map) = self.walk(v, curr_int, id_map, mermaid)
					line = "%s-- %s -->%s" % (currid, k, rng)
					if not line in mermaid:
						mermaid.append(line)				
				else:
					if type(v) in [str, unicode]:
						# :|
						v = v.replace('"', "&quot;")
						v = "\"''%s''\""% v
					line = "%s-- %s -->%s_%s(%s)" % (currid, k, currid, n, v)
					if not line in mermaid:
						mermaid.append(line)
						mermaid.append("class %s_%s literal;" % (currid, n))
			return (currid, curr_int, id_map)

	def build_mermaid(self, js):
		curr_int = 1
		mermaid = []
		id_map = {}
		mermaid.append("graph TD")
		mermaid.append("classDef object stroke:black,fill:#E1BA9C,rx:20px,ry:20px;")
		mermaid.append("classDef actor stroke:black,fill:#FFBDCA,rx:20px,ry:20px;")
		mermaid.append("classDef type stroke:red,fill:#FAB565,rx:20px,ry:20px;")
		mermaid.append("classDef name stroke:orange,fill:#FEF3BA,rx:20px,ry:20px;")
		mermaid.append("classDef dims stroke:black,fill:#c6c6c6,rx:20px,ry:20px;")
		mermaid.append("classDef infoobj stroke:#907010,fill:#fffa40,rx:20px,ry:20px")
		mermaid.append("classDef timespan stroke:blue,fill:#ddfffe,rx:20px,ry:20px")
		mermaid.append("classDef place stroke:#3a7a3a,fill:#aff090,rx:20px,ry:20px")
		mermaid.append("classDef event stroke:#1010FF,fill:#96e0f6,rx:20px,ry:20px")	
		mermaid.append("classDef literal stroke:black,fill:#f0f0e0;")
		mermaid.append("classDef classstyle stroke:black,fill:white;")
		self.walk(js, curr_int, id_map, mermaid)
		return "\n".join(mermaid)

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
				eg = self.generate_example(h[1], resource)
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

		# Create a simple list of the examples in /example/index.json
		if self.example_list:
			self.example_list.sort()
			listjs = json.dumps({"examples": self.example_list})
			fh = file('content/example/index.json', 'w')
			fh.write(listjs)
			fh.close()

	def generate_example(self, egtext, resource):
		# Yes really... 

		try:
			exec(egtext) 
		except Exception as e:
			print(">>> In %s" % resource.relative_path)
			print("Caught Exception from example code at %s: %r" % (sys.exc_info()[2].tb_lineno, e))
			print("Failed to execute example:\n%s" % h[1])
			return ""

		try:
			# Now in scope should be a top resource
			factory.pipe_scoped_contexts = False
			factory.toFile(top, compact=False)
			js = factory.toJSON(top)

			factory.pipe_scoped_contexts = True
			jsstr = factory.toHtml(top)
			factory.pipe_scoped_contexts = False

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
		except Exception as e:
			print(">>> In %s" % resource.relative_path)
			print("Caught Exception from serialization code at %s: %r" % (sys.exc_info()[2].tb_lineno, e))
			print("Failed to execute example:\n%s" % h[1])
			return ""

		try:
			# And build mermaid description
			mermaid = self.build_mermaid(js)
			# Build index references
			self.traverse(js, top.id, resource)
		except Exception as e:
			print(">>> In %s" % resource.relative_path)
			print("Caught Exception from mermaid/indexing code at %s: %r" % (sys.exc_info()[2].tb_lineno, e))
			print("Failed to execute example:\n%s" % h[1])
			return ""			

		# And return the JSON plus links, to be substed by the top level filter
		raw = top.id
		jsuri = raw + ".json"
		self.example_list.append(raw)
		rawq = urllib.quote(raw).replace('/', "%2F")
		playground = "http://json-ld.org/playground-dev/#startTab=tab-expanded&copyContext=true&json-ld=%s" % rawq
		turtle = raw + ".ttl" 
		turtle_play = "http://cdn.rawgit.com/niklasl/ldtr/v0.2.2/demo/?edit=true&url=%s" % turtle 
		egid = fp.replace('/', '_')
		mmid = self.uri_to_label(raw)
		resp = """
<a id="%s"></a>
<div class="jsonld">
%s
<div>
<div class="mermaid" id="mermaid_%s">
%s
</div>
<div id="mermaid_%s_svg"></div>
Other Representations: [JSON-LD (Raw)](%s) | 
[JSON-LD (Playground)](%s) |
[Turtle (Raw)](%s) |
[Turtle (Styled)](%s)


""" % (egid, jsstr, mmid, mermaid, mmid, raw, playground, turtle, turtle_play)	
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
	try:
		data = source.group(2)
	except:
		data = full

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


