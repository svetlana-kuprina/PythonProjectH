from src.masks import get_mask_account, get_mask_card_number


def mask_account_card (account_number:str) ->str:
    """Функция умеет обрабатывать информацию как о картах, так и о счетах"""


    if account_number[:4] == "Счет":
        account_number_mask = int(account_number[5:])
        return get_mask_account(account_number_mask)
    else:
        account_number_check = account_number.split()
        if len(account_number_check[-1]) != 16:
            return "Номер карты введен неверно.Введите 16 цифр Вашей карты"
        else:
            account_number_mask = int(account_number[-16:])
            return get_mask_card_number(account_number_mask)


def get_date(date_str:str) -> str:
    """Функция видоизменяет дату в формат ДД.ММ.ГГГГ"""


    return date_str[8:10] + '-' + date_str[5:7]+ '-' + date_str[0:4]
