from os import listdir
from os.path import isfile, join

mypath = "maps"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
dirs = listdir(mypath)
print(dirs)
print()
print("Found " + str(len(dirs)) + " maps.")
maps_file = open("maps.txt", "w")
for dir in dirs:
	print("Adding " + dir)
	maps_file.write(dir + "\n")
maps_file.close()