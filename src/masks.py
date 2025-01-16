from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску
    """
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        raise ValueError("Короткий или длинный номер карты")
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Принимает на вход номер счета и возвращает его маску
    """
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        raise ValueError("Короткий или длинный номер счета")
    return f"**{str_account_number[-4:]}"
