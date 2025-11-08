from unittest.mock import patch, mock_open

import pandas as pd

from src.read_csv_excel import read_csv, read_excel


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n650703;EXECUTED;"
    "2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;"
    "Перевод организации",
)
def test_read_csv(mock_open):
    """Тест функции read_csv. Используется Mock и patch"""

    expected_result = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    result = read_csv("test.csv")
    assert result == expected_result


def test_read_csv_error():
    """Тест функции read_csv. Ошибка файл не найден"""

    assert read_csv(" ") == []


def test_read_excel_error():
    """Тест функции read_excel. Ошибка файл не найден"""

    assert read_excel(" ") == []


@patch("pandas.read_excel")
def test_read_excel(mock_df):
    """Тест функции read_excel. Используется Mock и patch"""

    read_data = pd.DataFrame(
        {
            "id": ["650703"],
            "state": ["EXECUTED"],
            "date": ["2023-09-05T11:30:32Z"],
            "amount": ["16210"],
            "currency_name": ["Sol"],
            "currency_code": ["PEN"],
            "from": ["Счет 58803664561298323391"],
            "to": ["Счет 39745660563456619397"],
            "description": ["Перевод организации"],
        }
    )
    mock_df.return_value = read_data

    expected_result = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    result = read_excel("test.csv")
    assert result == expected_result
