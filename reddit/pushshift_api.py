import requests
import json
import pandas as pd
import datetime
import re
from profanity_filter import ProfanityFilter
pf = ProfanityFilter()


def get_posts_for_time_period(sub, beginning, end=int(datetime.datetime.now(
).timestamp())):
    """
    Gets posts from the given subreddit for the given time period in json form.

    Args:
        sub: A string representing the subreddit to retrieve posts from.
        beginning: The unix timestamp of when the posts should begin.
        end: The unix timestamp of when the posts should end (defaults to
        current time).

    Returns:
    """
    print("Querying pushshift")
    url = "https://apiv2.pushshift.io/reddit/submission/search/" \
        "?subreddit={0}" \
        "&limit=500" \
        "&after={1}" \
        "&before={2}".format(sub, beginning, end)

    response = requests.get(url)
    resp_json = response.json()
    return resp_json['data']


beginning_timestamp = int(datetime.datetime(
    year=2018, month=1, day=1).timestamp())
end_timestamp = int(datetime.datetime(year=2019, month=1, day=1).timestamp())
data = get_posts_for_time_period(
    "wallstreetbets", beginning_timestamp, end_timestamp)
all_data = data

while len(data) >= 500:
    # go back for more data
    last_one = data[499]
    beginning_timestamp = last_one['created_utc'] + 1
    data = get_posts_for_time_period(
        sub="wallstreetbets", beginning=beginning_timestamp, end=end_timestamp)
    all_data.extend(data)
# print(all_data)

df = pd.DataFrame()  # initialize dataframe

# loop through each post retrieved from GET request
for post in all_data:
    # append relevant data to dataframe
    # print(json.dumps(post, indent=4))
    # print(str(datetime.datetime.fromtimestamp(post['data']['created'])))
    # if "2018" in str(datetime.datetime.fromtimestamp(post['data']['created'])):
    # print(datetime.datetime.fromtimestamp(post['data']['created']))
    # if 'selftext' in post and ("$" in post['selftext'] or "$" in post['title']): 'subreddit': [post['subreddit']],
    # make list of ticks, dates, good/bad, trigger word
    # good/bad word dictionary
    if 'selftext' in post and (re.search(r"^.*\$[A-Z]+", post['title']) or re.search(r"^.*\$[A-Z]+", post['selftext'])):
        df = pd.concat(
            [df, pd.DataFrame({'title': [pf.censor(post['title'])],
                               'selftext': [pf.censor(post['selftext'])],
                               'time': [datetime.datetime.fromtimestamp
                                        (post['created_utc'])],
                               'tickers': (re.findall(r"^.*\$[A-Z]+$", post['title'])).extend(re.findall(r"^.*\$[A-Z]+$", post['selftext']))})])
        # df = pd.concat(
        #     [df, pd.DataFrame({'tickers': (re.findall(r"\$[A-Z]+$", post['title'])).extend(re.findall(r"\$[A-Z]+", post['selftext']))})])
df.to_csv("reddit/reddit_posts.csv")
