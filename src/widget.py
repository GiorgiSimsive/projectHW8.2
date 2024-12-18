from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_type_and_number: str) -> str:
    """
    Обрабатывает информацию как о картах, так и о счетах
    """
    parts = card_type_and_number.split()
    title = " ".join(parts[:-1])
    number = parts[-1]

    if len(number) == 16:
        hidden_number = get_mask_card_number(number)
    else:
        hidden_number = get_mask_account(number)
    return f"{title} {hidden_number}"


def get_date(date_format: str) -> str:
    """
    Меняет даты в формате "ДД.ММ.ГГГГ"
    """
    new_date_format = date_format[0:10].split("-")
    return ".".join(new_date_format[::-1])
