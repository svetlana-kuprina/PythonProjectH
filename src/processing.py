from datetime import datetime
from typing import Dict, List


def filter_by_state(list_operation: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция, которая принимает список словарей и опционально значение для ключа state
     (по умолчанию 'EXECUTED'). Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
        :param state:
        :type list_operation: List[Dict]"""

    new_list = []
    for item in list_operation:
        if item["state"] == state:
            new_list.append(item)
    return new_list


def sort_by_date(list_operation_d: List[Dict], sort: bool = True) -> List[Dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате"""

    for operation in list_operation_d:
        if len(operation["date"]) != 26:
            return "Не верный формат входных данных"
    return sorted(list_operation_d, key=lambda item: datetime.fromisoformat(item["date"]), reverse=sort)
