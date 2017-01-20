
import json
from cromulent.model import factory, Production, Acquisition, Purchase, Currency, \
	Identifier, Person 
from cromulent.vocab import Painting, InformationObject, Department, SupportPart, Type, \
	Auction, MuseumOrg, Place, Gallery, Activity, Actor, Group, MaterialStatement, \
	TimeSpan, ManMadeObject, MonetaryAmount, Curating, Inventorying, Provenance, \
	Attribution, Appraising, Dating, AuctionHouse, Auction, Bidding, AuctionCatalog, \
	LotNumber, Auctioneer, Bidding, AuctionLotSet, \
	materialTypes
from cromulent.extra import PhysicalObject, Payment, DestructionActivity, add_rdf_value
import yaml

ManMadeObject._uri_segment = "object"
Activity._uri_segment = "activity"
Place._uri_segment = "place"
InformationObject._uri_segment = "infoObject"
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
DestructionActivity._uri_segment = "activity"
PhysicalObject._uri_segment = "object"
Identifier._uri_segment = "identifier"

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
id_uri_hash['base_type'] = eg

# Base - Parts - Example 1
mmo = Painting()
mmo.label = "Example Painting"
mmo.made_of = materialTypes['watercolor']
part = SupportPart(mmo.id + "/part/1")
part.label = "Canvas Support"
part.made_of = materialTypes['canvas']
mmo.part = part
id_uri_hash['base_parts_thing'] = mmo

# Example 2
auc = Auction()
auc.label = "Example Auction"
lot = Activity(auc.id + "/part/1")
lot.label = "Example Auction of Lot"
auc.consists_of = lot
id_uri_hash['base_parts_activity'] = auc

# Example 3
museum = Place()
museum.label = "Example Museum Building"
gallery = Gallery(museum.id + '/part/1')
gallery.label = "Gallery W204"
city = Place("http://vocab.getty.edu/tgn/7023900-place")
city.label = "Los Angeles"
museum.spatially_contains = gallery
museum.spatially_within = city
id_uri_hash['base_parts_place'] = museum

# Example 4
ledger = InformationObject()
ledger.label = "Content of Ledger 1"
row = InformationObject(ledger.id + "/part/1")
row.label = "Content of Row 1"
ledger.composed_of = row
id_uri_hash['base_parts_info'] = ledger

# Example 5
museum = MuseumOrg()
museum.label = "Example Museum Organization"
dept = Department(museum.id + "/part/1")
dept.label = "Paintings Department"
museum.current_or_former_member = dept
id_uri_hash['base_parts_org'] = museum

# Base - Statements
obj2 = Painting()
obj2.label = "Example Painting on Canvas"
lo = MaterialStatement(obj2.id + "/statement/1")
lo.value = "Oil on Canvas"
obj2.referred_to_by = lo
id_uri_hash['base_stmt'] = obj2

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
id_uri_hash['prov_event'] = act

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
id_uri_hash['prov_create'] = act

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
id_uri_hash['prov_acq'] = act

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
id_uri_hash['prov_purchase'] = act

# Prov - Loss
act = Acquisition()
what = Painting()
what.label = "Example Lost Painting"
act.transferred_title_of = what
who = Person()
who.label = "Previous Owner"
act.transferred_title_from = who
when = TimeSpan()
when.label = "Time noticed as Lost"
when.begin_of_the_begin = "1790-12-04T00:00:00Z"
when.end_of_the_end = "1790-12-05T00:00:00Z"
act.timespan = when
id_uri_hash['prov_loss'] = act

# Prov - Destruction
dest = DestructionActivity()
what = Painting()
what.label = "Example Destroyed Painting"
dest.destroyed = what
when = TimeSpan()
when.begin_of_the_begin = "1823-03-01T00:00:00Z"
when.end_of_the_end = "1823-03-31T00:00:00Z"
dest.timespan = when
who = Person()
who.label = "Painting Destroyer"
dest.carried_out_by = who
id_uri_hash['prov_dest'] = dest

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
what = Painting()
who = Person()
start.transferred_title_of = what
start.transferred_title_to = who
end.transferred_title_of = what
end.transferred_title_from = who
act.carried_out_by = who
act.used_specific_object = what
end.occurs_after = start
act.started_by = start
act.finished_by = end
act.consists_of = inv
id_uri_hash['prov_curate'] = act

