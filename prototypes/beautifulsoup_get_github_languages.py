from pprint import pprint

import requests
from bs4 import BeautifulSoup

search_page = requests.get("https://github.com/search/advanced")
soup = BeautifulSoup(search_page.text, "html.parser")
languages = sorted([
    o["value"]
    for o in soup.find(id="search_language").find_all("option")
    if o["value"] != ""
], key=str.lower)

pprint(languages)
