import re
from typing import Any


def open_file_names(file_name: str) -> list:
    """Функция удаляет знаки препинания и цифры и возвращать только строки, содержащие имя"""
    with open("data/" + file_name, "r", encoding="utf-8") as file:
        file_contents = file.readlines()
        list_names = []
        list_names_cl = []

        for string in file_contents:
            str_date = ""
            for letter in string:
                if letter.isalpha():
                    str_date += letter
            list_names.append(str_date)
        for name in list_names:
            if name.isalpha():
                list_names_cl.append(name)

    return list_names_cl


def get_en_ru(list_names_cl: list) -> tuple[list[Any], list[Any]]:
    """Функция делит имена на рус и анг. и сортирует"""

    en = []
    ru = []
    for name in list_names_cl:
        match = re.search("[a-zA-Z]", name)
        if match:
            en.append(name)
        else:
            ru.append(name)

    ru.sort()
    en.sort()
    with open("data/en.txt", "w", encoding="utf-8") as file:
        en_str = "\n".join(en)
        file.write(en_str)
    with open("data/ru.txt", "w", encoding="utf-8") as file:
        ru_str = "\n".join(ru)
        file.write(ru_str)
    return en, ru


print(open_file_names("names.txt"))

print(get_en_ru(open_file_names("names.txt")))
