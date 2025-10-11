import random
from typing import List, Dict, Generator


def filter_by_currency(operation: List[Dict], val: str)->Generator:
    """ Функция, которая принимает на вход список словарей, представляющих транзакции,
    возвращать итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной"""


    if operation:
        for item in operation:
            if item['operationAmount']['currency']['code'] == val:
                yield item
    else:
        yield 'Нет итераций'


def transaction_descriptions(operation: List[Dict])->Generator:
    if operation:
        for item in operation:
            yield item ['description']
    else:
        yield 'Нет итераций'


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Generator:
    for number in range(start, stop+1):
        number_card = '0' * (16 - len(str(number))) + str(number)
        form_number_card = number_card[0:4] + ' ' + number_card[4:8] + ' ' + number_card[8:12] + ' ' + number_card[12:16]
        yield form_number_card


descriptions = card_number_generator(9999999999999998, 9999999999999999)
for _ in range(3):
     print(next(descriptions, "Нет больше операций"))