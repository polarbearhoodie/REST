import requests

baseurl = "http://localhost:5000/"

d = "description"
a = "amount"

won = {d: "Lottery", a: 1000.0}
lost = {d: "Gambling", a: 1250}

requests.post(baseurl + "income", json=won)
requests.post(baseurl + "expenses", json=lost)
