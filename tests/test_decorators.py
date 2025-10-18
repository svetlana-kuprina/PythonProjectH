import pytest
from src.decorators import log


def test_log():
    @log(filename='mylog.txt')
    def my_function(x, y):
        return x / y

    my_function(1, 1)
    with open("log/mylog.txt", 'r', encoding="utf-8") as file:
        result = file.read()
    assert result == 'Старт функции: 2025-10-18 15:58:42.527848\nmy_function ok\nСтоп функции: 2025-10-18 15:58:42.530339\n'

def test_log_no_file(capsys):
    @log()
    def my_function(x, y):
        return x / y

    my_function(1, 1)
    captured = capsys.readouterr()
    assert captured.out == 'Старт функции: 2025-10-18 15:58:42.527848\nmy_function ok\nСтоп функции: 2025-10-18 15:58:42.530339\n'
