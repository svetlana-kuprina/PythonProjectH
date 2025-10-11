from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


def test_filter_by_currency(transactions):
    """Тест для функции filter_by_currency
    Тест, проверяет, что функция корректно фильтрует транзакции по заданной валюте."""

    usd_transactions = filter_by_currency(transactions, "USD")
    exp1 = {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
            'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
            'to': 'Счет 11776614605963066702'}
    exp2 = {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
            'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
            'to': 'Счет 75651667383060284188'}

    assert next(usd_transactions) == exp1
    assert next(usd_transactions) == exp2


@pytest.mark.parametrize('transactions', [([{
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
        "amount": "9824.07",
        "currency": {
            "name": "RU",
            "code": "RU"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
},
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "RU",
                "code": "RU"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "RU",
                "code": "RU"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }, {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "RU",
                "code": "RU"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }])])
def test_filter_by_currency1(transactions):
    """Тест для функции filter_by_currency
    Тест, проверяет, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют."""

    assert list(filter_by_currency(transactions, 'USD')) == []


@pytest.mark.parametrize('transactions', [([])])
def test_filter_by_currency2(transactions):
    """Тест для функции filter_by_currency.
    Тест, проверяет, что генератор не завершается ошибкой при обработке пустого списка."""

    assert list(filter_by_currency(transactions, 'USD')) == ['Нет итераций']


def test_transaction_descriptions(transactions):
    """Тест для функции transaction_descriptions. Проверяет, что функция возвращает корректные
     описания для каждой транзакции"""

    usd_transactions = transaction_descriptions(transactions)
    exp1 = 'Перевод организации'
    exp2 = 'Перевод со счета на счет'

    assert next(usd_transactions) == exp1
    assert next(usd_transactions) == exp2


@pytest.mark.parametrize('transactions', [([])])
def test_transaction_descriptions2(transactions):
    """Тест для функции transaction_descriptions.
    Тест, проверяет, что генератор не завершается ошибкой при обработке пустого списка."""

    assert list(transaction_descriptions(transactions)) == ['Нет итераций']


def test_card_number_generator():
    """Тест для функции card_number_generator. Проверяет, что функция генератор выдает правильные номера карт
     в заданном диапазоне"""

    exp1 = '0000 0000 0000 0001'
    exp2 = '0000 0000 0000 0002'

    descriptions = card_number_generator(1, 2)
    assert (next(descriptions)) == exp1
    assert (next(descriptions)) == exp2


def test_card_number_generator2():
    """Тест для функции card_number_generator. Проверяет, что функция генератор выдает корректные номера карт."""

    exp1 = '0000 0000 0000 0099'
    exp2 = '0000 0000 0000 0100'

    descriptions = card_number_generator(99, 100)
    assert (next(descriptions)) == exp1
    assert (next(descriptions)) == exp2

def test_card_number_generator3():
    """Тест для функции card_number_generator. Проверяет, что функция генератор корректно обрабатывает
    крайние значения диапазона."""

    exp1 = '9999 9999 9999 9998'
    exp2 = '9999 9999 9999 9999'

    descriptions = card_number_generator(9999999999999998, 9999999999999999)
    assert (next(descriptions)) == exp1
    assert (next(descriptions)) == exp2