import os
from sqlite3 import adapt
from twilio.rest import Client
import dotenv
import time
from db_utils import get_all_users
import datetime
import smtplib

dotenv.load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
shopinder_email = os.environ['SHOPINDER_EMAIL']
shopinder_pw = os.environ['SHOPINDER_EMAIL_PASSWORD']


client = Client(account_sid, auth_token)

APP_PHONE_NUMBER = "+19706326241"

def send_email(recipient,message):
    email_session = smtplib.SMTP("smtp.gmail.com",587)
    email_session.starttls()
    email_session.login(shopinder_email,shopinder_pw)
    try:
      email_session.sendmail(shopinder_email, recipient, message)
      return True
    except:
        return False

def process_time(raw_date_str):
    time_split = raw_date_str.replace("T"," ").split(" ")
    time_comp_one,time_comp_two = time_split
    year,month,day = time_comp_one.split("-")
    hour,minute = time_comp_two.split(":")

    return [int(year),int(month),int(day),int(hour),int(minute)]

def time_is_now(item_time):
    current_date = datetime.datetime.now()
    cur_year = current_date.year
    cur_month = current_date.month
    cur_day = current_date.day

    date_vector = [cur_year,cur_month,cur_day]
    item_date_vector = [int(val) for val in item_time[0:3]]

    if date_vector != item_date_vector:
        return False
    
    cur_hour,cur_minute = [int(val) for val in time.strftime('%H:%M:%S').split(":")[0:2]]
    
    item_hour,item_minute = [int(val) for val in item_time[3:]]

    if cur_hour != item_hour:
        return False

    return abs(cur_minute - item_minute) <= 1       

jobs_completed = {}


def notify_users():
    all_users = get_all_users()

    for user in all_users:
        shopping_list = user["shopping_list"]
        for item in shopping_list:
            name = item["name"]
            notification_method = item["notificationMethod"]
            store = item["store"]
            product_url = item["productURL"]
            item_date = item["date"]
            email = user["email"]
            user_id = user["_id"]
            
            if user_id not in jobs_completed:
                jobs_completed[user_id] = []
            
            same_time = time_is_now(process_time(item_date))
            if same_time and product_url not in jobs_completed[user_id]:
                msg_body = f"A friendly Shopinder reminder to buy your product from {store}. \n Product name: {name} \n Found at: {product_url}"
                if notification_method.lower() == "email":
                    send_email(email,msg_body)
                    jobs_completed[user_id].append(product_url)
                elif notification_method.lower() == "phone":
                    user_phone_number = item["phoneNumber"].replace("-","")
                    if not user_phone_number.startswith("+1"):
                        user_phone_number = f"+1{user_phone_number}"
                
                    client.messages.create(body=msg_body,from_=APP_PHONE_NUMBER,to=user_phone_number)
                    jobs_completed[user_id].append(product_url)

                else:
                    # invalid notification_method found
                    continue



#main event loop (call notify users every 60 seconds, and notify users that have scheduled store products to buy at this current time)
starttime = time.time()
while True:
    notify_users()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

