"""
This library contains all of our unit tests for our functions.
"""
import datetime
import pytest
from generate_results import str_to_list
from graphing.graph_stock_info import (
    days_since_epoch,
    date_from_epoch_time
)
from reddit.pmaw_api import (
    str_create_timestamp,
    find_tickers,
    find_qmarks,
    find_long,
    find_short,
    str_create_timestamp,
    remove_dupes
)

# Scraping and analyzing Alpaca data

from stock_info.pull_stock_info import get_datetime

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

find_qmarks_cases = [
    # Check that any string with a question mark returns True.
    ('????!!??', True),
    # Check that any string without a question mark returns False.
    ('Hello!', False),
]

find_long_cases = [
    # Check that any string with the word "long" returns True.
    ('This is so long stocking.', True),
    # Check that any string without the word "long" returns False.
    ('This is so short.', False),
]

find_short_cases = [
    # Check that any string that contains the word "short" returns True.
    ('I am not short.', True),
    # Check that any string without "short" returns False.
    ('I am not tall.', False),
]

str_create_timestamp_cases = [
    # Check that an inputted string in datetime format will be outputted as a
    # datetime date that is an integer.
    (['2018-01-01'], 1514782800),
]

remove_dupes_cases = [
    # Check that empty strings in a list are removed.
    (['hello', '', 'hi'], ['hello', 'hi']),
    # Check that repeats in a list are removed.
    (['hello', 'hello', 'hi'], ['hello', 'hi']),
]

days_since_epoch_cases = [
    # Check that the number of days since the beginning of the epoch is correct.
    (datetime.date(1970, 1, 11), 10),
    # Check that if the inputted date is before the beginning of the epoch, a
    # negative integer is returned.
    (datetime.date(1960, 1, 11), -3653),
]

date_from_epoch_time_cases = [
    # Check that the datetime object returned is correct and aligns with the
    # beginning of the epoch and an inputted time difference of days.
    (10, datetime.date(1970, 1, 11)),
    # Check that the correct datetime object is returned when a time difference
    # of over a year is inputted.
    (366, datetime.date(1971, 1, 2)),
]

str_to_list_cases = [
    # Check that an inputted string with one comma is split determining on the
    # comma.
    ("hello, goodbye", ['hello', 'goodbye']),
    # Check that an inputted string with multiple commas is split correctly.
    ("hello, goodbye, see you again", ['hello', 'goodbye', 'see you again']),
    # Check that an inputted string with no commas outputs the original string.
    ("hello", ['hello']),
]

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

# Define additional testing lists and functions that check other properties of
# functions in gene_finder.py.


@ pytest.mark.parametrize("string,tickers", find_tickers_cases)
def test_find_tickers(string, tickers):
    """
    Check that the correct tickers are pulled out from a string.

    Args:
        string: A string representing the body or title of a Reddit post.
    """
    assert find_tickers(string) == tickers


@ pytest.mark.parametrize("string,tickers", find_tickers_cases)
def test_find_tickers(string, tickers):
    """
    Check that the correct tickers are pulled out from a string.

    Args:
        string: A string representing the body or title of a Reddit post.
    """
    assert find_tickers(string) == tickers
