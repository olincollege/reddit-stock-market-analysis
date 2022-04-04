import alpaca_trade_api as tradeapi
import pandas as pd
import json
from datetime import datetime, timedelta


def get_alpaca_account():
    """
    Loads the Alpaca credentials and displays the Alpaca account used to make
    the API requests. Will error if the user does not have Alpaca credentials.

    Args:
        None.

    Returns:
        account: A dictionary containing strings of information about the
        Alpaca account.
    """
    with open("stock_info/alpaca_credentials.json", "r") as file:
        creds = json.load(file)

    APCA_API_KEY_ID = creds['CLIENT_ID']
    APCA_API_SECRET_KEY = creds['CLIENT_SECRET']

    APCA_API_BASE_URL = "https://paper-API.alpaca.markets"

    API = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY,
                        APCA_API_BASE_URL, api_version='v2')
    return API


# Global Constants
API = get_alpaca_account()


def get_datetime(start_date, time_period):
    """
    Convert a start date and number of days to a start and end datetime.
    
    Args:
        start_date: A string containing the first date to pull data for in the
        format YYYY-MM-DD.
        time_period: An integer of the number of days to pull data for.
        
    Returns:
        start_date: The datetime at which to begin pulling stock information.
        end_date: The datetime at which to finish pulling stock information.
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    
    # allows the user to call a start date and a set number of days afterward
    # without having to find the end date manually
    delta = timedelta(days=time_period)
    end_date = start_date + delta
    return [start_date, end_date]


def is_valid_ticker(ticker):
    """
    Checks if a ticker symbol is valid

    Args:
        ticker: A ticker symbol

    Returns:
        True if the ticker is valid, False otherwise.
    """
    # Look for data from one day to see if we get results
    dates = get_datetime("2018-01-01", 1)
    start_date = dates[0]
    end_date = dates[1]

    any_data = API.get_bars(ticker, tradeapi.TimeFrame.Day,
                 start_date, end_date, adjustment='raw')
    if any_data:
        return True
    return False


def get_stock_info(ticker_symbol, start_date, time_period):
    """
    Creates a CSV file containing the open and close price for the desired
    stock each day.
    
    Args:
        ticker_symbol: A string of 1-4 uppercase letters representing the
        ticker symbol for the desired stock.
        start_date: A string containing the first date to pull data for in the
        format YYYY-MM-DD.
        time_period: An integer of the number of days to pull data for.
        
    Returns:
        A CSV file of the stock information containing the following headings:
        timestamp, open, high, low, close, volume, trade_count, and vwap. It
        appears in the stock_info folder.
    """
    dates = get_datetime(start_date, time_period)
    start_date = dates[0]
    end_date = dates[1]

    STOCK_DATA = API.get_bars(ticker_symbol, tradeapi.TimeFrame.Day,
                              start_date, end_date, adjustment='raw').df
    STOCK_DATA.to_csv(f'stock_info/data/{ticker_symbol}data.csv')
    return
