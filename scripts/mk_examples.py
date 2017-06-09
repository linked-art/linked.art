
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
    EndOfExistence, AttributeAssignment
from cromulent.vocab import Painting, InformationObject, Department, SupportPart, Type, \
	Auction, MuseumOrg, Place, Gallery, Activity, Actor, Group, MaterialStatement, \
	TimeSpan, ManMadeObject, MonetaryAmount, Curating, Inventorying, Provenance, \
	Attribution, Appraising, Dating, AuctionHouse, Auction, Bidding, AuctionCatalog, \
	LotNumber, Auctioneer, Bidding, AuctionLotSet, Theft, LocalNumber, AccessionNumber, \
	PrimaryAppellation, Sculpture, Description, Width, Height, DimensionStatement, \
	CreditStatement, RightsStatement, WebPage, PrimaryName, GivenName, FamilyName, \
	NamePrefix, NameSuffix, MiddleName, BiographyStatement, Nationality, Gender, \
	Exhibition, MuseumPlace, MultiExhibition, Naming, CollectionSet, \
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
	"auction": "model/provenance/auctions/index.html",
	"objid": "model/object/identity/index.html",
	"objabout": "model/object/aboutness/index.html",
	"objphys": "model/object/physical/index.html",
	"objrights": "model/object/rights/index.html",
	"objdig": "model/object/digital/index.html",
	"objprov": "model/object/provenance/index.html",
	"actor": "model/actor/index.html",
	"exh": "model/exhibition/index.html"
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
eg = Painting(art=1)
eg.label = "Simple Example Painting"
id_uri_hash['base_type'] = eg

# Base - Parts - Example 1
mmo = Painting(art=1)
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
museum.member = dept
id_uri_hash['base_parts_org'] = museum

# Base - Statements
obj2 = Painting(art=1)
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
what = Painting(art=1)
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


act = Production()
who = Actor()
who.label = "Example Glassblower"
what = Sculpture(art=1)
what.label = "Glass Sculpture"
act.carried_out_by = who
act.classified_as = Type("http://vocab.getty.edu/aat/300053932")
id_uri_hash['prov_create_technique'] = act

topact = Production()
what = Sculpture(art=1)
what.label = "Painted Sculpture"
topact.produced = what
act1 = Activity()
act1.classified_as = Type("http://vocab.getty.edu/aat/300264383")
who = Actor()
who.label = "Example Sculptor"
act1.carried_out_by = who
topact.consists_of = act1
act2 = Activity()
who2 = Actor()
who2.label = "Example Sculpture Painter"
act2.classified_as = Type("http://vocab.getty.edu/aat/300161986")
act2.carried_out_by = who2
topact.consists_of = act2
id_uri_hash['prov_create_roles'] = topact



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
what = Painting(art=1)
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
what = Painting(art=1)
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
id_uri_hash['prov_theft_sale'] = act

# Prov - Destruction
dest = EoEActivity()
what = Painting(art=1)
what.label = "Example Destroyed Painting"
dest.took_out_of_existence = what
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
what = Painting(art=1)
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
what = Painting(art=1)
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
dest = EoEActivity()
dest.took_out_of_existence = what
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
obj = Painting(art=1)
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

what = Painting(art=1)
what.label = "Example Painting"
id1 = AccessionNumber()
id1.label = "Accession Number for Painting"
id1.value = "X198-093"
what.identified_by = id1
id2 = LocalNumber()
id2.value = 677
id2.label = "Local Repository Number"
what.identified_by = id2
id_uri_hash['objid_legacy'] = what


# Legacy Identifiers with Collections

what = Painting(art=1)
what.label = "Example Painting"
id1 = AccessionNumber()
id1.value = "P1998-27"
what.identified_by = id1

idset = InformationObject()
idset.label = "Paintings Collection Identifiers"
id1.composed_from = idset

coll = CollectionSet()
coll.label = "Paintings Collection"
idset.refers_to = coll
coll.part = what
id_uri_hash['objid_linkcoll'] = what

what = Painting(art=1)
what.label = "Peasant and Sheep"
ttl = PrimaryAppellation()
ttl.value = "Peasant and Sheep"
what.identified_by = ttl
id_uri_hash['objid_title'] = what

