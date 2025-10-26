from src.utils import get_json_file
from unittest.mock import patch, mock_open


@patch("builtins.open", create=True)
def test_get_json_file(mock_open):
    """Тест функции get_json_file принимает на вход путь до JSON-файла и возвращает список словарей
     с данными о финансовых транзакциях. Используется Mock и patch"""

    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = """[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
     "operationAmount":
     {"amount": "31957.58","currency": {"name": "руб.", "code": "RUB" }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]"""
    assert get_json_file("test.txt") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    mock_open.assert_called_once_with("test.txt", "r", encoding="utf-8")


def test_get_json_file_err():
    """Тест функции get_json_file принимает на вход не верный путь до JSON-файла и возвращает пустой список"""

    test_f = "../data/1operations.json"
    assert get_json_file(test_f) == []


@patch("builtins.open", create=True)
def test_get_json_file_err2(mock_open):
    """Тест функции get_json_file JSON-файл содержит не верный формат и возвращает пустой список"""

    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = """[{'id': 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
     "operationAmount":
     {"amount": "31957.58","currency": {"name": "руб.", "code": "RUB" }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]"""
    assert get_json_file("test.txt") == []
    mock_open.assert_called_once_with("test.txt", "r", encoding="utf-8")
