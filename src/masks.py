def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты
    :type card_number: int
    :rtype: str
    """

    if type(card_number) is str:
        return 'Номер карты введен неверно.Введите 16 цифр Вашей карты, номер не может содержать буквы'
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        return 'Номер карты введен неверно.Введите 16 цифр Вашей карты'
    else:
        card_number_now = (
                card_number_str[0:4]
                + " "
                + card_number_str[4:8]
                + " "
                + card_number_str[8:12]
                + " "
                + card_number_str[12:16]
        )
        card_number_mask = card_number_now[0:7] + "** **** " + card_number_now[15:]
    return card_number_mask


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""

    if type(account_number) is str:
        return 'Номер счета введен неверно.Введите 20 цифр Вашего счета, номер не может содержать буквы'
    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        return 'Номер счета введен неверно.Введите 20 цифр Вашей карты'
    else:
        account_number_str = str(account_number)
        account_number_mask = "**" + str(account_number_str[-4:])
        return account_number_mask


#print(get_mask_card_number(card_number='qqqqqqqqqqqqqqqq'))
