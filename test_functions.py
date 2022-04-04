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
# TODO: pmaw_api remove_dupes_cases
remove_dupes_cases = [
    # Check that empty strings in a list are removed.
    (['hello', '', 'hi'], ['hello', 'hi']),
    # Check that repeats in a list are removed.
    (['hello', 'hello', 'hi'], ['hello', 'hi']),
]
# TODO: graph_stock_info days_since_epoch
days_since_epoch_cases = [
    # Check that the number of days since the beginning of the epoch is correct.
    (datetime.date(1970, 1, 11), 10),
]
# TODO: graph_stock_info date_from_epoch_time
date_from_epoch_time_cases = [
    # Check that the datetime object returned is correct and aligns with the
    # beginning of the epoch and the time difference.
    (10, datetime.date(1970, 1, 11)),
]
# TODO: generate_results str_to_list
str_to_list_cases = [
    # Check that an inputted string with one comma is split determining on the
    # comma.
    ("hello, goodbye", ['hello', 'goodbye']),
    # Check that an inputted string with multiple commas is split correctly.
    ("hello, goodbye, see you again", ['hello', 'goodbye', 'see you again']),
    # Check that an inputted string with no commas outputs the original string.
    ("hello", ['hello']),
]
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

