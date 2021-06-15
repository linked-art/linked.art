
from lxml import etree
import shutil

NS = {'rdf':"http://www.w3.org/1999/02/22-rdf-syntax-ns#",
	'xsd':"http://www.w3.org/2001/XMLSchema#",
	'rdfs':"http://www.w3.org/2000/01/rdf-schema#",
	'dcterms':"http://purl.org/dc/terms/",
	'owl':"http://www.w3.org/2002/07/owl#",
	'crm':"http://www.cidoc-crm.org/cidoc-crm/",
	'xml': "http://www.w3.org/XML/1998/namespace",
	'la': "https://linked.art/ns/terms/"
}

# Copy the full file out of model, into ns

fh = open('../content/ns/terms/index.xml')
data = fh.read()
fh.close()

try:
	dom = etree.XML(data)
except:
	data = data.encode('utf-8')
	dom = etree.XML(data)

out = """<rdf:RDF xml:lang="en" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xml:base="http://www.cidoc-crm.org/cidoc-crm/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:owl="http://www.w3.org/2002/07/owl#" xmlns:la="https://linked.art/ns/" xmlns:schema="http://schema.org/" xmlns:skos="http://www.w3.org/2004/02/skos/core#" xmlns:ore="http://www.openarchives.org/ore/terms/">

</rdf:RDF>"""


classes = dom.xpath("//rdfs:Class", namespaces=NS)
for c in classes:
	name = c.xpath('@rdf:about', namespaces=NS)[0]		
	name = name.replace(NS['la'], '')
	odom = etree.XML(out)
	odom.append(c)
	o = etree.tostring(odom, pretty_print=True).decode('utf-8')
	fh = open('../content/ns/terms/%s.xml' % name, 'w')
	fh.write(o)
	fh.close()

props = dom.xpath("//rdf:Property", namespaces=NS)
for p in props:
	name = p.xpath('@rdf:about', namespaces=NS)[0]		
	name = name.replace(NS['la'], '')
	odom = etree.XML(out)
	odom.append(p)
	o = etree.tostring(odom, pretty_print=True).decode('utf-8')
	fh = open('../content/ns/terms/%s.xml' % name, 'w')
	fh.write(o)
	fh.close()
