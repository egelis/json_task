import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')

with open("data_file.json", 'w') as write_file:
    json.dump(response.json(), write_file, indent=3)
