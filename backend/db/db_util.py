
import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DB_CONN_URL = os.environ["DB_CONN_URL"]

def get_all_users():
    client = MongoClient(DB_CONN_URL)

    try:
        db = client["user-data"]
        shopping_list = db["shopping-list"]
        post = {}
        all_users_data  = shopping_list.find(post)
        users_iterable = []

        for user in all_users_data:
            users_iterable.append(user)
        
        return users_iterable
    
    except Exception:
        client.close()
        return False


def find_or_register(user_data):
    client = MongoClient(DB_CONN_URL)
    try:
        db = client["user-data"]
        shopping_list = db["shopping-list"]

        google_sub_id = user_data["subID"]

        search_post = {"_id":google_sub_id}
        user_search = shopping_list.find_one(search_post)
        
        if user_search:
            client.close()
            return user_search
        else:
            new_user_post = {
                "_id":google_sub_id,
                "name":user_data["fullname"],
                "email":user_data["email"],
                "phone_number":"",
                "shopping_list":[]
            }
            shopping_list.insert_one(new_user_post)
            
            client.close()
            return new_user_post

    except Exception:
        client.close()
        return False

def add_item(google_id,item_data):
    client = MongoClient(DB_CONN_URL)
    try:
        db = client["user-data"]
        shopping_list = db["shopping-list"]

        post = {"_id":google_id}
        shopping_list.update_one(post,{"$push":{"shopping_list":item_data}})
        
        client.close()
        return True
    except Exception as e:
        client.close()
        return False

def remove_item(google_id,updated_shopping_list):
    client = MongoClient(DB_CONN_URL)
    try:
        db = client["user-data"]
        shopping_list = db["shopping-list"]

        post = {"_id":google_id}
        shopping_list.update_one(post,{"$set":{"shopping_list":updated_shopping_list}})
        
        client.close()
        return True
    except Exception as e:
        client.close()
        return False
    
    