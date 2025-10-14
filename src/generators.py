from typing import Dict, Generator, Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[Dict]:
    """
    Поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    return (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описания операций из списка транзакций
    """
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        yield (
            f"{number:016}"[:4]
            + " "
            + f"{number:016}"[4:8]
            + " "
            + f"{number:016}"[8:12]
            + " "
            + f"{number:016}"[12:16]
        )
