
import json
import yaml
import os

import cromulent
from cromulent.model import factory, Production, Acquisition, Purchase, Currency, \
	Identifier, Person, TransferOfCustody 
from cromulent.vocab import Painting, InformationObject, Department, SupportPart, Type, \
	Auction, MuseumOrg, Place, Gallery, Activity, Actor, Group, MaterialStatement, \
	TimeSpan, ManMadeObject, MonetaryAmount, Curating, Inventorying, Provenance, \
	Attribution, Appraising, Dating, AuctionHouse, Auction, Bidding, AuctionCatalog, \
	LotNumber, Auctioneer, Bidding, AuctionLotSet, Theft, \
	materialTypes
from cromulent.extra import PhysicalObject, Payment, DestructionActivity, add_rdf_value

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
DestructionActivity._uri_segment = "activity"
PhysicalObject._uri_segment = "object"
Identifier._uri_segment = "identifier"
TransferOfCustody._uri_segment = "activity"

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

id_uri_hash = {}

page_hash = {"base": "model/base/index.html",
	"prov": "model/provenance/index.html",
	"auction": "model/provenance/auctions/index.html",
	"objid": "model/object/identity/index.html",
	"objabout": "model/object/aboutness/index.html",
	"objphys": "model/object/physical/index.html",
	"objrights": "model/object/rights/index.html",
	"objdig": "model/object/digital/index.html"
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
id_uri_hash['prov_purchase'] = act

# Prov - Loss
act = TransferOfCustody()
what = Painting()
what.label = "Example Lost Painting"
act.transferred_custody_of = what
who = Person()
who.label = "Previous Owner"
act.transferred_custody_from = who
when = TimeSpan()
when.label = "Time noticed as Lost"
when.begin_of_the_begin = "1790-12-04T00:00:00Z"
when.end_of_the_end = "1790-12-05T00:00:00Z"
act.timespan = when
id_uri_hash['prov_loss'] = act

# Prov - Theft
act = Theft()
act.label = "Theft of Painting"
what = Painting()
what.label = "Example Stolen Painting"
act.transferred_custody_of = what
who = Person()
who.label = "Owner"
act.transferred_custody_from = who
who = Person()
who.label = "Unknown Thief"
act.transferred_custody_to = who
when = TimeSpan()
when.label = "Time of Theft"
when.begin_of_the_begin = "1940-07-10T00:00:00Z"
when.end_of_the_end = "1940-07-11T00:00:00Z"
id_uri_hash['prov_theft'] = act

# Prov - Sale of Stolen Object

act = TransferOfCustody()
act.label = "Sale of Stolen Object"
what = Painting()
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
id_uri_hash['prov_theft_sale'] = act

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

# Joint Ownership



# Prov - Curating and Inventorying
act = Curating()
act.label = "Ownership of the Painting"
start = Acquisition()
start.label = "Acquisition of Painting by Owner"
end = Acquisition()
end.label = "Owner gives Painting to someone else"
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
start.occurs_before = end
act.continued = start
act.continued_by = end
id_uri_hash['prov_curate'] = act

act = Curating()
act.label = "Ownership of the Painting"
inv = Inventorying()
inv.label = "Inventory Taking by Owner"
act.consists_of = inv
id_uri_hash['prov_inventory'] = act

# Full life time
act = Provenance()
what = Painting()
act.label = "Lifetime of Painting"
act.used_specific_object = what
prod = Production()
prod.produced = what
own1 = Curating()
own1.label = "Ownership by Artist"
c1 = Acquisition()
c1.transferred_title_of = what
own2 = Curating()
own2.label = "Ownership by first owner"
c2 = Purchase()
c2.transferred_title_of = what
own3 = Curating()
own3.label = "Ownership by second and final owner"
dest = DestructionActivity()
dest.destroyed = what
act.consists_of = prod
act.consists_of = own1
act.consists_of = c1
act.consists_of = own2
act.consists_of = c2
act.consists_of = own3
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
id_uri_hash["auction_lotset"] = lotset

# Auction - Purchase
purch = Purchase()
als = AuctionLotSet()
als.label = "Set of Objects"
purch.used_specific_object = als 
act = Purchase()
purch.consists_of = act
act.transferred_title_of = obj
act.transferred_title_from = seller
act.transferred_title_to = buyer
id_uri_hash['auction_purchase'] = purch


# Auction - Price - Starting Price

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
amnt.classified_as = Type("http://data.getty.edu/money/type/startingPrice")
amnt2 = MonetaryAmount()
amnt2.value = 4000
amnt2.currency = curr
amnt2.classified_as = Type("http://data.getty.edu/money/type/estimatedPrice")
amnt3 = MonetaryAmount()
amnt3.value = 3000
amnt3.currency = curr
amnt3.classified_as = Type("http://data.getty.edu/money/type/reservePrice")
lotset.dimension = amnt
lotset.dimension = amnt2
lotset.dimension = amnt3
id_uri_hash['auction_prices'] = lotset


# Auction - Purchase
purch = Purchase()
als = AuctionLotSet()
als.label = "Set of Objects"
purch.used_specific_object = als 
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
purch.consists_of = paymt
id_uri_hash['auction_purchase_price'] = purch


# Auction - Catalog
catalog = AuctionCatalog()
catalog.label = "Auction Catalog of Example Auction"
entry = InformationObject()
entry.label = "Description of Lot 16"
catalog.composed_of = entry
auc = Auction()
auc.label = "Example Auction, 1924"
catalog.refers_to = auc
lot = Activity()
lot.label = "Auction of Lot 16"
entry.refers_to = lot
lotset = AuctionLotSet()
lotset.label = "Lot 16"
entry.refers_to = lotset
id_uri_hash['auction_catalog'] = catalog



# ------ Build out the examples -------

prop_hash = {}
class_hash = {}
aat_hash = {}

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
		elif k == 'classified_as':
			if type(v) == list:
				for t in v:
					try:
						aat_hash[t][eg] = 1
					except:
						aat_hash[t] = {eg:1}
			else:
				try:
					aat_hash[v][eg] = 1
				except:
					aat_hash[v] = {eg:1}
		elif k in ['@context', 'id']:
			# Not actually properties
			pass
		else:		
			try:
				prop_hash[k][eg] = 1
			except:
				prop_hash[k] = {eg:1}
			# And now recurse
			if type(v) == dict:
				traverse(v, eg)

ym = []
for (k,what) in sorted(id_uri_hash.items()):
	factory.toFile(what, compact=False)
	ym.append("%s: %s" % (k, what.id.replace(baseUrl, '')))
	# Now walk the json of the objects and build an index
	js = factory.toJSON(what)
	traverse(js, k)
	# XXX: Now turn JSON-LD into TTL
	# XXX: And link in the macro

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


