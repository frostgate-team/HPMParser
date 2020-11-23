from xml.dom import minidom


maps = []

def main(map):
	dir = map

	xmldoc = minidom.parse("maps/" + dir + "/" + dir + ".hpm_StaticObject")
	itemlist = xmldoc.getElementsByTagName('File')
	print(len(itemlist))
	print(itemlist[0].attributes['Path'].value)

	with open("out/" + map + ".txt", "w") as result:
		for s in itemlist:
			print(s.attributes['Path'].value)
			result.write(s.attributes['Path'].value + "\n")
	result.close()

with open("maps.txt") as f:
	for line in f:
		maps.append(line.rstrip('\n'))

print(maps)

for map in maps:
	main(map)
