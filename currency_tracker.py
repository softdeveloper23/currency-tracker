import requests


def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]


eur_to_usd = get_exchange_rate("EUR", "USD")
print(f"1 EUR = {eur_to_usd} USD")
