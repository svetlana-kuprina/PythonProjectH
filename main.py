
from src.processing import filter_by_state, sort_by_date
from src.read_csv_excel import read_csv, read_excel
from src.search import process_bank_search
from src.utils import get_json_file
from src.widget import get_date, mask_account_card

number = str(
    input(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Ввод: """
    )
)

while True:
    if number == "1" or number == "2" or number == "3":
        break
    else:
        number = str(
            input(
                """Вы ввели не верное значение. Выберите один из пунктов
                    Выберите необходимый пункт меню:
                    1. Получить информацию о транзакциях из JSON-файла
                    2. Получить информацию о транзакциях из CSV-файла
                    3. Получить информацию о транзакциях из XLSX-файла
                    Ввод: """
            )
        )

if number == "1":
    status = str(
        input(
            """Для обработки выбран JSON-файл.
    Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

Ввод: """
        )
    )
elif number == "2":
    status = str(
        input(
            """Для обработки выбран CSV-файла.
        Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

    Ввод: """
        )
    )
else:
    status = str(
        input(
            """Для обработки выбран XLSX-файла.
            Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING

        Ввод: """
        )
    )

while True:
    if status == "EXECUTED" or status == "CANCELED" or status == "PENDING":
        break
    else:
        status = str(
            input(
                f"""Статус операции {status} недоступен.
               Введите статус, по которому необходимо выполнить фильтрацию.
           Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
                       Ввод: """
            )
        )

data_sort = str(
    input(
        """Отсортировать операции по дате? Да/Нет
                Ввод: """
    )
).lower()
while True:
    if data_sort == "да" or data_sort == "нет":
        break
    else:
        data_sort = str(
            input(
                """Вы ввели не верное значение.Введите Да или Нет.
                        Ввод: """
            )
        ).lower()
if data_sort == "да":
    data_sort_reverse = str(
        input(
            """Отсортировать по возрастанию или по убыванию?
                    Ввод: """
        )
    ).lower()
    while True:
        if data_sort_reverse == "по возрастанию" or data_sort_reverse == "по убыванию":
            break
        else:
            data_sort_reverse = str(
                input(
                    """Вы ввели не верное значение.Введите по возрастанию или по убыванию.
                            Ввод: """
                )
            ).lower()

val_yn = str(
    input(
        """Выводить только рублевые транзакции? Да/Нет
                Ввод: """
    )
).lower()
while True:
    if val_yn == "да" or val_yn == "нет":
        break
    else:
        val_yn = str(
            input(
                """Вы ввели не верное значение.Введите Да или Нет.
                        Ввод: """
            )
        ).lower()

search_yn = str(
    input(
        """Отфильтровать список транзакций по определенному слову в описании? Да/Нет
                Ввод: """
    )
).lower()
while True:
    if search_yn == "да" or search_yn == "нет":
        break
    else:
        search_yn = str(
            input(
                """Вы ввели не верное значение.Введите Да или Нет.
                        Ввод: """
            )
        ).lower()

if search_yn == "да":
    search = str(
        input(
            """Введите описание транзакций для фильтрации?
                    Ввод: """
        )
    ).lower()
print("Распечатываю итоговый список транзакций...")

if number == "1":
    json_file = "data/operations.json"
    list_operation = get_json_file(json_file)
    list_operation_state = filter_by_state(list_operation, status)

    if data_sort == "да":
        if data_sort_reverse == "по возрастанию":
            list_operation_state = sort_by_date(list_operation_state, False)
        else:
            list_operation_state = sort_by_date(list_operation_state)

    if search_yn == "да":
        list_operation_state = process_bank_search(list_operation_state, search)

    if val_yn == "да":
        len_list_operation = []
        for item in list_operation_state:
            if item["operationAmount"]["currency"]["code"] == "RUB":
                len_list_operation.append(item)
        if not len_list_operation:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        print(f"Всего банковских операций в выборке: {len(len_list_operation)}")
        for item in list_operation_state:
            if item["operationAmount"]["currency"]["code"] == "RUB":
                if item["description"] == "Открытие вклада":
                    print(f"{get_date(item['date'])} {item['description']}")
                    print(f"{mask_account_card(item['to'])}")
                    print(
                        f'Сумма : {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'
                    )
                else:
                    print(f"{get_date(item['date'])} {item['description']}")
                    print(f"{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}")
                    print(
                        f'Сумма : {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'
                    )

    else:
        if len(list_operation_state) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        print(f"Всего банковских операций в выборке: {len(list_operation_state)}")
        for item in list_operation_state:

            if item["description"] == "Открытие вклада":
                print(f"{get_date(item['date'])} {item['description']}")
                print(f"{mask_account_card(item['to'])}")
                print(f'Сумма : {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n')
            else:
                print(f"{get_date(item['date'])} {item['description']}")
                print(f"{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}")
                print(f'Сумма : {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n')


elif number == "2":
    csv_direct = "data/transactions.csv"
    list_operation = read_csv(csv_direct)
    list_operation_state = filter_by_state(list_operation, status)
    if data_sort == "да":
        if data_sort_reverse == "по возрастанию":
            list_operation_state = sort_by_date(list_operation_state, False)
        else:
            list_operation_state = sort_by_date(list_operation_state)

    if search_yn == "да":
        list_operation_state = process_bank_search(list_operation_state, search)

    if val_yn == "да":
        len_list_operation = []
        for item in list_operation_state:
            if item["currency_code"] == "RUB":
                len_list_operation.append(item)
        if not len_list_operation:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        print(f"Всего банковских операций в выборке: {len(len_list_operation)}")
        for item in list_operation_state:
            if str(item["currency_code"]) == "RUB":
                if item["description"] == "Открытие вклада":
                    print(f"{get_date(item['date'])} {item['description']}")
                    print(f"{mask_account_card(item['to'])}")
                    print(f'Сумма : {item["amount"]} {item["currency_name"]}\n')
                else:
                    print(f"{get_date(item['date'])} {item['description']}")
                    print(f"{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}")
                    print(f'Сумма : {item["amount"]} {item["currency_name"]}\n')

    else:
        if len(list_operation_state) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        print(f"Всего банковских операций в выборке: {len(list_operation_state)}")
        for item in list_operation_state:
            if item["description"] == "Открытие вклада":
                print(f"{get_date(item['date'])} {item['description']}")
                print(f"{mask_account_card(item['to'])}")
                print(f'Сумма : {item["amount"]} {item["currency_name"]}\n')
            else:
                print(f"{get_date(item['date'])} {item['description']}")
                print(f"{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}")
                print(f'Сумма : {item["amount"]} {item["currency_name"]}\n')

else:
    excel_direct = "data/transactions_excel.xlsx"
    list_operation = read_excel(excel_direct)
    list_operation_state = filter_by_state(list_operation, status)
    if data_sort == "да":
        if data_sort_reverse == "по возрастанию":
            list_operation_state = sort_by_date(list_operation_state, False)
        else:
            list_operation_state = sort_by_date(list_operation_state)

    if search_yn == "да":
        list_operation_state = process_bank_search(list_operation_state, search)

    if val_yn == "да":
        len_list_operation = []
        for item in list_operation_state:
            if item["currency_code"] == "RUB":
                len_list_operation.append(item)
        if not len_list_operation:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        print(f"Всего банковских операций в выборке: {len(len_list_operation)}")
        for item in list_operation_state:
            if str(item["currency_code"]) == "RUB":
                if item["description"] == "Открытие вклада":
                    print(f"{get_date(item['date'])} {item['description']}")
                    print(f"{mask_account_card(item['to'])}")
                    print(f'Сумма : {item["amount"]} {item["currency_name"]}\n')
                else:
                    print(f"{get_date(item['date'])} {item['description']}")
                    print(f"{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}")
                    print(f'Сумма : {item["amount"]} {item["currency_name"]}\n')

    else:
        if len(list_operation_state) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        print(f"Всего банковских операций в выборке: {len(list_operation_state)}")
        for item in list_operation_state:
            if item["description"] == "Открытие вклада":
                print(f"{get_date(item['date'])} {item['description']}")
                print(f"{mask_account_card(item['to'])}")
                print(f'Сумма : {item["amount"]} {item["currency_name"]}\n')
            else:
                print(f"{get_date(item['date'])} {item['description']}")
                print(f"{mask_account_card(item['from'])} -> {mask_account_card(item['to'])}")
                print(f'Сумма : {item["amount"]} {item["currency_name"]}\n')
