import requests
import json
import pandas as pd
import datetime
import re
#from profanity_filter import ProfanityFilter
#pf = ProfanityFilter()


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
        "&limit=100" \
        "&after={1}" \
        "&before={2}".format(sub, beginning, end)

    response = requests.get(url)
    resp_json = response.json()
    return resp_json['data']


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

data = get_posts_for_time_period(
    "wallstreetbets", beginning_timestamp, end_timestamp)
all_data = data
print(end_timestamp)
print(beginning_timestamp)

while len(data) >= 100:
    # go back for more data
    last_one = data[len(data)-1]
    beginning_timestamp = last_one['created_utc'] + 1
    print(last_one['created_utc'])
    data = get_posts_for_time_period(
        sub="wallstreetbets", beginning=beginning_timestamp, end=end_timestamp)
    all_data.extend(data)
print(len(all_data))

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
    if 'selftext' in post and (findall_tickers(post['title']) or \
                               findall_tickers(post['selftext'])):

        censored_title = post['title']  #pf.censor()
        censored_selftext = post['selftext']
        time = datetime.datetime.fromtimestamp(post['created_utc'])
        ticker_list = findall_tickers(post['title'] + post['selftext'])
        #ticker_list = (findall_tickers(post['title'])).extend(
        #               findall_tickers(post['selftext']))

        df = pd.concat(
            [df, pd.DataFrame({'title': [censored_title],
                               'selftext': [censored_selftext],
                               'time': [time],
                               'tickers': [ticker_list]})])
        # df = pd.concat(
        #     [df, pd.DataFrame({'tickers': (re.findall(r"\$[A-Z]+$", post['title'])).extend(re.findall(r"\$[A-Z]+", post['selftext']))})])
df.to_csv("reddit/reddit_posts.csv")
