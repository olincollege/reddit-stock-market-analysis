import pytest

# Scraping and analyzing Alpaca data

from stock_info.pull_stock_info import get_datetime

# TODO: pmaw_api find tickers
# TODO: pmaw_api find_qmarks
# TODO: pmaw_api find_long
# TODO: pmaw_api find_short
# TODO: pmaw_api str_create_timestamp
# TODO: pmaw_api remove_dupes
# TODO: pull_stock_info get_datetime
# TODO: graph_stock_info days_since_epoch
# TODO: graph_stock_info date_from_epoch_time
# TODO: generate_results str_to_list





# Define sets of test cases.
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


