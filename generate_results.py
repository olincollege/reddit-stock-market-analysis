from graphing.graph_stock_info import make_color_plot
from stock_info.pull_stock_info import get_stock_info, is_valid_ticker
from reddit.pmaw_api import remove_dupes
import pandas as pd

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


def get_annual_return(path):
    """
    Given a path to a csv containing 1 years worth of data from a stock,
    find the annual return / ROI
    """
    dataframe = pd.read_csv(path)

    start_val = list(dataframe['close'])[0]
    end_val = list(dataframe['close'])[-1]

    roi = ((end_val - start_val) / start_val) * 100

    return roi


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


def generate_results(ticker, date):
    """
    Pulls from alpaca and makes graphs and stuff
    """
    # Pull data from alpaca for the stock from the reddit post
    get_stock_info(ticker, date, 365)
    # Pull data from alpaca for S&P 500 to compare
    get_stock_info("SPY", date, 365)

    # Create data paths to stock csv files
    stock_path = (f"stock_info/data/{ticker}data.csv")
    # This path will always be the same
    spy_path = "stock_info/data/SPYdata.csv"

    make_color_plot(spy_path, "SPY")

    make_color_plot(stock_path, ticker)

    spy_ar = get_annual_return(spy_path)
    stock_ar = get_annual_return(stock_path)

    print("S&P 500 One Year Return: ", spy_ar)
    print(f"{ticker} One Year Return: ", stock_ar)


def reddit_overall_comparison():
    """
    Docstring here
    """
    dataframe = pd.read_csv("reddit/reddit_subs_filtered.csv")    
    reddit_annual_returns = []
    snp_annual_returns = []

    for submission in dataframe.itertuples():
        time = submission.time[:10]
        tickers = remove_dupes(str_to_list(submission.tickers))

        for ticker in tickers:
            if is_valid_ticker(ticker):
                # Collect data on reddit recommended ticker
                get_stock_info(ticker, time, 365)
                path = (f'stock_info/data/{ticker}data.csv')
                ar = get_annual_return(path)
                reddit_annual_returns.append(ar)
                
                # Then look at S&P 500 data over the same time period
                get_stock_info("SPY", time, 365)
                path = 'stock_info/data/SPYdata.csv'
                ar = get_annual_return(path)
                snp_annual_returns.append(ar)

    average_reddit_ar = sum(reddit_annual_returns) / len(reddit_annual_returns)
    average_snp_ar = sum(snp_annual_returns) / len(snp_annual_returns)
    print("Average reddit AR: ", average_reddit_ar)
    print("Average S&P 500 AR: ", average_snp_ar)

    

reddit_overall_comparison()
