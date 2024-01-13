import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_twitter_etl():
    # To Get KEYS Please Visit "https://developer.twitter.com/en/docs/twitter-api"
    access_key = "YOUR_ACCESS_KEY"
    access_secret = "YOUR_ACCESS_SECRET_KEY"
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET_KEY"

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # # # Creating an API object
    api = tweepy.API(auth)
    tweets = api.user_timeline(
        screen_name="@elonmusk",
        count=200,  # 200 is the maximum tweets allowed count
        include_rts=False,  # To Extract ReTweets value=True Not to Extract Retweets value=False
        tweet_mode="extended",  # Necessary to keep full_text, otherwise only the first 140 words are extracted
    )

    list = [] #Array to store the Fetched json data 
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {
            "user": tweet.user.screen_name,
            "text": text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at,
        }

        list.append(refined_tweet)

    df = pd.DataFrame(list)
    df.to_csv("refined_tweets.csv")
