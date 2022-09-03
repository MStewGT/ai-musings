from decouple import config
import tweepy
#Get Twitter keys from .env file
bearer_token = config('BEARER_TOKEN')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')
consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
print(access_token, access_token_secret, consumer_key, consumer_secret)

#Function to tweet provided text
def tweet(input):
    #Authenticate using Twitter key
    client = tweepy.Client(bearer_token,consumer_key, consumer_secret, access_token, access_token_secret)
    #Post the input to Twitter
    response = client.create_tweet(text=input)
    return response