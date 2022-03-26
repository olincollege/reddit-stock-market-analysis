Things to write unit tests for:

- In pull_stock_info.py, make sure timedelta does addition correctly
- In pull_stock_info.py, check that the string is being properly converted to datetime
- In all .py files, check that every function has a docstring


How to narrow down r/wallstreetbets posts:
- filter out promoted posts
- filter out posts containing videos
- keep posts containing a dollar sign followed by one or more capital letters (usually telling users to invest)
- keep posts containing a dollar sign followed by a number (usually indicates a merger)
    - look for company name in the post