# Full life time
act = Provenance()
what = Painting()
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
id_uri_hash['prov_lifetime'] = act

# Auction - Auction
auc = Auction()
auc.label = "Example Auction in London 1875-03-12,13"
h = AuctionHouse()
h.label = "Auction House, London"
auc.took_place_at = h
org = Group()
org.label = "Auction Company"
auc.carried_out_by = org
t = TimeSpan()
t.label = "12th and 13th of March, 1875"
t.begin_of_the_begin = "1875-03-12T00:00:00Z"
t.end_of_the_end = "1875-03-14T00:00:00Z"
auc.timespan = t
lot = Activity()
lot.label = "Auction of Lot 1"
auc.consists_of = lot
id_uri_hash["auction_base"] = auc

# Auction - Lot
lot = Activity()
lot.label = "Auction of Lot J-1823-5"
who = Auctioneer()
who.label = "Example Auctioneer"
lot.carried_out_by = who
lotset = AuctionLotSet()
lotset.label = "Set of Objects for Lot J-1823-5"
lot.used_specific_object = lotset
txn = Purchase()
txn.label = "Purchase of Lot"
lot.consists_of = txn
bidset = Activity()
bidset.label = "Bids made on Lot"
lot.consists_of = bidset
bidset.occurs_before = txn
id_uri_hash["auction_lot"] = lot

# Auction - LotSet
lotset = AuctionLotSet()
lotset.label = "Set of Objects for Lot 812"
ln = LotNumber()
ln.value = "812"
lotset.identified_by = ln
obj = Painting()
obj.label = "Example Painting"
lotset.part = obj
amnt = MonetaryAmount()
amnt.value = 500
amnt.currency = curr
amnt2 = MonetaryAmount()
amnt2.value = 4000
amnt2.currency = curr
lotset.starting_price = amnt
lotset.estimated_price = amnt2
id_uri_hash["auction_lotset"] = lotset

# Auction - Purchase
purch = Purchase()
purch.transferred_title_of = AuctionLotSet()
act = Purchase()
purch.consists_of = act
act.transferred_title_of = obj
act.transferred_title_from = seller
act.transferred_title_to = buyer
paymt = Payment()
paymt.paid_from = buyer
paymt.paid_to = seller
amt = MonetaryAmount()
amt.value = 4500
amt.currency = curr
paymt.paid_amount = amt
act.consists_of = paymt
act.sales_price = amt
act.offering_price = amt
id_uri_hash['auction_purchase'] = purch

prop_hash = {}
class_hash = {}

ym = []
for (v,what) in sorted(id_uri_hash.items()):
	factory.toFile(what, compact=False)
	ym.append("%s: %s" % (k, what.id.replace(baseUrl, '')))
	# Now walk the json of the objects and build an index


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
# a1 = Curating("1")
# a2 = Inventorying("2")
# a3 = Attribution("3")
# a4 = Dating("4")
# a5 = Appraising("6")

# what = Painting("1")
# what.label = "A Painting"
# who = Group("1")
# who.label = "Knoedler"

# a1.carried_out_by = who
# a1.used_specific_object = what
# a1.consists_of = a2
# a2.consists_of = a3
# a2.consists_of = a4
# a2.consists_of = a5

# a3.assigned_attribute_to = what
# a4.assigned_attribute_to = what
# a5.assigned_attribute_to = what

# artist = Actor("2")
# artist.label = "Artist"
# a3.assigned = artist

# ts = TimeSpan("1")
# ts.begin_of_the_begin = "1870-01-02"
# ts.end_of_the_end = "1870-01-04"
# a4.assigned = ts

# ma = MonetaryAmount("1")
# curr = Currency("2")
# curr.label = "dollars"
# ma.currency = curr
# ma.value = 1000
# a5.assigned = ma

#print factory.toString(a1, compact=False)
