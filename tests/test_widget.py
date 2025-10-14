import pytest

from src.widget import get_date, mask_account_card


def test_mask_card_number() -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_typ_error() -> None:
    with pytest.raises(TypeError):
        mask_account_card(1234567890)  # type: ignore


def test_value_error_empty_input() -> None:
    with pytest.raises(ValueError):
        mask_account_card("VISA")


def test_get_date() -> None:
    assert get_date("2025-01-11") == "11.01.2025"


def test_error_get_date() -> None:
    with pytest.raises(ValueError):
        get_date("2025-01")
