import argparse
from bot.orders import execute_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger

logger = setup_logger()

parser = argparse.ArgumentParser(description="Trading Bot CLI")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

args = parser.parse_args()

try:
    symbol = validate_symbol(args.symbol)
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)
    price = validate_price(args.price, order_type)

    logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

    result = execute_order(symbol, side, order_type, quantity, price)

    if result["success"]:
        logger.info(f"Order Success: {result['data']}")
        print("\n✅ ORDER PLACED SUCCESSFULLY")
        print(result["data"])
    else:
        logger.error(f"Order Failed: {result['error']}")
        print("\n❌ ORDER FAILED")
        print(result["error"])

except Exception as e:
    logger.error(f"Validation Error: {str(e)}")
    print("\n⚠️ VALIDATION ERROR")
    print(str(e))