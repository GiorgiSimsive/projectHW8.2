from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 4,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "GBP", "code": "GBP"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


def test_filter_usd(transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_eur(transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(transactions, "EUR"))
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_gbp(transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(transactions, "GBP"))
    assert len(result) == 1
    assert result[0]["id"] == 4


def test_filter_nonexistent_currency(transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(transactions, "JPY"))
    assert len(result) == 0


def test_transaction_descriptions(transactions: List[Dict[str, Any]]) -> None:
    descriptions = transaction_descriptions(transactions)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"

    with pytest.raises(StopIteration):
        next(descriptions)


def test_empty_transactions() -> None:
    descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(descriptions)


def test_card_number_generator() -> None:
    result = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected


def test_card_number_generator_large_range() -> None:
    result = list(card_number_generator(9999999999999995, 9999999999999999))
    expected = [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
    assert result == expected


@pytest.mark.parametrize(  # type: ignore
    "transactions, expected",
    [
        ([{"description": "Purchase"}], ["Purchase"]),
        ([{"description": ""}], []),
        ([{}], []),
        ([{"description": "Transfer"}, {"description": "Refund"}], ["Transfer", "Refund"]),
    ],
)
def test_transaction_descriptions(transactions, expected):  # type: ignore
    result = list(transaction_descriptions(transactions))
    assert result == expected


@pytest.mark.parametrize(  # type: ignore
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1234, 1235, ["0000 0000 0000 1234", "0000 0000 0000 1235"]),
        (0, 0, ["0000 0000 0000 0000"]),
    ],
)
def test_card_number_generator(start, end, expected):  # type: ignore
    result = list(card_number_generator(start, end))
    assert result == expected
