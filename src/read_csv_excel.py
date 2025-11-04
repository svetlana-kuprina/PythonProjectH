import csv
import pandas as pd


def read_csv(direct: str) -> list[dict[str, str]]:
    with open(direct, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(reader)


def read_excel(direct: str) -> list[dict[str, str]]:
    reader = pd.read_excel(direct)
    return reader.to_dict(orient="records")

# print(read_csv('../data/transactions.csv'))
# print(read_excel('../data/transactions_excel.xlsx'))
