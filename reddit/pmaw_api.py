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



beginning_timestamp = int(datetime.datetime(
    year=2018, month=1, day=1).timestamp())
end_timestamp = int(datetime.datetime(
    year=2019, month=1, day=1).timestamp())

subreddit="wallstreetbets"
limit=300

submissions = api.search_submissions(subreddit=subreddit, limit=limit,
                        before=end_timestamp, after=beginning_timestamp)

subs_df = pd.DataFrame(submissions)
#all_data = subs_json['data']

print(len(subs_df))

subs_df = subs_df[['title', 'selftext', 'created_utc']]
print(subs_df.columns)
print(subs_df.head(5))

for i, post in subs_df.iterrows():


if 'selftext' in post and (findall_tickers(post['title']) or \
                            findall_tickers(post['selftext'])):

    censored_title = post['title']  #pf.censor()
    censored_selftext = post['selftext']
    time = datetime.datetime.fromtimestamp(post['created_utc'])
    ticker_list = [findall_tickers(post['title'] + post['selftext'])]
        #ticker_list = (findall_tickers(post['title'])).extend(
        #               findall_tickers(post['selftext']))

    df = pd.concat(
        [df, pd.DataFrame({'title': [censored_title],
                           'selftext': [censored_selftext],
                           'time': [time],
                           'tickers': ticker_list})])