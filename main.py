from binance.client import Client
from binance.enums import *
import logging

# ---------- SET UP LOGGING ----------
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# ---------- BASIC BOT CLASS ----------
class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        # Use Spot Testnet base URL
        self.client.API_URL = 'https://testnet.binance.vision/api'
        logging.info("Bot initialized.")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market Order: {order}")
            print(f"Market order placed: {order}")
        except Exception as e:
            logging.error(f"Market Order Error: {str(e)}")
            print(f"Error placing market order: {str(e)}")

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit Order: {order}")
            print(f"Limit order placed: {order}")
        except Exception as e:
            logging.error(f"Limit Order Error: {str(e)}")
            print(f"Error placing limit order: {str(e)}")

# ---------- MAIN ENTRY POINT ----------
if __name__ == '__main__':
    api_key = "L4JHCGVDaFpHe2HLFIAVlfPzA4MDfoIN6wXCISMZxTUgZImLZIrw1IeSrmcaNndO"
    api_secret = "dgQ8kYGQnz84AbWAkxgReEpql8at0RtBDtQs8ZK51SxrhvUuoHaH59C683z2XbvV"

    bot = BasicBot(api_key, api_secret)

    while True:
        print("\nOptions:")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Symbol (e.g., BTCUSDT): ").upper()
            side = input("Side (buy/sell): ").lower()
            quantity = input("Quantity: ")
            bot.place_market_order(symbol, side, quantity)

        elif choice == '2':
            symbol = input("Symbol (e.g., BTCUSDT): ").upper()
            side = input("Side (buy/sell): ").lower()
            quantity = input("Quantity: ")
            price = input("Price: ")
            bot.place_limit_order(symbol, side, quantity, price)

        elif choice == '3':

            print("Goodbye 👋")
            break

        else:
            print("Invalid option. Try again.")
