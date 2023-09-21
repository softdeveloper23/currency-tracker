import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import requests


def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]


def update_exchange_rate():
    eur_to_usd = get_exchange_rate("EUR", "USD")
    exchange_rate_label.setText(f"1 EUR = {eur_to_usd:.2f} USD")


app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

exchange_rate_label = QLabel()
update_exchange_rate()

update_button = QPushButton("Update Exchange Rate")
update_button.clicked.connect(update_exchange_rate)

layout.addWidget(exchange_rate_label)
layout.addWidget(update_button)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
