#Write a function that creates a tweet from variable 'text' via the Twitter API.
import tweepy

def tweet(text):
    #Authentication details for Twitter API
    consumer_key = 'consumer_key'
    consumer_secret = 'consumer_secret'
    access_token = 'access_token'
    access_token_secret = 'access_token_secret'

    #Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #Tweet the text
    api.update_status(text)