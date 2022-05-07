from flask import Flask, send_from_directory,request,Response
import json
from product_scrapers import *

STATIC_PATH = "../frontend/public"

app = Flask(__name__)


@app.route("/")
def base():
    return send_from_directory(STATIC_PATH, 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory(STATIC_PATH, path)

@app.route("/stores")
def stores():
    with open("stores.json","r") as file:
        stores_data = json.loads(file.read())
        return stores_data

@app.route("/productinfo")
def productinfo():
    store_name = request.args.get('store_name')
    product_url = request.args.get('product_url')
    
    scraper_function = get_scraper_function(store_name)
    results = scraper_function(product_url)
    if isinstance(results,str):
        return Response({"status":"store request failed"},status=404)
    
    product_title,product_img_link,price_value,currency = results
    data = {
        "product_title": product_title,
        "product_img_link": product_img_link,
        "price_value": price_value,
        "currency": currency,
    }
    return data

if __name__ == "__main__":
    app.run(debug=True)
