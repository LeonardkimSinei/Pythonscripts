import csv
import json

with open('cpdcsv.csv') as cp:
    data = csv.DictReader(cp)
    data_list = list(data)
    print(type(data_list))
with open ('json_file', 'w') as json_output:
    json.dump(data_list, json_output, indent=4)
        
    