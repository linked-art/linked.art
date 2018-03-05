import json

fh = open('crm-profile.json')
data = fh.read()
fh.close()
js = json.loads(data)

out = {}

for (k,v) in js.items():
	if type(v) == list:
		out[k] = v[1]

def sorter(x):
	name = x[0]
	if name[0] == "P" and name[1].isdigit():
		end = name.find("_")
		if not name[end-1].isdigit():
			end -= 1
		return int(name[1:end])
	else:
		return 1000

oi = out.items()
oi.sort(key=sorter)

oh = open("multiplicity_table.md", 'w')
oh.write("Property | Multiples?\n")
oh.write("-------- | ---------\n")
for (o,i) in oi:
	oh.write("%s | %s\n" % (o, ["no","yes"][i])) 
oh.close()
