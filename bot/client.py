import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


class BinanceClient:
    def __init__(self):
        self.api_key = API_KEY
        self.api_secret = API_SECRET

    def place_order(self, symbol, side, order_type, quantity, price=None):
        # Simulated response (since we are not using real/testnet API)
        
        if order_type == "MARKET":
            return {
                "orderId": 123456,
                "status": "FILLED",
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "executedQty": quantity,
                "avgPrice": "simulated_market_price"
            }

        elif order_type == "LIMIT":
            if price is None:
                raise ValueError("Price required for LIMIT order")

            return {
                "orderId": 654321,
                "status": "NEW",
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "price": price,
                "quantity": quantity
            }

        else:
            raise ValueError("Invalid order type")