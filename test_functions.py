import pytest

# Scraping and analyzing Alpaca data

from stock_info.pull_stock_info import get_datetime

# Define sets of test cases.
get_datetime_cases = [
    # Check that the complement of A is T.
    ("A", "T"),
]
