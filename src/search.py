import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка."""

    search_data = []
    for operation in data:
        search_r = re.search(search, operation["description"], flags=re.IGNORECASE)
        if search_r is not None:
            search_data.append(operation)
    return search_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    categories_data = []
    categories_list = []
    for category in categories:
        for operation in data:
            match = re.search(category, operation["description"], flags=re.IGNORECASE)
            if match is not None:
                categories_list.append(operation["description"])
            categories_data = Counter(categories_list)
    return categories_data
