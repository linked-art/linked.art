
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

def regex_replace_fn(source, regex):
	try:
		repl = re.compile(regex)
	except:
		print "ERROR: Failing regex: %s" % regex
		return source
	return repl.sub(ctxtrepl, source)

def ctxtrepl(source):
	full = source.group(0)
	data = source.group(1)
	if ctxt.has_key(data):
		if type(ctxt[data]) == dict:
			crm = ctxt[data]['@id']
		else:
			crm = ctxt[data]
		return "<abbr title='%s'>%s</abbr>" % (crm, full)
	else:
		return data
