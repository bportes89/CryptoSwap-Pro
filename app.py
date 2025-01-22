from flask import Flask, render_template
import requests

app = Flask(__name__)

# API da CoinGecko para obter preços de criptomoedas
API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Lista de criptomoedas suportadas
CRYPTO_CURRENCIES = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "binancecoin": "BNB",
    "ripple": "XRP",
    "cardano": "ADA"
}

# Rota principal (página inicial)
@app.route("/")
def index():
    # Obter notícias de criptomoedas
    news_response = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=PT')
    news_data = news_response.json()
    latest_news = news_data['Data'][:5]  # Pegar as 5 primeiras notícias

    return render_template("index.html", cryptos=CRYPTO_CURRENCIES, news=latest_news)

if __name__ == "__main__":
    app.run(debug=True)