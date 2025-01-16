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
