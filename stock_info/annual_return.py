"""
Library for obtaining the annual return for a single stock.

The function get_annual_return allows us to obtain the ROI for a specific stock
using its market closing price per day and finding the first and last day for
the time we input.
"""
import pandas as pd


def get_annual_return(path):
    """
    Given a path to a csv containing 1 years worth of data from a stock,
    find the annual return / ROI.

    Args:
        path: A path to a csv file containing stock tickers.

    Returns:
        An integer representing the ROI of a stock.
    """
    dataframe = pd.read_csv(path)

    start_val = list(dataframe['close'])[0]
    end_val = list(dataframe['close'])[-1]

    roi = ((end_val - start_val) / start_val) * 100

    return roi
