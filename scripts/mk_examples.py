
import json
from cidoc_orm import factory
from vocab_mapping import Painting, SupportPart, Auction, Activity, materialTypes
import yaml

Painting._uri_segment = "object"
Auction._uri_segment = "activity"

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



