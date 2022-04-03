from graphing.graph_stock_info import make_color_plot
from stock_info.pull_stock_info import get_stock_info
from stock_info.annual_return import get_annual_return



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
    return