from os import listdir
from os.path import isfile, join

mypath = "out"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

final_list = []

for f in onlyfiles:
	with open(mypath + "/" + f) as file1:
		for line in file1:
			final_list.append(line.rstrip('\n') + "\n")


for entry in final_list:
	for entry1 in final_list:
		if entry == entry1:
			final_list.remove(entry)
			#final_list.remove(entry1)

f = open("out/meshlist.txt", "w")
for entry in final_list:
	f.write(entry)
f.close()
