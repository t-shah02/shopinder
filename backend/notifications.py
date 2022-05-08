import os
from twilio.rest import Client
import dotenv

dotenv.load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

APP_PHONE_NUMBER = "+19706326241"

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=APP_PHONE_NUMBER,
                     to='+15875742002'
                 )

print(message.sid)
                 

