from decouple import config
import tweepy

#Function to tweet provided text
def tweet(text):
    #get twitter keys from .env file
    bearer_token = config('TWITTER_TOKEN')
    #authenticate using twitter keys
    auth = tweepy.OAuth2BearerHandler('bearer_token')
    #create an API object
    api = tweepy.API(auth)
    #update status
    api.update_status(text)