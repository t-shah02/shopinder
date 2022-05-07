import json
from product_scrapers import *

with open("stores.json","r") as file:
    STORE_URLS_DICT = json.loads(file.read())



def is_valid_url(url : str):
    for store_name,base_url in STORE_URLS_DICT.items():
        if url.startswith(base_url):
            return store_name

    return False