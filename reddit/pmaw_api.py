from matplotlib.pyplot import title
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
    Searches a string for stock tickers.

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

def pull_raw_data(subreddit, limit, beginning_day, end_day):
    """
    Docstring here
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
    """

    subreddit = "wallstreetbets"

    all_data = pull_raw_data(subreddit, limit, beginning_day, end_day)

    # Init new dataframe
    df = pd.DataFrame()
    index = -1
    
    for post in all_data.itertuples():
    
        title = str(post[1])
        selftext = str(post[2])
        created_utc = post[3]

        if (findall_tickers(title) or findall_tickers(selftext)) and \
            (not(findall_questions(title) or findall_questions(selftext))):
            
            index += 1
            #censored_title = post['title']  #pf.censor()
            #censored_selftext = post['selftext']
            time = datetime.datetime.fromtimestamp(created_utc)
            ticker_list = findall_tickers(title + " " + selftext)

            df = pd.concat(
                [df, pd.DataFrame({'index' : [index],
                                'title': [title],
                                'selftext': [selftext],
                                'time': [time],
                                'tickers': [ticker_list]})])
    df.to_csv("reddit/reddit_subs_filtered.csv")


get_filtered_reddit_data(100000, "2018-01-01", "2019-01-01")