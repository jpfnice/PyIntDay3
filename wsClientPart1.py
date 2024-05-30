import requests

# methods: get post put delete head ...
import pprint
pp = pprint.PrettyPrinter(indent=2)



# response = requests.get("https://api.weather.gov/gridpoints/TOP/31,80/forecast")
# pp.pprint(response.headers)
# pp.pprint(response.status_code)
# js=response.json() # or response.text
# pp.pprint(js)

# response = requests.get('https://ipwhois.app/xml/128.178.115.174')
# print(response.status_code)
# pp.pprint(response.headers)
# print(response.text)
# #js=response.json()
# #pp.pprint(js)



response = requests.get("https://itunes.apple.com/search?term=dave+gahan&limit=10")


print(response.text)

js=response.json()
pp.pprint(js)
