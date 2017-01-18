
import json
from cromulent.model import factory, Production, Acquisition, Purchase, Currency
from cromulent.vocab import Painting, InformationObject, Department, SupportPart, Type, \
	Auction, MuseumOrg, Place, Gallery, Activity, Actor, Group, MaterialStatement, \
	TimeSpan, ManMadeObject, MonetaryAmount, Curating, Inventorying, Provenance, \
	Attribution, Appraising, Dating, AuctionHouse, Auction, Bidding, AuctionCatalog, \
	LotNumber, \
	materialTypes
from cromulent.extra import Payment, DestructionActivity, add_rdf_value
import yaml

ManMadeObject._uri_segment = "object"
Activity._uri_segment = "activity"
Place._uri_segment = "place"
InformationObject._uri_segment = "infoObject"
Group._uri_segment = "group"
Actor._uri_segment = "actor"
TimeSpan._uri_segment = "time"
Production._uri_segment = "activity"
Acquisition._uri_segment = "activity"
Purchase._uri_segment = "activity"
Payment._uri_segment = "activity"
MonetaryAmount._uri_segment = "money"
Currency._uri_segment = "money"
DestructionActivity._uri_segment = "activity"

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

add_rdf_value()

id_uri_hash = {}

### Make the identities auto-increment based on _uri_segment of the class
### Then expose all of the resources, not just the top level.

# Base - Type
eg = Painting()
eg.label = "Simple Example Painting"
factory.toFile(eg, compact=False)
id_uri_hash['base_type'] = eg.id.replace(baseUrl, '')

# Base - Parts - Example 1
mmo = Painting()
mmo.label = "Example Painting"
mmo.made_of = materialTypes['watercolor']
part = SupportPart(mmo.id + "/part/1")
part.label = "Canvas Support"
part.made_of = materialTypes['canvas']
mmo.part = part
factory.toFile(mmo, compact=False)
id_uri_hash['base_parts_thing'] = mmo.id.replace(baseUrl, '')


# Example 2
auc = Auction()
auc.label = "Example Auction"
lot = Activity(auc.id + "/part/1")
lot.label = "Example Auction of Lot"
auc.consists_of = lot
factory.toFile(auc, compact=False)
id_uri_hash['base_parts_activity'] = auc.id.replace(baseUrl, '')

# Example 3

museum = Place()
museum.label = "Example Museum Building"
gallery = Gallery(museum.id + '/part/1')
gallery.label = "Gallery W204"
city = Place("http://vocab.getty.edu/tgn/7023900-place")
city.label = "Los Angeles"
museum.spatially_contains = gallery
museum.spatially_within = city
factory.toFile(museum, compact=False)
id_uri_hash['base_parts_place'] = museum.id.replace(baseUrl, '')

# Example 4

ledger = InformationObject()
ledger.label = "Content of Ledger 1"
row = InformationObject(ledger.id + "/part/1")
row.label = "Content of Row 1"
ledger.composed_of = row
factory.toFile(ledger, compact=False)
id_uri_hash['base_parts_info'] = ledger.id.replace(baseUrl, '')

# Example 5

museum = MuseumOrg()
museum.label = "Example Museum Organization"
dept = Department(museum.id + "/part/1")
dept.label = "Paintings Department"
museum.current_or_former_member = dept
factory.toFile(museum, compact=False)
id_uri_hash['base_parts_org'] = museum.id.replace(baseUrl, '')

# Base - Statements

obj2 = Painting()
obj2.label = "Example Painting on Canvas"
lo = MaterialStatement(obj2.id + "/statement/1")
lo.value = "Oil on Canvas"
obj2.referred_to_by = lo
factory.toFile(obj2, compact=False)
id_uri_hash['base_stmt'] = obj2.id.replace(baseUrl, '')

# Provenance - General Activity

act = Activity()
who = Actor()
who.label = "Who"
when = TimeSpan()
when.label = "When"
when.begin_of_the_begin = "earliest-start-datetime"
when.end_of_the_end = "latest-end-datetime"
where = Place()
where.label = "Where"
act.carried_out_by = who
act.took_place_at = where
act.timespan = when
factory.toFile(act, compact=False)
id_uri_hash['prov_event'] = act.id.replace(baseUrl, '')

# Prov - Object Creation

act = Production()
who = Actor()
who.label = "Example Artist"
what = Painting()
what.label = "Example Painting"
when = TimeSpan()
where = Place()
where.label = "Example Artist's Studio"
when.begin_of_the_begin = "1780-03-05T00:00:00Z"
when.end_of_the_end = "1780-03-06T00:00:00Z"
act.carried_out_by = who
act.timespan = when
act.produced = what
act.took_place_at = where
factory.toFile(act, compact=False)
id_uri_hash['prov_create'] = act.id.replace(baseUrl, '')

# Prov - Acquisition

