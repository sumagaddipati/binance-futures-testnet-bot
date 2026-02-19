# Binance Futures Testnet Trading Bot (Python)

## Overview
This project is a simplified Python trading bot that places orders on **Binance Futures Testnet (USDT-M)**.  
It demonstrates clean code structure, CLI-based input handling, logging, validation, and error handling.

The bot supports:
- MARKET orders  
- LIMIT orders  
- BUY and SELL sides  

This project is intended as a technical assessment and focuses on correctness, structure, and robustness rather than trading strategy.

---

## Tech Stack
- Python 3.x  
- python-binance  
- argparse  
- logging  

---

## Project Structure

trading_bot/
│
├── bot/
│ ├── init.py

│ ├── client.py # Binance Futures testnet client

│ ├── orders.py # Order placement logic

│ ├── validators.py # Input validation

│ └── logging_config.py # Logging configuration
│
├── logs/
│ └── bot.log # API request/response logs
│
├── cli.py # CLI entry point

├── requirements.txt

└── README.md


---

## Setup Instructions

### 1. Clone the repository
git clone <your-repo-url>
cd trading_bot

### 2. Create and activate virtual environment
python -m venv venv
Windows

venv\Scripts\activate
Linux / macOS

source venv/bin/activate
### 3. Install dependencies
pip install -r requirements.txt

### 4. Set Environment Variables (Binance Futures Testnet)
Windows (PowerShell):

setx BINANCE_API_KEY "your_testnet_api_key"
setx BINANCE_API_SECRET "your_testnet_secret_key"
Restart the terminal after setting variables.

### How to Run
### MARKET Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
### LIMIT Order Example
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 60000
### Output
### The CLI prints:

Order request summary

Order ID

Order status

Executed quantity

Average price (if available)

All API requests, responses, and errors are logged to:

logs/bot.log
Logging
The log file contains:

One MARKET order log

One LIMIT order log

API request and response details

Error handling records

Assumptions & Notes
Uses Binance Futures Testnet (USDT-M) only

No real funds involved

Testnet liquidity is limited, so orders may remain in NEW state

executedQty and avgPrice may be 0 if the order is not filled

### Conclusion
This project demonstrates correct Binance Futures API usage, clean architecture, validation, logging, and CLI interaction, suitable for technical evaluation.
