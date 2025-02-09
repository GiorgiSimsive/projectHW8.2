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


def process_transaction(amount: float, currency: str) -> float:
    """
    Принимает сумму транзакции и валюту.
    Возвращает сумму транзакции в рублях.
    """
    if currency == "USD" or currency == "EUR":
        return convert_currency(amount, currency)
    else:
        return amount
