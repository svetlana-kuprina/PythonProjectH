
from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import mask_account_card

number = str(input('Введите название и номер счета или карты: '))

list_name_account_n =[]
list_name_account = number.split(' ')
for name in list_name_account:
    if name.isalpha():
        list_name_account_n.append(name)
print(' '.join(list_name_account_n) + " " + mask_account_card(number))






