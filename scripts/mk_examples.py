
import json
from cidoc_orm import factory
from vocab_mapping import Painting, InformationObject, Department, SupportPart, Type, \
	Auction, Museum, Place, Gallery, Activity, Group, materialTypes
import yaml

Painting._uri_segment = "object"
Auction._uri_segment = "activity"
Place._uri_segment = "place"
InformationObject._uri_segment = "infoObject"
Group._uri_segment = "group"

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

# Example 1
mmo = Painting("1")
mmo.label = "Example Painting"
mmo.made_of = materialTypes['watercolor']
part = SupportPart(mmo.id + "/part/1")
part.label = "Canvas Support"
part.made_of = materialTypes['canvas']
mmo.is_composed_of = part
factory.toFile(mmo, compact=False)

# Example 2
auc = Auction("1")
auc.label = "Example Auction"
lot = Activity(auc.id + "/part/1")
lot.label = "Example Auction of Lot"
auc.consists_of = lot
factory.toFile(auc, compact=False)

# Example 3

museum = Place("1")
museum.label = "Example Museum Building"
gallery = Gallery(museum.id + '/part/1')
gallery.label = "Gallery W204"
city = Place("http://vocab.getty.edu/tgn/7023900-place")
city.label = "Los Angeles"
museum.spatially_contains = gallery
museum.spatially_within = city
factory.toFile(museum, compact=False)

# Example 4

ledger = InformationObject("1")
ledger.label = "Content of Ledger 1"
row = InformationObject(ledger.id + "/part/1")
row.label = "Content of Row 1"
ledger.has_section = row
factory.toFile(ledger, compact=False)

# Example 5

museum = Museum("1")
museum.label = "Example Museum Institution"
dept = Department(museum.id + "/part/1")
dept.label = "Example Department"
museum.has_current_or_former_member = dept
factory.toFile(museum, compact=False)
