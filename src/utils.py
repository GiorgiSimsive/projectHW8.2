import json
import logging
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)


log_file = os.path.join(log_dir, "utils.log")
logging.basicConfig(
    filename=log_file, filemode="w", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger("utils")


def load_transactions(file_path: str) -> list:
    """
    Загружает данные о финансовых транзакциях из JSON-файла
    """
    if not os.path.exists(file_path):
        logger.warning(f"Файл {file_path} не найден. Возвращен пустой список.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно загружены {len(data)} транзакций из {file_path}.")
                return data
            else:
                logger.error(f"Некорректный формат данных в файле {file_path}.")
    except (json.JSONDecodeError, OSError):
        logger.error(f"Ошибка декодирования JSON в файле {file_path}.")

    return []
