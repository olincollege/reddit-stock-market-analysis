import tweepy
import json


with open("twitter_credentials.json", "r") as file:
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
# Elon user id = 44196397

## removed because function client.search_all_tweets is only available to users
## with Academic Research access
# def get_tweets(username, key_phrases = ["", "", "", ""]):
#     # may error if search_string is longer than 1024 characters
#     search_string = (f"from:{username} {key_phrases[0]} OR {key_phrases[1]}
#         OR {key_phrases[2]} OR {key_phrases[3]}")
#     return client.search_all_tweets(search_string, max_results = 10,
#        end_time = "2022-03-17", start_time = "2022-03-22")


# only calls the most recent 100 tweets and only from the last week
def get_tweets(user_id):
    elon_tweets = client.get_users_tweets(user_id, max_results = 100, end_time = "2022-03-20T00:00:00.00Z")
    return elon_tweets

