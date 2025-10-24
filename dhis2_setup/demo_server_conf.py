import requests
from requests.auth import HTTPBasicAuth
import json

BASE_URL = "https://play.dhis2.org/stable-2-41-6"
AUTH = ("admin", "district")

auth = HTTPBasicAuth(USERNAME, PASSWORD)
headers = {"Content-Type": "application/json"}
