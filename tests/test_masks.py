import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('card_number, exp', [(7000792289606361, '7000 79** **** 6361'),
                         (70007922896063611, 'Номер карты введен неверно.Введите 16 цифр Вашей карты'),
                         ('qqqqqqqqqqqqqqqq', 'Номер карты введен неверно.Введите 16 цифр Вашей карты, номер не может содержать буквы'),
                         (' ', 'Номер карты введен неверно.Введите 16 цифр Вашей карты, номер не может содержать буквы'),
                         (None, 'Номер карты введен неверно.Введите 16 цифр Вашей карты')])

def test_get_mask_card_number(card_number, exp):
    assert get_mask_card_number(card_number) == exp


@pytest.mark.parametrize('account_number, expected', [(73654108430135874305, '**4305'),
                         (12373654108430135874305, 'Номер счета введен неверно.Введите 20 цифр Вашей карты'),
                         (74305, 'Номер счета введен неверно.Введите 20 цифр Вашей карты'),
                         (1,'Номер счета введен неверно.Введите 20 цифр Вашей карты'),
                        (" ", 'Номер счета введен неверно.Введите 20 цифр Вашего счета, номер не может содержать буквы')])

def test_get_mask_account(account_number, expected):
    assert get_mask_account (account_number) == expected