import logging
from bot.client import BinanceFuturesClient
from bot.validators import validate_inputs

client = BinanceFuturesClient()

def place_order(symbol, side, order_type, quantity, price=None):
    validate_inputs(order_type, quantity, price)

    symbol = symbol.upper()

    try:
        # Required for Futures
        client.client.futures_change_leverage(
            symbol=symbol,
            leverage=10
        )

        logging.info(f"Leverage set to 10x for {symbol}")

        order_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            order_params["price"] = price
            order_params["timeInForce"] = "GTC"

        response = client.create_order(**order_params)

        return {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "0.00")
        }

    except Exception as e:
        logging.error(f"Order placement failed: {str(e)}")
        raise
