from bot.logging_config import setup_logger
setup_logger()   # 🔥 MUST be first

import argparse
import logging
from bot.orders import place_order

def main():
    logging.info("CLI started")

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        print("\nOrder Request")
        print(vars(args))

        result = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\nOrder Successful")
        for k, v in result.items():
            print(f"{k}: {v}")

    except Exception as e:
        print("\nOrder Failed")
        print(str(e))

if __name__ == "__main__":
    main()
