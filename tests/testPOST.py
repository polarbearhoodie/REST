import requests

baseurl = "http://localhost:5000/"

transact = {"description": "Lottery",  "amount": 1000.0}

requests.post(baseurl + "income", json=transact)