what = Painting(art=1)
what.label = "Self Portrait"
ttl = PrimaryAppellation()
ttl.value = "Self Portrait"
what.identified_by = ttl
ttl2 = Appellation()
ttl2.value = "Portrait of the Artist"
what.identified_by = ttl2
id_uri_hash['objid_title_alt'] = what

what = Sculpture(art=1)
what.label = "Sculpture of a Dragon"
id_uri_hash['objid_types'] = what

what = Painting(art=1)
what.label = "Example Painting"
what.description = "The Example Painting is a great example of exampleness."
desc = Description()
desc.value = "The Example Painting is a great example of exampleness."
what.referred_to_by = desc
id_uri_hash['objabout_description'] = what

what = Painting(art=1)
what.label = "Another Example Painting"
p2 = Painting(art=1)
p2.label = "Yet Another Example Painting"
what.related = p2
id_uri_hash['objabout_related'] = what

what = Painting(art=1)
what.label = "Self Portrait"
who = Actor()
who.label = "Artist"
what.depicts = who 
prd = Production()
prd.carried_out_by = who
what.produced_by = prd
id_uri_hash['objabout_depicts'] = what

what = Painting(art=1)
what.label = "Portrait of Lord Nelson"
concept = Type("http://vocab.getty.edu/aat/300055314")
concept.label = "War"
what.subject = concept  # dct:subject
id_uri_hash['objabout_subject'] = what

what = Painting(art=1)
what.label = "Example Impressionist Painting"
what.style = Type("http://vocab.getty.edu/aat/300021503")
id_uri_hash['objabout_style'] = what

what = Painting(art=1)
what.label = "Example 16x20 Painting"
w = Width()
w.value = 16
w.unit = dimensionUnits['inches']
what.dimension = w
h = Height()
h.value = 20
h.unit = dimensionUnits['inches']
what.dimension = h
id_uri_hash['objphys_dims'] = what

what = Painting(art=1)
what.label = "Example Painting"
dims = DimensionStatement()
dims.value = "The painting is approximately 16 inches wide, by 20 inches high"
what.referred_to_by = dims
id_uri_hash['objphys_dims_stmt'] = what

what = Sculpture(art=1)
what.label = "Example Marble Sculpture"
what.made_of = materialTypes['marble']
id_uri_hash['objphys_materials'] = what

what = Painting(art=1)
what.label = "Example Multi-Media Painting"
mats = MaterialStatement()
mats.value = "Oil, French Watercolors on Paper, Graphite and Ink on Canvas, with an Oak frame"
what.referred_to_by = mats
id_uri_hash['objphys_materials_stmt'] = what

what = Painting(art=1)
what.label = "Example Painting"
crdt = CreditStatement()
crdt.value = "Donation of Ms J. Smith; Example Organization"
what.referred_to_by = crdt
id_uri_hash['objrights_credit'] = what

what = Painting(art=1)
what.label = "Example Painting"
crdt = RightsStatement()
crdt.value = "Copyright of this object has not yet been assessed"
what.referred_to_by = crdt
id_uri_hash['objrights_rights_stmt'] = what


# This is kind of wacky, but it's what we've got

what = Painting(art=1)
what.label = "Example Painting"
copyright = Right()
copyright.classified_as = Type("http://rightsstatements.org/vocab/InC/1.0/")
copyright.label = "Copyright of Example Painting's content"
what.subject_to = copyright
cholder = Actor()
cholder.label = "Copyright Holder"
copyright.possessed_by = cholder
id_uri_hash['objrights_rights'] = what

what = Painting(art=1)
what.label = "Object"
cne = Right()
cne.classified_as = Type("http://rightsstatements.org/vocab/NKC/1.0/")
cne.label = "No known copyright"
what.subject_to = cne
id_uri_hash['objrights_nkc'] = what

# Digital

what = Painting(art=1)
what.label = "Painting"
img = VisualItem("http://example.org/images/image.jpg")
img.label = "Image of Painting"
img.format = "image/jpeg"
what.representation = img
id_uri_hash['objdig_image'] = what

what = Painting(art=1)
what.label = "Painting"
page = WebPage("http://example.org/collection/1/painting")
page.classified_as = Type("aat:300404670")
page.label = "Homepage for Painting"
page.format = "text/html"
what.subject_of = page
id_uri_hash['objdig_homepage'] = what

