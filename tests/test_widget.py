import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('check, check_exp', [('Счет 73654108430135874305', 'Счет **4305'),
                                              ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                              ('Счет ', "Номер счета введен неверно.Введите 20 цифр Вашего счета"),
                                              ('Visa Platinum 123', "Номер карты введен неверно.Введите 16 цифр Вашей карты"),
                                              (123, "Ошибка: Вы ввели некорректный номер счета или карты")])
def test_mask_account_card(check, check_exp):
    assert mask_account_card(check) == check_exp

@pytest.mark.parametrize('date, expected', [('2024-03-11T02:26:18.671407', '11-03-2024'),
                                            (12345, 'Не верный формат входных данных'),
                                            ('2024-03-11T02:26:18.67140', 'Не верный формат входных данных'),
                                            ('-T02:26:18.67140', 'Не верный формат входных данных')])
def test_get_date(date, expected):
    assert get_date (date) == expected
