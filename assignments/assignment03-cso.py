import requests 
import json 

filename = "cso.json"

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(url)

csoJSON = response.json()

with open (filename, "w") as fp:
    json.dump(csoJSON, fp, indent = 4)
