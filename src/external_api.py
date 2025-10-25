import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_external_api(transaction:dict) -> float:

    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        to = "RUB"
        from_ = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
        headers = {
            "apikey": os.getenv('APIKEY')
        }
        payload = {}

        response = requests.request("GET", url, headers=headers, data = payload)

        result = response.text
        result = json.loads(result)
        return result["result"]

    return transaction["operationAmount"]["amount"]

tr = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "10000.00",
      "currency": {
        "name": "евр.",
        "code": "EUR"
      }}}
print(get_external_api(tr))


#
#
# {'success': True, 'query':
#     {'from': 'EUR', 'to': 'RUB', 'amount': 10000},
#  'info': {'timestamp': 1761417844, 'rate': 92.569097},
#  'date': '2025-10-25', 'result': 925690.97})


