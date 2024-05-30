import requests

# methods: get post put delete head ...
import pprint
pp = pprint.PrettyPrinter(indent=2)

response = requests.get("http://localhost:5000/sqrt/abc")
pp.pprint(response.headers)
pp.pprint(response.status_code)
js=response.text # or response.text
pp.pprint(js)

response = requests.get("http://localhost:5000/")
pp.pprint(response.headers)
pp.pprint(response.status_code)
js=response.text # or response.text
pp.pprint(js)

response = requests.get("http://localhost:5000/articles")
pp.pprint(response.headers)
pp.pprint(response.status_code)
js=response.text # or response.text
pp.pprint(js)

response = requests.get("http://localhost:5000/numbers/12")
pp.pprint(response.headers)
pp.pprint(response.status_code)
js=response.text # or response.text
pp.pprint(js)
