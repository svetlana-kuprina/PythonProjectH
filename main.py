from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

#number = str(input("Введите название и номер счета или карты: "))
#str_date = str(input("Введите дату: "))
#
#list_name_account_n = []
#list_name_account = number.split(" ")
#for name in list_name_account:
#    if name.isalpha():
#        list_name_account_n.append(name)
#print(" ".join(list_name_account_n) + " " + mask_account_card(number))
#
#print(get_date(str_date))

list_test = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(list_test))

list_test1 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

print(sort_by_date(list_test1))#