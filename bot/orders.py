from bot.client import BinanceClient

client = BinanceClient()


def execute_order(symbol, side, order_type, quantity, price=None):
    try:
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        return {
            "success": True,
            "data": response
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }