# Read from csv write to json file. convert each occurrence of o with 0
# PFA the csv file.

import json

data = open('test.csv').read()
clean_list = data.split(",")
data_list = []
key_list = []
new_list = []
main = {}
x = []
for i in clean_list:
	data_clean = i.replace("o","0")
	data_clean = data_clean.strip('"')
	data_clean = data_clean.strip(' "')
	data_clean = data_clean.strip('"\n')
	data_list.append(data_clean)

print(data_list)

for i in data_list:
	data_1 = i.split("/")
	if len(data_1) <=1:
		key = data_1[0]
		main[key] = ""
	else:
		key = data_1[0]
		if key not in main:
			main[key] = []
		for i in data_1[1:]:
			main[key].append(i)
 			
with open('data.json','w') as outfile:
   	outfile.write(json.dumps(main,ensure_ascii=False))

print(main)

