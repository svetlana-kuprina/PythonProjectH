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
            return result["result"]
    except ConnectionError:
        raise ConnectionError("Connection error")
    except KeyError:
        raise KeyError("Key error")
    except Exception as e:
        raise e

    return transaction["operationAmount"]["amount"]
