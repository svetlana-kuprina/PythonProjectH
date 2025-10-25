import json


def get_json_file(json_file: str) -> list[dict]:
    """Функция принимат путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data_file = json.load(f)
            if data_file == None:
                data_file = []
            elif type(data_file) != list:
                data_file = []
    except FileNotFoundError:
        data_file = []
    except json.JSONDecodeError:
        data_file = []

    return data_file


if __name__ == "__main__":
    p = '../data/operations.json'
    print(get_json_file(p))
