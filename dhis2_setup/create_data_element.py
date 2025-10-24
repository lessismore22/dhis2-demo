import requests
import json

BASE_URL = "https://play.dhis2.org/stable-2-41-6"
AUTH = ("admin", "district")

data_element = {
    "name": "Number of Outpatient Visits",
    "shortName": "OPD Visits",
    "code": "OPD001",
    "valueType": "NUMBER",
    "aggregationType": "SUM",
    "domainType": "AGGREGATE",
    "zeroIsSignificant": True,
    "formName": "OPD Visits",
    "description": "Total number of patients visiting OPD weekly."
}

response = requests.post(
    BASE_URL + "dataElements",
    auth=AUTH,
    headers={"Content-Type": "application/json"},
    data=json.dumps(data_element)
)

print(response.status_code, response.text)

