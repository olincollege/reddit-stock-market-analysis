import csv
import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("newapi.csv")  # 'reddit/reddit_posts.csv')  #
title = df['title']
selftext = df['selftext']
time = df['time']
all_tickers = df['tickers']
# read pmaw api function
# list_selftext = selftext.tolist()
# list_title = title.tolist()


def remove_dupes(ticker_list):
    """
    removes empty strings and repeats
    """
    res = []
    [res.append(x) for x in ticker_list if x not in res]
    if '' in res:
        res.remove('')
    return res


existing_tickers = ['SPY']
for post in df.itertuples():
    index = post[2]
    title = str(post[3])
    selftext = str(post[4])
    time = str(post[5])[0:10]
    tickers = str(post[6][2:-3]).split("', '")
    if not re.findall(r'[Ll]ong', selftext + ' ' + title):
        tickers = remove_dupes(tickers)
        df.iat[index, 5] = [tickers]
        for single_ticker in tickers:
            if single_ticker not in existing_tickers:
                existing_tickers.append(single_ticker)
            else:
                tickers.remove(single_ticker)
        if not tickers:
            df.drop(labels=[index], axis=0, inplace=True)


print(len(df))

df.to_csv("see_if_it_works.csv")
# look for long, filter repeat ticker symbols, maintain date order
