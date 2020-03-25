import requests
import json


currencyInput = "EUR" # We can pull this from the front end later
parameters = {
    "base": "USD",
    "symbols": currencyInput
}

# def pullAPI():
response = requests.get("https://api.exchangeratesapi.io/latest", params=parameters)
# print(response.status_code)
# obj = "Spain"
# text = json.dumps(obj, sort_keys=True, indent=4)
# print(text)
# print(response.json())
currency = response.json()["rates"][currencyInput]

# pullAPI()
print(currency)
