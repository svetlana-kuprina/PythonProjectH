import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_external_api(transaction: dict) -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях. Если транзакция была в
    USD или EUR, происходит обращение к внешнему API"""

    try:
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            to = "RUB"
            from_ = transaction["operationAmount"]["currency"]["code"]
            amount = transaction["operationAmount"]["amount"]
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
            headers = {"apikey": os.getenv("APIKEY")}
            payload = {}
            response = requests.get(url, headers=headers, data=payload)

            result = response.text
            result = json.loads(result)
            return float(result["result"])
    except ConnectionError:
        raise ConnectionError("Connection error")
    except KeyError:
        raise KeyError("Key error")
    except Exception as e:
        raise e

    return float(transaction["operationAmount"]["amount"])

tr = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
tr2 = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "1000.00",
      "currency": {
        "name": "евр.",
        "code": "EUR"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
print(get_external_api(tr))
print(type(get_external_api(tr)))
print(get_external_api(tr2))
print(type(get_external_api(tr2)))
