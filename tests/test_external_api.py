from unittest.mock import patch, Mock

from src.external_api import get_external_api


def test_get_external_api():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"success": true, "query": {"from": "EUR", "to": "RUB", "amount": 10000},"info": {"timestamp": 1761461044, "rate": 92.569097}, "date": "2025-10-26", "result": 925690.97}'
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
    assert get_external_api(tr) == 925690.97


@patch('requests.get')
def test_get_external_api2(mock_get):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_get.return_value.json.loads.return_value = '{"success": true, "query": {"from": "EUR", "to": "RUB", "amount": 10000},"info": {"timestamp": 1761461044, "rate": 92.569097}, "date": "2025-10-26", "result": 925690.97}'
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
    assert get_external_api(tr) == 925690.97

