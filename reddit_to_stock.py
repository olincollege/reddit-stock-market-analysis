import csv
import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("newapi.csv")  # 'reddit/reddit_posts.csv')  #
title = df['title']
selftext = df['selftext']
time = df['time']
tickers = df['tickers']
list_selftext = selftext.tolist()
list_title = title.tolist()


def findall_markerwords(string):
    """
    Searches a string for stock tickers.

    Args:
        string: A string to be searched.

    Returns:
        A list of all the stock tickers in the string.
    """
    return re.findall(r"\$([A-Z]+)", string)


i = 0
for word in list_title:
    if re.findall(r'[Ll]ong', word):
print(i)
