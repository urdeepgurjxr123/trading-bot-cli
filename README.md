# 🚀 Trading Bot CLI (Python)

A modular, scalable, and production-style command-line trading bot built using Python.
This project simulates cryptocurrency trading operations with proper architecture, validation, and logging — designed to reflect real-world backend systems.

---

## 📌 Overview

This project demonstrates how a real trading bot works internally using a clean layered architecture:

* 🖥️ **CLI Layer** → Takes user input
* ✅ **Validation Layer** → Ensures correct data
* ⚙️ **Service Layer** → Handles business logic
* 🔌 **Client Layer** → Simulates API interaction

> ⚠️ Note: This project runs in **simulation mode** (no real trades executed).

---

## ✨ Features

* 📊 Command-line based trading system
* 🔁 Supports MARKET and LIMIT orders
* ✅ Strong input validation (symbol, side, quantity, price)
* 🧾 Logging system for tracking orders and errors
* 🧱 Clean and modular architecture
* 🔒 Environment variable support using `.env`
* ⚡ Robust error handling

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Simulated API layer
│   ├── orders.py          # Business logic layer
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging configuration
│
├── cli.py                 # Entry point (CLI interface)
├── .env                   # Environment variables
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

## ⚙️ Tech Stack

* Python 3.x
* python-dotenv
* argparse (built-in)
* logging (built-in)

---

## 🚀 Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/trading-bot-cli.git
cd trading-bot-cli
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔹 MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 🔹 LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000
```

---

## 🧪 Sample Output

```
✅ ORDER PLACED SUCCESSFULLY

{
  "orderId": 123456,
  "status": "FILLED",
  "symbol": "BTCUSDT",
  "side": "BUY",
  "type": "MARKET",
  "executedQty": 0.001,
  "avgPrice": "simulated_market_price"
}
```

---

## 📝 Logging

All activities (orders, errors, validations) are logged in:

```
trading_bot.log
```

Example log:

```
2026-04-22 10:00:00 - INFO - Placing order: BTCUSDT BUY MARKET 0.001
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

> Currently used for structure demonstration (no real API calls).

---

## ⚠️ Limitations

* No real API integration (simulation mode)
* No real-time market data
* No trading strategies implemented

---

## 🔮 Future Improvements

* 🔗 Integration with Binance Testnet API
* 📈 Real-time price tracking
* 🤖 Strategy-based automated trading
* 🌐 Web dashboard / GUI
* 📊 Backtesting system

---

## 💡 Learning Outcomes

* Clean Architecture Design
* CLI Application Development
* Input Validation Techniques
* Logging & Debugging
* Writing Production-Ready Code

---

## 👨‍💻 Author

Deepak Vikal


