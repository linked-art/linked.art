
import cromulent
import json
import os

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
fh = file('content/_include/prop_key_map.md', 'w')
fh.write(table)
fh.close()

