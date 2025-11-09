import json
import logging
import os

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
log_directory = os.path.join(os.path.dirname(__file__), "../logs", "utils.log")
file_handler = logging.FileHandler(log_directory, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_json_file(json_file: str) -> list[dict]:
    """Функция принимат путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data_file = json.load(f)
            if data_file is None:
                logger.error("Данные отсутствуют")
                data_file = []
                return data_file
            elif type(data_file) is not list:
                logger.error("Не верный формат данных")
                data_file = []
                return data_file
    except FileNotFoundError:
        logger.critical("Файл не найден")
        data_file = []
        return data_file
    except json.JSONDecodeError:
        logger.error("Данные не соответствуют формату JSON")
        data_file = []
        return data_file

    logger.info("Данные успешно прочитаны с JSON-файла")
    return data_file
