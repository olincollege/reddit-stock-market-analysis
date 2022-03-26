import alpaca_trade_api as tradeapi
import matplotlib.pyplot as plt
import pandas as pd
import json
import datetime

with open("stock_info/alpaca_credentials.json", "r") as file:
    creds = json.load(file)

APCA_API_KEY_ID = creds['CLIENT_ID']
APCA_API_SECRET_KEY = creds['CLIENT_SECRET']

APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
APCA_API_DATA_URL = "https://data.alpaca.markets"
APCA_RETRY_MAX = 3
APCA_RETRY_WAIT = 3
APCA_RETRY_CODES = 429504

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL,
                    api_version='v2')


account = api.get_account()
print(account)

def get_stock_info(ticker_symbol, start_date, timedelta):
    """
    Creates a CSV file containing the open and close price for the inputted
    stock each day.
    
    Args:
        ticker_symbol: A string of 1-4 uppercase letters representing the
        ticker symbol for the desired stock.
        start_date: A string containing the first date to pull data for in the
        format YYYY-MM-DD.
        timedelta: An integer of the number of days to pull data for.
        
    Returns:
        A CSV file of the stock information containing the following headings:
        timestamp, open, high, low, close, volume, trade_count, and vwap. It
        appears in the stock_info folder.
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    print(start_date)
    end_date = start_date + timedelta
    print(end_date)
    # STOCK_DATA = api.get_bars(ticker_symbol, tradeapi.TimeFrame.Day,
    #                           start_date, end_date, adjustment='raw').df
    # print(STOCK_DATA.head())
    # STOCK_DATA.to_csv(f'stock_info/{ticker_symbol}data.csv')
    return


