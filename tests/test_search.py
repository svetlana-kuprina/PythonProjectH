import pytest

from src.search import process_bank_operations, process_bank_search


@pytest.mark.parametrize(
    "search, exp",
    [
        (
            "Перевод организации",
            [
                {
                    "date": "2018-06-30T02:08:58.425572",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "id": 939719570,
                    "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "date": "2018-09-12T21:27:25.241689",
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "id": 594226727,
                    "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
                    "state": "CANCELED",
                    "to": "Счет 14211924144426031657",
                },
            ],
        )
    ],
)
def test_process_bank_search(transactions, search, exp):
    assert process_bank_search(transactions, search) == exp


@pytest.mark.parametrize("search, exp", [(["Перевод организации", "Операция"], {"Перевод организации": 2})])
def test_process_bank_operations(transactions, search, exp):
    assert process_bank_operations(transactions, search) == exp
