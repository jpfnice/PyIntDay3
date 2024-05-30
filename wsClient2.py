import requests
import pprint
pp = pprint.PrettyPrinter(indent=2)

sourceLang="en"
targetLang="it"
sourceText="What time is it"

url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sourceLang}&tl={targetLang}&dt=t&q={requests.utils.quote(sourceText)}";

print(url)
response = requests.get(url)

print(response.status_code)  
js=response.json()
pp.pprint(js)

