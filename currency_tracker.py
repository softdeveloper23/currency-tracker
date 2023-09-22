import requests


def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]


api_key = "e03da58520764a309704cb57e64dee00"
eur_to_usd = get_exchange_rate("EUR", "USD", api_key)
print(f"1 EUR = {eur_to_usd} USD")
