import tweepy
import json


with open("twitter/twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = creds['ACCESS_TOKEN']
ACCESS_SECRET = creds['ACCESS_SECRET']
CONSUMER_KEY = creds['API_TOKEN']
CONSUMER_SECRET = creds['API_SECRET']
BEARER_TOKEN = creds['BEARER_TOKEN']




client = tweepy.Client(BEARER_TOKEN)

# tweets from a specific user
user = client.get_user(username = 'elonmusk')



elon_tweets = client.get_users_tweets(44196397)
for tweet in elon_tweets:
    print(tweet)
