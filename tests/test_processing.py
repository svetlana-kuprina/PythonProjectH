from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, exp_operation",
    (
        [
            (
                "EXECUTED",
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
            ),
            (
                "CANCELED",
                [
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
            ),
        ]
    ),
)
def test_filter_by_state_s(list_operation: List[Dict], state: str, exp_operation: List[Dict]) -> None:
    """Тест для функции filter_by_state:
    Тестирование фильтрации списка словарей по заданному статусу state
    Параметризация тестов для различных возможных значений статуса state"""

    assert filter_by_state(list_operation, state) == exp_operation


def test_filter_by_state(list_operation: List[Dict]) -> None:
    """Тест для функции filter_by_state:
    Проверка работы функции при отсутствии словарей с указанным статусом state в списке."""

    assert filter_by_state(list_operation) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "sort, exp_operation",
    (
        [
            (
                True,
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
            ),
            (
                False,
                [
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                ],
            ),
        ]
    ),
)
def test_sort_by_date_s(list_operation: List[Dict], sort: bool, exp_operation: List[Dict]) -> None:
    """Тест для функции sort_by_date:
    Тестирование сортировки списка словарей по датам в порядке убывания и возрастания."""

    assert sort_by_date(list_operation, sort) == exp_operation


@pytest.mark.parametrize(
    "exp_operation",
    (
        [
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        ]
    ),
)
def test_sort_by_date(list_operation: List[Dict], exp_operation: List[Dict]) -> None:
    """Тест для функции sort_by_date:
    Проверка работы функции при отсутствии sort"""

    assert sort_by_date(list_operation) == exp_operation


@pytest.mark.parametrize(
    "sort2, exp_operation2",
    (
        [
            (
                True,
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
            ),
            (
                False,
                [
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                ],
            ),
        ]
    ),
)
def test_sort_by_date_repeat(list_operation_repeat: List[Dict], sort2: bool, exp_operation2: List[Dict]) -> None:
    """Тест для функции sort_by_date:
    Проверка корректности сортировки при одинаковых датах."""

    assert sort_by_date(list_operation_repeat, sort2) == exp_operation2


def test_sort_by_date_f(list_operation_f: List[Dict]) -> None:
    """Тест для функции sort_by_date:
    Тесты на работу функции с некорректными или нестандартными форматами дат."""

    assert sort_by_date(list_operation_f) == "Не верный формат входных данных"
