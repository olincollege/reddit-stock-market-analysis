import pandas as pd
from pmaw import PushshiftAPI
import datetime
import re

api = PushshiftAPI()


def find_tickers(string):
    """
    Searches a string for stock tickers.

    Args:
        string: A string to be searched.

    Returns:
        A list of all the stock tickers in the string.
    """
    return re.findall(r"\$([A-Z]+)", string)


def find_qmarks(string):
    """
    Searches a string for question marks.

    Args:
        string: A string to be searched.

    Returns:
        A list of question marks in the string.
    """
    q_list = re.findall(r"(\?)", string)
    if q_list:
        return True
    return False


def find_long(string):
    """
    Searches a string for the word long.

    Args:
        string: A string to be searched.

    Returns:
        A list of all of the word long as it appears in string.
    """
    long_list = re.findall(r'[Ll]ong ', string)
    if long_list:
        return True
    return False


def find_short(string):
    """
    Searches a string for the word short.

    Args:
        string: A string to be searched.

    Returns:
        A list of the word short as it appears in the string.
    """
    short_list = re.findall(r'[Ss]hort ', string)
    if short_list:
        return True
    return False


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
    creates a csv with the filtered data
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

        # Removes reddit submissions that don't contain a stock ticker or
        # the word long.
        # Removes reddit submissions that contain a question mark or
        # the word short.
        if find_tickers(all_text) and (not(find_qmarks(all_text))) and \
            (find_long(all_text)) and (not(find_short(all_text))):

            # Generate a list of all the stock tickers in a post
            #  and remove duplicates
            ticker_list = find_tickers(all_text)
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

                # Add specific, relevant information from the reddit submission
                # to our dataframe.
                df = pd.concat(
                    [df, pd.DataFrame({'title': [title],
                                       'selftext': [selftext],
                                       'time': [time],
                                       'tickers': [new_ticker_list]})])
    df.to_csv("reddit/reddit_subs_filtered.csv")
    return(existing_tickers)


reddit_tickers = get_filtered_reddit_data(100000, "2018-01-01", "2019-01-01")

dataframe = pd.read_csv("reddit/snp500.csv")
snp_tickers = list(dataframe['Symbol'])

matching_tickers = 0
for ticker in unique_ticker_list:
    if ticker in snp_tickers:
        matching_tickers+=1
print(unique_ticker_list)
print("Number of stocks reccomended by reddit: ", len(unique_ticker_list))
print("Number of reccomended stocks in the S&P 500: ", matching_tickers)
