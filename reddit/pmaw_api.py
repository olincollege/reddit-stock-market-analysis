import pandas as pd
from pmaw import PushshiftAPI
import datetime
import re

api = PushshiftAPI()


def findall_tickers(string):
    """
    Searches a string for stock tickers.

    Args:
        string: A string to be searched.

    Returns:
        A list of all the stock tickers in the string.
    """
    return re.findall(r"\$([A-Z]+)", string)


def findall_questions(string):
    """
    Searches a string for question marks.

    Args:
        string: A string to be searched.

    Returns:
        A list of all the stock tickers in the string.
    """
    return re.findall(r"(\?)", string)


def str_create_timestamp(date_str):
    """
    Docstring here
    The format of date_str will always be "XXXX-XX-XX"
    """
    year = int(date_str[0:4])
    month = int(date_str[5:7])
    day = int(date_str[8:])
    timestamp = int(datetime.datetime(
        year=year, month=month, day=day).timestamp())
    return timestamp


def remove_dupes(ticker_list):
    """
    removes empty strings and repeats
    """
    res = []
    [res.append(x) for x in ticker_list if x not in res]
    if '' in res:
        res.remove('')
    return res


def pull_raw_data(subreddit, limit, beginning_day, end_day):
    """
    Returns:
        subs_df: A dataframe containing the titles, body text, and date written
        of Reddit posts.
    """
    beginning_timestamp = str_create_timestamp(beginning_day)
    end_timestamp = str_create_timestamp(end_day)

    submissions = api.search_submissions(subreddit=subreddit, limit=limit,
                                         before=end_timestamp, after=beginning_timestamp)

    subs_df = pd.DataFrame(submissions)
    subs_df = subs_df[['title', 'selftext', 'created_utc']]
    subs_df = subs_df.sort_values(by='created_utc')
    print(len(subs_df))
    return subs_df
#all_data = subs_json['data']


def get_filtered_reddit_data(limit, beginning_day, end_day):
    """
    Docstring here
    creates a csv with only the raw data
    """

    subreddit = "wallstreetbets"

    all_data = pull_raw_data(subreddit, limit, beginning_day, end_day)

    # Init new dataframe
    df = pd.DataFrame()

    # Create a list of exixting tickers to remove posts talking about
    # the same stock. Start with SPY, our S&P500 ETF and baseline
    existing_tickers = ['SPY']

    for post in all_data.itertuples():

        title = str(post[1])
        selftext = str(post[2])
        created_utc = post[3]
        all_text = title + " " + selftext

        # Filters out all submissions that don't have a stock ticker
        # Or that contain a question mark
        # Or don't have the word long
        # or contain the word short
        if findall_tickers(all_text) and (not(findall_questions(all_text))) and (re.findall(r'[Ll]ong ', all_text)) and (not(re.findall(r'[Ss]hort ', all_text))):

            # Generate a list of all the stock tickers in a post
            #  and remove duplicates
            ticker_list = findall_tickers(all_text)
            ticker_list = remove_dupes(ticker_list)

            # filter out all but the first mention of each stock ticker
            new_ticker_list = []
            for ticker in ticker_list:
                if ticker not in existing_tickers:
                    existing_tickers.append(ticker)
                    new_ticker_list.append(ticker)

            if new_ticker_list:
                # censored_title = post['title']  #pf.censor()
                # censored_selftext = post['selftext']
                time = datetime.datetime.fromtimestamp(created_utc)

                df = pd.concat(
                    [df, pd.DataFrame({'title': [title],
                                       'selftext': [selftext],
                                       'time': [time],
                                       'tickers': [new_ticker_list]})])
    df.to_csv("reddit/reddit_subs_filtered.csv")
    return(existing_tickers)


unique_ticker_list = get_filtered_reddit_data(
    100000, "2018-01-01", "2019-01-01")

dataframe = pd.read_csv("reddit/snp500.csv")
snp_tickers = list(dataframe['Symbol'])

matching_tickers = 0
for ticker in unique_ticker_list:
    if ticker in snp_tickers:
        matching_tickers += 1
print(unique_ticker_list)
print("Number of stocks recommended by reddit: ", len(unique_ticker_list))
print("Number of recommended stocks in the S&P 500: ", matching_tickers)
