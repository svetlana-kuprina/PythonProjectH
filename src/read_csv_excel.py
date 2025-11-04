import csv
from typing import Hashable, Any

import pandas as pd


def read_csv(direct: str) -> list[dict[str, str]]:
    """Функция реализует считывание финансовых операций из CSV-файла"""
    try:

        with open(direct, encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            return list(reader)

    except FileNotFoundError:
        return []


def read_excel(direct: str) -> list[dict[Hashable, Any]]:
    """Функция реализует считывание финансовых операций из XLSX-файла"""
    try:

        reader = pd.read_excel(direct)
        return reader.to_dict(orient="records")

    except FileNotFoundError:
        return []
