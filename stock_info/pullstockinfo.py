import alpaca_trade_api as tradeapi
import matplotlib.pyplot as plt
import json

with open("stock_info/alpaca_credentials.json", "r") as file:
    creds = json.load(file)

APCA_API_KEY_ID = creds['CLIENT_ID']
APCA_API_SECRET_KEY = creds['CLIENT_SECRET']

APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
APCA_API_DATA_URL = "https://data.alpaca.markets"
APCA_RETRY_MAX = 3
APCA_RETRY_WAIT = 3
APCA_RETRY_CODES = 429504

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL, api_version='v2')


account = api.get_account()
print(account)


# Fetch Apple data from last 100 days
TESLA_DATA = api.get_bars("TSLA", tradeapi.TimeFrame.Day, "2021-06-01", "2021-07-01", adjustment='raw').df

print(TESLA_DATA)