act = Acquisition()
seller = Actor()
seller.label = "Seller"
buyer = Actor()
buyer.label = "Buyer"
when = TimeSpan()
when.label = "When"
when.begin_of_the_begin = "1890-01-04T00:00:00Z"
when.end_of_the_end = "1890-01-05T00:00:00Z"
act.timespan = when
where = Place()
where.label = "Art Gallery"
act.took_place_at = where
act.transferred_title_of = what
act.transferred_title_from = seller
act.transferred_title_to = buyer
factory.toFile(act, compact=False)
id_uri_hash['prov_acq'] = act.id.replace(baseUrl, '')

# Prov - Purchase

act = Purchase()
act.transferred_title_of = what
act.transferred_title_from = seller
act.transferred_title_to = buyer
paymt = Payment()
paymt.paid_from = buyer
paymt.paid_to = seller
amt = MonetaryAmount()
amt.value = 100
curr = Currency()
curr.label = "dollars"
amt.currency = curr
paymt.paid_amount = amt
act.consists_of = paymt
act.sales_price = amt
act.offering_price = amt
factory.toFile(act, compact=False)
id_uri_hash['prov_purchase'] = act.id.replace(baseUrl, '')

# Prov - Loss

act = Acquisition()
what.label = "Example Lost Painting"
act.transferred_title_of = what
seller.label = "Previous Owner"
act.transferred_title_from = seller
when.label = None
act.timespan = when
factory.toFile(act, compact=False)
id_uri_hash['prov_loss'] = act.id.replace(baseUrl, '')

# Prov - Destruction

dest = DestructionActivity()
what.label = "Example Destroyed Painting"
dest.destroyed = what
dest.timespan = when
buyer.label = "Painting Destroyer"
dest.carried_out_by = buyer
factory.toFile(dest, compact=False)
id_uri_hash['prov_dest'] = dest.id.replace(baseUrl, '')

# Prov - Curating and Inventorying

act = Curating()
act.label = "Looking After of the Painting"
start = Acquisition()
start.label = "Acquisition of Painting by Owner"
end = Acquisition()
end.label = "Owner gives Painting to someone else"
inv = Inventorying()
inv.label = "Inventory Taking by Owner"
owner = Actor()
owner.label = "Owner"

start.transferred_title_of = what
start.transferred_title_to = owner
end.transferred_title_of = what
end.transferred_title_from = owner
act.carried_out_by = owner
act.used_specific_object = what

end.occurs_after = start
act.started_by = start
act.finished_by = end
act.consists_of = inv
factory.toFile(act, compact=False)
id_uri_hash['prov_curate'] = act.id.replace(baseUrl, '')

# Full life time
act = Provenance()
act.label = "Provenance of Painting"
act.used_specific_object = what
prod = Production()
prod.produced = what
c1 = Acquisition()
c1.transferred_title_of = what
c2 = Purchase()
c2.transferred_title_of = what
dest = DestructionActivity()
dest.destroyed = what
act.consists_of = prod
act.consists_of = c1
act.consists_of = c2
act.consists_of = dest
factory.toFile(act, compact=False)
id_uri_hash['prov_lifetime'] = act.id.replace(baseUrl, '')

# Auction - Auction

auc = Auction()
auc.label = "Auction in London 1875-03-12,13"
h = AuctionHouse()
h.label = "Auction House, London"
auc.took_place_at = h
org = Group()
auc.carried_out_by = org
t = TimeSpan()
t.begin_of_the_begin = "1875-03-12T00:00:00Z"
t.end_of_the_end = "1875-03-14T00:00:00Z"
auc.timespan = t
factory.toFile(auc, compact=False)
id_uri_hash["auction_base"] = auc.id.replace(baseUrl, '')


ym = []
for (k,v) in sorted(id_uri_hash.items()):
	ym.append("%s: %s" % (k,v))


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


# ---------

# Attribute Assignment
a1 = Curating("1")
a2 = Inventorying("2")
a3 = Attribution("3")
a4 = Dating("4")
a5 = Appraising("6")

what = Painting("1")
what.label = "A Painting"
who = Group("1")
who.label = "Knoedler"

a1.carried_out_by = who
a1.used_specific_object = what
a1.consists_of = a2
a2.consists_of = a3
a2.consists_of = a4
a2.consists_of = a5

a3.assigned_attribute_to = what
a4.assigned_attribute_to = what
a5.assigned_attribute_to = what

artist = Actor("2")
artist.label = "Artist"
a3.assigned = artist

ts = TimeSpan("1")
ts.begin_of_the_begin = "1870-01-02"
ts.end_of_the_end = "1870-01-04"
a4.assigned = ts

ma = MonetaryAmount("1")
curr = Currency("2")
curr.label = "dollars"
ma.currency = curr
ma.value = 1000
a5.assigned = ma

#print factory.toString(a1, compact=False)
