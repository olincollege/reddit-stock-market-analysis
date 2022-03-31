from graphing.graph_stock_info import make_color_plot
from pull_stock_info import get_stock_info



def generate_results(ticker, date):
    """
    Pulls from alpaca and makes graphs and stuff
    """
    # Pull data from alpaca for the stock from the reddit post
    get_stock_info(ticker, date, 365)
    # Pull data from alpaca for S&P 500 to compare
    get_stock_info("SPY", date, 365)

    # Create data paths to stock csv files
    csv_path = (f"stock_info/data/{ticker}data.csv")
    # This path will always be the same
    spy_path = "stock_info/data/SPYdata.csv"

    make_color_plot(csv_path, ticker)

    make_color_plot(spy_path, "SPY")
    

    return