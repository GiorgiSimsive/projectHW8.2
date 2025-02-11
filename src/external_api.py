import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_currency(amount: float, from_currency: str, to_currency: str = "RUB") -> float:
    """
    Конвертирует сумму в валюте from_currency в рубли (RUB)
    """
    url = f"{BASE_URL}?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        result = float(data["result"])
        return result
    else:
        raise Exception(f"Ошибка при запросе курса валют: {response.status_code}")


def process_transaction(transaction: dict) -> float:
    """
    Принимает словарь транзакции.
    Извлекает сумму и валюту, возвращает сумму в рублях.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount = operation_amount.get("amount")
    currency = operation_amount.get("currency", {}).get("code")

    if amount is None or currency is None:
        raise ValueError("Некорректные данные транзакции: отсутствуют ключи 'amount' или 'currency'")

    if currency == "RUB":
        return float(amount)

    return convert_currency(float(amount), currency)
