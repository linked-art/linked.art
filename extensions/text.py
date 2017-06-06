
import re
from hyde.plugin import Plugin
import json

def regex_replace(source, regex, replace):
	try:
		repl = re.compile(regex)
	except:
		print "ERROR: Failing regex: %s" % regex
		return source
	return repl.sub(replace, source)

# Try to load in the context only once
fh = file('content/ns/context/1/full.jsonld')
data = fh.read()
fh.close()
ctxt = json.loads(data)['@context']

# And load up the AAT:Label mapping once
fh = file('extensions/aat_labels.json')
data = fh.read()
fh.close()
aat_labels = json.loads(data)

def regex_replace_fn(source, regex, fnname):
	try:
		repl = re.compile(regex)
	except:
		print "ERROR: Failing regex: %s" % regex
		return source
	try:
		fn = globals()[fnname]
	except:
		print "ERROR: No such function '%s'" % fnname
	return repl.sub(fn, source)

def aatlabel(source):
	full = source.group(0)
	data = source.group(1)
	label = aat_labels.get(full, "")
	label = label.replace('"', '')
	return '<a href="http://vocab.getty.edu/aat/%s" data-ot="%s" data-ot-title="AAT Term" data-ot-fixed="true" class="aat">aat:%s</a>' % (data, label, data)


def ctxtrepl(source):
	full = source.group(0)
	data = source.group(1)
	if ctxt.has_key(data):
		if type(ctxt[data]) == dict:
			crm = ctxt[data]['@id']
		else:
			crm = ctxt[data]
		return '<abbr data-ot="%s" data-ot-title="Linked Data Term" data-ot-fixed="true">%s</abbr>' % (crm, full)
	else:
		return full
