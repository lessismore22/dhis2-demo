import requests
from requests.auth import HTTPBasicAuth
import json

BASE_URL = "https://play.dhis2.org/stable-2-42-2"
USERNAME = "admin"
PASSWORD = "district"

auth = HTTPBasicAuth(USERNAME, PASSWORD)
headers = {"Content-Type": "application/json"}