what = Painting(art=1)
what.label = "Painting"
page = WebPage("http://example.org/journal/article")
page.label = "Webpage that discusses Painting"
page.format = "text/html"
what.subject_of = page
id_uri_hash['objdig_page'] = what

what = Sculpture(art=1)
what.label = "Sculpture"
img = VisualItem("http://iiif.example.org/image/1")
img.label = "IIIF Image API for Sculpture"
img.conforms_to = BaseResource("http://iiif.io/api/image")
what.representation = img
id_uri_hash['objdig_iiif_image'] = what

what = Painting(art=1)
what.label = "Painting"
mfst = InformationObject("http://iiif.example.org/presentation/1/manifest.json")
mfst.format = 'application/ld+json;profile="http://iiif.io/api/presentation/2/context.json"'
mfst.conforms_to = BaseResource("http://iiif.io/api/presentation")
what.subject_of = mfst
id_uri_hash['objdig_iiif_manifest'] = what

what = Painting(art=1)
what.label = "Painting"
prod = Production()
prod.label = "Production of Painting"
who = Person()
who.label = "Artist"
prod.carried_out_by = who
what.produced_by = prod
id_uri_hash['objprov_production'] = what

what = Painting(art=1)
what.label = "Painting"
who = MuseumOrg()
who.label = "Museum"
what.current_owner = who
acq = Acquisition()
who.acquired_title_through = acq
id_uri_hash['objprov_owner'] = what

what = Painting(art=1)
what.label = "Painting"
where = Place()
where.label = "Gallery W6"
what.current_location = where
id_uri_hash['objprov_location'] = what

### Actors

who = Person()
who.label = "J. Smith"
grp = MuseumOrg()
grp.label = "Example Museum Organization"
actor = Actor()
actor.label = "Unknown Person or Organization"
acq = Acquisition()
acq.transferred_title_from = who
acq.transferred_title_to = grp
acq.carried_out_by = actor
id_uri_hash['actor_type'] = acq

who = Person()
who.label = "J. Smith"
apl = PrimaryName()
apl.value = "J. Smith"
who.identified_by = apl
id_uri_hash['actor_name'] = who

who = Person()
who.label = "Lady Joan A. Smith, Duchess of Wolverhampton"
apl = PrimaryName()
apl.value = "Lady Joan A. Smith, Duchess of Wolverhampton"
who.identified_by = apl
given = GivenName()
given.value = "Joan"
fam = FamilyName()
fam.value = "Smith"
pref = NamePrefix()
pref.value = "Lady"
suff = NameSuffix()
suff.value = "Duchess of Wolverhampton"
mid = MiddleName()
mid.value = "A."
apl.composed_of = pref
apl.composed_of = given
apl.composed_of = mid
apl.composed_of = fam
apl.composed_of = suff
id_uri_hash['actor_name_parts'] = who

who = Person()
who.label = "Xavier Y. Zeelander"
pid = LocalNumber()
pid.value = 643
who.identified_by = pid
id_uri_hash['actor_identity'] = who

who = Person()
who.label = "Amanda B. Curtlett"
birth = BeginningOfExistence()
bts = TimeSpan()
bts.begin_of_the_begin = "1767-01-09"
bts.end_of_the_end = "1767-01-12"
birth.timespan = bts
death = EndOfExistence()
dts = TimeSpan()
dts.begin_of_the_begin = "1824-08-21"
dts.end_of_the_end = "1824-08-21"
death.timespan = dts
dloc = Place()
dloc.label = "Death Place"
death.took_place_at = dloc
who.brought_into_existence_by = birth
who.taken_out_of_existence_by = death 
id_uri_hash['actor_birthdeath'] = who

who = Person()
who.label = "David E. Frederickson"
bio = BiographyStatement()
bio.value = "Example biography"
who.referred_to_by = bio
id_uri_hash['actor_biog'] = who

who = Person()
who.label = "Gertrude H. Ingram"
img = VisualItem("http://example.org/images/gertrude.jpg")
img.label = "Image of G.H. Ingram"
img.format = "image/jpeg"
who.representation = img
id_uri_hash['actor_image'] = who

who = Person()
who.label = "Jeremy K. Lintott"
natl = Nationality()
natl.classified_as = Type("http://vocab.getty.edu/aat/300111159")
natl.label = "British"
who.member_of = natl
id_uri_hash['actor_nationality'] = who

