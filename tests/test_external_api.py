from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convert_currency, process_transaction


@pytest.fixture
def mock_requests_get():  # type: ignore
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 75.0}
        mock_get.return_value = mock_response
        yield mock_get


def test_convert_currency(mock_requests_get: MagicMock) -> None:
    result = convert_currency(1, "USD")
    assert result == 75.0


@patch("src.external_api.convert_currency", return_value=75.0)
def test_process_transaction_usd(mock_convert: MagicMock) -> None:
    transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}
    result = process_transaction(transaction)
    assert result == 75.0
    mock_convert.assert_called_once_with(1.0, "USD")


def test_process_transaction_rub() -> None:
    transaction = {"operationAmount": {"amount": 1000, "currency": {"code": "RUB"}}}
    result = process_transaction(transaction)
    assert result == 1000


def test_process_transaction_invalid() -> None:
    transaction = {"operationAmount": {"amount": 1000}}
    with pytest.raises(ValueError):
        process_transaction(transaction)
