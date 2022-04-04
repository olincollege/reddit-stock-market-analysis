"""
Test library functions to identify and graph the prices of Reddit-recommended
stocks.
"""
import datetime
import pytest

from generate_results import str_to_list
from graphing.graph_stock_info import (days_since_epoch, date_from_epoch_time)
from reddit.pmaw_api import (find_qmarks, find_long, find_short,
                             str_create_timestamp)
from stock_info.pull_stock_info import get_datetime

# TODO: pmaw_api find tickers
find_tickers_cases = [
    # Check that a string with no tickers returns an empty list.
    ("something with words", []),
    # Check that capital letters without a dollar sign are not counted.
    ("CAPITAL LETTERS", []),
    # Check that a valid ticker symbol is recorded
    ("Words$TSLA more wWORds", ['TSLA']),
    # Check that multiple ticker symbols are recorded
    ("Long $TSLA & $AAPLto be cool", ['TSLA', 'APPL']),
]


# TODO: pmaw_api find_qmarks
# TODO: pmaw_api find_long
# TODO: pmaw_api find_short
# TODO: pmaw_api str_create_timestamp
# TODO: pmaw_api remove_dupes
# TODO: graph_stock_info days_since_epoch
# TODO: graph_stock_info date_from_epoch_time
# TODO: generate_results str_to_list





# TODO: pull_stock_info get_datetime
get_datetime_cases = [
    # Check that a simple addition case returns a datetime.date object.
    ("2022-01-01", 10, [datetime.date(2022, 1, 1), 
                        datetime.date(2022, 1, 11)]),
    # Check addition for months.
    ("2022-01-01", 32, [datetime.date(2022, 1, 1), 
                        datetime.date(2022, 2, 1)]),
    # Check addition for years.
    ("2021-01-01", 365, [datetime.date(2021, 1, 1), 
                        datetime.date(2022, 1, 1)]),
]


