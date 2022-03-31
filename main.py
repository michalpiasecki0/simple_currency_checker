# this is a simple python script to check current exchange rates

import requests
import json

authentication_key = 'faba475fb52ff70f3f87f24e02bc3cf3'
base_link = 'http://data.fixer.io/api/latest?access_key='
full_link = f"{base_link}{authentication_key}"


# commented now not to use to many calls for fixer api
'''
response = requests.get(full_link)
content = response.json()

title_file = "data.json"
f = open(title_file, "w")
json.dump(content, f)
f.close()
'''



with open('data.json', 'r') as json_file:
   data = json.load(json_file)
current_pln = data['rates']['PLN']
print(current_pln)