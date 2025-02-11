import logging
import os
from typing import Union

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)


log_file = os.path.join(log_dir, "masks.log")
logging.basicConfig(
    filename=log_file, filemode="w", format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger("masks")


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску
    """
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        logger.error("Короткий или длинный номер карты")
        raise ValueError("Короткий или длинный номер карты")
    masked_card = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    logger.info(f"Маска номера карты создана: {masked_card}")
    return masked_card


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Принимает на вход номер счета и возвращает его маску
    """
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        logger.error("Короткий или длинный номер счета")
        raise ValueError("Короткий или длинный номер счета")
    masked_account = f"**{str_account_number[-4:]}"
    logger.info(f"Маска номера счета создана: {masked_account}")
    return masked_account
