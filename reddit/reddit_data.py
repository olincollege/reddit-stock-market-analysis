import pandas as pd
from stock_info.pull_stock_info import is_valid_ticker

def str_to_list(list_string):
    """
    Takes a string that is formatted like a list of strings and converts it to
    a list.

    Args:
        list_string: A string in the format "['item 1', 'item 2'].

    returns:
        A list of the string elements from the list string.
    """
    return list_string[2:-2].split("', '")


def get_reddit_stock_info():
    """
    Doctring here
    """
    # Pull S&P 500 stock ticker list from csv file
    dataframe = pd.read_csv("reddit/snp500.csv")
    snp_tickers = list(dataframe['Symbol'])

    # Pull reddit submission info from csv file
    dataframe = pd.read_csv("reddit/reddit_subs_filtered.csv")

    matching_tickers = 0
    valid_stocks = []
    # itertuples maintains data format, but lists become strings
    for submission in dataframe.itertuples():

        ticker_str = submission.tickers
        tickers = str_to_list(ticker_str)
        
        for ticker in tickers:
            if is_valid_ticker(ticker):
                valid_stocks.append(ticker)
            if ticker in snp_tickers:
                matching_tickers += 1

    print(valid_stocks)
    print("Number of stocks recommended by reddit: ", len(valid_stocks))
    print("Number of recommended stocks in the S&P 500: ", matching_tickers)
