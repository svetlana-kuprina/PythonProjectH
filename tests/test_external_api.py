from unittest.mock import patch, Mock

import pytest

from src.external_api import get_external_api


@patch("requests.get")
def test_get_external_api_error(mock_request_get):
    """Тест не верный API ключ"""

    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.text = '{"message":"Invalid authentication credentials"}'
    mock_request_get.return_value = mock_response

    tr = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "10000.00", "currency": {"name": "евр.", "code": "EUR"}},
    }
    with pytest.raises(KeyError) as excinfo:
        get_external_api(tr)
        assert excinfo.value.args[0] == KeyError("Key error")
        mock_request_get.assert_called_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=10000.00",
            headers={"apikey": "Hzn1ZfOBV2bvKNQBCgsZW72APuJSZI7"},
            data={},
        )


@patch("requests.get")
def test_get_external_api(mock_request_get):
    """Тест функции если транзакция была в USD или EUR, происходит обращение к внешнему API"""

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = """{"success": true, "query": {"from": "EUR", "to": "RUB", "amount": 10000},
    "info": {"timestamp": 1761461044, "rate": 92.569097}, "date": "2025-10-26", "result": 925690.97}"""
    mock_request_get.return_value = mock_response
    tr = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "10000.00", "currency": {"name": "евр.", "code": "EUR"}},
    }
    assert get_external_api(tr) == 925690.97
    mock_request_get.assert_called_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=10000.00",
        headers={"apikey": "Hzn1ZfOBV2bvKNQBCgsZW72APuJSZI72"},
        data={},
    )
