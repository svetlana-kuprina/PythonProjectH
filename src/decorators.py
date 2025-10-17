from datetime import time, datetime
from functools import wraps


def log(filename=''):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = datetime.now()
            if filename:
                with open("data/" + filename, 'a+', encoding="utf-8") as file:
                    time_start_file = 'Старт функции: ' + str(time_start) + "\n"
                    file.write(time_start_file)
            else:
                print(f"Старт функции: {time_start}")
            try:
                result = func(*args, **kwargs)
                time_end = datetime.now()
                if filename:
                    with open("data/" + filename, 'a+', encoding="utf-8") as file:
                        time_stop_file = 'Стоп функции: ' + str(time_end) + "\n"
                        file.write(time_stop_file)
                else:
                    print(f"Стоп функции: {time_end}")
                return result
            except Exception as exp:

                if filename:
                    with open("data/" + filename, 'a+', encoding="utf-8") as file:
                        file.write('Error: ' + str(exp) + ' ' + str(datetime.now()) + "\n")
                else:
                    print(f"Error: {exp}")

        return wrapper

    return decorator


if __name__ == '__main__':
    @log(filename='mylog.txt')
    def my_function(x, y):
        return x / y


    my_function(1, 0)
