from xml.dom import minidom


maps = []

ENGINE_VERSION = 3

def main(map):
	dir = map
	if ENGINE_VERSION == 3:
		xmldoc = minidom.parse("maps/" + dir + "/" + dir + ".hpm_StaticObject")
	else:
		xmldoc = minidom.parse("maps/" + dir + "/" + dir + ".map")
	itemlist = xmldoc.getElementsByTagName('File')
	print(len(itemlist))
	print(itemlist[0].attributes['Path'].value)

	with open("out/" + map + ".txt", "w+") as result:
		for s in itemlist:
			if ENGINE_VERSION == 2 and not (s.attributes['Path'].value.endswith(".dae")):
				continue
			print(s.attributes['Path'].value)
			result.write(s.attributes['Path'].value + "\n")
	result.close()

with open("maps.txt") as f:
	for line in f:
		maps.append(line.rstrip('\n'))

print(maps)

for map in maps:
	main(map)
