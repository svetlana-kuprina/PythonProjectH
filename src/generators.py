from typing import Dict, Generator, List


def filter_by_currency(operation: List[Dict], val: str) -> Generator:
    """Функция генератор, который принимает на вход список словарей, представляющих транзакции,
    возвращать итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной"""

    if operation:
        for item in operation:
            if item["operationAmount"]["currency"]["code"] == val:
                yield item
    else:
        yield "Нет итераций"


def transaction_descriptions(operation: List[Dict]) -> Generator:
    """Функция генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""

    if operation:
        for item in operation:
            yield item["description"]
    else:
        yield "Нет итераций"


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Generator:
    """Функция генератор, который выдает номера банковских карт в формате ХXXX XXXX XXXX XXXX, где X  — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""

    for number in range(start, stop + 1):
        number_card = "0" * (16 - len(str(number))) + str(number)
        form_number_card = (
            number_card[0:4] + " " + number_card[4:8] + " " + number_card[8:12] + " " + number_card[12:16]
        )
        yield form_number_card
