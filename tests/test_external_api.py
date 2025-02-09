from unittest.mock import MagicMock, patch

from src.external_api import convert_currency, process_transaction


@patch("requests.get")
def test_convert_currency(mock_get) -> None:  # type: ignore
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 1000.0}
    mock_get.return_value = mock_response

    result = convert_currency(1, "USD")
    assert result == 1000.0


@patch("src.external_api.convert_currency")
def test_process_transaction_usd(mock_convert) -> None:  # type: ignore
    mock_convert.return_value = 1000.0

    result = process_transaction(1, "USD")
    assert result == 1000.0


@patch("src.external_api.convert_currency")
def test_process_transaction_eur(mock_convert) -> None:  # type: ignore
    mock_convert.return_value = 90.0
    result = process_transaction(1, "EUR")
    assert result == 90.0


def test_process_transaction_other_currency() -> None:
    result = process_transaction(100, "GBP")
    assert result == 100
