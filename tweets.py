import tweepy
import os
import credentials

"""
deals with the tweepy API i.e. handling tweets and updating description
TODO: deal with mentions
"""
CONSUMER_KEY = credentials.API_key
CONSUMER_KEY_SECRET = credentials.API_secret_key
ACCESS_TOKEN = credentials.access_token
ACCESS_SECRET = credentials.access_token_secret

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

def post_tweet(tweet):
    status = api.update_status(status=tweet)


def update_description(about):
    api.update_profile(description=about)