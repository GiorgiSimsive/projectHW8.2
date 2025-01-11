def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list, descending: bool = True) -> list:
    """
    Сортирует по дате новый список
    """
    return sorted(data, key=lambda x: x["date"], reverse=descending)
