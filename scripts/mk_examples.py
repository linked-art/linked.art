
import json
from cidoc_orm import factory, Production, Acquisition, Purchase, Currency
from vocab_mapping import Painting, InformationObject, Department, SupportPart, Type, \
	Auction, Museum, Place, Gallery, Activity, Actor, Group, MaterialStatement, \
	TimeSpan, ManMadeObject, Payment, MonetaryAmount, DestructionActivity, \
	Curating, Inventorying, materialTypes
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

### Make the identities auto-increment based on _uri_segment of the class
### Then expose all of the resources, not just the top level.


# Base - Parts - Example 1
mmo = Painting("1")
mmo.label = "Example Painting"
mmo.made_of = materialTypes['watercolor']
part = SupportPart(mmo.id + "/part/1")
part.label = "Canvas Support"
part.made_of = materialTypes['canvas']
mmo.part = part
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
ledger.composed_of = row
factory.toFile(ledger, compact=False)

# Example 5

museum = Museum("1")
museum.label = "Example Museum"
dept = Department(museum.id + "/part/1")
dept.label = "Paintings Department"
museum.current_or_former_member = dept
factory.toFile(museum, compact=False)

# Base - Statements

obj2 = Painting("2")
obj2.label = "Example Painting on Canvas"
lo = MaterialStatement(obj2.id + "/statement/1")
lo.value = "Oil on Canvas"
obj2.referred_to_by = lo
factory.toFile(obj2, compact=False)

obj2 = Painting("3")
obj2.label = "Example Painting"
factory.toFile(obj2, compact=False)

# Provenance - General Activity

act = Activity("2")
who = Actor("1")
who.label = "Who"
when = TimeSpan("1")
when.label = "When"
when.begin_of_the_begin = "earliest-start-datetime"
when.end_of_the_end = "latest-end-datetime"
where = Place("1")
where.label = "Where"
act.carried_out_by = who
act.took_place_at = where
act.timespan = when
factory.toFile(act, compact=False)

# Prov - Object Creation

act = Production("3")
who = Actor("1")
who.label = "Example Artist"
what = Painting("1")
what.label = "Example Painting"
when = TimeSpan("1")
where = Place("1")
where.label = "Example Artist's Studio"
when.begin_of_the_begin = "1780-03-05T00:00:00Z"
when.end_of_the_end = "1780-03-06T00:00:00Z"
act.carried_out_by = who
act.timespan = when
act.produced = what
act.took_place_at = where
factory.toFile(act, compact=False)

# Prov - Acquisition

act = Acquisition("4")
seller = Actor("1")
seller.label = "Seller"
buyer = Actor("2")
buyer.label = "Buyer"
when = TimeSpan("1")
when.label = "When"
when.begin_of_the_begin = "1890-01-04T00:00:00Z"
when.end_of_the_end = "1890-01-05T00:00:00Z"
act.timespan = when
where = Place("1")
where.label = "Art Gallery"
act.took_place_at = where
act.transferred_title_of = what
act.transferred_title_from = seller
act.transferred_title_to = buyer
factory.toFile(act, compact=False)

# Prov - Purchase

act = Purchase("5")
act.transferred_title_of = what
act.transferred_title_from = seller
act.transferred_title_to = buyer
paymt = Payment("6")
paymt.paid_from = buyer
paymt.paid_to = seller
amt = MonetaryAmount("1")
amt.value = 100
curr = Currency("2")
curr.label = "dollars"
amt.currency = curr
paymt.paid_amount = amt
act.consists_of = paymt
act.sales_price = amt
act.offering_price = amt
factory.toFile(act, compact=False)

# Prov - Loss

act = Acquisition("6")
what.label = "Example Lost Painting"
act.transferred_title_of = what
seller.label = "Previous Owner"
act.transferred_title_from = seller
when.label = None
act.timespan = when
factory.toFile(act, compact=False)

# Prov - Destruction

dest = DestructionActivity("7")
what.label = "Example Destroyed Painting"
dest.destroyed = what
dest.timespan = when
buyer.label = "Painting Destroyer"
dest.carried_out_by = buyer
factory.toFile(dest, compact=False)

# Prov - Curating and Inventorying

act = Curating("8")
act.label = "Looking After of the Painting"
start = Acquisition("9")
end = Acquisition("10")
inv = Inventorying("11")
inv.label = "Inventory Taking"
what = Painting("3")
what.label = "Painting"
owner = Actor("5")
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





# Auction - 



