from src.decorators import log


def test_log():
    """Тестирование успешного выполнения функции с указанием имени файла"""

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x / y

    my_function(1, 1)
    with open("../src/log/mylog.txt", "r", encoding="utf-8") as file:
        read_text = file.readlines()
        assert "Старт функции" in read_text[0]
        assert read_text[1] == "my_function ok\n"
        assert "Стоп функции" in read_text[2]


def test_log_no_file(capsys):
    """Тестирование успешного выполнения функции без указания имени файла, вывода в консоль с фикстурой capsys"""

    @log()
    def my_function(x, y):
        return x / y

    my_function(1, 1)
    captured = capsys.readouterr()
    captured_list = captured.out.strip().split("\n")

    assert "Старт функции" in captured_list[0]
    assert captured_list[1] == "my_function ok"
    assert "Стоп функции" in captured_list[2]


def test_log_error():
    """Тестирование выполнения функции с ошибкой, с указанием имени файла"""

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x / y

    my_function(1, 0)
    with open("../src/log/mylog.txt", "r", encoding="utf-8") as file:
        read_text = file.readlines()
        assert "Старт функции" in read_text[0]
        assert "Error:" in read_text[1]
        assert "Стоп функции" in read_text[2]


def test_log_no_file_error(capsys):
    """Тестирование выполнения функции с ошибкой без указания имени файла, вывода в консоль с фикстурой capsys"""

    @log()
    def my_function(x, y):
        return x / y

    my_function(1, 0)
    captured = capsys.readouterr()
    captured_list = captured.out.strip().split("\n")

    assert "Старт функции" in captured_list[0]
    assert "Error:" in captured_list[1]
    assert "Стоп функции" in captured_list[2]
