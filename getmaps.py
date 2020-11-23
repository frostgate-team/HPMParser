from os import listdir
from os.path import isfile, join

mypath = "maps"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
dirs = listdir(mypath)
print(dirs)
# for dir in dirs:
	# onlyfiles.append([f for f in listdir(mypath + "/" + dir) if isfile(join(mypath + "/" + dir, f))])
# final_list = []
#print(onlyfiles)
maps_file = open("maps.txt", "w")
for dir in dirs:
	maps_file.write(dir + "\n")
maps_file.close()