import re
from collections import defaultdict


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
    """
    if not isinstance(data, list):
        raise TypeError("Ожидается список словарей.")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка должны быть словарями.")
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list, descending: bool = True) -> list:
    """
    Сортирует по дате новый список
    """
    if not isinstance(data, list):
        raise TypeError("Ожидается список словарей.")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка должны быть словарями.")
    if not all("date" in item for item in data):
        raise KeyError("Каждый словарь должен содержать ключ 'date'.")
    return sorted(data, key=lambda x: x["date"], reverse=descending)


def filter_transactions_by_description(transactions, search_string):  # type: ignore
    """
    Фильтрует список банковских операций по наличию строки поиска в описании.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions, categories):  # type: ignore
    """
    Подсчитывает количество банковских операций в каждой категории.
    """
    category_counts = defaultdict(int)

    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
    for category in categories:
        if category not in category_counts:
            category_counts[category] = 0

    return dict(category_counts)
