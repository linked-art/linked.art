
import requests
from ordereddict import OrderedDict
import json

aat_uri = "http://vocab.getty.edu/aat/"
sparql = "http://vocab.getty.edu/sparql.json?query=select+%3Fx+%3Fname+%3Fcode+%0A++++%7B+%3Fx+gvp%3AbroaderGeneric+aat%3A300411913+%3B+%0A+++++++++xl%3AaltLabel+%3Fy+%3B%0A+++++++++xl%3AprefLabel+%3Fz+.+%0A++++++%3Fy+gvp%3AtermType+%3Chttp%3A%2F%2Fvocab.getty.edu%2Fterm%2Ftype%2FUsedForTerm%3E+%3B%0A+++++++++gvp%3Aterm+%3Fcode+.%0A++++++%3Fz+gvp%3Aterm+%3Fname+.%0A++++++filter+%28langMatches%28lang%28%3Fname%29%2C+%22en%22%29%29%0A++++++filter+%28regex%28str%28%3Fcode%29%2C+%22%5E%5Ba-z-%5D%2B%24%22%29%29%0A++++%7D%0A&toc=Language_Queries&implicit=true&equivalent=false&_form=%2FqueriesF"

resp = requests.get(sparql)
data = resp.json()
results = data['results']['bindings']

languages = {}



for res in results:
	uri = res['x']['value']
	code = res['code']['value']
	name = res['name']['value']

	if uri in languages:
		# Duplicate... Prefer shorter codes
		old = languages[uri]
		if len(old['code']) > len(code):
			languages[uri] = {"code": code, "name": name}
	else:
		languages[uri] = {"code": code, "name": name}

items = languages.items()
items.sort(key = lambda x: x[1]['name'])

ctxt = OrderedDict()

ctxt['aat_vocab'] = aat_uri

for (uri, h) in items:
	ctxt[h['code']] = uri

context = json.dumps(ctxt, indent=2)
fh = open('../content/ns/v1/languages.json', 'w')
fh.write(context)
fh.close()
