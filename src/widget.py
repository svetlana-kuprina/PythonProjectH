from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_number: str) -> str:
    """Функция умеет обрабатывать информацию как о картах, так и о счетах"""
    try:
        list_name_account_n = []
        list_name_account = account_number.split(" ")
        for name in list_name_account:
            if name.isalpha():
                list_name_account_n.append(name)

        if account_number[:4] == "Счет":
            account_number_check = account_number.split()
            if len(account_number_check[-1]) != 20:
                return "Номер счета введен неверно.Введите 20 цифр Вашего счета"
            else:
                account_number_mask = int(account_number[5:])
                return " ".join(list_name_account_n) + " " + get_mask_account(account_number_mask)
        else:
            account_number_check = account_number.split()
            if len(account_number_check[-1]) != 16:
                return "Номер карты введен неверно.Введите 16 цифр Вашей карты"
            else:
                account_number_mask = int(account_number[-16:])
                return " ".join(list_name_account_n) + " " + get_mask_card_number(account_number_mask)

    except AttributeError:
        return "Ошибка: Вы ввели некорректный номер счета или карты"


def get_date(date_str: str) -> str:
    """Функция видоизменяет дату в формат ДД.ММ.ГГГГ"""
    if type(date_str) is int or type(date_str) is float:
        return 'Не верный формат входных данных'
    elif len(date_str) != 26:
        return 'Не верный формат входных данных'
    else:
        return date_str[8:10] + "-" + date_str[5:7] + "-" + date_str[0:4]
