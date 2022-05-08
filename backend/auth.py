import os
from google.oauth2 import id_token
import cachecontrol
import google.auth.transport.requests
import requests
import dotenv
import os

dotenv.load_dotenv()
GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]


def authenticate_google_token(encoded_token):
    session = requests.session()
    cached_session = cachecontrol.CacheControl(session)
    request = google.auth.transport.requests.Request(session=cached_session)
    id_info = id_token.verify_oauth2_token(encoded_token, request, GOOGLE_CLIENT_ID)
    return id_info
