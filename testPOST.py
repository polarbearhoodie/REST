import requests

baseurl = "http://localhost:5000/"

transact = {"description": "lottery",  "amount": 1000.0}

requests.post(baseurl + "incomes", json=transact)
