import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def converter(quote: str,  base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_ticker}&symbols={quote_ticker}')
        resp = json.loads(r.content)
        new_price = resp['rates'][quote_ticker] * amount
        new_price = round(new_price, 3)
        total_price =  f"Цена {amount} {base} в {quote} : {new_price}"


        return total_price