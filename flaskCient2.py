import requests

# methods: get post put delete head ...
import pprint
pp = pprint.PrettyPrinter(indent=2)

response = requests.post("http://localhost:5000/wrong/route")
pp.pprint(response.headers)
pp.pprint(response.status_code)
js=response.json() # or response.text
pp.pprint(js)


response = requests.get("http://localhost:5000/facto/7")
pp.pprint(response.headers)
pp.pprint(response.status_code)
js=response.json() # or response.text
pp.pprint(js)

response = requests.post("http://localhost:5000/facto/7")
pp.pprint(response.headers)
pp.pprint(response.status_code)
js=response.json() # or response.text
pp.pprint(js)

