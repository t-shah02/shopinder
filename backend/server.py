from flask import Flask, send_from_directory,request,Response
import json

from import_expression import find_imports
from product_scrapers import *
from auth import authenticate_google_token
from db.db_util import *

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

@app.route("/tokenauth",methods=["GET","POST"])
def tokenauth():
    if request.method == "POST":
        data_received = request.get_json()
        user_token = data_received.get("user_token")
        return authenticate_google_token(user_token)
    return Response({"status":"this endpoint only accepts POST requests"},status=403)


@app.route("/user",methods=["GET","POST"])
def handle_user():
    if request.method == "POST":
        data_received = request.get_json()
        user_resp = find_or_register(data_received)
        return user_resp

    
    return Response({"status":"this endpoint only accepts POST requests"},status=403,content_type="application/json")

@app.route("/additem",methods=["GET","POST"])
def additem():
    if request.method == "POST":
        data_received = request.get_json()
        google_id = data_received.get("googleID")
        item_data = data_received.get("itemData")
        add_item(google_id,item_data)
        return {"status":"success"}

    return Response({"status":"this endpoint only accepts POST requests"},status=403,content_type="application/json")


@app.route("/removeitem",methods=["GET","POST"])
def removeitem():
    if request.method == "POST":
        data_received = request.get_json()
        google_id = data_received.get("googleID")
        item_data = data_received.get("updatedShoppingList")
        remove_item(google_id,item_data)
        return {"status":"success"}

    return Response({"status":"this endpoint only accepts POST requests"},status=403,content_type="application/json")

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
