
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
ctxt = json.loads(data)

def regex_replace_fn(source, regex):
	print "called r_r_fn"
	try:
		repl = re.compile(regex)
	except:
		print "ERROR: Failing regex: %s" % regex
		return source
	return repl.sub(ctxtrepl, source)

def ctxtrepl(source):
	data = source.group(0)[1:-1]
	print "got data: %r" % data
	if ctxt.has_key(data):
		return "<abbr title='%s'>%s</abbr>" % (ctxt[data], data)
	else:
		return data
