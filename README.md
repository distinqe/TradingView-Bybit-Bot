# TradingView-Bybit-Bot

Bu proje, TradingView sinyallerini Bybit API üzerinden otomatik işlem yapacak şekilde bağlamak için oluşturulmuştur.

## Kullanım

1. `main.py` dosyasındaki Bybit API anahtarlarını ayarla.
2. Render veya farklı bir sunucuya deploy et.
3. `https://tradingview-bybit-bot.onrender.com/bybit-balance` adresinden API bağlantısını test et.

## Çevre Değişkenleri (Environment Variables)

Aşağıdaki değişkenleri Render'da tanımlaman gerekiyor:

- `BYBIT_API_KEY` → Bybit API Key
- `BYBIT_API_SECRET` → Bybit Secret Key
- `PORT` → 8000

## Kurulum ve Çalıştırma

```bash
pip install -r requirements.txt
python main.py
