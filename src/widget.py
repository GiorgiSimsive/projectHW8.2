from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_type_and_number: str) -> str:
    """
    Обрабатывает информацию как о картах, так и о счетах
    """
    if len(card_type_and_number.split()[-1]) == 16:
        new_number1 = get_mask_card_number(card_type_and_number.split()[-1])
        return f"{card_type_and_number[:-17]} {new_number1}"
    elif len(card_type_and_number.split()[-1]) == 20:
        new_number2 = get_mask_account(card_type_and_number.split()[-1])
        return f"{card_type_and_number[:-21]} **{new_number2[-4:]}"


def get_date(date_format: str) -> str:
    """
    Меняет даты в формате "ДД.ММ.ГГГГ"
    """
    new_date_format = date_format[0:10].split("-")
    return ".".join(new_date_format[::-1])
