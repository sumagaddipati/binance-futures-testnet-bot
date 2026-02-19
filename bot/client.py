import os
import time
import logging
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise EnvironmentError("API keys not found in environment variables")

        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        # ✅ Correct timestamp sync
        server_time = self.client.get_server_time()["serverTime"]
        local_time = int(time.time() * 1000)
        self.client.timestamp_offset = server_time - local_time

        logging.info("Binance Futures Testnet client initialized")

    def create_order(self, **params):
        try:
            params["recvWindow"] = 20000
            logging.info(f"Order request: {params}")
            response = self.client.futures_create_order(**params)
            logging.info(f"Order response: {response}")
            return response
        except Exception as e:
            logging.error(f"API error: {str(e)}")
            raise
