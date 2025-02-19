from flask import Flask, request, jsonify
import os
from pybit.unified_trading import HTTP

app = Flask(__name__)

# Bybit API bağlantısı
session = HTTP(
    api_key="8gks2c4UYUcMRfgKVq",
    api_secret="DTosWpDzt0NZEEszVw2ZFtKCC378wnQamzAi",
)

@app.route("/")
def home():
    return "TradingView Bybit Bot Çalışıyor!"

@app.route("/bybit-balance", methods=["GET"])
def get_balance():
    try:
        balance = session.get_wallet_balance(accountType="UNIFIED")
        return jsonify(balance)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
