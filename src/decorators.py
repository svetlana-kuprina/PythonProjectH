from datetime import datetime
from functools import wraps


def log(filename=""):
    """Декоратор логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = datetime.now()
            if filename:
                with open("../src/log/" + filename, "w", encoding="utf-8") as file:
                    time_start_file = "Старт функции: " + str(time_start) + "\n"
                    file.write(time_start_file)
            else:
                print(f"Старт функции: {time_start}")
            try:

                result = func(*args, **kwargs)
                time_end = datetime.now()
                if filename:
                    with open("../src/log/" + filename, "a+", encoding="utf-8") as file:
                        time_stop_file = str(func.__name__) + " ok" + "\n" + "Стоп функции: " + str(time_end) + "\n"
                        file.write(time_stop_file)
                else:
                    print(f"{str(func.__name__)} ok\nСтоп функции: {time_end}")
                return result

            except Exception as exp:
                if filename:
                    with open("../src/log/" + filename, "a+", encoding="utf-8") as file:
                        file.write(
                            str(func.__name__)
                            + " Error: "
                            + str(exp)
                            + "."
                            + " Inputs: "
                            + str(args)
                            + ","
                            + str(kwargs)
                            + "\n"
                            + "Стоп функции: "
                            + str(datetime.now())
                            + "\n"
                        )
                else:
                    print(
                        f"{str(func.__name__)} Error: {str(exp)}. Inputs: {str(args)}, {str(kwargs)} \nСтоп функции: {str(datetime.now())}"
                    )

        return wrapper

    return decorator