who = Person()
who.label = "Mabel N. Overton"
gender = Gender()
gender.classified_as = Type("http://vocab.getty.edu/aat/300189557")
gender.label = "feminine"
who.member_of = gender
id_uri_hash['actor_gender'] = who

who = Person()
who.label = "Patrick Q. Robertson"
active = Activity()
active.classified_as = Type("http://vocab.getty.edu/aat/300393177")
ats = TimeSpan()
ats.begin_of_the_begin = "1910-01-01"
ats.end_of_the_end = "1934-03-21"
active.timespan = ats
who.carried_out = active
id_uri_hash['actor_active'] = who

who = Person()
who.label = "Sameen T. Underwood"
dept = Department()
dept.label = "Paintings Department"
mus = MuseumOrg()
mus.label = "Example Museum"
who.member_of = dept
dept.member_of = mus
id_uri_hash['actor_membership'] = who

who = Person()
who.label = "Vincent Van Gogh"
ulan = BaseResource("http://vocab.getty.edu/ulan/500115588-agent")
ulan.label = "Van Gogh, Vincent"
who.exact_match = ulan
id_uri_hash['actor_ulan'] = who


### Exhibitions

exh = Exhibition()
exh.label = "Example Exhibition"
ts = TimeSpan()
ts.begin_of_the_begin = "2010-08-01"
ts.end_of_the_end = "2011-06-01"
exh.timespan = ts
mus = MuseumPlace()
mus.label = "Example Museum's Location"
exh.took_place_at = mus
mus2 = MuseumOrg()
mus2.label = "Example Museum"
exh.carried_out_by = mus2
id_uri_hash['exh_activity'] = exh


exh = Exhibition()
exh.label = "Example Exhibition"
obj = Painting(art=1)
obj.label = "Painting"
obj2 = Painting(art=1)
obj2.label = "Another Painting"
obj3 = Sculpture(art=1)
obj3.label = "Sculpture"
exh.used_specific_object = obj
exh.used_specific_object = obj2
exh.used_specific_object = obj3
id_uri_hash['exh_objects'] = exh

xfer = TransferOfCustody()
xfer.label = "Custody Transfer of Painting for Exhibition"
exh = Exhibition()
exh.label = "Example Exhibition"
obj = Painting(art=1)
obj.label = "Painting"
mus = MuseumOrg()
mus.label = "Exhibiting Museum"
owner = MuseumOrg()
owner.label = "Owning Museum"
xfer.transferred_custody_of = obj
xfer.transferred_custody_to = mus
xfer.transferred_custody_from = owner
xfer.specific_purpose = exh
exh.used_specific_object = obj
exh.carried_out_by = mus
obj.current_owner = owner
id_uri_hash['exh_custody'] = xfer

exh = Exhibition()
exh.label = "Example Exhibition"
obj = Painting(art=1)
obj.label = "Real Painting Name"
aa = Naming()
name = Appellation()
name.value = "Exhibition Specific Name"
aa.assigned = name
aa.assigned_to = obj
exh.consists_of = aa
id_uri_hash['exh_labels'] = exh

exh = Exhibition()
exh.label = "Example Exhibition"
obj = Painting(art=1)
obj.label = "Painting"
exh.used_specific_object = obj
img = VisualItem("http://example.org/images/object-at-exhibition.jpg")
img.format = "image/jpeg"
obj.representation = img
exh.representation = img
id_uri_hash['exh_image'] = exh

multi = MultiExhibition()
multi.label = "Example Travelling Exhibition at Two Museums"
ts = TimeSpan()
ts.begin_of_the_begin = "1980-10-01"
ts.end_of_the_end = "1981-08-14"
multi.timespan = ts
exh = Exhibition()
exh.label = "Exhibition at Museum 1"
ts2 = TimeSpan()
ts2.begin_of_the_begin = "1980-10-01"
ts2.end_of_the_end = "1981-03-01"
exh.timespan = ts2
exh2 = Exhibition()
exh2.label = "Exhibition at Museum 2"
ts3 = TimeSpan()
ts3.begin_of_the_begin = "1981-03-14"
ts3.end_of_the_end = "1981-08-14"
exh2.timespan = ts3
multi.consists_of = exh
multi.consists_of = exh2
id_uri_hash['exh_multi'] = multi



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
