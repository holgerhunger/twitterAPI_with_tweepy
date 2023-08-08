# Twitter API with tweepy
# Status: 08.08.2023
# Author: Holger Hunger
# Access to the free Twitter API v2 with Tweepy.
# There are only three API endpoints available in free access.
# They are called one after the other in this demo program.
# First the account and username are requested and displayed.
# Then a tweet is sent.
# After 20 seconds the tweet is deleted again.

import requests
import tweepy
import pandas as pd
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret,
                       return_type=requests.Response,
                       wait_on_rate_limit=True)

tweet_text = "Hello Twitter World! X"

print("Twitter API v2 test programm\n")

print("User data:")
# GET /2/users/me
tweets = client.get_me()
# Save data as dictionary
tweets_dict = tweets.json()
# Extract "data" value from dictionary
tweets_data = tweets_dict['data']
# Transform to pandas Dataframe
df = pd.json_normalize(tweets_data)
print(df, '\n')

# POST /2/tweets
print(f"Create Tweet: {tweet_text}")
tweets = client.create_tweet(text=tweet_text)
# Save data as dictionary
tweets_dict = tweets.json()
# Extract "data" value from dictionary
tweets_data = tweets_dict['data']
tweet_id = tweets_data["id"]
# Transform to pandas Dataframe
df = pd.json_normalize(tweets_data)
print(df, '\n')

# Wait 20s
sleep(20)

# DELETE /2/tweets/:id
print(f"Delete Tweet ID: {tweet_id}")
tweets = client.delete_tweet(id=tweet_id)
# Save data as dictionary
tweets_dict = tweets.json()
# Extract "data" value from dictionary
tweets_data = tweets_dict['data']
# Transform to pandas Dataframe
df = pd.json_normalize(tweets_data)
print(df)
